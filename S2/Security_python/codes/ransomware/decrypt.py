import os
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA

def unpad(data):
    
    return data.rstrip(b"\0")

def dec_file(file_path, aes_key):
   
    output_dir = "./test_dec"
    os.makedirs(output_dir, exist_ok=True)  # Crée le dossier s'il n'existe pas

    # Construire le chemin de sortie en supprimant .enc et en mettant dans test_dec
    filename = os.path.basename(file_path).replace(".enc", "")
    output_file = os.path.join(output_dir, filename)

    # Lire le fichier chiffré
    with open(file_path, "rb") as f:
        ciphertext = f.read()

    # Déchiffrement AES
    cipher = AES.new(bytes.fromhex(aes_key), AES.MODE_ECB)  # ECB utilisé ici
    plaintext = unpad(cipher.decrypt(ciphertext))

    # Sauvegarde du fichier déchiffré
    with open(output_file, "wb") as f:
        f.write(plaintext)

    print(f"Déchiffré : {file_path} → {output_file}")
    return output_file

def decrypt_keys_file(keys_file_enc):
    
    if not os.path.exists("key.private"):
        print("Erreur : Clé privée 'key.private' introuvable.")
        return None

    # Charger la clé privée RSA
    with open("key.private", "rb") as f:
        private_key = RSA.import_key(f.read())

    cipher_rsa = PKCS1_OAEP.new(private_key)

    # Lire et déchiffrer keys.txt.enc
    with open(keys_file_enc, "rb") as f:
        encrypted_keys = f.read()

    decrypted_keys = cipher_rsa.decrypt(encrypted_keys).decode()

    return decrypted_keys.splitlines()

def compare_files(file1, file2):
    """Compare deux fichiers et indique s'ils sont identiques"""
    with open(file1, "rb") as f1, open(file2, "rb") as f2:
        return f1.read() == f2.read()

def search_dir():
    """Déchiffre tous les fichiers à partir de keys.txt.enc"""
    keys_file_enc = "keys.txt.enc"
    
    # Déchiffrer keys.txt.enc pour obtenir les clés AES
    decrypted_pairs = decrypt_keys_file(keys_file_enc)
    if decrypted_pairs is None:
        return
    
    for pair in decrypted_pairs:
        file_path, aes_key = pair.split(":")
        
        # Vérifier si le fichier chiffré existe
        if os.path.exists(file_path):
            decrypted_file = dec_file(file_path, aes_key)

            # Comparaison avec l'original s'il existe encore
            original_file = file_path.replace(".enc", "")
            if os.path.exists(original_file):
                if compare_files(original_file, decrypted_file):
                    print(f" Fichiers identiques : {original_file} et {decrypted_file}")
                else:
                    print(f"Différence détectée entre : {original_file} et {decrypted_file}")