import socket
import multiprocessing

UltraList=[]
lock = multiprocessing.Lock()

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
        #client.settimeout(60)
        multiprocessing.Process(target = listenToClient,args = (client,address,),daemon=True).start()
        print('new Process started')




def listenToClient(client, address):
    print('Found a client')
    size = 1024
    global UltraList
    while True:
        print('trying to get lock')
        lock.acquire()
        print('Got lock')
        try:
            data = client.recv(size)
            print('Client data recieved')
            data = data.decode('ascii')
            print('Client Data Decoded')
            print(data)
            if data:
                print('Splitting into list')
                datlist= data.split(' ')
                print('split the list')
                nodename = datlist[0]
                if("NEW" in datlist):
                    print('new connection releasing lock')
                    lock.release()
                    continue
                else:
                    print('parsing response')
                    coords = data.split("!")[1]
                    coords = coords.split(",")
                    x= int(coords[0])
                    y= int(coords[1])
                    tup=(x,y)
                    UltraList.append(tup)
                    print(UltraList)
                    lock.release()
                    continue
            else:
                lock.release()
                raise error('Client disconnected')
        except:
            print('whoa! and exception!')
            lock.release()
            client.close()
            break



if __name__ == "__main__":
    print('Starting Server')
    ThreadedServer('127.0.0.1',80)
