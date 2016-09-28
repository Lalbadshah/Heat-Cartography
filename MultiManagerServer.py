import socket
import threading
import asyncio

UltraList=[]
lock = threading.Lock()

class ThreadedServer(threading.Thread):
    def __init__(self, host, port, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        super().__init__()
        self.args = args
        self.kwargs = kwargs
        return

    def run(self):
        pass

    def listen(self):
        print('Now Listening for clients')
        print('Current Running Threads')
        print(threading.activeCount())
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            print('Accepting a client')
            #client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address),daemon=True).start()
            print('new Thread started')
        #    print(threading.activeCount())

    def listenToClient(self, client, address):
        print(threading.activeCount())
        print('Found a client')
        size = 1024
        while True:
            print('trying to get lock')
            yield from lock
            print('Got lock')
            try:
                data = client.recv(size)
                print('Client connected')
                data = data.decode('ascii')
                if data:
                    datlist = data.split("")
                    nodename = datlist[0]
                    if("NEW" in datlist):
                        continue
                    else:
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
                    raise error('Client disconnected')
            except:
                client.close()
                break
        threading.Thread.join()

if __name__ == "__main__":
    port_num = input("Port? ")
    ThreadedServer('127.0.0.1',int(port_num)).listen()
