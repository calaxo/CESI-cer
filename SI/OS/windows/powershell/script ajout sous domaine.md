
#
# Script Windows PowerShell pour le déploiement d’AD DS
#

Import-Module ADDSDeployment
Install-ADDSDomain `
-NoGlobalCatalog:$false `
-CreateDnsDelegation:$true `
-Credential (Get-Credential) `
-DatabasePath "C:\Windows\NTDS" `
-DomainMode "WinThreshold" `
-DomainType "ChildDomain" `
-InstallDns:$true `
-LogPath "C:\Windows\NTDS" `
-NewDomainName "dingue" `
-NewDomainNetbiosName "DINGUE" `
-ParentDomainName "zinzin.main.fr" `
-NoRebootOnCompletion:$false `
-SiteName "dingue" `
-SysvolPath "C:\Windows\SYSVOL" `
-Force:$true


