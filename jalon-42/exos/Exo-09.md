# Exercice 9 : Équations Différentielles ($\bigstar$$\bigstar$$\bigstar$$\bigstar$$\bigstar$)

## Problème

Résoudre rigoureusement l'équation différentielle suivante, définie sur $\mathbb{R}$ :
$$1y''(t) + 0y'(t) + 9y(t) = 9 \cos(2t)$$

## Démonstration pas à pas

1. **Équation homogène associée :**
   $(H) : y''(t) + 9y(t) = 0$.
   Équation caractéristique : $r^2 + 9 = 0$.
   Discriminant $\Delta = -36 < 0$. Racines complexes : $r = \pm 3i$.
   Solution homogène : $y_H(t) = \lambda_1 \cos(3t) + \lambda_2 \sin(3t)$ avec $(\lambda_1, \lambda_2) \in \mathbb{R}^2$.

2. **Recherche de la solution particulière :**
   Second membre $d(t) = 9 \cos(2t)$. Puisque $2i$ n'est pas racine, on cherche $y_P(t) = A \cos(2t)$.
   Dérivées : $y_P'(t) = -2A \sin(2t)$ et $y_P''(t) = -4A \cos(2t)$.
   Injection dans l'équation : $-4A \cos(2t) + 9A \cos(2t) = 5A \cos(2t) = 9 \cos(2t)$.
   Par identification : $5A = 9 \implies A = \frac{9}{5}$.
   Solution particulière : $y_P(t) = \frac{9}{5} \cos(2t)$.

3. **Solution générale complète :**
   $y(t) = \lambda_1 \cos(3t) + \lambda_2 \sin(3t) + \frac{9}{5} \cos(2t)$.
