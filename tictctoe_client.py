import socket
import pickle
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 6666))
sym=s.recv(2048).decode('utf-8')



sid=[0]
psid=[0]
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def DrawBoard():    
    print(" %c | %c | %c " % (board[0],board[1],board[2]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[3],board[4],board[5]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[6],board[7],board[8]))    
    print("   |   |   ") 

def diogn(cha):
    if (board[0]==cha and board[4]==cha and board[8]==cha) or ( board[2]==cha and board[4]==cha and board[6]==cha):
        return True
def coln(cha):
    if (board[0]==cha and board[3]==cha and board[6]==cha) or (board[1]==cha and board[4]==cha and board[7]==cha) or (board[2]==cha and board[5]==cha and board[8]==cha):
        return True
def rows(cha):
    if (board[0]==cha and board[1]==cha and board[2]==cha) or (board[3]==cha and board[4]==cha and board[5]==cha) or (board[6]==cha and board[7]==cha and board[8]==cha):
        return True

def checkwin(cha):
    if diogn(cha)==True or coln(cha)==True or rows(cha)==True:
        return True
def isempty(mov):
    if board[mov]==' ':
        return True
    else:
        return False

def xmove():
    global board
    if psid[0]>0:
        board=reciv()
        print(board,type(board))
        print(board[4],type(board[4]))

    DrawBoard()
    while True:
        mov=input("X's move: ")

        mov=int(mov)-1
        if (isempty(mov)==True) and (mov<=9) and (mov>=0):
            print('inside if ')
            print(mov)
            board[mov]='X'
            print(board)
            sende(sym,1,board)
            print('msg sended')
            psid[0]=psid[0]+1
            break

    DrawBoard()
    if checkwin('X')==True:
        print('X win')
        exit()
    if checkwin('O')==True:
        print('O win')
        exit()



def omove():
    global board
    board=reciv()
    DrawBoard()
    while True:
        mov=input("O's move: ")
        try:
            mov=int(mov)-1
            if (isempty(mov)==True) and (mov<=9) and (mov>=0):
                board[mov]='O'
                sende(sym,sid,board)
                break

        except:
            pass
    DrawBoard()
    if checkwin('O')==True:
        print('O win')
        exit()
    if checkwin('X')==True:
        print('X win')
        exit()


def sende(sym,sid,brdc):
    brd = ','.join(brdc)
    print(brd)
    s.sendall(str.encode(sym+";"+str(sid)+";"+str(brd)))
def reciv():
    aa=(s.recv(2048).decode('utf-8'))
    a,b,c=aa.split(';')
    x=c.split(',')
    return x

while True:
    if sym=='X':
        xmove()
    elif sym=='O':
        omove()
    
    
