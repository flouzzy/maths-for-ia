---
uuid: "jalon-23"
title: "Séries entières, calcul du rayon de convergence (règle de d'Alembert-Cauchy) et propriétés de la somme"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/modelisation-analytique
prev: "[[Jalon-22.md]]"
next: "[[Jalon-24.md]]"
---

# Jalon 23 : Séries entières, calcul du rayon de convergence et propriétés de la somme

## 1. Genèse et Motivation : L'Échafaudage Cognitif

Historiquement, l'étude des séries entières est née de la volonté d'étendre la notion de polynôme, objet algébrique maniable par excellence, à une infinité de termes. Les mathématiciens du XVIIe et XVIIIe siècle, tels que Newton, Taylor, ou Euler, cherchaient à représenter des fonctions transcendantes (comme le sinus, le cosinus, ou l'exponentielle) à l'aide d'outils simples : l'addition et la multiplication. L'idée est vertigineuse : une fonction, aussi complexe soit-elle, pourrait être décrite localement comme une somme infinie de puissances.

Cependant, une somme infinie ne se comporte pas toujours de manière docile. Contrairement à un polynôme évalué en n'importe quel point réel ou complexe, une série infinie peut diverger, s'échapper vers l'infini. Il fallait donc délimiter un "domaine de validité", une zone de sécurité où la série se comporte raisonnablement. C'est ici qu'intervient la notion cruciale de **rayon de convergence**. Imaginez un disque centré à l'origine dans le plan complexe : à l'intérieur stricte de ce disque, la série converge de manière absolue (et même normale sur les compacts). Sur le bord, le comportement est incertain. À l'extérieur, c'est l'explosion, la divergence grossière.

Les séries entières constituent la clé de voûte de l'analyse analytique. Elles permettent non seulement de calculer des valeurs, mais aussi de résoudre des équations différentielles et de fonder rigoureusement la théorie des fonctions d'une variable complexe.

## 2. Formalisation et Exégèse Conceptuelle

### 2.1. Définition d'une série entière

**A. Énoncé Symbolique Strict :**
Soit $\mathbb{K}$ le corps $\mathbb{R}$ ou $\mathbb{C}$. On appelle série entière de la variable $z \in \mathbb{K}$ une série de fonctions de la forme $\sum a_n z^n$, où $(a_n)_{n \in \mathbb{N}}$ est une suite d'éléments de $\mathbb{K}$.

**B. Anatomie et Typage Chirurgical :**
- $\mathbb{K} \in \{\mathbb{R}, \mathbb{C}\}$ désigne le corps de base (réel ou complexe).
- $z \in \mathbb{K}$ est la variable libre.
- $(a_n)_{n \in \mathbb{N}} \in \mathbb{K}^{\mathbb{N}}$ est la suite des **coefficients** de la série entière.
- La notation $\sum a_n z^n$ désigne la série de fonctions $z \mapsto \sum_{n=0}^{+\infty} a_n z^n$. Le terme général pour un $z$ fixé est $u_n(z) = a_n z^n$.

**C. Exemples de Validation :**
- *Exemple trivial :* Si $a_n = 0$ pour tout $n > N$, la série entière est simplement un polynôme de degré au plus $N$. Elle converge pour tout $z \in \mathbb{K}$.
- *Exemple fondamental :* La série géométrique $\sum z^n$, où $a_n = 1$ pour tout $n \in \mathbb{N}$.

**D. Cas Pathologiques et Contre-exemples :**
La série $\sum n! z^n$ (où $a_n = n!$) croît si rapidement que pour tout $z \neq 0$, $|n! z^n| \to +\infty$. Elle ne converge qu'en $z = 0$.

### 2.2. Le Lemme d'Abel

Le Lemme d'Abel est le résultat fondateur qui structure le domaine de convergence d'une série entière.

**A. Énoncé Symbolique Strict :**
Soit $\sum a_n z^n$ une série entière. S'il existe un nombre $z_0 \in \mathbb{K}^*$ tel que la suite $(a_n z_0^n)_{n \in \mathbb{N}}$ soit bornée, alors pour tout $z \in \mathbb{K}$ vérifiant $|z| < |z_0|$, la série $\sum a_n z^n$ est absolument convergente. De plus, pour tout $0 < r < |z_0|$, la convergence est normale sur le disque fermé $\bar{D}(0, r)$.

**B. Anatomie et Typage Chirurgical :**
- $z_0 \in \mathbb{K}^*$ est un point d'évaluation non nul.
- La condition "la suite $(a_n z_0^n)_{n \in \mathbb{N}}$ est bornée" signifie qu'il existe $M > 0$ tel que pour tout $n \in \mathbb{N}$, $|a_n z_0^n| \leq M$.
- L'implication est forte : une condition faible (suite bornée en un point) entraîne une condition forte (convergence absolue) sur tout le disque ouvert de rayon $|z_0|$.

**C. Exemples de Validation :**
Pour $\sum z^n$, en choisissant $z_0 = 1$, la suite $(1^n)$ est constante égale à 1, donc bornée. Le lemme d'Abel assure la convergence absolue pour tout $z$ tel que $|z| < 1$.

**D. Cas Pathologiques :**
Le lemme d'Abel ne dit rien sur le comportement sur le cercle de rayon $|z_0|$ lui-même.

### 2.3. Rayon de Convergence

**A. Énoncé Symbolique Strict :**
Soit $\sum a_n z^n$ une série entière. On définit le rayon de convergence $R \in [0, +\infty]$ par :
$$ R = \sup \{ r \geq 0 \mid (a_n r^n)_{n \in \mathbb{N}} \text{ est bornée} \} $$

**B. Anatomie et Typage Chirurgical :**
- L'ensemble $E = \{ r \geq 0 \mid (a_n r^n) \text{ est bornée} \}$ contient toujours au moins $0$, il est donc non vide.
- Le suprémum (la plus petite borne supérieure) $R$ peut être fini (un réel positif) ou infini ($+\infty$ si $E = \mathbb{R}^+$).
- Conséquence directe du Lemme d'Abel :
  - Pour $|z| < R$, la série converge absolument.
  - Pour $|z| > R$, le terme général ne tend pas vers 0, la série diverge (grossièrement).

**C. Exemples de Validation :**
- Pour $\sum n! z^n$, $R = 0$.
- Pour $\sum z^n$, $(r^n)$ est bornée ssi $r \leq 1$. Donc $R = 1$.
- Pour $\sum \frac{z^n}{n!}$, $(r^n/n!) \to 0$ pour tout $r \geq 0$, donc la suite est bornée pour tout $r$. Ainsi $R = +\infty$.

**D. Cas Pathologiques :**
Le calcul de $R$ ne résout pas la question de la convergence pour $|z| = R$. Par exemple, $\sum z^n$ (diverge partout sur le cercle $|z|=1$), $\sum \frac{z^n}{n}$ (converge partout sur $|z|=1$ sauf en $z=1$), $\sum \frac{z^n}{n^2}$ (converge absolument partout sur $|z|=1$).

### 2.4. Calcul du Rayon : Règle de d'Alembert

**A. Énoncé Symbolique Strict :**
Soit $\sum a_n z^n$ une série entière telle que $a_n \neq 0$ à partir d'un certain rang. Si la limite suivante existe :
$$ \lim_{n \to +\infty} \left| \frac{a_{n+1}}{a_n} \right| = L \in [0, +\infty] $$
Alors le rayon de convergence $R$ est donné par :
$$ R = \frac{1}{L} $$
(avec les conventions $1/0 = +\infty$ et $1/+\infty = 0$).

**B. Anatomie et Typage Chirurgical :**
- $a_n$ sont les coefficients. La règle ne s'applique que si presque tous les $a_n$ sont non nuls pour pouvoir former le quotient.
- $L$ caractérise la croissance asymptotique des coefficients.

**C. Exemples de Validation :**
Pour $\sum \frac{z^n}{n!}$, on a $a_n = 1/n!$. Le quotient est $\left| \frac{1/(n+1)!}{1/n!} \right| = \frac{1}{n+1}$, qui tend vers $0 = L$. Donc $R = +\infty$.

**D. Cas Pathologiques :**
La série $\sum z^{2n}$ a ses coefficients de rang impair nuls, la règle de d'Alembert ne s'applique pas directement aux coefficients $a_n$. Il faut ruser (poser $Z = z^2$ ou utiliser le critère de Cauchy-Hadamard).

## 3. Démonstrations Complètes à Blanc

### Démonstration du Lemme d'Abel

Soit $\sum a_n z^n$ une série entière. Supposons qu'il existe $z_0 \in \mathbb{K}^*$ tel que la suite $(a_n z_0^n)_{n \in \mathbb{N}}$ soit bornée par $M > 0$.
Soit $z \in \mathbb{K}$ tel que $|z| < |z_0|$. Posons $q = \frac{|z|}{|z_0|}$. Puisque $|z| < |z_0|$, on a $0 \leq q < 1$.
Nous devons montrer que la série $\sum a_n z^n$ converge absolument, c'est-à-dire que $\sum |a_n z^n| < +\infty$.
Évaluons le terme général en valeur absolue :
$$ |a_n z^n| = |a_n z_0^n| \cdot \left| \frac{z}{z_0} \right|^n $$
Par hypothèse, $|a_n z_0^n| \leq M$, d'où :
$$ |a_n z^n| \leq M q^n $$
La série $\sum M q^n$ est une série géométrique de raison $q \in [0, 1[$, elle est donc convergente.
Par le théorème de comparaison des séries à termes positifs, la série $\sum |a_n z^n|$ converge.
Ainsi, la série $\sum a_n z^n$ est absolument convergente.

De plus, si on considère un réel $r$ tel que $0 < r < |z_0|$, pour tout $z \in \bar{D}(0, r)$ (donc $|z| \leq r$), on a :
$$ |a_n z^n| \leq |a_n| r^n = |a_n z_0^n| \left( \frac{r}{|z_0|} \right)^n \leq M \left( \frac{r}{|z_0|} \right)^n $$
La série géométrique de terme général $M (r/|z_0|)^n$ converge et est indépendante de $z$, ce qui prouve la convergence normale sur $\bar{D}(0, r)$.

### Démonstration de la Règle de d'Alembert

Soit $\sum a_n z^n$ une série entière avec $a_n \neq 0$ pour $n$ assez grand. Supposons que $\lim_{n \to +\infty} \left| \frac{a_{n+1}}{a_n} \right| = L$.
Pour un $z \in \mathbb{K}^*$ fixé, appliquons le critère de d'Alembert pour les séries numériques à la série $\sum |a_n z^n|$.
Le rapport de deux termes consécutifs est :
$$ \frac{|a_{n+1} z^{n+1}|}{|a_n z^n|} = \left| \frac{a_{n+1}}{a_n} \right| |z| $$
Par hypothèse, cette quantité tend vers $L |z|$ lorsque $n \to +\infty$.
- Premier cas : $0 < L < +\infty$.
  Si $L |z| < 1$, c'est-à-dire $|z| < \frac{1}{L}$, le critère de d'Alembert implique que la série $\sum |a_n z^n|$ converge.
  Si $L |z| > 1$, c'est-à-dire $|z| > \frac{1}{L}$, le critère implique que le terme général ne tend pas vers 0, donc la série diverge.
  Ceci caractérise exactement le rayon de convergence : $R = \frac{1}{L}$.
- Deuxième cas : $L = 0$.
  Pour tout $z \in \mathbb{K}$, la limite est $0 < 1$, donc la série converge absolument pour tout $z$. D'où $R = +\infty = 1/0$.
- Troisième cas : $L = +\infty$.
  Pour tout $z \neq 0$, la limite est $+\infty > 1$, la série diverge grossièrement. Elle ne converge qu'en $z = 0$. D'où $R = 0 = 1/+\infty$.

## 4. Propriétés de la Somme (Continuité et Dérivabilité)

À l'intérieur du disque ouvert de convergence, la somme d'une série entière se comporte de manière particulièrement lisse.

**A. Énoncé Symbolique Strict :**
Soit $\sum a_n z^n$ une série entière de rayon de convergence $R > 0$.
Soit $f : D(0, R) \to \mathbb{K}$ définie par $f(z) = \sum_{n=0}^{+\infty} a_n z^n$.
Alors :
1. $f$ est continue sur $D(0, R)$.
2. Si $\mathbb{K} = \mathbb{R}$, $f$ est indéfiniment dérivable (de classe $\mathcal{C}^\infty$) sur $]-R, R[$, et ses dérivées s'obtiennent par dérivation terme à terme :
   $$ f'(x) = \sum_{n=1}^{+\infty} n a_n x^{n-1} $$
   Le rayon de convergence de la série dérivée est également $R$.

**B. Anatomie et Typage Chirurgical :**
- La fonction somme $f$ hérite des propriétés des monômes $z^n$, car la convergence est "suffisamment forte" (normale sur tout compact inclus dans le disque ouvert).
- La dérivation terme à terme est une permutation légitime des limites $\frac{d}{dx}$ et $\sum_{n=0}^{+\infty}$, justifiée par la convergence uniforme de la série dérivée sur tout segment $[-r, r]$ pour $0 \leq r < R$.

*(Fin du cours magistral sur les séries entières).*
