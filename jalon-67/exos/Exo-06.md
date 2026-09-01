---
title: "Exercice 6 : Un contre-exemple classique avec perte de masse"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 6 : Un contre-exemple classique avec perte de masse

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $f_n = n \mathbf{1}_{]0, 1/n]}$. Calculer $\lim \int f_n$ et $\int \lim f_n$. Expliquer mathématiquement pourquoi le théorème de Beppo Levi échoue et identifier l'hypothèse violée.

## Correction Détaillée

1. Déterminons la limite simple $f(x) = \lim_{n \to \infty} f_n(x)$ pour tout $x \in \mathbb{R}$.
   - Si $x \le 0$, $f_n(x) = 0$ pour tout $n$, donc $\lim f_n(x) = 0$.
   - Si $x > 0$, il existe un entier $N$ tel que $1/N < x$. Pour tout $n \ge N$, $x \notin ]0, 1/n]$, donc $f_n(x) = 0$. La limite est donc aussi $0$.
   Conclusion : La suite de fonctions converge simplement vers la fonction nulle $f = 0$.
2. Calculons l'intégrale de la limite :
   $$\int_{\mathbb{R}} \lim_{n \to \infty} f_n(x) dx = \int_{\mathbb{R}} 0 dx = 0$$
3. Calculons l'intégrale de $f_n$ pour un $n$ fixé :
   $$\int_{\mathbb{R}} f_n(x) dx = \int_0^{1/n} n dx = n \left( \frac{1}{n} - 0 \right) = 1$$
4. Limite des intégrales :
   $$\lim_{n \to \infty} \int_{\mathbb{R}} f_n(x) dx = \lim_{n \to \infty} 1 = 1$$
5. On observe que $1 \neq 0$. L'égalité du théorème de Beppo Levi n'est pas vérifiée.
6. **L'hypothèse violée :** Le théorème de Beppo Levi exige que la suite de fonctions soit **croissante**.
   Vérifions si $(f_n)$ est croissante : $f_1 = \mathbf{1}_{]0, 1]}$, et $f_2 = 2 \mathbf{1}_{]0, 1/2]}$.
   Prenons $x = 3/4$. On a $f_1(3/4) = 1$ et $f_2(3/4) = 0$.
   Donc $f_2(3/4) < f_1(3/4)$. La suite n'est pas croissante, ce qui explique l'échec du théorème. Toute la "masse" s'échappe vers 0.
