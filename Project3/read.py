import grin
import print_module


class InputProcessor:
    def __init__(self, input_line: str):
        """Initializes the InputProcessor instance."""
        self._input = input_line
        self._order = []
        self._store_dict = {}
        self._label = {}
        self._go_sub_index = []

    def set_input(self, input_line: str) -> None:
        """Set the input line for processing."""
        self._input = input_line

    def read_input(self) -> None:
        """Read and process the input line."""
        parsed_input = grin.parse([self._input])
        for line in parsed_input:
            if line[0].kind() == grin.GrinTokenKind.LET:
                self.execute_let(line)
            elif line[0].kind() == grin.GrinTokenKind.PRINT:
                self.execute_print(line)
            elif line[0].kind() == grin.GrinTokenKind.INNUM:
                self.execute_in_num(line)
            elif line[0].kind() == grin.GrinTokenKind.INSTR:
                self.execute_in_str(line)
            elif (line[0].kind() == grin.GrinTokenKind.ADD or line[0].kind() == grin.GrinTokenKind.SUB or
                  line[0].kind() == grin.GrinTokenKind.MULT or line[0].kind() == grin.GrinTokenKind.DIV):
                self.execute_operations(line)
            elif line[0].kind() == grin.GrinTokenKind.GOTO:
                self.execute_go_to(line)
            elif line[0].kind() == grin.GrinTokenKind.END:
                self.execute_end()
            elif line[0].kind() == grin.GrinTokenKind.GOSUB:
                self.execute_go_sub(line)
            elif line[0].kind() == grin.GrinTokenKind.RETURN:
                self.execute_return()
            elif line[1].kind() == grin.GrinTokenKind.COLON:
                self.execute_label_marker(line)


    def execute_return(self) -> None:
        """Execute the return instruction and add it to the order list."""
        self._order.append(['IGNORE_RETURN', 'return'])

    def execute_end(self) -> None:
        """Execute the end instruction and add it to the order list."""
        self._order.append(['IGNORE_END', 'end'])

    def execute_label_marker(self, line: list) -> None:
        """Execute the label marker instruction and add it to the label dictionary."""
        label = line[0].text()
        string = ""
        for lst in line[2:]:
            string += f'{lst.text()} '
        self._label[label] = len(self._order)
        self._input = string
        self.read_input()

    def execute_let(self, line: list) -> None:
        """Execute the let instruction and add it to the order list."""
        if len(line) == 3:
            var = line[1].text()
            if (line[2].kind() == grin.GrinTokenKind.LITERAL_STRING or
                    line[2].kind() == grin.GrinTokenKind.LITERAL_INTEGER or
                    line[2].kind() == grin.GrinTokenKind.LITERAL_FLOAT or
                    line[2].kind() == grin.GrinTokenKind.IDENTIFIER):
                self._order.append([var, 'let', line[2]])

    def execute_in_num(self, line: list) -> None:
        """Execute the in_num instruction and add it to the order list."""
        if len(line) == 2:
            var = line[1].text()
            self._order.append([var, 'in_num'])

    def execute_in_str(self, line: list) -> None:
        """Execute the in_str instruction and add it to the order list."""
        if len(line) == 2:
            var = line[1].text()
            self._order.append([var, 'in_str'])

    def execute_operations(self, line: list) -> None:
        """Execute the operation instruction and add it to the order list."""
        if len(line) == 3:
            operation = line[0].value()
            var = line[1].text()
            if operation == 'ADD':
                self._order.append([var, 'add', line[2]])
            elif operation == 'SUB':
                self._order.append([var, 'sub', line[2]])
            elif operation == 'MULT':
                self._order.append([var, 'mult', line[2]])
            elif operation == 'DIV':
                self._order.append([var, 'div', line[2]])

    def execute_go_to(self, line: list) -> None:
        """Execute the goto instruction and add it to the order list."""
        if (line[1].kind() == grin.GrinTokenKind.LITERAL_INTEGER or
                line[1].kind() == grin.GrinTokenKind.LITERAL_STRING):
            if len(line) == 2:
                self._order.append(['IGNORE_GOTO', 'goto', line[1]])
            else:
                compare_operator = line[4].text()
                self._order.append(['IGNORE_GOTO', 'goto_if', line[1], line[3], compare_operator, line[5]])
        else:
            self._order.append(['IGNORE_GOTO', 'goto', 'ERROR'])

    def execute_go_sub(self, line: list) -> None:
        """Execute the gosub instruction and add it to the order list."""
        if (line[1].kind() == grin.GrinTokenKind.LITERAL_INTEGER or
                line[1].kind() == grin.GrinTokenKind.LITERAL_STRING):
            if len(line) == 2:
                self._order.append(['IGNORE_GOSUB', 'gosub', line[1]])
            else:
                compare_operator = line[4].text()
                self._order.append(['IGNORE_GOSUB', 'gosub_if', line[1], line[3], compare_operator, line[5]])

        else:
            self._order.append(['IGNORE_GOSUB', 'gosub', 'ERROR'])

    def execute_print(self, line) -> None:
        """Execute the print instruction and add it to the order list."""
        if len(line) == 2:
            var = line[1].text()
            if line[1].kind() == grin.GrinTokenKind.IDENTIFIER:
                if var not in self._store_dict.keys():
                    self._order.append([var, 'print'])
                    self._store_dict[var] = 0
                else:
                    self._order.append([var, 'print'])
            elif (line[1].kind() == grin.GrinTokenKind.LITERAL_STRING or line[1].kind() ==
                  grin.GrinTokenKind.LITERAL_INTEGER or line[1].kind() == grin.GrinTokenKind.LITERAL_FLOAT):
                self._order.append(['IGNORE_PRINT', 'print', line[1].value()])

    def information(self) -> list:
        """Return the information consisting of order list, store_dict, label, and go_sub_index."""
        return [self._order, self._store_dict, self._label, self._go_sub_index]


def handle_user_input(interpreter, line_input: str) -> None:
    """Handle user input by setting the input line and reading it using the interpreter."""
    interpreter.set_input(line_input)
    interpreter.read_input()


def run_program() -> None:
    """Run the program by continuously taking user input until a period is entered."""
    interpreter = InputProcessor('')
    while True:
        line_input = input().strip()
        handle_user_input(interpreter, line_input)
        if line_input == '.':
            info = interpreter.information()
            print_object = print_module.PrintModule(info[0], info[1], info[2], info[3])
            print_object.execute_instructions()
            return False
