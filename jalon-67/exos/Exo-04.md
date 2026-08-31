---
title: "Continuité par ensembles croissants"
difficulty: $\bigstar\bigstar\bigstar\star\star$
---
# Continuité par ensembles croissants
**Énoncé :**
Soit $f$ une fonction mesurable positive et intégrable sur $(X, \mathcal{M}, \mu)$. Soit $(A_n)$ une suite croissante de sous-ensembles mesurables, $\bigcup A_n = X$.
Montrer que $\lim_{n \to \infty} \int_{A_n} f d\mu = \int_X f d\mu$.

**Correction :**
1. Posons $f_n = f \cdot \mathbf{1}_{A_n}$.
2. Puisque $f \ge 0$ et $A_n \subset A_{n+1}$, on a pour tout $x$, $\mathbf{1}_{A_n}(x) \le \mathbf{1}_{A_{n+1}}(x)$.
   Donc $f_n(x) \le f_{n+1}(x)$. La suite $(f_n)$ est croissante, positive et mesurable.
3. Pour tout $x \in X$, il existe $N$ tel que $x \in A_N$, donc pour $n \ge N$, $x \in A_n$.
   Ainsi $\lim_{n \to \infty} \mathbf{1}_{A_n}(x) = 1$. Donc $f_n$ converge point par point vers $f \cdot 1 = f$.
4. Par le TCM :
   $\lim_{n \to \infty} \int_X f_n d\mu = \int_X f d\mu$.
5. Or $\int_X f_n d\mu = \int_X f \cdot \mathbf{1}_{A_n} d\mu = \int_{A_n} f d\mu$. La proposition est démontrée.
