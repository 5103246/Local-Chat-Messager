import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = '/tmp/udp_socket_file'

client_address = '/tmp/udp_client_socket_file'

message = b'Message to send the client'

sock.bind(client_address)

try:
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)
    
    print('waiting to receive')
finally:
    print('closing socket')
    sock.close()