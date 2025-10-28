import socket

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

hots = socket.gethostname()
port = 444

print("Connection to {host}:{port}...")
client.connect((host, port))
print(f"Connected to {host}:{port}, grabbing header")
message = client.recv(1024)
print(f"Received from {host}:{port}")
client.close()
print(f"Close connection with {host}:{port}")

print("Received from {}:{} : {}".format(host,port,message))


