from concurrent.futures import thread
import socket
import threading

port = 4141
host = socket.gethostbyname(socket.gethostname())
addres = (host,port)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(addres)

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(64).decode('utf-8')
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode('utf-8')
            if msg == 'DISCONNECT' :
                connected = False

            print(f"[{addr}] {msg}")

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {host}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client , args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        
print(f"[STARTING THE SERVER]")
start()
