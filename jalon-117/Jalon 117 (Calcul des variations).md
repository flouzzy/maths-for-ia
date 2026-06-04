---
uuid: "jalon-117"
title: "Calcul des variations"
year: 3
trimester: 10
tags:
  - math/analyse
  - ia/optimisation
prev: "[[Jalon 116 (Variétés riemanniennes).md]]"
next: "[[Jalon 118 (Conditions d'optimalité du second ordre pour les fonctionnelles et introduction aux multiplicateurs de Lagrange de dimension infinie.).md]]"
---

# Jalon 117 : Calcul des variations

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous deviez construire une route entre deux villes séparées par des montagnes, des rivières et des forêts.
    - Vous ne cherchez pas un simple nombre, vous cherchez tout le **tracé de la route** (une fonction $y(x)$).
    - Pour chaque tracé possible, vous calculez un score total (le coût de construction, le temps de trajet, la consommation d'essence). Ce score global s'appelle une **Fonctionnelle**.
    - Le **Calcul des variations**, c'est l'art de trouver le tracé parfait qui minimise ce score.
    - L'**Équation d'Euler-Lagrange**, c'est la "recette" qui vous dit, kilomètre par kilomètre, comment la route doit tourner pour que le coût final soit le plus bas possible.
- **Le "Pourquoi on a inventé ça" :** Pour comprendre les lois fondamentales de l'univers. La lumière prend toujours le chemin le plus rapide (principe de Fermat), et une planète suit toujours la trajectoire qui demande le moins d'énergie. En IA, cela nous permet de chercher non pas un poids optimal, mais une **fonction optimale** tout entière.
- **Visualisation :** On imagine une corde tenue par deux points. Si on change un tout petit peu la forme de la corde (une "variation"), le score change. On cherche la forme où n'importe quel petit changement ne fait plus baisser le score.

## 2. Formalisation & Rigueur Académique

Soit $y : [x_1, x_2] \to \mathbb{R}$ une fonction de classe $\mathcal{C}^1$. On considère une fonctionnelle de la forme :
$$J(y) = \int_{x_1}^{x_2} L(x, y(x), y'(x)) dx$$
où $L$ est le **Lagrangien**. On cherche $y$ qui minimise $J$ avec conditions aux bords $y(x_1)=y_1$ and $y(x_2)=y_2$.

### A. Dérivée au sens de Gâteaux

> **Définition :** On appelle variation de $y$ toute fonction $h \in \mathcal{C}^1$ telle que $h(x_1)=h(x_2)=0$. La dérivée de Gâteaux de $J$ dans la direction $h$ est :
> $$\delta J(y, h) = \lim_{\epsilon \to 0} \frac{J(y + \epsilon h) - J(y)}{\epsilon}$$

### B. Équation d'Euler-Lagrange

> **Théorème :** Si $y$ est un extremum de $J$, alors pour tout $x \in [x_1, x_2]$, $y$ doit satisfaire l'équation différentielle suivante :
> $$\frac{\partial L}{\partial y} - \frac{d}{dx} \left( \frac{\partial L}{\partial y'} \right) = 0$$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration de l'Équation d'Euler-Lagrange

1. **Calcul de la variation :**
   $\delta J = \frac{d}{d\epsilon} \left( \int L(x, y+\epsilon h, y'+\epsilon h') dx \right) |_{\epsilon=0}$.
2. **Passage de la dérivée sous l'intégrale :**
   $\delta J = \int \left( \frac{\partial L}{\partial y} h + \frac{\partial L}{\partial y'} h' \right) dx$.
3. **Intégration par parties (IPP) sur le second terme :**
   $\int_{x_1}^{x_2} \frac{\partial L}{\partial y'} h'(x) dx = \left[ \frac{\partial L}{\partial y'} h(x) \right]_{x_1}^{x_2} - \int_{x_1}^{x_2} \frac{d}{dx} \left( \frac{\partial L}{\partial y'} \right) h(x) dx$.
4. **Utilisation des conditions aux bords :** Comme $h(x_1)=h(x_2)=0$, le terme entre crochets est nul.
5. **Regroupement :**
   $\delta J = \int_{x_1}^{x_2} \left( \frac{\partial L}{\partial y} - \frac{d}{dx} \left( \frac{\partial L}{\partial y'} \right) \right) h(x) dx$.
6. **Lemme fondamental du calcul des variations :** Si $\int g(x) h(x) dx = 0$ pour toute fonction $h$ "gentille", alors $g(x) = 0$ partout.
7. **Conclusion :** Le terme entre parenthèses est nul. L'équation d'Euler-Lagrange est démontrée.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Le chemin le plus court
**Énoncé :** Trouver la fonction $y(x)$ qui minimise la longueur $L = \int_{x_1}^{x_2} \sqrt{1 + (y')^2} dx$.
**Correction Détaillée :**
1. Lagrangien : $L = \sqrt{1 + (y')^2}$.
2. $\frac{\partial L}{\partial y} = 0$.
3. $\frac{\partial L}{\partial y'} = \frac{y'}{\sqrt{1 + (y')^2}}$.
4. Euler-Lagrange : $0 - \frac{d}{dx} \left( \frac{y'}{\sqrt{1 + (y')^2}} \right) = 0$.
5. Intégration : $\frac{y'}{\sqrt{1 + (y')^2}} = C$ (constante).
6. Cela implique $y' = A$ (constante).
7. **Résultat :** $y(x) = Ax + B$. Le chemin le plus court est une droite.

### Exercice 2 : Niveau Avancé (Lagrangien dépendant de y'')
**Énoncé :** Trouver l'équation d'Euler-Lagrange pour $J(y) = \int L(x, y, y', y'') dx$.
**Correction Détaillée :**
En faisant deux IPP, on fait apparaître des dérivées d'ordre 4. L'équation devient $\frac{\partial L}{\partial y} - \frac{d}{dx} \frac{\partial L}{\partial y'} + \frac{d^2}{dx^2} \frac{\partial L}{\partial y''} = 0$. C'est le principe utilisé pour modéliser les poutres flexibles ou les courbes "splines" en informatique graphique.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** De nombreux problèmes d'apprentissage peuvent être formulés comme la recherche d'une fonction dans un espace de Hilbert (RKHS) qui minimise une perte fonctionnelle.
- **Example Concret :**
    - **Régularisation de Tikhonov :** On minimise $Loss(f) + \lambda \int \|f'(x)\|^2 dx$. L'équation d'Euler-Lagrange de ce problème définit la "forme" idéale de la fonction apprise (souvent une spline ou un noyau).
    - **Active Contours (Snakes) :** En segmentation d'image, on définit une courbe qui "colle" aux bords des objets en minimisant une énergie. Le mouvement de la courbe est guidé par l'équation d'Euler-Lagrange.
    - **Flow-Matching and ODEs :** Pour transformer un bruit en une image, on cherche le champ de vecteurs le plus "économe" (énergie minimale). On résout cela par du calcul des variations pour obtenir des trajectoires droites et rapides.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 38 (Théorème fondamental de l'analyse).md]], [[Jalon 47 (Dérivées partielles d'ordre deux et Hessienne).md]]
- **Concepts Futurs dépendants :** [[Jalon 118 (Conditions d'optimalité du second ordre pour les fonctionnelles et introduction aux multiplicateurs de Lagrange de dimension infinie.).md]], [[Jalon 128 (Flots de gradient).md]]
