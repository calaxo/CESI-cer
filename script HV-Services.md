Rename-Computer -NewName "HV-Services" -Force 

dism /online /enable-feature /featureName:SNMP /featureName:WMISnmpProvider

$regPath = "HKLM:\SYSTEM\CurrentControlSet\Services\SNMP\Parameters\ValidCommunities"
if (-not (Test-Path $regPath)) {
    New-Item -Path "HKLM:\SYSTEM\CurrentControlSet\Services\SNMP\Parameters" -Name "ValidCommunities"
}
Set-ItemProperty -Path $regPath -Name "trklsnMP16!" -Value 4

$ipPermPath = "HKLM:\SYSTEM\CurrentControlSet\Services\SNMP\Parameters\PermittedManagers"
if (-not (Test-Path $ipPermPath)) {
    New-Item -Path "HKLM:\SYSTEM\CurrentControlSet\Services\SNMP\Parameters" -Name "PermittedManagers"
}
Set-ItemProperty -Path $ipPermPath -Name "1" -Value "192.168.20.15"

# Redémarrage du service SNMP
Restart-Service -Name SNMP





netsh advfirewall firewall add rule name="Open Zabbix agentd port 165 inbound" dir=in action=allow protocol=UDP remoteip=192.168.20.15 localport=161

$vm_home = 'C:\VM'
$vm_name = 'DC1'
$my_VHD = "vm_name-disk.vhdx"
$my_iso = "C:\VM\winserv22.iso" # Assurez-vous que l'ISO est présent à cet emplacement
$my_switch = 'VM'





# Vérification du dossier pour stocker la VM
if (-not (Test-Path $vm_home)) {
    Write-Host "Le dossier VM n'existe pas. Création en cours..." -ForegroundColor Yellow
    New-Item -Path $vm_home -ItemType Directory
    Write-Host "Dossier créé : $vm_home" -ForegroundColor Green
} else {
    Write-Host "Le dossier VM existe déjà : $vm_home" -ForegroundColor Green
}

# Vérification du disque virtuel
if (-not (Test-Path "$vm_home\$my_VHD")) {
    Write-Host "Le disque virtuel n'existe pas. Création en cours..." -ForegroundColor Yellow
    New-VHD -Path "$vm_home\$my_VHD" -SizeBytes 100GB -Dynamic
    Write-Host "Disque virtuel créé : $my_VHD" -ForegroundColor Green
} else {
    Write-Host "Le disque virtuel existe déjà : $my_VHD" -ForegroundColor Green
}

# Vérification de l'existence du commutateur réseau
$is_present = Get-VMSwitch | Where-Object Name -eq $my_switch
if (-not $is_present) {
    Write-Host "Le commutateur NAT n'existe pas. Création en cours..." -ForegroundColor Yellow
    $NetCard = Read-Host "Quelle carte réseau souhaitez-vous utiliser pour le NAT ?"
    New-VMSwitch -Name $my_switch -NetAdapterName $NetCard -SwitchType Internal
    Write-Host "Commutateur NAT créé : $my_switch" -ForegroundColor Green
} else {
    Write-Host "Le commutateur NAT existe déjà : $my_switch" -ForegroundColor Green
}

# Vérification de l'existence de la VM
$VM_present = Get-VM -Name $vm_name -ErrorAction SilentlyContinue
if (-not $VM_present) {
    Write-Host "La VM n'existe pas. Création en cours..." -ForegroundColor Yellow
    New-VM -Name $vm_name -MemoryStartupBytes 32GB -Generation 2 -Path $vm_home

    # Ajout du disque dur virtuel
    Add-VMHardDiskDrive -VMName $vm_name -Path "$vm_home\$my_VHD"

    # Connexion au commutateur réseau
    Get-VM $vm_name | Get-VMNetworkAdapter | Connect-VMNetworkAdapter -SwitchName $my_switch

    Write-Host "VM créée : $vm_name" -ForegroundColor Green
} else {
    Write-Host "La VM existe déjà : $vm_name" -ForegroundColor Green
}

# Ajout de l'ISO si nécessaire
$ISOExist = Get-VMDvdDrive -VMName $vm_name -ErrorAction SilentlyContinue
if (-not $ISOExist) {
    Write-Host "Ajout de l'ISO à la VM..." -ForegroundColor Yellow
    Add-VMDvdDrive -VMName $vm_name -Path $my_iso
    Write-Host "ISO ajouté : $my_iso" -ForegroundColor Green
} else {
    Write-Host "L'ISO est déjà attaché." -ForegroundColor Green
}

# Configuration du firmware de la VM
Set-VMFirmware -VMName $vm_name -EnableSecureBoot Off -BootOrder (Get-VMDvdDrive -VMName $vm_name), (Get-VMHardDiskDrive -VMName $vm_name)

# Configuration des processeurs
Set-VMProcessor -VMName $vm_name -Count 2

Write-Host "Configuration de la VM $vm_name terminée avec succès !" -ForegroundColor Green
