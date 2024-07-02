from dataclasses import dataclass


@dataclass
class Operands:
    first_operand: int
    second_operand: int


def operands_factory(first_operand: int, second_operand: int) -> Operands:
    if not isinstance(first_operand, int) or not isinstance(second_operand, int):
        raise (TypeError("Operands must be integers"))
    return Operands(first_operand, second_operand)
