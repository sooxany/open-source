def safe_division(number, divisor, ignore_overflow, ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise
result = safe_division(1.0, 10**500, True, False)
print(result)
result = safe_division(1.0, 0.0, False, True)
print(result)