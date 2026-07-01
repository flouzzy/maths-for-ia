---
---
# Exercice 4 : Noyau, Image et Théorème du Rang (Difficulté : **)

## Énoncé du problème

Soit $\mathbb{K}$ le corps des nombres réels, noté $\mathbb{K} = \mathbb{R}$.
On considère les $\mathbb{K}$-espaces vectoriels $E = \mathbb{R}^3$ et $F = \mathbb{R}^2$.
Soit $f$ l'application de $E$ vers $F$ définie pour tout vecteur $\mathbf{v} = (x,y,z) \in E$ par :
$$ f(x,y,z) = (x-y, y-z) $$
On admettra que $f$ est une application linéaire de $E$ dans $F$.

1.  Déterminer une base et la dimension du noyau de $f$, noté $\operatorname{Ker}(f)$.
2.  Déterminer une base et la dimension de l'image de $f$, notée $\operatorname{Im}(f)$.
3.  Vérifier le théorème du rang pour l'application linéaire $f$.

---

## Correction détaillée

### Question 1 : Détermination du noyau de $f$

Le noyau de l'application linéaire $f$, noté $\operatorname{Ker}(f)$, est défini comme l'ensemble des vecteurs $\mathbf{v} \in E$ tels que $f(\mathbf{v}) = \mathbf{0}_F$, où $\mathbf{0}_F$ représente le vecteur nul de l'espace vectoriel $F$.
Dans notre cas, l'espace de départ est $E = \mathbb{R}^3$ et l'espace d'arrivée est $F = \mathbb{R}^2$. Le vecteur nul de $F$ est $\mathbf{0}_F = (0,0)$.

Soit un vecteur $\mathbf{v} = (x,y,z) \in \mathbb{R}^3$.
L'appartenance de $\mathbf{v}$ au noyau $\operatorname{Ker}(f)$ est caractérisée par l'équation vectorielle $f(x,y,z) = (0,0)$.
En substituant la définition de l'application $f$, nous obtenons :
$$ (x-y, y-z) = (0,0) $$
Cette égalité de vecteurs dans $\mathbb{R}^2$ est équivalente au système d'équations linéaires suivant, en égalant les composantes correspondantes :
$$ \begin{cases} x - y = 0 & \quad (L_1) \\ y - z = 0 & \quad (L_2) \end{cases} $$

Résolvons ce système d'équations pour exprimer $x, y, z$ en fonction d'un paramètre.
À partir de l'équation $(L_1)$, $x - y = 0$:
En ajoutant le terme $y$ aux deux membres de l'équation, nous obtenons :
$$ x - y + y = 0 + y $$
$$ x = y \quad (L_3) $$

À partir de l'équation $(L_2)$, $y - z = 0$:
En ajoutant le terme $z$ aux deux membres de l'équation, nous obtenons :
$$ y - z + z = 0 + z $$
$$ y = z \quad (L_4) $$

En combinant les résultats des équations $(L_3)$ et $(L_4)$, nous déduisons que $x=y$ et $y=z$. Par la propriété de transitivité de l'égalité, cela implique que $x=y=z$.
Ainsi, tout vecteur $\mathbf{v} = (x,y,z)$ appartenant à $\operatorname{Ker}(f)$ doit satisfaire la condition $x = y = z$.
Les vecteurs du noyau sont donc de la forme $(x,x,x)$ pour tout scalaire $x \in \mathbb{R}$.

Nous pouvons factoriser le scalaire $x$ de ce vecteur pour exprimer sa structure :
$$ (x,x,x) = x \cdot (1,1,1) $$
Le noyau $\operatorname{Ker}(f)$ est donc l'ensemble de tous les multiples scalaires du vecteur $(1,1,1)$.
Par définition, cela signifie que $\operatorname{Ker}(f)$ est l'espace vectoriel engendré par le vecteur $(1,1,1)$.
$$ \operatorname{Ker}(f) = \operatorname{Vect}((1,1,1)) $$

Pour déterminer une base de $\operatorname{Ker}(f)$, nous devons trouver un ensemble de vecteurs qui est à la fois générateur de $\operatorname{Ker}(f)$ et linéairement indépendant.
L'ensemble $B_{\operatorname{Ker}(f)} = \{ (1,1,1) \}$ est un ensemble générateur de $\operatorname{Ker}(f)$ par construction.
Vérifions la liberté linéaire de cet ensemble. Soit $\alpha \in \mathbb{R}$ un scalaire tel que $\alpha \cdot (1,1,1) = \mathbf{0}_E$.
$$ (\alpha \cdot 1, \alpha \cdot 1, \alpha \cdot 1) = (0,0,0) $$
$$ (\alpha, \alpha, \alpha) = (0,0,0) $$
En égalant les composantes de ces vecteurs, nous obtenons $\alpha = 0$.
Puisque le seul scalaire $\alpha$ qui satisfait cette condition est $\alpha = 0$, le vecteur $(1,1,1)$ est linéairement indépendant.
De plus, le vecteur $(1,1,1)$ est non nul.
Par conséquent, l'ensemble $B_{\operatorname{Ker}(f)} = \{ (1,1,1) \}$ est une base de $\operatorname{Ker}(f)$.

La dimension du noyau de $f$, qui est le nombre de vecteurs dans une base de $\operatorname{Ker}(f)$, est $\dim(\operatorname{Ker}(f)) = 1$.

### Question 2 : Détermination de l'image de $f$

L'image de l'application linéaire $f$, notée $\operatorname{Im}(f)$, est définie comme l'ensemble des vecteurs $\mathbf{w} \in F$ pour lesquels il existe au moins un vecteur $\mathbf{v} \in E$ tel que $f(\mathbf{v}) = \mathbf{w}$.
Pour une application linéaire $f: E \to F$, l'image $\operatorname{Im}(f)$ est un sous-espace vectoriel de $F$.
De plus, l'image d'une application linéaire est engendrée par les images des vecteurs d'une base quelconque de l'espace de départ $E$.

Considérons la base canonique de l'espace vectoriel de départ $E = \mathbb{R}^3$, notée $B_E = \{ \mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3 \}$, où les vecteurs sont définis comme suit :
*   $\mathbf{e}_1 = (1,0,0) \in \mathbb{R}^3$
*   $\mathbf{e}_2 = (0,1,0) \in \mathbb{R}^3$
*   $\mathbf{e}_3 = (0,0,1) \in \mathbb{R}^3$

Calculons les images de ces vecteurs par l'application $f$:
*   Pour le vecteur $\mathbf{e}_1 = (1,0,0)$:
    $$ f(\mathbf{e}_1) = f(1,0,0) = (1-0, 0-0) = (1,0) $$
*   Pour le vecteur $\mathbf{e}_2 = (0,1,0)$:
    $$ f(\mathbf{e}_2) = f(0,1,0) = (0-1, 1-0) = (-1,1) $$
*   Pour le vecteur $\mathbf{e}_3 = (0,0,1)$:
    $$ f(\mathbf{e}_3) = f(0,0,1) = (0-0, 0-1) = (0,-1) $$

L'image de $f$ est l'espace vectoriel engendré par ces trois vecteurs images :
$$ \operatorname{Im}(f) = \operatorname{Vect}((1,0), (-1,1), (0,-1)) $$
Ces vecteurs appartiennent à l'espace vectoriel $F = \mathbb{R}^2$. La dimension de $F$ est $\dim(F) = 2$. Par conséquent, la dimension de $\operatorname{Im}(f)$ ne peut pas excéder 2, c'est-à-dire $\dim(\operatorname{Im}(f)) \le 2$.
Nous devons extraire une base de l'ensemble de vecteurs générateurs $S = \{ (1,0), (-1,1), (0,-1) \}$.

Considérons les deux premiers vecteurs de l'ensemble $S$: $\mathbf{u}_1 = (1,0)$ et $\mathbf{u}_2 = (-1,1)$.
Vérifions si ces deux vecteurs sont linéairement indépendants dans $\mathbb{R}^2$.
Soient $\alpha, \beta \in \mathbb{R}$ des scalaires tels que $\alpha \mathbf{u}_1 + \beta \mathbf{u}_2 = \mathbf{0}_F$.
$$ \alpha(1,0) + \beta(-1,1) = (0,0) $$
Effectuons la multiplication scalaire pour chaque terme :
$$ (\alpha \cdot 1, \alpha \cdot 0) + (\beta \cdot (-1), \beta \cdot 1) = (0,0) $$
$$ (\alpha, 0) + (-\beta, \beta) = (0,0) $$
Effectuons l'addition vectorielle des deux vecteurs résultants :
$$ (\alpha - \beta, 0 + \beta) = (0,0) $$
$$ (\alpha - \beta, \beta) = (0,0) $$
Cette égalité de vecteurs est équivalente au système d'équations linéaires suivant, en égalant les composantes :
$$ \begin{cases} \alpha - \beta = 0 & \quad (L_5) \\ \beta = 0 & \quad (L_6) \end{cases} $$
De l'équation $(L_6)$, nous avons directement $\beta = 0$.
Substituons cette valeur de $\beta$ dans l'équation $(L_5)$:
$$ \alpha - 0 = 0 $$
$$ \alpha = 0 $$
Puisque les seuls scalaires $\alpha$ et $\beta$ qui satisfont l'équation $\alpha \mathbf{u}_1 + \beta \mathbf{u}_2 = \mathbf{0}_F$ sont $\alpha = 0$ et $\beta = 0$, les vecteurs $\mathbf{u}_1 = (1,0)$ et $\mathbf{u}_2 = (-1,1)$ sont linéairement indépendants.

Nous avons trouvé deux vecteurs linéairement indépendants, $(1,0)$ et $(-1,1)$, qui appartiennent à l'espace vectoriel $F = \mathbb{R}^2$.
Puisque la dimension de $\mathbb{R}^2$ est $\dim(\mathbb{R}^2) = 2$, tout ensemble de 2 vecteurs linéairement indépendants dans $\mathbb{R}^2$ forme une base de $\mathbb{R}^2$.
Par conséquent, l'ensemble $B_{\operatorname{Im}(f)} = \{ (1,0), (-1,1) \}$ est une base de $\operatorname{Im}(f)$.
De plus, cela implique que $\operatorname{Im}(f) = \mathbb{R}^2$.

Pour une complétude rigoureuse, nous pouvons vérifier que le troisième vecteur image, $(0,-1)$, est une combinaison linéaire des vecteurs de la base $B_{\operatorname{Im}(f)}$.
Cherchons des scalaires $c_1, c_2 \in \mathbb{R}$ tels que $c_1(1,0) + c_2(-1,1) = (0,-1)$.
$$ (c_1 \cdot 1 + c_2 \cdot (-1), c_1 \cdot 0 + c_2 \cdot 1) = (0,-1) $$
$$ (c_1 - c_2, c_2) = (0,-1) $$
Ce qui conduit au système d'équations :
$$ \begin{cases} c_1 - c_2 = 0 \\ c_2 = -1 \end{cases} $$
De la seconde équation, nous avons $c_2 = -1$.
Substituons la valeur de $c_2 = -1$ dans la première équation :
$$ c_1 - (-1) = 0 $$
$$ c_1 + 1 = 0 $$
$$ c_1 = -1 $$
Ainsi, nous avons $(-1)(1,0) + (-1)(-1,1) = (-1,0) + (1,-1) = (0,-1)$.
Le vecteur $(0,-1)$ est bien une combinaison linéaire de $(1,0)$ et $(-1,1)$, ce qui confirme qu'il est redondant pour la génération de l'espace et que $B_{\operatorname{Im}(f)}$ est bien une base.

La dimension de l'image de $f$, qui est le nombre de vecteurs dans la base $B_{\operatorname{Im}(f)}$, est $\dim(\operatorname{Im}(f)) = 2$.
Le rang de l'application linéaire $f$, noté $\operatorname{rg}(f)$, est défini comme la dimension de son image.
Donc, $\operatorname{rg}(f) = \dim(\operatorname{Im}(f)) = 2$.

### Question 3 : Vérification du théorème du rang

Le théorème du rang est un résultat fondamental de l'algèbre linéaire qui établit une relation entre la dimension de l'espace de départ, la dimension du noyau et la dimension de l'image d'une application linéaire.
Pour toute application linéaire $f: E \to F$, le théorème du rang stipule que :
$$ \dim(E) = \dim(\operatorname{Ker}(f)) + \dim(\operatorname{Im}(f)) $$

Appliquons ce théorème aux résultats obtenus pour l'application linéaire $f$ :
*   La dimension de l'espace vectoriel de départ $E = \mathbb{R}^3$ est $\dim(E) = 3$.
*   D'après les calculs détaillés de la Question 1, la dimension du noyau de $f$ est $\dim(\operatorname{Ker}(f)) = 1$.
*   D'après les calculs détaillés de la Question 2, la dimension de l'image de $f$ est $\dim(\operatorname{Im}(f)) = 2$.

Substituons ces valeurs numériques dans la formule du théorème du rang :
$$ 3 = 1 + 2 $$
Effectuons l'addition dans le membre de droite de l'égalité :
$$ 3 = 3 $$
L'égalité est vérifiée. Par conséquent, le théorème du rang est satisfait pour l'application linéaire $f$ considérée.
