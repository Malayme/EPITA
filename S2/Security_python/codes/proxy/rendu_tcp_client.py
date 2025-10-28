import socket


def tcp_client(port):
    open_ = 0
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    host = socket.gethostname()
    test = client.connect_ex((host, port))
    if test == 0:
        open_ = 1
    else:
        open_ = 0
        print('Port:',port, 'is closed')

    if (open_ == 1):
        print(f"Connection to {host}:{port}...")
        print(f"Connected to {host}:{port}, grabbing header")
        message = client.recv(1024)
        print(f"Received from {host}:{port}")
        client.close()
        print(f"Closed connection with {host}:{port}")

        print("Received from {}:{} : {}".format(host, port, message))


port = [777, 555, 444, 333]

for i in port:
    tcp_client(i)
