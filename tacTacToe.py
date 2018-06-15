import os
arr=[['1','2','3'],['4','5','6'],['7','8','9']]

def board():
    print("\n\n")
    print("\t\t ",arr[0][0],"|",arr[0][1],"|",arr[0][2])
    print("\t\t-------------")
    print("\t\t ",arr[1][0] , "|" , arr[1][1] , "|", arr[1][2])
    print("\t\t-------------")
    print("\t\t ", arr[2][0], "|", arr[2][1], "|", arr[2][2])
def player1():
    validInput=False
    print("\nPlayer 1's turn: ",end='')
    while not validInput:
        ch=input()
        for i in range(3):
            for j in range(3):
                if ch==arr[i][j]:
                    arr[i][j]='X'
                    validInput=True

def player2():
    validInput = False
    print("\nPlayer 2's turn: ",end='')
    while not validInput:
        ch = input()
        for i in range(3):
            for j in range(3):
                if ch == arr[i][j]:
                    arr[i][j] = 'O'
                    validInput = True

def player1Win():
    won=False
    if arr[0][0]=='X' and arr[0][0]==arr[0][1] and arr[0][0]==arr[0][2]:
        won=True
    elif arr[1][0] == 'X' and arr[1][0] == arr[1][1] and arr[1][0] == arr[1][2]:
        won = True
    elif arr[2][0] == 'X' and arr[2][0] == arr[2][1] and arr[2][0] == arr[2][2]:
        won = True
    elif arr[0][0] == 'X' and arr[0][0] == arr[1][0] and arr[0][0] == arr[2][0]:
        won = True
    elif arr[0][1] == 'X' and arr[0][1] == arr[1][1] and arr[0][1] == arr[2][1]:
        won = True
    elif arr[0][2] == 'X' and arr[0][2] == arr[1][2] and arr[0][2] == arr[2][2]:
        won = True
    elif arr[0][0] == 'X' and arr[0][0] == arr[1][1] and arr[0][0] == arr[2][2]:
        won = True
    elif arr[0][2] == 'X' and arr[0][2] == arr[1][1] and arr[0][2] == arr[2][0]:
        won = True
    if won:
        return True

def player2Win():
    won=False
    if arr[0][0]=='O' and arr[0][0]==arr[0][1] and arr[0][0]==arr[0][2]:
        won=True
    elif arr[1][0] == 'O' and arr[1][0] == arr[1][1] and arr[1][0] == arr[1][2]:
        won = True
    elif arr[2][0] == 'O' and arr[2][0] == arr[2][1] and arr[2][0] == arr[2][2]:
        won = True
    elif arr[0][0] == 'O' and arr[0][0] == arr[1][0] and arr[0][0] == arr[2][0]:
        won = True
    elif arr[0][1] == 'O' and arr[0][1] == arr[1][1] and arr[0][1] == arr[2][1]:
        won = True
    elif arr[0][2] == 'O' and arr[0][2] == arr[1][2] and arr[0][2] == arr[2][2]:
        won = True
    elif arr[0][0] == 'O' and arr[0][0] == arr[1][1] and arr[0][0] == arr[2][2]:
        won = True
    elif arr[0][2] == 'O' and arr[0][2] == arr[1][1] and arr[0][2] == arr[2][0]:
        won = True
    if won:
        return True

counter=int(0)
game=True
print("\n\tX represents player 1 and O represents player 2\n")
board()
k='y'
while k=='y' or k=='Y':

    while game:
        #board()

        player1()
        os.system('cls')
        print("\n\tX represents player 1 and O represents player 2\n")
        board()
        if player1Win()==True:
            print("\n\tPlayer 1 Win")
            break
        counter+=1
        if counter==5:
            print("\n\tGame is Draw")
            game=False
            break
        #os.system('cls')
        #print("\n")
        player2()
        os.system('cls')
        print("\n\tX represents player 1 and O represents player 2\n")
        board()
        if player2Win()==True:
            print("\n\tPlayer 2 Win")
            break;
    k=input("Do you wand to play again?(y/n)")
    if(k=='y' or k=='Y'):
        counter=0
        arr = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        os.system('cls')
        print("\n\tX represents player 1 and O represents player 2\n")
        board()
