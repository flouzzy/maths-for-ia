---
uuid: "exo-67-04"
title: "Exercice 04 : Démonstration d'une identité avec le logarithme"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 04 : Démonstration d'une identité avec le logarithme ($\bigstar\bigstar\star\star\star$)

## Énoncé

Montrer que $\int_0^1 \frac{-\ln(1-x)}{x} dx = \frac{\pi^2}{6}$ en utilisant le développement en série entière du logarithme.

## Corrigé Rigoureux

1. **Série :** Pour $x \in ]0, 1[$, $-\ln(1-x) = \sum_{n=1}^\infty \frac{x^n}{n}$. En divisant par $x > 0$, on obtient $\frac{-\ln(1-x)}{x} = \sum_{n=1}^\infty \frac{x^{n-1}}{n}$.
2. **Positivité :** Chaque terme $u_n(x) = \frac{x^{n-1}}{n}$ est positif sur $]0, 1[$.
3. **Beppo Levi :** On peut intervertir l'intégrale et la somme :
$$\int_0^1 \sum_{n=1}^\infty \frac{x^{n-1}}{n} dx = \sum_{n=1}^\infty \int_0^1 \frac{x^{n-1}}{n} dx$$
4. **Calcul de l'intégrale du terme général :**
$\int_0^1 \frac{x^{n-1}}{n} dx = \frac{1}{n} \left[ \frac{x^n}{n} \right]_0^1 = \frac{1}{n^2}$.
5. **Conclusion :** La somme est donc $\sum_{n=1}^\infty \frac{1}{n^2}$, qui est connue pour valoir $\frac{\pi^2}{6}$ (Problème de Bâle).
