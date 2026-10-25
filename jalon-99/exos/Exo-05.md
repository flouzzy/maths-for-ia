# Exercice 5 : Jauge de Minkowski $\bigstar\bigstar\bigstar\star\star$

## Énoncé
Soit $E = C([-1, 1], \mathbb{R})$. Soit $U = \{f \in E \mid \int_{-1}^1 f(t) dt < 1, f(0) > -1 \}$.
La jauge de $U$ est-elle une norme ?

## Correction Complète
L'ensemble $U$ est convexe.
Vérifions d'abord s'il est absorbant. Soit $f \in E$.
Pour un petit $\lambda > 0$, l'intégrale $\int \lambda f$ peut être rendue arbitrairement petite.
Mais la condition $\lambda f(0) > -1$ nécessite que $f(0)$ ne soit pas trop négatif.
Si $f(0) \leq 0$, il existe toujours $\lambda > 0$ tel que $\lambda f(0) > -1$.
Donc $U$ est absorbant.
On définit la jauge de Minkowski $p_U(f) = \inf\{\lambda > 0 \mid f \in \lambda U\}$.
Pour que $p_U$ soit une norme, il faut que $p_U$ soit finie, sous-additive, positivement homogène, symétrique et séparatrice.
Or, $U$ n'est pas symétrique (c'est-à-dire que $f \in U \nRightarrow -f \in U$).
Par exemple, pour $f(t) = -2$. $f(0) = -2 \ngtr -1$, donc $f \notin U$.
Mais pour $g(t) = 2$, l'intégrale vaut $4$, qui n'est pas $<1$.
Donc l'ensemble n'est pas symétrique.
De ce fait, $p_U(-f) \neq p_U(f)$ en général.
La jauge de Minkowski ne définit donc pas une norme (qui requiert $p(-f) = p(f)$), mais seulement une fonctionnelle sous-linéaire, ce qui suffit néanmoins pour appliquer la forme analytique du théorème de Hahn-Banach. $\blacksquare$
