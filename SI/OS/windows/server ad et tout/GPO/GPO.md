
- Un premier type de paramètres qui s’appliquera en fonction de l’utilisateur connecté sur la machine, quelle que soit la machine.
    
- Un second type qui s’appliquera sur la machine, quel que soit l’utilisateur connecté
1. Exécutez gpmc.msc → Créez un nouvel objet de stratégie de groupe → Modifiez-le : Allez à « Configuration ordinateur » → Stratégies → Paramètres Windows → Paramètres de sécurité → Configuration avancée de la stratégie d’audit → Stratégies d’audit → Ouvrir/fermer la session :
    
    - Auditer l’ouverture de session → Sélectionnez : Réussites et échecs
        

1. Allez dans le Journal des événements → Définissez :
    
    - Taille maximale du journal de sécurité : 4 Go
        
    - Méthode de conservation du journal de sécurité : « Remplacer les événements si nécessaire ».