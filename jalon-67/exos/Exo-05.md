# Exercice 5 : Calcul probabiliste d'espérance

**Difficulté :** $\bigstar$$\bigstar$$\bigstar$$\star$$\star$

## Énoncé
Soit $X \sim \mathcal{E}(\lambda)$. Montrer que $\mathbb{E}[e^{tX}]$ peut se calculer via Beppo-Levi en développant l'exponentielle.

## Correction Détaillée
1. $\mathbb{E}[e^{tX}] = \int_0^\infty e^{tx} \lambda e^{-\lambda x} dx$. On développe $e^{tx} = \sum_{n=0}^\infty \frac{(tx)^n}{n!}$.
2. Pour $t \ge 0$, les termes sont positifs, Beppo-Levi s'applique. On intègre terme à terme.
3. Pour $t < \lambda$, on trouve la somme d'une série géométrique $\frac{\lambda}{\lambda - t}$.
