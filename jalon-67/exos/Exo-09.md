# Exercice 9 : Dangers de la décroissance \quad $\bigstar\bigstar\bigstar\bigstar\star$

Donner un contre-exemple si $f_n \ge f_{n+1}$ (Théorème de convergence monotone décroissante) sans condition supplémentaire.

**Correction :**
Il faut intégrabilité du premier terme. Contre-exemple : $f_n = \mathbb{1}_{[n, \infty[}$. La suite décroît vers $f=0$. $\int f_n = \infty$ pour tout $n$, mais $\int f = 0 \neq \infty$. Si $\int f_1 < \infty$, Beppo Levi s'applique à $f_1 - f_n \ge 0$ (croissante).
