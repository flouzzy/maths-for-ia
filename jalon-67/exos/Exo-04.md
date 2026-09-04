# Exercice 04 : Fonctions de répartition et mesures ($\bigstar$$\bigstar$$\star$$\star$$\star$)

## Énoncé

Soit $\mu$ une mesure sur $\mathbb{R}$. Montrer que l'application $F(x) = \mu(]-\infty, x])$ est continue à droite et croissante.

## Correction Détaillée

1. **Croissance :** Soit $x \le y$. Alors $]-\infty, x] \subset ]-\infty, y]$. Par monotonie de la mesure, $F(x) = \mu(]-\infty, x]) \le \mu(]-\infty, y]) = F(y)$. Donc $F$ est croissante.
2. **Continuité à droite :** Soit $x \in \mathbb{R}$ et $(x_n)$ une suite décroissante tendant vers $x$.
   Considérons la suite d'ensembles $A_n = ]-\infty, x_n]$.
3. **Emboîtement :** Comme $(x_n)$ est décroissante, $x_{n+1} \le x_n$, donc $A_{n+1} \subset A_n$. La suite $(A_n)$ est donc décroissante pour l'inclusion.
4. **Intersection :** L'intersection de ces ensembles est $\bigcap_{n \in \mathbb{N}} A_n = ]-\infty, x]$. En effet, si $y \le x$, alors $y \le x_n$ pour tout $n$, donc $y \in A_n$. Si $y > x$, alors pour $n$ assez grand, $y > x_n$, donc $y \notin A_n$.
5. **Continuité séquentielle :** En supposant que $\mu(A_0) < +\infty$, le théorème de continuité décroissante pour les mesures affirme que $\mu(\bigcap A_n) = \lim_{n \to \infty} \mu(A_n)$.
   Donc $\mu(]-\infty, x]) = \lim_{n \to \infty} \mu(]-\infty, x_n])$, c'est-à-dire $F(x) = \lim_{n \to \infty} F(x_n)$. Ceci caractérise exactement la continuité à droite de $F$ en $x$.
