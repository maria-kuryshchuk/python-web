import socket
from datetime import datetime

server = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM,

)
print('Starting the SERVER at', datetime.now())

server.bind(
    ("127.0.0.1", 1234)  #localhost

)

server.listen(5)
print("Server is listening")

while True:
    user_socket, address = server.accept()
    print(f"User {user_socket} connected!")

    data = user_socket.recv(2048)
    print(data.decode("utf-8"))

    user_socket.send("You are connected".encode("utf-8"))

