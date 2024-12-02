
j'ai utiliser hyperV au lieu de oracle VirtualBox
[[Virtualisation]]

# Infra:
[[Base via model OSI]]

![[Pasted image 20241115084942.png]]
pour eviter que les VM choppent le dhcp du reseaux de cesi ou de mon partage de CO il a fallu fair un reseaux NAT

c'est trés simple dans VirtualBox

mais avec hyper V il faut passer par powershell


###  commande pour voir les carte réseaux en rapport avec hyperV
	Get-NetAdapter | Where-Object { $_.InterfaceDescription -like "Hyper-V*" }
et récupérer le ifIndex ( InterfaceIndex)


###  commande pour assigner une adresse de passerelle a notre réseaux
``` powershell
New-NetIPAddress -IPAddress 192.168.10.254 -PrefixLength 24 -InterfaceIndex 23
```

	
###  commande pour assigner une plage d'adresse interne a notre reseaux
``` powershell
New-NetNat -Name NAT-OUT -InternalIPInterfaceAddressPrefix 192.168.10.0/24
```


![[Pasted image 20241115090615.png]]


dans Hyper-V on a un réseaux interne qui n'est pas sensé avoir d'accès vers l'extérieur

donc tout par PowerShell

le NAT est normalement dans un routeur pour transformer des adresse IP locale ( genre 192.168.1.15)
vers une adresse IP qui est plus haute (publique)
la transformation se passe dans les deux sens et peux influer sur les port( comme ouverture de port sur box d'FAI pour serv minecraft ou WEB )


on a donc un réseaux de 192.168.10.0 a 192.168.10.255


adresse du DC1 : 192.168.10.5
	plage du DHCP : 192.168.10.10 a 192.168.10.200



j'ai aussi créer un domaine sur DC1 sur lequel je peux me connecter via la VM windows 10
		zinzin.main.fr





[[comment fair un projet]]