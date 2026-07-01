# Exercice 1 : Applications linéaires élémentaires (Difficulté : \*)

## Énoncé du problème

On considère l'application $f: \mathbb{R}^2 \to \mathbb{R}^3$ définie pour tout vecteur $(x, y) \in \mathbb{R}^2$ par :
$$f(x, y) = (x+y, x-y, 2x)$$
où $\mathbb{R}$ est le corps des nombres réels. L'ensemble $\mathbb{R}^2$ est l'espace vectoriel des couples de nombres réels, et $\mathbb{R}^3$ est l'espace vectoriel des triplets de nombres réels, tous deux munis des opérations d'addition vectorielle et de multiplication par un scalaire usuelles sur le corps $\mathbb{R}$.

1.  Démontrer que $f$ est une application linéaire.
2.  Déterminer le noyau de $f$, noté $\text{ker}(f)$. En donner une base et préciser sa dimension.
3.  Déterminer l'image de $f$, notée $\text{Im}(f)$. En donner une base et préciser sa dimension (qui est le rang de $f$).
4.  Vérifier le théorème du rang pour l'application $f$.

## Correction détaillée

### 1. Démontrer que $f$ est une application linéaire.

Pour qu'une application $f: E \to F$ soit linéaire, où $E$ et $F$ sont des espaces vectoriels sur un corps $K$, elle doit satisfaire deux propriétés fondamentales :
a) Additivité : $f(\mathbf{u} + \mathbf{v}) = f(\mathbf{u}) + f(\mathbf{v})$ pour tous vecteurs $\mathbf{u}, \mathbf{v} \in E$.
b) Homogénéité : $f(\lambda \mathbf{u}) = \lambda f(\mathbf{u})$ pour tout scalaire $\lambda \in K$ et tout vecteur $\mathbf{u} \in E$.

Dans le cadre de cet exercice, l'espace de départ est $E = \mathbb{R}^2$, l'espace d'arrivée est $F = \mathbb{R}^3$, et le corps des scalaires est $K = \mathbb{R}$.

Soient $\mathbf{u} = (x_1, y_1)$ et $\mathbf{v} = (x_2, y_2)$ deux vecteurs arbitraires de l'espace vectoriel $\mathbb{R}^2$.
Soit $\lambda \in \mathbb{R}$ un scalaire arbitraire.

#### Propriété a) : Additivité

Calculons d'abord la somme des vecteurs $\mathbf{u}$ et $\mathbf{v}$ dans $\mathbb{R}^2$:
$$\mathbf{u} + \mathbf{v} = (x_1, y_1) + (x_2, y_2) = (x_1+x_2, y_1+y_2)$$
Appliquons ensuite la fonction $f$ à ce vecteur somme :
$$f(\mathbf{u} + \mathbf{v}) = f(x_1+x_2, y_1+y_2)$$
Par la définition de $f$, où la première composante est la somme des coordonnées, la deuxième est leur différence, et la troisième est le double de la première coordonnée :
$$f(\mathbf{u} + \mathbf{v}) = ((x_1+x_2)+(y_1+y_2), (x_1+x_2)-(y_1+y_2), 2(x_1+x_2))$$
Réorganisons les termes au sein de chaque composante pour regrouper les termes relatifs à $\mathbf{u}$ et $\mathbf{v}$ :
$$f(\mathbf{u} + \mathbf{v}) = ((x_1+y_1)+(x_2+y_2), (x_1-y_1)+(x_2-y_2), 2x_1+2x_2)$$

Calculons maintenant la somme des images $f(\mathbf{u})$ et $f(\mathbf{v})$ :
$$f(\mathbf{u}) = (x_1+y_1, x_1-y_1, 2x_1)$$
$$f(\mathbf{v}) = (x_2+y_2, x_2-y_2, 2x_2)$$
Effectuons l'addition de ces deux vecteurs dans $\mathbb{R}^3$ :
$$f(\mathbf{u}) + f(\mathbf{v}) = ((x_1+y_1)+(x_2+y_2), (x_1-y_1)+(x_2-y_2), (2x_1)+(2x_2))$$
En comparant les expressions obtenues pour $f(\mathbf{u} + \mathbf{v})$ et $f(\mathbf{u}) + f(\mathbf{v})$, nous observons qu'elles sont identiques.
Ainsi, la propriété d'additivité $f(\mathbf{u} + \mathbf{v}) = f(\mathbf{u}) + f(\mathbf{v})$ est vérifiée.

#### Propriété b) : Homogénéité

Calculons d'abord le produit du scalaire $\lambda$ par le vecteur $\mathbf{u}$ dans $\mathbb{R}^2$:
$$\lambda \mathbf{u} = \lambda (x_1, y_1) = (\lambda x_1, \lambda y_1)$$
Appliquons ensuite la fonction $f$ à ce vecteur :
$$f(\lambda \mathbf{u}) = f(\lambda x_1, \lambda y_1)$$
Par la définition de $f$ :
$$f(\lambda \mathbf{u}) = (\lambda x_1 + \lambda y_1, \lambda x_1 - \lambda y_1, 2\lambda x_1)$$
Factorisons le scalaire $\lambda$ dans chaque composante du vecteur résultant :
$$f(\lambda \mathbf{u}) = (\lambda(x_1 + y_1), \lambda(x_1 - y_1), \lambda(2x_1))$$
Nous pouvons extraire le scalaire $\lambda$ du vecteur :
$$f(\lambda \mathbf{u}) = \lambda(x_1 + y_1, x_1 - y_1, 2x_1)$$
Par la définition de $f(\mathbf{u})$, nous reconnaissons l'expression entre parenthèses :
$$f(\lambda \mathbf{u}) = \lambda f(\mathbf{u})$$
Ainsi, la propriété d'homogénéité $f(\lambda \mathbf{u}) = \lambda f(\mathbf{u})$ est vérifiée.

Puisque les deux propriétés d'additivité et d'homogénéité sont satisfaites, l'application $f: \mathbb{R}^2 \to \mathbb{R}^3$ est bien une application linéaire.

### 2. Déterminer le noyau de $f$, $\text{ker}(f)$. En donner une base et sa dimension.

Le noyau de $f$, noté $\text{ker}(f)$, est défini comme l'ensemble des vecteurs $\mathbf{u} \in \mathbb{R}^2$ tels que leur image par $f$ est le vecteur nul de l'espace d'arrivée $\mathbb{R}^3$.
Formellement : $\text{ker}(f) = \{ \mathbf{u} \in \mathbb{R}^2 \mid f(\mathbf{u}) = \mathbf{0}_{\mathbb{R}^3} \}$.
Soit un vecteur $\mathbf{u} = (x, y) \in \mathbb{R}^2$. Le vecteur nul de $\mathbb{R}^3$ est $\mathbf{0}_{\mathbb{R}^3} = (0, 0, 0)$.
L'équation $f(x, y) = (0, 0, 0)$ se traduit par le système d'équations linéaires suivant :
1.  $x+y = 0$
2.  $x-y = 0$
3.  $2x = 0$

Nous allons résoudre ce système étape par étape :
À partir de l'équation (3) :
$$2x = 0$$
En divisant par 2 (qui est non nul dans $\mathbb{R}$), nous obtenons :
$$x = 0$$
Substituons la valeur de $x=0$ dans l'équation (1) :
$$0+y = 0$$
$$y = 0$$
Vérifions ces valeurs $x=0$ et $y=0$ dans l'équation (2) :
$$0-0 = 0$$
L'équation (2) est satisfaite.

Par conséquent, le seul vecteur $(x, y)$ de $\mathbb{R}^2$ qui satisfait la condition $f(x, y) = \mathbf{0}_{\mathbb{R}^3}$ est le vecteur nul $(0, 0)$.
Donc, le noyau de $f$ est $\text{ker}(f) = \{ (0, 0) \}$.

L'espace vectoriel $\{(0,0)\}$ est l'espace vectoriel réduit au vecteur nul. Une base de cet espace est l'ensemble vide $\emptyset$.
La dimension de $\text{ker}(f)$, notée $\text{dim}(\text{ker}(f))$, est le nombre de vecteurs dans sa base. Puisque la base est l'ensemble vide, la dimension est 0.
$$\text{dim}(\text{ker}(f)) = 0$$

### 3. Déterminer l'image de $f$, $\text{Im}(f)$. En donner une base et sa dimension.

L'image de $f$, notée $\text{Im}(f)$, est l'ensemble des vecteurs de l'espace d'arrivée $\mathbb{R}^3$ qui sont des images d'au moins un vecteur de l'espace de départ $\mathbb{R}^2$ par l'application $f$.
Formellement : $\text{Im}(f) = \{ f(x,y) \mid (x,y) \in \mathbb{R}^2 \}$.
Considérons un vecteur générique $f(x,y)$ dans $\text{Im}(f)$ :
$$f(x,y) = (x+y, x-y, 2x)$$
Nous pouvons décomposer ce vecteur en une somme de vecteurs, en regroupant les termes dépendant de $x$ et ceux dépendant de $y$ :
$$f(x,y) = (x, x, 2x) + (y, -y, 0)$$
En factorisant les scalaires $x$ et $y$ de chaque vecteur :
$$f(x,y) = x(1,1,2) + y(1,-1,0)$$
Cette expression montre que tout vecteur dans l'image de $f$ peut être écrit comme une combinaison linéaire des vecteurs $v_1 = (1,1,2)$ et $v_2 = (1,-1,0)$.
Par conséquent, l'image de $f$ est l'espace vectoriel engendré par ces deux vecteurs :
$$\text{Im}(f) = \text{Vect}((1,1,2), (1,-1,0))$$

Pour déterminer une base de $\text{Im}(f)$, nous devons vérifier si les vecteurs $v_1$ et $v_2$ sont linéairement indépendants.
Soient $\lambda_1, \lambda_2 \in \mathbb{R}$ deux scalaires tels que leur combinaison linéaire est égale au vecteur nul de $\mathbb{R}^3$:
$$\lambda_1 v_1 + \lambda_2 v_2 = \mathbf{0}_{\mathbb{R}^3}$$
$$\lambda_1(1,1,2) + \lambda_2(1,-1,0) = (0,0,0)$$
Ceci conduit au système d'équations linéaires suivant, en égalant les composantes :
1.  $\lambda_1 + \lambda_2 = 0$
2.  $\lambda_1 - \lambda_2 = 0$
3.  $2\lambda_1 = 0$

Nous allons résoudre ce système étape par étape :
À partir de l'équation (3) :
$$2\lambda_1 = 0$$
En divisant par 2, nous obtenons :
$$\lambda_1 = 0$$
Substituons la valeur de $\lambda_1=0$ dans l'équation (1) :
$$0 + \lambda_2 = 0$$
$$\lambda_2 = 0$$
Vérifions ces valeurs $\lambda_1=0$ et $\lambda_2=0$ dans l'équation (2) :
$$0 - 0 = 0$$
L'équation (2) est satisfaite.

Puisque la seule solution au système est $\lambda_1 = 0$ et $\lambda_2 = 0$, les vecteurs $v_1 = (1,1,2)$ et $v_2 = (1,-1,0)$ sont linéairement indépendants.
Comme ils engendrent $\text{Im}(f)$ et sont linéairement indépendants, ils forment une base de $\text{Im}(f)$.
Une base de $\text{Im}(f)$ est donc $\{(1,1,2), (1,-1,0)\}$.
La dimension de $\text{Im}(f)$, notée $\text{dim}(\text{Im}(f))$, est le nombre de vecteurs dans cette base, soit 2.
Le rang de $f$, noté $\text{rg}(f)$, est par définition la dimension de son image.
$$\text{rg}(f) = \text{dim}(\text{Im}(f)) = 2$$

### 4. Vérifier le théorème du rang.

Le théorème du rang est un résultat fondamental en algèbre linéaire qui relie la dimension de l'espace de départ, la dimension du noyau, et la dimension de l'image d'une application linéaire. Pour une application linéaire $f: E \to F$, où $E$ est un espace vectoriel de dimension finie, le théorème stipule que :
$$\text{dim}(E) = \text{dim}(\text{ker}(f)) + \text{dim}(\text{Im}(f))$$

Appliquons ce théorème à l'application linéaire $f: \mathbb{R}^2 \to \mathbb{R}^3$ que nous avons étudiée :
L'espace de départ $E$ est $\mathbb{R}^2$. Sa dimension est $\text{dim}(\mathbb{R}^2) = 2$.
D'après nos calculs de la partie 2, la dimension du noyau de $f$ est $\text{dim}(\text{ker}(f)) = 0$.
D'après nos calculs de la partie 3, la dimension de l'image de $f$ est $\text{dim}(\text{Im}(f)) = 2$.

Vérifions l'égalité du théorème du rang en substituant ces valeurs :
$$\text{dim}(\text{ker}(f)) + \text{dim}(\text{Im}(f)) = 0 + 2$$
$$\text{dim}(\text{ker}(f)) + \text{dim}(\text{Im}(f)) = 2$$
Nous comparons cette somme à la dimension de l'espace de départ :
$$\text{dim}(E) = 2$$
L'égalité est vérifiée :
$$2 = 2$$
Le théorème du rang est bien vérifié pour l'application linéaire $f$.
