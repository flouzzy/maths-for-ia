---
uuid: "exo-67-01"
title: "Exercice 01 : Application directe sur une série de fonctions basique"
difficulty: "$\star\star\star\star\star$"
---

# Exercice 01 : Application directe sur une série de fonctions basique ($\star\star\star\star\star$)

## Énoncé

Soit $f_n(x) = \sum_{k=1}^n x^k$ pour $x \in [0, 1[$. Calculer $\lim_{n \to \infty} \int_0^{1/2} f_n(x) dx$.

## Corrigé Rigoureux

1. **Mesurabilité et positivité :** Les fonctions $f_n(x)$ sont polynomiales, donc continues et mesurables. Pour $x \in [0, 1/2]$, $x^k \ge 0$, donc $f_n(x) \ge 0$.
2. **Monotonie :** $f_{n+1}(x) - f_n(x) = x^{n+1} \ge 0$. La suite est croissante.
3. **Application de Beppo Levi :** $\lim_{n \to \infty} \int_0^{1/2} f_n(x) dx = \int_0^{1/2} \lim_{n \to \infty} f_n(x) dx$.
La limite est la série géométrique $\sum_{k=1}^\infty x^k = \frac{x}{1-x}$.
Donc $\int_0^{1/2} \frac{x}{1-x} dx = \int_0^{1/2} \left(\frac{1}{1-x} - 1\right) dx = [-\ln(1-x) - x]_0^{1/2} = \ln(2) - \frac{1}{2}$.
