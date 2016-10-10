import socket
import multiprocessing
import heatmap

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
        client.settimeout(60)
        multiprocessing.Process(target = listenToClient,args = (client,address,)).start()
        print('new Process started')

def heatmapper():
    global UltraList
    print "Processing %d points..." % len(UltraList)
    print(UltraList)
    hm = heatmap.Heatmap()
    img = hm.heatmap(UltraList).save("classic.png")
    print "Processed %d points... and saved image" % len(UltraList)



def listenToClient(client, address):
    print('Found a client')
    size = 1024
    global UltraList
    count=0
    while True:

        try:
            data = client.recv(size)
            print('Checking for client data')
            data = data.decode('ascii')
            print('Client Data Decoded')
            print(data)
            if data:
                print('Splitting into list')
                datlist= data.split(' ')
                print('split the list')
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
                    print('trying to get lock')
                    lock.acquire()
                    print('Got lock')
                    UltraList.append(tup)
                    if(len(UltraList)==10):
                        heatmapper()
                        del UltraList[:]
                    print(UltraList)
                    lock.release()
                    continue
            else:
                count+=1
                if(count==100):
                    raise ValueError('A very specific bad thing happened')
        except:
            print('whoa! an exception!')
            client.close()
            self.join()
            break



if __name__ == "__main__":
    print('Starting Server')
    ThreadedServer('127.0.0.1',80)
