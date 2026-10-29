# Exercice 4 : Orthogonalisation de Gram-Schmidt (Polynômes)

## Énoncé

Dans $L^2([-1, 1])$, orthogonaliser la base $(1, t, t^2)$.

*Niveau de difficulté :* $\bigstar\bigstar\star\star\star$

## Correction

1. **Vecteur 1 :** $e_1(t) = 1$.
2. **Vecteur 2 :** On pose $v_2(t) = t - \frac{\langle t, 1 \rangle}{\|1\|^2} 1$. On sait que $\langle t, 1 \rangle = \int_{-1}^1 t dt = 0$. Donc $e_2(t) = t$.
3. **Vecteur 3 :** On pose $v_3(t) = t^2 - \frac{\langle t^2, 1 \rangle}{\|1\|^2} 1 - \frac{\langle t^2, t \rangle}{\|t\|^2} t$.
4. **Calculs :** $\langle t^2, 1 \rangle = \frac{2}{3}$. $\|1\|^2 = 2$. $\langle t^2, t \rangle = 0$.
5. **Résultat :** $e_3(t) = t^2 - \frac{2/3}{2} \cdot 1 = t^2 - \frac{1}{3}$.
6. **Conclusion :** La famille orthogonale est $(1, t, t^2 - 1/3)$. Ce sont les trois premiers polynômes de Legendre à un facteur multiplicatif près.
