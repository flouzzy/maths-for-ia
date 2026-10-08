# Exercice 4

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $(X_n)_{n \in \mathbb{N}}$ une suite de variables aléatoires réelles. Montrer que $\sup_{n} X_n$ est une variable aléatoire étendue (à valeurs dans $\mathbb{R} \cup \{+\infty\}$).

## Correction Détaillée

**Correction de l'exercice 4 :**

1. Soit $Z = \sup_{n} X_n$. On utilise à nouveau le critère sur les intervalles ouverts $]a, +\infty]$ qui engendrent la tribu borélienne étendue.
2. On cherche à écrire l'événement $\{Z > a\}$ en fonction des $X_n$.
3. Le supremum d'une suite est strictement supérieur à $a$ si et seulement si au moins un des termes de la suite est strictement supérieur à $a$.
4. Ainsi, on a l'égalité ensembliste : $\{Z > a\} = \bigcup_{n \in \mathbb{N}} \{X_n > a\}$.
5. Pour chaque $n$, $X_n$ est une variable aléatoire, donc $\{X_n > a\} \in \mathcal{F}$.
6. La tribu $\mathcal{F}$ est par définition stable par union dénombrable.
7. Donc, l'union infinie $\bigcup_{n \in \mathbb{N}} \{X_n > a\}$ appartient à $\mathcal{F}$.
8. Par conséquent, $\sup_n X_n$ est une variable aléatoire (mesurable).
$\blacksquare$
