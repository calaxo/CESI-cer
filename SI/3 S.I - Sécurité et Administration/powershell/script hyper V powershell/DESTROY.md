``` powershell
$vm_home = 'F:\vmdev'
$vm_name = 'DevHyperV'
$my_VHD='hd20GB.vhdx'
$my_iso="F:\vmdevubuntu.iso"


$VM_present =  get-vm -name $vm_name -ErrorAction SilentlyContinue

  

if ($VM_present) {

  

Write-host "VM Present" -f Green

Remove-VM  $vm_name -Force

Write-host "VM Present" -f Red

}


if (Test-Path $vm_home\$vm_name) {

    # Folder exists - Do something here

    Write-host "Folder Exists!" -ForegroundColor Green

  Remove-Item $vm_home -Recurse -Force


    Write-host "folder deleted" -ForegroundColor Red
}





```
