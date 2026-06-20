# Exercice 4 : Noyau, Image et Théorème du Rang (Difficulté : **)

## Énoncé du problème

Soit $\mathbb{K}$ le corps des nombres réels, $\mathbb{K} = \mathbb{R}$.
On considère les $\mathbb{K}$-espaces vectoriels $E = \mathbb{R}^3$ et $F = \mathbb{R}^2$.
Soit $f$ l'application de $E$ vers $F$ définie pour tout $\mathbf{v} = (x,y,z) \in E$ par :
$$ f(x,y,z) = (x-y, y-z) $$
On admettra que $f$ est une application linéaire.

1.  Déterminer une base et la dimension du noyau de $f$, noté $\operatorname{Ker}(f)$.
2.  Déterminer une base et la dimension de l'image de $f$, notée $\operatorname{Im}(f)$.
3.  Vérifier le théorème du rang pour l'application linéaire $f$.

---

## Correction détaillée

### Question 1 : Détermination du noyau de $f$

Le noyau de $f$, $\operatorname{Ker}(f)$, est l'ensemble des vecteurs $\mathbf{v} \in E$ tels que $f(\mathbf{v}) = \mathbf{0}_F$, où $\mathbf{0}_F$ est le vecteur nul de $F$.
Soit $\mathbf{v} = (x,y,z) \in \mathbb{R}^3$.
L'équation $f(x,y,z) = (0,0)$ se traduit par le système d'équations linéaires suivant :
$$ \begin{cases} x - y = 0 \\ y - z = 0 \end{cases} $$
De la première équation, nous déduisons $x = y$.
De la seconde équation, nous déduisons $y = z$.
Par conséquent, tout vecteur $\mathbf{v}$ appartenant à $\operatorname{Ker}(f)$ doit satisfaire la condition $x = y = z$.
Les vecteurs du noyau sont donc de la forme $(x,x,x)$ pour tout $x \in \mathbb{R}$.
On peut écrire $(x,x,x) = x(1,1,1)$.
Le noyau est donc l'ensemble des multiples scalaires du vecteur $(1,1,1)$.
Ainsi, $\operatorname{Ker}(f) = \operatorname{Vect}((1,1,1))$.
Le vecteur $(1,1,1)$ est non nul et engendre $\operatorname{Ker}(f)$, il forme donc une base de $\operatorname{Ker}(f)$.
Une base pour $\operatorname{Ker}(f)$ est $B_{\operatorname{Ker}(f)} = \{ (1,1,1) \}$.
La dimension du noyau de $f$ est $\dim(\operatorname{Ker}(f)) = 1$.

### Question 2 : Détermination de l'image de $f$

L'image de $f$, $\operatorname{Im}(f)$, est l'ensemble des vecteurs $\mathbf{w} \in F$ pour lesquels il existe un vecteur $\mathbf{v} \in E$ tel que $f(\mathbf{v}) = \mathbf{w}$.
L'image d'une application linéaire est engendrée par les images des vecteurs d'une base de l'espace de départ $E$.
Considérons la base canonique de $E = \mathbb{R}^3$, notée $B_E = \{ \mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3 \}$, où $\mathbf{e}_1=(1,0,0)$, $\mathbf{e}_2=(0,1,0)$, $\mathbf{e}_3=(0,0,1)$.

Calculons les images de ces vecteurs :
*   $f(\mathbf{e}_1) = f(1,0,0) = (1-0, 0-0) = (1,0)$.
*   $f(\mathbf{e}_2) = f(0,1,0) = (0-1, 1-0) = (-1,1)$.
*   $f(\mathbf{e}_3) = f(0,0,1) = (0-0, 0-1) = (0,-1)$.

L'image de $f$ est donc l'espace vectoriel engendré par ces trois vecteurs :
$$ \operatorname{Im}(f) = \operatorname{Vect}((1,0), (-1,1), (0,-1)) $$
Ces vecteurs appartiennent à $F = \mathbb{R}^2$. L'espace $\mathbb{R}^2$ est de dimension 2, donc l'image de $f$ ne peut pas avoir une dimension supérieure à 2.
Nous devons extraire une base de l'ensemble de vecteurs $\{ (1,0), (-1,1), (0,-1) \}$.
Considérons les deux premiers vecteurs : $\mathbf{u}_1 = (1,0)$ et $\mathbf{u}_2 = (-1,1)$.
Vérifions s'ils sont linéairement indépendants. Soient $\alpha, \beta \in \mathbb{R}$ tels que $\alpha \mathbf{u}_1 + \beta \mathbf{u}_2 = \mathbf{0}_F$:
$$ \alpha(1,0) + \beta(-1,1) = (0,0) $$
$$ (\alpha - \beta, \beta) = (0,0) $$
Ce qui implique $\beta = 0$ et $\alpha - \beta = 0 \implies \alpha = 0$.
Les vecteurs $(1,0)$ et $(-1,1)$ sont donc linéairement indépendants.
Puisqu'ils sont deux vecteurs linéairement indépendants dans l'espace de dimension 2, $F = \mathbb{R}^2$, ils forment une base de $\mathbb{R}^2$.
Par conséquent, $\operatorname{Im}(f) = \mathbb{R}^2$.
Une base pour $\operatorname{Im}(f)$ est $B_{\operatorname{Im}(f)} = \{ (1,0), (-1,1) \}$.
La dimension de l'image de $f$ est $\dim(\operatorname{Im}(f)) = 2$.
Le rang de $f$ est $\operatorname{rg}(f) = \dim(\operatorname{Im}(f)) = 2$.

### Question 3 : Vérification du théorème du rang

Le théorème du rang stipule que pour toute application linéaire $f: E \to F$, la dimension de l'espace de départ $E$ est égale à la somme de la dimension de son noyau et de la dimension de son image :
$$ \dim(E) = \dim(\operatorname{Ker}(f)) + \dim(\operatorname{Im}(f)) $$
Dans notre cas :
*   La dimension de l'espace de départ $E = \mathbb{R}^3$ est $\dim(E) = 3$.
*   D'après la Question 1, la dimension du noyau est $\dim(\operatorname{Ker}(f)) = 1$.
*   D'après la Question 2, la dimension de l'image est $\dim(\operatorname{Im}(f)) = 2$.

Vérifions l'égalité :
$$ 3 = 1 + 2 $$
L'égalité est satisfaite. Le théorème du rang est vérifié pour l'application linéaire $f$.