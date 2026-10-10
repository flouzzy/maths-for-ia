# Exercice 10 : Marche aléatoire, indépendance et réflexion
Difficulté : $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soient $(X_i)_{i \geq 1}$ une suite de variables aléatoires i.i.d. telles que $\mathbb{P}(X_i = 1) = \mathbb{P}(X_i = -1) = 1/2$.
On pose $S_0 = 0$ et $S_n = \sum_{i=1}^n X_i$.
Soit $T = \inf\{n \geq 1 \mid S_n = 1\}$ le temps de premier passage en $1$.
Les variables aléatoires $S_n$ sont-elles indépendantes ? Qu'en est-il de la probabilité conditionnelle au temps $T$ ?

**Correction :**
1. **Dépendance des $S_n$ :**
Par définition, $S_n = S_{n-1} + X_n$. Connaître $S_{n-1}$ donne une information énorme sur $S_n$ (elle ne peut valoir que $S_{n-1}+1$ ou $S_{n-1}-1$).
Par exemple, $\mathbb{P}(S_2 = 2 | S_1 = 1) = \mathbb{P}(X_2 = 1) = 1/2$.
Mais $\mathbb{P}(S_2 = 2) = \mathbb{P}(X_1=1, X_2=1) = 1/4$.
Comme $\mathbb{P}(S_2 = 2 | S_1 = 1) \neq \mathbb{P}(S_2 = 2)$, les variables $S_1$ et $S_2$ ne sont pas indépendantes.
2. **Principe de réflexion (intuition d'indépendance) :**
La variable $T$ est un temps d'arrêt. conditionnellement à l'événement $\{T = k\}$, l'évolution de la marche aléatoire pour $n > k$ ne dépend que des pas $(X_{k+1}, X_{k+2}, \dots)$.
Puisque les pas initiaux et futurs sont indépendants, la trajectoire *après* le temps $T$ est indépendante de la trajectoire *avant* le temps $T$.
Soit une trajectoire atteignant $1$ au temps $T$. Pour toute trajectoire atteignant une valeur $x > 1$ au temps $n$, il existe une trajectoire équiprobable atteignant $2 - x$ par symétrie des $X_i$ après le temps $T$.
C'est le principe de la propriété de Markov forte, qui dérive directement de l'indépendance mutuelle stricte de tous les incréments $X_i$.
