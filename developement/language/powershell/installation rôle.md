
``` powershell 


# Démarrer la VM
Start-VM -Name $vm_name
Write-Host "Starting the VM..." -ForegroundColor Yellow
Start-Sleep -Seconds 30  # Temps d'attente pour démarrer

# Configurer les rôles via PowerShell Direct
$domain_name = Read-Host "Entrez le nom du domaine à configurer"
$vm_session = New-PSSession -VMName $vm_name -Credential (Get-Credential)

Invoke-Command -Session $vm_session -ScriptBlock {
    Write-Host "Installing roles..." -ForegroundColor Yellow

    # Installation des rôles
    Install-WindowsFeature -Name DHCP -IncludeManagementTools
    Install-WindowsFeature -Name DNS -IncludeManagementTools
    Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
    Install-WindowsFeature -Name Print-Server

    Write-Host "Roles installed successfully." -ForegroundColor Green

    # Configuration du contrôleur de domaine
    $domainName = $using:domain_name
    Install-ADDSForest -DomainName $domainName -InstallDns -SafeModeAdministratorPassword (ConvertTo-SecureString "P@ssword123" -AsPlainText -Force) -Force
    Write-Host "Domain configured successfully." -ForegroundColor Green
}

Remove-PSSession $vm_session
Write-Host "Configuration completed!" -ForegroundColor Green


```




ca marche comment New PSSession en powershell notament pour executer du code dans dees VM

