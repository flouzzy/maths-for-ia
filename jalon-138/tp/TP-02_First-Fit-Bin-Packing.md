# TP 2 : Simulation de l'Inégalité de McDiarmid sur le Problème de Bin Packing

## Objectif du TP
Ce TP vise à programmer un algorithme glouton de résolution du problème de Bin Packing (Next Fit / First Fit) et à étudier empiriquement la concentration de la solution par rapport à la borne théorique de McDiarmid.

---

## Exercice Pratique : Simulation en Python

### Code Source
Copiez et exécutez le script suivant dans votre environnement Python :

```python
import numpy as np
import matplotlib.pyplot as plt

def first_fit_bin_packing(weights, c=1.0):
    """
    Algorithme heuristique First Fit pour le Bin Packing.
    Renvoie le nombre de boîtes nécessaires de capacité c.
    """
    bins = []
    for w in weights:
        placed = False
        for i in range(len(bins)):
            if bins[i] + w <= c:
                bins[i] += w
                placed = True
                break
        if not placed:
            bins.append(w)
    return len(bins)

# Fixer la graine pour reproductibilité
np.random.seed(42)

# Paramètres
n = 200                # Nombre d'objets
num_simulations = 5000 # Nombre de simulations de Monte Carlo

# Générer les poids aléatoirement (Uniforme sur [0, 0.8])
# Les constantes de McDiarmid pour la fonction B sont c_i = 1
sim_results = np.zeros(num_simulations)
for s in range(num_simulations):
    weights = np.random.uniform(0, 0.8, n)
    sim_results[s] = first_fit_bin_packing(weights)

# Estimation empirique de l'espérance
mean_B = np.mean(sim_results)

# Calculer les probabilités empiriques de déviation
t_values = np.arange(0, 15, 0.5)
emp_probs = []
mcdiarmid_bounds = []

for t in t_values:
    # P(|B - E[B]| >= t)
    prob = np.mean(np.abs(sim_results - mean_B) >= t)
    emp_probs.append(prob)
    
    # McDiarmid bound: 2 * exp(-2 * t^2 / sum(c_i^2)) avec sum(c_i^2) = n
    bound = 2 * np.exp(- 2 * (t**2) / n)
    mcdiarmid_bounds.append(bound)

# Tracé des courbes
plt.figure(figsize=(10, 6))
plt.semilogy(t_values, emp_probs, 'go-', label='Probabilité Empirique P(|B - E[B]| >= t)')
plt.semilogy(t_values, mcdiarmid_bounds, 'r--', linewidth=2, label='Borne Théorique de McDiarmid')
plt.grid(True, which="both", ls="-")
plt.xlabel('Seuil de déviation t')
plt.ylabel('Probabilité (échelle logarithmique)')
plt.title(f'Concentration du Bin Packing (n={n}, {num_simulations} simulations)')
plt.legend()
plt.show()
```

---

## Questions et Travail d'Analyse
1. **Rigueur mathématique de l'heuristique :** La fonction `first_fit_bin_packing` satisfait-elle la propriété des différences bornées ? Justifier en décrivant l'impact du changement du poids d'un unique objet sur le résultat de l'algorithme First Fit.
2. **Qualité de la borne :** L'inégalité de McDiarmid est-elle très lâche par rapport aux observations empiriques ? À votre avis, pourquoi la borne de McDiarmid est-elle pessimiste dans ce cas concret ?
3. **Variance empirique :** Calculez la variance empirique de vos simulations et vérifiez si elle est conforme à la borne supérieure donnée par l'inégalité d'Efron-Stein ($\text{Var}(B) \le n/2$).
