---
uuid: "jalon-118"
title: "Optimalité et Multiplicateurs de Lagrange (Master)"
year: 3
trimester: 10
tags:
  - math/analyse
  - ia/optimisation
prev: "[[Jalon 117 (Calcul des variations).md]]"
next: "[[Jalon 119 (Connexions avec les groupes de Lie).md]]"
---

# Jalon 118 : Optimalité et Multiplicateurs de Lagrange (Master)

## 1. Présentation du concept clé

- **La Métaphore :**
    - **Le second ordre :** Imaginez que vous ayez trouvé le point le plus bas d'un drap (le minimum). Pour être sûr que c'est un vrai creux (et pas un sommet plat), vous appuyez dessus avec votre doigt. Si le drap résiste et revient à sa place, c'est que la "courbure" est bonne. C'est l'**optimalité du second ordre**.
    - **Lagrange en dimension infinie :** Imaginez que vous deviez tracer le chemin le plus court entre deux points, mais avec une règle supplémentaire : le chemin doit passer par une ville précise ou avoir une certaine "aire" en dessous (une **contrainte**). Le **Multiplicateur de Lagrange**, c'est comme une amende que vous payez chaque fois que vous vous éloignez de la règle. Pour minimiser vos dépenses totales (coût du chemin + amendes), vous allez naturellement trouver le chemin qui respecte la règle tout en étant le plus court possible.
- **Le "Pourquoi on a inventé ça" :** Pour résoudre des problèmes d'optimisation complexes où l'on ne peut pas simplement bouger librement. En ingénierie, on veut minimiser le poids d'un pont mais il **doit** supporter une charge. En IA, on veut minimiser l'erreur mais le modèle **doit** rester simple ou respecter des lois d'éthique.
- **Visualisation :** Une surface courbe avec une ligne tracée dessus. On cherche le point le plus bas de la surface mais en restant obligatoirement sur la ligne.

## 2. Formalisation

### A. Seconde Variation et Condition de Legendre

Soit $J(y) = \int_{x_1}^{x_2} L(x, y, y') dx$ une fonctionnelle.

> **Définition 1 (Seconde Variation) :**
> Si $y$ est un point stationnaire ($\delta J = 0$), la seconde variation dans la direction $h$ est :
> $$\delta^2 J(y, h) = \int_{x_1}^{x_2} \left( \frac{\partial^2 L}{\partial y^2} h^2 + 2\frac{\partial^2 L}{\partial y \partial y'} h h' + \frac{\partial^2 L}{\partial y'^2} (h')^2 \right) dx$$

> **Théorème (Condition de Legendre) :**
> Pour que $y$ soit un minimum local de $J$, il est nécessaire que la courbure par rapport à la pente soit positive partout :
> $$\forall x \in [x_1, x_2], \quad \frac{\partial^2 L}{\partial y'^2}(x, y(x), y'(x)) \ge 0$$

### B. Multiplicateurs de Lagrange (Dimension infinie)

On veut minimiser $J(y)$ sous la contrainte fonctionnelle $G(y) = 0$.

> **Théorème :** Soit $E$ un espace de Banach. Soient $J, G : E \to \mathbb{R}$ deux fonctionnelles de classe $\mathcal{C}^1$. Si $y$ est un extremum local de $J$ restreint à $\{ y \mid G(y)=0 \}$, et si $G'(y) \neq 0$, alors il existe un réel $\lambda$ (le multiplicateur) tel que :
> $$\delta J(y) + \lambda \delta G(y) = 0$$
> Cela revient à chercher les points stationnaires du **Lagrangien** $\mathcal{L}(y, \lambda) = J(y) + \lambda G(y)$.

## 3. Démonstrations

### Démonstration : Condition d'optimalité avec contrainte intégrale

Cherchons à minimiser $J(y) = \int_{x_1}^{x_2} f(x, y, y') dx$ sous la contrainte $K(y) = \int_{x_1}^{x_2} g(x, y, y') dx = C$.

1. **Construction du Lagrangien :** On définit $L^* = f + \lambda g$.
2. **Variation totale :** Soit $h$ une variation. On veut que pour l'optimal $y$, tout changement $\delta y = \epsilon h$ préserve la contrainte au premier ordre.
3. **Équation d'Euler-Lagrange modifiée :** En appliquant le résultat du Jalon 117 au nouveau lagrangien $L^*$, on obtient :
   $$\left( \frac{\partial f}{\partial y} + \lambda \frac{\partial g}{\partial y} \right) - \frac{d}{dx} \left( \frac{\partial f}{\partial y'} + \lambda \frac{\partial g}{\partial y'} \right) = 0$$
4. **Conclusion :** Pour résoudre le problème, on résout cette EDO (qui dépend de $\lambda$), puis on utilise la valeur de la contrainte $K(y)=C$ pour trouver la valeur précise du paramètre $\lambda$.

## 4. Exercices d'Application

### Exercice 1 : La chaînette (Problème isopérimétrique)
**Énoncé :** Une corde de longueur $L$ fixée à ses extrémités pend sous son propre poids. Quelle forme prend-elle ?
**Correction Détaillée :**
1. **Énergie potentielle :** $J(y) = \int \rho g y \sqrt{1 + y'^2} dx$ (à minimiser).
2. **Contrainte :** $\int \sqrt{1 + y'^2} dx = L$ (longueur fixe).
3. **Lagrangien :** $L^* = (y + \lambda) \sqrt{1 + y'^2}$.
4. **Résolution :** L'équation d'Euler-Lagrange mène à une solution de la forme $y(x) = a \cosh(\frac{x-b}{a}) - \lambda$.
**Résultat :** La forme est un cosinus hyperbolique, appelé "Chaînette".

### Exercice 2 : Niveau Avancé (Inégalité de Poincaré)
**Énoncé :** Trouver la plus petite constante $\lambda$ telle que $\int_0^1 y^2 dx \le \lambda \int_0^1 (y')^2 dx$ pour $y(0)=y(1)=0$.
**Correction Détaillée :**
C'est un problème d'optimalité du second ordre. On cherche le minimum de $\int (y')^2$ sous la contrainte $\int y^2 = 1$. Le multiplicateur de Lagrange mène à l'équation des ondes $y'' + \frac{1}{\lambda} y = 0$. La plus petite valeur propre donne $\lambda = 1/\pi^2$.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, nous utilisons les multiplicateurs de Lagrange pour l'**Apprentissage sous contraintes** (Constrained Learning).
- **Example Concret :**
    - **Régularisation parcimonieuse (Lasso) :** On minimise l'erreur sous la contrainte que la norme des poids soit petite ($\|w\|_1 \le C$). L'algorithme utilise le multiplicateur de Lagrange pour transformer cette contrainte en un terme de pénalité dans la perte.
    - **Fairness in AI :** On veut minimiser la perte tout en imposant une contrainte d'équité (ex: $P(\hat{Y}=1 | Group=A) = P(\hat{Y}=1 | Group=B)$). C'est une optimisation fonctionnelle avec contrainte résolue par les outils de ce jalon.
    - **Physics-Informed Neural Networks (PINNs) :** On minimise l'erreur sur les données sous la contrainte que le réseau satisfasse une équation de physique (ex: Navier-Stokes). On traite cette contrainte par des multiplicateurs de Lagrange de dimension infinie.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 117 (Calcul des variations).md]], [[Jalon 123 (Problèmes d'optimisation sous contraintes).md]] (anticipé)
- **Concepts Futurs dépendants :** [[Jalon 124 (Conditions de Karush-Kuhn-Tucker).md]], [[Jalon 125 (Opérateurs proximaux).md]]
