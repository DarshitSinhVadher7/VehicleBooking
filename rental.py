
def calculate_rental_charge(daily_rate, rental_days):
    if not isinstance(rental_days, int) or isinstance(rental_days, bool):
        raise ValueError("Rental days must be a whole number.")
    if rental_days <= 0:
        raise ValueError("Rental days must be greater than zero.")
    if daily_rate <= 0:
        raise ValueError("Daily rate must be greater than zero.")

    return daily_rate * rental_days
