# Exercice 9 - Difficulté \quad $\bigstar$$\bigstar$$\bigstar$$\bigstar$$\bigstar$

## Énoncé
Soit $E = \mathcal{M}_n(\mathbb{R})$ l'espace vectoriel des matrices carrées.
On considère l'endomorphisme $\phi : E \to E$ défini par $\phi(M) = M^T$.
1. Calculer $\phi \circ \phi$.
2. En déduire les valeurs propres possibles de $\phi$.
3. Déterminer les sous-espaces propres associés et vérifier que $\phi$ est diagonalisable.

## Solution Complète

**Étape 1 : Composition de l'endomorphisme**
Pour toute matrice $M \in \mathcal{M}_n(\mathbb{R})$ :
$$(\phi \circ \phi)(M) = \phi(\phi(M)) = \phi(M^T) = (M^T)^T = M$$
Ainsi, $\phi \circ \phi = \text{Id}_E$.
L'endomorphisme $\phi$ est donc une involution (ou symétrie).

**Étape 2 : Valeurs propres possibles**
Le polynôme $P(X) = X^2 - 1$ est un polynôme annulateur de $\phi$ puisque $P(\phi) = \phi^2 - \text{Id}_E = 0$.
D'après le cours sur la réduction des endomorphismes, les valeurs propres de $\phi$ sont nécessairement des racines d'un de ses polynômes annulateurs.
Les racines de $X^2 - 1 = 0$ sont $1$ et $-1$.
Le spectre de $\phi$ est donc inclus dans $\{-1, 1\}$.

**Étape 3 : Sous-espaces propres**
Cherchons les sous-espaces propres.
- Pour $\lambda = 1$ : $E_1 = \ker(\phi - \text{Id}_E)$. C'est l'ensemble des matrices telles que $\phi(M) = M$, soit $M^T = M$. C'est l'ensemble $\mathcal{S}_n(\mathbb{R})$ des matrices symétriques. La dimension de cet espace est $\frac{n(n+1)}{2}$.
- Pour $\lambda = -1$ : $E_{-1} = \ker(\phi + \text{Id}_E)$. C'est l'ensemble des matrices telles que $\phi(M) = -M$, soit $M^T = -M$. C'est l'ensemble $\mathcal{A}_n(\mathbb{R})$ des matrices antisymétriques. La dimension de cet espace est $\frac{n(n-1)}{2}$.

**Étape 4 : Conclusion sur la diagonalisabilité**
Faisons la somme des dimensions des sous-espaces propres :
$$\dim(E_1) + \dim(E_{-1}) = \frac{n^2 + n}{2} + \frac{n^2 - n}{2} = \frac{2n^2}{2} = n^2$$
Or la dimension de l'espace total $E = \mathcal{M}_n(\mathbb{R})$ est exactement $n^2$.
Puisque la somme des dimensions des sous-espaces propres est égale à la dimension de l'espace global, l'espace $E$ est la somme directe de ces sous-espaces propres : $E = \mathcal{S}_n(\mathbb{R}) \oplus \mathcal{A}_n(\mathbb{R})$.
L'endomorphisme $\phi$ possède donc une base complète de vecteurs propres, il est **diagonalisable**.
