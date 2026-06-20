# Exercice 1 : Applications linéaires élémentaires (Difficulté : \*)

## Énoncé du problème

On considère l'application $f: \mathbb{R}^2 \to \mathbb{R}^3$ définie pour tout $(x, y) \in \mathbb{R}^2$ par :
$$f(x, y) = (x+y, x-y, 2x)$$
où $\mathbb{R}$ est le corps des nombres réels.

1.  Démontrer que $f$ est une application linéaire.
2.  Déterminer le noyau de $f$, noté $\text{ker}(f)$. En donner une base et préciser sa dimension.
3.  Déterminer l'image de $f$, notée $\text{Im}(f)$. En donner une base et préciser sa dimension (qui est le rang de $f$).
4.  Vérifier le théorème du rang pour l'application $f$.

## Correction détaillée

### 1. Démontrer que $f$ est une application linéaire.

Pour qu'une application $f: E \to F$ soit linéaire, où $E$ et $F$ sont des espaces vectoriels sur un corps $K$, elle doit satisfaire deux propriétés :
a) $f(\mathbf{u} + \mathbf{v}) = f(\mathbf{u}) + f(\mathbf{v})$ pour tous $\mathbf{u}, \mathbf{v} \in E$.
b) $f(\lambda \mathbf{u}) = \lambda f(\mathbf{u})$ pour tout $\lambda \in K$ et tout $\mathbf{u} \in E$.

Soient $\mathbf{u} = (x_1, y_1)$ et $\mathbf{v} = (x_2, y_2)$ deux vecteurs de $\mathbb{R}^2$.
Soit $\lambda \in \mathbb{R}$ un scalaire.

#### Propriété a) : Additivité
$\mathbf{u} + \mathbf{v} = (x_1+x_2, y_1+y_2)$.
Calculons $f(\mathbf{u} + \mathbf{v})$ :
$$f(\mathbf{u} + \mathbf{v}) = f(x_1+x_2, y_1+y_2) = ((x_1+x_2)+(y_1+y_2), (x_1+x_2)-(y_1+y_2), 2(x_1+x_2))$$
Réorganisons les termes :
$$f(\mathbf{u} + \mathbf{v}) = ((x_1+y_1)+(x_2+y_2), (x_1-y_1)+(x_2-y_2), 2x_1+2x_2)$$
Par ailleurs, calculons $f(\mathbf{u}) + f(\mathbf{v})$ :
$$f(\mathbf{u}) = (x_1+y_1, x_1-y_1, 2x_1)$$
$$f(\mathbf{v}) = (x_2+y_2, x_2-y_2, 2x_2)$$
$$f(\mathbf{u}) + f(\mathbf{v}) = ((x_1+y_1)+(x_2+y_2), (x_1-y_1)+(x_2-y_2), (2x_1)+(2x_2))$$
Nous constatons que $f(\mathbf{u} + \mathbf{v}) = f(\mathbf{u}) + f(\mathbf{v})$. La première propriété est vérifiée.

#### Propriété b) : Homogénéité
$\lambda \mathbf{u} = (\lambda x_1, \lambda y_1)$.
Calculons $f(\lambda \mathbf{u})$ :
$$f(\lambda \mathbf{u}) = f(\lambda x_1, \lambda y_1) = (\lambda x_1 + \lambda y_1, \lambda x_1 - \lambda y_1, 2\lambda x_1)$$
Factorisons $\lambda$ dans chaque composante :
$$f(\lambda \mathbf{u}) = (\lambda(x_1 + y_1), \lambda(x_1 - y_1), \lambda(2x_1))$$
$$f(\lambda \mathbf{u}) = \lambda(x_1 + y_1, x_1 - y_1, 2x_1)$$
Par définition de $f(\mathbf{u})$, on a :
$$f(\lambda \mathbf{u}) = \lambda f(\mathbf{u})$$
La deuxième propriété est vérifiée.

Puisque les deux propriétés sont satisfaites, $f$ est bien une application linéaire.

### 2. Déterminer le noyau de $f$, $\text{ker}(f)$. En donner une base et sa dimension.

Le noyau de $f$, $\text{ker}(f)$, est l'ensemble des vecteurs $\mathbf{u} \in \mathbb{R}^2$ tels que $f(\mathbf{u}) = \mathbf{0}_{\mathbb{R}^3}$, où $\mathbf{0}_{\mathbb{R}^3}$ est le vecteur nul de $\mathbb{R}^3$.
Soit $\mathbf{u} = (x, y) \in \mathbb{R}^2$.
$f(x, y) = (0, 0, 0)$ implique le système d'équations linéaires suivant :
1.  $x+y = 0$
2.  $x-y = 0$
3.  $2x = 0$

À partir de l'équation (3), nous déduisons directement $x = 0$.
Substituons $x=0$ dans l'équation (1) :
$0+y = 0 \implies y = 0$.
Vérifions ces valeurs dans l'équation (2) :
$0-0 = 0$, ce qui est consistant.

Ainsi, le seul vecteur $(x, y)$ qui satisfait $f(x, y) = (0, 0, 0)$ est $(0, 0)$.
Donc, $\text{ker}(f) = \{(0, 0)\}$.

Une base de $\text{ker}(f)$ est l'ensemble vide $\emptyset$, car le noyau ne contient que le vecteur nul.
La dimension de $\text{ker}(f)$, notée $\text{dim}(\text{ker}(f))$, est 0.

### 3. Déterminer l'image de $f$, $\text{Im}(f)$. En donner une base et sa dimension.

L'image de $f$, $\text{Im}(f)$, est l'ensemble des vecteurs de $\mathbb{R}^3$ qui sont des images de vecteurs de $\mathbb{R}^2$ par $f$.
$\text{Im}(f) = \{ f(x,y) \mid (x,y) \in \mathbb{R}^2 \}$.
On peut écrire $f(x,y)$ comme une combinaison linéaire de vecteurs fixes :
$$f(x,y) = (x+y, x-y, 2x) = (x,x,2x) + (y,-y,0)$$
$$f(x,y) = x(1,1,2) + y(1,-1,0)$$
Ceci signifie que l'image de $f$ est l'espace vectoriel engendré par les vecteurs $v_1 = (1,1,2)$ et $v_2 = (1,-1,0)$.
$\text{Im}(f) = \text{Vect}((1,1,2), (1,-1,0))$.

Pour trouver une base de $\text{Im}(f)$, nous devons vérifier si les vecteurs $v_1$ et $v_2$ sont linéairement indépendants.
Soient $\lambda_1, \lambda_2 \in \mathbb{R}$ tels que $\lambda_1 v_1 + \lambda_2 v_2 = \mathbf{0}_{\mathbb{R}^3}$.
$$\lambda_1(1,1,2) + \lambda_2(1,-1,0) = (0,0,0)$$
Ceci conduit au système d'équations :
1.  $\lambda_1 + \lambda_2 = 0$
2.  $\lambda_1 - \lambda_2 = 0$
3.  $2\lambda_1 = 0$

De l'équation (3), nous obtenons $\lambda_1 = 0$.
Substituons $\lambda_1 = 0$ dans l'équation (1) :
$0 + \lambda_2 = 0 \implies \lambda_2 = 0$.
Substituons $\lambda_1 = 0$ et $\lambda_2 = 0$ dans l'équation (2) :
$0 - 0 = 0$, ce qui est consistant.

Puisque la seule solution est $\lambda_1 = 0$ et $\lambda_2 = 0$, les vecteurs $v_1 = (1,1,2)$ et $v_2 = (1,-1,0)$ sont linéairement indépendants.
Ils forment donc une base de $\text{Im}(f)$.
Une base de $\text{Im}(f)$ est $\{(1,1,2), (1,-1,0)\}$.
La dimension de $\text{Im}(f)$, notée $\text{dim}(\text{Im}(f))$, est le nombre de vecteurs dans sa base, soit 2.
Le rang de $f$ est $\text{rg}(f) = \text{dim}(\text{Im}(f)) = 2$.

### 4. Vérifier le théorème du rang.

Le théorème du rang stipule que pour une application linéaire $f: E \to F$, où $E$ est un espace vectoriel de dimension finie, on a :
$$\text{dim}(E) = \text{dim}(\text{ker}(f)) + \text{dim}(\text{Im}(f))$$

Dans notre cas :
L'espace de départ $E$ est $\mathbb{R}^2$. Sa dimension est $\text{dim}(\mathbb{R}^2) = 2$.
Nous avons trouvé $\text{dim}(\text{ker}(f)) = 0$.
Nous avons trouvé $\text{dim}(\text{Im}(f)) = 2$.

Vérifions l'égalité :
$\text{dim}(\text{ker}(f)) + \text{dim}(\text{Im}(f)) = 0 + 2 = 2$.
Cette somme est égale à la dimension de l'espace de départ $\mathbb{R}^2$.
$$2 = 2$$
Le théorème du rang est bien vérifié pour cette application linéaire.