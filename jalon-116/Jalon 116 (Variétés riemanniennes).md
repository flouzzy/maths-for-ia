---
uuid: "jalon-116"
title: "Variétés riemanniennes"
year: 3
trimester: 10
tags:
  - math/geometrie
  - ia/abstraction
prev: "[[Jalon 115 (Démonstration du théorème de Stokes généralisé).md]]"
next: "[[Jalon 117 (Calcul des variations).md]]"
---

# Jalon 116 : Variétés riemanniennes

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous marchiez sur un trampoline géant.
    - À certains endroits, le tissu est très tendu (distance courte), à d'autres il est très lâche ou étiré (distance longue).
    - Pour mesurer votre trajet, vous ne pouvez pas utiliser une règle rigide. Vous avez besoin d'une règle souple qui s'adapte à la tension du tissu à chaque pas. Cette règle locale s'appelle la **Métrique de Riemann**.
    - Si vous voulez aller d'un point A à un point B le plus vite possible, vous n'allez pas forcément suivre une ligne droite visuelle : vous allez suivre la courbe qui demande le moins d'effort (le chemin le plus court sur le tissu). Ce chemin s'appelle une **Géodésique**. C'est la "ligne droite" du monde courbe.
- **Le "Pourquoi on a inventé ça" :** Pour pouvoir faire de la vraie géométrie (distances, angles, volumes) sur des objets qui ne sont pas plats. C'est le cadre de la théorie d'Einstein (la gravité courbe l'espace) et de l'IA géométrique (les données forment des variétés courbes).
- **Visualisation :** La surface de la Terre. Le chemin le plus court entre Paris et Tokyo est un "grand cercle" (une géodésique). Vue sur une carte plate, cette ligne semble courbe, mais sur le globe, c'est la trajectoire la plus directe.

## 2. Formalisation & Rigueur Académique

Soit $M$ une variété différentielle.

### A. Le Tenseur Métrique

> **Définition 1 (Métrique Riemannienne) :**
> Une métrique riemannienne $g$ sur $M$ est la donnée, en chaque point $p \in M$, d'un produit scalaire $g_p$ sur l'espace tangent $T_p M$, tel que $p \mapsto g_p$ soit lisse.
> Dans une carte locale, on le note par ses composantes $g_{ij}(x) = g_x(\frac{\partial}{\partial x_i}, \frac{\partial}{\partial x_j})$.

### B. Longueur et Distance

> **Définition 2 (Longueur d'une courbe) :**
> La longueur d'une courbe $\gamma : [a, b] \to M$ est :
> $$L(\gamma) = \int_a^b \sqrt{g_{\gamma(t)}(\gamma'(t), \gamma'(t))} dt$$
> La distance riemannienne $d(p, q)$ est l'infimum des longueurs des courbes reliant $p$ à $q$.

### C. Géodésiques

Une géodésique est une courbe de "vitesse constante" qui ne tourne pas par rapport à la surface.

> **Équation des géodésiques :**
> Dans une carte locale, une courbe $\gamma(t)$ est une géodésique si elle vérifie :
> $$\frac{d^2 \gamma^k}{dt^2} + \sum_{i,j} \Gamma^k_{ij} \frac{d\gamma^i}{dt} \frac{d\gamma^j}{dt} = 0$$
> où $\Gamma^k_{ij}$ sont les **symboles de Christoffel**, calculés à partir des dérivées de la métrique $g_{ij}$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Lien entre distance et géodésique (Intuition)

On veut minimiser l'énergie $E(\gamma) = \frac{1}{2} \int \|\gamma'(t)\|^2 dt$.

1. **Calcul des variations :** On considère une petite perturbation de la courbe $\gamma_\epsilon = \gamma + \epsilon h$.
2. **Dérivée de l'énergie :** On cherche $\gamma$ telle que $\frac{dE}{d\epsilon}|_{\epsilon=0} = 0$.
3. **Développement :**
   $\delta E = \int g_{ij} \gamma'^i h'^j + \frac{1}{2} \partial_k g_{ij} \gamma'^i \gamma'^j h^k$.
4. **IPP sur le premier terme :** On fait passer la dérivée de $h'$ vers les autres termes.
5. **Équations d'Euler-Lagrange :** On obtient un système d'équations qui est exactement l'équation des géodésiques mentionnée plus haut.
6. **Conclusion :** Les chemins de longueur minimale sont nécessairement des géodésiques. C'est l'équivalent du principe de moindre action en physique.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : La métrique de la sphère
**Énoncé :** Sur la sphère $S^2$ de rayon $R$, en coordonnées $(\theta, \phi)$, la métrique est $ds^2 = R^2 d\theta^2 + R^2 \sin^2 \theta d\phi^2$. Calculer la longueur du cercle équatorial.
**Correction Détaillée :**
1. Équateur : $\theta = \pi/2$ (constant), donc $d\theta = 0$.
2. $\phi$ varie de $0$ à $2\pi$.
3. $ds = \sqrt{0 + R^2 \sin^2(\pi/2) d\phi^2} = R d\phi$.
4. $L = \int_0^{2\pi} R d\phi = 2\pi R$.
**Résultat :** Cohérent avec la géométrie classique.

### Exercice 2 : Niveau Avancé (Courbure et Transport Parallèle)
**Énoncé :** Pourquoi, si on transporte un vecteur le long d'un triangle sur une sphère, ne revient-il pas dans sa direction initiale ?
**Correction Détaillée :**
C'est le phénomène d'holonomie. La courbure de la variété empêche les espaces tangents d'être "parallèles" de manière globale. L'angle de décalage est proportionnel à l'intégrale de la courbure de Gauss sur la surface du triangle (Théorème de Gauss-Bonnet).

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** L'**Information Geometry** voit l'ensemble des paramètres d'un modèle comme une variété riemannienne. La métrique utilisée est la **Matrice d'Information de Fisher**.
- **Example Concret :**
    - **Natural Gradient Descent :** Au lieu de mettre à jour les poids par $\theta \leftarrow \theta - \eta \nabla L$ (Euclidien), on utilise $\theta \leftarrow \theta - \eta I(\theta)^{-1} \nabla L$ (Riemannien). Cela garantit que le pas de l'IA a la même "taille" en termes de changement de comportement du modèle, quelle que soit la courbure de l'espace des paramètres.
    - **Diffusion sur Variétés :** Pour générer des données qui respectent des contraintes (ex: des protéines), on définit un processus de diffusion dont le bruit suit les géodésiques de la variété des contraintes.
    - **Hyperbolic Embeddings :** Pour représenter des hiérarchies (arbres, graphes sociaux), on utilise des variétés à courbure négative (Espace Hyperbolique). La géométrie riemannienne y permet de placer une infinité de points "loin" les uns des autres tout en restant dans un espace de petite dimension.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 113 (Tenseurs et Formes différentielles).md]], [[Jalon 109 (Topologie des sous-variétés de Rn).md]]
- **Concepts Futurs dépendants :** [[Jalon 117 (Calcul des variations).md]], [[Jalon 143 (Théorie spectrale des graphes).md]]
