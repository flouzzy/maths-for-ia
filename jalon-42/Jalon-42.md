---
uuid: "jalon-42"
title: "Équations différentielles linéaires du second ordre"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/optimisation
prev: "[[Jalon 41 (Équations différentielles linéaires du premier ordre et méthode de variation de la constante.).md]]"
next: "[[Jalon 43 (Systèmes différentiels linéaires d'ordre 1 et calcul de l'exponentielle de matrice.).md]]"
---
# Jalon 42 : Équations différentielles linéaires du second ordre à coefficients constants

## 1. Introduction

L'étude des équations différentielles linéaires du second ordre trouve ses racines profondes dans la modélisation des phénomènes dynamiques de la physique classique. Dès le XVIIe siècle, l'essor de la mécanique analytique avec Isaac Newton et ses fameuses lois du mouvement a mis en lumière que l'évolution temporelle des systèmes mécaniques est dictée par l'accélération, soit la dérivée seconde de la position. Qu'il s'agisse des oscillations d'un pendule, de la résonance d'un circuit RLC, ou du mouvement des planètes perturbé par des forces de rappel, l'équation universelle qui émerge est intrinsèquement du second ordre. Mathématiquement, c'est Euler et Cauchy qui ont rigoureusement posé les fondations pour résoudre ces équations, transformant un problème d'analyse fonctionnelle en un problème d'algèbre polynomiale via l'équation caractéristique, révélant ainsi un lien sublime entre la dérivation, les nombres complexes et les comportements oscillatoires amortis ou amplifiés.

## 2. Définitions, Théorèmes et Structures Algébriques

### Équation homogène et équation caractéristique

Soient $a, b, c \in \mathbb{R}$ avec $a \neq 0$, et $d : I \to \mathbb{R}$ une fonction continue sur un intervalle $I \subset \mathbb{R}$. L'équation différentielle linéaire du second ordre à coefficients constants se présente sous la forme générale :
$$(E) : a y''(t) + b y'(t) + c y(t) = d(t)$$

L'équation homogène (ou sans second membre) associée est définie par :
$$(H) : a y''(t) + b y'(t) + c y(t) = 0$$

L'espace des solutions de $(H)$ forme un espace vectoriel sur $\mathbb{R}$. Par isomorphisme avec un espace de polynômes, nous introduisons l'équation caractéristique dans $\mathbb{C}$ :
$$a r^2 + b r + c = 0$$
Le discriminant de cette équation algébrique est $\Delta = b^2 - 4ac$.

### Structure des solutions de l'équation homogène

> **Théorème fondamental de l'équation homogène :**
> L'ensemble des solutions de l'équation différentielle $(H)$ est un espace vectoriel de dimension 2 sur $\mathbb{R}$, dont une base $(y_1, y_2)$ dépend strictement du signe du discriminant $\Delta$.
>
> 1. **Si $\Delta > 0$ :** L'équation caractéristique admet deux racines réelles distinctes $r_1, r_2 = \frac{-b \pm \sqrt{\Delta}}{2a}$.
>    La solution générale de $(H)$ est donnée par :
>    $$y_H(t) = \lambda_1 e^{r_1 t} + \lambda_2 e^{r_2 t}, \quad (\lambda_1, \lambda_2) \in \mathbb{R}^2$$
>
> 2. **Si $\Delta = 0$ :** L'équation caractéristique admet une racine réelle double $r_0 = -\frac{b}{2a}$.
>    La solution générale de $(H)$ est :
>    $$y_H(t) = (\lambda_1 + \lambda_2 t) e^{r_0 t}, \quad (\lambda_1, \lambda_2) \in \mathbb{R}^2$$
>
> 3. **Si $\Delta < 0$ :** L'équation caractéristique admet deux racines complexes conjuguées $r = \alpha \pm i \beta$, où $\alpha = -\frac{b}{2a}$ et $\beta = \frac{\sqrt{-\Delta}}{2a}$.
>    La solution générale réelle de $(H)$ est :
>    $$y_H(t) = e^{\alpha t} \left(\lambda_1 \cos(\beta t) + \lambda_2 \sin(\beta t)\right), \quad (\lambda_1, \lambda_2) \in \mathbb{R}^2$$

**Exemple d'application immédiate :**
Résolvons l'équation $y''(t) + 3y'(t) + 2y(t) = 0$.
L'équation caractéristique est $r^2 + 3r + 2 = 0$. On calcule $\Delta = 3^2 - 4(1)(2) = 9 - 8 = 1 > 0$.
Les racines sont $r_1 = \frac{-3-1}{2} = -2$ et $r_2 = \frac{-3+1}{2} = -1$.
La solution générale est donc $y_H(t) = \lambda_1 e^{-2t} + \lambda_2 e^{-t}$, pour $\lambda_1, \lambda_2 \in \mathbb{R}$.

**Configurations pathologiques :**
Il est crucial d'observer que si $a = 0$, l'équation dégénère en une équation du premier ordre $b y'(t) + c y(t) = d(t)$, qui présente des propriétés structurelles fondamentalement différentes (espace de dimension 1), nécessitant l'utilisation du théorème de Cauchy-Lipschitz d'ordre 1. De plus, un coefficient de frottement $b=0$ et une force de rappel négative $c < 0$ ($\Delta > 0$, mais racines opposées) mène à des solutions divergentes $e^{r t}$, traduisant une instabilité exponentielle physique.

### Structure des solutions de l'équation complète

> **Théorème de superposition (Équation Complète) :**
> Soit $(E)$ l'équation complète $a y''(t) + b y'(t) + c y(t) = d(t)$.
> La solution générale $y(t)$ de $(E)$ est la somme de la solution générale de l'équation homogène $y_H(t)$ et d'une solution particulière $y_P(t)$ de l'équation complète :
> $$y(t) = y_H(t) + y_P(t)$$

## 3. Démonstrations Pas-à-Pas

### Démonstration : Racine double de l'équation caractéristique ($\Delta = 0$)

Nous voulons prouver rigoureusement que si $\Delta = 0$, alors $y_2(t) = t e^{r_0 t}$ est bien solution de $a y'' + b y' + c y = 0$ et indépendante de $y_1(t) = e^{r_0 t}$.
On sait que $r_0 = -\frac{b}{2a}$, d'où $2ar_0 + b = 0$. De plus, comme $r_0$ est racine double, $ar_0^2 + br_0 + c = 0$.

1. Soit la fonction candidate $y_2(t) = t e^{r_0 t}$.
2. Calculons la première dérivée par la règle du produit :
   $$y_2'(t) = e^{r_0 t} + t r_0 e^{r_0 t} = (1 + r_0 t) e^{r_0 t}$$
3. Calculons la seconde dérivée :
   $$y_2''(t) = r_0 e^{r_0 t} + r_0(1 + r_0 t) e^{r_0 t} = (2r_0 + r_0^2 t) e^{r_0 t}$$
4. Injectons $y_2(t)$, $y_2'(t)$ et $y_2''(t)$ dans l'équation $(H)$ :
   $$a(2r_0 + r_0^2 t) e^{r_0 t} + b(1 + r_0 t) e^{r_0 t} + c(t e^{r_0 t})$$
5. Factorisons par $e^{r_0 t}$ et regroupons les termes en $t$ :
   $$e^{r_0 t} \left[ t (a r_0^2 + b r_0 + c) + (2a r_0 + b) \right]$$
6. Par hypothèse sur $r_0$, le premier terme entre parenthèses est $0$ (racine de l'équation) et le second est également $0$ (puisque $r_0 = -b/(2a)$).
7. Le résultat est $e^{r_0 t} \left[ t(0) + 0 \right] = 0$. Donc $y_2(t)$ est bien une solution.
8. L'indépendance linéaire (Wronskien) est immédiate car le ratio $\frac{t e^{r_0 t}}{e^{r_0 t}} = t$ n'est pas une constante.

## 4. Applications Avancées

Les équations du second ordre constituent le squelette mathématique de la théorie du contrôle optimal. Dans le contexte de l'apprentissage profond (Deep Learning), l'optimisation par Descente de Gradient Stochastique avec Momentum (SGD+Momentum) représente la discrétisation directe d'une équation différentielle amortie. En définissant une fonction de perte $L(x)$, la dynamique du paramètre $x(t)$ obéit à :
$$m x''(t) + \gamma x'(t) + \nabla L(x(t)) = 0$$
Où $m$ représente l'inertie du modèle et $\gamma$ le coefficient de friction (damping). Une analyse rigoureuse du polynôme caractéristique de l'approximation de Taylor au second ordre de $\nabla L$ permet de dimensionner ces hyperparamètres pour atteindre le régime critique ($\Delta = 0$), garantissant la convergence la plus rapide vers le minimum global sans oscillations destructrices.
