import socket

import sys 



# Create a TCP/IP socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



# Connect the socket to the port where the server is listening

server_address = (sys.argv[1], 9091)

#print >>sys.stderr, 'connecting to %s port %s' % server_address

sock.connect(server_address)



try:

    

    # Send data

    message = '%s'%sys.argv[2]

    #print >>sys.stderr, 'sending "%s"' % message

    sock.sendall(message)

    data = sock.recv(4)

    #print >>sys.stderr, 'received %s' % data
    print data


finally:

    #print >>sys.stderr, 'closing socket'

    sock.close
