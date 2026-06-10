---
uuid: "jalon-128"
title: "Flots de gradient"
year: 3
trimester: 11
tags:
  - math/analyse
  - ia/optimisation
prev: "[[Jalon 127 (Théorème du représentant dans les RKHS).md]]"
next: "[[Jalon 129 (Optimisation stochastique).md]]"
---

# Jalon 128 : Flots de gradient

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous posiez une bille au sommet d'une montagne (la fonction de perte $L$).
    - La **Descente de Gradient** classique (Jalon 45), c'est comme si la bille faisait des petits sauts successifs. Si le saut est trop grand, la bille peut rater le trou.
    - Le **Flot de Gradient**, c'est le mouvement parfait et fluide de la bille qui glisse. La bille ne s'arrête jamais, elle suit la ligne de plus grande pente à chaque millième de seconde.
    - C'est l'idéal théorique de l'apprentissage : un mouvement sans saccades qui nous mène directement au creux le plus profond.
- **Le "Pourquoi on a inventé ça" :** Pour comprendre comment les réseaux de neurones apprennent "vraiment". En passant du discret (les pas) au continu (le flot), on peut utiliser les outils de la physique (équations différentielles) pour prouver que l'IA va converger vers une bonne solution, même dans des espaces très complexes.
- **Visualisation :** Un champ de vecteurs (Jalon 112) où toutes les flèches pointent vers le bas de la vallée. Le flot est la trajectoire d'un point qui suit ces flèches.

## 2. Formalisation

Soit $f : \mathbb{R}^n \to \mathbb{R}$ une fonction de classe $\mathcal{C}^1$.

### A. Définition du Flot de Gradient

> **Définition (Flot de gradient) :**
> On appelle flot de gradient associé à $f$ l'équation différentielle du premier ordre :
> $$\dot{x}(t) = \frac{dx}{dt}(t) = -\nabla f(x(t))$$
> Avec une condition initiale $x(0) = x_0$.
> La solution $t \mapsto x(t)$ est la trajectoire de plus grande pente descendante.

### B. Propriétés de Décroissance

> **Théorème :** La fonction objectif $f$ décroît strictement le long des trajectoires non stationnaires.
> $$\frac{d}{dt} f(x(t)) = -\| \nabla f(x(t)) \|^2$$

### C. Convergence vers les points critiques

Si $f$ est convexe et admet un minimum, alors $x(t)$ converge vers un point $x^*$ tel que $\nabla f(x^*) = 0$. En dimension infinie (espaces de Hilbert), on parle de **Flots de gradient métriques**.

## 3. Démonstrations

### Démonstration : La perte diminue toujours le long du flot

1. **Règle de la chaîne :** Calculons la dérivée temporelle de la valeur de la fonction $f$ au point courant $x(t)$.
   $$\frac{d}{dt} [f(x(t))] = \langle \nabla f(x(t)), \dot{x}(t) \rangle$$
2. **Utilisation de l'équation du flot :** Remplaçons $\dot{x}(t)$ par sa définition $-\nabla f(x(t))$.
   $$\frac{d}{dt} f(x(t)) = \langle \nabla f(x(t)), -\nabla f(x(t)) \rangle$$
3. **Produit scalaire :** Par définition du produit scalaire :
   $$\frac{d}{dt} f(x(t)) = - \langle \nabla f(x(t)), \nabla f(x(t)) \rangle = - \| \nabla f(x(t)) \|^2$$
4. **Conclusion :** Comme une norme au carré est toujours positive ou nulle, la dérivée de $f$ par rapport au temps est toujours négative ou nulle.
   - Si $\nabla f \neq 0$, la perte diminue strictement.
   - Si $\nabla f = 0$, la bille est arrêtée (point critique).

## 4. Exercices d'Application

### Exercice 1 : Flot d'une fonction quadratique
**Énoncé :** Résoudre le flot de gradient pour $f(x) = \frac{1}{2} x^T A x$ où $A$ est une matrice symétrique définie positive.
**Correction Détaillée :**
1. **Gradient :** $\nabla f(x) = Ax$.
2. **EDO :** $\dot{x}(t) = -Ax(t)$.
3. **Résolution (Jalon 43) :** $x(t) = e^{-At} x_0$.
4. **Comportement :** Comme $A$ est définie positive, ses valeurs propres $\lambda_i$ sont $>0$. Les composantes du vecteur tendent vers 0 selon des exponentielles $e^{-\lambda_i t}$.
**Résultat :** Le flot converge vers l'origine (le minimum unique) à une vitesse dictée par la plus petite valeur propre de $A$.

### Exercice 2 : Niveau Avancé (Lien avec la descente de gradient)
**Énoncé :** Montrer que la descente de gradient discrète $x_{k+1} = x_k - \eta \nabla f(x_k)$ est une approximation d'Euler du flot de gradient.
**Correction Détaillée :**
L'approximation d'Euler pour $\dot{x} = G(x)$ est $\frac{x(t+\eta) - x(t)}{\eta} = G(x(t))$. En posant $x_k = x(k\eta)$ et $G = -\nabla f$, on retrouve exactement la formule de l'algorithme. Cela prouve que pour un pas $\eta$ très petit, l'algorithme suit la trajectoire "physique" idéale.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** Le passage au continu permet d'utiliser les outils de la **Géométrie Riemannienne** (Jalon 116) pour définir des flots de gradient plus intelligents (Natural Gradient Flow).
- **Example Concret :**
    - **Neural ODEs :** Au lieu d'apprendre des poids, on apprend directement le champ de vecteurs qui définit le flot. L'IA devient un système dynamique continu.
    - **Wasserstein Gradient Flow :** C'est le flot de gradient dans l'espace des mesures de probabilité. Il est utilisé pour prouver que les algorithmes de Langevin (utilisés dans les modèles de diffusion) convergent vers la distribution de données réelle.
    - **Flow Matching :** Une technique moderne pour entraîner des modèles génératifs ultra-rapides en apprenant à faire correspondre le flot du modèle à un flot de gradient idéal reliant le bruit aux données.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 112 (Champs de vecteurs et Crochet de Lie).md]], [[Jalon 45 (Différentiabilité et Gradient).md]]
- **Concepts Futurs dépendants :** [[Jalon 129 (Optimisation stochastique).md]], [[Jalon 130 (Régularisation implicite de la descente de gradient dans les modèles sur-paramétrés.).md]]
