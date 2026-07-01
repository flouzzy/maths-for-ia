---
uuid: "exo-14-5"
title: "Exercice 5 - Suites (Difficulté 3 étoiles)"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/convergence
  - exercice
---
# Exercice 5
Montrer rigoureusement que la suite définie par $u_n = \sum_{k=1}^n \frac{1}{n+k}$ est convergente.

## Correction

Étudions le sens de variation de la suite $(u_n)_{n \in \mathbb{N}^*}$.
Pour $n \ge 1$ :
$$
\begin{align*}
u_{n+1} - u_n &= \sum_{k=1}^{n+1} \frac{1}{n+1+k} - \sum_{k=1}^n \frac{1}{n+k} \\
&= \left( \frac{1}{n+2} + \frac{1}{n+3} + \dots + \frac{1}{2n+1} + \frac{1}{2n+2} \right) - \left( \frac{1}{n+1} + \frac{1}{n+2} + \dots + \frac{1}{2n} \right)
\end{align*}
$$
Tous les termes se simplifient sauf le premier de $u_n$ et les deux derniers de $u_{n+1}$ :
$$
\begin{align*}
u_{n+1} - u_n &= \frac{1}{2n+1} + \frac{1}{2n+2} - \frac{1}{n+1} \\
&= \frac{1}{2n+1} + \frac{1}{2(n+1)} - \frac{2}{2(n+1)} \\
&= \frac{1}{2n+1} - \frac{1}{2n+2}
\end{align*}
$$
Comme $2n+1 < 2n+2$, on a $\frac{1}{2n+1} > \frac{1}{2n+2}$.
Donc $u_{n+1} - u_n > 0$. La suite $(u_n)$ est strictement croissante.

Montrons que la suite $(u_n)$ est majorée.
Pour tout entier $n \ge 1$ et pour tout $k \in \{1, \dots, n\}$, on a $n+k > n$.
Donc $\frac{1}{n+k} < \frac{1}{n}$.
En sommant ces inégalités de $k=1$ à $n$ :
$$
\begin{align*}
u_n &= \sum_{k=1}^n \frac{1}{n+k} \\
&< \sum_{k=1}^n \frac{1}{n} \\
&= n \cdot \frac{1}{n} = 1
\end{align*}
$$
La suite $(u_n)$ est majorée par $1$.

Par le théorème de convergence monotone, une suite croissante et majorée est convergente.
La suite $(u_n)_{n \in \mathbb{N}^*}$ est donc convergente (sa limite, non demandée ici, s'obtient par les sommes de Riemann et vaut $\ln(2)$).
