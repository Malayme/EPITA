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
