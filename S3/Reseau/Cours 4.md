Pare-feu de nouvelle generation (NGFW) => controle les applications
VPN GRE => encapsule les protocols de routage
AAA = Authentication Authorization Accounting
IPS => se base sur des signatures
onion de securite => plusieurs couches de securite
VPN site a site => le user ne sait pas qu'il y a un vpn
VPN a distance => le user sait (cyberghost....)
WSA = Web Security Appliance => sert uniquement a bloque les requetes du Web
ESA = E-mail Secutity Appliance => pareil mais pour les mails

## Authentification

**Telnet** : 
R2(config)#enable secret class
R2(config)#line vty 0 4 ==> ligne virtuel, 0 4 = 5 lignes, donc que 5 admin peut acceder a la ligne
R2(config-line)#password cisco
R2(config-line)#login
R2(config-line)#transport input telnet ssh => authorise telnet et ssh sur la ligne

Contact : telnet <[IP]>

**SSH** :
R2(config)#username yann secret yann
R2(config)#ip domain-name epita.lab
R2(config)#crypto key generate rsa modulus 1024
The name for the keys will be: R2.epita.lab

% The key modulus size is 1024 bits
% Generating 1024 bit RSA keys, keys will be non-exportable...[OK]

R2(config)
Mar  1 00:18:15.355: %SSH-5-ENABLED: SSH 1.99 has been enabled
R2(config)#ip ssh version 2
R2(config)#line vty 0 4
R2(config-line)#login local

Contact : #ssh -l yann 192.168.10.2


Config DHCP Server :

ip dhcp excluded-address 192.168.13.254
ip dhcp pool EPITA
network 192.168.13.0 255.255.255.0
default-router 192.168.13.254
dns-server 8.8.8.8 8.8.4.4