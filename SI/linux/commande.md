
## pwd

pour afficher tout le chemin du dossier actuel


tree
faut l'installer
et ca fait
## tree -L 2 x
x = niveau de l'arbre a afficher 
pour rentrer dans les dossiers


## mkdir -p /etc/ssl/certificats/CA

**`-p`** : Option qui permet de créer des répertoires parents si nécessaire



Cependant

- **`.pem`** peut contenir plusieurs types de données (certificat, clé privée, chaîne de certificats, etc.).
    
- **`.crt`** contient généralement uniquement un certificat public.
    

**Utilisation** :

- **`.pem`** est plus généraliste et peut être utilisé pour stocker plusieurs informations liées à la cryptographie.
    
- **`.crt`** est généralement utilisé pour les certificats SSL.
    

**Format** :

- Les fichiers **`.pem`** sont toujours en texte encodé Base64.
    
- Les fichiers **`.crt`** peuvent être soit en Base64 (texte), soit en binaire (DER)


## ll letre (èl letre èl)

afficher les fichier et leur droit du dossier actuel