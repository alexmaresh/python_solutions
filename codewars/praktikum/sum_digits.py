# A three-digit number is given (it can be negative). Find the sum of its digits.

def sum_digits(x=int) -> int:
    digits = [int(d) for d in str(abs(x))]
    return sum(digits)
