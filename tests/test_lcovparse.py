#!/usr/bin/env python2
"""Test coverage.py"""

from __future__ import division
import os
import unittest
import json
import difflib

from .context import lcovparse
from lcovparse import lcovparse

class LcovparseTests(unittest.TestCase):
    """Test lcovparse."""
    def compare_lines(self, actual_lines, expected_lines, filename):
        """Helper for comparing lines.

        Outputs a unified diff.
        """
        self.assertEqual(actual_lines,
                         expected_lines,
                         "\n\n" + "\n".join(
                             difflib.unified_diff(
                                 expected_lines,
                                 actual_lines,
                                 os.path.relpath(filename),
                                 os.path.relpath(filename),
                                 lineterm="")))

    def test_from_lcov(self):
        """Test Coverage.from_lcov(file)."""
        path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(path, "branch-lcov.info")) as lcov_file:
          result = lcovparse(lcov_file.read())
        expected_file = os.path.join(path, "branch-lcov.info.json")
        with open(expected_file) as expected:
            expected_lines = [x.strip() for x in expected.read().splitlines()] # No newlines
            actual_lines = [x.strip() for x in json.dumps(result, indent=2, sort_keys=True).splitlines()]
            self.compare_lines(actual_lines, expected_lines, expected_file)

if __name__ == '__main__':
    unittest.main()
