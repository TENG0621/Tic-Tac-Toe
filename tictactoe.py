#for 2 players tic-tac toe

from turtle import clear


board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

current_player = "X" #First Player is "X"

winner = None #since winning has no value, "NONE"

#function for the tic-tac-toe board 
#array is based on the "board"
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#function for the player input 
def player_input(board):
    player = int(input("Enter a number 1-9 : "))
    while True:
        if player >= 1 and player <= 9 and board[player - 1] == "-":
            #making sure is whithin the range and the board is still empty ("-")
            board[player - 1] = current_player
            break

        else:
            print("Invalid. Please try again")
            player = int(input("Enter a number 1-9 : "))

#function when winning horizontal condition  
def check_horizontal(board):
    global winner #global means it can be changed 
    if board[0] == board[1] == board [2] and board[1] != "-": #make sure its not 3 of "-"
        winner = board[0] #either one is fine since thier all equal "X "or "O" 
        return True
    
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True 

    elif board[6] == board[7] == board[8] and board[8] != "-":
        winner = board[6]
        return True 

#function when winning vertical condition 
def check_vertical(board):
    global winner 
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True 

    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True 

    elif board[3] == board[5] == board[8] and board[3] != "-":
        winner = board[3]
        return True 

#function when winning diagonal condition
def check_diagonal(board):
    global winner 
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True 
        
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True 

#function when switch the player 
def switch_player(board):
    global current_player
    if current_player == "X": 
        current_player = "O" #when the player 2 insert its input, channges to "O"

    else:
        current_player = "X" 


while True:
    print_board(board)
    player_input(board)

    #checking if there is a winning condition
    if check_horizontal(board) or check_vertical(board) or check_diagonal(board):
        print("Congratulation, the winner is : " + winner)

        #ask user if they want to play again
        again = input("Do you want to play again ? [y/n] : ")
        if again == "y":
            continue

        elif again == "n":
            print("Thank you for playing")
            break

    #checking if there is a tie condition
    if "-" not in board:
        print_board(board)
        print("It's a tie !")

        #ask user if they want to play again
        again = input("Do you want to play again ? [y/n] : ")
        if again == "y":
            continue

        elif again == "n":
            print("Thank you for playing")
            break

    switch_player(board)





