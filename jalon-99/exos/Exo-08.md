# Exercice 8 : $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit $E = L^1([0,1])$. Considérons le sous-espace $F = \{ f \in E \mid \int_0^1 f(t) dt = 0 \}$. Montrer que $F$ est fermé. Si $g \in E \setminus F$, construire un hyperplan séparant $g$ de $F$.

## Correction

**Étape 1 : Fermeture de F**
La forme linéaire $\varphi(f) = \int_0^1 f(t) dt$ est continue sur $L^1$, car $|\varphi(f)| \le \int_0^1 |f(t)| dt = ||f||_1$.
Ainsi, $\varphi \in (L^1)' = L^\infty$.
$F$ est le noyau $\ker(\varphi)$. C'est donc un hyperplan fermé (et un sous-espace vectoriel).

**Étape 2 : Séparation**
Soit $g \notin F$, ce qui signifie $\alpha = \int_0^1 g(t) dt \neq 0$.
Puisque $F$ est un sous-espace, pour séparer $g$ de $F$, on utilise la forme linéaire $\varphi$ elle-même.
Sur $F$, on a $\varphi(f) = 0$.
Pour $g$, on a $\varphi(g) = \alpha$.
Supposons $\alpha > 0$ (quitte à considérer $-\varphi$).
Alors $\varphi(f) = 0 < \alpha/2 < \alpha = \varphi(g)$.
L'hyperplan affine d'équation $\int_0^1 h(t) dt = \alpha/2$ sépare strictement $F$ et le point $g$. $\blacksquare$
