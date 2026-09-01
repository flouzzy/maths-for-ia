---
title: "Exercice 9 : Limite et mesure de densité"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 9 : Limite et mesure de densité

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit $f$ une fonction mesurable sur $\mathbb{R}$ à valeurs dans $[0, +\infty]$. On définit pour tout borélien $A$ la mesure de densité : $\nu(A) = \int_A f d\lambda$. Montrer en utilisant le théorème de Beppo Levi que $\nu$ est bien une mesure (en particulier, démontrer la $\sigma$-additivité).

## Correction Détaillée

1. Pour montrer que $\nu$ est une mesure, il faut vérifier deux points : $\nu(\emptyset) = 0$ et la $\sigma$-additivité.
2. $\nu(\emptyset) = \int_\emptyset f d\lambda = \int \mathbf{1}_\emptyset f d\lambda = \int 0 d\lambda = 0$.
3. Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'ensembles boréliens disjoints deux à deux. Posons $A = \bigcup_{n=0}^\infty A_n$.
   On veut montrer que $\nu(A) = \sum_{n=0}^\infty \nu(A_n)$.
4. Exprimons $\nu(A)$ avec une intégrale :
   $$\nu(A) = \int_A f d\lambda = \int_{\mathbb{R}} f \mathbf{1}_A d\lambda$$
5. Puisque les $A_n$ sont disjoints, la fonction indicatrice de leur union est la somme des fonctions indicatrices :
   $$\mathbf{1}_A = \sum_{n=0}^\infty \mathbf{1}_{A_n}$$
6. Ainsi, on cherche à intégrer la fonction $g(x) = f(x) \sum_{n=0}^\infty \mathbf{1}_{A_n}(x) = \sum_{n=0}^\infty f(x) \mathbf{1}_{A_n}(x)$.
7. Posons $u_n(x) = f(x) \mathbf{1}_{A_n}(x)$. Chaque $u_n$ est mesurable (car $f$ et $\mathbf{1}_{A_n}$ le sont) et **positive** (car $f \ge 0$).
8. Nous sommes exactement dans les conditions du corollaire du théorème de Beppo Levi pour les séries de fonctions positives. On peut intervertir l'intégrale et la somme :
   $$\nu(A) = \int_{\mathbb{R}} \left( \sum_{n=0}^\infty u_n \right) d\lambda = \sum_{n=0}^\infty \int_{\mathbb{R}} u_n d\lambda$$
9. Or, $\int_{\mathbb{R}} u_n d\lambda = \int_{\mathbb{R}} f \mathbf{1}_{A_n} d\lambda = \int_{A_n} f d\lambda = \nu(A_n)$.
10. On obtient bien :
    $$\nu(A) = \sum_{n=0}^\infty \nu(A_n)$$
    Ceci démontre la $\sigma$-additivité de $\nu$. L'intégrale d'une fonction positive permet de construire une nouvelle mesure. Beppo Levi est le garant axiomatique de cette construction.
