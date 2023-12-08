import grammar_generator
from grammar_generator import *


class Grammar:
    def __init__(self, command_dict, generate_count, start_variable_name):
        """Initializes the Grammar object."""
        self._command_dict = command_dict
        self._generate_count = generate_count
        self._start_variable_name = start_variable_name
        self._probability_dict = {}
        self._random_choice = ''
        self._run_once = 0
        self._temporary_base_line = ''
        self._new_list = []

    def initial_line(self) -> None:
        """Set up the initial line based on the starting variable."""
        if self._start_variable_name in self._command_dict.keys():
            self._probability_dict = Rule().create_probability_dict(self._command_dict[self._start_variable_name])
            self._random_choice = Option(self._probability_dict).execute_random()
        else:
            raise VariableNotDefinedError(f'Variable {self._start_variable_name} is not defined.')

    def replace_variable_symbols(self) -> None:
        """Executes the program by replacing variable symbols with their random choices."""
        grammar_generator.VariableSymbol(self._command_dict)
        grammar_generator.TerminalSymbol(self._command_dict)

        if self._run_once == 0:
            self.initial_line()
            self._temporary_base_line = self._random_choice
            self._run_once += 1

        for word in self._temporary_base_line.split():
            if '[' in word and ']' in word:
                if word[1:-1] in self._command_dict:
                    self._probability_dict = Rule().create_probability_dict(self._command_dict[word[1:-1]])
                    self._random_choice = Option(self._probability_dict).execute_random()
                    self.replace_words(self._temporary_base_line, word, self._random_choice)
                    self._temporary_base_line = convert_list(self._new_list)
                else:
                    raise VariableNotDefinedError(f'Variable {word[1:-1]} is not defined.')

    def replace_words(self, string: str, old_word: str, new_word: str) -> None:
        """Replaces words in the string with a new word."""
        self._new_list = string.split()
        self._new_list[self._new_list.index(old_word)] = new_word

    def run(self) -> None:
        """Runs the grammar generation process."""
        VariableSymbol(self._command_dict).create_variable_symbol_dict()
        TerminalSymbol(self._command_dict).create_terminal_symbol_dict()

        for _ in range(self._generate_count):
            self._run_once = 0
            self.replace_variable_symbols()
            run = True
            while run:
                self.replace_variable_symbols()
                if check_done(self._temporary_base_line):
                    run = False
            while 'EMPTY' in self._temporary_base_line:
                self._temporary_base_line = self._temporary_base_line.replace('EMPTY', '')
            print(self._temporary_base_line)


def convert_list(lst: list) -> str:
    """Converts a list of words into a string."""
    string = ''
    for i in range(len(lst)):
        if i == len(lst) - 1:
            string += f'{lst[i]}'
        else:
            string += f'{lst[i]} '
    return string


def check_done(string: str) -> bool:
    """Checks if all variable symbols in the string have been replaced."""
    boolean = True
    lst = string.split()
    for word in lst:
        if '[' in word and ']' in word:
            return False
    return boolean
