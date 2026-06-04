# TP 4 : L'Inégalité d'Efron-Stein en Action

## Objectif du TP
Ce TP montre comment estimer la variance d'une fonction complexe en utilisant l'inégalité d'Efron-Stein par une méthode de ré-échantillonnage de type Jackknife, et à comparer cette borne à la variance réelle estimée par Monte Carlo.

---

## Exercice Pratique : Simulation en Python

### Code Source
Copiez et exécutez le script suivant dans votre environnement Python :

```python
import numpy as np

def complex_function(X):
    """
    Fonction non linéaire complexe : moyenne des carrés pondérée par des sinus.
    X: vecteur de taille n
    """
    n = len(X)
    weights = np.sin(np.arange(n)) + 2.0
    return np.sum(weights * (X**2)) / n

# Graine
np.random.seed(42)

# Paramètres
n = 50
num_simulations = 10000

# Lois de probabilité de base (uniforme sur [0, 1])
# Échantillon fantôme X' pour Efron-Stein
# Nous simulons de grands ensembles pour estimer la variance réelle
Z_vals = np.zeros(num_simulations)
for s in range(num_simulations):
    X = np.random.uniform(0, 1, n)
    Z_vals[s] = complex_function(X)

# Variance réelle estimée par Monte Carlo
var_real = np.var(Z_vals)

# Estimation de la borne d'Efron-Stein sur un seul échantillon par ré-échantillonnage
# Tirer un échantillon X de référence
X_ref = np.random.uniform(0, 1, n)
Z_ref = complex_function(X_ref)

sum_diff_sq = 0
num_resamples = 500 # Tirages fantômes pour chaque coordonnée

for i in range(n):
    # Pour chaque coordonnée, on tire num_resamples copies de X'_i
    # et on calcule la moyenne de (Z - Z'_i)^2
    diff_sq_accum = 0
    for _ in range(num_resamples):
        x_prime_i = np.random.uniform(0, 1)
        
        # Créer le vecteur modifié
        X_mod = X_ref.copy()
        X_mod[i] = x_prime_i
        
        Z_mod = complex_function(X_mod)
        diff_sq_accum += (Z_ref - Z_mod)**2
        
    sum_diff_sq += np.mean(diff_sq_accum) / num_resamples

# Borne d'Efron-Stein: (1/2) * sum_i E[(Z - Z'_i)^2]
efron_stein_bound = 0.5 * sum_diff_sq

print("--- RÉSULTATS DE LA SIMULATION ---")
print(f"Variance empirique réelle de Z : {var_real:.6f}")
print(f"Borne supérieure d'Efron-Stein : {efron_stein_bound:.6f}")
print(f"La borne est-elle respectée ?  : {efron_stein_bound >= var_real}")
print(f"Rapport Borne / Variance       : {efron_stein_bound / var_real:.2f}x")
```

---

## Questions et Travail d'Analyse
1. **Rapport d'efficacité :** Le rapport entre la borne d'Efron-Stein et la variance réelle est-il proche de 1 ? Pourquoi l'inégalité d'Efron-Stein est-elle considérée comme une borne de variance très robuste ?
2. **Comparaison avec McDiarmid :** Calculez analytiquement les constantes de McDiarmid $c_i$ pour la fonction `complex_function` sur $[0, 1]^n$. Calculez la borne supérieure de variance dérivée de McDiarmid ($\text{Var}(Z) \le \frac{1}{2} \sum c_i^2$) et comparez-la à la borne obtenue via Efron-Stein.
3. **Application pratique :** Dans quel cas de figure pratique en science des données préfère-t-on estimer la variance avec Efron-Stein plutôt que par des simulations complètes de Monte Carlo ?
