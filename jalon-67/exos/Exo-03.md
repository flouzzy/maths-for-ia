---
uuid: "exo-67-03"
title: "Exercice 03 : Calcul d'une intégrale paramétrée par limite de suites croissantes"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 03 : Calcul d'une intégrale paramétrée par limite de suites croissantes ($\bigstar\bigstar\star\star\star$)

## Énoncé

Évaluer l'intégrale $I = \int_0^\infty e^{-x} \sum_{n=1}^\infty \frac{x^{n-1}}{n!} dx$.

## Corrigé Rigoureux

1. **Positivité :** Les fonctions $u_n(x) = e^{-x} \frac{x^{n-1}}{n!}$ sont positives et mesurables sur $]0, \infty[$.
2. **Beppo Levi :** On peut permuter l'intégrale et la somme :
$$I = \sum_{n=1}^\infty \int_0^\infty e^{-x} \frac{x^{n-1}}{n!} dx$$
3. **Fonction Gamma :** L'intégrale correspondante s'exprime avec la fonction Gamma : $\int_0^\infty e^{-x} x^{n-1} dx = \Gamma(n) = (n-1)!$.
Ainsi, $\int_0^\infty e^{-x} \frac{x^{n-1}}{n!} dx = \frac{(n-1)!}{n!} = \frac{1}{n}$.
La somme devient $I = \sum_{n=1}^\infty \frac{1}{n}$, qui diverge vers $+\infty$.
