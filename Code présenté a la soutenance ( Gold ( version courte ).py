2
#Tictactoe_ai

#This function displays the matrix every round.
def display_matrix(matrix):
    for row in matrix:
        print(" | ".join(row))
        print("-" * 9)

#This function checks if a player has won
def check_victory(matrix, player):
    return any(all(matrix[i][j] == player for j in range(3))\
         or all(matrix[j][i] == player for j in range(3)) for i in range(3)) or \
           all(matrix[i][i] == player for i in range(3))\
             or all(matrix[i][2 - i] == player for i in range(3))



#(AI)ia_move first looks for a winning move for the AI, then a move to block the opponent. 
# If none of these moves are possible, she chooses a strategic position by default.
def ia_move(matrix):
    for player in ["O", "X"]:  # Check if AI can win or needs to block X
        for i in range(3):
            for j in range(3):
                if matrix[i][j] not in "XO":
                    matrix[i][j] = player
                    if check_victory(matrix, player):
                        return i, j
                    matrix[i][j] = str(3 * i + j + 1)
    return (1, 1) if matrix[1][1] not in "XO" else next((i, j)\
         for i, j in [(0, 0), (0, 2), (2, 0), (2, 2),\
             (0, 1), (1, 0), (1, 2), (2, 1)] if matrix[i][j] not in "XO")

#Matrix initialization,player = "X" initializes the first player as "X"

def tic_tac_toe():

#Choice of mode 
    mode = input("Choose mode: 1 for two players, 2 for single player against AI: ")
    if mode not in {"1", "2"}: return

    matrix = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
    player = "X"

# 9-round game loop
    for turn in range(9):
        display_matrix(matrix)

#(Choise of mode): Loop supports both modes : 
# we put an "if" to present the validity checks of the choice of the box,
#  then introduce an "else" to call the function ia
        if mode == "1"or player == "X":

#checks if the square is not already occupied, if the choice is valid,
# it is converted into coordinates (line, col) on the board.
            choice = input(f"Player {player}, enter cell number (1-9): ")
            if not choice.isdigit() or not (1 <= int(choice) <= 9) \
                or matrix[(int(choice) - 1) // 3][(int(choice) - 1) % 3] in "XO":
                print("Invalid move, try again.")
                continue
            row, col = (int(choice) - 1) // 3, (int(choice) - 1) % 3


#(AI) This block of code executes if it is the AI's turn to play. 
# It calls the ia_move() function to choose an optimal square, 
# records the coordinates of that square, 
# and displays a message to inform players that the AI ​​has played.

        else:
            row, col = ia_move(matrix)
            print("AI (O) played.")



#The chosen square is updated on the board with the player's symbol ("X" or "O"). 
# Then, verify_victory is called to see if this move created a victory condition. 
# If so, the board is displayed one last time, and a victory message is displayed. 
# The game ends with return.

        matrix[row][col] = player
        if check_victory(matrix, player):
            display_matrix(matrix)
            print(f"Player {player} wins!")
            return
        
#change of player
        player = "O" if player == "X" else "X"
        

#drawn game
    display_matrix(matrix)
    print("It's a draw!")

tic_tac_toe()
