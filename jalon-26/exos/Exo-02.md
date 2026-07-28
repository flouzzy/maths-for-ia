---
uuid: "jalon-26-exo-02"
title: "Produit scalaire sur l'espace des fonctions continues"
difficulty: 2
---

# Exercice 2 : Produit scalaire sur l'espace des fonctions continues (Difficulté ★★☆☆☆)

Soit $E = C([0, 1], \mathbb{R})$ l'espace vectoriel des fonctions continues de $[0, 1]$ dans $\mathbb{R}$. On munit $E$ de l'application $\langle f, g \rangle = \int_0^1 f(t)g(t)dt$.

1. Démontrer avec la plus stricte rigueur que cette application définit bien un produit scalaire sur $E$. Vous porterez une attention particulière à l'axiome de définition positive, en justifiant précisément pourquoi $\langle f, f \rangle = 0 \implies f = 0_E$.
2. En utilisant l'inégalité de Cauchy-Schwarz, démontrer que pour toute fonction $f \in E$ strictement positive, on a l'inégalité : $\left( \int_0^1 f(t) dt \right) \left( \int_0^1 \frac{1}{f(t)} dt \right) \ge 1$.
3. Caractériser l'ensemble des fonctions $f$ pour lesquelles cette inégalité est une égalité.

## Démonstration Rigoureuse à Blanc

1. Vérifions méthodiquement les axiomes définissant un produit scalaire. Soient $f, g, h \in E$ et $\lambda \in \mathbb{R}$.
   - **Symétrie :**
     $$ \langle f, g \rangle = \int_0^1 f(t)g(t) dt = \int_0^1 g(t)f(t) dt = \langle g, f \rangle $$
     La symétrie découle trivialement de la commutativité du produit dans $\mathbb{R}$.
   - **Bilinéarité :** Par symétrie, il suffit de vérifier la linéarité par rapport à la première variable.
     $$ \langle \lambda f + g, h \rangle = \int_0^1 (\lambda f(t) + g(t))h(t) dt = \int_0^1 (\lambda f(t)h(t) + g(t)h(t)) dt $$
     Par linéarité de l'intégrale de Riemann sur le segment $[0, 1]$ :
     $$ \langle \lambda f + g, h \rangle = \lambda \int_0^1 f(t)h(t) dt + \int_0^1 g(t)h(t) dt = \lambda \langle f, h \rangle + \langle g, h \rangle $$
     La forme est donc bien bilinéaire symétrique.
   - **Positivité :** Pour toute fonction $f \in E$, évaluons $\langle f, f \rangle$.
     $$ \langle f, f \rangle = \int_0^1 f(t)^2 dt $$
     Puisque la fonction $t \mapsto f(t)^2$ est positive ou nulle sur $[0, 1]$, et que les bornes d'intégration sont dans l'ordre croissant ($0 \le 1$), la positivité de l'intégrale garantit que $\langle f, f \rangle \ge 0$.
   - **Caractère défini :** Supposons que $\langle f, f \rangle = 0$, soit $\int_0^1 f(t)^2 dt = 0$.
     La fonction $h(t) = f(t)^2$ est continue sur le segment $[0, 1]$ et est partout positive ou nulle. Le théorème fondamental de l'intégration des fonctions continues de signe constant affirme que si l'intégrale d'une fonction continue et positive sur un segment d'intérieur non vide est nulle, alors cette fonction est identiquement nulle sur ce segment.
     Ainsi, pour tout $t \in [0, 1]$, $f(t)^2 = 0$, ce qui implique $f(t) = 0$. La fonction $f$ est donc bien la fonction nulle, $f = 0_E$.
   L'application est bilinéaire, symétrique et définie positive, c'est un produit scalaire sur $E$.

2. Soit $f \in E$ une fonction strictement positive sur $[0, 1]$. Définissons deux nouvelles fonctions $u, v \in E$ astucieusement choisies pour faire apparaître les termes de l'inégalité demandée via leurs carrés :
   $$ u(t) = \sqrt{f(t)} \quad \text{et} \quad v(t) = \frac{1}{\sqrt{f(t)}} $$
   Ces fonctions sont bien continues sur $[0, 1]$ car $f$ est continue et ne s'annule pas (elle est strictement positive).
   Calculons leur norme au carré :
   $$ \|u\|^2 = \int_0^1 u(t)^2 dt = \int_0^1 f(t) dt $$
   $$ \|v\|^2 = \int_0^1 v(t)^2 dt = \int_0^1 \frac{1}{f(t)} dt $$
   Évaluons maintenant leur produit scalaire :
   $$ \langle u, v \rangle = \int_0^1 u(t)v(t) dt = \int_0^1 \sqrt{f(t)} \frac{1}{\sqrt{f(t)}} dt = \int_0^1 1 dt = 1 $$
   Appliquons l'inégalité de Cauchy-Schwarz à ces deux fonctions :
   $$ \langle u, v \rangle^2 \le \|u\|^2 \|v\|^2 $$
   En substituant les expressions calculées, nous obtenons instantanément :
   $$ 1^2 \le \left( \int_0^1 f(t) dt \right) \left( \int_0^1 \frac{1}{f(t)} dt \right) $$
   L'inégalité est démontrée.

3. L'égalité dans Cauchy-Schwarz est vérifiée si et seulement si les fonctions $u$ et $v$ sont liées. Dans cet espace vectoriel fonctionnel, cela signifie qu'il existe un scalaire réel $\lambda$ tel que pour tout $t \in [0, 1]$, $u(t) = \lambda v(t)$.
   Exprimons cette condition en fonction de $f$ :
   $$ \sqrt{f(t)} = \lambda \frac{1}{\sqrt{f(t)}} $$
   Puisque $f(t) > 0$, on peut multiplier par $\sqrt{f(t)}$ :
   $$ f(t) = \lambda $$
   Ainsi, la fonction $f$ doit être constante sur l'intervalle $[0, 1]$. Réciproquement, si $f(t) = c > 0$, l'intégrale de $f$ vaut $c$, et l'intégrale de $1/f$ vaut $1/c$. Leur produit donne bien $c \cdot (1/c) = 1$, ce qui confirme la validité de notre caractérisation.
   $\blacksquare$
