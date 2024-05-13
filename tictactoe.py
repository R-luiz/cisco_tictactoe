from random import randrange

def display_board(board):
    for i in range(3):
        print("+-------+-------+-------+\n|       |       |       |")
        print(f"|   {board[i][0]}   |   {board[i][1]}   |   {board[i][2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")
    return


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    target = input("Enter your move: ")
    try:
        target = int(target)
    except ValueError as ve:
        print(f"Enter an integer between 1 and 9 included : {ve}")
        return enter_move(board)
    except:
        print(f"Enter an integer between 1 and 9 included :")
        enter_move(board)
        return
    if  0 >= target or target >= 10 or target == 5:
        print(f"Invalid move. Enter an integer between 1 and 9 included :")
        return enter_move(board)
        
    dic = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
    if board[dic[target][0]][dic[target][1]] == ("O" or "X"):
        print("Invalid move, try again :")
        return enter_move(board)
    board[dic[target][0]][dic[target][1]] = "O"
    return board

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    freesq = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "O" and board[i][j] != "X":
                freesq.append((i,j))
    return freesq

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for i in range(3):
        for j in range(3):
            hsq = 0
            vsq = 0
            d1sq = 0
            d2sq = 0
            for k in range(3):
                if (i + k < 3 and board[i + k][j] == sign):
                    hsq += 1
                if (j + k < 3 and board[i][j + k] == sign):
                    vsq += 1
                if (i + k < 3 and j + k < 3 and board[i + k][j + k] == sign):
                    d1sq += 1
                if (i + k < 3 and j - k >= 0 and board[i + k][j - k] == sign):
                    d2sq += 1
            if 3 in (hsq, vsq, d1sq, d2sq):
                return True
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    freesq = make_list_of_free_fields(board)
    move = freesq[randrange(len(freesq))]
    board[move[0]][move[1]] = "X"
    return board

def main():
	board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
	display_board(board)
	sign = "X"
	while (not victory_for(board, sign)) and (len(make_list_of_free_fields(board)) != 0):
		if sign == "O":
			sign = "X"
		else:
			sign = "O"
		if sign == "O":
			enter_move(board)
			display_board(board)
		else:
			draw_move(board)
			display_board(board)
	if not victory_for(board, sign):
		print("It's a tie")
		return
	else:
		if sign == "O":
			print("You won!")
		else:
			print("Computer Won!")

if __name__ == '__main__':
	main()



















