
# AUTOMATED UNIT TESTING

import pytest

from app import (
    calculate_total,
    apply_discount,
    calculate_final_amount
)


def test_calculate_total():
    assert calculate_total(100, 2) == 200


def test_apply_discount():
    assert apply_discount(1000, 10) == 900


def test_final_amount():
    assert calculate_final_amount(1000, 2, 10) == 1800


def test_invalid_price():
    with pytest.raises(ValueError):
        calculate_total(-100, 2)


def test_invalid_discount():
    with pytest.raises(ValueError):
        apply_discount(1000, 120)
