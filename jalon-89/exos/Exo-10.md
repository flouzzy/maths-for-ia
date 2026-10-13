# Exercice 10

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Théorème d'Erdős-Rényi sur les graphes

Soit $G(n, p_n)$ un graphe aléatoire d'Erdős-Rényi avec $n$ sommets et où chaque arête est présente avec probabilité $p_n$ indépendamment.
On considère la présence de triangles (cycles de longueur 3). Soit $X_n$ le nombre de triangles dans $G(n, p_n)$.
On suppose que $p_n \ll \frac{1}{n}$. Montrer que, presque sûrement pour $n$ assez grand, le graphe ne contient aucun triangle.

**Correction détaillée :**
1. Il y a $\binom{n}{3}$ triplets de sommets possibles dans un graphe de taille $n$.
2. Pour qu'un triplet forme un triangle, ses trois arêtes doivent être présentes. L'indépendance de la présence des arêtes implique que la probabilité pour un triplet donné de former un triangle est $p_n^3$.
3. Par linéarité de l'espérance, l'espérance du nombre de triangles est $\mathbb{E}[X_n] = \binom{n}{3} p_n^3$.
4. Asymptotiquement, $\binom{n}{3} \sim \frac{n^3}{6}$. L'hypothèse de l'énoncé $p_n \ll \frac{1}{n}$ signifie que $n \cdot p_n \to 0$, d'où $p_n = o(n^{-1})$.
5. Ainsi, $\mathbb{E}[X_n] \sim \frac{n^3 p_n^3}{6} = o(1)$. L'espérance tend vers zéro.
6. Plus finement, supposons un régime où $\sum_{n} \mathbb{E}[X_n] < +\infty$. C'est le cas si par exemple $p_n \le \frac{c}{n^{4/3}}$.
7. Considérons l'événement $A_n = \{X_n \ge 1\}$, c'est-à-dire qu'il y a au moins un triangle dans le graphe de taille $n$.
8. Par l'inégalité de Markov, $\mathbb{P}(A_n) = \mathbb{P}(X_n \ge 1) \le \frac{\mathbb{E}[X_n]}{1}$.
9. Puisque nous avons supposé $\sum \mathbb{E}[X_n] < +\infty$, par comparaison, $\sum \mathbb{P}(A_n) < +\infty$.
10. Par le premier lemme de Borel-Cantelli, $\mathbb{P}(\limsup A_n) = 0$. Donc, presque sûrement, il n'existe qu'un nombre fini d'indices $n$ où le graphe possède un triangle. Asymptotiquement, il n'y a pas de triangle.
