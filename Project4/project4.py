from grammar import Grammar
from grammar import VariableNotDefinedError
from grammar import VariableNameError


class BracketExistsError(Exception):
    """Custom exception for bracket existence."""
    pass


class ParseFile:

    def __init__(self, file: str, generate_count: int, start_variable_name: str) -> None:
        """Initializes the ParseFile object."""
        self._command_dict = {}
        self._read_list = []
        self._file = file
        self._generate_count = generate_count
        self._start_variable_name = start_variable_name

    def read_file(self) -> None:
        """Read lines from the input file and stores them in a list"""
        with open(self._file, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line != '':
                    self._read_list.append(stripped_line)

    def create_dict(self) -> None:
        """Creates a dictionary from the list that contains all the lines from the file."""
        self.read_file()
        for i in range(len(self._read_list)):
            if self._read_list[i] == '{':
                self._command_dict[self._read_list[i + 1]] = []
                m = i + 2
                while self._read_list[m] != '}':
                    self._command_dict[self._read_list[i + 1]].append(self._read_list[m])
                    m += 1

    def return_values(self) -> list:
        """Returns a list of values from the ParseFile object."""
        self.create_dict()
        return [self._command_dict, self._generate_count, self._start_variable_name]


def check_valid_start_variable(start_variable: str) -> bool:
    """Checks if the start variable name is valid."""
    for i in start_variable:
        if not i.isalpha() and not i.isdigit():
            return False
    return True


def main() -> None:
    """Main function to execute the program."""
    try:
        file = str(input())
        check_file = open(file)
        check_file.close()
        generate_count = int(input())
        if generate_count < 1:
            raise ValueError
        start_variable_name = str(input())
        if '[' in start_variable_name and ']' in start_variable_name:
            raise BracketExistsError
        elif len(start_variable_name.split()) > 1:
            raise VariableNameError
        elif not check_valid_start_variable(start_variable_name):
            raise VariableNameError

        read_file_object = ParseFile(file, generate_count, start_variable_name)
        command_dict = read_file_object.return_values()
        Grammar(*command_dict).run()

    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Number of random sentences to be generated and weights for all options must be positive integers.")
    except VariableNotDefinedError as e:
        print(e)
    except BracketExistsError:
        print("Brackets are not allowed for start variable inputs.")
    except VariableNameError:
        print("Name of variable must ONLY include letters and integers with no white spaces.")


if __name__ == '__main__':
    main()
