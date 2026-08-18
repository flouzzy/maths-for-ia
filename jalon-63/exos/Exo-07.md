---
uuid: "exo-jalon-63-07"
title: "Exercice 7 : Borne de l'union (Union Bound) en Probabilité"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Borne de l'union (Union Bound) en Probabilité

## Énoncé

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace de probabilité. Soit $(A_n)_{n \geq 1}$ une suite d'événements. Démontrer la généralisation continue de la borne de l'union : si $\sum_{n=1}^{+\infty} \mathbb{P}(A_n) < +\infty$, alors la probabilité de l'événement $limsup A_n$ est nulle (Lemme de Borel-Cantelli). On rappelle que $\limsup A_n = \bigcap_{N=1}^{\infty} \bigcup_{n=N}^{\infty} A_n$.

## Correction Détaillée

Définissons l'événement $B_N = \bigcup_{n=N}^{\infty} A_n$.
Cet événement $B_N$ correspond à l'union des événements à partir du rang $N$.
La suite $(B_N)_{N \geq 1}$ est une suite décroissante d'ensembles ($B_{N+1} \subset B_N$).
La mesure $\mathbb{P}$ est finie (mesure de probabilité, de masse totale 1). On peut donc appliquer la continuité décroissante.
$$ \mathbb{P}(\limsup A_n) = \mathbb{P}\left( \bigcap_{N=1}^{\infty} B_N \right) = \lim_{N \to \infty} \mathbb{P}(B_N) $$

Majorons $\mathbb{P}(B_N)$ en utilisant l'inégalité de sous-additivité (inégalité de Boole) :
$$ \mathbb{P}(B_N) = \mathbb{P}\left( \bigcup_{n=N}^{\infty} A_n \right) \leq \sum_{n=N}^{\infty} \mathbb{P}(A_n) $$

Par hypothèse, la série à termes positifs $\sum_{n=1}^{+\infty} \mathbb{P}(A_n)$ converge.
Le terme $\sum_{n=N}^{\infty} \mathbb{P}(A_n)$ représente exactement le **reste d'ordre $N-1$** d'une série convergente.
Un résultat fondamental d'analyse réelle stipule que le reste d'une série convergente tend vers $0$ lorsque $N \to +\infty$.
Ainsi, $\lim_{N \to \infty} \sum_{n=N}^{\infty} \mathbb{P}(A_n) = 0$.

Par pincement, puisque $\mathbb{P}(B_N) \geq 0$, il s'ensuit que :
$$ \lim_{N \to \infty} \mathbb{P}(B_N) = 0 $$
Et donc, $\mathbb{P}(\limsup A_n) = 0$. $\blacksquare$
