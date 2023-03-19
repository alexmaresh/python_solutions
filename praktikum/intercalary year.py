# Is the given year a leap year?
# (A year is a leap year if its number is a multiple of 4 but not a multiple of 100, and also if it is a multiple of 400.)

def leap_year(x:int) -> str:
    res = "YES" if x % 4 == 0 and x % 100 !=0 or x % 400 == 0 else "NO"
    return res

