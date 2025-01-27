



Set-VMProcessor -VMName "HV1" -ExposeVirtualizationExtensions $true
Set-VMProcessor -VMName "HV2" -ExposeVirtualizationExtensions $true
Set-VMProcessor -VMName "HV-Services" -ExposeVirtualizationExtensions $true




netsh advfirewall firewall add rule name="ICMP Allow incoming V4 echo request" protocol=icmpv4:8,any dir=in action=allow