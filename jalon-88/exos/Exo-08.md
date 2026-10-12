# Exercice 8 : Indépendance et minimum de variables géométriques

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soient $X_1$ et $X_2$ deux variables aléatoires indépendantes suivant respectivement des lois géométriques de paramètres $p_1 \in ]0,1[$ et $p_2 \in ]0,1[$.
Le support est défini sur $\mathbb{N}^* = \{{1, 2, 3, \ldots\}}$ avec $\mathbb{P}(X_i = k) = p_i(1-p_i)^{{k-1}}$.
Soit $Y = \min(X_1, X_2)$.
1. Pour tout entier $n \ge 1$, calculer $\mathbb{P}(X_1 > n)$.
2. Exprimer l'événement $\{{Y > n\}}$ en fonction d'événements liés à $X_1$ et $X_2$.
3. En déduire que $Y$ suit également une loi géométrique, dont on précisera le paramètre.

---
**Correction détaillée :**

**Question 1 : Fonction de survie d'une loi géométrique**
Soit $n \ge 1$. Par définition de la loi géométrique, la somme infinie de la probabilité est :
$$ \mathbb{P}(X_1 > n) = \sum_{{k=n+1}}^{{\infty}} \mathbb{P}(X_1 = k) = \sum_{{k=n+1}}^{{\infty}} p_1(1-p_1)^{{k-1}} $$
On effectue un changement d'indice $j = k - (n+1)$, donc quand $k = n+1$, $j=0$.
$$ \mathbb{P}(X_1 > n) = \sum_{{j=0}}^{{\infty}} p_1(1-p_1)^{{j+n}} = p_1(1-p_1)^n \sum_{{j=0}}^{{\infty}} (1-p_1)^j $$
C'est une série géométrique de raison $q = 1-p_1$ avec $|q| < 1$. Sa somme vaut $\frac{{1}}{{1-q}} = \frac{{1}}{{p_1}}$.
$$ \mathbb{P}(X_1 > n) = p_1(1-p_1)^n \frac{{1}}{{p_1}} = (1-p_1)^n $$
(Intuition : ne pas avoir de succès lors des $n$ premiers essais signifie échouer $n$ fois de suite, dont la probabilité est bien $(1-p_1)^n$).

**Question 2 : Expression de l'événement**
$Y$ est le minimum de $X_1$ et $X_2$. Dire que le minimum de deux nombres est strictement supérieur à $n$ est strictement équivalent à dire que les deux nombres sont simultanément strictement supérieurs à $n$.
$$ \{{Y > n\}} = \{{ \min(X_1, X_2) > n\}} = \{{X_1 > n\}} \cap \{{X_2 > n\}} $$

**Question 3 : Loi du minimum**
Utilisons l'expression trouvée et l'hypothèse d'indépendance :
$$ \mathbb{P}(Y > n) = \mathbb{P}(\{{X_1 > n\}} \cap \{{X_2 > n\}}) $$
Par indépendance des variables $X_1$ et $X_2$, les événements $\{{X_1 > n\}}$ et $\{{X_2 > n\}}$ sont indépendants.
$$ \mathbb{P}(Y > n) = \mathbb{P}(X_1 > n) \times \mathbb{P}(X_2 > n) $$
D'après la question 1 :
$$ \mathbb{P}(Y > n) = (1-p_1)^n \times (1-p_2)^n = ((1-p_1)(1-p_2))^n $$
Posons $1 - p = (1-p_1)(1-p_2)$, c'est-à-dire $p = 1 - (1-p_1)(1-p_2) = p_1 + p_2 - p_1 p_2$.
Alors $\mathbb{P}(Y > n) = (1-p)^n$.
Pour trouver la loi de $Y$, calculons la probabilité ponctuelle pour tout entier $k \ge 1$ :
$$ \mathbb{P}(Y = k) = \mathbb{P}(Y > k-1) - \mathbb{P}(Y > k) $$
$$ \mathbb{P}(Y = k) = (1-p)^{{k-1}} - (1-p)^k = (1-p)^{{k-1}}(1 - (1-p)) = p(1-p)^{{k-1}} $$
On reconnait l'expression exacte d'une loi géométrique.
Ainsi, le minimum de deux lois géométriques indépendantes suit une loi géométrique de paramètre $p = p_1 + p_2 - p_1 p_2$. $\blacksquare$
