---
uuid: "jalon-41"
title: "Équations différentielles linéaires du premier ordre et méthode de variation de la constante"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/systemes-dynamiques
prev: "[[Jalon 40 (Intégrales dépendant d'un paramètre).md]]"
next: "[[Jalon 42 (Équations différentielles linéaires du second ordre à coefficients constants.).md]]"
---

# Jalon 41 : Équations différentielles linéaires du premier ordre et méthode de variation de la constante

## 1. Origine et intuition géométrique

L'étude des équations différentielles prend sa source dans le besoin viscéral de la physique de prédire l'évolution d'un système dont on ne connaît que la loi instantanée de variation. L'invention du calcul différentiel par Newton et Leibniz au XVIIe siècle a fourni le langage mathématique adéquat : si l'on connaît la vitesse d'un mobile (sa dérivée) en fonction de sa position ou du temps, peut-on reconstruire sa trajectoire complète ?

Une équation différentielle du premier ordre de la forme $y'(t) = f(t, y(t))$ traduit géométriquement l'existence d'un champ de tangentes. En chaque point $(t, y)$, la fonction $f$ prescrit la pente de la courbe solution passant par ce point. Résoudre l'équation revient à tracer une courbe intégrale qui "épouse" parfaitement ce champ de directions en tout point.

Historiquement, des mathématiciens comme Euler ont développé des méthodes d'approximation numérique pour suivre ces courbes, tandis que Cauchy et Lipschitz, plus tard, poseront le cadre rigoureux garantissant l'existence et l'unicité de telles trajectoires sous des hypothèses de régularité.

## 2. Définitions et structures algébriques

Dans ce qui suit, on désigne par $I$ un intervalle d'intérieur non vide de $\mathbb{R}$, et $\mathbb{K}$ désigne $\mathbb{R}$ ou $\mathbb{C}$.

### A. Équation différentielle linéaire scalaire du premier ordre

**Définition 1 (Équation complète et homogène associée) :**
Soient $a : I \to \mathbb{K}$ et $b : I \to \mathbb{K}$ deux fonctions continues sur l'intervalle $I$.
L'équation différentielle linéaire scalaire du premier ordre associée à $a$ et $b$, notée $(E)$, est l'équation d'inconnue $y : I \to \mathbb{K}$ dérivable, définie par :
$$(E) : \forall t \in I, \quad y'(t) + a(t)y(t) = b(t)$$

L'équation différentielle homogène associée, notée $(H)$, est obtenue en annulant le second membre $b$ :
$$(H) : \forall t \in I, \quad y'(t) + a(t)y(t) = 0$$

### B. Structure de l'ensemble des solutions de l'équation homogène

**Théorème 1 (Espace des solutions de (H)) :**
L'ensemble $\mathcal{S}_H$ des solutions de l'équation homogène $(H)$ sur $I$ est un $\mathbb{K}$-espace vectoriel de dimension 1.
Explicitement, si $A : I \to \mathbb{K}$ est une primitive quelconque de la fonction continue $a$ sur $I$, alors :
$$\mathcal{S}_H = \left\{ t \mapsto C e^{-A(t)} \mathrel{\Big|} C \in \mathbb{K} \right\}$$

**Exemple d'application immédiate :**
Considérons l'équation $(H) : y'(t) + \frac{2t}{1+t^2} y(t) = 0$ sur $I = \mathbb{R}$.
Ici, $a(t) = \frac{2t}{1+t^2}$, qui est continue sur $\mathbb{R}$.
Une primitive évidente est $A(t) = \ln(1+t^2)$.
Les solutions sont donc les fonctions de la forme $y_H(t) = C e^{-\ln(1+t^2)} = \frac{C}{1+t^2}$ avec $C \in \mathbb{R}$.

### C. Structure de l'ensemble des solutions de l'équation complète

**Théorème 2 (Espace affine des solutions de (E)) :**
L'ensemble $\mathcal{S}_E$ des solutions de l'équation avec second membre $(E)$ est un espace affine de direction $\mathcal{S}_H$.
Autrement dit, si $y_P \in \mathcal{S}_E$ est une solution particulière de $(E)$, alors toute solution $y$ de $(E)$ s'écrit de manière unique :
$$y = y_H + y_P$$
avec $y_H \in \mathcal{S}_H$.

**Théorème 3 (Problème de Cauchy) :**
Soit $t_0 \in I$ et $y_0 \in \mathbb{K}$. Le problème de Cauchy :
$$\begin{cases}
y'(t) + a(t)y(t) = b(t) \\
y(t_0) = y_0
\end{cases}$$
admet une unique solution définie sur l'intervalle $I$ tout entier.

## 3. Démonstrations et méthodes de résolution

### Méthode de la variation de la constante

La méthode de la variation de la constante (attribuée à Lagrange) est un algorithme systématique pour déterminer une solution particulière $y_P$ de l'équation complète $(E)$ connaissant la forme générale des solutions de $(H)$.

**Démonstration pas à pas :**
Soit $A$ une primitive de $a$ sur $I$. On sait que toute solution de l'équation homogène $(H)$ s'écrit $t \mapsto C e^{-A(t)}$ avec $C \in \mathbb{K}$ constant.
On cherche une solution particulière de $(E)$ sous la forme :
$$y_P(t) = C(t) e^{-A(t)}$$
où $C : I \to \mathbb{K}$ est une fonction dérivable (la "constante" devient une fonction, d'où le nom de la méthode).

1. **Dérivation de $y_P$ :**
   Par la règle de dérivation d'un produit, on obtient pour tout $t \in I$ :
   $$y_P'(t) = C'(t) e^{-A(t)} + C(t) \left( -a(t) e^{-A(t)} \right)$$

2. **Injection dans l'équation $(E)$ :**
   On impose que $y_P$ soit solution de $(E)$ :
   $$y_P'(t) + a(t)y_P(t) = b(t)$$
   En substituant $y_P'(t)$ et $y_P(t)$, cela donne :
   $$C'(t) e^{-A(t)} - C(t) a(t) e^{-A(t)} + a(t) C(t) e^{-A(t)} = b(t)$$

3. **Simplification et intégration :**
   Les termes en $C(t)$ s'annulent miraculeusement (c'est l'essence de la méthode), laissant :
   $$C'(t) e^{-A(t)} = b(t) \iff C'(t) = b(t) e^{A(t)}$$
   La fonction $t \mapsto b(t) e^{A(t)}$ étant continue sur $I$ (produit et composée de fonctions continues), elle y admet des primitives. On peut donc choisir pour $C$ la fonction :
   $$C(t) = \int_{t_0}^t b(s) e^{A(s)} \, ds$$
   où $t_0 \in I$ est fixé arbitrairement.

4. **Construction de la solution particulière :**
   On obtient alors la solution particulière explicite :
   $$y_P(t) = \left( \int_{t_0}^t b(s) e^{A(s)} \, ds \right) e^{-A(t)}$$

**Exemple d'application de la méthode :**
Résolvons l'équation $(E) : y'(t) - 2ty(t) = t$ sur $\mathbb{R}$.
1. **Équation homogène $(H) : y'(t) - 2ty(t) = 0$.**
   Ici $a(t) = -2t$, dont une primitive est $A(t) = -t^2$.
   Les solutions de $(H)$ sont de la forme $y_H(t) = C e^{t^2}$, avec $C \in \mathbb{R}$.
2. **Variation de la constante :**
   On cherche une solution particulière de la forme $y_P(t) = C(t) e^{t^2}$.
   On a $y_P'(t) = C'(t)e^{t^2} + 2t C(t) e^{t^2}$.
   L'équation $(E)$ devient : $\left(C'(t)e^{t^2} + 2t C(t) e^{t^2}\right) - 2t \left(C(t)e^{t^2}\right) = t$.
   Ce qui donne $C'(t)e^{t^2} = t \iff C'(t) = t e^{-t^2}$.
3. **Calcul de la primitive $C(t)$ :**
   $C(t) = -\frac{1}{2} e^{-t^2}$. (On prend la primitive s'annulant à l'infini, ou n'importe quelle constante d'intégration, par ex. 0).
4. **Solution particulière et générale :**
   $y_P(t) = \left( -\frac{1}{2} e^{-t^2} \right) e^{t^2} = -\frac{1}{2}$.
   La solution générale est donc $y(t) = C e^{t^2} - \frac{1}{2}$, avec $C \in \mathbb{R}$.

## 4. Connexions avec l'optimisation et le Machine Learning

Les équations différentielles ordinaires (EDO) du premier ordre jouent un rôle structurant dans la théorie contemporaine de l'apprentissage automatique, notamment dans l'analyse continue des algorithmes d'optimisation.

### Gradient Flow (Flot de gradient)
La méthode de descente de gradient, algorithme omniprésent pour l'entraînement des réseaux de neurones, met à jour les paramètres $\theta$ d'un modèle selon la règle discrète $\theta_{k+1} = \theta_k - \eta \nabla L(\theta_k)$, où $L$ est la fonction de perte et $\eta$ le taux d'apprentissage.
Si l'on considère le pas $\eta$ comme un incrément temporel $\Delta t \to 0$, l'algorithme discret s'identifie au schéma d'Euler explicite résolvant l'EDO non linéaire du premier ordre appelée flot de gradient :
$$\frac{d\theta}{dt}(t) = -\nabla L(\theta(t))$$
L'étude de cette EDO (existence de trajectoires bornées, convergence asymptotique vers un point critique) par des méthodes analytiques continues permet d'établir des garanties théoriques fortes (comme la régularisation implicite) qui sont ensuite transposées aux itérations discrètes.

### Neural Ordinary Differential Equations (Neural ODEs)
Proposées récemment, les *Neural ODEs* remplacent les couches séquentielles discrètes des réseaux profonds résiduels (ResNets) par un flot continu. Au lieu d'une dynamique discrète $h_{k+1} = h_k + f_{\theta_k}(h_k)$, l'état caché $h(t)$ évolue selon une équation différentielle ordinaire paramétrée par un réseau de neurones $f_\theta$ :
$$\frac{dh}{dt} = f_\theta(h(t), t)$$
La prédiction finale du modèle correspond à l'intégration de cette EDO d'un instant initial $t_0$ à un instant final $T$. L'apprentissage des paramètres $\theta$ s'effectue alors en calculant le gradient par rapport à un état adjoint, ce qui revient à résoudre une autre EDO du premier ordre "à rebours dans le temps" (la méthode de l'état adjoint, étroitement liée au principe du maximum de Pontryagin), économisant drastiquement la mémoire par rapport à la rétropropagation classique.
