if __name__ == "__main__":
# ini adalah jawaban soal nomor4
    board = {
        'top-L': ' ',
        'top-M': ' ',
        'top-R': ' ',
        'mid-L': ' ',
        'mid-M': ' ',
        'mid-R': ' ',
        'low-L': ' ',
        'low-M': ' ',
        'low-R': ' '
    }
    winner = None
    player = "X"

def printBoard(board):

    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def playGames(playerX, playerO):
    printBoard(board)
    global winner
    for i in range(len(board)):
        while True:
            boardslot = input('Giliran anda : ')
            if board[boardslot] == ' ':
                break
            else:
                print('Opss! Try again: ')

        if i % 2 == 0:
            board[boardslot] = playerX
        else:
            board[boardslot] = playerO
        printBoard(board)

playGames('X','O')







                        






