import socket

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

print(f"Connecting to {host} on port {port}...")
client.connect((host, port))
print(f"Connected to {host} on port {port}, grabbing header")
message = client.recv(1024)
print(f"Received from: {host}:{port}")
client.close()
print(f"Closed connection with {host}:{port}")

print("Received from {}:{}:{}".format(host, port, message))
