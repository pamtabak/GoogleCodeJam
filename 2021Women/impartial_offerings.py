# minimum number of treats she needs to buy to be able to offer at least one treat to all pets while complying with her impartiality rules.

# reading inputs
t = int(input())  # read a line with a single integer

for execution in range(0, t):
    n = int(input())
    sizes = [int(s) for s in raw_input().split(" ")]

    pets_by_size = {}
    for pet in sizes:
        if (pet not in pets_by_size):
            pets_by_size[pet] = 0
        pets_by_size[pet] += 1
    keys = pets_by_size.keys()
    keys.sort()
    current_amount_of_treats = 1
    total_amount_of_treats = 0
    for pet in keys:
        total_amount_of_treats += pets_by_size[pet]*current_amount_of_treats
        current_amount_of_treats += 1
    print("Case #" + str(execution + 1) + ": " + str(total_amount_of_treats))
