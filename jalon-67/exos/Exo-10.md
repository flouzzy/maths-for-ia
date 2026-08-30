---
title: "Exercice 10 : Limite d'intégrale de Haar"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 10 : Limite d'intégrale de Haar

## Énoncé

Soit $X = [0, 1]$ muni de la mesure de Lebesgue $\lambda$.
Soit $(A_n)$ une suite disjointe d'ensembles mesurables de $X$, et $c_n \ge 0$.
Soit la fonction définie par $f(x) = \sum_{n=1}^\infty c_n \mathbf{1}_{A_n}(x)$.
En utilisant le théorème de Beppo Levi, démontrer formellement que $\int_X f d\lambda = \sum_{n=1}^\infty c_n \lambda(A_n)$.

## Correction

1. **Identification de la série :**
La fonction est définie de manière abstraite comme une série infinie.
Posons $u_n(x) = c_n \mathbf{1}_{A_n}(x)$.
Chaque $u_n$ est la constante positive $c_n$ multipliée par une indicatrice d'un ensemble mesurable. Elle est donc mesurable et positive pour tout $x$.
On a par définition $f(x) = \sum_{n=1}^\infty u_n(x)$.

2. **Interversion :**
Par le corollaire d'intégration terme à terme du théorème de convergence monotone de Lebesgue (série de fonctions positives), nous sommes autorisés à intervertir le signe somme intégrale $\int$ avec la série discrète $\sum$.
$$ \int_X f(x) d\lambda = \int_X \left( \sum_{n=1}^\infty u_n(x) \right) d\lambda = \sum_{n=1}^\infty \int_X u_n(x) d\lambda. $$

3. **Calcul de l'intégrale élémentaire :**
Pour un rang $n$, l'intégrale de la fonction simple correspondante est la définition de base de l'intégrale de Lebesgue : l'aire sous le rectangle abstrait.
$$ \int_X u_n(x) d\lambda = \int_X c_n \mathbf{1}_{A_n}(x) d\lambda = c_n \lambda(A_n). $$

4. **Conclusion de la preuve :**
En remplaçant ce terme scalaire dans la sommation, il vient irrémédiablement :
$$ \int_X f d\lambda = \sum_{n=1}^\infty c_n \lambda(A_n). $$
Ce résultat, d'une grande abstraction, permet de construire l'intégrale des fonctions en "escalier infinies", très utilisées dans les ondelettes de Haar ou la décomposition temps-fréquence en traitement du signal.
