import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8080))
s.listen(5)

# 服务器端编程
conn, addr = s.accept()
print(f'Connected by {addr}')
data = conn.recv(1024)
conn.sendall(data)

conn.close()
s.close()

# 客户端编程
s.connect(('localhost', 8080))
s.sendall(b'Hello, server')
data = s.recv(1024)
print(f'Received {data}')

s.close()


## server side
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.50.3', 58080))
server.listen(5)

while True:
    conn, addr = server.accept()
    print(f'Connected by {addr}')
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
    conn.close()


## client
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 58080))
client.sendall(b'Hello, server')
data = client.recv(1024)
print(f'Received {data}')
client.close()
print(b'bytes object')
