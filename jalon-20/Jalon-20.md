---
uuid: "jalon-20"
title: "Dérivées successives, formules de Taylor-Lagrange, Taylor-Young et développements limités"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/approximation-locale
prev: "[[Jalon 19 (Dérivabilité).md]]"
next: "[[Jalon 21 (Suites de fonctions).md]]"
---

# Jalon 20 : Dérivées successives, formules de Taylor-Lagrange, Taylor-Young et développements limités

## 1. Présentation du concept clé

La compréhension des variations d'une fonction à travers sa dérivée première est une avancée majeure du calcul différentiel. Cependant, cette simple information est souvent insuffisante pour capter la complexité globale de la trajectoire ou du comportement d'une fonction. Imaginez que vous observez le mouvement d'une particule : la position vous donne le lieu, la dérivée première vous donne la vitesse, mais pour comprendre comment la vitesse évolue, vous avez besoin de l'accélération, soit la dérivée seconde. Poursuivez ce raisonnement et vous touchez à l'essence des dérivées successives.

C'est ici qu'intervient le génie de Brook Taylor (et plus tard de Colin Maclaurin, Joseph-Louis Lagrange et Thomas Bayes) : si une fonction est suffisamment "lisse" (c'est-à-dire qu'elle possède de nombreuses dérivées successives), il est possible de l'approximer localement par un polynôme. Les polynômes sont les structures algébriques les plus simples et les plus stables à manipuler (sommes et produits). Les formules de Taylor fournissent la recette exacte pour construire le polynôme qui "épouse" au plus près la courbe de la fonction en un point donné. Plus on ajoute de termes (liés aux dérivées d'ordre supérieur), plus l'approximation devient précise et s'étend sur un voisinage plus large, jusqu'à se confondre avec la fonction elle-même sous certaines conditions analytiques. Ce passage du complexe transcendantal au polynomial est le cœur battant de l'analyse locale.

## 2. Formalisation

### A. Énoncé Symbolique Strict

**Dérivées successives :**
Soit $I$ un intervalle de $\mathbb{R}$, $f : I \to \mathbb{R}$ et $a \in I$. On définit par récurrence la dérivée d'ordre $n$ (notée $f^{(n)}$) par :
- $f^{(0)} = f$
- Si $f^{(n)}$ est définie et dérivable sur $I$, $f^{(n+1)} = (f^{(n)})'$

**Formules de Taylor :**
Soit $f$ une fonction suffisamment régulière sur un intervalle $I$ et $a, x \in I$. Le polynôme de Taylor de degré $n$ de $f$ en $a$ est donné par :
$T_n(x) = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!} (x-a)^k$

1. **Théorème de Taylor-Young (Approximation asymptotique locale) :**
Si $f$ est de classe $C^n$ sur $I$, alors au voisinage de $a$ :
$f(x) = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!} (x-a)^k + o((x-a)^n) \quad \text{lorsque } x \to a$

2. **Théorème de Taylor-Lagrange (Évaluation globale du reste) :**
Si $f$ est de classe $C^{n+1}$ sur $I$, alors pour tout $x \in I$, il existe $c$ strictement compris entre $a$ et $x$ tel que :
$f(x) = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!} (x-a)^k + \frac{f^{(n+1)}(c)}{(n+1)!} (x-a)^{n+1}$

3. **Développement Limité (DL) :**
Une fonction $f$ admet un développement limité d'ordre $n$ en $a$ s'il existe un polynôme $P_n$ de degré au plus $n$ tel que $f(x) = P_n(x) + o((x-a)^n)$ lorsque $x \to a$. Si $f$ est de classe $C^n$, $P_n$ est unique et correspond au polynôme de Taylor.

### B. Anatomie et Typage Chirurgical

- $I$ : intervalle de $\mathbb{R}$, sous-ensemble connexe de la droite réelle.
- $f : I \to \mathbb{R}$ : application à valeurs réelles.
- $f^{(k)}(a)$ : scalaire réel, valeur de la $k$-ième dérivée évaluée en $a$. C'est le coefficient qui porte l'information de la variation d'ordre $k$.
- $k!$ (factorielle) : scalaire entier $k(k-1)\dots 1$. C'est le facteur de normalisation issu des dérivées successives du monôme $(x-a)^k$.
- $o((x-a)^n)$ : notation de Landau. Cela représente une fonction $\epsilon(x)$ telle que $\epsilon(x)/(x-a)^n \to 0$ quand $x \to a$. C'est le "petit reste" qui garantit que l'erreur de l'approximation décroît plus vite que $(x-a)^n$.
- $\frac{f^{(n+1)}(c)}{(n+1)!} (x-a)^{n+1}$ : Reste de Lagrange. Contrairement au reste de Young, c'est une forme explicite de l'erreur globale sur l'intervalle $[a, x]$. Le point $c$ existe mais est généralement inconnu.

### C. Exemples de Validation

**Exemple trivial (Taylor-Young) :**
Soit $f(x) = \sin(x)$ en $a=0$.
$f^{(0)}(0) = 0$, $f^{(1)}(0) = \cos(0)=1$, $f^{(2)}(0) = -\sin(0)=0$, $f^{(3)}(0) = -\cos(0)=-1$.
D'où $DL_3(0)$ de $\sin(x)$ : $\sin(x) = x - \frac{x^3}{3!} + o(x^3) = x - \frac{x^3}{6} + o(x^3)$.

**Exemple complexe (Opérations sur les DL) :**
Soit à calculer le DL d'ordre 3 en 0 de $h(x) = e^x \cos(x)$.
DL de $e^x$ à l'ordre 3 : $1 + x + \frac{x^2}{2} + \frac{x^3}{6} + o(x^3)$.
DL de $\cos(x)$ à l'ordre 3 : $1 - \frac{x^2}{2} + o(x^3)$.
Par produit des parties principales (en tronquant tout ce qui dépasse $x^3$) :
$h(x) = (1 + x + \frac{x^2}{2} + \frac{x^3}{6})(1 - \frac{x^2}{2}) + o(x^3)$
$h(x) = 1 - \frac{x^2}{2} + x - \frac{x^3}{2} + \frac{x^2}{2} + o(x^3)$
$h(x) = 1 + x - \frac{x^3}{2} + o(x^3)$.

### D. Cas Pathologiques et Contre-exemples

**Fonction infiniment dérivable mais avec une série de Taylor qui ne converge pas vers elle :**
Considérons la fonction $f(x) = e^{-1/x^2}$ si $x \neq 0$, et $f(0) = 0$.
Par un calcul rigoureux de la limite des quotients différentiels, on démontre que $f$ est infiniment dérivable en $0$ et que pour tout $n \in \mathbb{N}$, $f^{(n)}(0) = 0$.
Le polynôme de Taylor en $0$ pour tout ordre $n$ est donc $T_n(x) = 0$.
Ainsi, le DL de $f$ est $f(x) = 0 + o(x^n)$.
Cependant, pour tout $x \neq 0$, $f(x) > 0$. L'approximation locale par Taylor-Young est correcte (car l'erreur $e^{-1/x^2}$ décroît plus vite que toute puissance de $x$), mais la série infinie de Taylor ne reconstitue pas la fonction hors de 0. On dit que $f$ n'est pas analytique en 0.

## 3. Démonstrations

### A. Démonstration de la Formule de Taylor-Lagrange (Ordre $n$)

Soit $f : [a, b] \to \mathbb{R}$ une fonction de classe $C^{n+1}$.
Fixons $x \in [a,b]$ avec $x > a$. On définit le polynôme de Taylor $T_n(t)$ pour tout $t \in [a, x]$ par :
$T_n(t) = \sum_{k=0}^n \frac{f^{(k)}(t)}{k!} (x-t)^k$

L'objectif est d'évaluer la différence $f(x) - T_n(a)$.
Introduisons la fonction auxiliaire $\varphi : [a, x] \to \mathbb{R}$ définie par :
$\varphi(t) = f(x) - \sum_{k=0}^n \frac{f^{(k)}(t)}{k!} (x-t)^k - A \frac{(x-t)^{n+1}}{(n+1)!}$
où $A$ est une constante réelle choisie de sorte que $\varphi(a) = 0$.
Remarquons que $\varphi(x) = f(x) - f(x) - A \cdot 0 = 0$.

Puisque $f$ est $C^{n+1}$, $\varphi$ est continue sur $[a, x]$ et dérivable sur $]a, x[$. Avec $\varphi(a) = \varphi(x) = 0$, nous sommes dans les conditions du théorème de Rolle.
Il existe donc $c \in ]a, x[$ tel que $\varphi'(c) = 0$.

Calculons la dérivée $\varphi'(t)$ pour $t \in ]a, x[$ :
$\varphi'(t) = - \frac{d}{dt} \left[ \sum_{k=0}^n \frac{f^{(k)}(t)}{k!} (x-t)^k \right] - A \frac{d}{dt} \left[ \frac{(x-t)^{n+1}}{(n+1)!} \right]$
La première dérivée est une somme télescopique :
$\frac{d}{dt} \left[ \sum_{k=0}^n \frac{f^{(k)}(t)}{k!} (x-t)^k \right] = \sum_{k=0}^n \left( \frac{f^{(k+1)}(t)}{k!} (x-t)^k - \frac{f^{(k)}(t)}{k!} k(x-t)^{k-1} \right)$
Pour $k=0$, le terme est $f'(t)$.
La somme se déploie :
$= f'(t) + \left( \frac{f''(t)}{1!} (x-t) - f'(t) \right) + \left( \frac{f'''(t)}{2!} (x-t)^2 - \frac{f''(t)}{1!} (x-t) \right) + \dots + \left( \frac{f^{(n+1)}(t)}{n!} (x-t)^n - \frac{f^{(n)}(t)}{(n-1)!} (x-t)^{n-1} \right)$
Tous les termes s'annulent sauf le dernier. Donc :
$\frac{d}{dt} \left[ T_n(t) \right] = \frac{f^{(n+1)}(t)}{n!} (x-t)^n$

Revenons à $\varphi'(t)$ :
$\varphi'(t) = - \frac{f^{(n+1)}(t)}{n!} (x-t)^n - A \frac{(n+1)(-1)(x-t)^n}{(n+1)!}$
$\varphi'(t) = - \frac{f^{(n+1)}(t)}{n!} (x-t)^n + A \frac{(x-t)^n}{n!} = \frac{(x-t)^n}{n!} (A - f^{(n+1)}(t))$

Comme $\varphi'(c) = 0$ et $c < x$ (donc $(x-c)^n \neq 0$), il faut nécessairement que :
$A - f^{(n+1)}(c) = 0 \implies A = f^{(n+1)}(c)$.

Nous avons défini $A$ tel que $\varphi(a) = 0$. En remplaçant $A$ dans l'équation initiale de $\varphi(a) = 0$ :
$0 = f(x) - \sum_{k=0}^n \frac{f^{(k)}(a)}{k!} (x-a)^k - f^{(n+1)}(c) \frac{(x-a)^{n+1}}{(n+1)!}$
$f(x) = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!} (x-a)^k + \frac{f^{(n+1)}(c)}{(n+1)!} (x-a)^{n+1}$

Ce qui achève la démonstration du Théorème de Taylor-Lagrange. $\blacksquare$

## 4. Exercices d'Application

*(Les exercices complets sont disponibles dans les dossiers `exos/` et `tp/`.)*

## 5. Application en Intelligence Artificielle

En optimisation des réseaux de neurones et dans les algorithmes d'apprentissage automatique, la formule de Taylor est au cœur des méthodes de second ordre.
Si l'on considère une fonction de coût (Loss) $L(\theta)$ paramétrée par les poids $\theta \in \mathbb{R}^d$, la descente de gradient classique repose sur une approximation de Taylor au premier ordre :
$L(\theta + \Delta \theta) \approx L(\theta) + \nabla L(\theta)^\top \Delta \theta$.
Pour minimiser ce terme, on choisit $\Delta \theta = -\eta \nabla L(\theta)$.

Cependant, dans des paysages de perte complexes (ravins étroits, plateaux), l'information de courbure est cruciale. L'approximation de Taylor au second ordre s'écrit :
$L(\theta + \Delta \theta) \approx L(\theta) + \nabla L(\theta)^\top \Delta \theta + \frac{1}{2} \Delta \theta^\top H(\theta) \Delta \theta$
où $H(\theta)$ est la matrice Hessienne (généralisation de la dérivée seconde en dimension supérieure).
En dérivant cette approximation par rapport à $\Delta \theta$ et en l'égalisant à zéro, on obtient la méthode de Newton :
$\Delta \theta = - H(\theta)^{-1} \nabla L(\theta)$.
Cette méthode converge quadratiquement, utilisant explicitement la courbure pour adapter le pas dans chaque direction. Des algorithmes modernes comme L-BFGS (Limited-memory Broyden-Fletcher-Goldfarb-Shanno) exploitent cette formulation théorique en approximant $H^{-1}$ pour éviter le coût prohibitif d'inversion matricielle pour des millions de paramètres.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 19 (Dérivabilité)]]
- **Concepts Futurs dépendants :** [[Jalon 23 (Séries entières)]], [[Jalon 47 (Dérivées partielles d'ordre deux)]], [[Jalon 131 (Algorithmes d'optimisation de second ordre en grande dimension)]]
