import socket

host = "127.0.0.1"
port = 8007
bufsize = 1024

sock = socket.socket()
sock.bind((host, port))
sock.listen(1)
conn, addr = sock.accept()

print 'connected:', addr
data = "hello"
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data)

conn.close()