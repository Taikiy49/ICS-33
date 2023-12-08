import random


class VariableNotDefinedError(Exception):
    """Custom exception for variable that is not defined."""
    pass


class VariableNameError(Exception):
    """Custom exception for variable name that is invalid."""
    pass


class Rule:
    def __init__(self):
        """Initializes the Rule object."""
        self._probability_dict = {}

    def check_word(self, word: str) -> bool:
        """Checks if word contains anything other than a letter or digit. If so, returns False."""
        for i in word[1:-1]:
            if not i.isalpha() and not i.isdigit():
                return False
        return True

    def create_probability_dict(self, lst: list) -> dict:
        """Creates a probability dictionary from the given list."""
        total_value = 0
        for line in lst:
            num = line.split()[0]
            split_line = line.split()
            if len(split_line) > 1:
                word_line = line[line.index(' ') + 1:]
                split_word_line = word_line.split()
                for word in split_word_line:
                    if '[' in word and ']' not in word:
                        raise VariableNameError
                    if '[' in word and ']' in word:
                        if not self.check_word(word):
                            raise VariableNameError
            else:
                word_line = 'EMPTY'
            total_value += int(num)
            self._probability_dict[word_line] = num

        for key, value in self._probability_dict.items():
            self._probability_dict[key] = int(self._probability_dict[key]) / total_value
        return self._probability_dict


class Option:
    def __init__(self, probability_dict):
        """Initializes the Option object."""
        self._probability_dict = probability_dict

    def execute_random(self) -> str:
        """Executes a random choice based on the probability dictionary."""
        choices = []
        prob = []
        for key, value in self._probability_dict.items():
            choices.append(key)
            prob.append(value)
        return random.choices(choices, prob)[0]


class VariableSymbol:
    def __init__(self, command_dict):
        """Initializes the VariableSymbol object."""
        self._command_dict = command_dict

    def create_variable_symbol_dict(self) -> list:
        """Creates a list of variable symbols from the command dictionary."""
        variable_list = []
        for value in self._command_dict.values():
            for line in value:
                for word in line.split():
                    if '[' in word and ']' in word:
                        variable_list.append(word)
        return variable_list


class TerminalSymbol:
    def __init__(self, command_dict):
        """Initializes the TerminalSymbol object."""
        self._command_dict = command_dict

    def create_terminal_symbol_dict(self) -> list:
        """Creates a list of terminal symbols from the command dictionary."""
        terminal_list = []
        for value in self._command_dict.values():
            for line in value:
                for word in line.split():
                    if '[' not in word and ']' not in word:
                        terminal_list.append(word)
        return terminal_list
