import unittest
import io
import contextlib
import project1
import prepare
import create_lists


class Project1Test(unittest.TestCase):

    def test_file_raises_no_error(self):
        file = '../samples/sample_input.txt'
        with contextlib.redirect_stdout(io.StringIO()) as output:
            project1.print_outcome(prepare.Device(create_lists.lst(file)).prepare_outcome())
        string = output.getvalue()
        self.assertEqual(string[0], '@')

    def test_file_raises_error(self):
        file = '../samples/sample_input.tnt' # replaced txt with tnt
        with self.assertRaises(FileNotFoundError) as context:
            with contextlib.redirect_stdout(io.StringIO()):
                project1.print_outcome(prepare.Device(create_lists.lst(file)).prepare_outcome())
        self.assertEqual(type(context.exception), FileNotFoundError)

    def test_four_devices_four_propagates(self):
        file = '../samples/sample_input.txt'
        with contextlib.redirect_stdout(io.StringIO()) as output:
            project1.print_outcome(prepare.Device(create_lists.lst(file)).prepare_outcome())
        string = output.getvalue()
        with open('../samples/sample_output.txt', 'r') as file:
            self.assertEqual(string, file.read())

    def test_two_devices_two_propagates(self):
        file = '../samples/sample_input2.txt'
        with contextlib.redirect_stdout(io.StringIO()) as output:
            project1.print_outcome(prepare.Device(create_lists.lst(file)).prepare_outcome())
        string = output.getvalue()
        with open('../samples/sample_output2.txt', 'r') as file:
            self.assertEqual(string, file.read())

    def test_no_cancellation_only_alert(self):
        file = '../samples/sample_input3.txt'
        with contextlib.redirect_stdout(io.StringIO()) as output:
            project1.print_outcome(prepare.Device(create_lists.lst(file)).prepare_outcome())

        string = output.getvalue()
        with open('../samples/sample_output3.txt', 'r') as file:
            self.assertEqual(string, file.read())

    def test_same_one_alert_sends_to_multiple_devices(self):
        file = '../samples/sample_input4.txt'
        with contextlib.redirect_stdout(io.StringIO()) as output:
            project1.print_outcome(prepare.Device(create_lists.lst(file)).prepare_outcome())
        string = output.getvalue()
        with open('../samples/sample_output4.txt', 'r') as file:
            self.assertEqual(string, file.read())
