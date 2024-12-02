
![[Pasted image 20241122162729.png]]


``` powershell
# Importer le module Active Directory si nécessaire
# Import-Module ActiveDirectory

# Définir le chemin de l'OU (unité d'organisation)
$OUPath = "OU=utilisateur,OU=Domain Controllers,DC=zinzin,DC=main,DC=fr"

# Créer l'OU IT si elle n'existe pas déjà
if (-not (Get-ADOrganizationalUnit -Filter "Name -eq 'IT'" -SearchBase "OU=utilisateur,OU=Domain Controllers,DC=zinzin,DC=main,DC=fr" -ErrorAction SilentlyContinue)) {
    New-ADOrganizationalUnit -Name "IT" -Path "OU=utilisateur,OU=Domain Controllers,DC=zinzin,DC=main,DC=fr"
    Write-Host "OU 'IT' créée avec succès."
} else {
    Write-Host "L'OU 'IT' existe déjà."
}

# Mot de passe pour les utilisateurs
$password = ConvertTo-SecureString "Password!" -AsPlainText -Force

# Liste des utilisateurs à créer
$users = @(
    @{GivenName="Ada"; Surname="Lovelace"; SamAccountName="ada.lovelace"},
    @{GivenName="James"; Surname="Gosling"; SamAccountName="james.gosling"},
    @{GivenName="Margaret"; Surname="Hamilton"; SamAccountName="margaret.hamilton"},
    @{GivenName="Alan"; Surname="Turing"; SamAccountName="alan.turing"}
)

# Boucle pour créer les utilisateurs
foreach ($user in $users) {
    $userFullName = "$($user.GivenName) $($user.Surname)"
    
    # Vérifier si l'utilisateur existe déjà
    if (-not (Get-ADUser -Filter "SamAccountName -eq '$($user.SamAccountName)'" -ErrorAction SilentlyContinue)) {
        New-ADUser `
            -GivenName $user.GivenName `
            -Surname $user.Surname `
            -SamAccountName $user.SamAccountName `
            -UserPrincipalName "$($user.SamAccountName)@example.com" `
            -Name $userFullName `
            -Path $OUPath `
            -AccountPassword $password `
            -Enabled $true `
            -PasswordNeverExpires $false `
            -ChangePasswordAtLogon $false

        Write-Host "Utilisateur $userFullName créé avec succès."
    } else {
        Write-Host "L'utilisateur $userFullName existe déjà."
    }
}

```


``` powershell
clear-host;
$comptes = Import-Csv -Path "C:\liste.csv"
foreach ($compte in $comptes)
{
$Displayname = $compte.Prenom + " " + $compte.Nom
$UserFirstname = $compte.Prenom
$UserLastname = $compte.Nom
$SAM = $compte.SAM
$UPN = $compte.SAM + "@" + $compte.Domaine
$Password = $compte.Password
$OU = "OU=Utilisateurs,DC=mondomaine,DC=local"
New-ADUser -Name "$Displayname" -DisplayName "$Displayname" -SamAccountName $SAM -UserPrincipalName $UPN -GivenName "$UserFirstname" -Surname "$UserLastname" -AccountPassword (ConvertTo-SecureString $Password -AsPlainText -Force) -Enabled $true -Path "$OU" -ChangePasswordAtLogon $false –PasswordNeverExpires $true -server mondomaine.local
}
```



