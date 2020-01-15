import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def connect(self):
        client = socket.socket()
        client.connect((host, port))

        message = input(" -> ")

        while (message.lower().strip() != "bye"):
            client.send(message.encode())
            data = client.recv(1024).decode()

            print("Peer (server):", str(data))

            message = input(" -> ")
        
        client.close()
        
if __name__ == "main":
    host = socket.gethostname()
    port = 5000
    client = Client(host, port)
    client.connect()