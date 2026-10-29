# Exercice 3 : Théorème de Riesz et dérivation

## Énoncé

Soit $H_0^1([0, 1])$ l'espace de Sobolev des fonctions $f \in C^1$ avec $f(0)=f(1)=0$, muni du produit scalaire $\langle f, g \rangle = \int_0^1 f'(t) g'(t) dt$. Soit $L(f) = \int_0^1 f(t) dt$. Trouver $u \in H_0^1$ tel que $L(f) = \langle f, u \rangle$.

*Niveau de difficulté :* $\bigstar\bigstar\star\star\star$

## Correction

1. **Continuité de L :** Par l'inégalité de Poincaré, $\|f\|_{L^2} \le C \|f'\|_{L^2}$, donc $L$ est continue sur cet espace de Hilbert. Le théorème de Riesz s'applique.
2. **Équation de Riesz :** On cherche $u$ tel que $\int_0^1 f(t) dt = \int_0^1 f'(t) u'(t) dt$.
3. **Intégration par parties :** En intégrant par parties le second membre : $\int_0^1 f'(t) u'(t) dt = [f(t)u'(t)]_0^1 - \int_0^1 f(t) u''(t) dt$. Comme $f(0)=f(1)=0$, cela vaut $-\int_0^1 f(t) u''(t) dt$.
4. **Identification :** Pour que l'égalité soit vraie pour tout $f$, on doit avoir $-u''(t) = 1$ presque partout.
5. **Résolution de l'EDO :** $u'(t) = -t + A$, puis $u(t) = -t^2/2 + At + B$.
6. **Conditions aux limites :** $u \in H_0^1 \implies u(0)=u(1)=0$. $u(0)=0 \implies B=0$. $u(1) = -1/2 + A = 0 \implies A=1/2$.
7. **Conclusion :** Le représentant de Riesz est $u(t) = \frac{1}{2} t (1-t)$.
