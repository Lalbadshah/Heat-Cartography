import socket
import heatmapExample

UltraList=[]
mastercount=0

def ThreadedServer(host,port):
    host = host
    port = port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host,port))
    listen(sock)

def listen(sock):
    print('Now Listening for clients')
    sock.listen(5)
    while True:
        client, address = sock.accept()
        print('Accepting a client')
        client.settimeout(60)
        listenToClient(client,address)

def listenToClient(client,address):
    print('Found a client')
    size = 1024
    count=0
    while True:

            data = client.recv(size)
            data = data.decode('ascii')
            print(data)
            if data:
                datlist= data.split(' ')
                nodename = datlist[0]
                if("NEW" in datlist):
                    print('new connection')
                    continue
                else:
                    print('parsing response')
                    coords = data.split("!")[1]
                    coords = coords.split(",")
                    x= int(coords[0])
                    y= int(coords[1])
                    tup=(x,y)
                    UltraList.append(tup)
                    if(len(UltraList)>9):
                        print("Trying to create heatmap")
                        global mastercount
                        mastercount+=1
                        print("updated mastercount")
                        heatmapExample.heatmapper(UltraList,mastercount)
                        print("heatmapper execution comepleted")
                        del UltraList[:]
                        print("list cleared")
                    print(UltraList)
                    continue
            else:
                if(count==100):
                    raise ValueError('A very specific bad thing happened')



if __name__ == "__main__":
    print('Starting Server')
    ThreadedServer('127.0.0.1',80)
