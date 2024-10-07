# CESI-cge

## proba

    choix du prisonnier:
        theoreme de nash(esque il vaut mieux coopérer)

    ```python
# pluie
#marc
A = np.array([[-50, -150],
              [-50, -70]])


#B Nicole
B = np.array([[-5, 0],
              [-5, 15]])

# Créer le jeu à deux joueurs
game = nash.Game(A, B)

# Trouver les équilibres de Nash
equilibria = game.support_enumeration()

# Afficher les résultats
print("Équilibres de Nash :")
for eq in equilibria:
    print("pluie",eq)
    
    
    
#soleil
#marc
A = np.array([[50, 0],
              [-75, 70]])

# Player B's payoff matrix
#B Nicole
B = np.array([[50, 0],
              [50, 15]])

# Créer le jeu à deux joueurs
game = nash.Game(A, B)

# Trouver les équilibres de Nash
equilibria = game.support_enumeration()

# Afficher les résultats
print("Équilibres de Nash :")
for eq in equilibria:
    print("soleil",eq)
    

    ```

# autre