---
title: "Exercice 9 : Généralisation avec liminf : Preuve du Lemme de Fatou"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 9 : Généralisation avec liminf : Preuve du Lemme de Fatou

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Problème

Prouver rigoureusement le Lemme de Fatou : Pour toute suite $(f_n)$ de fonctions mesurables positives, $\int \liminf_{n \to \infty} f_n \le \liminf_{n \to \infty} \int f_n$. On exige l'utilisation explicite du Théorème de Convergence Monotone.

## Démonstration et Résolution

### Étape 1 : Construction d'une suite auxiliaire croissante
Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables à valeurs dans $[0, +\infty]$.
Pour forcer l'application du théorème de Beppo Levi, nous devons construire une suite croissante de fonctions. Posons, pour tout $n \in \mathbb{N}$ :
$$ g_n(x) = \inf_{k \ge n} f_k(x) $$
Comme l'infimum dénombrable de fonctions mesurables est mesurable, chaque $g_n$ est mesurable. Puisque les $f_k$ sont positives, les $g_n$ le sont aussi.

### Étape 2 : Monotonie de la suite auxiliaire
Étudions la croissance de $g_n$.
L'ensemble sur lequel porte l'infimum pour $g_{n+1}$ est $\{k \in \mathbb{N} \mid k \ge n+1\}$. Cet ensemble est strictement inclus dans l'ensemble de l'infimum pour $g_n$, qui est $\{k \in \mathbb{N} \mid k \ge n\}$.
Le minimum pris sur un ensemble plus petit est nécessairement plus grand ou égal.
Donc, pour tout $x \in X$, $g_n(x) \le g_{n+1}(x)$. La suite $(g_n)$ est croissante.

### Étape 3 : Lien avec la limite inférieure
Par définition formelle de la limite inférieure d'une suite, la limite de cette suite des infimums partiels est exactement la $\liminf$ :
$$ \lim_{n \to \infty} g_n(x) = \sup_{n \ge 0} \inf_{k \ge n} f_k(x) = \liminf_{n \to \infty} f_n(x) $$

### Étape 4 : Application du Théorème de Beppo Levi
La suite $(g_n)$ étant mesurable, positive et croissante, le Théorème de Convergence Monotone s'applique de plein droit :
$$ \int_X \left( \lim_{n \to \infty} g_n(x) \right) d\mu = \lim_{n \to \infty} \int_X g_n(x) d\mu $$
Ce qui se réécrit, avec l'Étape 3 :
$$ \int_X \left( \liminf_{n \to \infty} f_n(x) \right) d\mu = \lim_{n \to \infty} \int_X g_n(x) d\mu $$
Notons que puisque la suite numérique $(\int g_n)$ est croissante, sa limite est équivalente à sa limite inférieure : $\lim \int g_n = \liminf \int g_n$.

### Étape 5 : Majoration fondamentale et conclusion
Par définition de l'infimum partiel, pour tout $k \ge n$, $g_n(x) \le f_k(x)$.
En particulier, pour le cas limite d'égalité d'indice, pour tout $n$, on a $g_n(x) \le f_n(x)$.
La monotonie de l'intégrale implique :
$$ \int_X g_n(x) d\mu \le \int_X f_n(x) d\mu $$
Passons à la limite inférieure sur cette inégalité de suites numériques :
$$ \liminf_{n \to \infty} \int_X g_n(x) d\mu \le \liminf_{n \to \infty} \int_X f_n(x) d\mu $$
En substituant le membre de gauche par notre résultat de l'Étape 4, on obtient l'inégalité finale et absolue :
$$ \int_X \left( \liminf_{n \to \infty} f_n(x) \right) d\mu \le \liminf_{n \to \infty} \int_X f_n(x) d\mu $$
La démonstration est terminée, sans aucune ellipse, liant intrinsèquement Fatou à Beppo Levi.
