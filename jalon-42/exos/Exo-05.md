# Exercice 5 : Équations Différentielles ($\bigstar$$\bigstar$$\bigstar$$\star$$\star$)

## Problème

Résoudre rigoureusement l'équation différentielle suivante, définie sur $\mathbb{R}$ :
$$1y''(t) + -4y'(t) + 4y(t) = 5 t$$

## Démonstration pas à pas

1. **Équation homogène associée :**
   $(H) : y''(t) - 4y'(t) + 4y(t) = 0$.
   Équation caractéristique : $r^2 - 4r + 4 = 0 \implies (r-2)^2 = 0$.
   Discriminant $\Delta = 0$, racine double $r_0 = 2$.
   Solution homogène : $y_H(t) = (\lambda_1 + \lambda_2 t) e^{2t}$ avec $(\lambda_1, \lambda_2) \in \mathbb{R}^2$.

2. **Recherche de la solution particulière :**
   Second membre $d(t) = 5 t$. On cherche $y_P(t) = A t + B$.
   Dérivées : $y_P'(t) = A$ et $y_P''(t) = 0$.
   Injection dans l'équation : $0 - 4A + 4(At + B) = 5 t$.
   $4At + (4B - 4A) = 5 t$.
   Par identification : $4A = 5 \implies A = \frac{5}{4}$.
   Et $4B - 4A = 0 \implies B = A = \frac{5}{4}$.
   Solution particulière : $y_P(t) = \frac{5}{4} t + \frac{5}{4}$.

3. **Solution générale complète :**
   $y(t) = (\lambda_1 + \lambda_2 t) e^{2t} + \frac{5}{4} t + \frac{5}{4}$.
