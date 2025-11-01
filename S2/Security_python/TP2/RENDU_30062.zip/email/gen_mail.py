import os
import re
from jinja2 import Template
import csv

def re_encode(file_path):
    #fichier en mode binaire
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    
    #encodage iso-8859-1
    decoded_data = binary_data.decode('iso-8859-1')
    
    #extension .html
    base_name, _ = os.path.splitext(file_path)
    new_file_path = f"{base_name}.html"
    
    #sauvegarde
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.write(decoded_data)

    print(f"Encodage réussi à : {new_file_path}")

def fix_links(file_path, phishing_url, commande_id):
    # Lis fichier
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    #Jinja2 ????
    new_link = f'{phishing_url}?commande={{ commande_id }}'
    
    # Remplacement des liens
    nv_liens = re.sub(r'href="[^"]*"', f'href="{new_link}"', content)
    
    # Remplacer les informations statiques par des variables Jinja2
    nv_liens = nv_liens.replace("Dupond et Dupont", "{{ destinataires }}")
    nv_liens = nv_liens.replace("82 ALLEE DES FLEURS ETAGE 1 – 96969 VALHALLA", "{{ adresse }}")
    nv_liens = nv_liens.replace("FR123456789AB", "{{ commande_id }}")
    
    # Sauvegarde
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(nv_liens)

    print(f"Changement liens à : {file_path}")

def generate_email(file_path, client_data):
    # Lis fichier
    with open(file_path, 'r', encoding='utf-8') as file:
        template_content = file.read()
    
    # Compilation Jinja 2 ???
    template = Template(template_content)
    email_content = template.render(
        destinataires=client_data.get("destinataires"),
        adresse=client_data.get("adresse"),
        commande_id=client_data.get("commande_id"),
        phishing_url=f"{client_data.get('phishing_url')}?commande={client_data.get('commande_id')}"
    )
    
    return email_content

def generate_phishing_emails(csv_path, template_path, output_dir):
    #répertoire de sortie s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)
    
    #template
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()
    template = Template(template_content)
    
    #fichier CSV
    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            #données de la cible
            destinataires = row.get("destinataires")
            adresse = row.get("adresse")
            commande_id = row.get("commande_id")
            phishing_url = row.get("phishing_url")
            
            #contenu de l'email
            email_content = template.render(
                destinataires=destinataires,
                adresse=adresse,
                commande_id=commande_id,
                phishing_url=f"{phishing_url}?commande={commande_id}"
            )
            
            # Sauvegarde
            output_file_path = os.path.join(output_dir, f"{destinataires.replace(' ', '_')}.html")
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(email_content)
            
            print(f"Email généré pour {destinataires} : {output_file_path}")

