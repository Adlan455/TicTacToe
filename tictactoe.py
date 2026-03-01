import random
def printboard(board):
    board1 = '\n'

    for i in range(0,9):

        try:
            board1 += str(board[i])
        except:
            board1 += board[i]

        if (i+1) % 3:
            board1 += ' | '

        elif (i+1) == 9:
            board1 += '\n'
            break           
        else:
            board1 += '\n- . - . -\n'
    return board1

def checkwin(board):
    winning_combos = [
        (0, 1, 2),  # top row
        (3, 4, 5),  # middle row
        (6, 7, 8),  # bottom row
        (0, 3, 6),  # left column
        (1, 4, 7),  # middle column
        (2, 5, 8),  # right column
        (0, 4, 8),  # diagonal
        (2, 4, 6)   # diagonal
    ]
    
    for a, b, c in winning_combos:
        if board[a] == board[b] == board[c]:
            print(printboard(board))
            print(f"{board[a]} won")
            return False
    
    return True


def playermove(player):

    player1 = input(f'Player {player}, type in your move from 1-9.\n')
    while not isinstance(board[int(player1) - 1],int): 
        print('Move is not valid.\n')
        player1 = input(f'Player {player}, type in your move from 1-9.\n')

    board[int(player1) - 1] = 'x'

    # if player:
    #     board[int(player1) - 1] = 'o'
    #     player = 0
    # else:
    #     board[int(player1) - 1] = 'x'
    #     player = 1


def computer(board):
    winning_combos = [
        (0, 1, 2),  # top row
        (3, 4, 5),  # middle row
        (6, 7, 8),  # bottom row
        (0, 3, 6),  # left column
        (1, 4, 7),  # middle column
        (2, 5, 8),  # right column
        (0, 4, 8),  # diagonal
        (2, 4, 6)   # diagonal
    ]
    
    #possible moves
    possible_moves = set([x-1 for x in board if isinstance(x,int)])
    move_log = set([i for i, char in enumerate(board) if char == 'o'])


    for a,b,c in winning_combos:
        values = [board[a], board[b], board[c]]
        if values.count('x') >= 2 and any(isinstance(item, int) for item in values): # defensive logic
            move = next((v for v in values if v != 'x' and v != 'o'),None)
            print('in order, ',move)
            board[move - 1] = 'o'
            return

    #priority 1, find intersection of combos, possible moves and made moves

    intersection =  possible_moves & move_log 
    winnable = [combo for combo in winning_combos if set(combo).issubset(intersection)]
    if winnable:
        rand_tuple = random.choice(list(winnable))
        move = random.choice(list(rand_tuple))
        return

    # #priority 2, find interesction of combos and possible moves
    # winnable = [combo for combo in winning_combos if set(combo).issubset(possible_moves)]
    # rand_tuple = random.choice(winnable)
    # move = random.choice(rand_tuple)
    # return

    #priority 3, only moves or no set up to win.
    else:
        move = random.choice(list(possible_moves))
        board[move] = 'o'
        return



# player2 = input('Player 2, type in your move from 1-9.\n')
# board[int(player2) - 1] = 'o'

board = [x for x in range(1,10)]
counter = 0
while checkwin(board) and counter < 9:
    print(printboard(board))
    player = 0 
    playermove(player)
    if not checkwin(board):
        break
    counter +=1
    player = 1
    if counter == 9:
        print('\nDRAW\n')
        break
    computer(board)
    counter += 1

