import socket

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#nouvelle instance créée, AF_INET -> utilise l'IPv4 définit le type d'adresse IP; SOCK_DGRAM -> socket est de type UDP

host = socket.gethostname()
#obtient le nom de l'hôte local, renvoie le nom du réseau ou de la machine

port = 666
#numéro de port sur lequel le client va envoyer et recevoir des données, doit correspondre à celui du serveur auquel on se connecte

print(f"Sending UDP to {host}:{port} ")
#indique le nom de l'hôte et le port auxquels le client va envoyer des données. Le message est formaté avec le nom de l'hôte et le port via l'utilisation de f-strings.

client.sendto(b'Banner query\r\n',(host, port))
#envoie un message en UDP à l'adresse spécifiée par le tuple (host, port), message (en bytes), retour chariot et saut de ligne, (host, port) désigne la destination du message

print(f"Waiting for response...")

message = client.recvfrom(1024)
#méthode recvfrom() est utilisée pour recevoir des données depuis le serveur. 1024 taille maximale du message à recevoir (1024 octets), retourne un tuple contenant le message reçu et l'adresse du serveur. Ce message est stocké dans la variable message

print(f"Received paquet from {host}:{port} : {message}")
#affiche le message reçu du serveur. Elle utilise la même adresse host et port que dans l'envoi, et le message est imprimé sous forme de tuple.

