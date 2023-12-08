import grin

class ControlFlowInstruction:
    """Base class for control flow instructions."""
    def __init__(self, i: int, order: list, store_dict: dict, label: dict, go_sub_index: list):
        """Initialize a ControlFlowInstruction instance."""
        self._i = i
        self._order = order
        self._store_dict = store_dict
        self._label = label
        self._go_sub_index = go_sub_index

    def process_jump(self, jump: int):
        """Process the jump instruction."""
        if jump == 0:
            print('Target cannot be 0.')
            self._i = len(self._order)
        elif self._i < 0 or self._i > len(self._order):
            print('Target line does not exist.')
            self._i = len(self._order)

class GotoAndGosub(ControlFlowInstruction):
    """Class for Goto and Gosub instructions."""
    def execute(self):
        """Execute the Goto or Gosub instruction."""
        if self._order[self._i][1] == 'gosub':
            self._go_sub_index.append(self._i)

        if self._order[self._i][2] != 'ERROR':
            if self._order[self._i][2].kind() == grin.GrinTokenKind.LITERAL_INTEGER:
                jump_value = self._order[self._i][2].value()
                self._i += jump_value
                self.process_jump(jump_value)

            elif self._order[self._i][2].kind() == grin.GrinTokenKind.LITERAL_STRING:
                if self._order[self._i][2].value() in self._label.keys():
                    self._i = self._label[self._order[self._i][2].value()]
                else:
                    print('Label does not exist.')
                    self._i = len(self._order)
        else:
            print("Target must be an integer or string.")
            self._i = len(self._order)

        return [self._i, self._order, self._store_dict, self._label, self._go_sub_index]

class GotoIfAndGosubIf(ControlFlowInstruction):
    """Class for GotoIf and GosubIf instructions."""
    def execute(self):
        """Execute the GotoIf or GosubIf instruction."""
        if self._order[self._i][1] == 'gosub_if':
            self._go_sub_index.append(self._i)

        compare1 = self._order[self._i][3]
        compare2 = self._order[self._i][5]
        compare_operator = self._order[self._i][4]
        if self.compare_operator(compare1, compare2, compare_operator):
            if self._order[self._i][2].kind() == grin.GrinTokenKind.LITERAL_INTEGER:
                jump_value = self._order[self._i][2].value()
                self._i += jump_value
                self.process_jump(jump_value)

            elif self._order[self._i][2].kind() == grin.GrinTokenKind.LITERAL_STRING:
                if self._order[self._i][2].value() in self._label.keys():
                    self._i = self._label[self._order[self._i][2].value()]
                else:
                    print('Label does not exist.')
                    self._i = len(self._order)
        else:
            self._i += 1

        return [self._i, self._order, self._store_dict, self._label, self._go_sub_index]

    def compare_operator(self, c1: grin.GrinToken, c2: grin.GrinToken, co: str) -> bool:
        """Compare two values based on the given operator."""
        compare_list = [c1, c2]
        new_compare_list = []
        for c in compare_list:
            if c.kind() == grin.GrinTokenKind.IDENTIFIER and c.value() in self._store_dict.keys():
                new_compare_list.append(self._store_dict[c.value()])
            elif c.kind() == grin.GrinTokenKind.IDENTIFIER:
                new_compare_list.append(0)
            elif c.kind() == grin.GrinTokenKind.LITERAL_INTEGER:
                new_compare_list.append(c.value())
            else:
                print('ERROR: Not comparable.')
                self._i = len(self._order)

        c1 = int(new_compare_list[0])
        c2 = int(new_compare_list[1])

        if co == '<':
            if c1 < c2:
                return True
        elif co == '<=':
            if c1 <= c2:
                return True
        elif co == '>':
            if c1 > c2:
                return True
        elif co == '>=':
            if c1 >= c2:
                return True
        elif co == '=':
            if c1 == c2:
                return True
        elif co == '<>':
            if c1 != c2:
                return True
