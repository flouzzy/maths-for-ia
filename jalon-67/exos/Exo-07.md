---
title: "Exercice 7 : Application aux espaces de suites (l_1)"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 7 : Application aux espaces de suites (l_1)

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Considérons $\mathbb{N}$ muni de la tribu discrète $\mathcal{P}(\mathbb{N})$ et de la mesure de comptage $\mu$. Montrer que l'intégrale d'une fonction $f : \mathbb{N} \to \mathbb{R}_+$ par rapport à $\mu$ coïncide avec la série $\sum_{n=0}^\infty f(n)$, en utilisant le théorème de convergence monotone.

## Correction Détaillée

1. L'espace mesuré est $(\mathbb{N}, \mathcal{P}(\mathbb{N}), \mu)$ où $\mu(A) = \mathrm{card}(A)$.
2. Soit $f : \mathbb{N} \to \mathbb{R}_+$ une fonction arbitraire (toutes sont mesurables sur $\mathcal{P}(\mathbb{N})$).
3. On peut exprimer $f$ comme une limite d'une suite de fonctions à support fini. Définissons la suite de fonctions $(f_N)_{N \in \mathbb{N}}$ par :
   $$f_N(n) = \begin{cases} f(n) & \text{si } n \le N \\ 0 & \text{si } n > N \end{cases}$$
   Autrement dit, $f_N = f \cdot \mathbf{1}_{\{0, 1, \dots, N\}}$.
4. Propriétés de la suite $(f_N)$ :
   - Positivité : $f_N \ge 0$.
   - Croissance : Pour un $n$ fixé, si $N$ augmente, $f_N(n)$ reste constant (égal à $f(n)$) dès que $N \ge n$, et vaut $0$ avant. La suite est donc croissante.
   - Limite : $\lim_{N \to \infty} f_N(n) = f(n)$ pour tout $n \in \mathbb{N}$.
5. Chaque $f_N$ est une fonction étagée simple, prenant les valeurs $f(0), \dots, f(N)$ sur les singletons $\{0\}, \dots, \{N\}$, et 0 ailleurs.
   Par définition de l'intégrale d'une fonction étagée :
   $$\int_{\mathbb{N}} f_N d\mu = \sum_{k=0}^N f(k) \mu(\{k\}) = \sum_{k=0}^N f(k) \times 1 = \sum_{k=0}^N f(k)$$
6. Appliquons le théorème de Beppo Levi à la suite $(f_N)$ :
   $$\int_{\mathbb{N}} f d\mu = \int_{\mathbb{N}} \left( \lim_{N \to \infty} f_N \right) d\mu = \lim_{N \to \infty} \int_{\mathbb{N}} f_N d\mu$$
7. En remplaçant par l'expression de l'intégrale de $f_N$ :
   $$\int_{\mathbb{N}} f d\mu = \lim_{N \to \infty} \sum_{k=0}^N f(k) = \sum_{k=0}^\infty f(k)$$
8. Conclusion : L'intégrale de Lebesgue par rapport à la mesure de comptage unifie la notion d'intégration et de sommation de séries discrètes.
