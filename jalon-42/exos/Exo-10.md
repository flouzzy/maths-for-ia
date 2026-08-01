# Exercice 10 : Équations Différentielles ($\bigstar$$\bigstar$$\bigstar$$\bigstar$$\bigstar$)

## Problème

Résoudre rigoureusement l'équation différentielle suivante, définie sur $\mathbb{R}$ :
$$1y''(t) + 3y'(t) + 2y(t) = 10 e^t$$

## Démonstration pas à pas

1. **Équation homogène associée :**
   $(H) : y''(t) + 3y'(t) + 2y(t) = 0$.
   Équation caractéristique : $r^2 + 3r + 2 = 0$.
   Discriminant $\Delta = 3^2 - 4(1)(2) = 9 - 8 = 1 > 0$.
   Racines : $r_1 = \frac{-3-1}{2} = -2$ et $r_2 = \frac{-3+1}{2} = -1$.
   Solution homogène : $y_H(t) = \lambda_1 e^{-2t} + \lambda_2 e^{-t}$ avec $(\lambda_1, \lambda_2) \in \mathbb{R}^2$.

2. **Recherche de la solution particulière :**
   Second membre $d(t) = 10 e^t$. Puisque $1$ n'est pas racine de l'équation caractéristique, on cherche $y_P(t) = A e^t$.
   Dérivées : $y_P'(t) = A e^t$ et $y_P''(t) = A e^t$.
   Injection dans l'équation : $A e^t + 3 A e^t + 2 A e^t = 6 A e^t = 10 e^t$.
   Par identification : $6A = 10 \implies A = \frac{10}{6}$.
   Solution particulière : $y_P(t) = \frac{10}{6} e^t$.

3. **Solution générale complète :**
   $y(t) = \lambda_1 e^{-2t} + \lambda_2 e^{-t} + \frac{10}{6} e^t$.
