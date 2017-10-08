import socket
import sys

port = ''
host = 'localhost'
if len(sys.argv)==1:
	print("no port specified.default is 12344")
	port = 12344
else:
	port = int(sys.argv[1])

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port)) #bind the socket
sock.listen(1) #listen for incoming connection

conn, addr = sock.accept()
print("New connection from ",addr)
while True:
    data = conn.recv(1024)
    incoming = data.decode()
    param = incoming.split()
    if param[0] == "get":
        file = open(param[1], "rb")
        part = file.read(1024)
        while (part):
            print("Sent", repr(part))
            conn.send(part)
            part = file.read(1024)
        file.close()
        break
    else:
        print("wrong input client")
        break
conn.close()
