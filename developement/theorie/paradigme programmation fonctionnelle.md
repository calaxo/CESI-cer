La programmation fonctionnelle est un paradigme de programmation dans lequel :

- les programmes sont exprimés comme des arbres d'expressions
- le contrôle de flot est fait en combinant des fonctions plutôt qu'en assignant des valeurs
    - utiliser des [fonction d'ordre supérieur](app://obsidian.md/fonction%20d'ordre%20sup%C3%A9rieur)
    - ne pas utiliser d'[état](app://obsidian.md/programmation.%C3%A9tat)
    - ne pas utiliser d'entrée/sortie cachée (en sortant du champ local)
- les fonctions sont (le plus souvent, le plus possible) [pures](app://obsidian.md/fonction%20pure) (limiter au maximum / complètement [effet de bord](app://obsidian.md/programmation.effet%20de%20bord))




La programmation fonctionnelle est un paradigme de programmation dans lequel :

- les programmes sont exprimés comme des arbres d'expressions
- le contrôle de flot est fait en combinant des fonctions plutôt qu'en assignant des valeurs
    - utiliser des [fonction d'ordre supérieur](app://obsidian.md/fonction%20d'ordre%20sup%C3%A9rieur)
    - ne pas utiliser d'[état](app://obsidian.md/programmation.%C3%A9tat)
    - ne pas utiliser d'entrée/sortie cachée (en sortant du champ local)
- les fonctions sont (le plus souvent, le plus possible) [pures](app://obsidian.md/fonction%20pure) (limiter au maximum / complètement [effet de bord](app://obsidian.md/programmation.effet%20de%20bord))

effet de bord

En programmation, une [fonction](app://obsidian.md/programmation.fonction) est dite à effet de bord si elle modifie un [état](app://obsidian.md/programmation.%C3%A9tat) en dehors de son environnement local.


Exemples d'effets de bord

- la modification d'une variable non-locale
- le [passage par référence](app://obsidian.md/programmation.passage%20par%20r%C3%A9f%C3%A9rence) d'un [argument](app://obsidian.md/argument%20d'une%20fonction) mutable
- la modification d'une [variable statique](app://obsidian.md/programmation.variable%20statique) locale
- le fait d'appeler une autre fonction à effet de bord

[Effet de bord (informatique)](zotero://select/groups/5383243/items/HK8W8STH) - [Page](zotero://open-pdf/groups/5383243/items/FHGCUVX5?annotation=FRXYERKZ)

# Problèmes des effets de bord

Les effets de bord posent problème pour :

- la lisibilité (l'influence d'un effet de bord n'est pas bien circonscrite)
- la réutilisabilité des [fonctions](app://obsidian.md/programmation.fonction) / [procédures](app://obsidian.md/programmation.proc%C3%A9dure)


fonction d'ordre supérieur

Une [fonction](app://obsidian.md/programmation.fonction) qui possède au moins une des propriétés suivantes :

- elle prend une ou plusieurs [fonctions](app://obsidian.md/programmation.fonction) en entrée
- elle renvoie une [fonction](app://obsidian.md/programmation.fonction)


procédure

Une procédure est l'encapsulation d'un ensemble d'instructions.  
Une procédure peut possèder des [paramètres](app://obsidian.md/param%C3%A8tre%20d'une%20fonction) qui peuvent influencer son exécution.  
Contrairement à une fonction, une procédure ne peut pas retourner de valeur. Elle peut cependant [modifier ses paramètres](app://obsidian.md/programmation.modification%20des%20param%C3%A8tres)


modification des paramètres

La modification des paramètres désigne le fait, pour une [fonction](app://obsidian.md/programmation.fonction) ou une [procédure](app://obsidian.md/programmation.proc%C3%A9dure), de modifier la valeur de ses [arguments](app://obsidian.md/programmation.argument%20d'une%20fonction) (modifier la valeur des variables qui lui sont passées) en passant par la modification de ses [paramètres](app://obsidian.md/param%C3%A8tre%20d'une%20fonction) (la modification du paramètre entraine la modification de l'argument).  
La modification des paramètres constitue un [effet de bord](app://obsidian.md/programmation.effet%20de%20bord).  
En particulier, les [fonctions pures](app://obsidian.md/fonction%20pure) ne peuvent pas modifier leurs paramètres.