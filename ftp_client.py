import socket
import sys

port = ''
if len(sys.argv)==1:
	print("No port specified,default is 12344")
	port=12344
else:
	port = int(sys.argv[1])
host = 'localhost'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:	#try to connect to server
	sock.connect((host,port))
except socket.error as msg:	#if we got error,close the socket and exit
	sock.close()
	print("Cannot connect to server")
	sys.exit(1)

if sock is not None:
    msg = input("input message")
    param = msg.split()
    if param[0]== "get" :
        sock.send(msg.encode())
        with open(param[2],'wb') as file:
            print("file opened")
            while True:
                print("receiving data")
                data = sock.recv(1024)
                if not data:
                    break
                file.write(data)
            file.close()
            sock.close()
    else :
        sock.send(msg.encode())
    print("file received")