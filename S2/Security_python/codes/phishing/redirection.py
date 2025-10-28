import re

def remplacer_liens(fichier_entree, fichier_sortie, lien_malicious="malware.php"):
    with open(fichier_entree, "r", encoding="utf-8") as f:
        contenu = f.read()

    pattern = r'https?://[\w./-]+'

    contenu_modifie = re.sub(pattern, lien_malicious, contenu)

    with open(fichier_sortie, "w", encoding="utf-8") as f:
        f.write(contenu_modifie)

    print("Liens remplacés dans {fichier_sortie}")

remplacer_liens("input.html", "output.html")
