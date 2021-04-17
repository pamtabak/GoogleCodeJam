def check_if_know_someone_in_common (friends_1, friends_2):
    for f1 in friends_1:
        for f2 in friends_2:
            if f1 == f2:
                return True
    return False

# reading inputs
t = int(input())  # read a line with a single integer

for execution in range(0, t):
    m, n, p = [int(s) for s in raw_input().split(" ")]
    #first, we extract all the information we need
    #there are m managers, n non managers and p pais we want to know the amount of time until they meet
    team_members = [] #represent if the team members know each other
    for line in range(m + n):
        team_members.append(str(raw_input()))
    times = ""
    for line in range(p):
        # we want to check the amount of time for pair_1 to meet pair_2 (or if that is impossible)
        pair_1, pair_2 = [int(s) for s in raw_input().split(" ")])
        # first, lets try "brute force".
        # we check if pair1 and pair 2 know each other
        # if they dont, we check if they know someone in common
        # if they dont, we check if the people they know know someone in common
        # and so on
        time = -1 # this is the worst case scenario
        # we need to remember that for each team session to happen, there must be a manager that already knows the other two participants
    
    print("Case #" + str(execution + 1) + ": " + times)