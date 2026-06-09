---
uuid: "jalon-121"
title: "Ensembles et Fonctions convexes"
year: 3
trimester: 11
tags:
  - math/optimisation
  - ia/fondations
prev: "[[Jalon 120 (Livrable IA).md]]"
next: "[[Jalon 122 (Notion de sous-gradient).md]]"
---

# Jalon 121 : Ensembles et Fonctions convexes

## 1. Présentation du concept clé

- **La Métaphore :**
    - Un **Ensemble Convexe**, c'est comme un ballon bien gonflé ou un bloc de pâte à modeler sans aucun trou ni aucune bosse vers l'intérieur. Si vous prenez deux points n'importe où à l'intérieur et que vous tirez un fil entre eux, le fil reste entièrement à l'intérieur.
    - Une **Fonction Convexe**, c'est un bol parfait. Si vous posez une règle sur les bords du bol, la règle passe toujours "au-dessus" du fond du bol.
- **Le "Pourquoi on a inventé ça" :** Pour garantir la réussite de l'optimisation. Dans un monde convexe (un bol), si vous lâchez une bille, elle finira toujours, absolument toujours, au point le plus bas (le minimum global). Il n'y a pas de "faux trous" (minima locaux) pour piéger la bille. C'est le paradis du mathématicien et de l'ingénieur en IA.
- **Visualisation :** L'**Épigraphe**. Imaginez que vous versiez de la peinture dans votre bol. Toute la zone remplie de peinture (au-dessus de la courbe) forme un ensemble solide qui est lui-même convexe.

## 2. Formalisation

Soit $E$ un espace vectoriel réel.

### A. Ensembles Convexes

> **Définition 1 (Ensemble convexe) :**
> Une partie $C \subset E$ est **convexe** si pour tous $x, y \in C$ et tout $\lambda \in [0, 1]$ :
> $$(1-\lambda)x + \lambda y \in C$$
> L'enveloppe convexe d'un ensemble est le plus petit convexe le contenant.

### B. Fonctions Convexes

> **Définition 2 (Fonction convexe) :**
> Soit $C$ un ensemble convexe. Une application $f : C \to \mathbb{R}$ est **convexe** si pour tous $x, y \in C$ et tout $\lambda \in [0, 1]$ :
> $$f((1-\lambda)x + \lambda y) \le (1-\lambda)f(x) + \lambda f(y)$$
> Si l'inégalité est stricte pour $x \neq y$ et $\lambda \in ]0, 1[$, on dit que $f$ est **strictement convexe**.

### C. L'Épigraphe

> **Définition 3 (Épigraphe) :**
> L'épigraphe de $f$, noté $epi(f)$, est l'ensemble des points situés "au-dessus" de son graphe :
> $$epi(f) = \{ (x, t) \in C \times \mathbb{R} \mid f(x) \le t \}$$
> **Théorème :** $f$ est convexe si et seulement si $epi(f)$ est un ensemble convexe.

## 3. Démonstrations

### Démonstration : Un minimum local d'une fonction convexe est global

1. **Hypothèse :** Soit $f$ une fonction convexe sur $C$. Supposons que $x^*$ soit un minimum local : il existe un voisinage $V$ de $x^*$ tel que $\forall x \in V \cap C, f(x^*) \le f(x)$.
2. **Preuve par l'absurde :** Supposons qu'il existe un point $y \in C$ tel que $f(y) < f(x^*)$.
3. **Construction du segment :** Considérons les points $z_\lambda = (1-\lambda)x^* + \lambda y$ pour $\lambda \in [0, 1]$.
4. **Utilisation de la convexité :**
   $f(z_\lambda) \le (1-\lambda)f(x^*) + \lambda f(y)$.
   Comme $f(y) < f(x^*)$, alors $(1-\lambda)f(x^*) + \lambda f(y) < (1-\lambda)f(x^*) + \lambda f(x^*) = f(x^*)$.
   Donc $f(z_\lambda) < f(x^*)$ pour tout $\lambda \in ]0, 1]$.
5. **Contradiction :** Pour $\lambda$ suffisamment petit, $z_\lambda$ appartient au voisinage $V$. On a donc trouvé un point dans le voisinage avec une valeur plus petite que $f(x^*)$, ce qui contredit le fait que $x^*$ est un minimum local.
6. **Conclusion :** $x^*$ est nécessairement un minimum global.

## 4. Exercices d'Application

### Exercice 1 : Convexité des normes
**Énoncé :** Montrer que toute norme sur un espace vectoriel est une fonction convexe.
**Correction Détaillée :**
Soit $\| \cdot \|$ une norme. Pour tous $x, y$ et $\lambda \in [0, 1]$ :
1. $\| (1-\lambda)x + \lambda y \| \le \| (1-\lambda)x \| + \| \lambda y \|$ (Inégalité triangulaire).
2. $\| (1-\lambda)x \| + \| \lambda y \| = |1-\lambda| \cdot \|x\| + |\lambda| \cdot \|y\|$ (Homogénéité).
3. Comme $\lambda \in [0, 1]$, alors $|1-\lambda| = 1-\lambda$ et $|\lambda| = \lambda$.
4. Donc $\| (1-\lambda)x + \lambda y \| \le (1-\lambda)\|x\| + \lambda \|y\|$.
**Résultat :** La définition de la convexité est vérifiée. Toutes les boules unités sont des ensembles convexes.

### Exercice 2 : Niveau Avancé (Matrices PSD)
**Énoncé :** Montrer que l'ensemble $\mathcal{S}_n^+(\mathbb{R})$ des matrices symétriques semi-définies positives est un cône convexe.
**Correction Détaillée :**
Soient $A, B \in \mathcal{S}_n^+$. Pour tout vecteur $v$, $v^T A v \ge 0$ et $v^T B v \ge 0$.
Alors $v^T ((1-\lambda)A + \lambda B) v = (1-\lambda) v^T A v + \lambda v^T B v$. Comme c'est une somme de termes positifs pour $\lambda \in [0, 1]$, le résultat est $\ge 0$.
**Utilité :** En IA, de nombreux problèmes (comme l'apprentissage de métriques) consistent à optimiser une fonction sur cet ensemble convexe.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** L'**Optimisation Convexe** est la seule branche de l'optimisation où l'on possède des algorithmes ultra-rapides et garantis. En IA, on essaie toujours de se ramener à de la convexité quand c'est possible.
- **Example Concret :**
    - **Régression Logistique :** La fonction de perte (Log-Loss) est convexe par rapport aux poids. C'est pour cela qu'on peut entraîner un classifieur linéaire très facilement et qu'il convergera toujours vers la même solution unique.
    - **Support Vector Machines (SVM) :** Le problème de la marge maximale est une optimisation quadratique sous contraintes linéaires. Comme l'objectif et les contraintes sont convexes, on peut le résoudre parfaitement (globalement).
    - **Maximum d'Entropie :** Chercher la distribution de probabilité qui a l'entropie maximale sous certaines contraintes est un problème de maximisation d'une fonction concave (donc minimisation d'une convexe), garantissant une solution unique et stable.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 33 (Formes quadratiques).md]], [[Jalon 34 (Topologie élémentaire des espaces vectoriels normés).md]], [[Jalon 99 (Théorème de Hahn-Banach (forme géométrique)).md]]
- **Concepts Futurs dépendants :** [[Jalon 122 (Notion de sous-gradient).md]], [[Jalon 123 (Problèmes d'optimisation sous contraintes).md]]
