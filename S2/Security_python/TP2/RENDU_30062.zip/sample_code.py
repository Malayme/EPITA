# Decoder de iso-8859-1 en utf-8 HTML
import quopri

encoded_string = "Texte en iso-8859-1"
decoded_html = quopri.decodestring(encoded_string).decode("iso-8859-1")

# Utilisation des templates avec Jinja2 - pip install Jinja2
from jinja2 import Template

# Création de l'object Template à partir du contenu du fichier
with open("template.html", "r", encoding="utf-8") as f:
    template = Template(f.read())

# Compilation de la template avec les données destinataire
rendered_html = template.render(name="Alice", address="1 rue des phishés, 96699 LALALAND")

# Lecture d'un fichier CSV
import csv

with open("data.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["name"], row["age"], row["city"])

