---
uuid: "jalon-41"
title: "Équations différentielles linéaires du premier ordre"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/systemes-dynamiques
prev: "[[Jalon 40 (Intégrales dépendant d'un paramètre).md]]"
next: "[[Jalon 42 (Équations différentielles linéaires du second ordre à coefficients constants.).md]]"
---

# Jalon 41 : Équations différentielles linéaires du premier ordre

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez que vous poussez un petit bateau sur un étang. La vitesse à laquelle le bateau avance (la dérivée) dépend de deux choses : le courant de l'eau qui l'entraîne naturellement (la partie homogène de l'équation) et la force avec laquelle vous le poussez (le second membre). Une équation différentielle du premier ordre, c'est comme une règle de conduite qui vous dit, à chaque instant, quelle doit être votre vitesse en fonction de votre position actuelle.
- **Le "Pourquoi on a inventé ça" :** La nature ne nous donne pas souvent des positions directes, elle nous donne des lois de mouvement (des forces, des taux de croissance). Pour retrouver la trajectoire complète (la position), il faut "remonter" de la dérivée à la fonction. C'est le cœur de la physique, de la biologie (croissance de populations) et de l'IA (évolution des poids d'un réseau).
- **Visualisation :** Imaginez un champ de petites flèches sur une feuille. Chaque flèche indique la direction à suivre. Résoudre l'équation, c'est tracer une courbe qui suit parfaitement ces flèches.

## 2. Formalisation & Rigueur Académique

Soient $a$ et $b$ deux fonctions continues sur un intervalle $I \subset \mathbb{R}$. On considère l'équation différentielle linéaire du premier ordre $(E)$ :
$$y'(t) + a(t) y(t) = b(t)$$

### A. L'Équation Homogène

L'équation homogène associée est $(H) : y'(t) + a(t) y(t) = 0$.

> **Théorème (Solution de l'équation homogène) :**
> Les solutions de $(H)$ sur $I$ sont les fonctions de la forme :
> $$y_H(t) = C e^{-A(t)}$$
> où $C \in \mathbb{R}$ est une constante et $A$ est une primitive de $a$ sur $I$.

### B. L'Équation Complète

> **Théorème (Structure de l'ensemble des solutions) :**
> L'ensemble des solutions de $(E)$ est un espace affine de dimension 1. La solution générale est de la forme :
> $$y(t) = y_H(t) + y_P(t)$$
> où $y_P$ est une solution particulière de $(E)$.

> **Théorème de Cauchy-Lipschitz (Cas linéaire) :**
> Pour tout $t_0 \in I$ et $y_0 \in \mathbb{R}$, il existe une unique solution $y$ de $(E)$ telle que $y(t_0) = y_0$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Méthode de la Variation de la Constante

On cherche une solution particulière de $(E)$ sous la forme $y_P(t) = \lambda(t) e^{-A(t)}$, où $\lambda$ est une fonction dérivable (on "fait varier" la constante $C$).

1. **Calcul de la dérivée :**
   $y_P'(t) = \lambda'(t) e^{-A(t)} + \lambda(t) (-a(t)) e^{-A(t)}$.
   $y_P'(t) = \lambda'(t) e^{-A(t)} - a(t) y_P(t)$.

2. **Injection dans l'équation (E) :**
   $(y_P'(t) + a(t) y_P(t)) = b(t)$
   $(\lambda'(t) e^{-A(t)} - a(t) y_P(t) + a(t) y_P(t)) = b(t)$
   $\lambda'(t) e^{-A(t)} = b(t)$.

3. **Isolement de $\lambda'$ :**
   $\lambda'(t) = b(t) e^{A(t)}$.

4. **Intégration :**
   La fonction $\lambda'$ est continue (car $b, a$ et $e^A$ le sont), elle admet donc une primitive $\lambda(t) = \int b(t) e^{A(t)} dt$.

5. **Conclusion :**
   Une solution particulière est $y_P(t) = \left( \int b(t) e^{A(t)} dt \right) e^{-A(t)}$.
   La solution générale est $y(t) = \left( C + \int_{t_0}^t b(s) e^{A(s)} ds \right) e^{-A(t)}$.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Résolution d'une équation simple
**Énoncé :** Résoudre sur $\mathbb{R}$ : $y'(t) + 2t y(t) = t$.
**Correction Détaillée :**
1. **Équation homogène :** $y' + 2ty = 0$. Primitive de $2t$ est $t^2$.
   $y_H(t) = C e^{-t^2}$.
2. **Solution particulière :** On remarque que $y_P(t) = 1/2$ est une solution évidente (sa dérivée est nulle, et $2t(1/2) = t$).
   *Note : on aurait pu utiliser la variation de la constante, mais l'observation directe est plus rapide.*
3. **Solution générale :** $y(t) = C e^{-t^2} + \frac{1}{2}$.

### Exercice 2 : Niveau Avancé (Facteur intégrant)
**Énoncé :** Résoudre $t y' - y = t^2$ sur $]0, +\infty[$.
**Correction Détaillée :**
1. **Normalisation :** $y' - \frac{1}{t} y = t$. Ici $a(t) = -1/t$.
2. **Homogène :** $\int a(t) dt = -\ln(t)$. $y_H(t) = C e^{\ln(t)} = C t$.
3. **Variation de la constante :** $y_P(t) = \lambda(t) t$.
   $y_P'(t) = \lambda'(t) t + \lambda(t)$.
   Injection : $(\lambda' t + \lambda) - \frac{1}{t}(\lambda t) = t \implies \lambda' t = t \implies \lambda' = 1$.
   Donc $\lambda(t) = t$.
4. **Solution :** $y(t) = (C + t) t = C t + t^2$.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, de nombreux processus d'optimisation sont des discrétisations d'équations différentielles du premier ordre. La **descente de gradient** $\theta_{t+1} = \theta_t - \eta \nabla L(\theta_t)$ peut être vue comme la discrétisation d'Euler de l'EDO :
  $$\frac{d\theta}{dt} = -\nabla L(\theta)$$
- **Exemple Concret :**
    - **Apprentissage avec Momentum :** L'ajout d'un terme de momentum transforme l'équation en une EDO du second ordre (Jalon 42), mais on peut la réécrire comme un système de deux équations du premier ordre. Comprendre la stabilité des solutions de ces EDO permet de choisir le bon **taux d'apprentissage** (learning rate) pour éviter que le modèle n'oscille ou ne diverge.
    - **Neural ODEs :** Cette architecture remplace les couches discrètes $h_{t+1} = f(h_t)$ par une évolution continue $\frac{dh}{dt} = f(h(t), t, \theta)$. Le réseau "apprend" l'équation différentielle elle-même. Pour prédire, on résout l'équation du premier ordre à l'aide de solveurs numériques (Runge-Kutta).

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 38 (Théorème fondamental de l'analyse).md]], [[Jalon 19 (Dérivabilité).md]]
- **Concepts Futurs dépendants :** [[Jalon 42 (Équations différentielles linéaires du second ordre à coefficients constants.).md]], [[Jalon 128 (Flots de gradient).md]]
