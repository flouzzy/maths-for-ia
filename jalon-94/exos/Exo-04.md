# Exercice 4 : Fiabilité des composants électroniques \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
La durée de vie $X$ d'un composant électronique suit une loi exponentielle de paramètre $\lambda = 0.01$ (en jours).
Pour qu'un système fonctionne en continu, on dispose de $n=100$ composants de rechange que l'on utilise les uns après les autres (le $i$-ème est allumé dès que le $(i-1)$-ème tombe en panne).
Soit $T = \sum_{i=1}^{100} X_i$ la durée de fonctionnement totale du système.
Estimer la probabilité que le système fonctionne pendant au moins $11000$ jours.

**Correction :**

Chaque durée de vie $X_i$ suit une loi exponentielle $\mathcal{E}(\lambda = 0.01)$.
L'espérance est $\mu = \mathbb{E}[X_i] = \frac{1}{\lambda} = \frac{1}{0.01} = 100$ jours.
La variance est $\sigma^2 = \text{Var}(X_i) = \frac{1}{\lambda^2} = \frac{1}{0.0001} = 10000$.

La durée totale est $T = \sum_{i=1}^{100} X_i$.
L'espérance de la somme est $\mathbb{E}[T] = 100 \times 100 = 10000$ jours.
La variance de la somme est $\text{Var}(T) = 100 \times 10000 = 1000000$.
L'écart-type total est $\sigma_T = \sqrt{1000000} = 1000$.

On utilise le TCL pour approcher la distribution de $T$. La variable aléatoire $Z = \frac{T - 10000}{1000}$ suit approximativement une loi $\mathcal{N}(0, 1)$.

On cherche $\mathbb{P}(T \ge 11000)$.
$$\mathbb{P}(T \ge 11000) = \mathbb{P}\left( \frac{T - 10000}{1000} \ge \frac{11000 - 10000}{1000} \right)$$
$$\mathbb{P}(T \ge 11000) = \mathbb{P}(Z \ge 1)$$

Pour une loi normale centrée réduite :
$$\mathbb{P}(Z \ge 1) = 1 - \Phi(1)$$
On sait que $\Phi(1) \approx 0.8413$.
Ainsi :
$$\mathbb{P}(T \ge 11000) \approx 1 - 0.8413 = 0.1587$$
Le système a donc approximativement $15.87\%$ de chance de durer plus de $11000$ jours.
