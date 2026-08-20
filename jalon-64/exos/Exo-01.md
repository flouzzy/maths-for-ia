---
title: "Exercice 1 : Mesure d'un singleton et d'un segment"
difficulty: "$\bigstar\star\star\star\star$"
---

## Énoncé

1. Soit $a \in \mathbb{R}$. Démontrer, en utilisant uniquement la définition de la mesure extérieure par recouvrement d'intervalles ouverts, que la mesure extérieure du singleton $\{a\}$ est nulle, i.e., $\lambda^*(\{a\}) = 0$.
2. Soit $[a,b]$ un segment de $\mathbb{R}$ avec $a < b$. Démontrer que $\lambda^*([a,b]) = b - a$.

## Correction Détaillée

### 1. Mesure d'un singleton
Soit $\epsilon > 0$. Considérons l'intervalle ouvert $I_1 = \left] a - \frac{\epsilon}{2}, a + \frac{\epsilon}{2} \right[$.
Clairement, le singleton $\{a\}$ est inclus dans $I_1$.
La famille constituée du seul intervalle $I_1$ (en complétant par des ensembles vides si on exige une suite infinie) forme un recouvrement ouvert de $\{a\}$.
La longueur de cet intervalle est $\ell(I_1) = \left( a + \frac{\epsilon}{2} \right) - \left( a - \frac{\epsilon}{2} \right) = \epsilon$.
Par définition de la mesure extérieure, qui est l'infimum sur tous les recouvrements, nous avons :
$$\lambda^*(\{a\}) \le \ell(I_1) = \epsilon$$
Puisque la mesure extérieure est toujours à valeurs positives ou nulles (somme de longueurs positives), nous avons $0 \le \lambda^*(\{a\}) \le \epsilon$.
Cette double inégalité étant vérifiée pour tout $\epsilon > 0$ arbitrairement petit, on en déduit par passage à la limite :
$$\lambda^*(\{a\}) = 0$$

### 2. Mesure du segment $[a,b]$
**Majoration :**
Pour tout $\epsilon > 0$, considérons l'intervalle ouvert $I = \left] a - \frac{\epsilon}{2}, b + \frac{\epsilon}{2} \right[$.
Le segment $[a,b]$ est strictement inclus dans $I$. La longueur de $I$ est $\ell(I) = b - a + \epsilon$.
Ainsi, par définition de l'infimum, $\lambda^*([a,b]) \le b - a + \epsilon$.
En faisant tendre $\epsilon$ vers $0$, on obtient la majoration :
$$\lambda^*([a,b]) \le b - a$$

**Minoration :**
Soit $(I_n)_{n \in \mathbb{N}}$ un recouvrement quelconque de $[a,b]$ par des intervalles ouverts.
Comme $[a,b]$ est un espace compact (théorème de Borel-Lebesgue), il existe un sous-recouvrement fini. Soient $I_{n_1}, I_{n_2}, \dots, I_{n_k}$ ces intervalles.
Puisque l'union finie de ces intervalles recouvre l'intervalle $[a,b]$, la somme de leurs longueurs doit nécessairement être supérieure ou égale à la distance entre $a$ et $b$. (Cela se prouve rigoureusement par récurrence finie sur le nombre d'intervalles en les réordonnant).
Donc $\sum_{n=1}^{+\infty} \ell(I_n) \ge \sum_{j=1}^{k} \ell(I_{n_j}) \ge b - a$.
Comme cette inégalité est vraie pour tout recouvrement, le passage à l'infimum donne :
$$\lambda^*([a,b]) \ge b - a$$

Par double inégalité, on a bien $\lambda^*([a,b]) = b - a$.
