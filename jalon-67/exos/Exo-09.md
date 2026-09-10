## Exercice 9 : Application probabiliste (Espérance du temps d'attente) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $X$ une variable aléatoire à valeurs dans $\mathbb{N}$.
**Question :** Montrer que $\mathbb{E}[X] = \sum_{n=1}^\infty \mathbb{P}(X \ge n)$.

**Solution :**
1. On peut écrire $X = \sum_{n=1}^\infty \mathbf{1}_{\{X \ge n\}}$.
2. En effet, si $X(\omega) = k$, alors $\mathbf{1}_{\{X \ge n\}}(\omega) = 1$ pour $n \in \{1, \dots, k\}$ et $0$ au-delà. La somme vaut bien $k$.
3. La suite des sommes partielles $S_N = \sum_{n=1}^N \mathbf{1}_{\{X \ge n\}}$ est croissante et positive.
4. Par Beppo Levi, on peut intervertir espérance (qui est l'intégrale par rapport à la mesure de probabilité) et somme infinie.
5. $\mathbb{E}[X] = \mathbb{E}\left[ \sum_{n=1}^\infty \mathbf{1}_{\{X \ge n\}} \right] = \sum_{n=1}^\infty \mathbb{E}[\mathbf{1}_{\{X \ge n\}}]$.
6. Or l'espérance d'une indicatrice est la probabilité de l'ensemble. Donc $\mathbb{E}[X] = \sum_{n=1}^\infty \mathbb{P}(X \ge n)$. $\blacksquare$
