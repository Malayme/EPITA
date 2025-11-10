R1 route par defaut : ip route 0000 0000 s2/0

2 types d'ACL : standard => bloque le reseau
etendu => bloque les services

ACL standard se configure le plus pres possible de la destination :
-  <1-99>            IP standard access list
  <100-199>         IP extended access list
- #access-list 10 permit 192.168.20.0 0.0.0.255 => authorise un reseau
- #access-list 10 deny 192.168.10.0 0.0.0.255 => interdit un reseau
IN/OUT : on veut bloquer l'acces en out selon le reseau voulu
- #int f0/1
- #ip access-group 10 out
- #show access-list
ACL etendu se configure au plus pres de la source :
- access-list 100 deny icmp src+wildcard dest+wildcard
- #access-list 100 permit ip any any => authorise tous les autres
- #int f0/1
- #ip access-group 100 in

## OSPF

- R1(config)#router ospf 10
- #router-id 1.1.1.1
Annoncer les reseaux que le router connait :
- #network 192.168.10.0 0.0.0.255 area 0
faire ca pour tous les routers et leurs reseaux.
si on change l'id :
- clear ip ospf process
Voir les routes ospf : 
- #do show ip ospf neighbor
Diffuser la route par defaut qui va sur internet
- #default information originate
Configure la NAT sur le routeur de peripherique :
- R1(config)#router ospf 10
R1(config-router)#passive-interface f0/0
R1(config-router)#passive-interface default
R1(config-router)#
R1(config-router)#no passive-interface s2/0


- #access-list 10 permit any
- #ip nat inside source list 10 int  f0/0 overload
- #int s2/0
R2(config-if)#ip nat inside
R2(config-if)#exit
R2(config)#int s2/1
R2(config-if)#ip nat inside
R2(config-if)#exit
R2(config)#int f0/0
R2(config-if)#op nat outside
