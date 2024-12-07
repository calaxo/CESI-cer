
au meme niveau qui IP( layer 2)

du coup super bas niveau met permet de fair du monitoring super efficaces sans agents

par contre aucune sécurité et faut bien definir la zone snmp 

pour ce balader dans les info d'un apareil via snmp on utilise l'arbre snmp

![[Exemple-dOID-dans-un-arbre-dinformation-de-gestion-SNMP35-1632-La-syntaxe-et-le.png]]

avec juste des numero pour savoir ou aller dans l'arbre genre:
OID=1.3.6.1.2.1.26


pour acceder au groupe smnp faut juste un identifiant et mod de passe


zaabix


jammais vraiment nommer nos zone smnp public et privée


nom de la public pour mon labo:
trkl



l'installer ou le metre en place sur nos machine

verifier que le port 161 est bien accessible

port :161/162

`.\SnmpWalk.exe -r:127.0.0.1 -c:"workshop" -os:.1.3.6.1.2.1.1 -op:.1.3.6.1.2.1.7`

snmpwalk -v2c -c trkl 127.0.0.1 .1.3.6.1.2.1.1


Le nombre d'OID exposés par un système dépend de la richesse de l'implémentation SNMP, des services gérés et de la façon dont chaque système est configuré