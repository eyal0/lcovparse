import sys

version = VERSION = __version__ = "0.0.4"


def lcovparse(combined):
    # clean and strip lines
    assert 'end_of_record' in combined, 'lcov file is missing "end_of_record" line(s)'
    files = filter(lambda f: f != '', combined.strip().split("end_of_record"))
    reports = map(_part, files)
    return reports


def _part(chunk):
    report = {
        "test": None,
        "file": None,
        "stats": {},
        "lines": [],
        "functions": [],
        "branches": []
    }
    map(lambda l: _line(l, report), chunk.split('\n'))
    return report


def _line(l, report):
    """
    http://ltp.sourceforge.net/test/coverage/lcov.readme.php#10
    """
    if l == '':
        return None
    method, content = tuple(l.strip().split(':', 1))
    content = content.strip()
    if method == 'TN':
        # test title
        report["test"] = content

    elif method == 'SF':
        # file name
        report["file"] = content

    elif method == 'LF':
        # lines found
        report['stats']['lines'] = int(content)

    elif method == 'LH':
        # line hit
        report['stats']['hit'] = int(content)

    elif method == 'DA':
        if 'null' not in content:
            line, hit = map(int, content.split(',', 1))
            report['lines'].append(dict(line=line, hit=hit))

    # ---------
    # Functions
    # ---------
    elif method == 'FNF':
        # functions found
        report["stats"]["fn_found"] = int(content)

    elif method == 'FNH':
        report["stats"]["fn_hit"] = int(content)

    elif method == 'FN':
        line, name = content.split(',', 1)
        report['functions'].append(dict(line=int(line), name=name))

    elif method == 'FNDA':
        # function names
        # FNDA:75,get_user
        hit, name = content.split(',', 1)
        if hit not in (None, '-', ''):
            for fn in report['functions']:
                if fn['name'] == name:
                    fn['hit'] = int(hit)

    # --------
    # Branches
    # --------
    elif method == 'BRF':
        report['stats']['br_found'] = int(content)

    elif method == 'BRH':
        report['stats']['br_hit'] = int(content)

    elif method == 'BRDA':
        # branch names
        # BRDA:10,1,0,1
        line, block, branch, taken = content.split(',', 3)
        report['branches'].append(dict(
            line=int(line),
            block=int(block),
            branch=int(branch),
            taken=0 if taken == '-' else int(taken)))

    else:
        sys.stdout.write("Unknown method name %s" % method)
