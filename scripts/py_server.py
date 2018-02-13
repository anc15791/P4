import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (sys.argv[1], 9091)
sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()

    try:
        data = connection.recv(4)
        path = '/sys/class/net/%s/speed'%data

        with open(path) as f:
            contents = f.read()

        if data:
            connection.sendall(contents)
        else:
            break

    finally:
        connection.close()
