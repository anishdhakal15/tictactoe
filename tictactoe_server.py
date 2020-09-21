import socket
from _thread import *
host = 'yourhost'
port = #port
global data2
data2=''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))
s.listen(2)
print('Waiting for a connection.')
def x_host(conn):
    global data2
    while True:
        try:
            a=data2.split(';')
            a=a[0]
            if a=='O':
                print("if==o")
                conn.sendall(str.encode(data2))
                data2=conn.recv(2048).decode('utf-8')
        except:
            pass
        if data2=='':
            print("if ==''")
            data2=conn.recv(2048).decode('utf-8')
    conn.close()
def o_host(bonn):
    global data2
    while True:
        try:
            a=data2.split(';')
            a=a[0]
            if a=='X':
                print('send ata ohost')
                bonn.sendall(str.encode(data2))
                data2=bonn.recv(2048).decode('utf-8')
        except:
            pass
    bonn.close()
c=1
while True:
    if c==1:
        c1='X'
        print(c1)
        conn, addr = s.accept()
        conn.send(str.encode(c1))
        start_new_thread(x_host,(conn,))
        c=c+1
    elif c==2:
        c1='O'
        print(c1)
        bonn, bddr = s.accept()
        bonn.send(str.encode(c1))
        start_new_thread(o_host,(bonn,))
        c=c+1
    
    #data =data.decode('utf-8')

    #print('connected to: '+addr[0]+':'+str(addr[1]))
'''

    socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 6666))
    s.recv(2048)
b'O'
>>> s.sendall(str.encode(a))
>>> s.recv(2048)
'''

