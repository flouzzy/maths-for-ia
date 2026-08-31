---
title: "Application directe du TCM"
difficulty: $\bigstar\star\star\star\star$
---
# Application directe du TCM
**Énoncé :**
Soit $f_n(x) = \mathbf{1}_{[0, n]}(x) \cdot \left(1 - \frac{x}{n}\right)^n$. Calculer $\lim_{n \to +\infty} \int_0^{+\infty} f_n(x) dx$.

**Correction :**
1. Pour tout $x \in \mathbb{R}^+$, $\lim_{n \to \infty} f_n(x) = e^{-x}$. Posons $f(x) = e^{-x}$.
2. La suite $(f_n)$ est-elle croissante ? Soit $x \ge 0$. Pour $n > x$, $f_n(x) = (1 - \frac{x}{n})^n$.
   On a $\ln f_n(x) = n \ln(1 - \frac{x}{n})$. La fonction $y \mapsto \frac{1}{y} \ln(1 - xy)$ est croissante sur $(0, 1/x)$. Donc $(f_n)$ est croissante.
3. Les $f_n$ sont positives et mesurables.
4. D'après le Théorème de Convergence Monotone :
   $\lim_{n \to \infty} \int_0^{+\infty} f_n(x) dx = \int_0^{+\infty} e^{-x} dx$.
5. Or, $\int_0^{+\infty} e^{-x} dx = \left[ -e^{-x} \right]_0^{+\infty} = 1$.
   Donc la limite est $1$.
