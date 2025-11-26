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