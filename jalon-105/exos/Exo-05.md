# Exercice 5 : Opérateur de Volterra $\bigstar\bigstar\bigstar\star\star$
## Énoncé
Soit $H = L^2([0,1])$ muni de son produit scalaire usuel réel.
On définit l'opérateur de Volterra $V : H \to H$ par :
$$ (Vf)(x) = \int_0^x f(y) dy $$
1. Déterminer l'adjoint $V^*$ de l'opérateur de Volterra.
2. Démontrer que $V + V^*$ est un opérateur de rang 1. Préciser cet opérateur.

## Correction
1. Soient $f, g \in L^2([0,1])$. Calculons le produit scalaire $\langle Vf, g \rangle$ :
$$ \langle Vf, g \rangle = \int_0^1 (Vf)(x) g(x) dx = \int_0^1 \left( \int_0^x f(y) dy \right) g(x) dx $$
Cette expression est une intégrale double sur le domaine $D = \{ (x,y) \in [0,1]^2 \mid 0 \le y \le x \le 1 \}$.
D'après le théorème de Fubini, on peut intervertir l'ordre d'intégration. En intégrant d'abord par rapport à $x$, l'intervalle pour $x$ devient $[y, 1]$, tandis que $y$ varie de $0$ à $1$ :
$$ \langle Vf, g \rangle = \int_0^1 \left( \int_y^1 g(x) dx \right) f(y) dy $$
$$ = \int_0^1 f(y) \left( \int_y^1 g(x) dx \right) dy $$
Pour identifier cela avec $\langle f, V^*g \rangle = \int_0^1 f(y) (V^*g)(y) dy$, on déduit que :
$$ (V^*g)(y) = \int_y^1 g(x) dx $$
En renommant la variable libre par $x$ et la variable muette d'intégration par $y$ pour la présentation standard, on a :
$$ (V^*g)(x) = \int_x^1 g(y) dy $$

2. Calculons la somme $(V + V^*)f$ pour toute fonction $f \in H$ :
$$ ((V + V^*)f)(x) = (Vf)(x) + (V^*f)(x) = \int_0^x f(y) dy + \int_x^1 f(y) dy $$
D'après la relation de Chasles pour l'intégrale :
$$ = \int_0^1 f(y) dy $$
Cette valeur est une constante par rapport à la variable $x$. On peut l'écrire comme :
$$ ((V + V^*)f)(x) = \langle f, \mathbf{1} \rangle \cdot \mathbf{1}(x) $$
où $\mathbf{1}$ est la fonction constante égale à 1 sur $[0,1]$.
L'image de l'opérateur $V + V^*$ est donc générée par le seul vecteur (la fonction) $\mathbf{1}$.
L'opérateur $V + V^*$ est bien un opérateur de projection unidimensionnel non normalisé, donc il est de rang 1.
