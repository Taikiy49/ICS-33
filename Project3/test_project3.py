import unittest
import io
import contextlib
import read
import print_module


class TestRunProgram(unittest.TestCase):
    def test_let_and_print_work(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            print_test_file('../Project3/project3_test_files/test1_input').execute_instructions()
        with open('../Project3/project3_test_files/test1_output', 'r') as file:
            self.assertEqual(output.getvalue(), file.read())

    def test_add_sub_mult_div(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            print_test_file('../Project3/project3_test_files/test2_input').execute_instructions()
        with open('../Project3/project3_test_files/test2_output', 'r') as file:
            self.assertEqual(output.getvalue(), file.read())

    def test_goto_and_gosub_and_return_work(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            print_test_file('../Project3/project3_test_files/test3_input').execute_instructions()
        with open('../Project3/project3_test_files/test3_output', 'r') as file:
            self.assertEqual(output.getvalue(), file.read())

    def test_if_and_labels_and_string_operations_work(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            print_test_file('../Project3/project3_test_files/test4_input').execute_instructions()
        with open('../Project3/project3_test_files/test4_output', 'r') as file:
            self.assertEqual(output.getvalue(), file.read())

    def test_when_variable_assigned_to_variable_with_no_value_through_let(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            print_test_file('../Project3/project3_test_files/test5_input').execute_instructions()
        with open('../Project3/project3_test_files/test5_output', 'r') as file:
            self.assertEqual(output.getvalue(), file.read())

    def test_goto_label_does_not_exist(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            print_test_file('../Project3/project3_test_files/test6_input').execute_instructions()
        self.assertEqual(output.getvalue(), 'Label does not exist.\n')

    def test_go_sub_label_does_not_exist(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            print_test_file('../Project3/project3_test_files/test7_input').execute_instructions()
        self.assertEqual(output.getvalue(), 'Label does not exist.\n')

    def test_goto_not_string_or_integer(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            print_test_file('../Project3/project3_test_files/test8_input').execute_instructions()
        self.assertEqual(output.getvalue(), 'Target must be an integer or string.\n')

    def test_gosub_not_string_or_integer(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            print_test_file('../Project3/project3_test_files/test9_input').execute_instructions()
        self.assertEqual(output.getvalue(), 'Target must be an integer or string.\n')

    def test_if_all_comparison_operators_work(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            print_test_file('../Project3/project3_test_files/test10_input').execute_instructions()
        with open('../Project3/project3_test_files/test10_output', 'r') as file:
            self.assertEqual(output.getvalue(), file.read())

    def test_if_no_gosub_to_return_to_prints_error_message(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            print_test_file('../Project3/project3_test_files/test11_input').execute_instructions()
        self.assertEqual(output.getvalue(), 'RETURN does not have a GOSUB to return to.\n')


def print_test_file(input_file):
    interpreter = read.InputProcessor('')
    with open(input_file, 'r') as file:
        input_list = [line.strip() for line in file.readlines()]
    for inp in input_list:
        read.handle_user_input(interpreter, inp)
    info = interpreter.information()
    print_object = print_module.PrintModule(info[0], info[1], info[2], info[3])
    return print_object


if __name__ == '__main__':
    unittest.main()
