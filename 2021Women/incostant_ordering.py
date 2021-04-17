# We want to build a string with English alphabet uppercase letters in sorted order. However, we want the order to be sometimes strictly increasing and sometimes strictly decreasing.
# The first letter of the string must be A. After that, the string must contain one or more blocks of letters.
# The i-th block must contain exactly Li letters. Each letter in the i -th block must be later in the
# alphabet than its preceding letter in the string if i
# is odd and earlier in the alphabet than its preceding letter if i
# is even. Notice that for the first letter of a block, its preceding letter exists, even though it is not in the block.
# Strings that follow all of these rules are called valid. There can be multiple valid strings, and we want to find the alphabetically first one.

# reading inputs
t = int(input())  # read a line with a single integer

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for execution in range(0, t):
    n = int(input())
    block_sizes = [int(s) for s in raw_input().split(" ")]

    string = "A"
    for i in range(len(block_sizes)):
        current_letter_index = 0
        if (i % 2 != 0):
            current_letter_index = block_sizes[i]
        for j in range(block_sizes[i]):
            # checking if the i-th block is odd or even
            if (i % 2 == 0):
                current_letter_index += 1
                if (j == (block_sizes[i] - 1) and i < (len(block_sizes) - 1) and current_letter_index < block_sizes[i + 1]):
                    #it means the next block is even and we need to have the necessary amount of letters to "return"
                    current_letter_index = block_sizes[i + 1]
            else:
                current_letter_index -= 1
            string += letters[current_letter_index]

    print("Case #" + str(execution + 1) + ": " + string)
