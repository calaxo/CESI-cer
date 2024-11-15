dans python

import pandas as pd
pour utiliser des tableau beaucoup plus simplement(querry, colonne, ligne, calcul)

# retour du prosit 2:

Marges d’erreur nécessaire pour les prévisions pas les représentations des donnes. 

Retro régression linéaire bonne. 

Observer donne et tirer des hypothèses puis les vérifier. 

Trouver les formules pour les codes utilise. 

Savoir comment fonctionne notre code. 

Equation de la droite. 

Coefficient R² nous dis si ma droite représente t’elle mes données ? 

Afficher la droite de régression avec sa formule  

Plus le coefficient de corrélation est important plus de chance qu’il y a un lien linéaire  

Voir ce qu’est un Histogramme  

Faire des diagrammes en battons au lieu des histogrammes  

Analyser le type d’utilisateur  

 Moyennes avec des écart types (moyennes très sensible aux valeurs extrêmes)

# retour de prosit 3

avant de choisir une methode il faut comparer les autre sollution:

- Z-score est utile lorsque les données suivent une distribution normale, mais il est sensible aux valeurs extrêmes. 
    

- IQR est non paramétrique et plus robuste aux valeurs extrêmes, mais il peut ne pas fonctionner bien pour des distributions asymétriques. 
    

- Pourcentage du Maximum est simple à implémenter mais peut ne pas être adapté pour des séries temporelles avec une grande variabilité. 
    

- Statistiques Robustes sont efficaces pour les données avec des distributions non normales et des valeurs extrêmes, mais peuvent être plus complexes à calculer.


dans les cas de savoir quand il y a un dépassement de ressource(cpu, ram, network)

on a pris direct le Pourcentage du Maximum( moyenne de chaque jour puis conparasion avec 30% )

c'était le meilleur mais on a pas pu expliquer pourquoi on a pas pris le reste 

et dans la vrai vie faudrait lisser la courbe(aussi utiliser pour faire de la prédiction a cours terme)




