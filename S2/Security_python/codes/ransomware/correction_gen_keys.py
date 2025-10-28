from Crypto.PublicKey import RSA
import os

CURDIR = os.path.dirname(os.path.realpath(__file__))

#Fonction génère clés RSA
def gen_keys():
    private_key = RSA.generate(2048)

    #Sauvegarde la clé privée
    with open(f"{CURDIR}/key.private", "wb") as private_file:
        private_file.write(private_key.export_key())

    #Extrait clé public
    public_key = private_key.publickey()

    #Sauvegarde clé public
    with open (f"{CURDIR}/key.public", "wb") as public_file:
        public_file.write(public_key.export_key())



