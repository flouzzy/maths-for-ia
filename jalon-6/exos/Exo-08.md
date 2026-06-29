# Exercice 8 : Étude d'une Relation d'Équivalence sur l'Espace des Fonctions Lisses et Structure Algébrique du Quotient
**Difficulté :** ⭐⭐⭐⭐

## Énoncé
Soit $E = \mathcal{C}^\infty(\mathbb{R})$ l'ensemble des fonctions réelles indéfiniment dérivables sur $\mathbb{R}$. Cet ensemble est muni de sa structure d'espace vectoriel réel usuelle (addition de fonctions et multiplication par un scalaire) et de la multiplication ponctuelle des fonctions, faisant de $(E, +, \cdot)$ un anneau commutatif.

On définit sur $E$ la relation $\mathcal{R}$ de la manière suivante : pour toutes fonctions $f, g \in E$,
$$f \mathcal{R} g \iff f(0) = g(0) \quad \text{et} \quad f'(0) = g'(0)$$

1.  Démontrer que $\mathcal{R}$ est une relation d'équivalence sur $E$.
2.  Caractériser les classes d'équivalence de $E$ modulo $\mathcal{R}$. Décrire l'ensemble quotient $E/\mathcal{R}$.
3.  Montrer que l'ensemble quotient $E/\mathcal{R}$ peut être muni d'une structure d'espace vectoriel réel. Préciser les lois d'addition et de multiplication par un scalaire et vérifier qu'elles sont bien définies et satisfont les axiomes d'espace vectoriel.
4.  Montrer que l'ensemble quotient $E/\mathcal{R}$ peut être muni d'une structure d'anneau commutatif. Préciser la loi de multiplication et vérifier qu'elle est bien définie et satisfait les axiomes d'anneau.
5.  Identifier l'anneau $(E/\mathcal{R}, +, \times)$ avec un anneau commutatif connu. Établir un isomorphisme explicite.

## Correction Détaillée

### 1. Démonstration que $\mathcal{R}$ est une relation d'équivalence

Pour démontrer que $\mathcal{R}$ est une relation d'équivalence sur $E$, nous devons vérifier les trois propriétés suivantes : réflexivité, symétrie et transitivité.

*   **Réflexivité :** Pour toute fonction $f \in E$, nous devons montrer que $f \mathcal{R} f$.
    Par définition de la relation $\mathcal{R}$, $f \mathcal{R} f$ si et seulement si $f(0) = f(0)$ et $f'(0) = f'(0)$.
    Ces deux égalités sont vérifiées par définition de l'égalité ponctuelle pour toute fonction $f$.
    Donc, la relation $\mathcal{R}$ est réflexive.

*   **Symétrie :** Pour toutes fonctions $f, g \in E$, nous devons montrer que si $f \mathcal{R} g$, alors $g \mathcal{R} f$.
    Supposons que $f \mathcal{R} g$. Par définition de $\mathcal{R}$, cela signifie que $f(0) = g(0)$ et $f'(0) = g'(0)$.
    Puisque l'égalité est une relation symétrique, nous pouvons écrire $g(0) = f(0)$ et $g'(0) = f'(0)$.
    Ces deux conditions sont précisément la définition de $g \mathcal{R} f$.
    Donc, la relation $\mathcal{R}$ est symétrique.

*   **Transitivité :** Pour toutes fonctions $f, g, h \in E$, nous devons montrer que si $f \mathcal{R} g$ et $g \mathcal{R} h$, alors $f \mathcal{R} h$.
    Supposons que $f \mathcal{R} g$. Par définition de $\mathcal{R}$, cela signifie que $f(0) = g(0)$ et $f'(0) = g'(0)$.
    Supposons également que $g \mathcal{R} h$. Par définition de $\mathcal{R}$, cela signifie que $g(0) = h(0)$ et $g'(0) = h'(0)$.
    En combinant les égalités, nous avons :
    $f(0) = g(0)$ et $g(0) = h(0)$, ce qui implique $f(0) = h(0)$ par transitivité de l'égalité.
    De même, $f'(0) = g'(0)$ et $g'(0) = h'(0)$, ce qui implique $f'(0) = h'(0)$ par transitivité de l'égalité.
    Les conditions $f(0) = h(0)$ et $f'(0) = h'(0)$ sont précisément la définition de $f \mathcal{R} h$.
    Donc, la relation $\mathcal{R}$ est transitive.

Puisque $\mathcal{R}$ est réflexive, symétrique et transitive, $\mathcal{R}$ est bien une relation d'équivalence sur $E$.

### 2. Caractérisation des classes d'équivalence et description de l'ensemble quotient

Soit $f \in E$. La classe d'équivalence de $f$, notée $[f]$, est l'ensemble de toutes les fonctions $g \in E$ telles que $g \mathcal{R} f$.
Par définition de $\mathcal{R}$, $g \in [f]$ si et seulement si $g(0) = f(0)$ et $g'(0) = f'(0)$.
Ainsi, une classe d'équivalence $[f]$ est entièrement caractérisée par les valeurs de la fonction $f$ et de sa première dérivée $f'$ au point $x=0$.
Toutes les fonctions appartenant à une même classe d'équivalence $[f]$ partagent la même valeur en $0$ et la même valeur de leur dérivée première en $0$.
Nous pouvons donc identifier chaque classe d'équivalence par le couple de réels $(f(0), f'(0))$.

L'ensemble quotient $E/\mathcal{R}$ est l'ensemble de toutes ces classes d'équivalence.
Nous pouvons définir une application $\Phi : E \to \mathbb{R}^2$ par $\Phi(f) = (f(0), f'(0))$.
Deux fonctions $f$ et $g$ sont en relation si et seulement si $\Phi(f) = \Phi(g)$.
L'ensemble quotient $E/\mathcal{R}$ est donc en bijection naturelle avec l'ensemble des couples de réels $\mathbb{R}^2$.
Nous pouvons écrire $E/\mathcal{R} \cong \mathbb{R}^2$. Chaque élément de $E/\mathcal{R}$ est un couple $(a,b)$ où $a \in \mathbb{R}$ est la valeur de la fonction en 0 et $b \in \mathbb{R}$ est la valeur de sa dérivée en 0.

### 3. Structure d'espace vectoriel réel sur $E/\mathcal{R}$

L'ensemble $E = \mathcal{C}^\infty(\mathbb{R})$ est un espace vectoriel réel avec les lois d'addition et de multiplication par un scalaire définies pour $f, g \in E$ et $\lambda \in \mathbb{R}$ par :
*   $(f+g)(x) = f(x) + g(x)$ pour tout $x \in \mathbb{R}$.
*   $(\lambda f)(x) = \lambda f(x)$ pour tout $x \in \mathbb{R}$.

Nous allons définir des lois d'addition et de multiplication par un scalaire sur $E/\mathcal{R}$ à partir de celles de $E$.

*   **Définition de l'addition sur $E/\mathcal{R}$ :**
    Pour deux classes $[f], [g] \in E/\mathcal{R}$, on définit leur somme comme la classe de la somme des représentants :
    $$[f] + [g] = [f+g]$$

*   **Vérification que l'addition est bien définie :**
    Pour que cette définition soit valide, nous devons montrer que le résultat de l'opération ne dépend pas du choix des représentants. Autrement dit, si $f \mathcal{R} f'$ et $g \mathcal{R} g'$, alors nous devons montrer que $(f+g) \mathcal{R} (f'+g')$.
    Supposons $f \mathcal{R} f'$. Cela signifie $f(0) = f'(0)$ et $f'(0) = f''(0)$.
    Supposons $g \mathcal{R} g'$. Cela signifie $g(0) = g'(0)$ et $g'(0) = g''(0)$.
    Considérons la fonction $(f+g)$. Sa valeur en $0$ est $(f+g)(0) = f(0) + g(0)$.
    Considérons la fonction $(f'+g')$. Sa valeur en $0$ est $(f'+g')(0) = f'(0) + g'(0)$.
    Puisque $f(0) = f'(0)$ et $g(0) = g'(0)$, il s'ensuit que $f(0) + g(0) = f'(0) + g'(0)$.
    Donc, $(f+g)(0) = (f'+g')(0)$.

    Considérons la dérivée de $(f+g)$ en $0$. La dérivée d'une somme est la somme des dérivées : $(f+g)'(x) = f'(x) + g'(x)$.
    Donc, $(f+g)'(0) = f'(0) + g'(0)$.
    De même, $(f'+g')'(0) = f''(0) + g''(0)$.
    Puisque $f'(0) = f''(0)$ et $g'(0) = g''(0)$, il s'ensuit que $f'(0) + g'(0) = f''(0) + g''(0)$.
    Donc, $(f+g)'(0) = (f'+g')'(0)$.
    Comme $(f+g)(0) = (f'+g')(0)$ et $(f+g)'(0) = (f'+g')'(0)$, nous avons bien $(f+g) \mathcal{R} (f'+g')$.
    L'addition sur $E/\mathcal{R}$ est donc bien définie.

*   **Définition de la multiplication par un scalaire sur $E/\mathcal{R}$ :**
    Pour une classe $[f] \in E/\mathcal{R}$ et un scalaire $\lambda \in \mathbb{R}$, on définit leur produit comme la classe du produit du représentant par le scalaire :
    $$\lambda [f] = [\lambda f]$$

*   **Vérification que la multiplication par un scalaire est bien définie :**
    Nous devons montrer que si $f \mathcal{R} f'$, alors $(\lambda f) \mathcal{R} (\lambda f')$.
    Supposons $f \mathcal{R} f'$. Cela signifie $f(0) = f'(0)$ et $f'(0) = f''(0)$.
    Considérons la fonction $(\lambda f)$. Sa valeur en $0$ est $(\lambda f)(0) = \lambda f(0)$.
    Considérons la fonction $(\lambda f')$. Sa valeur en $0$ est $(\lambda f')(0) = \lambda f'(0)$.
    Puisque $f(0) = f'(0)$, il s'ensuit que $\lambda f(0) = \lambda f'(0)$.
    Donc, $(\lambda f)(0) = (\lambda f')(0)$.

    Considérons la dérivée de $(\lambda f)$ en $0$. La dérivée d'un produit par un scalaire est le produit du scalaire par la dérivée : $(\lambda f)'(x) = \lambda f'(x)$.
    Donc, $(\lambda f)'(0) = \lambda f'(0)$.
    De même, $(\lambda f')'(0) = \lambda f''(0)$.
    Puisque $f'(0) = f''(0)$, il s'ensuit que $\lambda f'(0) = \lambda f''(0)$.
    Donc, $(\lambda f)'(0) = (\lambda f')'(0)$.
    Comme $(\lambda f)(0) = (\lambda f')(0)$ et $(\lambda f)'(0) = (\lambda f')'(0)$, nous avons bien $(\lambda f) \mathcal{R} (\lambda f')$.
    La multiplication par un scalaire sur $E/\mathcal{R}$ est donc bien définie.

*   **Vérification des axiomes d'espace vectoriel :**
    Puisque les lois sur $E/\mathcal{R}$ sont définies à partir des lois sur $E$ et que $E$ est un espace vectoriel, les propriétés des lois sur $E/\mathcal{R}$ sont héritées de $E$. Soient $[f], [g], [h] \in E/\mathcal{R}$ et $\lambda, \mu \in \mathbb{R}$.

    1.  **Associativité de l'addition :**
        $([f] + [g]) + [h] = [f+g] + [h]$ (par définition de l'addition sur $E/\mathcal{R}$)
        $= [(f+g)+h]$ (par définition de l'addition sur $E/\mathcal{R}$)
        $= [f+(g+h)]$ (car l'addition est associative dans $E$)
        $= [f] + [g+h]$ (par définition de l'addition sur $E/\mathcal{R}$)
        $= [f] + ([g] + [h])$ (par définition de l'addition sur $E/\mathcal{R}$).

    2.  **Commutativité de l'addition :**
        $[f] + [g] = [f+g]$ (par définition de l'addition sur $E/\mathcal{R}$)
        $= [g+f]$ (car l'addition est commutative dans $E$)
        $= [g] + [f]$ (par definition de l'addition sur $E/\mathcal{R}$).

    3.  **Élément neutre pour l'addition :**
        Soit $z(x) = 0$ la fonction nulle dans $E$. Sa classe est $[z]$.
        Pour toute classe $[f] \in E/\mathcal{R}$ :
        $[f] + [z] = [f+z]$ (par définition de l'addition sur $E/\mathcal{R}$)
        $= [f]$ (car $z$ est l'élément neutre de l'addition dans $E$).
        La classe de la fonction nulle, $[z]$, est l'élément neutre de l'addition dans $E/\mathcal{R}$. Notons que $z(0)=0$ et $z'(0)=0$.

    4.  **Élément opposé pour l'addition :**
        Pour toute classe $[f] \in E/\mathcal{R}$, considérons la classe $[-f]$.
        $[f] + [-f] = [f+(-f)]$ (par définition de l'addition sur $E/\mathcal{R}$)
        $= [z]$ (car $-f$ est l'opposé de $f$ dans $E$).
        La classe $[-f]$ est l'opposé de $[f]$ dans $E/\mathcal{R}$.

    5.  **Distributivité de la multiplication par un scalaire sur l'addition des scalaires :**
        $(\lambda + \mu)[f] = [(\lambda + \mu)f]$ (par définition de la multiplication par un scalaire sur $E/\mathcal{R}$)
        $= [\lambda f + \mu f]$ (car la multiplication par un scalaire est distributive sur l'addition dans $E$)
        $= [\lambda f] + [\mu f]$ (par définition de l'addition sur $E/\mathcal{R}$)
        $= \lambda[f] + \mu[f]$ (par définition de la multiplication par un scalaire sur $E/\mathcal{R}$).

    6.  **Distributivité de la multiplication par un scalaire sur l'addition des vecteurs :**
        $\lambda([f] + [g]) = \lambda[f+g]$ (par définition de l'addition sur $E/\mathcal{R}$)
        $= [\lambda(f+g)]$ (par définition de la multiplication par un scalaire sur $E/\mathcal{R}$)
        $= [\lambda f + \lambda g]$ (car la multiplication par un scalaire est distributive sur l'addition dans $E$)
        $= [\lambda f] + [\lambda g]$ (par définition de l'addition sur $E/\mathcal{R}$)
        $= \lambda[f] + \lambda[g]$ (par définition de la multiplication par un scalaire sur $E/\mathcal{R}$).

    7.  **Compatibilité de la multiplication par un scalaire avec la multiplication des scalaires :**
        $(\lambda \mu)[f] = [(\lambda \mu)f]$ (par définition de la multiplication par un scalaire sur $E/\mathcal{R}$)
        $= [\lambda (\mu f)]$ (par associativité de la multiplication des scalaires dans $E$)
        $= \lambda [\mu f]$ (par définition de la multiplication par un scalaire sur $E/\mathcal{R}$)
        $= \lambda (\mu[f])$ (par définition de la multiplication par un scalaire sur $E/\mathcal{R}$).

    8.  **Élément neutre pour la multiplication par un scalaire :**
        $1[f] = [1f]$ (par définition de la multiplication par un scalaire sur $E/\mathcal{R}$)
        $= [f]$ (car 1 est l'élément neutre de la multiplication par un scalaire dans $E$).

Toutes les propriétés des espaces vectoriels sont vérifiées. Par conséquent, $(E/\mathcal{R}, +, \cdot)$ est un espace vectoriel réel.

### 4. Structure d'anneau commutatif sur $E/\mathcal{R}$

L'ensemble $E = \mathcal{C}^\infty(\mathbb{R})$ est un anneau commutatif avec l'addition de fonctions (définie précédemment) et la multiplication ponctuelle des fonctions, définie pour $f, g \in E$ par :
*   $(f \cdot g)(x) = f(x) \cdot g(x)$ pour tout $x \in \mathbb{R}$.

Nous allons définir une loi de multiplication sur $E/\mathcal{R}$ à partir de celle de $E$.

*   **Définition de la multiplication sur $E/\mathcal{R}$ :**
    Pour deux classes $[f], [g] \in E/\mathcal{R}$, on définit leur produit comme la classe du produit ponctuel des représentants :
    $$[f] \times [g] = [f \cdot g]$$

*   **Vérification que la multiplication est bien définie :**
    Pour que cette définition soit valide, nous devons montrer que le résultat de l'opération ne dépend pas du choix des représentants. Autrement dit, si $f \mathcal{R} f'$ et $g \mathcal{R} g'$, alors nous devons montrer que $(f \cdot g) \mathcal{R} (f' \cdot g')$.
    Supposons $f \mathcal{R} f'$. Cela signifie $f(0) = f'(0)$ et $f'(0) = f''(0)$.
    Supposons $g \mathcal{R} g'$. Cela signifie $g(0) = g'(0)$ et $g'(0) = g''(0)$.

    Considérons la fonction $(f \cdot g)$. Sa valeur en $0$ est $(f \cdot g)(0) = f(0) \cdot g(0)$.
    Considérons la fonction $(f' \cdot g')$. Sa valeur en $0$ est $(f' \cdot g')(0) = f'(0) \cdot g'(0)$.
    Puisque $f(0) = f'(0)$ et $g(0) = g'(0)$, il s'ensuit que $f(0) \cdot g(0) = f'(0) \cdot g'(0)$.
    Donc, $(f \cdot g)(0) = (f' \cdot g')(0)$.

    Considérons la dérivée de $(f \cdot g)$ en $0$. Par la règle de Leibniz pour la dérivation d'un produit : $(f \cdot g)'(x) = f'(x)g(x) + f(x)g'(x)$.
    Donc, $(f \cdot g)'(0) = f'(0)g(0) + f(0)g'(0)$.
    De même, $(f' \cdot g')'(0) = f''(0)g'(0) + f'(0)g''(0)$.
    Puisque $f'(0) = f''(0)$, $f(0) = f'(0)$, $g(0) = g'(0)$ et $g'(0) = g''(0)$, nous pouvons substituer :
    $(f' \cdot g')'(0) = f'(0)g(0) + f(0)g'(0)$.
    Donc, $(f \cdot g)'(0) = (f' \cdot g')'(0)$.
    Comme $(f \cdot g)(0) = (f' \cdot g')(0)$ et $(f \cdot g)'(0) = (f' \cdot g')'(0)$, nous avons bien $(f \cdot g) \mathcal{R} (f' \cdot g')$.
    La multiplication sur $E/\mathcal{R}$ est donc bien définie.

*   **Vérification des axiomes d'anneau commutatif :**
    Puisque les lois sur $E/\mathcal{R}$ sont définies à partir des lois sur $E$ et que $E$ est un anneau commutatif, les propriétés des lois sur $E/\mathcal{R}$ sont héritées de $E$. Nous avons déjà vérifié que $(E/\mathcal{R}, +)$ est un groupe abélien (partie 3). Il reste à vérifier les propriétés de la multiplication. Soient $[f], [g], [h] \in E/\mathcal{R}$.

    1.  **Associativité de la multiplication :**
        $([f] \times [g]) \times [h] = [f \cdot g] \times [h]$ (par définition de la multiplication sur $E/\mathcal{R}$)
        $= [(f \cdot g) \cdot h]$ (par définition de la multiplication sur $E/\mathcal{R}$)
        $= [f \cdot (g \cdot h)]$ (car la multiplication est associative dans $E$)
        $= [f] \times [g \cdot h]$ (par définition de la multiplication sur $E/\mathcal{R}$)
        $= [f] \times ([g] \times [h])$ (par définition de la multiplication sur $E/\mathcal{R}$).

    2.  **Commutativité de la multiplication :**
        $[f] \times [g] = [f \cdot g]$ (par définition de la multiplication sur $E/\mathcal{R}$)
        $= [g \cdot f]$ (car la multiplication est commutative dans $E$)
        $= [g] \times [f]$ (par définition de la multiplication sur $E/\mathcal{R}$).

    3.  **Élément neutre pour la multiplication :**
        Soit $u(x) = 1$ la fonction constante égale à 1 dans $E$. Sa classe est $[u]$.
        Pour toute classe $[f] \in E/\mathcal{R}$ :
        $[f] \times [u] = [f \cdot u]$ (par définition de la multiplication sur $E/\mathcal{R}$)
        $= [f]$ (car $u$ est l'élément neutre de la multiplication dans $E$).
        La classe de la fonction constante 1, $[u]$, est l'élément neutre de la multiplication dans $E/\mathcal{R}$. Notons que $u(0)=1$ et $u'(0)=0$.

    4.  **Distributivité de la multiplication sur l'addition :**
        $[f] \times ([g] + [h]) = [f] \times [g+h]$ (par définition de l'addition sur $E/\mathcal{R}$)
        $= [f \cdot (g+h)]$ (par définition de la multiplication sur $E/\mathcal{R}$)
        $= [f \cdot g + f \cdot h]$ (car la multiplication est distributive sur l'addition dans $E$)
        $= [f \cdot g] + [f \cdot h]$ (par définition de l'addition sur $E/\mathcal{R}$)
        $= ([f] \times [g]) + ([f] \times [h])$ (par définition de la multiplication sur $E/\mathcal{R}$).

Toutes les propriétés des anneaux commutatifs sont vérifiées. Par conséquent, $(E/\mathcal{R}, +, \times)$ est un anneau commutatif.

### 5. Identification de l'anneau $(E/\mathcal{R}, +, \times)$ avec un anneau connu

Nous avons vu que chaque classe d'équivalence $[f]$ est entièrement déterminée par le couple $(f(0), f'(0))$. Cela suggère un isomorphisme avec un anneau dont les éléments sont des couples de réels.

Considérons l'anneau des nombres duaux, noté $\mathbb{R}[\epsilon]$ où $\epsilon^2 = 0$. Les éléments de cet anneau sont de la forme $a + b\epsilon$ avec $a, b \in \mathbb{R}$.
L'addition est $(a+b\epsilon) + (c+d\epsilon) = (a+c) + (b+d)\epsilon$.
La multiplication est $(a+b\epsilon) \times (c+d\epsilon) = ac + ad\epsilon + bc\epsilon + bd\epsilon^2 = ac + (ad+bc)\epsilon$.

Définissons l'application $\Psi : E/\mathcal{R} \to \mathbb{R}[\epsilon]$ par :
$$\Psi([f]) = f(0) + f'(0)\epsilon$$

Nous allons montrer que $\Psi$ est un isomorphisme d'anneaux.

1.  **$\Psi$ est bien définie :**
    Si $[f] = [g]$, alors $f \mathcal{R} g$, ce qui signifie $f(0) = g(0)$ et $f'(0) = g'(0)$.
    Donc, $f(0) + f'(0)\epsilon = g(0) + g'(0)\epsilon$, ce qui implique $\Psi([f]) = \Psi([g])$.
    L'application $\Psi$ est donc bien définie.

2.  **$\Psi$ est un homomorphisme d'anneaux :**
    *   **Homomorphisme pour l'addition :**
        $\Psi([f] + [g]) = \Psi([f+g])$ (par définition de l'addition dans $E/\mathcal{R}$)
        $= (f+g)(0) + (f+g)'(0)\epsilon$ (par définition de $\Psi$)
        $= (f(0)+g(0)) + (f'(0)+g'(0))\epsilon$ (par propriétés de la somme de fonctions)
        $= (f(0) + f'(0)\epsilon) + (g(0) + g'(0)\epsilon)$ (par définition de l'addition dans $\mathbb{R}[\epsilon]$)
        $= \Psi([f]) + \Psi([g])$ (par définition de $\Psi$).
        $\Psi$ est un homomorphisme additif.

    *   **Homomorphisme pour la multiplication :**
        $\Psi([f] \times [g]) = \Psi([f \cdot g])$ (par définition de la multiplication dans $E/\mathcal{R}$)
        $= (f \cdot g)(0) + (f \cdot g)'(0)\epsilon$ (par définition de $\Psi$)
        $= (f(0)g(0)) + (f'(0)g(0) + f(0)g'(0))\epsilon$ (par propriétés du produit de fonctions et de la dérivée d'un produit)
        $= (f(0) + f'(0)\epsilon) \times (g(0) + g'(0)\epsilon)$ (par définition de la multiplication dans $\mathbb{R}[\epsilon]$)
        $= \Psi([f]) \times \Psi([g])$ (par définition de $\Psi$).
        $\Psi$ est un homomorphisme multiplicatif.

    *   **$\Psi$ préserve l'élément neutre multiplicatif :**
        L'élément neutre multiplicatif dans $E/\mathcal{R}$ est $[u]$ où $u(x)=1$.
        $\Psi([u]) = u(0) + u'(0)\epsilon = 1 + 0\epsilon = 1$.
        L'élément neutre multiplicatif dans $\mathbb{R}[\epsilon]$ est $1 + 0\epsilon$, donc $\Psi$ préserve l'unité.

3.  **$\Psi$ est injectif :**
    Supposons $\Psi([f]) = \Psi([g])$.
    Alors $f(0) + f'(0)\epsilon = g(0) + g'(0)\epsilon$.
    Par unicité de l'écriture des nombres duaux, cela implique $f(0) = g(0)$ et $f'(0) = g'(0)$.
    Par définition de $\mathcal{R}$, cela signifie $f \mathcal{R} g$, donc $[f] = [g]$.
    $\Psi$ est donc injectif.

4.  **$\Psi$ est surjectif :**
    Soit un élément $a + b\epsilon \in \mathbb{R}[\epsilon]$, avec $a, b \in \mathbb{R}$.
    Nous devons trouver une fonction $f \in E$ telle que $\Psi([f]) = a + b\epsilon$.
    C'est-à-dire, nous cherchons une fonction $f \in \mathcal{C}^\infty(\mathbb{R})$ telle que $f(0) = a$ et $f'(0) = b$.
    Un exemple d'une telle fonction est $f(x) = a + bx$.
    Cette fonction est de classe $\mathcal{C}^\infty(\mathbb{R})$ (c'est un polynôme).
    Pour cette fonction, $f(0) = a + b(0) = a$ et $f'(x) = b$, donc $f'(0) = b$.
    Ainsi, $\Psi([a+bx]) = a + b\epsilon$.
    Pour tout élément de $\mathbb{R}[\epsilon]$, il existe une classe d'équivalence dans $E/\mathcal{R}$ dont l'image par $\Psi$ est cet élément.
    $\Psi$ est donc surjectif.

Puisque $\Psi$ est un homomorphisme d'anneaux bijectif, $\Psi$ est un isomorphisme d'anneaux.
Par conséquent, l'anneau $(E/\mathcal{R}, +, \times)$ est isomorphe à l'anneau des nombres duaux $\mathbb{R}[\epsilon]$.