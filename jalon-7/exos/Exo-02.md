# Exercice 2 : Vérification de la Liberté d'une Famille Unitaire Non Nulle

## Énoncé

Soit $\mathbb{K}$ un corps commutatif quelconque.
Soit $E$ un $\mathbb{K}$-espace vectoriel.
Soit $v$ un vecteur de $E$ tel que $v \neq 0_E$, où $0_E$ désigne le vecteur nul de l'espace vectoriel $E$.

Démontrer que la famille de vecteurs $\mathcal{F} = \{v\}$ est une famille libre dans $E$.

## Correction Détaillée

Pour démontrer qu'une famille de vecteurs est libre dans un espace vectoriel, nous devons montrer que la seule combinaison linéaire de ces vecteurs qui est égale au vecteur nul est celle dont tous les coefficients scalaires sont nuls.

Dans le cas de la famille $\mathcal{F} = \{v\}$, qui ne contient qu'un seul vecteur, nous devons considérer une combinaison linéaire de ce vecteur $v$ qui est égale au vecteur nul $0_E$.
Soit $\lambda$ un scalaire appartenant au corps $\mathbb{K}$.
Nous posons l'équation suivante :
$$ \lambda \cdot v = 0_E $$
Notre objectif est de démontrer que cette équation implique nécessairement que le scalaire $\lambda$ est égal à l'élément neutre de l'addition dans le corps $\mathbb{K}$, noté $0_{\mathbb{K}}$.

Nous allons analyser cette équation en considérant deux cas possibles pour le scalaire $\lambda$.

**Cas 1 :** Supposons que $\lambda = 0_{\mathbb{K}}$.
Si le scalaire $\lambda$ est l'élément nul du corps $\mathbb{K}$, alors l'équation devient :
$$ 0_{\mathbb{K}} \cdot v $$
Par l'un des axiomes fondamentaux de la définition d'un espace vectoriel, le produit du scalaire nul $0_{\mathbb{K}}$ par n'importe quel vecteur $v$ de l'espace $E$ est toujours égal au vecteur nul de l'espace $E$.
$$ 0_{\mathbb{K}} \cdot v = 0_E $$
Dans ce cas, l'équation $\lambda \cdot v = 0_E$ est satisfaite lorsque $\lambda = 0_{\mathbb{K}}$. Ce cas est donc compatible avec la définition d'une famille libre.

**Cas 2 :** Supposons que $\lambda \neq 0_{\mathbb{K}}$.
Si le scalaire $\lambda$ est un élément non nul du corps $\mathbb{K}$, alors, par définition d'un corps, il admet un inverse multiplicatif dans $\mathbb{K}$. Nous noterons cet inverse $\lambda^{-1}$.
Nous allons multiplier l'équation initiale $\lambda \cdot v = 0_E$ par ce scalaire $\lambda^{-1}$ à gauche.
$$ \lambda^{-1} \cdot (\lambda \cdot v) = \lambda^{-1} \cdot 0_E $$
En utilisant l'axiome d'associativité de la multiplication scalaire dans un espace vectoriel, nous pouvons regrouper les scalaires :
$$ (\lambda^{-1} \cdot \lambda) \cdot v = \lambda^{-1} \cdot 0_E $$
Par la définition de l'inverse multiplicatif dans le corps $\mathbb{K}$, le produit $\lambda^{-1} \cdot \lambda$ est égal à l'élément neutre de la multiplication dans le corps $\mathbb{K}$, noté $1_{\mathbb{K}}$.
$$ 1_{\mathbb{K}} \cdot v = \lambda^{-1} \cdot 0_E $$
De plus, par un autre axiome fondamental de la définition d'un espace vectoriel, le produit de n'importe quel scalaire (ici $\lambda^{-1}$) par le vecteur nul $0_E$ est toujours égal au vecteur nul de l'espace $E$.
$$ 1_{\mathbb{K}} \cdot v = 0_E $$
Enfin, par un dernier axiome fondamental de la définition d'un espace vectoriel, le produit de l'élément neutre de la multiplication du corps $1_{\mathbb{K}}$ par un vecteur $v$ est égal à ce vecteur $v$ lui-même.
$$ v = 0_E $$
Cette conclusion, $v = 0_E$, contredit directement l'hypothèse de l'énoncé qui stipule que $v \neq 0_E$.
Puisque notre hypothèse $\lambda \neq 0_{\mathbb{K}}$ a conduit à une contradiction avec une donnée de l'énoncé, cette hypothèse doit être fausse.

Par conséquent, la seule possibilité pour le scalaire $\lambda$ est que $\lambda = 0_{\mathbb{K}}$.

En résumé, nous avons montré que si $\lambda \cdot v = 0_E$, alors nécessairement $\lambda = 0_{\mathbb{K}}$.
Ceci correspond exactement à la définition d'une famille libre.

Nous pouvons donc conclure que la famille $\mathcal{F} = \{v\}$ est une famille libre dans $E$.
