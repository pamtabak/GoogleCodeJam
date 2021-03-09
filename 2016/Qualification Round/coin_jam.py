# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import math

# transform a number in any base
def base_x (number, base):
    base_number = ""
    largest_exponent = int(math.log(number, base))
    for current_exponent in range(largest_exponent, -1, -1):
        current_value = int(math.pow(base, current_exponent))
        if (number >= current_value):
            base_number += "1"
            number -= current_value
        else:
            base_number += "0"
    return base_number

def is_prime(number):
    # to check if a number is prime we dont need to check if it is divided by all number - 1
    # we only need to check until sqrt
    if number == 2:
        # First prime number. We would need to change the iterator below
        # to work on this case as well, all others work
        return True
    for i in range(2, int(math.ceil(math.sqrt(number))) + 1):
        if number % i == 0:
            return False
    return True

#reading inputs
t = int(input())  # read a line with a single integer
n, j = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case


print("Case #1:")

