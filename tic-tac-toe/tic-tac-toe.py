def ticTacToe():
    game, player = False, str("O")
    
    #Really goofy winState array. represents each type of row win (found in tallyWin) if O wins anythin the value will be 30, if X wins it will be -30
    winState, positions = [0,0,0,0,0,0,0,0],[" "," "," "," "," "," "," "," "," "]
    print("---Tic-Tac-Toe---")
    while True:
        boardDisplay(positions)


        print(player, "\'s turn, please input 1-9 to select position:")
        move = input()
        if positions[int(move)-1] == " ":
            positions[int(move)-1] = player
        else:
            print("Place already Take!")
            continue

        winState = tallyWin(move, player, winState)

        if int(30) in winState:
            boardDisplay(positions)
            return print("O Wins!")
        elif int(-30) in winState:
            boardDisplay(positions)
            return print("X Wins!")


        if player == str("O"):
            player = str("X")
        else:
            player = str("O")

    return 0



#stole this bit, wasn't going to bother typing out the whole board.
def boardDisplay(positions):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(positions[0], positions[1], positions[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(positions[3], positions[4], positions[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(positions[6], positions[7], positions[8]))
    print("\t     |     |")
    print("\n")
    return 0




#Pirate software if statement ass section.
def tallyWin(move, player,winState):
    move = int(move)-1
    value = 10 if player == "O" else -10
    if move in [0,1,2]: winState[0] += value
    if move in [3,4,5]: winState[1] += value
    if move in [6,7,8]: winState[2] += value
    if move in [0,3,6]: winState[3] += value
    if move in [1,4,7]: winState[4] += value
    if move in [2,5,8]: winState[5] += value
    if move in [0,4,8]: winState[6] += value
    if move in [2,4,6]: winState[7] += value
    return winState

ticTacToe()
