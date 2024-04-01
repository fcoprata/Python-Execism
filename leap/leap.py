def leap_year(year) -> bool:
    """
    Check if a given year is a leap year.

    A leap year is a year that is exactly divisible by 4, except for years that are exactly divisible by 100.
    However, years that are exactly divisible by 400 are also leap years.

    Args:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False
