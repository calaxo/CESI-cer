``` powershell

$vm_home = 'F:\vmdev'

$vm_name = 'DevHyperV'

$my_VHD = 'hd20GB.vhdx'

$my_iso = "F:\vmdevubuntu.iso"

$my_switch = 'NAT'

  

  

# powershell check if directory exists

if (Test-Path $vm_home\$vm_name) {

    # Folder exists - Do something here

    Write-host "Folder Exists!" -ForegroundColor Green

}

else {

    # Folder does not exist - Do something else here

    Write-host "Folder Doesn't Exists!" -ForegroundColor Red

    mkdir -p $vm_home\$vm_name

     Write-host "Folder Created" -ForegroundColor Yellow

}

  
  
  

if (Test-Path $vm_home\$vm_name\$my_VHD) {

    Write-host "virtual Disk Exist" -ForegroundColor Green

}

  

else {

    Write-host "virtual Disk Doesn't Exists!" -ForegroundColor Red

    New-VHD -Path $vm_home\$vm_name\$my_VHD -SizeBytes 20GB -Dynamic

    Write-host "virtual Disk Created" -ForegroundColor Yellow

  

}

  
  
  

$is_present = Get-VMSwitch | Where-Object Name -eq $my_switch

if ($is_present) {

    Write-host "NAT Network Present" -ForegroundColor Green

}

else {

    Write-host "NAT Network Doesn't Exists!" -ForegroundColor Red

    $NetCard = Read-Host "quelle carte reseaux faut t'il utiliser ?"; 

    New-VMSwitch -Name $my_switch -NetAdapterName $NetCard

    Write-host "NAT Network Created" -ForegroundColor Yellow

}

  

$VM_present = get-vm -name $vm_name -ErrorAction SilentlyContinue

if ($VM_present) {

    Write-host "VM Present" -f Green

}

else {

    Write-Host "Vm Doesn't Exists!" -f Red;

    New-VM -name $vm_name -MemoryStartupBytes 2GB -Generation "2" -Path $vm_home

    Add-VMHardDiskDrive -VMName $vm_name -Path $vm_home\$vm_name\$my_VHD

    Get-VM  $vm_name | Get-VMNetworkAdapter | Connect-VMNetworkAdapter -SwitchName $my_switch

    Write-host "VM Created" -f Yellow

}

  
  

$SW_present = get-vm -name $vm_name -ErrorAction SilentlyContinue

if ($SW_present) {

    Write-host "switch  connecté" -f Green

}

else {

    Write-Host "switch pas connecté" -f Red;

     Add-VMHardDiskDrive -VMName $vm_name -Path $vm_home\$vm_name\$my_VHD

    Get-VM $vm_name | Get-VMNetworkAdapter | Connect-VMNetworkAdapter -SwitchName $my_switch

    Write-host "Switch vien d'etre conecté" -f Yellow

}

  
  
  
  

$boot_HD = get-VMHardDiskDrive -VMName $vm_name

  

if ($boot_HD -ne $null ) {

    Write-host "disque  lie" -f Green

}

else {

    Write-Host "disque non lie" -f Red

    Add-VMHardDiskDrive -VMName $vm_name -Path $vm_home\$vm_name\$my_VHD

    Write-host "disque lie" -f Yellow

}

  
  
  
  
  
  

# Set-VM -VMName 'demovm' -ProcessorCount 2 -MemoryStartupBytes 2gb -DynamicMemory -MemoryMinimumBytes 512mb -MemoryMaximumBytes 4gb

  
  

$ISOExist = Get-VMDvdDrive -VMName $vm_name -ErrorAction SilentlyContinue

  

if ($ISOExist.Count -gt 0) {

    Write-Host "ISO Exist" -ForegroundColor Green

}

else {

    Write-Host "ISO Doesn't Exists!" -ForegroundColor Red

    Add-VMDvdDrive -VMName $vm_name -Path $my_iso

    Write-Host "ISO Disk Created" -ForegroundColor Yellow

}

  
  
  
  
  
  

Set-VMFirmware -VMName $vm_name -EnableSecureBoot Off -BootOrder $boot_DVD, $boot_HD, $boot_LAN


```
