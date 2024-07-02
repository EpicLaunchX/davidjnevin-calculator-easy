import pytest
from src.pytemplate.domain.models import operands_factory


def test_operands_initialization():
    operands = operands_factory(5, 10)
    assert operands.first_operand == 5
    assert operands.second_operand == 10


def test_operands_type_checking():
    with pytest.raises(TypeError):
        operands_factory("5", 10)
    with pytest.raises(TypeError):
        operands_factory(5, "10")
    with pytest.raises(TypeError):
        operands_factory(5, 10.5)


def test_operands_negative_numbers():
    operands = operands_factory(-5, -10)
    assert operands.first_operand == -5
    assert operands.second_operand == -10


def test_operands_zero():
    operands = operands_factory(0, 0)
    assert operands.first_operand == 0
    assert operands.second_operand == 0
