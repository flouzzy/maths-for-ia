---
uuid: "jalon-8-exo-03"
title: "Exercice 3 : Analyse complète d'une application linéaire"
tags:
  - math/algebre-lineaire
  - exercice
---
# Exercice 3 : Analyse complète d'une application linéaire (Difficulté : ★★☆☆☆)

## Énoncé
Soit $f : \mathbb{R}^3 \to \mathbb{R}^3$ l'application définie pour tout $(x,y,z) \in \mathbb{R}^3$ par :
$$f(x,y,z) = (x-y, y-z, z-x)$$

1.  Démontrer que $f$ est une application linéaire.
2.  Déterminer le noyau $\ker f$ de $f$. En donner une base et sa dimension.
3.  L'application $f$ est-elle injective ? Justifier votre réponse.
4.  Déterminer l'image $\text{Im } f$ de $f$. En donner une base et sa dimension (le rang de $f$).
5.  L'application $f$ est-elle surjective ? Justifier votre réponse.
6.  Vérifier le théorème du rang pour cette application.

## Correction Détaillée

### 1. Démonstration que $f$ est une application linéaire

Pour montrer que $f$ est une application linéaire, nous devons vérifier deux propriétés : l'additivité et l'homogénéité.

**a) Additivité :**
Soient $u = (x_1, y_1, z_1) \in \mathbb{R}^3$ et $v = (x_2, y_2, z_2) \in \mathbb{R}^3$.
Alors $u+v = (x_1+x_2, y_1+y_2, z_1+z_2)$.

Calculons $f(u+v)$ :
$$f(u+v) = f(x_1+x_2, y_1+y_2, z_1+z_2)$$
$$f(u+v) = ((x_1+x_2)-(y_1+y_2), (y_1+y_2)-(z_1+z_2), (z_1+z_2)-(x_1+x_2))$$
$$f(u+v) = (x_1-y_1+x_2-y_2, y_1-z_1+y_2-z_2, z_1-x_1+z_2-x_2)$$

Calculons $f(u) + f(v)$ :
$$f(u) = (x_1-y_1, y_1-z_1, z_1-x_1)$$
$$f(v) = (x_2-y_2, y_2-z_2, z_2-x_2)$$
$$f(u) + f(v) = (x_1-y_1+x_2-y_2, y_1-z_1+y_2-z_2, z_1-x_1+z_2-x_2)$$

Nous constatons que $f(u+v) = f(u) + f(v)$. La propriété d'additivité est vérifiée.

**b) Homogénéité :**
Soit $\lambda \in \mathbb{R}$ et $u = (x,y,z) \in \mathbb{R}^3$.
Alors $\lambda u = (\lambda x, \lambda y, \lambda z)$.

Calculons $f(\lambda u)$ :
$$f(\lambda u) = f(\lambda x, \lambda y, \lambda z)$$
$$f(\lambda u) = (\lambda x - \lambda y, \lambda y - \lambda z, \lambda z - \lambda x)$$
$$f(\lambda u) = (\lambda(x-y), \lambda(y-z), \lambda(z-x))$$

Calculons $\lambda f(u)$ :
$$f(u) = (x-y, y-z, z-x)$$
$$\lambda f(u) = \lambda(x-y, y-z, z-x)$$
$$\lambda f(u) = (\lambda(x-y), \lambda(y-z), \lambda(z-x))$$

Nous constatons que $f(\lambda u) = \lambda f(u)$. La propriété d'homogénéité est vérifiée.

Puisque $f$ vérifie l'additivité et l'homogénéité, $f$ est bien une application linéaire.

### 2. Détermination du noyau $\ker f$

Par définition, $\ker f = \{ (x,y,z) \in \mathbb{R}^3 \mid f(x,y,z) = (0,0,0) \}$.
Nous devons résoudre le système d'équations linéaires suivant :
$$
\begin{cases}
x-y = 0 & (L_1) \\
y-z = 0 & (L_2) \\
z-x = 0 & (L_3)
\end{cases}
$$
De $(L_1)$, nous obtenons $x=y$.
De $(L_2)$, nous obtenons $y=z$.
En substituant $y$ par $x$ dans $y=z$, nous obtenons $x=z$.
Ainsi, $x=y=z$.
Vérifions avec $(L_3)$ : $z-x = x-x = 0$, ce qui est compatible.

Donc, les vecteurs du noyau sont de la forme $(x,x,x)$ pour tout $x \in \mathbb{R}$.
$$\ker f = \{ (x,x,x) \mid x \in \mathbb{R} \}$$
Nous pouvons écrire ces vecteurs comme $x \cdot (1,1,1)$.
$$\ker f = \text{Vect}((1,1,1))$$
Une base de $\ker f$ est donc la famille $((1,1,1))$.
La dimension de $\ker f$ est le nombre de vecteurs dans cette base, soit $1$.
$$\dim(\ker f) = 1$$

### 3. Injectivité de $f$

Une application linéaire $f$ est injective si et seulement si son noyau est réduit au vecteur nul, c'est-à-dire $\ker f = \{0_{\mathbb{R}^3}\}$.
Dans notre cas, $\ker f = \text{Vect}((1,1,1))$. Puisque $(1,1,1) \neq (0,0,0)$, le noyau n'est pas réduit au vecteur nul.
Par conséquent, $f$ n'est pas injective.

### 4. Détermination de l'image $\text{Im } f$

Par définition, $\text{Im } f = \{ f(x,y,z) \mid (x,y,z) \in \mathbb{R}^3 \}$.
L'image est engendrée par les images des vecteurs d'une base de l'espace de départ $\mathbb{R}^3$. Utilisons la base canonique $\mathcal{B}_c = (e_1, e_2, e_3)$ où $e_1=(1,0,0)$, $e_2=(0,1,0)$, $e_3=(0,0,1)$.

Calculons les images de ces vecteurs :
$f(e_1) = f(1,0,0) = (1-0, 0-0, 0-1) = (1,0,-1)$
$f(e_2) = f(0,1,0) = (0-1, 1-0, 0-0) = (-1,1,0)$
$f(e_3) = f(0,0,1) = (0-0, 0-1, 1-0) = (0,-1,1)$

Donc, $\text{Im } f = \text{Vect}((1,0,-1), (-1,1,0), (0,-1,1))$.
Pour trouver une base de $\text{Im } f$, nous devons extraire une famille libre de ces vecteurs.
Vérifions si ces vecteurs sont linéairement indépendants. Soient $\alpha, \beta, \gamma \in \mathbb{R}$ tels que :
$$\alpha(1,0,-1) + \beta(-1,1,0) + \gamma(0,-1,1) = (0,0,0)$$
Ceci conduit au système d'équations :
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
En substituant dans $(L'_3)$ : $-\alpha + \alpha = 0$, ce qui est toujours vrai.
Cela signifie que les vecteurs sont linéairement dépendants. Par exemple, si nous prenons $\alpha=1$, alors $\beta=1$ et $\gamma=1$.
$$1 \cdot (1,0,-1) + 1 \cdot (-1,1,0) + 1 \cdot (0,-1,1) = (1-1+0, 0+1-1, -1+0+1) = (0,0,0)$$
Puisque la somme des trois vecteurs est le vecteur nul, ils sont liés.
Nous pouvons exprimer un vecteur en fonction des autres, par exemple $f(e_3) = -f(e_1) - f(e_2)$.
Donc, $f(e_3)$ est redondant pour engendrer l'image.
Ainsi, $\text{Im } f = \text{Vect}((1,0,-1), (-1,1,0))$.
Vérifions si les deux vecteurs restants, $v_1=(1,0,-1)$ et $v_2=(-1,1,0)$, sont linéairement indépendants.
Soient $\alpha, \beta \in \mathbb{R}$ tels que $\alpha v_1 + \beta v_2 = (0,0,0)$.
$$\alpha(1,0,-1) + \beta(-1,1,0) = (0,0,0)$$
$$(\alpha-\beta, \beta, -\alpha) = (0,0,0)$$
Ceci conduit au système :
$$
\begin{cases}
\alpha - \beta = 0 \\
\beta = 0 \\
-\alpha = 0
\end{cases}
$$
De la deuxième équation, $\beta=0$. En substituant dans la première, $\alpha-0=0 \implies \alpha=0$. La troisième équation est alors $-\alpha=0 \implies 0=0$, ce qui est cohérent.
Donc, $\alpha=0$ et $\beta=0$. Les vecteurs $v_1$ et $v_2$ sont linéairement indépendants.
Une base de $\text{Im } f$ est donc la famille $((1,0,-1), (-1,1,0))$.
La dimension de $\text{Im } f$ est le nombre de vecteurs dans cette base, soit $2$.
Le rang de $f$ est $\text{rg } f = \dim(\text{Im } f) = 2$.

### 5. Surjectivité de $f$

Une application linéaire $f: E \to F$ est surjective si et seulement si son image est égale à l'espace d'arrivée $F$, c'est-à-dire $\text{Im } f = F$.
Dans notre cas, l'espace d'arrivée est $\mathbb{R}^3$, et $\dim(\mathbb{R}^3) = 3$.
Nous avons trouvé que $\dim(\text{Im } f) = 2$.
Puisque $\dim(\text{Im } f) \neq \dim(\mathbb{R}^3)$, l'image n'est pas l'espace d'arrivée tout entier.
Par conséquent, $f$ n'est pas surjective.

### 6. Vérification du théorème du rang

Le théorème du rang stipule que pour toute application linéaire $f: E \to F$ où $E$ est de dimension finie, on a :
$$\dim E = \dim(\ker f) + \text{rg}(f)$$
Dans notre cas, $E = \mathbb{R}^3$, donc $\dim E = 3$.
Nous avons calculé $\dim(\ker f) = 1$.
Nous avons calculé $\text{rg}(f) = \dim(\text{Im } f) = 2$.

Vérifions l'égalité :
$$3 = 1 + 2$$
$$3 = 3$$
Le théorème du rang est bien vérifié pour cette application linéaire.