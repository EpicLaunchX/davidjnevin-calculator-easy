class Operands:
    def __init__(self, first_operand: int, second_operand: int):
        if not isinstance(first_operand, int) or not isinstance(second_operand, int):
            raise TypeError("Both Operands must be integers")
        self.first_operand = first_operand
        self.second_operand = second_operand

