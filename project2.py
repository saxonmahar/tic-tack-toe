def printboard(xState, ZState):
    zero = 'X' if xState[0] else ('O' if ZState[0] else 0)
    one = 'X' if xState[1] else ('O' if ZState[1] else 1)
    two = 'X' if xState[2] else ('O' if ZState[2] else 2)
    three = 'X' if xState[3] else ('O' if ZState[3] else 3)
    four = 'X' if xState[4] else ('O' if ZState[4] else 4)
    five = 'X' if xState[5] else ('O' if ZState[5] else 5)
    six = 'X' if xState[6] else ('O' if ZState[6] else 6)
    seven = 'X' if xState[7] else ('O' if ZState[7] else 7)
    eight = 'X' if xState[8] else ('O' if ZState[8] else 8)
    print(f"{zero} | {one} | {two}")
    print("--|---|--")
    print(f"{three} | {four} | {five}")
    print("--|---|--")
    print(f"{six} | {seven} | {eight}")


if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ZState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("Welcome to Tic Tac Toe")
    while True:
        printboard(xState, ZState)
        if turn == 1:
            print("X's turn")
            value = int(input("Enter the position number: "))
            xState[value] = 1  # Update xState
            turn = 0  # Switch turn to O
        else:
            print("O's turn")
            value = int(input("Enter the position number: "))
            ZState[value] = 1  # Update ZState
            turn = 1  # Switch turn to X

        # Check if the game is over
        if xState[0] == xState[1] == xState[2] == 1 or xState[3] == xState[4] == xState[5] == 1 or xState[6] == xState[7] == xState[8] == 1 or xState[0] == xState[3] == xState[6] == 1 or xState[1] == xState[4] == xState[7] == 1 or xState[2] == xState[5] == xState[8] == 1 or xState[0] == xState[4] == xState[8] == 1 or xState[2] == xState[4] == xState[6] == 1:
            printboard(xState, ZState)
            print("X wins")
            break
        elif ZState[0] == ZState[1] == ZState[2] == 1 or ZState[3] == ZState[4] == ZState[5] == 1 or ZState[6] == ZState[7] == ZState[8] == 1 or ZState[0] == ZState[3] == ZState[6] == 1 or ZState[1] == ZState[4] == ZState[7] == 1 or ZState[2] == ZState[5] == ZState[8] == 1 or ZState[0] == ZState[4] == ZState[8] == 1 or ZState[2] == ZState[4] == ZState[6] == 1:
            printboard(xState, ZState)
            print("O wins")
            break
        elif 0 not in xState and 0 not in ZState:
            printboard(xState, ZState)
            print("It's a tie")
            break