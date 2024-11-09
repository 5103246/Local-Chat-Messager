import socket
import sys

args = sys.argv

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = '/tmp/app_socket_file'
print('connecting to {}'.format(server_address))

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    if args[1] is None:
        message = 'no data from client side'
    else:
        message = ''
        for i in range(1, len(args)):
            message += args[i] + ' '
        
    sock.sendall(message.encode())
    
    sock.settimeout(4)
    
    try:
        while True:
            data = str(sock.recv(4096))
            if data:
                print('Server response: ' + data)
            else:
                print('no data from server side')
                break
    except(TimeoutError):
        print('Socket timeout, ending listening for server message')
finally:
    print('closing socket')
    sock.close()