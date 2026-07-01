---
uuid: "exo-14-6"
title: "Exercice 6 - Suites (Difficulté 3 étoiles)"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/convergence
  - exercice
---
# Exercice 6
Démontrer rigoureusement le théorème d'encadrement (Théorème des Gendarmes).
Soient $(u_n)$, $(v_n)$, $(w_n)$ trois suites réelles.
Si $\forall n \in \mathbb{N}, v_n \le u_n \le w_n$ et si $\lim_{n \to \infty} v_n = l$ et $\lim_{n \to \infty} w_n = l$, alors $\lim_{n \to \infty} u_n = l$.

## Correction

Soit $\epsilon > 0$.
Puisque $(v_n)$ converge vers $l$, il existe $N_1 \in \mathbb{N}$ tel que :
$$ \forall n \ge N_1, \quad |v_n - l| < \epsilon $$
Ceci est équivalent à :
$$ \forall n \ge N_1, \quad l - \epsilon < v_n < l + \epsilon \quad (1) $$

Puisque $(w_n)$ converge vers $l$, il existe $N_2 \in \mathbb{N}$ tel que :
$$ \forall n \ge N_2, \quad |w_n - l| < \epsilon $$
Ceci est équivalent à :
$$ \forall n \ge N_2, \quad l - \epsilon < w_n < l + \epsilon \quad (2) $$

Posons $N = \max(N_1, N_2)$.
Soit $n \ge N$.
Comme $n \ge N_1$, l'inégalité (1) est vraie.
Comme $n \ge N_2$, l'inégalité (2) est vraie.
De plus, par hypothèse sur les suites, $v_n \le u_n \le w_n$.

Nous pouvons combiner ces inégalités.
De (1), nous extrayons $l - \epsilon < v_n$.
Comme $v_n \le u_n$, par transitivité, nous obtenons $l - \epsilon < u_n$.
De (2), nous extrayons $w_n < l + \epsilon$.
Comme $u_n \le w_n$, par transitivité, nous obtenons $u_n < l + \epsilon$.

En rassemblant les deux, pour tout $n \ge N$ :
$$ l - \epsilon < u_n < l + \epsilon $$
Ceci est exactement équivalent à $|u_n - l| < \epsilon$.

Nous avons donc montré que :
$$ \forall \epsilon > 0, \exists N \in \mathbb{N}, \forall n \ge N, |u_n - l| < \epsilon $$
La suite $(u_n)$ converge donc vers $l$.
