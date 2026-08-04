---
title: "Exercice 10 : Différentiabilité et Gradient"
difficulty: "★★★★★"
---

# Exercice 10 : Extremum sous contrainte et multiplicateur de Lagrange (Approche géométrique)

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit $f, g : \mathbb{R}^2 \to \mathbb{R}$ deux fonctions de classe $\mathcal{C}^1$. On cherche à maximiser $f(x, y)$ sous la contrainte $g(x, y) = c$. Soit $M_0(x_0, y_0)$ un tel extremum local. Démontrer géométriquement, en utilisant la notion de différentielle et de gradient, qu'il existe un scalaire $\lambda \in \mathbb{R}$ tel que $\nabla f(x_0, y_0) = \lambda \nabla g(x_0, y_0)$, en supposant que $\nabla g(x_0, y_0) \neq 0$.

---
## Correction Détaillée

L'ensemble de contrainte est la courbe de niveau $\mathcal{C} = \{(x, y) \in \mathbb{R}^2 \mid g(x, y) = c\}$.
La condition $\nabla g(x_0, y_0) \neq 0$ assure que le point $M_0$ est régulier pour la courbe $\mathcal{C}$. Le théorème des fonctions implicites garantit alors que $\mathcal{C}$ admet une tangente euclidienne au point $M_0$.

**1. Vecteur tangent et gradient de la contrainte :**
Soit $\gamma(t) = (x(t), y(t))$ une courbe paramétrée de classe $\mathcal{C}^1$ incluse dans $\mathcal{C}$ telle que $\gamma(0) = M_0$.
Puisque la courbe est sur $\mathcal{C}$, on a $g(\gamma(t)) = c$ pour tout $t$.
Dérivons cette expression par rapport à $t$ au point $t=0$ en utilisant la règle de la chaîne :
$$ \frac{d}{dt} g(\gamma(t)) \Big|_{t=0} = 0 \implies dg_{M_0}(\gamma'(0)) = 0 \implies \langle \nabla g(M_0), \gamma'(0) \rangle = 0 $$
Cette relation indique que le vecteur gradient $\nabla g(M_0)$ est orthogonal à tout vecteur tangent $\gamma'(0)$ à la courbe $\mathcal{C}$ en $M_0$.

**2. Condition d'optimalité locale pour la fonction objectif $f$ :**
La fonction scalaire composée $\phi(t) = f(\gamma(t))$ représente la valeur de la fonction objectif restreinte aux déplacements le long de la contrainte.
Puisque $M_0$ (soit $t=0$) est un extremum local de $f$ sur $\mathcal{C}$, $t=0$ est un extremum local de $\phi(t)$ sur $\mathbb{R}$.
Une condition nécessaire d'optimalité pour une fonction dérivable d'une variable réelle est la nullité de sa dérivée :
$$ \phi'(0) = 0 $$
Appliquons la règle de la chaîne à $\phi$ :
$$ \phi'(0) = df_{M_0}(\gamma'(0)) = \langle \nabla f(M_0), \gamma'(0) \rangle = 0 $$
Cette équation signifie que le vecteur gradient de l'objectif $\nabla f(M_0)$ est lui aussi orthogonal à la courbe $\mathcal{C}$ en $M_0$.

**3. Conclusion géométrique et algébrique :**
Dans le plan $\mathbb{R}^2$, l'orthogonal à une droite (la tangente) est une droite vectorielle (la direction normale de dimension 1).
Puisque les deux gradients $\nabla f(M_0)$ et $\nabla g(M_0)$ sont orthogonaux au même vecteur non nul $\gamma'(0)$ (vecteur tangent), ils appartiennent tous deux à l'espace normal, qui est de dimension 1 engendré par $\nabla g(M_0) \neq 0$.
Par conséquent, ces deux vecteurs sont colinéaires. Il existe donc un réel $\lambda$ (le multiplicateur de Lagrange) tel que :
$$ \nabla f(M_0) = \lambda \nabla g(M_0) $$
Cette colinéarité géométrique traduit l'impossibilité d'augmenter la fonction $f$ sans quitter l'ensemble de niveau $g=c$.
