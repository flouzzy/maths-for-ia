---
title: "Exercice 08 : Lemme de Borel-Cantelli via l'intégration (Partie 1)"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 08 : Lemme de Borel-Cantelli via l'intégration (Partie 1)

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit $(A_n)$ une suite d'ensembles mesurables. On pose $f(x) = \sum_{n=1}^\infty \mathbf{1}_{A_n}(x)$, le nombre de fois où $x$ appartient aux ensembles. Montrer que si $\sum \mu(A_n) < \infty$, alors $f(x)$ est finie presque partout.

---

## Correction détaillée

1. **Construction d'une suite de fonctions positives :**
Posons $f_N = \sum_{n=1}^N \mathbf{1}_{A_n}$. Chaque $f_N$ est une fonction simple positive.
L'intégrale de $f_N$ est, par linéarité (démontrée sur les fonctions simples) :
$$ \int f_N \, d\mu = \sum_{n=1}^N \mu(A_n) $$

2. **Monotonie et supremum :**
La suite $(f_N)$ est croissante et tend vers $f$. $f$ est mesurable positive.
Par la propriété de croissance de l'intégrale, $\int f_N \, d\mu \le \int f \, d\mu$.
Si le théorème de convergence monotone était déjà prouvé (Jalon 67), on passerait à la limite, mais on peut ici raisonner directement avec le supremum.
Comme $\int f_N \, d\mu$ est majoré par $\sum_{n=1}^\infty \mu(A_n) = M < \infty$, on admettra (ou on utilisera Beppo-Levi qui sera prouvé formellement plus tard) que $\int f \, d\mu \le M < \infty$.

3. **Finitude presque partout :**
On a montré dans le cours que si $\int f \, d\mu < \infty$, alors $f$ est finie presque partout.
Preuve (rappel) : Soit $E = \{x \mid f(x) = +\infty\}$. Pour tout entier $k$, $f(x) \ge k \mathbf{1}_E(x)$.
Donc $\int f \, d\mu \ge k \mu(E)$. Puisque $\int f \, d\mu < \infty$, pour que cela tienne pour tout $k$, il faut impérativement $\mu(E) = 0$.
Donc l'ensemble des points $x$ appartenant à une infinité de $A_n$ (pour lesquels $f(x) = +\infty$) est de mesure nulle.
