
import pytest
from rental import calculate_rental_charge


@pytest.mark.parametrize(
    "daily_rate, rental_days, expected",
    [
        (45, 1, 45),  
        (50, 3, 150),  
    ],
)
def test_valid_rental_charges(daily_rate, rental_days, expected):
    assert calculate_rental_charge(daily_rate, rental_days) == expected


@pytest.mark.parametrize("rental_days", [0, -1])
def test_invalid_rental_days(rental_days):
    with pytest.raises(ValueError):
        calculate_rental_charge(45, rental_days)


def test_invalid_non_integer_rental_days():
    with pytest.raises(ValueError):
        calculate_rental_charge(45, 1.5)
