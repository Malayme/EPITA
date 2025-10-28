import socket

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#nouveau socket pour le serveur, socket utilise l'IPv4, utilise le protocole UDP

host = socket.gethostname()
#obtient le nom d'hôte de la machine locale. Cela renvoie le nom du serveur sur lequel le script s'exécute.

port = 666
#serveur est configuré pour écouter sur le port 666

server.bind((host, port))
#serveur "lie" le socket à une adresse et à un port spécifiques en utilisant la méthode bind()

print(f"Running UDP server on {host}:{port}")
#affiche un message indiquant que le serveur UDP est en cours d'exécution sur l'adresse et le port spécifiés

while True: #server en continue
    message, address = server.recvfrom(1024)
    #attend que le serveur reçoive un message UDP,  jusqu'à 1024 octets de données

    print(f"Received UDP from {address} {message}")
    #Une fois le message reçu, cette ligne affiche l'adresse de l'expéditeur ainsi que le contenu du message reçu.

    message = "Hello!\r\n"
    #serveur prépare une réponse

    server.sendto(message.encode('ascii'), address)
    #envoie la réponse préparée au client, Le message "Hello!\r\n" est encodé en bytes avec l'encodage ASCII

    print(f"Sent UDP {address}")
    #ffiche un message indiquant que la réponse a été envoyée au client à l'adresse spécifiée.

