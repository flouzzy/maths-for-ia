---
uuid: jalon-83-exo-07
title: "Exercice 07 - Dérivation des distributions"
---

# Exercice 07 $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
L'espace de Sobolev $H^1(]0, 1[)$ est l'ensemble des fonctions $u \in L^2(]0, 1[)$ dont la dérivée distributionnelle $u'$ appartient à $L^2(]0, 1[)$.
1. Soit $u(x) = x^{3/4}$. Démontrer que $u \in H^1(]0, 1[)$.
2. Soit $v(x) = x^{1/4}$. Démontrer que $v \notin H^1(]0, 1[)$, bien que $v \in L^2(]0, 1[)$.
3. Pourquoi la notion de "valeur au bord" (Trace) $u(0)$ est-elle bien définie pour les fonctions de $H^1$ (comme $u$) mais pas de manière évidente pour n'importe quelle fonction $L^2$ ? (Invoquez le théorème d'injection de Sobolev).

**Correction pas à pas :**
1. Vérifions d'abord que $u \in L^2$.
$$ \int_0^1 |x^{3/4}|^2 dx = \int_0^1 x^{3/2} dx = \left[ \frac{x^{5/2}}{5/2} \right]_0^1 = \frac{2}{5} < +\infty $$
Donc $u \in L^2(]0, 1[)$.
La dérivée distributionnelle de $u$ coïncide avec sa dérivée usuelle car $u$ est lisse sur $]0, 1[$ et localement intégrable, sans discontinuités à l'intérieur de l'ouvert. $u'(x) = \frac{3}{4} x^{-1/4}$.
Vérifions si $u' \in L^2$ :
$$ \int_0^1 |u'(x)|^2 dx = \int_0^1 \frac{9}{16} x^{-1/2} dx = \frac{9}{16} \left[ 2 x^{1/2} \right]_0^1 = \frac{18}{16} = \frac{9}{8} < +\infty $$
Donc $u' \in L^2$. En conclusion, $u \in H^1(]0, 1[)$.

2. Pour $v(x) = x^{1/4}$.
$$ \int_0^1 |x^{1/4}|^2 dx = \int_0^1 x^{1/2} dx = \frac{2}{3} < +\infty $$ donc $v \in L^2$.
Sa dérivée est $v'(x) = \frac{1}{4} x^{-3/4}$.
Regardons l'intégrale de son carré :
$$ \int_0^1 |v'(x)|^2 dx = \frac{1}{16} \int_0^1 x^{-3/2} dx $$
Cette intégrale est de la forme $\int_0^1 \frac{1}{x^\alpha} dx$ avec $\alpha = 3/2 > 1$. Elle est donc divergente en 0 (intégrale de Riemann). L'intégrale vaut $+\infty$.
Par conséquent, $v' \notin L^2(]0, 1[)$, donc $v \notin H^1(]0, 1[)$.

3. Dans $L^2$, une fonction n'est définie que "presque partout". Changer sa valeur en un seul point (comme $x=0$) ne change pas l'objet mathématique. L'expression $u(0)$ n'a donc rigoureusement aucun sens formel pour un élément pur de $L^2$.
Cependant, le théorème d'injection de Sobolev (en dimension 1) stipule que $H^1(]0, 1[) \hookrightarrow C^0([0, 1])$. C'est-à-dire que toute fonction de $H^1$ admet un unique représentant continu sur l'intervalle fermé. C'est la régularité imposée par l'intégrabilité de la dérivée qui empêche la fonction d'osciller sauvagement. Pour ce représentant continu, l'évaluation au bord $u(0)$ a un sens mathématique strict. C'est crucial pour imposer des conditions de Dirichlet en EDP (ex: bout d'une corde attachée, potentiel nul à la surface). $\blacksquare$
