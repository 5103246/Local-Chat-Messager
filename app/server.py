import socket
import os
from faker import Faker

fake = Faker()

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = '/tmp/app_socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))

sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        print('connection from {}'.format(client_address))
        
        while True:
            data = connection.recv(4096)
            print('Received: ' + str(data))
            
            if data:
                response = fake.text()
                connection.sendall(response.encode())
            else:
                print('no data from client side')
                break
                
    finally:
        print('closing socket')
        connection.close()