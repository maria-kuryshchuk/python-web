import socket

client = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM,
)

client.connect(
    ("127.0.0.1", 1234)
)

while True:
    client.send(input(":::").encode("utf-8"))

    data = client.recv(2048)
    print(data.decode("utf-8"))
