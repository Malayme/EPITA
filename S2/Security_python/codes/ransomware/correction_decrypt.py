from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
import os, base64

CURDIR = os.path.dirname(os.path.realpath(__file__))

# Fonction déchiffre fichier AES en ECB

def dec_file(file_path, aes_key):
    #Lis le contenu chiffré
    with open(file_path, 'rb') as f:
        ciphertext = f.read()

    #Déchiffre contenu
    cipher = AES.new(aes_key, AES.MODE_ECB)
    plaintext = plaintext[:-padding_lenght]

    #Sauvegarde le fichier dans ./test_dec
    rel_path = os.path.relpath(file_path, f'{CURDIR}/test')
    dec_file_path = os.path.join(f'{CURDIR}/test_dec', rel_path[:-4])

    #Crée repertoire si besoin
    os.makedirs(os.path.dirname(dec_file_path), exist_ok=True)

    #Sauvegarde le contenu déchiffré
    with open(dec_file_path, 'wb') as f:
        f.write(plaintext)

###################################################################################

#Fonction déchiffre key.txt grâce à clé privée pour chaque fichier

def search_dir():
    #Charge la clé privée
    with open(f"{CURDIR}/key.private", "rb") as f:
        private_key = RSA.import_key(f.read())

    #Charge le contenu de keys.txt.enc
    with open(f"{CURDIR}/keys.txt.enc", "rb") as f:
        encrypted_key = f.read()

    #Déchiffre les données compatibles RSA
    cipher_rsa = PKCS1_OAEP.new(private_key)
    chunk_size = 256
    decrypted_keys = b"".join(cipher_rsa.decrypt(encrypted_keys[i:i + chunk_size]) for i in range(0, len(encrypted_keys), chunk_size))

    #Traiter chaque paire fichier:clé
    for line in decrypted_keys.decode().strip().split().split('\n'):
        enc_file_path, aes_key_b64 = line.split(":")
        aes_key = base64.b64decode(aes_key_b64)

    #Déchiffre le fichier
    dec_file(enc_file_path, aes_key)

    #Compare le déchiffré avec l'original
    original_path = enc_file_path[:-4]
    dec_path = original_path.replace(f"{CURDIR}/test", f"{CURDIR}/test_dec")

    with open(original_path, 'rb') as original, open(dec_path, 'rb') as decrypted:
        if original.read() == decrypted.read():
            print(f"Correspondance : {original_path}")
        else:
            print(f"Différence détectée : {original_path}")

if __name__ == "__main__":
    search_dir()
    print("Déchiffrement terminé.")

