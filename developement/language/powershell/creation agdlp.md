
``` powershell

# Importer le module Active Directory si nécessaire

# Import-Module ActiveDirectory

  

# Définir les informations de base pour votre domaine

$BaseDN = "DC=dingue,DC=main,DC=fr"

  

# Fonction pour créer une OU si elle n'existe pas

function Create-OU {

    param (

        [string]$OUName,

        [string]$ParentPath

    )

    $OUPath = "OU=$OUName,$ParentPath"

    if (-not (Get-ADOrganizationalUnit -Filter "Name -eq '$OUName'" -SearchBase $ParentPath -ErrorAction SilentlyContinue)) {

        New-ADOrganizationalUnit -Name $OUName -Path $ParentPath

        Write-Host "OU '$OUName' créée sous '$ParentPath'."

    } else {

        Write-Host "OU '$OUName' existe déjà sous '$ParentPath'."

    }

    return $OUPath

}

  

# Fonction pour créer un groupe si nécessaire

function Create-Group {

    param (

        [string]$GroupName,

        [string]$ParentOU

    )

    $GroupPath = "$ParentOU"

    if (-not (Get-ADGroup -Filter "Name -eq '$GroupName'" -SearchBase $ParentOU -ErrorAction SilentlyContinue)) {

        New-ADGroup -Name $GroupName -GroupScope Global -GroupCategory Security -Path $GroupPath

        Write-Host "Groupe '$GroupName' créé dans '$ParentOU'."

    } else {

        Write-Host "Groupe '$GroupName' existe déjà dans '$ParentOU'."

    }

}

  

# Créer l'OU principale AGDLP

$OUAGDLP = Create-OU -OUName "AGDLP" -ParentPath $BaseDN

  

# Créer l'OU pour les Groupes sous AGDLP

$OUGroupes = Create-OU -OUName "Groupes" -ParentPath $OUAGDLP

  

# Créer des groupes de sécurité sous l'OU Groupes

$GroupNames = @(

    "Grp-Service-Client",

    "Grp-Service-Commerce",

    "Grp-Service-Sinistres",

    "Grp-Service-Juridique",

    "Grp-Direction-Agence"

)

  

foreach ($GroupName in $GroupNames) {

    Create-Group -GroupName $GroupName -ParentOU $OUGroupes

}

  

# Créer l'OU pour les Utilisateurs sous AGDLP

$OUUtilisateur = Create-OU -OUName "Utilisateur" -ParentPath $OUAGDLP

  

# Créer des sous-OUs pour les utilisateurs

Create-OU -OUName "Administrateurs" -ParentPath $OUUtilisateur

Create-OU -OUName "Usr-Service-Client" -ParentPath $OUUtilisateur

Create-OU -OUName "Usr-Service-Commerce" -ParentPath $OUUtilisateur

Create-OU -OUName "Usr-Service-Sinistres" -ParentPath $OUUtilisateur

Create-OU -OUName "Usr-Service-Juridique" -ParentPath $OUUtilisateur

Create-OU -OUName "Usr-Direction-Agence" -ParentPath $OUUtilisateur

  

# Créer l'OU pour les Ressources sous AGDLP

$OURessource = Create-OU -OUName "Ressource" -ParentPath $OUAGDLP

  

# Créer des sous-OUs pour les ressources

$OUFldrServiceClient = Create-OU -OUName "Fldr-Service-Client" -ParentPath $OURessource

$OUFldrServiceCommerce = Create-OU -OUName "Fldr-Service-Commerce" -ParentPath $OURessource

$OUFldrServiceSinistres = Create-OU -OUName "Fldr-Service-Sinistres" -ParentPath $OURessource

$OUFldrServiceJuridique = Create-OU -OUName "Fldr-Service-Juridique" -ParentPath $OURessource

$OUFldrDirectionAgence = Create-OU -OUName "Fldr-Direction-Agence" -ParentPath $OURessource

  

# Fonction pour créer des droits spécifiques dans les ressources

function Create-Rights {

    param (

        [string]$BaseName,

        [string]$ParentOU

    )

    $Rights = @("Ecriture", "Lecture", "Modification")

    foreach ($Right in $Rights) {

        Create-Group -GroupName "Droit-$BaseName-$Right" -ParentOU $ParentOU

    }

}

  

# Créer des droits dans les ressources

Create-Rights -BaseName "Service-Client" -ParentOU $OUFldrServiceClient

Create-Rights -BaseName "Service-Commerce" -ParentOU $OUFldrServiceCommerce

Create-Rights -BaseName "Service-Sinistres" -ParentOU $OUFldrServiceSinistres

Create-Rights -BaseName "Juridique" -ParentOU $OUFldrServiceJuridique

Create-Rights -BaseName "Direction" -ParentOU $OUFldrDirectionAgence

  

# Créer une OU Ordinateurs au niveau racine (hors AGDLP)

$OUOrdinateurs = Create-OU -OUName "Ordinateurs" -ParentPath $BaseDN

Create-OU -OUName "Portables" -ParentPath $OUOrdinateurs

Create-OU -OUName "Fix" -ParentPath $OUOrdinateurs

$OUServeurs = Create-OU -OUName "Serveurs" -ParentPath $OUOrdinateurs

Create-OU -OUName "AD" -ParentPath $OUServeurs

Create-OU -OUName "Autre" -ParentPath $OUServeurs

  

Write-Host "Arborescence AD créée avec succès."

```

créée grace a 
[[boucle user active directory]]