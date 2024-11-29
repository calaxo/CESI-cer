
le raid ne permet n'est pas considerer comme un moyen de backup


Redundant Arry of Independant Disks


unité de stockage via plusieur hdd


performance ou tolerance au panne


## RAID 0
stripping/bande 
meilleure performance lecture ecriture
## RAID1
mirroring
n'importe quel disque interchangeable

meilleur lecture mais écriture normale
## RAID 5
stripping avec parité 

si on perd un disk on perte soit des bit de parité ou de la donnée qu'on peut reconstituer avec des bits de parité

perte de 1 seule disk

plus lent a cause de la parité
## RAID 10

### 1+0

RAID 0 de RAID 1

repartition de donnée en bande sur des disque en mirroir
## RAID 50

### RAID 5+0


RAID 0 de RAID 5

repartition de données en bande sur des disk en repartition+parité