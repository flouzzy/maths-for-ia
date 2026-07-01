---
uuid: "exo-14-4"
title: "Exercice 4 - Suites (Difficulté 2 étoiles)"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/convergence
  - exercice
---
# Exercice 4
Soient $(u_n)_{n \in \mathbb{N}}$ et $(v_n)_{n \in \mathbb{N}}$ deux suites réelles convergentes vers $l$ et $l'$ respectivement.
Montrer rigoureusement que la suite somme définie par $w_n = u_n + v_n$ converge vers $l + l'$.

## Correction

Soit $\epsilon > 0$.
Puisque $(u_n)$ converge vers $l$, il existe un entier $N_1 \in \mathbb{N}$ tel que :
$$ \forall n \ge N_1, |u_n - l| < \frac{\epsilon}{2} $$

Puisque $(v_n)$ converge vers $l'$, il existe un entier $N_2 \in \mathbb{N}$ tel que :
$$ \forall n \ge N_2, |v_n - l'| < \frac{\epsilon}{2} $$

Posons $N = \max(N_1, N_2)$.
Soit $n \ge N$.
Comme $N \ge N_1$, on a $n \ge N_1$, donc $|u_n - l| < \frac{\epsilon}{2}$.
De même, comme $N \ge N_2$, on a $n \ge N_2$, donc $|v_n - l'| < \frac{\epsilon}{2}$.

Évaluons la distance entre $w_n$ et $l + l'$ :
$$
\begin{align*}
|w_n - (l + l')| &= |(u_n + v_n) - (l + l')| \\
&= |(u_n - l) + (v_n - l')|
\end{align*}
$$

Par l'inégalité triangulaire $|a+b| \le |a| + |b|$, nous obtenons :
$$
\begin{align*}
|(u_n - l) + (v_n - l')| &\le |u_n - l| + |v_n - l'| \\
&< \frac{\epsilon}{2} + \frac{\epsilon}{2} \\
&= \epsilon
\end{align*}
$$

Ainsi, pour tout $n \ge N$, $|w_n - (l + l')| < \epsilon$.
Ceci démontre que la suite $(w_n)_{n \in \mathbb{N}}$ converge vers $l + l'$.
