# display the board (9 positions)
# Make sure board is empty
# Provide numbers for each cell
# Provide error message for filling a filled cell
# If game is over, send message saying you won

theBoard = {'7':' ','8':' ','9':' ','4':' ','5':' ','6':' ','1':' ','2':' ','3':' '}
boardKeys = []


for key in theBoard:
    boardKeys.append(key)
    
#print(boardKeys)
    
def printBoard(board):
    print(board['7'] + '/' + board['8'] + '/' + board['9'])
    print('-+-+-')

    print(board['4'] + '/' + board['5'] + '/' + board['6'])
    print('-+-+-')
    
    print(board['1'] + '/' + board['2'] + '/' + board['3'])
    print('-+-+-')

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It is the turn of " + turn + ". Specify the place you want to play.")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count+=1
        else:
            print("Sorry this cell is already filled.")

            continue

        if count >= 5:

            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("Game over")
                print("Player " + turn + " won the game!")

                break

            if theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("Game over")
                print("Player " + turn + " won the game!")

                break

            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("Game over")
                print("Player " + turn + " won the game!")

                break

            if theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ':
                printBoard(theBoard)
                print("Game over")
                print("Player " + turn + " won the game!")

                break

            if theBoard['8'] == theBoard['5'] == theBoard['2'] != ' ':
                printBoard(theBoard)
                print("Game over")
                print("Player " + turn + " won the game!")

                break

            if theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("Game over")
                print("Player " + turn + " won the game!")

                break

            if theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("Game over")
                print("Player " + turn + " won the game!")

                break

            if theBoard['9'] == theBoard['5'] == theBoard['1'] != ' ':
                printBoard(theBoard)
                print("Game over")
                print("Player " + turn + " won the game!")

                break

        if count == 9:
            print("Game over")
            print("The game is tied")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Do you want to restart? (y/n)")

    if restart == 'y' or restart == 'Y':
        for key in boardKeys:
            theBoard[key] = ' '
        game() # recursive function (function in the same function)

if __name__ == "__main__":
    game()