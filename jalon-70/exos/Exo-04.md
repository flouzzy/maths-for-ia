# Exercice 4 : Mesure produit mixte (Continue-Discrète) (★★★☆☆)

**Énoncé :**
Soit $X = [0,1]$ muni de la mesure de Lebesgue $\lambda$ et $Y = \{1, 2, 3\}$ muni de la mesure de comptage $\delta$.
Soit $\pi = \lambda \otimes \delta$ la mesure produit sur $X \times Y$.
Soit l'ensemble $E = \{(x, y) \in X \times Y \mid y \leq 2x\}$.
1. Dessiner ou décrire les sections de $E$ selon la variable $y$.
2. Calculer la mesure de $E$ en intégrant par rapport aux sections en $y$.
3. Calculer la mesure de $E$ en intégrant par rapport aux sections en $x$. Vérifier que les résultats coïncident.

**Correction :**
1. $E$ est un sous-ensemble de $[0,1] \times \{1,2,3\}$.
   Les sections en $y$ (pour $y \in \{1,2,3\}$) sont $E^y = \{x \in [0,1] \mid y \leq 2x\} = \{x \in [0,1] \mid x \geq y/2\}$.
   - Pour $y = 1$, $E^1 = [\frac{1}{2}, 1]$.
   - Pour $y = 2$, $E^2 = [1, 1] = \{1\}$.
   - Pour $y = 3$, $E^3 = \emptyset$ (car $x$ devrait être $\geq 1.5$, or $x \leq 1$).
2. Intégration selon $y$ :
   $\pi(E) = \int_Y \lambda(E^y) \, d\delta(y) = \sum_{y \in \{1,2,3\}} \lambda(E^y)$.
   $\lambda(E^1) = 1 - 0.5 = 0.5$.
   $\lambda(E^2) = \lambda(\{1\}) = 0$.
   $\lambda(E^3) = \lambda(\emptyset) = 0$.
   Donc $\pi(E) = 0.5 + 0 + 0 = 0.5$.
3. Intégration selon $x$ :
   Fixons $x \in [0,1]$. La section $E_x = \{y \in \{1,2,3\} \mid y \leq 2x\}$.
   Sa mesure de comptage $\delta(E_x)$ est le nombre d'entiers dans $\{1,2,3\}$ inférieurs ou égaux à $2x$.
   - Si $0 \leq x < 1/2$, alors $2x < 1$, donc aucun entier n'est admissible : $E_x = \emptyset$, $\delta(E_x) = 0$.
   - Si $1/2 \leq x < 1$, alors $1 \leq 2x < 2$, le seul entier est $y=1$ : $E_x = \{1\}$, $\delta(E_x) = 1$.
   - Si $x = 1$, alors $2x = 2$, les entiers sont $y=1, 2$ : $E_1 = \{1,2\}$, $\delta(E_x) = 2$.
   L'intégrale vaut :
   $\pi(E) = \int_0^1 \delta(E_x) \, d\lambda(x) = \int_0^{1/2} 0 \, dx + \int_{1/2}^1 1 \, dx$ (la valeur ponctuelle en $x=1$ ne change pas l'intégrale).
   $\pi(E) = [x]_{1/2}^1 = 1 - 0.5 = 0.5$.
   Les résultats sont bien identiques. L'espace produit mesure 0.5.
