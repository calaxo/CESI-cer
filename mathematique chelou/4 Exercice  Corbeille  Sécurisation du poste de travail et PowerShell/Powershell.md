écrit en UpperCamelCase et non  lowerCamelCase c'est aussi appelé PascalCase

sécurité :
	Get-ExecutionPolicy :
		- sur Windows 10/11 de base c'est sur  Restricted du coup on peut rien lancer
		- sauf avec : Set-ExecutionPolicy RemoteSigned
		- sur Windows server c'est sur RemoteSigned 
		- il y a une détection pour faire fonctionner que les script local et pas ceux du WEB (Mark Of The Web comme pour les fichiers office)

	$passwd = Read-Host "Tapez le mot de passe associé :" –AsSecureString
–AsSecureString poue le Read-Host permet de rentrer du texte qui peut ps etre chopper par d'autre programme




En powershell, listez les comptes utilisateurs locaux de la machne.

Créez un nouveau compte non administrateur.

Créez un nouveau compte administrateur.

Attention, dans les 2 cas il faut demander de taper le login souhaité, le mot de passe et re-taper le mot de passe pour vérification.

[Indice](https://moodle.cesi.fr/pluginfile.php/153466/mod_resource/content/3/co/_1_-_Corbeille_Securisation_poste_de_travail.html#)

Un script qui peut être long mais pour des raisons de vérification. Ecrivez bien l'algorithme avant.

[Solution](https://moodle.cesi.fr/pluginfile.php/153466/mod_resource/content/3/co/_1_-_Corbeille_Securisation_poste_de_travail.html#)

 # lister les comptes locaux 

 Get-LocalUser 

 # créer un compte user non administrateur »

 $userName = Read-Host "Quel login faut-il mettre (ex. BWILLIS) ?"; 

 $fullName = Read-Host "Quel est le nom complet (ex. Bruce Willis) ?"; 

 $passwd = Read-Host "Tapez le mot de passe associé :" –AsSecureString 

$passwd_confirm = Read-Host "Retapez le mot de passe pour vérification :" –AsSecureString 

 # vu que les mots de passe sont mis en secure string, on les passe en binaire pour comparaison sinon pas de comparaison possible 

 $pwd1_text = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($passwd)) 

 $pwd2_text = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($passwd_confirm)) 

 if ($pwd1_text -ne $pwd2_text) 

 { 

 write-Host "le mot de passe et sa confirmation ne correspondent pas !"; 

 } 

 else 

 { 

 New-LocalUser $userName -Password $passwd -FullName $fullName; 

write-Host "Le compte utilisateur de $fullName est créé."; 

 } 

 # pour mettre ce compte Administrateur, il faut simplement l'ajouter dans le groupe local "Administrateurs" 

 # attention les Windows Anglais ont le groupe nommé "Administrators" 

 Add-LocalGroupMember -Group 'Administrators' -Member ($userName) –Verbose 