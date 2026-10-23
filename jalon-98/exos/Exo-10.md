# Exercice 10 : Optimisation d'un problème mal posé
$\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Soit $E = L^2([0,1])$. On cherche $u \in E$ minimisant $\int_0^1 (u(t) - t)^2 dt$ sous la contrainte $\int_0^1 u(t)dt = 1$.
Démontrer par la dualité (Hahn-Banach géométrique) que ce problème admet une unique solution et la calculer analytiquement.

## Correction Détaillée
1. On cherche la projection orthogonale de $f(t)=t$ sur le sous-espace affine $V = \{ u \mid \langle u, 1 \rangle = 1 \}$.
2. Soit $H = \{ u \mid \langle u, 1 \rangle = 0 \}$ l'hyperplan vectoriel directeur. $V = u_0 + H$ avec $u_0 = 1$.
3. D'après le théorème de projection, le minimum est atteint pour l'unique $u \in V$ tel que $u - f \in H^\perp$.
4. $H^\perp = \text{Vect}(1)$, donc il existe une constante $C$ telle que $u(t) - t = C$.
5. Soit $u(t) = t + C$.
6. On injecte dans la contrainte : $\int_0^1 (t+C) dt = 1 \implies \frac{1}{2} + C = 1 \implies C = \frac{1}{2}$.
7. L'unique solution est $u(t) = t + 0.5$.
8. Vérification de la dualité : la valeur de la forme linéaire $\langle \cdot, 1 \rangle$ sature sur la direction orthogonale au sous-espace, illustrant la séparation par Hahn-Banach de la boule de rayon minimal et de l'hyperplan affine. $\blacksquare$
