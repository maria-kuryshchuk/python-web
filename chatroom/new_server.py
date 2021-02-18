import threading
import socket

host = 'localhost'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicknames = []

def broadcast(message): #message to all participants
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = client.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f' {nickname} left the chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break
def recieve():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('MARIIA'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        clients.append(client)

        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joined the chat!'.encode('utf-8'))
        client.send('Connected to the server'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening.....")
recieve()