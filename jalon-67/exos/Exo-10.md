# Exercice 10 : Application aux probabilités - Espérance d'un temps d'arrêt \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $X \ge 0$ une variable aléatoire entière. Prouver que $\mathbb{E}[X] = \sum_{n=1}^\infty \mathbb{P}(X \ge n)$.

**Correction :**
On écrit $X = \sum_{n=1}^\infty \mathbb{1}_{\{X \ge n\}}$. Ce sont des variables positives. Par sommation terme à terme (corollaire du TCM), l'espérance de la somme est la somme des espérances, et $\mathbb{E}[\mathbb{1}_{A}] = \mathbb{P}(A)$, d'où le résultat direct. Formellement : $\int_{\Omega} \sum \mathbb{1}_{\{X \ge n\}} d\mathbb{P} = \sum \int_{\Omega} \mathbb{1}_{\{X \ge n\}} d\mathbb{P}$.
