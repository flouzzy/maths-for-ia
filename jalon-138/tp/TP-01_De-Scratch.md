# TP 1 : Simulation et Vérification Empirique de l'Inégalité de Hoeffding

## Objectif du TP
Ce TP a pour objectif d'illustrer de manière empirique l'inégalité de Hoeffding pour une somme de variables indépendantes et de comparer la borne théorique avec les fréquences observées lors de simulations de Monte Carlo.

---

## Exercice Pratique : Simulation en Python

### Code Source
Copiez et exécutez le script suivant dans votre environnement Python (avec les bibliothèques `numpy` et `matplotlib` installées) :

```python
import numpy as np
import matplotlib.pyplot as plt

# Fixer la graine aléatoire pour la reproductibilité
np.random.seed(42)

def simulate_hoeffding(n, num_simulations, t_values):
    """
    Simule une somme de n variables de Rademacher et calcule les fréquences
    d'écarts par rapport à la moyenne pour différents seuils t.
    """
    # Générer num_simulations échantillons de taille n à valeurs dans {-1, 1}
    # Chaque X_i est une variable de Rademacher
    X = np.random.choice([-1, 1], size=(num_simulations, n))
    
    # Calculer la somme Sn pour chaque simulation
    Sn = np.sum(X, axis=1)
    
    # Fréquences empiriques de dépassement
    emp_probs = []
    # Bornes théoriques de Hoeffding
    hoeffding_bounds = []
    
    for t in t_values:
        # P(Sn >= t)
        prob = np.mean(Sn >= t)
        emp_probs.append(prob)
        
        # Borne de Hoeffding: exp(-t^2 / (2 * n))
        bound = np.exp(- (t**2) / (2 * n))
        hoeffding_bounds.append(bound)
        
    return emp_probs, hoeffding_bounds

# Paramètres
n = 100               # Nombre de variables aléatoires
num_simulations = 100000  # Nombre de simulations de Monte Carlo
t_values = np.arange(0, 40, 2)  # Seuils de déviation t

# Exécution de la simulation
emp_probs, hoeffding_bounds = simulate_hoeffding(n, num_simulations, t_values)

# Visualisation des résultats
plt.figure(figsize=(10, 6))
plt.semilogy(t_values, emp_probs, 'bo-', label='Probabilité Empirique P(Sn >= t)')
plt.semilogy(t_values, hoeffding_bounds, 'r--', linewidth=2, label='Borne Théorique de Hoeffding')
plt.grid(True, which="both", ls="-")
plt.xlabel('Seuil de déviation t')
plt.ylabel('Probabilité (échelle logarithmique)')
plt.title(f'Vérification empirique de Hoeffding (n={n}, {num_simulations} simulations)')
plt.legend()
plt.show()
```

---

## Questions et Travail d'Analyse
1. **Observation de la borne :** La courbe de la probabilité empirique passe-t-elle bien en dessous de la borne de Hoeffding pour tous les seuils $t$ ? Pourquoi cette borne est-elle qualifiée de "non asymptotique" ?
2. **Impact de $n$ :** Modifiez la valeur de $n$ dans le script ($n = 10$ puis $n = 1000$). Comment se comporte l'écart entre la borne théorique et la probabilité empirique ?
3. **Cas asymétrique :** Remplacez les variables de Rademacher par des variables de Bernoulli $Y_i \sim \mathcal{B}(p)$ avec $p = 0.1$. Modifiez le code pour recentrer la somme (considérer $S_n - n p$) et ajuster les bornes $[a_i, b_i]$ de Hoeffding. Que constatez-vous sur l'écart de la borne ?
