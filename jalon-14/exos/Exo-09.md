---
uuid: "exo-14-9"
title: "Exercice 9 - Suites (Difficulté 5 étoiles)"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/convergence
  - exercice
---
# Exercice 9
Démontrer rigoureusement le Lemme de Cesàro.
Soit $(u_n)_{n \in \mathbb{N}^*}$ une suite réelle convergeant vers $l \in \mathbb{R}$.
Soit $(v_n)_{n \in \mathbb{N}^*}$ la suite des moyennes de Cesàro, définie par $v_n = \frac{1}{n}\sum_{k=1}^n u_k$.
Montrer que $\lim_{n \to \infty} v_n = l$.

## Correction

L'objectif est de montrer que pour tout $\epsilon > 0$, il existe un rang $N$ à partir duquel $|v_n - l| < \epsilon$.

Soit $\epsilon > 0$ fixé.
La suite $(u_n)$ converge vers $l$. Donc il existe $N_1 \in \mathbb{N}^*$ tel que pour tout $n > N_1$, on ait $|u_n - l| < \frac{\epsilon}{2}$.

Écrivons la différence $v_n - l$ :
$$
\begin{align*}
v_n - l &= \left( \frac{1}{n} \sum_{k=1}^n u_k \right) - l \\
&= \left( \frac{1}{n} \sum_{k=1}^n u_k \right) - \left( \frac{1}{n} \sum_{k=1}^n l \right) \\
&= \frac{1}{n} \sum_{k=1}^n (u_k - l)
\end{align*}
$$

Soit $n > N_1$. Nous découpons la somme en deux parties, pour séparer les termes qui sont "proches" de $l$ de ceux qui ne le sont pas forcément (ceux d'indices $\le N_1$).
$$
\sum_{k=1}^n (u_k - l) = \sum_{k=1}^{N_1} (u_k - l) + \sum_{k=N_1+1}^n (u_k - l)
$$

Appliquons l'inégalité triangulaire :
$$
\begin{align*}
|v_n - l| &= \left| \frac{1}{n} \sum_{k=1}^{N_1} (u_k - l) + \frac{1}{n} \sum_{k=N_1+1}^n (u_k - l) \right| \\
&\le \frac{1}{n} \left| \sum_{k=1}^{N_1} (u_k - l) \right| + \frac{1}{n} \sum_{k=N_1+1}^n |u_k - l|
\end{align*}
$$

Le terme $\sum_{k=1}^{N_1} (u_k - l)$ est une somme finie de nombres réels et ne dépend pas de $n$. Notons cette somme constante $S_{N_1} = \left| \sum_{k=1}^{N_1} (u_k - l) \right|$.

Pour la deuxième somme, par définition de $N_1$, pour tout $k \ge N_1+1$, on a $|u_k - l| < \frac{\epsilon}{2}$. Donc :
$$
\begin{align*}
\frac{1}{n} \sum_{k=N_1+1}^n |u_k - l| &< \frac{1}{n} \sum_{k=N_1+1}^n \frac{\epsilon}{2} \\
&= \frac{1}{n} (n - N_1) \frac{\epsilon}{2} \\
&< \frac{n}{n} \frac{\epsilon}{2} = \frac{\epsilon}{2}
\end{align*}
$$

Nous avons donc pour $n > N_1$ :
$$ |v_n - l| < \frac{S_{N_1}}{n} + \frac{\epsilon}{2} $$

Le terme $S_{N_1}$ est fixé. La suite $\frac{S_{N_1}}{n}$ converge vers $0$ lorsque $n$ tend vers l'infini.
Il existe donc un entier $N_2 \in \mathbb{N}^*$ tel que pour tout $n \ge N_2$, on ait $\frac{S_{N_1}}{n} < \frac{\epsilon}{2}$.
(Concrètement, il suffit de prendre $N_2 = \lfloor \frac{2 S_{N_1}}{\epsilon} \rfloor + 1$).

Posons $N = \max(N_1, N_2)$.
Soit $n \ge N$.
Comme $n \ge N_1$, la décomposition est valide.
Comme $n \ge N_2$, on a $\frac{S_{N_1}}{n} < \frac{\epsilon}{2}$.

Par conséquent :
$$
\begin{align*}
|v_n - l| &< \frac{S_{N_1}}{n} + \frac{\epsilon}{2} \\
&< \frac{\epsilon}{2} + \frac{\epsilon}{2} \\
&= \epsilon
\end{align*}
$$

Nous avons rigoureusement démontré que :
$$ \forall \epsilon > 0, \exists N \in \mathbb{N}^*, \forall n \ge N, |v_n - l| < \epsilon $$
Le Lemme de Cesàro est ainsi prouvé.
