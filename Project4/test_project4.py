import unittest
import io
import contextlib
from project4 import ParseFile
from grammar import Grammar
from grammar_generator import *


class Project4Test(unittest.TestCase):

    def test_if_variable_works(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            BehindTheScenes('../Project4/test_files/test_file1.txt', 1, 'HowIsBoo').return_value()
        self.assertEqual(output.getvalue(), 'Boo is excited today!\n')

    def test_if_variable_inside_variable_works(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            BehindTheScenes('../Project4/test_files/test_file1.txt', 1, 'HowIsBoo2').return_value()
        self.assertEqual(output.getvalue(), 'Boo is feeling very sick today :(\n')

    def test_if_line_prints_multiple_times(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            BehindTheScenes('../Project4/test_files/test_file1.txt', 3, 'HowIsBoo2').return_value()
        self.assertEqual(output.getvalue(), 'Boo is feeling very sick today :(\nBoo is feeling very sick today '
                                            ':(\nBoo is feeling very sick today :(\n')

    def test_if_triple_nested_variable_works(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            BehindTheScenes('../Project4/test_files/test_file1.txt', 1, 'HowIsBoo3').return_value()
        self.assertEqual(output.getvalue(), 'This should print!\n')

    def test_raises_error_when_variable_not_defined(self):
        try:
            BehindTheScenes('../Project4/test_files/test_file1.txt', 1, 'HowIsBoo4').return_value()
        except Exception as e:
            self.assertEqual(type(e), VariableNotDefinedError)

    def test_raises_error_when_option_does_not_have_a_weight(self):
        try:
            BehindTheScenes('../Project4/test_files/test_file1.txt', 1, 'HowIsBoo5').return_value()
        except Exception as e:
            self.assertEqual(type(e), ValueError)

    def test_raises_error_when_variable_name_invalid(self):
        try:
            BehindTheScenes('../Project4/test_files/test_file1.txt', 1, 'HowIsBoo6').return_value()
        except Exception as e:
            self.assertEqual(type(e), VariableNameError)

    def test_empty_string_works(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            BehindTheScenes('../Project4/test_files/test_file1.txt', 1, 'HowIsBoo7').return_value()
        self.assertEqual(output.getvalue(), 'Hello  World!\n')

    def test_raises_error_due_to_invalid_characters_in_variable_name(self):
        try:
            BehindTheScenes('../Project4/test_files/test_file1.txt', 1, 'HowIsBoo8').return_value()
        except Exception as e:
            self.assertEqual(type(e), VariableNameError)

    def test_start_variable_name_does_not_exist(self):
        try:
            BehindTheScenes('../Project4/test_files/test_file1.txt', 1, 'HowIsBooThatDoesNotExist').return_value()
        except Exception as e:
            self.assertEqual(type(e), VariableNotDefinedError)

    def test_invalid_start_variable_name(self):
        try:
            BehindTheScenes('../Project4/test_files/test_file1.txt', 1, '-HowIsBooInvalidStartVariable-').return_value()
        except Exception as e:
            self.assertEqual(type(e), VariableNotDefinedError)


class BehindTheScenes:

    def __init__(self, file, count, variable):
        self._file = file
        self._count = count
        self._variable = variable

    def return_value(self):
        readfile_file_object = ParseFile(self._file, self._count, self._variable)
        return Grammar(*readfile_file_object.return_values()).run()

