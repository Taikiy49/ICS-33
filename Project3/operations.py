import grin


class Operator:
    def __init__(self, operation: str, store_dict: dict, order: list, i: int):
        """Initializes the Operator instance."""
        self._operation = operation
        self._store_dict = store_dict
        self._order = order
        self._i = i

    def execute_operation(self) -> None:
        """Execute the specified operation and update the store_dict and index accordingly."""
        value1_var = self._order[self._i][0]
        value2_grin = self._order[self._i][2]

        if value1_var in self._store_dict.keys():
            value1 = self._store_dict[value1_var]
        else:
            self._store_dict[value1_var] = 0
            value1 = 0

        if value2_grin.kind() == grin.GrinTokenKind.IDENTIFIER:
            if value2_grin.value() in self._store_dict.keys():
                value2 = self._store_dict[value2_grin.value()]
            else:
                self._store_dict[value2_grin.value()] = 0
                value2 = 0
        else:
            value2 = value2_grin.value()

        if self._operation == 'add':
            if (type(value1) is str and type(value2) is not str) or (type(value1) is not str and type(value2) is str):
                print('Can only add strings with strings.')
                self._i = len(self._order)
            else:
                self._store_dict[value1_var] = value1 + value2
                self._i += 1

        elif self._operation == 'sub':
            if type(value1) is str or type(value2) is str:
                print('Cannot subtract with strings.')
                self._i = len(self._order)
            else:
                self._store_dict[value1_var] = value1 - value2
                self._i += 1

        elif self._operation == 'mult':
            if ((type(value1) is str and type(value2) is float) or (type(value1) is float and type(value2) is str)
                    or (type(value1) is str and type(value2) is str)):
                print('Cannot multiply string w/ float, float w/ string, or string w/ string.')
                self._i = len(self._order)
            else:
                self._store_dict[value1_var] = value1 * value2
                self._i += 1
        elif self._operation == 'div':
            if type(value1) is int and type(value2) is int:
                self._store_dict[value1_var] = value1 // value2
                self._i += 1
            else:
                if type(value1) is str or type(value2) is str:
                    print('Cannot divide with strings.')
                    self._i = len(self._order)
                else:
                    self._store_dict[value1_var] = value1 / value2
                    self._i += 1

    def return_info(self) -> list:
        """Execute the operation and return updated store_dict, order, and index."""
        self.execute_operation()
        return [self._store_dict, self._order, self._i]
