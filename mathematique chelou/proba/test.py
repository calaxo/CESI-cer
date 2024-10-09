import nashpy as nash
import numpy as np



# pluie

MarcPluie = np.array([[-50, -150],
              [-50, -70]])


#B Nicole
NicolePluie = np.array([[-5, 0],
              [-5, 15]])

# Créer le jeu à deux joueurs
game = nash.Game(MarcPluie, NicolePluie)

# Trouver les équilibres de Nash
equilibria = game.support_enumeration()

# Afficher les résultats
print("Équilibres de Nash :")
for eq in equilibria:
    print("en cas de certitude de pluie:",eq)
    
    
    
#soleil
#marc
MarcSoleil = np.array([[50, 0],
              [-75, 70]])

# Player B's payoff matrix
#B Nicole
NicoleSoleil = np.array([[50, 0],
              [50, 15]])

# Créer le jeu à deux joueurs
game = nash.Game(MarcSoleil, NicoleSoleil)

# Trouver les équilibres de Nash
equilibria = game.support_enumeration()

# Afficher les résultats
print("Équilibres de Nash :")
for eq in equilibria:
    print("en cas de certitude de soleil",eq)
    


