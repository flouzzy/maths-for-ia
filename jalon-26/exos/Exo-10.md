---
uuid: "jalon-26-exo-10"
title: "Moindres carrés"
difficulty: 4
---

# Exercice 10 : Moindres carrés (Difficulté ★★★★☆)

Soit $A \in \mathcal{M}_{m,n}(\mathbb{R})$ avec $m > n$ et de rang $n$. Soit $b \in \mathbb{R}^m$. Le système $Ax = b$ n'a en général pas de solution exacte.
On cherche à minimiser la norme euclidienne $\|Ax - b\|^2$.
1. Montrer que ce problème est équivalent à chercher la projection orthogonale de $b$ sur $\text{Im}(A)$.
2. En déduire que le vecteur $x$ optimal est solution du système dit d'équations normales : $A^T A x = A^T b$.
3. Montrer que la matrice $A^T A$ est inversible sous l'hypothèse que $A$ est de rang $n$.

## Démonstration Rigoureuse à Blanc

1. L'ensemble $\{Ax \mid x \in \mathbb{R}^n\}$ est par définition l'image de $A$, notée $\text{Im}(A)$, qui est un sous-espace vectoriel de $\mathbb{R}^m$.
   - Le problème de minimisation $\min_{x \in \mathbb{R}^n} \|Ax - b\|$ s'écrit : trouver $y \in \text{Im}(A)$ tel que $\|y - b\|$ soit minimal.
   - Par le théorème de la projection orthogonale, on sait que ce minimum est unique et est atteint exactement lorsque $y$ est la projection orthogonale de $b$ sur $\text{Im}(A)$, c'est-à-dire $y = p_{\text{Im}(A)}(b)$.
   - Le problème équivaut donc à trouver $x$ tel que $Ax = p_{\text{Im}(A)}(b)$.

2. Soit $x$ le vecteur optimal tel que $Ax = p_{\text{Im}(A)}(b)$.
   - Par propriété de la projection, le résidu $b - Ax$ est orthogonal au sous-espace $\text{Im}(A)$.
   - Cela signifie que pour tout $z \in \text{Im}(A)$, $\langle z, b - Ax \rangle = 0$.
   - Or tout $z \in \text{Im}(A)$ s'écrit $z = Ay$ pour un $y \in \mathbb{R}^n$.
   - Le produit scalaire canonique dans $\mathbb{R}^m$ est $\langle U, V \rangle = U^T V$.
   - Donc $\forall y \in \mathbb{R}^n, (Ay)^T (b - Ax) = 0$.
   - $y^T A^T (b - Ax) = 0$.
   - Cette identité doit être vraie pour tout vecteur $y$, ce qui implique que le vecteur $A^T(b - Ax)$ est nul.
   - $A^T(b - Ax) = 0 \iff A^T b - A^T A x = 0 \iff A^T A x = A^T b$.
   - C'est l'équation normale de la méthode des moindres carrés.

3. Montrons que $A^T A$ est inversible. Elle est inversible si et seulement si son noyau est réduit à $\{0\}$.
   - Soit $x \in \ker(A^T A)$. Alors $A^T A x = 0$.
   - Multiplions à gauche par $x^T$ : $x^T A^T A x = 0$.
   - $(Ax)^T (Ax) = 0 \implies \|Ax\|^2 = 0 \implies Ax = 0$.
   - Donc $x \in \ker(A)$.
   - Or par hypothèse, le rang de $A$ (matrice $m \times n$) est $n$. Par le théorème du rang, la dimension du noyau de $A$ est $n - n = 0$.
   - Donc $x = 0$.
   - On a prouvé que $\ker(A^T A) = \{0\}$, la matrice $A^T A$ (qui est de taille $n \times n$) est donc inversible. Le système normal a une solution unique.
   $\blacksquare$
