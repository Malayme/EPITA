Yann Lemaire-Suau & Ange-Olivier Johnson
Cyber 2 - B

## Schema de l'architecture
![[Architecture-Projet.png]]


## Script de creation des utilisateurs :
```
# ==========================================
# --- SECTION CONFIGURATION ---
# ==========================================

# 1. Chemin absolu vers le fichier CSV source.
# IMPORTANT : Assurez-vous que le compte qui exécute le script a les droits de lecture sur ce fichier.
$CheminCSV = "C:\Users\Administrateur\ADUsers.csv"

# 2. Racine de l'OU où les sous-OU départementales sont situées.
# Les utilisateurs seront créés dans OU=Department,OU=Paris,...
$RacineParisDN = "OU=Paris,DC=fra,DC=company,DC=corp"

# 3. Configuration du mot de passe initial.
# Active Directory exige que les mots de passe soient passés sous forme de "SecureString".
$MotDePasseClair = "TempP@ssword!2025!"
# Conversion de la chaîne claire en chaîne sécurisée.
$SecurePassword = ConvertTo-SecureString $MotDePasseClair -AsPlainText -Force

# 4. Définition du séparateur utilisé dans le fichier CSV.
# Si votre CSV utilise des points-virgules, changez "," en ";" ici.
$Delimiteur = "," 

# ==========================================
# --- IMPORT DES MODULES ET DÉMARRAGE ---
# ==========================================

# Charge le module nécessaire pour interagir avec Active Directory.
# Nécessite les outils RSAT installés.
Import-Module ActiveDirectory

Write-Host "--- Début du processus de création des utilisateurs PARIS (V5 Final) ---" -ForegroundColor Cyan
Write-Host "Lecture du fichier CSV : $CheminCSV"
Write-Host "Délimiteur utilisé : [$Delimiteur]"

# ==========================================
# --- TRAITEMENT DU FICHIER CSV ---
# ==========================================
# Cette section utilise une méthode robuste pour lire les CSV générés par Excel
# qui ont souvent des problèmes d'encodage avec les accents français.

try {
    # Vérification basique de l'existence du fichier.
    if (-not (Test-Path $CheminCSV)) { throw "Le fichier n'existe pas au chemin indiqué." }

    # --- GESTION DE L'ENCODAGE ---
    # On force l'utilisation de l'encodage "Windows-1252" (ANSI).
    # Import-Csv standard échoue souvent à lire correctement les accents (é, è, ç)
    # si le fichier n'est pas en UTF-8 parfait. Cette méthode contourne le problème.
    $Encoding1252 = [System.Text.Encoding]::GetEncoding(1252)
    # Lecture de tout le contenu texte du fichier avec cet encodage spécifique.
    $ContenuBrut = [System.IO.File]::ReadAllText($CheminCSV, $Encoding1252)

    # --- CONVERSION CSV ---
    # On transforme le texte brut en objets PowerShell en utilisant le délimiteur spécifié.
    $ListeUtilisateurs = $ContenuBrut | ConvertFrom-Csv -Delimiter $Delimiteur

    # Vérification si le fichier est vide ou mal lu.
    if ($ListeUtilisateurs.Count -eq 0) { throw "Le fichier semble vide ou aucune donnée n'a été extraite." }
    Write-Host "Lecture réussie. $($ListeUtilisateurs.Count) lignes de données trouvées." -ForegroundColor Gray

    # --- DIAGNOSTIC DE STRUCTURE ---
    Write-Host "`n--- VÉRIFICATION DES COLONNES ---" -ForegroundColor Yellow
    
    # On vérifie uniquement la présence de la colonne 'City' qui est cruciale pour notre filtre principal.
    # Si Import-Csv a échoué à cause d'un mauvais délimiteur, les propriétés n'existeront pas.
    # On regarde la première ligne ([0]) pour voir les propriétés détectées.
    if (-not $ListeUtilisateurs[0].PSObject.Properties['City']) {
         Write-Error "ERREUR CRITIQUE : La colonne 'City' est introuvable dans les entêtes du CSV."
         Write-Host "Causes possibles : Le délimiteur '$Delimiteur' est incorrect, ou le nom de la colonne dans le CSV n'est pas exactement 'City'." -ForegroundColor Yellow
         # On arrête tout si la structure est mauvaise.
         break
    }
    Write-Host "Vérification OK : La colonne 'City' est bien détectée." -ForegroundColor Green
    Write-Host "Le script va poursuivre le traitement." -ForegroundColor Gray
    Write-Host "----------------------`n"

}
catch {
    # Capture des erreurs globales de lecture de fichier (fichier verrouillé, disque plein, etc.)
    Write-Error "ARRÊT DU SCRIPT LORS DE LA LECTURE DU FICHIER."
    Write-Host "Détails : $($_.Exception.Message)" -ForegroundColor Red
    # Arrêt complet du script.
    break
}

# ==========================================
# --- BOUCLE PRINCIPALE DE CRÉATION ---
# ==========================================

# Initialisation des compteurs pour le rapport final.
$CompteurCrees = 0; $CompteurIgnores = 0; $CompteurErreurs = 0

# On itère sur chaque ligne importée du CSV.
foreach ($Utilisateur in $ListeUtilisateurs
```


## Etape 1
Mise en place de l'adresse IP et de la foret parent 1.
Creation de la foret :
![[Pasted image 20251124144545.png]]
IP de la machine parent "New York":
![[Pasted image 20251124143903.png]]

Le ping depuis la machine hote de la VM: 
![[Pasted image 20251124143755.png]]
## Etape 2
Creation des OU de departement :
![[Pasted image 20251124152440.png]]
Creation des OUs Groupes, Ordinateurs, Utilisateurs dans chaque departement :
![[Pasted image 20251124160734.png]]
Le script : 
```
# Importation du module Active Directory
Import-Module ActiveDirectory

# 1. Définir le chemin de l'OU parente des départements
# REMPLACER 'DC=votredomaine,DC=local' par le DistinguishedName de votre domaine.
$ParentOUPath = "OU=New-York,DC=company,DC=corp"

# 2. Définir les noms des sous-OUs à créer
$SubOUNames = @("Utilisateurs", "Groupes", "Ordinateurs")

# 3. Récupérer toutes les OUs de département sous 'New-York'
# -SearchScope OneLevel assure de ne prendre que les OUs immédiatement sous 'New-York'
try {
    $DepartmentOUs = Get-ADOrganizationalUnit -Filter * -SearchBase $ParentOUPath -SearchScope OneLevel -ErrorAction Stop
}
catch {
    Write-Error "Impossible de récupérer les OUs sous $ParentOUPath. Vérifiez que le chemin est correct et que le module ActiveDirectory est chargé."
    exit 1
}

if ($DepartmentOUs.Count -eq 0) {
    Write-Warning "Aucune OU de département trouvée sous $ParentOUPath."
    exit 0
}

# 4. Parcourir chaque OU de département et créer les sous-OUs
foreach ($DepartmentOU in $DepartmentOUs) {
    $DepartmentOUName = $DepartmentOU.Name
    $DepartmentOUDN = $DepartmentOU.DistinguishedName

    Write-Host "Traitement de l'OU de département: $($DepartmentOUName)..."

   # ... (Code précédent inchangé jusqu'ici)

# 4. Parcourir chaque OU de département et créer les sous-OUs
foreach ($DepartmentOU in $DepartmentOUs) {
    $DepartmentOUName = $DepartmentOU.Name
    $DepartmentOUDN = $DepartmentOU.DistinguishedName

    Write-Host "Traitement de l'OU de département: $($DepartmentOUName)..."

    # Boucle pour créer chaque sous-OU (Utilisateurs, Groupes, Ordinateurs)
    foreach ($SubOUName in $SubOUNames) {
        $NewOUPath = "OU=$SubOUName,$DepartmentOUDN"

        # Tenter de récupérer la sous-OU. Si elle n'existe pas, l'erreur est silencieuse.
        # On utilise une variable pour éviter d'imprimer l'objet AD si trouvé.
        $ExistingOU = $null
        try {
            # Tente de récupérer l'OU. Si elle n'existe pas, une erreur est générée.
            $ExistingOU = Get-ADOrganizationalUnit -Identity $NewOUPath -ErrorAction Stop
        }
        catch {
            # Si on arrive ici, l'OU n'existe PAS, ce qui est normal lors de la première exécution.
            # Le bloc catch est exécuté, mais ne fait rien.
        }

        # La variable $ExistingOU est $null si l'OU n'existe pas (grâce au catch)
        if ($ExistingOU -eq $null) {
            try {
                # Créer la nouvelle sous-OU
                New-ADOrganizationalUnit -Name $SubOUName -Path $DepartmentOUDN -ProtectedFromAccidentalDeletion $true -ErrorAction Stop

                Write-Host "   -> Sous-OU '$($SubOUName)' créée avec succès." -ForegroundColor Green
            }
            catch {
                Write-Error "   -> ERREUR lors de la création de '$($SubOUName)' dans '$($DepartmentOUName)': $($_.Exception.Message)" -ForegroundColor Red
            }
        } else {
            Write-Host "   -> Sous-OU '$($SubOUName)' existe déjà. Ignorée." -ForegroundColor Yellow
        }
    }
    Write-Host "---"
    }
}

Write-Host "Script terminé."
```
Creation des Utilisateurs dans les OUs:
Troubleshooting: le fichier contenait des utilisateurs avec "New York" et "New-York" ce qui cree un conflit, dans notre script. Nous avons modifier le fichier .csv en remplacant tout ceux avec "New-York" par "New York".

Pour verifier que dans les OUs on faisait cette commande :
``cat ADUsers.csv | grep 'Gestion de projet' | grep "New York" | wc -l`` (exemple pour l'OU Gestion de projet a New York) qui nous a retourne 30.

Et lorsque l'on verifie en voulant tous les supprimes :
![[Pasted image 20251126144617.png]]

## Poste Client
On configure l'adresse IP : 
![[Pasted image 20251126150337.png]]On se connecte avec l'utilisateur "alanb":
![[Pasted image 20251126151450.png]]
## GPO
Politique de Complexité des Mots de Passe : 
La longueur :
![[Pasted image 20251126152535.png]]
Complexite : 
![[Pasted image 20251126152610.png]]

Verrouillage de l'ecran automatique : 
Activation:
![[Pasted image 20251126152949.png]]
Protection de l'ecran de veille par un mot de passe :
![[Pasted image 20251126153054.png]]
Delai de l'ecran de veille (600 secondes car $10*60 = 600$) :
![[Pasted image 20251126154033.png]]
Puis on lie nos GPO  a notre domaine :
![[Pasted image 20251126154142.png]]
## Partage Reseau :

On cree le dossier :
![[Pasted image 20251126161301.png]]
Creation du groupe Marketing dans l'OU Marketing:
![[Pasted image 20251126162744.png]]

Configuration : 
On configure un partage en SMB Rapide :![[Pasted image 20251126161503.png]]
Le chemin : 
![[Pasted image 20251126161703.png]]
Notre chemin distant d'acces au partage est : \\DC\Marketing_Campaigns

Configuration pour que le groupe Marketing ait les droits de modifications:
![[Pasted image 20251126162931.png]]

On a bien notre chemin distant sur notre poste client : 
![[Pasted image 20251126163155.png]]

Creation du dossier "Public":
![[Pasted image 20251126163246.png]]
Le groupe "Utilisateurs du domaine" est un builtin donc nous avons pas besoin de le creer.
On repete les etapes precedentes de partage et de tache en selectionnant le bon dossier.
Notre chemin distant est :  \\DC\public
On met les bonnes autorisations : ![[Pasted image 20251126163833.png]]
On verifie sur notre poste de travail :
![[Pasted image 20251126163918.png]]

## GPO "Drive_Mappings"

Creation de la GPO pour l'OU Marketing :
![[Pasted image 20251126164519.png]]
Configuration de la GPO :
On map les differents lecteurs : 
Pour Public :
![[Pasted image 20251126165117.png]]
Pour Marketing_Campaigns :
![[Pasted image 20251126165310.png]]

On configure le fait que l'utilisateur doit etre dans le groupe Marketing:

![[Pasted image 20251126165558.png]]
On voit bien alors tous les mappages : 
![[Pasted image 20251126165644.png]]

## DNS
On configure le DNS pour rediriger vers prestataire.ext et inversement (on fait les meme etapes pour les deux, seul le nom et l'adresse changent):
![[Pasted image 20251126170338.png]]

![[Pasted image 20251126170401.png]]
On peut maintenant verifier avec un ping : 
![[Pasted image 20251126170648.png]]
## Relation d'approbation
On cree une nouvelle approbation : ![[Pasted image 20251126170930.png]]
![[Pasted image 20251126171031.png]]
![[Pasted image 20251126171042.png]]
On choisit "domaine specifie" car on connait les identifiants des deux domaines :
![[Pasted image 20251126171136.png]]
On gagne du temps en ne specifiant pas : ![[Pasted image 20251126171336.png]]
## RODC

On connecte notre serveur RODC a notre domaine company.corp : 
![[Pasted image 20251128104224.png]]

On pre-cree le compte :
![[Pasted image 20251128104529.png]]
On a bien pre-cree le groupe :
![[Pasted image 20251128105809.png]]
On configure la Politique de Réplication des Mots de Passe : ![[Pasted image 20251128110014.png]]
On voit bien que les comptes administrateurs sont refuses : 
![[Pasted image 20251128110304.png]]
Et que les utilisateurs de Marketing sont autorises :
![[Pasted image 20251128111008.png]]

On ajoute notre RODC a notre domaine New York : 
![[Pasted image 20251128112417.png]]
On coche la case pour etre en RODC :
![[Pasted image 20251128112541.png]]
## Verification :
On se connecte avec un utilisateur de Paris sur le poste client : ![[Pasted image 20251128120056.png]]
![[aaronp.png]]

