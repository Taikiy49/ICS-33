import grin
import operations
import go_methods


class PrintModule:

    def __init__(self, order: list, store_dict: dict, label: dict, go_sub_index: list):
        """Initializes the PrintModule instance."""
        self._i = 0
        self._order = order
        self._store_dict = store_dict
        self._label = label
        self._go_sub_index = go_sub_index

    def execute_instructions(self) -> None:
        """Executes all instructions in the order list."""
        while self._i < len(self._order):
            if self._order[self._i][1] == 'let':
                if self._order[self._i][2].kind() == grin.GrinTokenKind.IDENTIFIER:
                    if self._order[self._i][2].value() in self._store_dict.keys():
                        self._store_dict[self._order[self._i][0]] = self._store_dict[self._order[self._i][2].value()]
                    else:
                        self._store_dict[self._order[self._i][0]] = 0
                else:
                    self._store_dict[self._order[self._i][0]] = self._order[self._i][2].value()
                self._i += 1

            elif self._order[self._i][1] == 'in_num':
                n = input()
                try:
                    if float(n):
                        if n.isdigit():
                            self._store_dict[self._order[self._i][0]] = int(n)
                        else:
                            self._store_dict[self._order[self._i][0]] = float(n)
                        self._i += 1

                except ValueError:
                    print("Input must be an integer or float.")

            elif self._order[self._i][1] == 'in_str':
                n = input()
                self._store_dict[self._order[self._i][0]] = n
                self._i += 1

            elif self._order[self._i][1] == 'add':
                info = operations.Operator('add', self._store_dict, self._order, self._i).return_info()
                self._store_dict, self._order, self._i = info[0], info[1], info[2]

            elif self._order[self._i][1] == 'sub':
                info = operations.Operator('sub', self._store_dict, self._order, self._i).return_info()
                self._store_dict, self._order, self._i = info[0], info[1], info[2]

            elif self._order[self._i][1] == 'mult':
                info = operations.Operator('mult', self._store_dict, self._order, self._i).return_info()
                self._store_dict, self._order, self._i = info[0], info[1], info[2]

            elif self._order[self._i][1] == 'div':
                info = operations.Operator('div', self._store_dict, self._order, self._i).return_info()
                self._store_dict, self._order, self._i = info[0], info[1], info[2]

            elif self._order[self._i][1] == 'print':
                if self._order[self._i][0] == 'IGNORE_PRINT':
                    print(self._order[self._i][2])
                else:
                    print(self._store_dict[self._order[self._i][0]])
                self._i += 1

            elif self._order[self._i][1] == 'goto' or self._order[self._i][1] == 'gosub':
                info = go_methods.GotoAndGosub(self._i, self._order, self._store_dict, self._label, self._go_sub_index).execute()
                self._i, self._order, self._store_dict, self._label, self._go_sub_index = info

            elif self._order[self._i][1] == 'goto_if' or self._order[self._i][1] == 'gosub_if':
                info = go_methods.GotoIfAndGosubIf(self._i, self._order, self._store_dict, self._label, self._go_sub_index).execute()
                self._i, self._order, self._store_dict, self._label, self._go_sub_index = info

            elif self._order[self._i][1] == 'return':
                if self._go_sub_index:
                    self._i = self._go_sub_index[-1] + 1
                    self._go_sub_index.pop(-1)
                else:
                    print('RETURN does not have a GOSUB to return to.')
                    self._i = len(self._order)

            elif self._order[self._i][1] == 'end':
                self._i = len(self._order)