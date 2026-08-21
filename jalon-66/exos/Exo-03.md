# Exercice 3 : Intégrale par rapport à la mesure de Dirac \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $\delta_2$ la mesure de Dirac en 2 sur $\mathbb{R}$. Calculer $\int_{\mathbb{R}} e^x \mathbf{1}_{[0,5]}(x) \, d\delta_2(x)$.

**Correction :**
Soit $f(x) = e^x \mathbf{1}_{[0,5]}(x)$. C'est une fonction mesurable positive.

On sait que pour toute fonction mesurable positive $g$, $\int_{\mathbb{R}} g \, d\delta_a = g(a)$.

Ainsi, $\int_{\mathbb{R}} f \, d\delta_2 = f(2)$.

Puisque $2 \in [0,5]$, $\mathbf{1}_{[0,5]}(2) = 1$.
Donc $f(2) = e^2 \cdot 1 = e^2$.

L'intégrale vaut $e^2$.
