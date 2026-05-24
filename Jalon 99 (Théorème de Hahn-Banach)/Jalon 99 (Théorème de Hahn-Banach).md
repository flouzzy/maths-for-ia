---
uuid: "jalon-99"
title: "Théorème de Hahn-Banach (forme géométrique)"
year: 3
trimester: 9
tags:
  - math/analyse
  - ia/optimisation
prev: "[[Jalon 98 (Théorème de Hahn-Banach (forme analytique)).md]]"
next: "[[Jalon 100 (Démonstration du théorème de Banach-Steinhaus).md]]"
---

# Jalon 99 : Théorème de Hahn-Banach (forme géométrique)

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez deux nuages de fumée (des ensembles convexes) qui flottent dans une pièce. Tant que les deux nuages ne s'imbriquent pas, vous pouvez toujours glisser une immense plaque de verre plate (un **hyperplan**) entre eux sans toucher aucun des deux nuages.
    - La plaque de verre sépare l'espace en deux : le "côté A" et le "côté B".
    - Le **Théorème de Hahn-Banach** garantit que cette plaque existe toujours, même si la pièce a une infinité de dimensions. C'est l'outil qui permet de tracer des frontières nettes entre deux mondes qui ne se mélangent pas.
- **Le "Pourquoi on a inventé ça" :** Pour formaliser la notion de "séparation". En économie ou en IA, on veut souvent séparer les "bons choix" des "mauvais choix". Les formes géométriques de Hahn-Banach prouvent que l'on peut toujours utiliser des fonctions simples (linéaires) pour faire ce découpage, à condition que les ensembles soient "bombés" (convexes).
- **Visualisation :** Deux patates disjointes dans le plan. On trace une droite qui passe entre les deux. En dimension 3, c'est un plan. En dimension $n$, c'est un hyperplan.

## 2. Formalisation & Rigueur Académique

Soit $E$ un espace vectoriel normé (ou un espace topologique localement convexe).

### A. Séparation au sens large

> **Théorème (Hahn-Banach - 1ère forme géométrique) :**
> Soient $A$ et $B$ deux ensembles **convexes** non vides et **disjoints** de $E$.
> Si $A$ est **ouvert**, alors il existe une forme linéaire continue $L \in E^*$ non nulle et un réel $\alpha$ tels que :
> $$\forall a \in A, \forall b \in B, \quad L(a) < \alpha \le L(b)$$
> On dit que l'hyperplan $\{ x \mid L(x) = \alpha \}$ sépare $A$ et $B$ au sens large.

### B. Séparation stricte

> **Théorème (Hahn-Banach - 2ème forme géométrique) :**
> Soient $A$ et $B$ deux ensembles **convexes** non vides et **disjoints**.
> Si $A$ est **fermé** et $B$ est **compact**, alors il existe $L \in E^*$ et deux réels $\alpha, \epsilon > 0$ tels que :
> $$\forall a \in A, \forall b \in B, \quad L(a) \le \alpha - \epsilon < \alpha + \epsilon \le L(b)$$
> Ici, il existe une "marge de sécurité" entre les deux ensembles et l'hyperplan.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Lien avec la forme analytique : La Jauge de Minkowski

Pour prouver la forme géométrique, on transforme un ensemble convexe en une fonction sous-linéaire.

1. **La Jauge :** Soit $C$ un convexe ouvert contenant 0. On définit la jauge de $C$ par :
   $$j_C(x) = \inf \{ t > 0 \mid x/t \in C \}$$
2. **Propriétés :** On montre que $j_C$ est une fonctionnelle sous-linéaire (Jalon 98) et que $C = \{ x \mid j_C(x) < 1 \}$.
3. **Application de Hahn-Banach analytique :**
   - On définit une forme linéaire sur un petit espace (ex: une droite passant par un point hors de $C$).
   - On l'étend à tout l'espace en restant sous la jauge $j_C$.
4. **Conclusion :** La forme linéaire obtenue $L$ vérifiera $L(x) < 1$ pour tout $x \in C$. L'ensemble $\{ x \mid L(x) = 1 \}$ est l'hyperplan cherché.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Séparation d'un point et d'un fermé
**Énoncé :** Soit $C$ un convexe fermé et $x_0 \notin C$. Montrer qu'on peut séparer strictement $x_0$ de $C$.
**Correction Détaillée :**
1. $\{x_0\}$ est un ensemble compact (car fini).
2. $C$ est un ensemble fermé.
3. Les deux sont disjoints et convexes.
4. Par la 2ème forme géométrique de Hahn-Banach, il existe un hyperplan séparateur strict.
**Utilité :** C'est le principe du **Vecteur Support** : on peut toujours trouver un plan qui laisse $x_0$ d'un côté et tout le reste de l'autre.

### Exercice 2 : Niveau Avancé (Théorème du point fixe de Kakutani)
**Énoncé :** Pourquoi la convexité est-elle indispensable ?
**Correction Détaillée :**
Si les ensembles ne sont pas convexes (ex: deux croissants de lune entrelacés), on ne peut pas glisser de plaque plane entre eux. On pourrait avoir besoin d'une surface courbe. Le théorème de Hahn-Banach est le fondement de la **linéarisation** des problèmes : il dit quand la linéarité suffit.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Le succès des **Support Vector Machines (SVM)** repose entièrement sur ce jalon. Trouver la "marge maximale" est exactement ce que décrit la 2ème forme géométrique.
- **Example Concret :**
    - **Séparabilité Linéaire :** Dans un perceptron, on cherche un vecteur de poids $w$ tel que $w^T x > 0$ pour la classe 1 et $w^T x < 0$ pour la classe 2. Hahn-Banach garantit que si les enveloppes convexes des deux classes ne se touchent pas, un tel $w$ existe.
    - **Dualité forte en Deep Learning :** Pour analyser les paysages de perte, on regarde si un minimum local est "séparable" des autres par un hyperplan dans l'espace des fonctions. Cela aide à comprendre la géométrie des réseaux de neurones.
    - **Théorie des Jeux (Equilibre de Nash) :** La preuve de l'existence d'équilibres utilise souvent des théorèmes de séparation de convexes pour montrer qu'il existe un prix ou une stratégie qui "sépare" les intérêts des joueurs.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 98 (Théorème de Hahn-Banach (forme analytique)).md]], [[Jalon 121 (Ensembles convexes).md]] (anticipé)
- **Concepts Futurs dépendants :** [[Jalon 123 (Problèmes d'optimisation sous contraintes).md]], [[Jalon 124 (Conditions de Karush-Kuhn-Tucker).md]]
