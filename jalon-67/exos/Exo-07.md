---
title: "Lemme de Borel-Cantelli (Partie directe)"
difficulty: $\bigstar\bigstar\bigstar\bigstar\star$
---
# Lemme de Borel-Cantelli (Partie directe)
**Énoncé :**
Soit $(A_n)$ une suite d'événements tels que $\sum \mathbb{P}(A_n) < +\infty$.
En utilisant le TCM sur les fonctions indicatrices, montrer que $\mathbb{P}(\limsup A_n) = 0$.

**Correction :**
1. Soit $N(x) = \sum_{n=1}^\infty \mathbf{1}_{A_n}(x)$. $N(x)$ est le nombre d'événements qui se réalisent pour l'issue $x$.
2. Par le corollaire du TCM :
   $\mathbb{E}[N] = \mathbb{E}\left[\sum_{n=1}^\infty \mathbf{1}_{A_n}\right] = \sum_{n=1}^\infty \mathbb{E}[\mathbf{1}_{A_n}] = \sum_{n=1}^\infty \mathbb{P}(A_n)$.
3. Par hypothèse, cette somme est finie. Ainsi, la variable $N$ a une espérance finie, donc $N(x) < +\infty$ presque sûrement.
4. $\limsup A_n$ est exactement l'événement $\{ x \mid x \text{ appartient à une infinité de } A_n \}$, soit $\{ x \mid N(x) = +\infty \}$.
5. Comme $N$ est finie p.s., $\mathbb{P}(N = +\infty) = 0$, donc $\mathbb{P}(\limsup A_n) = 0$.
