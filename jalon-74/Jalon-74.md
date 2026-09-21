---
uuid: "jalon-74"
title: "Inégalités fondamentales : Hölder, Minkowski, Jensen"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/optimisation
prev: "[[Jalon 73 (Définition des espaces Lp).md]]"
next: "[[Jalon 75 (Preuve de la complétude des espaces Lp).md]]"
---

# Inégalités fondamentales de l'analyse fonctionnelle

## Introduction

L'étude des espaces fonctionnels et de l'intégration, au cœur de la théorie de la mesure, repose sur la maîtrise d'inégalités permettant de comparer, borner et évaluer les normes de fonctions. Les inégalités de Hölder, de Minkowski et de Jensen constituent l'ossature analytique sur laquelle reposent la géométrie des espaces $L^p$, la théorie des probabilités et l'optimisation moderne.
Ces inégalités ne sont pas de simples majorations techniques ; elles traduisent des propriétés géométriques profondes telles que la convexité des espaces, l'indépendance linéaire des signaux et la conservation de l'énergie.

## Définitions, Théorèmes et Exemples

### L'Inégalité de Jensen

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré de probabilité, c'est-à-dire tel que $\mu(X) = 1$. Soit $f$ une fonction intégrable et $\phi : I \to \mathbb{R}$ une fonction convexe sur un intervalle $I$ contenant l'image de $f$.

**Théorème (Inégalité de Jensen) :**
$$ \phi \left( \int_X f d\mu \right) \le \int_X \phi(f) d\mu $$
En termes probabilistes, pour une variable aléatoire $Z$ :
$$ \phi(\mathbb{E}[Z]) \le \mathbb{E}[\phi(Z)] $$

**Dissection des variables :**
- $X$ : l'espace de base (univers).
- $\mu$ : une mesure de probabilité (masse totale $1$).
- $f$ : la fonction d'intérêt (ou variable aléatoire).
- $\phi$ : la fonction de coût ou de transformation, strictement convexe.

**Exemples concrets de validation :**
1. **La fonction exponentielle :** $\phi(x) = \exp(x)$. On obtient $\exp(\mathbb{E}[Z]) \le \mathbb{E}[\exp(Z)]$. Si $Z$ prend les valeurs $0$ et $1$ avec probabilité $0.5$. $\mathbb{E}[Z] = 0.5$. $\exp(0.5) \approx 1.648$. $\mathbb{E}[\exp(Z)] = 0.5 \exp(0) + 0.5 \exp(1) = 0.5(1 + 2.718) = 1.859$. $1.648 \le 1.859$.
2. **La fonction carré :** $\phi(x) = x^2$. On obtient $(\mathbb{E}[Z])^2 \le \mathbb{E}[Z^2]$, ce qui équivaut à la positivité de la variance : $\text{Var}(Z) = \mathbb{E}[Z^2] - (\mathbb{E}[Z])^2 \ge 0$.
3. **La fonction logarithme (concave) :** L'inégalité s'inverse. $\phi(x) = -\ln(x)$ est convexe. $-\ln(\mathbb{E}[Z]) \le \mathbb{E}[-\ln(Z)]$ donne $\ln(\mathbb{E}[Z]) \ge \mathbb{E}[\ln(Z)]$.
4. **Moyenne harmonique vs arithmétique :** $\phi(x) = \frac{1}{x}$ sur $]0, +\infty[$. $\frac{1}{\mathbb{E}[Z]} \le \mathbb{E}[\frac{1}{Z}]$. Pour $Z \in \{2, 4\}$ équiprobable, $\mathbb{E}[Z] = 3 \\implies 1/3 \approx 0.333$. $\mathbb{E}[1/Z] = 0.5(0.5 + 0.25) = 0.375$.
5. **Cas limite déterministe :** Si $Z$ est constante égale à $c$, $\mathbb{E}[Z] = c$, $\phi(\mathbb{E}[Z]) = \phi(c)$, et $\mathbb{E}[\phi(Z)] = \phi(c)$. L'inégalité est une égalité, confirmant que seule la variance crée l'écart de Jensen.

**Cas pathologiques :** Si $\phi$ n'est pas convexe, ou si $\mu$ n'est pas de masse $1$ (par exemple, la mesure de Lebesgue sur $\mathbb{R}$), l'inégalité est fausse.

### L'Inégalité de Hölder

Soient $p, q \in [1, +\infty]$ tels que $\frac{1}{p} + \frac{1}{q} = 1$. Les nombres $p$ et $q$ sont dits conjugués.

**Théorème (Inégalité de Hölder) :**
Pour toutes fonctions $f \in L^p(\mu)$ et $g \in L^q(\mu)$, le produit $fg$ appartient à $L^1(\mu)$ et :
$$ \|fg\|_1 \le \|f\|_p \cdot \|g\|_q $$
Soit de manière développée :
$$ \int_X |f(x)g(x)| d\mu(x) \le \left( \int_X |f(x)|^p d\mu(x) \right)^{1/p} \left( \int_X |g(x)|^q d\mu(x) \right)^{1/q} $$

**Dissection des variables :**
- $p, q$ : exposants réels ou infinis conjugués. Si $p=1, q=\infty$. Si $p=2, q=2$.
- $\| \cdot \|_p$ : la norme dans l'espace $L^p$.
- $f, g$ : fonctions mesurables définies sur $X$.

**Exemples concrets de validation :**
1. **Cas Euclidien (Cauchy-Schwarz) :** Si $p=q=2$, dans $\mathbb{R}^n$, $|\sum x_i y_i| \le \sqrt{\sum x_i^2} \sqrt{\sum y_i^2}$. Pour $x=(1, 2)$ et $y=(3, 4)$, le produit scalaire est $3+8=11$. Les normes sont $\sqrt{5}$ et $\sqrt{25}=5$. On a bien $11 \le 5\sqrt{5} \approx 11.18$.
2. **Cas asymétrique p=1, q=infini :** $\int |fg| \le \|f\|_1 \|g\|_\infty$. Si $f(x) = e^{-x}$ sur $[0, \infty[$ (norme $L^1$ = 1) et $g(x) = \sin(x)$ (norme $L^\infty$ = 1). $\int_0^\infty e^{-x}|\sin(x)| dx \le 1 \cdot 1 = 1$.
3. **Cas de suites p=4, q=4/3 :** $x = (1, 1)$, $y = (2, 0)$. $\|xy\|_1 = |1 \cdot 2| + |1 \cdot 0| = 2$. $\|x\|_4 = (1^4 + 1^4)^{1/4} = 2^{1/4}$. $\|y\|_{4/3} = (2^{4/3} + 0)^{3/4} = 2$. Le produit des normes est $2 \cdot 2^{1/4} \approx 2.378 \ge 2$.
4. **Vecteurs orthogonaux :** $x = (1, 0)$, $y = (0, 1)$. $\|xy\|_1 = 0$. Inégalité trivialement respectée : $0 \le 1 \cdot 1$.
5. **Cas d'égalité :** L'égalité est atteinte si et seulement si $|f|^p$ et $|g|^q$ sont proportionnels presque partout.

**Cas pathologiques :** Si $\frac{1}{p} + \frac{1}{q} \neq 1$, l'inégalité est fausse ou n'a pas de sens dimensionnel homogène.

### L'Inégalité de Minkowski

Soit $p \in [1, +\infty]$.

**Théorème (Inégalité de Minkowski) :**
Pour toutes fonctions $f, g \in L^p(\mu)$, la somme $f+g$ appartient à $L^p(\mu)$ et :
$$ \|f+g\|_p \le \|f\|_p + \|g\|_p $$

**Exemples concrets de validation :**
1. **Cas p=1 (valeur absolue standard) :** $\int |f+g| \le \int |f| + \int |g|$.
2. **Cas p=2 (triangle euclidien) :** Dans $\mathbb{R}^2$, pour $x=(1,0)$ et $y=(0,1)$, $\|x+y\|_2 = \|(1,1)\|_2 = \sqrt{2} \approx 1.414$. Et $\|x\|_2 + \|y\|_2 = 1 + 1 = 2$. On a bien $1.414 \le 2$.
3. **Cas p=infini :** $\sup |f+g| \le \sup |f| + \sup |g|$.
4. **Alignement p=2 :** Pour $x=(1,2)$ et $y=(2,4)$ (colinéaires de même sens), $\|x+y\|_2 = \|(3,6)\|_2 = \sqrt{45} \approx 6.708$. $\|x\|_2 = \sqrt{5}$, $\|y\|_2 = \sqrt{20} = 2\sqrt{5}$. La somme est $3\sqrt{5} = \sqrt{45}$. L'égalité est stricte.
5. **Cas p < 1 (Attention !) :** L'inégalité est **inversée** ou fausse. Pour $p=0.5$, la sphère unitaire n'est plus convexe.

## Demonstrations

### Lemme de Young
Pour tous $a, b \ge 0$ et $p, q \in ]1, +\infty[$ conjugués :
$$ ab \le \frac{a^p}{p} + \frac{b^q}{q} $$
*Preuve :* La fonction logarithme est strictement concave. Or $\frac{1}{p} + \frac{1}{q} = 1$. Donc :
$$ \ln\left( \frac{a^p}{p} + \frac{b^q}{q} \right) \ge \frac{1}{p}\ln(a^p) + \frac{1}{q}\ln(b^q) = \ln(a) + \ln(b) = \ln(ab) $$
Par croissance stricte de l'exponentielle, le résultat s'ensuit.

### Démonstration de l'inégalité de Hölder
Supposons $\|f\|_p > 0$ et $\|g\|_q > 0$. Posons les fonctions normalisées :
$$ u(x) = \frac{|f(x)|}{\|f\|_p} \quad \text{et} \quad v(x) = \frac{|g(x)|}{\|g\|_q} $$
Pour presque tout $x$, appliquons le lemme de Young :
$$ u(x)v(x) \le \frac{u(x)^p}{p} + \frac{v(x)^q}{q} $$
En intégrant sur $X$ :
$$ \int_X u(x)v(x) d\mu \le \frac{1}{p} \int_X u(x)^p d\mu + \frac{1}{q} \int_X v(x)^q d\mu $$
Or par définition de la normalisation :
$$ \int_X u(x)^p d\mu = \int_X \frac{|f(x)|^p}{\|f\|_p^p} d\mu = \frac{\|f\|_p^p}{\|f\|_p^p} = 1 $$
De même, $\int_X v(x)^q d\mu = 1$.
Donc :
$$ \int_X \frac{|f(x)g(x)|}{\|f\|_p \|g\|_q} d\mu \le \frac{1}{p}(1) + \frac{1}{q}(1) = 1 $$
Ce qui donne bien $\|fg\|_1 \le \|f\|_p \|g\|_q$.

### Démonstration de l'inégalité de Minkowski
L'inégalité est triviale pour $p=1$ (inégalité triangulaire classique scalaire) et $p=\infty$.
Pour $1 < p < \infty$, notons que $|f+g|^p = |f+g| \cdot |f+g|^{p-1} \le |f| \cdot |f+g|^{p-1} + |g| \cdot |f+g|^{p-1}$.
En intégrant :
$$ \int |f+g|^p \le \int |f| \cdot |f+g|^{p-1} + \int |g| \cdot |f+g|^{p-1} $$
Soit $q$ le conjugué de $p$, donc $q = \frac{p}{p-1}$, ce qui implique $(p-1)q = p$.
Appliquons l'inégalité de Hölder à chaque terme du membre de droite :
$$ \int |f| \cdot |f+g|^{p-1} \le \|f\|_p \cdot \left( \int (|f+g|^{p-1})^q \right)^{1/q} = \|f\|_p \cdot \|f+g\|_p^{p/q} $$
Puisque $p/q = p-1$, on obtient :
$$ \|f+g\|_p^p \le (\|f\|_p + \|g\|_p) \cdot \|f+g\|_p^{p-1} $$
Si $\|f+g\|_p = 0$, l'inégalité est triviale. Sinon, en divisant les deux membres par $\|f+g\|_p^{p-1}$, on obtient l'inégalité de Minkowski :
$$ \|f+g\|_p \le \|f\|_p + \|g\|_p $$

## Applications en Physique, Logique et Intelligence Artificielle

En Apprentissage Profond (Deep Learning) et Théorie de l'Information, ces inégalités sont omniprésentes :
- **Divergence de Kullback-Leibler (KL) :** La preuve que $D_{KL}(P || Q) \ge 0$ repose intégralement sur l'inégalité de Jensen appliquée à la fonction strictement convexe $-\log(x)$. Ceci justifie la minimisation de la Cross-Entropy.
- **Variational Auto-Encoders (VAE) :** La borne inférieure sur l'évidence (ELBO) est obtenue par une application directe de l'inégalité de Jensen : $\log \mathbb{E}_{Z}[P(X|Z)] \ge \mathbb{E}_{Z}[\log P(X|Z)]$.
- **Régularisation Norme $L^p$ :** L'inégalité de Minkowski garantit que les normes $L^p$ (comme Lasso avec $p=1$ ou Ridge avec $p=2$) définissent des ensembles de contraintes convexes, garantissant l'existence d'un minimum global unique pour les problèmes strictement convexes.
