def leap_year(year):
    if type(year) is not int:
        raise TypeError("Year must be an integer number")

    if year % 4 == 0:
        return True
    else:
        return False
