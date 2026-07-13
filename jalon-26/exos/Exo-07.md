---
uuid: "jalon-26-exo-07"
title: "Endomorphismes antisymétriques"
difficulty: 4
---

# Exercice 7 : Endomorphismes antisymétriques (Difficulté ★★★★☆)

Soit $E$ un espace euclidien. Un endomorphisme $u \in \mathcal{L}(E)$ est dit antisymétrique si pour tous $x, y \in E$, $\langle u(x), y \rangle = - \langle x, u(y) \rangle$.
1. Montrer que $u$ est antisymétrique si et seulement si pour tout $x \in E$, $\langle u(x), x \rangle = 0$.
2. Montrer que si $u$ est antisymétrique, $\ker(u)$ et $\text{Im}(u)$ sont supplémentaires orthogonaux dans $E$.
3. Que dire des valeurs propres réelles de $u$ ?

## Démonstration Rigoureuse à Blanc

1. $\Rightarrow$ : Supposons $u$ antisymétrique. Pour tout $x \in E$, $\langle u(x), x \rangle = - \langle x, u(x) \rangle$.
   - Par symétrie du produit scalaire, $\langle u(x), x \rangle = \langle x, u(x) \rangle$.
   - Donc $2 \langle u(x), x \rangle = 0 \implies \langle u(x), x \rangle = 0$.
   - $\Leftarrow$ : Supposons que pour tout $x$, $\langle u(x), x \rangle = 0$. Soient $x, y \in E$.
   - Évaluons la forme sur $x+y$ : $\langle u(x+y), x+y \rangle = 0$.
   - Par linéarité et bilinéarité : $\langle u(x) + u(y), x + y \rangle = \langle u(x), x \rangle + \langle u(x), y \rangle + \langle u(y), x \rangle + \langle u(y), y \rangle = 0$.
   - Or $\langle u(x), x \rangle = 0$ et $\langle u(y), y \rangle = 0$. Il reste $\langle u(x), y \rangle + \langle u(y), x \rangle = 0$.
   - Donc $\langle u(x), y \rangle = - \langle x, u(y) \rangle$ (par symétrie). $u$ est antisymétrique.

2. On doit d'abord prouver que $\ker(u) \perp \text{Im}(u)$.
   - Soit $x \in \ker(u)$ et $y \in \text{Im}(u)$. Alors $u(x) = 0$ et il existe $z \in E$ tel que $y = u(z)$.
   - Calculons leur produit scalaire : $\langle x, y \rangle = \langle x, u(z) \rangle$.
   - Puisque $u$ est antisymétrique, $\langle x, u(z) \rangle = -\langle u(x), z \rangle$.
   - Or $x \in \ker(u)$, donc $u(x) = 0$. Ainsi $-\langle 0, z \rangle = 0$.
   - Donc $\langle x, y \rangle = 0$, d'où $\ker(u) \subset (\text{Im}(u))^\perp$.
   - Par le théorème du rang, $\dim(E) = \dim(\ker(u)) + \dim(\text{Im}(u))$.
   - Dans un espace euclidien de dimension finie, $\dim((\text{Im}(u))^\perp) = \dim(E) - \dim(\text{Im}(u)) = \dim(\ker(u))$.
   - Les deux espaces ont la même dimension et l'un est inclus dans l'autre, donc $\ker(u) = (\text{Im}(u))^\perp$. Ils sont supplémentaires orthogonaux.

3. Soit $\lambda \in \mathbb{R}$ une valeur propre réelle de $u$, et $x \neq 0_E$ un vecteur propre associé.
   - Par définition, $u(x) = \lambda x$.
   - Calculons $\langle u(x), x \rangle$. D'après la question 1, puisque $u$ est antisymétrique, $\langle u(x), x \rangle = 0$.
   - Mais on a aussi $\langle u(x), x \rangle = \langle \lambda x, x \rangle = \lambda \langle x, x \rangle = \lambda \|x\|^2$.
   - Donc $\lambda \|x\|^2 = 0$.
   - Comme $x$ est un vecteur propre, $x \neq 0_E$, donc $\|x\|^2 > 0$.
   - Il s'ensuit que nécessairement $\lambda = 0$.
   - Les seules valeurs propres réelles possibles d'un endomorphisme antisymétrique sont $0$.
   $\blacksquare$
