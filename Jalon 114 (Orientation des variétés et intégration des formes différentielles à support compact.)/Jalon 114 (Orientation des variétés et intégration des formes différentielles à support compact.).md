---
uuid: "jalon-114"
title: "Orientation et Intégration sur variétés"
year: 3
trimester: 10
tags:
  - math/geometrie
  - ia/abstraction
prev: "[[Jalon 113 (Tenseurs et Formes différentielles).md]]"
next: "[[Jalon 115 (Démonstration du théorème de Stokes généralisé).md]]"
---

# Jalon 114 : Orientation et Intégration sur variétés

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :**
    - **L'Orientation :** Imaginez que vous peigniez un ruban. Pour que le travail soit propre, vous devez décider quel côté est le "dessus" et quel côté est le "dessous". Si vous pouvez faire tout le tour du ruban et revenir au point de départ en restant toujours sur le "dessus", le ruban est **orientable**. (Le ruban de Möbius, lui, ne l'est pas : on finit par se retrouver la tête en bas sans s'en rendre compte !).
    - **L'Intégration :** Vous voulez calculer la quantité totale de peinture utilisée sur une sphère géante. Comme vous n'avez que des petits pinceaux plats, vous peignez morceau par morceau (chaque morceau est une **carte locale**).
    - **La Partition de l'Unité :** C'est l'astuce pour ne pas peindre deux fois le même endroit là où les morceaux se chevauchent. On utilise un "dosage" qui s'estompe aux bords pour que la somme des dosages sur chaque point soit toujours égale à 1.
- **Le "Pourquoi on a inventé ça" :** Pour calculer des masses, des flux d'énergie ou des probabilités sur des mondes courbes. Sans orientation, on ne pourrait pas définir de "flux" (on ne saurait pas si l'énergie entre ou sort). Sans intégration, on ne pourrait pas définir de "moyenne" sur une variété.
- **Visualisation :** Une sphère recouverte de petits patchs colorés qui se fondent les uns dans les autres.

## 2. Formalisation & Rigueur Académique

Soit $M$ une variété différentielle de dimension $n$.

### A. Orientation

> **Définition 1 (Variété Orientable) :**
> $M$ est dite **orientable** s'il existe un atlas dont tous les changements de cartes $\psi_{ij} = \phi_j \circ \phi_i^{-1}$ ont un jacobien strictement positif :
> $$\det(J_{\psi_{ij}}) > 0$$
> Une **orientation** est le choix d'un tel atlas (maximal).

### B. Intégration d'une n-forme

Soit $\omega$ une $n$-forme différentielle sur $M$ à support compact.

1. **Dans une carte $(U, \phi)$ :** Si le support de $\omega$ est inclus dans $U$, on définit :
   $$\int_M \omega = \int_{\phi(U)} f(x) dx_1 \dots dx_n$$
   où $f$ est la fonction telle que $\phi^* (f dx_1 \wedge \dots \wedge dx_n) = \omega$.
2. **Globalement (Partition de l'unité) :** Soit $(\rho_i)$ une famille de fonctions lisses telles que $\sum \rho_i = 1$ et chaque $\rho_i$ a un support dans une carte $U_i$. On définit :
   $$\int_M \omega = \sum_i \int_M \rho_i \omega$$

### C. Propriétés Fondamentales

> **Théorème :** L'intégrale est bien définie, c'est-à-dire qu'elle ne dépend ni de l'atlas orienté choisi, ni de la partition de l'unité utilisée.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Indépendance du changement de carte

Soient deux cartes $(U, \phi)$ and $(V, \psi)$ recouvrant le support de $\omega$. Notons $h = \psi \circ \phi^{-1}$ le changement de coordonnées.

1. **Expression dans la première carte :** $\omega$ s'écrit $\omega = f dx_1 \wedge \dots \wedge dx_n$.
2. **Expression dans la seconde carte :** $\omega$ s'écrit $\omega = g dy_1 \wedge \dots \wedge dy_n$.
3. **Lien entre les deux :** Par la formule du changement de variable pour les formes différentielles :
   $f = (g \circ h) \cdot \det(J_h)$.
4. **Calcul de l'intégrale :**
   $\int_{\phi(U)} f(x) d^n x = \int_{\phi(U)} g(h(x)) \det(J_h(x)) d^n x$.
5. **Utilisation de la formule de Riemann :** D'après le théorème du changement de variable dans $\mathbb{R}^n$ (Jalon 46) :
   $$\int_{\psi(V)} g(y) d^n y = \int_{\phi(U)} g(h(x)) |\det(J_h(x))| d^n x$$
6. **Conclusion :** Comme l'atlas est orienté, $\det(J_h) > 0$, donc $|\det(J_h)| = \det(J_h)$. Les deux calculs donnent le même résultat. L'orientation est donc la condition sine qua non pour que l'intégration ait un sens global.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Aire de la sphère $S^2$
**Énoncé :** Calculer l'intégrale de la forme volume $\omega = \sin \theta d\theta \wedge d\phi$ sur la sphère unité (en coordonnées sphériques).
**Correction Détaillée :**
1. Le domaine est $\theta \in [0, \pi]$ and $\phi \in [0, 2\pi]$.
2. $\int_{S^2} \omega = \int_0^{2\pi} \int_0^\pi \sin \theta d\theta d\phi$.
3. $\int_0^\pi \sin \theta d\theta = [-\cos \theta]_0^\pi = 1 - (-1) = 2$.
4. $\int_0^{2\pi} 2 d\phi = 4\pi$.
**Résultat :** On retrouve bien la surface de la sphère $4\pi r^2$ avec $r=1$.

### Exercice 2 : Niveau Avancé (Ruban de Möbius)
**Énoncé :** Pourquoi ne peut-on pas intégrer une 2-forme de manière cohérente sur un ruban de Möbius ?
**Correction Détaillée :**
Si on essaie de définir une forme volume partout non nulle, on s'aperçoit qu'en faisant un tour, le signe du Jacobien change obligatoirement à cause de la torsion. On ne peut pas trouver d'atlas orienté. L'intégrale dépendrait du "sens" dans lequel on a décidé de commencer le calcul, ce qui est mathématiquement inacceptable.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, pour calculer la **Perte de Reconstruction** sur une variété (ex: dans un Auto-encodeur géométrique), on doit intégrer l'erreur sur toute la surface des données.
- **Example Concret :**
    - **Manifold Sampling (MCMC) :** Pour générer des échantillons réalistes sur une variété (ex: des molécules stables), on utilise des algorithmes (HMC) qui simulent une particule se déplaçant sur la variété. La probabilité de trouver la particule dans une zone dépend de l'intégrale de la mesure de Gibbs sur cette zone.
    - **Normalisation sur Variété :** Dans les réseaux de neurones pour la vision 360° (sphérique), on doit normaliser les activations. Pour cela, on calcule l'espérance et la variance en intégrant les signaux sur la sphère $S^2$ en utilisant les outils de ce jalon.
    - **Information Geometry :** On voit l'espace des modèles $\theta$ comme une variété (la variété de Fisher). La distance entre deux modèles est une intégrale sur cette variété.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 113 (Tenseurs et Formes différentielles).md]], [[Jalon 110 (Variétés différentielles abstraites).md]]
- **Concepts Futurs dépendants :** [[Jalon 115 (Démonstration du théorème de Stokes généralisé).md]], [[Jalon 116 (Variétés riemanniennes).md]]
