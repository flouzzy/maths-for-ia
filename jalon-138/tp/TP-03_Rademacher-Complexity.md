# TP 3 : Concentration de la Complexité de Rademacher Empirique

## Objectif du TP
Ce TP a pour objectif de simuler la complexité de Rademacher empirique pour une classe de classifieurs linéaires et de vérifier numériquement sa forte concentration autour de sa moyenne théorique.

---

## Exercice Pratique : Simulation en Python

### Code Source
Copiez et exécutez le script suivant dans votre environnement Python :

```python
import numpy as np
import matplotlib.pyplot as plt

def empirical_rademacher_complexity(X, H, num_rad_draws=500):
    """
    Calcule la complexité de Rademacher empirique de la classe H sur l'échantillon X.
    X: échantillon de taille n (points en dimension d)
    H: ensemble de vecteurs de poids (classifieurs linéaires) de taille (M, d)
    """
    n = X.shape[0]
    M = H.shape[0]
    
    rad_complexities = []
    for _ in range(num_rad_draws):
        # Tirer des variables de Rademacher indépendantes {-1, 1}
        sigma = np.random.choice([-1, 1], size=n)
        
        # Calculer les projections pour toutes les hypothèses de H
        # projections = (1/n) * sum_{i=1}^n sigma_i * h(X_i)
        # h(X_i) = sign(<w, X_i>)
        predictions = np.sign(np.dot(H, X.T)) # taille (M, n)
        
        # Calculer le produit avec sigma
        val = np.dot(predictions, sigma) / n # taille (M,)
        
        # Prendre le supremum sur H
        rad_complexities.append(np.max(val))
        
    return np.mean(rad_complexities)

# Fixer la graine aléatoire
np.random.seed(42)

# Paramètres du problème
n = 100               # Taille de l'échantillon
d = 2                 # Dimension de l'espace
M = 50                # Nombre d'hypothèses dans H (vecteurs de poids unitaires aléatoires)
num_samples_sim = 1000 # Nombre d'échantillons S simulés

# Générer la classe H fixe de classifieurs linéaires (hyperplans)
H = np.random.normal(size=(M, d))
H /= np.linalg.norm(H, axis=1, keepdims=True) # normaliser

# Simuler la complexité de Rademacher empirique sur différents échantillons S
rad_emp_values = np.zeros(num_samples_sim)
for s in range(num_samples_sim):
    # Générer un échantillon S tiré uniformément sur la sphère unité
    X = np.random.normal(size=(n, d))
    X /= np.linalg.norm(X, axis=1, keepdims=True)
    
    # Calculer la complexité de Rademacher empirique sur cet échantillon
    rad_emp_values[s] = empirical_rademacher_complexity(X, H, num_rad_draws=100)

# Calculer les statistiques
mean_rad = np.mean(rad_emp_values)
t_values = np.arange(0, 0.15, 0.005)
emp_probs = []
mcdiarmid_bounds = []

# Les fonctions de classification binaire sont à valeurs dans {-1, 1}, donc B=1
# Les constantes c_i valent 2B/n = 2/n
# sum(c_i^2) = n * (4 / n^2) = 4/n
for t in t_values:
    prob = np.mean(np.abs(rad_emp_values - mean_rad) >= t)
    emp_probs.append(prob)
    
    bound = 2 * np.exp(- 2 * (t**2) / (4 / n)) # 2 * exp(-n * t^2 / 2)
    mcdiarmid_bounds.append(bound)

# Visualisation
plt.figure(figsize=(10, 6))
plt.semilogy(t_values, emp_probs, 'o-', label='Probabilité Empirique P(|Rad - E[Rad]| >= t)')
plt.semilogy(t_values, mcdiarmid_bounds, 'r--', linewidth=2, label='Borne Théorique de McDiarmid')
plt.grid(True, which="both", ls="-")
plt.xlabel('Seuil de déviation t')
plt.ylabel('Probabilité (échelle logarithmique)')
plt.title('Concentration de la Complexité de Rademacher Empirique')
plt.legend()
plt.show()
```

---

## Questions et Travail d'Analyse
1. **Rôle des variables de Rademacher :** Expliquez la différence entre l'aléa lié aux variables $\sigma_i$ (utilisées pour calculer la complexité empirique) et l'aléa lié au tirage de l'échantillon $S$ (qui cause les fluctuations étudiées ici).
2. **Impact de la dimension $d$ :** Si vous augmentez la dimension $d$ de l'espace ($d=10$ ou $d=100$), les constantes $c_i = 2B/n$ changent-elles ? Comment la borne théorique est-elle affectée ?
3. **Optimisation :** Proposez une explication physique sur la raison pour laquelle la complexité de Rademacher empirique fluctue si peu d'un échantillon à un autre.
