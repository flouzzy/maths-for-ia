---
title: "Exercice 10 : Matrice de Gram et indépendance linéaire"
difficulty: 5
---

## Énoncé Formel et Typage Rigoureux
Soit $\mathbb{K}$ un corps commutatif (typiquement $\mathbb{R}$ ou $\mathbb{C}$) et $E$ un $\mathbb{K}$-espace vectoriel. L'enjeu est d'éprouver la consistance algébrique des formes bilinéaires.
Soit $E$ un espace préhilbertien réel. Pour une famille de $k$ vecteurs $u_1, ..., u_k$ de $E$, on définit la Matrice de Gram $G(u_1, ..., u_k) \in M_k(\mathbb{R})$ par $G_{i,j} = \langle u_i, u_j \rangle$.
1. Montrer que $G$ est une matrice symétrique.
2. Pour tout vecteur $X = (x_1, ..., x_k)^T \in \mathbb{R}^k$, exprimer le produit $X^T G X$ sous la forme d'une norme au carré dans $E$.
3. En déduire que la matrice de Gram $G$ est définie positive (c'est-à-dire $X^T G X > 0$ pour tout $X \neq 0$) si et seulement si la famille $(u_1, ..., u_k)$ est linéairement indépendante.

## Preuve Analytique Pas-à-Pas (Zéro Ellipse)
La démarche déductive exige une formalisation intégrale sans ellipse.
**1. Symétrie de la matrice :**
L'élément général est $G_{i,j} = \langle u_i, u_j \rangle$.
Puisque le produit scalaire sur un espace réel est symétrique, on a :
$G_{j,i} = \langle u_j, u_i \rangle = \langle u_i, u_j \rangle = G_{i,j}$.
Donc la matrice $G$ est bien symétrique ($G^T = G$).

**2. Expression de la forme quadratique :**
Soit $X = (x_1, ..., x_k)^T$ un vecteur colonne.
Calculons $X^T G X$ par la formule explicite :
$X^T G X = \sum_{i=1}^k \sum_{j=1}^k x_i G_{i,j} x_j$
Substituons la définition de $G_{i,j}$ :
$X^T G X = \sum_{i=1}^k \sum_{j=1}^k x_i \langle u_i, u_j \rangle x_j$
Par bilinéarité du produit scalaire, nous pouvons faire entrer les scalaires $x_i$ et $x_j$ à l'intérieur :
$X^T G X = \sum_{i=1}^k \sum_{j=1}^k \langle x_i u_i, x_j u_j \rangle$
En sortant les sommes à l'intérieur du produit scalaire :
$X^T G X = \langle \sum_{i=1}^k x_i u_i, \sum_{j=1}^k x_j u_j \rangle$
Posons le vecteur $V = \sum_{i=1}^k x_i u_i \in E$. Alors l'expression est $\langle V, V \rangle$.
Par définition de la norme induite :
$X^T G X = \| \sum_{i=1}^k x_i u_i \|^2$.

**3. Caractérisation de l'indépendance linéaire :**
Nous devons prouver l'équivalence : $G$ est définie positive $\iff$ $(u_1, ..., u_k)$ est une famille libre.

**Sens direct ($\implies$) : Supposons $G$ définie positive.**
On a donc $X^T G X = 0 \implies X = 0$.
Soit une combinaison linéaire nulle des vecteurs $u_i$ : $\sum_{i=1}^k x_i u_i = 0_E$.
Alors la norme au carré de ce vecteur est nulle : $\| \sum_{i=1}^k x_i u_i \|^2 = 0$.
D'après la question 2, cela équivaut à $X^T G X = 0$, où $X$ est le vecteur des coefficients $(x_i)$.
Puisque $G$ est définie positive, cela implique obligatoirement $X = 0$, donc tous les coefficients $x_i$ sont nuls.
La famille $(u_1, ..., u_k)$ est bien linéairement indépendante (libre).

**Sens réciproque ($\impliedby$) : Supposons que $(u_1, ..., u_k)$ est une famille libre.**
Soit $X \in \mathbb{R}^k$. D'après la question 2, $X^T G X = \| \sum_{i=1}^k x_i u_i \|^2$.
Puisqu'une norme au carré est toujours positive, on a déjà $X^T G X \ge 0$.
Si $X^T G X = 0$, alors $\| \sum_{i=1}^k x_i u_i \|^2 = 0$, ce qui implique que le vecteur est nul : $\sum_{i=1}^k x_i u_i = 0_E$.
Or la famille est libre (hypothèse). La seule solution pour une combinaison linéaire nulle est d'avoir tous les coefficients nuls.
Donc $x_1 = 0, ..., x_k = 0$, ce qui signifie $X = 0$.
Ainsi, $X^T G X = 0 \implies X = 0$. Ceci, combiné à la positivité, montre que $G$ est définie positive.

**Conclusion :** L'inversibilité (et le caractère défini positif) de la matrice de Gram est un test parfait, purement numérique, de l'indépendance linéaire d'une famille de vecteurs.
