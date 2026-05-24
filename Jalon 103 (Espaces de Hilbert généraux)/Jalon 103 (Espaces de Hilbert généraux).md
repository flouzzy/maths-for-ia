---
uuid: "jalon-103"
title: "Espaces de Hilbert généraux"
year: 3
trimester: 9
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 102 (Topologies faibles et faibles-*).md]]"
next: "[[Jalon 104 (Bases hilbertiennes).md]]"
---

# Jalon 103 : Espaces de Hilbert généraux

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez que vous soyez dans une pièce avec un miroir magique.
    - Pour chaque point de la pièce (un vecteur), le miroir vous montre une manière de regarder la pièce (une forme linéaire).
    - L'**Espace de Hilbert**, c'est une pièce où la géométrie est parfaite : on peut mesurer des distances, des angles, et faire des projections (trouver l'ombre d'un objet sur le sol).
    - Le **Théorème de Représentation de Riesz**, c'est le miroir lui-même : il dit que n'importe quel "regard" ou "mesure" que vous portez sur l'espace peut en fait être résumé par un seul vecteur caché dans la pièce. Si vous voulez multiplier un nombre par 2, c'est comme faire un produit scalaire avec un vecteur de longueur 2. Tout ce qui est abstrait (les formes linéaires) devient concret (des vecteurs).
- **Le "Pourquoi on a inventé ça" :** Pour unifier l'algèbre et l'analyse. En dimension finie, on sait tout projeter. En dimension infinie, c'est beaucoup plus dur. Les espaces de Hilbert sont les seuls espaces de dimension infinie où l'on garde toutes nos intuitions géométriques (perpendicularité, plus court chemin).
- **Visualisation :** Une lampe qui projette l'ombre d'un objet sur un mur. Dans un Hilbert, l'ombre (la projection) est unique et c'est le point du mur le plus proche de l'objet.

## 2. Formalisation & Rigueur Académique

Soit $H$ un espace vectoriel complexe.

### A. Produit Scalaire et Hilbert

> **Définition 1 (Produit Scalaire) :**
> On appelle produit scalaire une forme hermitienne définie positive $\langle \cdot, \cdot \rangle : H \times H \to \mathbb{C}$. Elle induit une norme $\|x\| = \sqrt{\langle x, x \rangle}$.

> **Définition 2 (Espace de Hilbert) :**
> Un espace de Hilbert est un espace muni d'un produit scalaire qui est **complet** pour la norme associée.

### B. Théorème de Projection

> **Théorème (Projection sur un convexe fermé) :**
> Soit $C$ un ensemble convexe fermé non vide de $H$. Pour tout $x \in H$, il existe un unique $p \in C$ tel que :
> $$\|x - p\| = \inf_{y \in C} \|x - y\|$$
> Ce point $p$ est appelé la **projection de $x$ sur $C$**.

### C. Théorème de Représentation de Riesz

C'est l'un des résultats les plus profonds de l'analyse fonctionnelle.

> **Théorème de Riesz :**
> Pour toute forme linéaire continue $L \in H^*$, il existe un **unique** vecteur $a \in H$ tel que :
> $$\forall x \in H, \quad L(x) = \langle x, a \rangle$$
> De plus, on a l'égalité des normes : $\|L\|_{H^*} = \|a\|_H$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration du Théorème de Riesz

1. **Existence :** Si $L = 0$, alors $a = 0$ convient. Supposons $L \neq 0$.
2. **Noyau de L :** Soit $M = \ker(L)$. Comme $L$ est continue, $M$ est un sous-espace vectoriel fermé de $H$.
3. **Orthogonal de M :** Comme $L \neq 0$, $M \neq H$. Il existe donc un vecteur $z \in M^\perp$ non nul (d'après le théorème de projection sur un sous-espace).
4. **Candidat pour a :** On cherche $a = \alpha z$. On veut $L(x) = \langle x, \alpha z \rangle = \bar{\alpha} \langle x, z \rangle$.
5. **Calcul de $\alpha$ :** On remarque que pour tout $x$, le vecteur $v = L(x)z - L(z)x$ appartient au noyau $M$ car $L(v) = L(x)L(z) - L(z)L(x) = 0$.
6. **Utilisation de l'orthogonalité :** Comme $z \perp M$, on a $\langle v, z \rangle = 0$.
   $\langle L(x)z - L(z)x, z \rangle = 0 \implies L(x) \|z\|^2 - L(z) \langle x, z \rangle = 0$.
   $L(x) = \langle x, \frac{\overline{L(z)}}{\|z\|^2} z \rangle$.
7. **Conclusion :** Le vecteur $a = \frac{\overline{L(z)}}{\|z\|^2} z$ convient.
8. **Unicité :** Si $\langle x, a \rangle = \langle x, b \rangle$ pour tout $x$, alors $\langle x, a-b \rangle = 0$, donc $a-b=0$.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Évaluation ponctuelle
**Énoncé :** Soit $H = L^2([0, 1])$. Existe-t-il un vecteur $a \in H$ tel que $\int_0^1 f(x) a(x) dx = f(0)$ pour tout $f$ continue ?
**Correction Détaillée :**
Non. L'application $L(f) = f(0)$ n'est pas continue sur $L^2$. On peut trouver des fonctions dont l'intégrale du carré est minuscule mais qui valent 1 en 0 (ex: pics très fins). Comme $L$ n'est pas continue, le théorème de Riesz ne s'applique pas. Cela montre qu'il n'existe pas de "fonction" de Dirac dans $L^2$.

### Exercice 2 : Niveau Avancé (RKHS)
**Énoncé :** Dans un espace de Hilbert de fonctions, si l'évaluation $f \mapsto f(x)$ est continue pour tout $x$, on dit que c'est un **RKHS**. Montrer qu'il existe une fonction $k_x$ telle que $f(x) = \langle f, k_x \rangle$.
**Correction Détaillée :**
C'est une application immédiate du théorème de Riesz. La fonction $k(x, y) = \langle k_y, k_x \rangle$ est appelée le **Noyau Reproduisant**. Toute la théorie des SVM et des processus gaussiens découle de l'existence de ces vecteurs $k_x$.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Les espaces de Hilbert sont le terrain de jeu du **Machine Learning à noyaux** (Kernel Methods). Le théorème de Riesz est ce qui permet de transformer une opération de comparaison (le noyau) en un simple produit scalaire.
- **Example Concret :**
    - **Support Vector Machines (SVM) :** L'hyperplan séparateur optimal est un vecteur dans un espace de Hilbert. Le théorème de Riesz garantit que ce vecteur existe et qu'il peut être exprimé comme une combinaison linéaire des données d'entraînement (Théorème du Représentant, Jalon 127).
    - **Calcul du Gradient :** En optimisation, le gradient $\nabla f$ est défini comme le vecteur qui représente la différentielle $df$ via le théorème de Riesz. Sans Hilbert, la notion de gradient n'existerait pas de manière géométrique.
    - **Quantum Machine Learning :** Les états d'un ordinateur quantique sont des vecteurs dans un espace de Hilbert complexe. Les algorithmes d'IA quantique utilisent les propriétés de projection et de Riesz pour manipuler l'information.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L2).md]], [[Jalon 101 (Application ouverte et Graphe fermé).md]]
- **Concepts Futurs dépendants :** [[Jalon 105 (Opérateurs adjoints).md]], [[Jalon 126 (Noyaux définis positifs).md]]
