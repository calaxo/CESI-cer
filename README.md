# CESI-cge

## proba

    choix du prisonnier:
        theoreme de nash(esque il vaut mieux coopérer)
### en python

```python

A = np.array([[-50, -150],
              [-50, -70]])



B = np.array([[-5, 0],
              [-5, 15]])


game = nash.Game(A, B)


equilibria = game.support_enumeration()


print("Équilibres de Nash :")
for eq in equilibria:
    print("pluie",eq)


A = np.array([[50, 0],
              [-75, 70]])


B = np.array([[50, 0],
              [50, 15]])


game = nash.Game(A, B)


equilibria = game.support_enumeration()


print("Équilibres de Nash :")
for eq in equilibria:
    print("soleil",eq)
    

```

### en math normal