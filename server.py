import socket

server_socket = socket.socket()
print('Socket Created')
server_socket.bind(('localhost', 9999))
server_socket.listen(3)
print('Waiting for connections')

while True:
    client_socket, address = server_socket.accept()
    print('Connected with', address)
    client_socket.send('Welcome!')
    client_socket.close()