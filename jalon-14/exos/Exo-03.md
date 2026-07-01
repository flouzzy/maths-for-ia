---
uuid: "exo-14-3"
title: "Exercice 3 - Suites (Difficulté 2 étoiles)"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/convergence
  - exercice
---
# Exercice 3
Montrer que toute suite convergente à valeurs dans $\mathbb{R}$ est bornée.

## Correction

Soit $(u_n)_{n \in \mathbb{N}}$ une suite réelle convergeant vers une limite $l \in \mathbb{R}$.
Par définition de la convergence, pour tout $\epsilon > 0$, il existe $N \in \mathbb{N}$ tel que pour tout $n \ge N$, on ait $|u_n - l| < \epsilon$.

Fixons $\epsilon = 1$.
Il existe donc un entier $N_1 \in \mathbb{N}$ tel que pour tout $n \ge N_1$, $|u_n - l| < 1$.

Par l'inégalité triangulaire, pour $n \ge N_1$ :
$$
\begin{align*}
|u_n| &= |(u_n - l) + l| \\
&\le |u_n - l| + |l| \\
&< 1 + |l|
\end{align*}
$$

Considérons maintenant les termes de la suite pour les indices $n < N_1$. Ces termes sont en nombre fini : $u_0, u_1, \ldots, u_{N_1-1}$.
L'ensemble $\{|u_0|, |u_1|, \ldots, |u_{N_1-1}|\}$ est un ensemble fini non vide de nombres réels.
Il admet donc un plus grand élément.
Posons $M' = \max(|u_0|, |u_1|, \ldots, |u_{N_1-1}|)$.

Soit $M = \max(M', 1 + |l|)$. $M$ est un réel positif.
Pour tout entier $n \in \mathbb{N}$, deux cas se présentent :
- Soit $n < N_1$, alors $|u_n| \le M' \le M$.
- Soit $n \ge N_1$, alors $|u_n| < 1 + |l| \le M$.

Dans tous les cas, $\forall n \in \mathbb{N}, |u_n| \le M$.
Cela prouve que la suite $(u_n)_{n \in \mathbb{N}}$ est bornée.
