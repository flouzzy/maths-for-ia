---
title: "Exercice 1 : Produit scalaire canonique et inégalité triangulaire dans $\mathbb{R}^n$"
difficulty: 1
---

## Énoncé
Soit $E = \mathbb{R}^n$ muni du produit scalaire canonique $\langle x, y \rangle = \sum_{i=1}^n x_i y_i$.
1. Démontrer que pour tout $x, y \in E$, $\|x + y\|^2 = \|x\|^2 + 2\langle x, y \rangle + \|y\|^2$.
2. En déduire, en utilisant l'inégalité de Cauchy-Schwarz, l'inégalité triangulaire : $\|x + y\| \le \|x\| + \|y\|$.

## Correction Détaillée
1. **Développement de la norme au carré :**
   Par définition de la norme associée au produit scalaire :
   $$\|x + y\|^2 = \langle x + y, x + y \rangle$$
   Par bilinéarité (linéarité à gauche puis à droite) :
   $$\langle x + y, x + y \rangle = \langle x, x + y \rangle + \langle y, x + y \rangle$$
   $$\langle x + y, x + y \rangle = \langle x, x \rangle + \langle x, y \rangle + \langle y, x \rangle + \langle y, y \rangle$$
   Puisque le produit scalaire est symétrique (sur $\mathbb{R}$), $\langle y, x \rangle = \langle x, y \rangle$.
   $$\|x + y\|^2 = \|x\|^2 + 2\langle x, y \rangle + \|y\|^2$$

2. **Preuve de l'inégalité triangulaire :**
   D'après la question 1, on a :
   $$\|x + y\|^2 = \|x\|^2 + 2\langle x, y \rangle + \|y\|^2$$
   Or, pour tout réel $a$, on a $a \le |a|$. Donc :
   $$\langle x, y \rangle \le |\langle x, y \rangle|$$
   Ce qui donne :
   $$\|x + y\|^2 \le \|x\|^2 + 2|\langle x, y \rangle| + \|y\|^2$$
   D'après l'inégalité de Cauchy-Schwarz, on sait que $|\langle x, y \rangle| \le \|x\| \cdot \|y\|$. On substitue :
   $$\|x + y\|^2 \le \|x\|^2 + 2\|x\|\|y\| + \|y\|^2$$
   Le membre de droite est un produit remarquable :
   $$\|x + y\|^2 \le (\|x\| + \|y\|)^2$$
   Puisque les normes sont des quantités positives, la fonction racine carrée, strictement croissante sur $\mathbb{R}^+$, conserve l'ordre. On obtient donc :
   $$\|x + y\| \le \|x\| + \|y\|$$
   Ce qui achève la démonstration.
