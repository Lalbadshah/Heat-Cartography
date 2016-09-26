import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1',80)
#print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
flag=0;
while(flag==0):
    try:

        # Send data
        message = input('Enter Message to send: ')
        #print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(message.encode('ascii'))
    except:
        sock.close()
        break
