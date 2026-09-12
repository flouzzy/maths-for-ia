---
title: "Exercice 2 : Invariance par translation de la mesure extérieure"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

## Énoncé

Soit $A$ une partie de $\mathbb{R}$. Pour tout $x \in \mathbb{R}$, on définit la translation de $A$ par le vecteur $x$ comme l'ensemble :
$$A + x = \{ y + x \mid y \in A \}$$
Démontrer formellement que la mesure extérieure de Lebesgue est invariante par translation, c'est-à-dire :
$$\forall A \subset \mathbb{R}, \forall x \in \mathbb{R}, \quad \lambda^*(A + x) = \lambda^*(A)$$

## Correction Détaillée

Nous allons démontrer l'égalité en procédant par double inégalité (majoration et minoration).
Soit $A \subset \mathbb{R}$ et $x \in \mathbb{R}$.

**Première étape : $\lambda^*(A+x) \le \lambda^*(A)$**
Si $\lambda^*(A) = +\infty$, l'inégalité est trivialement vérifiée. Supposons donc que $\lambda^*(A) < +\infty$.
Soit $\epsilon > 0$. Par définition de la mesure extérieure, il existe un recouvrement de $A$ par une suite d'intervalles ouverts $(I_n)_{n \in \mathbb{N}^*}$ telle que :
$$A \subset \bigcup_{n=1}^{+\infty} I_n \quad \text{et} \quad \sum_{n=1}^{+\infty} \ell(I_n) \le \lambda^*(A) + \epsilon$$

Considérons les intervalles translatés $J_n = I_n + x$.
Si $I_n = ]a_n, b_n[$, alors $J_n = ]a_n + x, b_n + x[$.
Les ensembles $J_n$ sont clairement des intervalles ouverts. De plus, leur longueur est préservée par translation :
$$\ell(J_n) = (b_n + x) - (a_n + x) = b_n - a_n = \ell(I_n)$$

Vérifions qu'ils recouvrent $A+x$. Soit $z \in A+x$. Par définition, il existe $y \in A$ tel que $z = y + x$. Comme $(I_n)$ recouvre $A$, il existe un indice $k$ tel que $y \in I_k$. Donc $z = y + x \in I_k + x = J_k$. Ainsi :
$$A+x \subset \bigcup_{n=1}^{+\infty} J_n$$

Par définition de l'infimum pour la mesure extérieure de $A+x$, on a :
$$\lambda^*(A+x) \le \sum_{n=1}^{+\infty} \ell(J_n) = \sum_{n=1}^{+\infty} \ell(I_n) \le \lambda^*(A) + \epsilon$$
Cette inégalité étant vraie pour tout $\epsilon > 0$, en faisant tendre $\epsilon$ vers $0$, on obtient :
$$\lambda^*(A+x) \le \lambda^*(A)$$

**Deuxième étape : $\lambda^*(A) \le \lambda^*(A+x)$**
Nous appliquons astucieusement le résultat de la première étape à l'ensemble $B = A + x$ et à la translation par le vecteur $-x$.
Par la première inégalité, nous avons :
$$\lambda^*(B + (-x)) \le \lambda^*(B)$$
En remplaçant $B$ par $A+x$, il vient :
$$\lambda^*((A+x) - x) \le \lambda^*(A+x)$$
$$\lambda^*(A) \le \lambda^*(A+x)$$

**Conclusion :**
Les deux inégalités impliquent l'égalité absolue : $\lambda^*(A + x) = \lambda^*(A)$. La mesure extérieure est invariante par translation sur tout $\mathcal{P}(\mathbb{R})$.
