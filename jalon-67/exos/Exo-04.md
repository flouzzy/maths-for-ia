---
title: "Exercice 4"
---
## Exercice 4 : Convergence de normes dans $L^1$ $\bigstar\bigstar\star$

**Énoncé :**
Soit $f \in L^1(\mathbb{R})$. Montrer que $\lim_{n \to \infty} \int_{\mathbb{R}} |f(x)| \mathbf{1}_{[-n, n]}(x) dx = \int_{\mathbb{R}} |f(x)| dx$.

**Correction Détaillée :**
1. Posons $g_n(x) = |f(x)| \mathbf{1}_{[-n, n]}(x)$.
2. La fonction $g_n$ est mesurable et positive.
3. Pour tout $x \in \mathbb{R}$, on a $[-n, n] \subset [-(n+1), n+1]$.
4. Donc $\mathbf{1}_{[-n, n]}(x) \le \mathbf{1}_{[-(n+1), n+1]}(x)$.
5. En multipliant par $|f(x)| \ge 0$, on obtient $g_n(x) \le g_{n+1}(x)$.
   La suite $(g_n)$ est donc une suite croissante de fonctions mesurables positives.
6. La limite simple de $g_n(x)$ est $|f(x)| \lim_{n \to \infty} \mathbf{1}_{[-n, n]}(x) = |f(x)| \mathbf{1}_{\mathbb{R}}(x) = |f(x)|$.
7. D'après le théorème de convergence monotone, l'intégrale de la limite est la limite des intégrales :
   $$\int_{\mathbb{R}} |f(x)| dx = \lim_{n \to \infty} \int_{\mathbb{R}} |f(x)| \mathbf{1}_{[-n, n]}(x) dx$$
8. On a bien prouvé l'égalité demandée. Cela justifie qu'on peut toujours approcher la norme d'une fonction $L^1$ par son intégrale sur des compacts exhaustifs.
