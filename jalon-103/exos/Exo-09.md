# Exercice 9 : Bases de Haar

## Énoncé

Montrer que les fonctions de Haar forment un système orthogonal dans $L^2([0, 1])$.

*Niveau de difficulté :* $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Correction

1. **Définition :** La fonction de Haar mère est $\psi(t) = 1$ sur $[0, 1/2[$, $-1$ sur $[1/2, 1[$ et 0 ailleurs. On considère $\phi(t) = 1$.
2. **Orthogonalité 1 :** $\langle \psi, \phi \rangle = \int_0^1 \psi(t) \cdot 1 dt = \int_0^{1/2} 1 dt - \int_{1/2}^1 1 dt = \frac{1}{2} - \frac{1}{2} = 0$.
3. **Translations et dilatations :** Soit $\psi_{j,k}(t) = 2^{j/2} \psi(2^j t - k)$. Si on prend deux fonctions avec des supports disjoints, leur produit scalaire est nul car l'intégrale du produit l'est.
4. **Même support :** Si l'une est contenue dans le support de l'autre (niveaux d'échelle différents), disons $\psi_{j,k}$ sur un demi-intervalle de $\psi_{J,K}$ avec $j > J$. La fonction $\psi_{J,K}$ est constante sur le support de $\psi_{j,k}$. Donc le produit scalaire est proportionnel à l'intégrale de $\psi_{j,k}$ qui est nulle.
5. **Conclusion :** Le système de Haar est un système orthogonal de l'espace de Hilbert $L^2([0, 1])$. Il est d'ailleurs complet (base hilbertienne).
