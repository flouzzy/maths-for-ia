---
uuid: "exo-14-2"
title: "Exercice 2 - Suites (Difficulté 1 étoiles)"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/convergence
  - exercice
---
# Exercice 2
Soit la suite $u_n = \frac{n}{n+1}$ pour $n \in \mathbb{N}$. Montrer rigoureusement que la limite est $1$.

## Correction

Soit $\epsilon > 0$. On cherche $N \in \mathbb{N}$ tel que pour tout $n \ge N$, $|u_n - 1| < \epsilon$.

Calculons $|u_n - 1|$ :
$$
\begin{align*}
|u_n - 1| &= \left|\frac{n}{n+1} - 1\right| \\
&= \left|\frac{n - (n+1)}{n+1}\right| \\
&= \left|\frac{-1}{n+1}\right| \\
&= \frac{1}{n+1} \quad \text{(car } n+1 > 0\text{)}
\end{align*}
$$

La condition $|u_n - 1| < \epsilon$ devient :
$$
\begin{align*}
\frac{1}{n+1} &< \epsilon \\
n+1 &> \frac{1}{\epsilon} \\
n &> \frac{1}{\epsilon} - 1
\end{align*}
$$

D'après la propriété d'Archimède de $\mathbb{R}$, il existe un entier $N$ tel que $N > \frac{1}{\epsilon} - 1$.
On peut choisir $N = \max(0, \lfloor \frac{1}{\epsilon} - 1 \rfloor + 1)$.

Soit $n \ge N$.
Alors $n > \frac{1}{\epsilon} - 1$.
D'où $n+1 > \frac{1}{\epsilon}$.
Ce qui implique $\frac{1}{n+1} < \epsilon$.
Et par conséquent, $|u_n - 1| < \epsilon$.

Nous avons donc prouvé :
$$ \forall \epsilon > 0, \exists N \in \mathbb{N}, \forall n \ge N, |u_n - 1| < \epsilon $$
La suite $(u_n)_{n \in \mathbb{N}}$ converge donc vers $1$.
