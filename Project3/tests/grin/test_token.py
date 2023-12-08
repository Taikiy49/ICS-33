# test_lexing.py
#
# ICS 33 Fall 2023
# Project 3: Why Not Smile?
#
# Unit tests for the provided grin.lexing module.
#
# WHAT YOU NEED TO DO: Nothing, unless you make changes to grin.lexing
# (which shouldn't be necessary).

from grin.token import GrinTokenKind, GrinToken
import unittest



class GrinTokenKindTest(unittest.TestCase):
    def test_indexes_are_unique(self):
        indexes = set(kind.index() for kind in GrinTokenKind.__members__.values())
        self.assertEqual(len(indexes), len(GrinTokenKind.__members__))
