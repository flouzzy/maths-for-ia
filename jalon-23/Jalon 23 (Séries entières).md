---
uuid: "jalon-23"
title: "Séries entières, calcul du rayon de convergence (règle de d'Alembert-Cauchy) et propriétés de la somme"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/modelisation-analytique
prev: "[[Jalon 22 (Séries de fonctions).md]]"
next: "[[Jalon 24 (Livrable IA).md]]"
---

# Jalon 23 : Séries entières, calcul du rayon de convergence (règle de d'Alembert-Cauchy) et propriétés de la somme

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez un élastique magique attaché à l'origine (zéro). Vous pouvez tirer cet élastique vers la gauche ou la droite. Les **Séries entières**, ce sont comme des polynômes qui n'en finissent jamais (de degré infini). La "magie" de l'élastique, c'est le **Rayon de Convergence** : c'est la distance maximale jusqu'où vous pouvez tirer l'élastique sans qu'il ne casse (sans que la somme ne devienne infinie). À l'intérieur de cette distance, tout est lisse et parfait. À l'extérieur, tout explose.
- **Le "Pourquoi on a inventé ça" :** Parfois, on connaît une règle simple pour passer d'un terme au suivant, mais on ne sait pas calculer la valeur finale. Les séries entières permettent de définir de nouvelles fonctions très complexes (comme l'exponentielle ou le sinus) à partir de règles de multiplication très simples. C'est l'outil qui fait le pont entre l'algèbre (calculer des puissances) et l'analyse (étudier des courbes).
- **Visualisation :** Imaginez un disque de lumière sur un plan. À l'intérieur du disque, l'image est nette et détaillée. Dès que vous sortez du disque, l'image devient blanche et saturée (elle diverge). Le rayon de ce disque est le rayon de convergence.

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $(a_n)_{n \in \mathbb{N}}$ une suite de complexes.
1. **Série Entière :** On appelle série entière de la variable complexe $z$, la série de fonctions $\sum a_n z^n$.
2. **Rayon de Convergence ($R$) :** Il existe un unique $R \in [0, +\infty] \cup \{+\infty\}$ tel que :
   - Si $|z| < R$, la série converge absolument.
   - Si $|z| > R$, la série diverge grossièrement.
   L'ensemble $\{ z \in \mathbb{C} \mid |z| < R \}$ est appelé **disque ouvert de convergence**.
3. **Disque de Convergence :** Sur tout segment inclus dans $]-R, R[$, la série entière converge normalement.

### B. Théorèmes, Propositions & Lemmes
> **Lemme d'Abel (Pivot) :**
> S'il existe $z_0 \neq 0$ tel que la suite $(a_n z_0^n)$ est bornée, alors pour tout $z$ tel que $|z| < |z_0|$, la série $\sum a_n z^n$ converge absolument.

> **Règle de d'Alembert (pour le rayon) :**
> Si $\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = L \in [0, +\infty]$, alors le rayon de convergence est $R = \frac{1}{L}$ (avec $1/0 = \infty$ et $1/\infty = 0$).

> **Propriétés de la somme :**
> À l'intérieur du disque de convergence, la fonction $S(z) = \sum_{n=0}^\infty a_n z^n$ est de classe $C^\infty$. On peut la dériver et l'intégrer terme à terme, et le rayon de convergence reste le même.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : La dérivation terme à terme conserve le rayon de convergence
Soit $\sum a_n z^n$ de rayon $R$. Montrons que la série dérivée $\sum n a_n z^{n-1}$ a le même rayon de convergence $R'$.

1. **Initialisation / Cadre :** 
   Soit $R$ le rayon de $\sum a_n z^n$ et $R'$ celui de $\sum (n+1) a_{n+1} z^n$ (qui est la même que la dérivée, à un décalage d'indice près).
   Rappelons que $R = \sup \{ |z| \mid (a_n z^n) \text{ est bornée} \}$.

2. **Étape 1 : Comparaison des termes généraux**
   Pour tout $z \neq 0$ :
   $|a_n z^n| = \frac{1}{n} |n a_n z^n| = \frac{|z|}{n} |n a_n z^{n-1}|$.
   Si la série dérivée converge en $z$, alors son terme général $n a_n z^{n-1}$ tend vers 0, donc il est borné.
   Alors $|a_n z^n|$ est aussi borné (car $\frac{|z|}{n} \to 0$).
   Par définition du rayon, cela implique $|z| \le R$.
   Ceci étant vrai pour tout $z$ où la dérivée converge, on a $R' \le R$.

3. **Étape 2 : L'autre sens (utilisation d'un point intermédiaire)**
   Soit $z$ tel que $|z| < R$. Choisissons $r$ tel que $|z| < r < R$.
   Comme $r < R$, la série $\sum a_n r^n$ converge absolument, donc son terme général est borné : $|a_n r^n| \le M$.
   Ecrivons le terme de la série dérivée :
   $|n a_n z^{n-1}| = \frac{n}{|z|} |a_n z^n| = \frac{n}{|z|} |a_n r^n| \left| \frac{z}{r} \right|^n$.
   En utilisant la borne $M$ :
   $$|n a_n z^{n-1}| \le \frac{M}{|z|} n \left| \frac{z}{r} \right|^n$$

4. **Étape 3 : Convergence de la majorante**
   Posons $q = |z/r|$. Comme $|z| < r$, on a $q < 1$.
   La série $\sum n q^n$ est une série géométrique dérivée. Elle converge car $q < 1$ (critère de d'Alembert : $\frac{(n+1)q^{n+1}}{nq^n} = \frac{n+1}{n} q \to q < 1$).
   Par comparaison, la série $\sum n a_n z^{n-1}$ converge absolument.
   Ceci étant vrai pour tout $|z| < R$, on a $R \le R'$.

5. **Conclusion :**
   Par double inégalité $R' \le R$ et $R \le R'$, on en déduit $R = R'$. La dérivation ne change pas le domaine de convergence.

## 4. Exercices d'Application & Pratique de Concours
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Calcul de rayon de convergence
**Énoncé :** Déterminer le rayon de convergence de la série $\sum_{n=1}^\infty \frac{(-1)^n}{n 3^n} z^{2n}$.
**Correction Détaillée :**
1. Posons $u_n(z) = a_n z^{2n}$ avec $a_n = \frac{(-1)^n}{n 3^n}$.
2. Utilisons le critère de d'Alembert sur la série numérique $\sum |u_n(z)|$ :
   $\left| \frac{u_{n+1}(z)}{u_n(z)} \right| = \left| \frac{z^{2(n+1)}}{(n+1) 3^{n+1}} \times \frac{n 3^n}{z^{2n}} \right|$.
3. Simplifions :
   $\left| \frac{u_{n+1}(z)}{u_n(z)} \right| = |z|^2 \times \frac{n}{n+1} \times \frac{3^n}{3^{n+1}} = |z|^2 \times \frac{n}{n+1} \times \frac{1}{3}$.
4. Passage à la limite :
   $\lim_{n \to \infty} \left| \frac{u_{n+1}(z)}{u_n(z)} \right| = \frac{|z|^2}{3} \times 1 = \frac{|z|^2}{3}$.
5. La série converge si $\frac{|z|^2}{3} < 1$, soit $|z|^2 < 3$, d'où $|z| < \sqrt{3}$.
**Conclusion :** Le rayon de convergence est $R = \sqrt{3}$.

### Exercice 2 : Niveau Avancé (Développement en série entière)
**Énoncé :** Développer en série entière la fonction $f(x) = \frac{1}{(1-x)^2}$ et préciser le rayon.
**Correction Détaillée :**
1. On connaît le développement de la série géométrique : $\frac{1}{1-x} = \sum_{n=0}^\infty x^n$ pour $|x| < 1$.
2. On remarque que $f(x)$ est la dérivée de $g(x) = \frac{1}{1-x}$.
   - En effet, $g'(x) = - \frac{-1}{(1-x)^2} = \frac{1}{(1-x)^2} = f(x)$.
3. D'après le théorème de dérivation terme à terme :
   $f(x) = \frac{d}{dx} \left( \sum_{n=0}^\infty x^n \right) = \sum_{n=0}^\infty \frac{d}{dx}(x^n)$.
4. Calculons la dérivée :
   - Pour $n=0$, la dérivée est 0.
   - Pour $n \ge 1$, $(x^n)' = nx^{n-1}$.
5. On obtient : $f(x) = \sum_{n=1}^\infty n x^{n-1}$.
6. Par décalage d'indice $k = n-1$ : $f(x) = \sum_{k=0}^\infty (k+1) x^k$.
**Conclusion :** $\frac{1}{(1-x)^2} = \sum_{n=0}^\infty (n+1) x^n$ avec un rayon $R = 1$.

## 5. Ancrage & Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** Les séries entières sont la base de la définition des **Fonctions Génératrices** en combinatoire et en probabilités. Elles permettent de manipuler des distributions de données discrètes comme des objets analytiques continus.
- **Exemple Concret :** Dans la modélisation des **Graphes Aléatoires** et des **Réseaux de Neurones à Largeur Infinie (Infinite Width limits)**, on utilise les séries entières pour calculer les moments d'une distribution de poids. De plus, les **Noyaux (Kernels)** utilisés en machine learning (comme le noyau RBF/Gaussien) peuvent être vus comme des séries entières de produits scalaires. Comprendre le rayon de convergence de ces séries permet de savoir pour quelles plages de données le modèle reste stable et mathématiquement prévisible.

## 6. Liens Sémantiques & Maillage Obsidian
- **Concepts Précédents requis :** [[Jalon 16 (Séries numériques à termes positifs)]], [[Jalon 22 (Séries de fonctions)]]
- **Concepts Futurs dépendants :** [[Jalon 24 (Livrable IA)]], [[Jalon 31 (Introduction à la réduction de Jordan et structure des nilpotents.)]], [[Jalon 43 (Systèmes différentiels linéaires d'ordre 1 et calcul de l'exponentielle de matrice.)]], [[Jalon 93 (Fonctions caractéristiques)]]
