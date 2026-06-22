---
uuid: "jalon-8-exo-04"
title: "Exercice 4 : Noyau, Image et Rang d'un Endomorphisme"
tags:
  - math/algebre-lineaire
  - exercice
---
# Exercice 4 : Noyau, Image et Rang d'un Endomorphisme (Difficulté : ★★☆☆☆)

## Énoncé
Soit $f : \mathbb{R}^3 \to \mathbb{R}^3$ l'application définie pour tout $(x,y,z) \in \mathbb{R}^3$ par :
$$f(x,y,z) = (x-y, y-z, z-x)$$

1.  Déterminer le noyau de $f$, $\ker f$, et en donner une base.
2.  Déterminer l'image de $f$, $\text{Im } f$, et en donner une base.
3.  Vérifier le théorème du rang pour l'application $f$.

## Correction Détaillée

### 1. Détermination du noyau de $f$ et d'une base de $\ker f$

Par définition, le noyau de $f$ est l'ensemble des vecteurs $v = (x,y,z) \in \mathbb{R}^3$ tels que $f(v) = 0_{\mathbb{R}^3}$.
Nous devons résoudre le système d'équations linéaires suivant :
$$f(x,y,z) = (0,0,0)$$
Ce qui se traduit par :
$$
\begin{cases}
x - y = 0 & (L_1) \\
y - z = 0 & (L_2) \\
z - x = 0 & (L_3)
\end{cases}
$$

De l'équation $(L_1)$, nous obtenons $x = y$.
De l'équation $(L_2)$, nous obtenons $y = z$.
En substituant $y$ par $x$ dans la deuxième équation, nous avons $x = z$.
Ainsi, les trois équations impliquent $x = y = z$.

Vérifions avec la troisième équation $(L_3)$: $z - x = 0$. Si $x=z$, alors $z-x=0$ est bien vérifiée.
Donc, un vecteur $(x,y,z)$ appartient à $\ker f$ si et seulement si $x=y=z$.

Nous pouvons écrire les vecteurs du noyau sous la forme :
$$(x,y,z) = (x,x,x) = x(1,1,1)$$
où $x$ est un scalaire réel quelconque.

Le noyau de $f$ est donc l'ensemble des multiples du vecteur $(1,1,1)$.
$$\ker f = \{ x(1,1,1) \mid x \in \mathbb{R} \} = \text{Vect}((1,1,1))$$

Une base de $\ker f$ est la famille constituée du seul vecteur non nul $(1,1,1)$.
$$\mathcal{B}_{\ker f} = ((1,1,1))$$
La dimension du noyau de $f$ est donc $\dim(\ker f) = 1$.

### 2. Détermination de l'image de $f$ et d'une base de $\text{Im } f$

Par définition, l'image de $f$ est l'ensemble des vecteurs $w \in \mathbb{R}^3$ tels qu'il existe un vecteur $v=(x,y,z) \in \mathbb{R}^3$ pour lequel $w = f(v)$.
Nous pouvons écrire $f(x,y,z)$ comme une combinaison linéaire des vecteurs de la base canonique de $\mathbb{R}^3$ :
$$f(x,y,z) = (x-y, y-z, z-x)$$
$$f(x,y,z) = x(1,0,-1) + y(-1,1,0) + z(0,-1,1)$$

L'image de $f$ est donc l'espace vectoriel engendré par les vecteurs $v_1 = (1,0,-1)$, $v_2 = (-1,1,0)$ et $v_3 = (0,-1,1)$.
$$\text{Im } f = \text{Vect}(v_1, v_2, v_3) = \text{Vect}((1,0,-1), (-1,1,0), (0,-1,1))$$

Pour trouver une base de $\text{Im } f$, nous devons extraire une famille libre et génératrice de ces vecteurs.
Vérifions si ces vecteurs sont linéairement indépendants. Nous cherchons des scalaires $\alpha, \beta, \gamma \in \mathbb{R}$ tels que :
$$\alpha v_1 + \beta v_2 + \gamma v_3 = (0,0,0)$$
$$\alpha(1,0,-1) + \beta(-1,1,0) + \gamma(0,-1,1) = (0,0,0)$$
Ce qui donne le système :
$$
\begin{cases}
\alpha - \beta = 0 & (L'_1) \\
\beta - \gamma = 0 & (L'_2) \\
-\alpha + \gamma = 0 & (L'_3)
\end{cases}
$$
De $(L'_1)$, nous avons $\alpha = \beta$.
De $(L'_2)$, nous avons $\beta = \gamma$.
Donc $\alpha = \beta = \gamma$.
En substituant dans $(L'_3)$, nous obtenons $-\alpha + \alpha = 0$, ce qui est toujours vrai.
Cela signifie que les vecteurs $v_1, v_2, v_3$ sont linéairement dépendants. Par exemple, si nous prenons $\alpha=1$, alors $\beta=1$ et $\gamma=1$, ce qui donne $v_1 + v_2 + v_3 = (0,0,0)$.

Puisque la famille $(v_1, v_2, v_3)$ est liée, elle n'est pas une base. Nous devons en extraire une sous-famille libre qui engendre toujours $\text{Im } f$.
Les vecteurs $v_1 = (1,0,-1)$ et $v_2 = (-1,1,0)$ sont clairement linéairement indépendants, car l'un n'est pas un multiple de l'autre.
Nous savons que $v_3 = -v_1 - v_2$. Donc $v_3$ est une combinaison linéaire de $v_1$ et $v_2$.
Par conséquent, $\text{Vect}(v_1, v_2, v_3) = \text{Vect}(v_1, v_2)$.

Ainsi, une base de $\text{Im } f$ est la famille $\mathcal{B}_{\text{Im } f} = ((1,0,-1), (-1,1,0))$.
La dimension de l'image de $f$ est donc $\dim(\text{Im } f) = 2$.

### 3. Vérification du théorème du rang

Le théorème du rang stipule que pour toute application linéaire $f : E \to F$ où $E$ est un espace vectoriel de dimension finie, on a :
$$\dim E = \dim(\ker f) + \text{rg}(f)$$
où $\text{rg}(f) = \dim(\text{Im } f)$.

Dans notre cas :
- L'espace de départ est $E = \mathbb{R}^3$, donc $\dim E = 3$.
- Nous avons trouvé $\dim(\ker f) = 1$.
- Nous avons trouvé $\text{rg}(f) = \dim(\text{Im } f) = 2$.

Vérifions l'égalité :
$$3 = 1 + 2$$
$$3 = 3$$
L'égalité est vérifiée. Le théorème du rang est bien confirmé pour cette application linéaire.