import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def run(self):
        server = socket.socket()
        server.bind((self.host, self.port))
        server.listen()
        conn, addr = server.accept()
        print("Connection from:", str(addr))

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("Peer (client):", str(data))
            data = input(" -> ")
            conn.send(data.encode())
        conn.close()
        
if __name__ == "main":
    host = socket.gethostname()
    port = 5000
    server = Server(host, port)
    server.run()