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
        message = 'Node1 !6,9'
        #print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(message.encode('ascii'))
        ans = input('Continue?')
        if(ans=='y'):
            flag=0
        else:
            flag=1
    except:
        sock.close()
        break
