# Exercice 8 : Continuité d'une forme linéaire par Riesz

## Énoncé

Dans $L^2(0, 1)$, l'application $L(f) = \int_0^{1/2} f(t) dt$ est-elle continue ? Trouver son représentant de Riesz.

*Niveau de difficulté :* $\bigstar\bigstar\bigstar\bigstar\star$

## Correction

1. **Reformulation :** On peut réécrire $L(f) = \int_0^1 f(t) \mathbf{1}_{[0, 1/2]}(t) dt$.
2. **Identification :** Ceci a exactement la forme d'un produit scalaire $\langle f, u \rangle$ dans $L^2(0, 1)$ avec $u(t) = \mathbf{1}_{[0, 1/2]}(t)$.
3. **Continuité :** Par l'inégalité de Cauchy-Schwarz, $|L(f)| = |\langle f, u \rangle| \le \|f\|_2 \|u\|_2$.
4. **Calcul de la norme :** $\|u\|_2 = \sqrt{\int_0^{1/2} 1^2 dt} = \sqrt{1/2}$. Donc $L$ est continue de norme $1/\sqrt{2}$.
5. **Conclusion :** Le représentant de Riesz est la fonction indicatrice $u = \mathbf{1}_{[0, 1/2]}$, c'est un vecteur de $L^2$ qui encode l'opération de moyenne sur la première moitié de l'intervalle.
