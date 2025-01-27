
$NewComputerName = "NAS"  # Remplacez par le nom souhaité
$DomainName = Read-Host "quel est le domaine a rejoindre"   # Remplacez par le nom de domaine
$DomainUser =  Read-Host "identifiant admin du domaine:"        # Remplacez par un utilisateur du domaine
$DomainPassword =  Read-Host "mot de passe admin"  # Remplacez par le mot de passe

Write-Host "Renommage du PC en $NewComputerName..." -ForegroundColor Yellow
Rename-Computer -NewName $NewComputerName -Force -Restart

Write-Host "Ajout au domaine $DomainName..." -ForegroundColor Yellow
Add-Computer -DomainName $DomainName -Credential (New-Object System.Management.Automation.PSCredential("$DomainUser", (ConvertTo-SecureString "$DomainPassword" -AsPlainText -Force))) -Force -Restart

# Activer la fonctionnalité de partage de fichiers
Write-Host "Activation de la fonctionnalité de partage de fichiers..." -ForegroundColor Yellow
Install-WindowsFeature -Name FS-FileServer

# Création du dossier partagé
$SharedFolder = "C:\PARTAGE"
if (-not (Test-Path $SharedFolder)) {
    Write-Host "Création du dossier de partage : $SharedFolder" -ForegroundColor Yellow
    New-Item -Path $SharedFolder -ItemType Directory
}

# Configuration du partage
Write-Host "Configuration du partage $SharedFolder..." -ForegroundColor Yellow
New-SmbShare -Name "PARTAGE" -Path $SharedFolder -FullAccess Everyone
Write-Host "Partage $SharedFolder configuré avec succès !" -ForegroundColor Green






