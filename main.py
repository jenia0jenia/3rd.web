import socket

host = "127.0.0.1"
port = 8000
bufsize = 1024

sock = socket.socket()
sock.bind((host, port))
sock.listen(1)
conn, addr = sock.accept()

print 'connected:', addr

while True:
    data = conn.recv(1024)
    conn.send(data)
    if not data:
        break

conn.close()