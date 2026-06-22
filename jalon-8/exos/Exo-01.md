---
uuid: "jalon-8-exo-01"
title: "Exercice 1 : Noyau, Image et Rang d'une application linéaire simple"
tags:
  - math/algebre-lineaire
  - exercice
---
# Exercice 1 : Noyau, Image et Rang d'une application linéaire simple (Difficulté : ★☆☆☆☆)

## Énoncé
Soit $f : \mathbb{R}^2 \to \mathbb{R}^3$ l'application définie pour tout $(x,y) \in \mathbb{R}^2$ par $f(x,y) = (x, y, x+y)$.

1. Montrer que $f$ est une application linéaire.
2. Déterminer le noyau $\ker f$ de $f$ et sa dimension.
3. Déterminer l'image $\text{Im } f$ de $f$ et sa dimension.
4. Vérifier le théorème du rang pour cette application.

## Correction Détaillée

1. **Montrer que $f$ est une application linéaire.**
   Pour montrer que $f$ est une application linéaire, nous devons vérifier deux propriétés : l'additivité et l'homogénéité.

   *Additivité :* Soient $u = (x_1, y_1) \in \mathbb{R}^2$ et $v = (x_2, y_2) \in \mathbb{R}^2$.
   Leur somme est $u+v = (x_1+x_2, y_1+y_2)$.
   Calculons $f(u+v)$ :
   $$f(u+v) = f(x_1+x_2, y_1+y_2) = (x_1+x_2, y_1+y_2, (x_1+x_2)+(y_1+y_2))$$
   Calculons $f(u)+f(v)$ :
   $$f(u) = (x_1, y_1, x_1+y_1)$$
   $$f(v) = (x_2, y_2, x_2+y_2)$$
   $$f(u)+f(v) = (x_1+x_2, y_1+y_2, (x_1+y_1)+(x_2+y_2))$$
   Puisque l'addition dans $\mathbb{R}$ est commutative et associative, nous avons $(x_1+y_1)+(x_2+y_2) = x_1+x_2+y_1+y_2 = (x_1+x_2)+(y_1+y_2)$.
   Par conséquent, $f(u+v) = f(u)+f(v)$. L'additivité est vérifiée.

   *Homogénéité :* Soit $\lambda \in \mathbb{R}$ et $u = (x,y) \in \mathbb{R}^2$.
   Le produit scalaire est $\lambda u = (\lambda x, \lambda y)$.
   Calculons $f(\lambda u)$ :
   $$f(\lambda u) = f(\lambda x, \lambda y) = (\lambda x, \lambda y, \lambda x + \lambda y)$$
   Calculons $\lambda f(u)$ :
   $$\lambda f(u) = \lambda (x, y, x+y) = (\lambda x, \lambda y, \lambda(x+y))$$
   Puisque la multiplication dans $\mathbb{R}$ est distributive sur l'addition, nous avons $\lambda(x+y) = \lambda x + \lambda y$.
   Par conséquent, $f(\lambda u) = \lambda f(u)$. L'homogénéité est vérifiée.

   Puisque $f$ satisfait les propriétés d'additivité et d'homogénéité, $f$ est une application linéaire.

2. **Déterminer le noyau $\ker f$ de $f$ et sa dimension.**
   Par définition, le noyau de $f$ est l'ensemble des vecteurs de l'espace de départ $\mathbb{R}^2$ qui sont envoyés sur le vecteur nul de l'espace d'arrivée $\mathbb{R}^3$.
   $$\ker f = \{ (x,y) \in \mathbb{R}^2 \mid f(x,y) = (0,0,0) \}$$
   Nous devons résoudre le système d'équations $f(x,y) = (0,0,0)$ :
   $$
   \begin{cases}
   x = 0 & (L_1) \\
   y = 0 & (L_2) \\
   x+y = 0 & (L_3)
   \end{cases}
   $$
   D'après l'équation $(L_1)$, nous avons $x=0$.
   D'après l'équation $(L_2)$, nous avons $y=0$.
   Substituons ces valeurs dans l'équation $(L_3)$ : $0+0=0$, ce qui est une égalité vraie.
   Ainsi, les seules valeurs de $x$ et $y$ qui satisfont le système sont $x=0$ et $y=0$.
   Le noyau de $f$ est donc $\ker f = \{ (0,0) \}$.
   Le noyau est réduit au seul vecteur nul de $\mathbb{R}^2$.
   La dimension du noyau est $\dim(\ker f) = 0$.

3. **Déterminer l'image $\text{Im } f$ de $f$ et sa dimension.**
   Par définition, l'image de $f$ est l'ensemble des vecteurs de l'espace d'arrivée $\mathbb{R}^3$ qui sont atteints par $f$.
   $$\text{Im } f = \{ f(x,y) \mid (x,y) \in \mathbb{R}^2 \}$$
   Tout vecteur de l'image est de la forme $(x, y, x+y)$ pour certains scalaires $x,y \in \mathbb{R}$.
   Nous pouvons décomposer un tel vecteur comme une somme de vecteurs :
   $$(x, y, x+y) = (x, 0, x) + (0, y, y)$$
   Nous pouvons ensuite factoriser les scalaires $x$ et $y$ :
   $$(x, y, x+y) = x(1,0,1) + y(0,1,1)$$
   Cela signifie que tout vecteur de l'image est une combinaison linéaire des vecteurs $v_1 = (1,0,1)$ et $v_2 = (0,1,1)$.
   Donc, $\text{Im } f = \text{Vect}((1,0,1), (0,1,1))$.
   Pour trouver la dimension de $\text{Im } f$, nous devons déterminer si la famille de vecteurs $(v_1, v_2)$ est libre.
   Supposons qu'il existe des scalaires $\alpha, \beta \in \mathbb{R}$ tels que $\alpha v_1 + \beta v_2 = (0,0,0)$.
   $$\alpha(1,0,1) + \beta(0,1,1) = (0,0,0)$$
   $$(\alpha \cdot 1 + \beta \cdot 0, \alpha \cdot 0 + \beta \cdot 1, \alpha \cdot 1 + \beta \cdot 1) = (0,0,0)$$
   $$(\alpha, \beta, \alpha+\beta) = (0,0,0)$$
   Ceci conduit au système d'équations :
   $$
   \begin{cases}
   \alpha = 0 \\
   \beta = 0 \\
   \alpha+\beta = 0
   \end{cases}
   $$
   Les deux premières équations nous donnent directement $\alpha=0$ et $\beta=0$.
   La troisième équation $0+0=0$ est satisfaite.
   Puisque les seuls scalaires $\alpha$ et $\beta$ qui satisfont l'équation sont $\alpha=0$ et $\beta=0$, les vecteurs $v_1$ et $v_2$ sont linéairement indépendants.
   La famille $(v_1, v_2)$ est une famille génératrice et libre de $\text{Im } f$, c'est donc une base de $\text{Im } f$.
   La dimension de l'image est le nombre de vecteurs dans cette base, soit $\dim(\text{Im } f) = 2$.
   Par définition, le rang de $f$ est $\text{rg}(f) = \dim(\text{Im } f) = 2$.

4. **Vérifier le théorème du rang pour cette application.**
   Le théorème du rang stipule que pour toute application linéaire $f : E \to F$ où $E$ est un espace vectoriel de dimension finie, on a la relation :
   $$\dim E = \dim(\ker f) + \text{rg}(f)$$
   Dans notre cas, l'espace de départ est $E = \mathbb{R}^2$, donc sa dimension est $\dim E = 2$.
   D'après la question 2, nous avons trouvé $\dim(\ker f) = 0$.
   D'après la question 3, nous avons trouvé $\text{rg}(f) = 2$.
   Substituons ces valeurs dans la formule du théorème du rang :
   $$2 = 0 + 2$$
   $$2 = 2$$
   L'égalité est vérifiée. Le théorème du rang est bien confirmé pour cette application linéaire.