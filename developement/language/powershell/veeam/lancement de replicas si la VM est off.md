

# pour DC1
``` powershell

# Paramètres
$SourceMachine = "DC1"
$Plan = "LaunchDC1"
$SourceMachineIP = "192.168.40.245"
$ReplicationCommand = "Start-ReplicationCommand" # Remplacez par la commande réelle pour démarrer la réplication
$SmtpServer = "copieur.o2switch.net"
$SmtpPort = 26
$SmtpUser = "informatique@assurancesplusfr.sc1caax1193.universe.wf"
$SmtpPassword = "informatique!alertemail"
$EmailFrom = "informatique@assurancesplusfr.sc1caax1193.universe.wf"
$EmailTo = "calaxoservice@gmail.com"
$Subject = "Alerte : La machine $SourceMachine est hors ligne"

# Fonction d'envoi d'alerte par e-mail
function Send-AlertEmail {
    $Body = @"
Bonjour,

La machine source de la réplication ($SourceMachine) est actuellement hors ligne. 
Veuillez vérifier son état et intervenir si nécessaire.

Cordialement,
Votre système
"@
    
    $EmailMessage = @{
        From       = $EmailFrom
        To         = $EmailTo
        Subject    = $Subject
        Body       = $Body
        SmtpServer = $SmtpServer
        Port       = $SmtpPort
        UseSsl     = $true
        Credential = New-Object System.Management.Automation.PSCredential($SmtpUser, (ConvertTo-SecureString $SmtpPassword -AsPlainText -Force))
    }

    Send-MailMessage @EmailMessage
}

# Fonction pour démarrer la réplication
function Start-Replication {
    Write-Output "Démarrage de la réplication pour la machine $SourceMachine..."
	Get-VBRFailoverPlan -Name $Plan | Start-VBRFailoverPlan

    }

# Boucle de vérification toutes les 3 minutes
while ($true) {
    # Tester la connexion à la machine source
    $PingResult = Test-Connection $SourceMachineIP -Count 2 -Quiet

    if ($PingResult -eq $false) {
        Write-Output "La machine $SourceMachine est hors ligne. Envoi d'une alerte..."
        
        # Envoi de l'alerte par e-mail
        Send-AlertEmail

        # Lancer la réplication si la machine est hors ligne
        Start-Replication
    } else {
        Write-Output "La machine $SourceMachine est en ligne. Aucune action nécessaire."
    }

    # Attendre 3 minutes avant de vérifier à nouveau
    Start-Sleep -Seconds 180
}

```
lien vers DC1 via autre reseaux
ip virtuel dans le reseaux emetteur
![[Pasted image 20241209230834.png]]
et nat classique( transfert de port meme si ya pas de port car icmp en dessou niveau osi)


![[Pasted image 20241209230815.png]]

# pour NAS

``` powershell
# Paramètres
$SourceMachine = "NAS"
$Plan = "LaunchNAS"
$SourceMachineIP = "192.168.40.246"
$ReplicationCommand = "Start-ReplicationCommand" # Remplacez par la commande réelle pour démarrer la réplication
$SmtpServer = "copieur.o2switch.net"
$SmtpPort = 26
$SmtpUser = "informatique@assurancesplusfr.sc1caax1193.universe.wf"
$SmtpPassword = "informatique!alertemail"
$EmailFrom = "informatique@assurancesplusfr.sc1caax1193.universe.wf"
$EmailTo = "calaxoservice@gmail.com"
$Subject = "Alerte : La machine $SourceMachine est hors ligne"

# Fonction d'envoi d'alerte par e-mail
function Send-AlertEmail {
    $Body = @"
Bonjour,

La machine source de la réplication ($SourceMachine) est actuellement hors ligne. 
Veuillez vérifier son état et intervenir si nécessaire.

Cordialement,
Votre système
"@
    
    $EmailMessage = @{
        From       = $EmailFrom
        To         = $EmailTo
        Subject    = $Subject
        Body       = $Body
        SmtpServer = $SmtpServer
        Port       = $SmtpPort
        UseSsl     = $true
        Credential = New-Object System.Management.Automation.PSCredential($SmtpUser, (ConvertTo-SecureString $SmtpPassword -AsPlainText -Force))
    }

    Send-MailMessage @EmailMessage
}

# Fonction pour démarrer la réplication
function Start-Replication {
    Write-Output "Démarrage de la réplication pour la machine $SourceMachine..."
	Get-VBRFailoverPlan -Name $Plan | Start-VBRFailoverPlan

    }

# Boucle de vérification toutes les 3 minutes
while ($true) {
    # Tester la connexion à la machine source
    $PingResult = Test-Connection $SourceMachineIP -Count 2 -Quiet

    if ($PingResult -eq $false) {
        Write-Output "La machine $SourceMachine est hors ligne. Envoi d'une alerte..."
        
        # Envoi de l'alerte par e-mail
        Send-AlertEmail

        # Lancer la réplication si la machine est hors ligne
        Start-Replication
    } else {
        Write-Output "La machine $SourceMachine est en ligne. Aucune action nécessaire."
    }

    # Attendre 3 minutes avant de vérifier à nouveau
    Start-Sleep -Seconds 180
}



```
lien vers NAS via autre reseaux


parreil que pour DC1
![[Pasted image 20241209231428.png]]

![[Pasted image 20241209231447.png]]



et dans veeam

![[Pasted image 20241209232408.png]]

faut passer par des failover plan

![[Pasted image 20241209232426.png]]