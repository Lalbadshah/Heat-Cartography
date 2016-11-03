import socket
import sys
import random
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1',80)
#print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
flag=0
while(flag==0):
    i=1
    while(i!=11):
        message = random.choice(['Node1 !6,9','Node2 !600,900','Node3 !500,500','Node4 !6,800'])
        print (message)
        sock.sendall(message.encode('ascii'))
        i+=1
        time.sleep(2)
    if(input("Send more?[y/n]")=='n'):
        flag=1
