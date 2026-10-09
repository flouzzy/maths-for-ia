# Exercice 3

**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé

Soit $X$ une variable aléatoire réelle. Quelle est la tribu engendrée par $X$, notée $\sigma(X)$, si $X$ est une fonction constante $X(\omega) = c$ pour tout $\omega \in \Omega$ ?

## Correction Détaillée

**Correction de l'exercice 3 :**

1. Par définition, $\sigma(X) = \{ X^{-1}(B) \mid B \in \mathcal{B}(\mathbb{R}) \}$.
2. Évaluons $X^{-1}(B)$ pour un borélien $B$.
   - Si la constante $c \in B$, alors pour tout $\omega \in \Omega$, $X(\omega) = c \in B$, d'où $X^{-1}(B) = \Omega$.
   - Si $c \notin B$, alors aucun $\omega \in \Omega$ ne vérifie $X(\omega) \in B$, d'où $X^{-1}(B) = \emptyset$.
3. Ainsi, la tribu engendrée par une constante ne contient que deux éléments : $\Omega$ et $\emptyset$.
4. Conclusion : $\sigma(X) = \{\emptyset, \Omega\}$, c'est la tribu triviale ou grossière.
$\blacksquare$
