---
uuid: "exo-14-1"
title: "Exercice 1 - Suites (Difficulté 1 étoiles)"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/convergence
  - exercice
---
# Exercice 1
Soit la suite définie par $u_n = \frac{1}{n}$ pour $n \in \mathbb{N}^*$.
Montrer rigoureusement par la définition formelle de la limite que la suite $(u_n)_{n \in \mathbb{N}^*}$ converge vers $0$.

## Correction

Soit $\epsilon > 0$ un réel fixé, aussi petit que l'on veut.
On cherche un entier $N \in \mathbb{N}^*$ tel que pour tout $n \ge N$, on ait $|u_n - 0| < \epsilon$.

La condition s'écrit :
$$
\begin{align*}
|u_n - 0| &< \epsilon \\
\left|\frac{1}{n}\right| &< \epsilon \\
\frac{1}{n} &< \epsilon \quad \text{(car } n > 0\text{)} \\
n &> \frac{1}{\epsilon}
\end{align*}
$$

Par la propriété d'Archimède de $\mathbb{R}$, il existe un entier naturel $N$ tel que $N > \frac{1}{\epsilon}$.
Posons $N = \lfloor \frac{1}{\epsilon} \rfloor + 1$. Cet entier $N$ vérifie bien $N > \frac{1}{\epsilon}$.

Soit $n \ge N$.
Alors $n \ge N > \frac{1}{\epsilon}$.
D'où $\frac{1}{n} < \epsilon$.
Ce qui donne $\left|\frac{1}{n} - 0\right| < \epsilon$.

Nous avons donc montré que :
$$ \forall \epsilon > 0, \exists N \in \mathbb{N}^*, \forall n \ge N, |u_n - 0| < \epsilon $$
La suite $(u_n)_{n \in \mathbb{N}^*}$ converge donc vers $0$.
