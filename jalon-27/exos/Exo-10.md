---
uuid: "jalon-27-exo-10"
title: "Exercice 10 : Rayleigh quotient"
---
# Exercice 10 : Rayleigh quotient

**Difficulté :** ★★★★★

## Énoncé

Pour une matrice symétrique réelle $A$, montrer que le quotient de Rayleigh $R(x) = \frac{x^T A x}{x^T x}$ vérifie $\lambda_{\min} \leq R(x) \leq \lambda_{\max}$ où $\lambda_{\min}, \lambda_{\max}$ sont les valeurs propres extrêmes.

## Démonstration sans ellipse

Soit $A$ une matrice symétrique. D'après le théorème spectral, il existe une base orthonormée de vecteurs propres $(e_1, \dots, e_n)$ avec $Ae_i = \lambda_i e_i$.
Toute valeur propre $\lambda_i$ vérifie $\lambda_{\min} \leq \lambda_i \leq \lambda_{\max}$.
Soit $x \neq 0$. Décomposons $x$ dans la base $(e_i)$ : $x = \sum_{i=1}^n x_i e_i$.
Alors $x^T x = \sum_{i=1}^n x_i^2$.
Et $Ax = \sum_{i=1}^n x_i \lambda_i e_i$, donc $x^T A x = \sum_{i=1}^n \lambda_i x_i^2$.
En minorant chaque $\lambda_i$ par $\lambda_{\min}$ :
$$ x^T A x \geq \sum_{i=1}^n \lambda_{\min} x_i^2 = \lambda_{\min} \sum_{i=1}^n x_i^2 = \lambda_{\min} x^T x $$
De même, en majorant :
$$ x^T A x \leq \lambda_{\max} x^T x $$
En divisant par $x^T x > 0$, on obtient bien :
$$ \lambda_{\min} \leq \frac{x^T A x}{x^T x} \leq \lambda_{\max} $$
L'égalité est atteinte pour les vecteurs propres correspondants. $\blacksquare$
