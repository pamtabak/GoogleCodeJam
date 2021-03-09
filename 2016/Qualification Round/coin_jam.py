# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import math

# transform a number in any base
def number_to_base_x (number, base):
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

def base_x_to_number (number_sequence, base):
    number = 0
    largest_exponent = len(number_sequence) - 1
    for exponent in range(0, len(number_sequence)):
        if (number_sequence[exponent] == "1"):
            number += int(math.pow(base, largest_exponent - exponent))
    return number

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

def is_jam_coin(sequence):
    #consider all bases between 2 and 10
    for base in range(2, 11):
        number = base_x_to_number(sequence, base)
        if (is_prime(number)):
            return False
    return True

def first_non_trivial_divisor (number):
	for i in range(2, int(math.sqrt(number)) + 1):
		if (number % i == 0):
			return i

def generate_sequence(last_sequence, n):
    next_sequence_int = int(last_sequence, 2) + 1 #we are adding one int to the last sequence
    bin_number = str(bin(next_sequence_int))[2:]
    bin_number = "0"*(n-len(bin_number)) + bin_number
    return bin_number

#reading inputs
t = int(input())  # read a line with a single integer
n, j = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

#we need to find j different jam coin sequences with size n

print("Case #1:")

#All jam coins follow this rule: The first digit is 1 and the last digit is 1
#So we will only generate the n-2 digits in the middle
current_binary_sequence = "0"*(n-2)
coins_found = 0
while (coins_found < j):
    sequence = "1" + current_binary_sequence + "1"
    if (is_jam_coin(sequence)):
        coins_found += 1
        line_to_print = sequence
        for base in range(2, 11):
            line_to_print += " " + str(first_non_trivial_divisor(base_x_to_number(sequence, base)))
        print(line_to_print)
    current_binary_sequence = generate_sequence(current_binary_sequence, n-2)
