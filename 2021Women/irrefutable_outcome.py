t = int(input())  # read a line with a single integer
#t = 1

for execution in range(0, t):
    board = str(raw_input())
    #board = "IOIOIOOIO"

    current_player = "I"
    other_player = "O"
    while (True):
        # the player must remove one piece: either the leftmost or the rightmost
        # it needs to remove the one that maximizes its winning or minimizes its losses

        # we first check if the game is over
        if (len(board) == 0 or (board[0] != current_player and board[len(board) - 1] != current_player)):
            current_player = other_player
            break

        # now we check if there is only one play possible (only one of the extremities can be removed)
        if (board[0] == current_player and board[len(board) - 1] != current_player):
            board = board[1:]
        elif (board[0] != current_player and board[len(board) - 1] == current_player):
            board = board[:-1]
        else:
            # it means both the rightmost and leftmost piece are from that player, so we need to choose what is the best option
            if (len(board) == 1):
                board = ""  # the winner is the current player
                break
            # we will shift to left until we find two equal chars
            left_shift = 1
            while (left_shift < len(board) and board[left_shift] != board[left_shift - 1]):
                left_shift += 1
            if (left_shift == len(board)):
                # we need to decide the winner
                # depends on the amount of moves
                if (len(board) % 2 == 0):
                    current_player = other_player
                board = ""
                break
            right_shift = 1
            while (right_shift < len(board) and board[-(right_shift + 1)] != board[- right_shift]):
                right_shift += 1

            if (current_player == board[left_shift] and current_player == board[-right_shift]):
                # current player wins, since both ends of the string are with his piece
                # it depends whether he choose to go right or left
                if (left_shift > right_shift):
                    board = board[:-right_shift]
                else:
                    board = board[left_shift:]
            elif (current_player == board[left_shift]):
                board = board[left_shift:]
            elif (current_player == board[-right_shift]):
                board = board[:-right_shift]
                # current_player = other_player
            else:
                # neither of the ends are the current_player, so the other player wins
                board[left_shift:-right_shift]
                current_player = other_player
            break

            # changing player
        tmp_player = other_player
        other_player = current_player
        current_player = tmp_player

    pontuation = 1 + len(board)
    result = current_player + " " + str(pontuation)
    print("Case #" + str(execution + 1) + ": " + result)
