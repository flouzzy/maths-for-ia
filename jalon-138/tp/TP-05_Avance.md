# TP 5 : Phénomène de Concentration et Malédiction de la Dimension

## Objectif du TP
Ce TP illustre le phénomène surprenant de concentration des distances dans les espaces de grande dimension, montrant que toutes les distances mutuelles entre points ont tendance à devenir presque constantes.

---

## Exercice Pratique : Simulation en Python

### Code Source
Copiez et exécutez le script suivant dans votre environnement Python :

```python
import numpy as np
import matplotlib.pyplot as plt

def simulate_distances(n, dimensions):
    """
    Génère n points dans le cube [0, 1]^d pour différentes dimensions,
    et calcule les distributions des distances mutuelles.
    """
    results = {}
    for d in dimensions:
        # Générer n points dans [0, 1]^d
        X = np.random.uniform(0, 1, size=(n, d))
        
        # Calculer la matrice des distances euclidiennes mutuelles
        # Distances entre tous les couples distincts
        dists = []
        for i in range(n):
            for j in range(i + 1, n):
                dists.append(np.linalg.norm(X[i] - X[j]))
        
        results[d] = np.array(dists)
    return results

# Fixer la graine
np.random.seed(42)

# Paramètres
n = 200 # Nombre de points
dimensions = [2, 10, 100, 1000] # Dimensions à tester

# Lancer la simulation
dist_data = simulate_distances(n, dimensions)

# Visualisation des histogrammes des distances normalisées par la dimension
plt.figure(figsize=(12, 8))
for d in dimensions:
    # Normaliser par le diamètre maximal théorique de la boîte sqrt(d)
    norm_dists = dist_data[d] / np.sqrt(d)
    
    # Calculer moyenne et écart-type
    mu = np.mean(norm_dists)
    std = np.std(norm_dists)
    
    plt.hist(norm_dists, bins=50, alpha=0.5, 
             label=f'Dim {d} (Moy={mu:.3f}, Écart-type={std:.3f})', density=True)

plt.xlabel('Distance euclidienne normalisée (d_eucl / sqrt(d))')
plt.ylabel('Densité de probabilité')
plt.title('Concentration des distances mutuelles en grande dimension')
plt.legend()
plt.grid(True)
plt.show()
```

---

## Questions et Travail d'Analyse
1. **Analyse de la variance :** Comment évolue l'écart-type des distances normalisées lorsque la dimension $d$ augmente ? Qu'indique cette tendance concernant la dispersion des points dans l'espace ?
2. **L'illusion de la proximité :** Si toutes les distances normalisées se concentrent autour de leur moyenne (environ $0.408$), qu'arrive-t-il à la distinction entre un point "proche" et un point "lointain" ?
3. **Application aux modèles d'IA :** En quoi ce phénomène explique-t-il la nécessité de réduire la dimension des données (via ACP, auto-encodeurs, etc.) avant d'appliquer des algorithmes basés sur des métriques de distance (comme le partitionnement spectral ou les K-Means) ?
