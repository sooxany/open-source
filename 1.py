def remainder(number, divisor):
    return number % divisor

assert remainder(20, 7) == 6
assert remainder(number=20, divisor=7) == 6 # keyword arguments
assert remainder(20, divisor=7) == 6 # mixed!
assert remainder(divisor=7, number=20) == 6 # change the order
