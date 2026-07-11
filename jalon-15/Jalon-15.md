---
uuid: "jalon-15"
title: "Sous-suites, valeurs d'adhérence et preuve par séparation du théorème de Bolzano-Weierstrass"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/compacite
prev: "[[Jalon-14.md]]"
next: "[[Jalon-16.md]]"
---
# Jalon 15 : Sous-suites, valeurs d'adhérence et preuve par séparation du théorème de Bolzano-Weierstrass

## 1. Genèse et Exégèse Conceptuelle

Historiquement, l'appréhension du continu et des limites a longtemps été freinée par des suites au comportement d'apparence chaotique, refusant obstinément de converger vers une limite unique. L'idée de sous-suite émerge alors comme un filtre cognitif, une extraction chirurgicale de l'ordre au sein du désordre. Si l'on imagine une foule dont la trajectoire globale semble erratique, le mathématicien, tel un observateur sélectif, choisira de ne fixer son attention que sur une sous-population spécifique. Bien que la dynamique globale fuie toute stabilisation, la trajectoire extraite révélera souvent une destination précise. C'est ici qu'intervient la puissance fondatrice du théorème de Bolzano-Weierstrass, assurant que dans un espace confiné (borné), l'infinité de l'accumulation force invariablement une convergence partielle. Cette notion est l'infrastructure même de la compacité, indispensable pour garantir l'existence de solutions à des problèmes d'optimisation.

## 2. Énoncé Symbolique et Typage Chirurgical

### A. Anatomie des Définitions Formelles
Soit $E$ un espace vectoriel normé (typiquement $\mathbb{R}$ ou $\mathbb{C}$) et soit $(u_n)_{n \in \mathbb{N}} \in E^{\mathbb{N}}$ une suite d'éléments de $E$.
1. **Extraction de Sous-suite :** Une suite $(v_k)_{k \in \mathbb{N}}$ est définie comme une *sous-suite* (ou *suite extraite*) de $(u_n)_{n \in \mathbb{N}}$ si et seulement s'il existe une application extractrice $\phi : \mathbb{N} \to \mathbb{N}$ qui est **strictement croissante** (c'est-à-dire $\forall k \in \mathbb{N}, \phi(k+1) > \phi(k)$) telle que pour tout entier naturel $k \in \mathbb{N}, v_k = u_{\phi(k)}$. L'application $\phi$ sélectionne les indices conservés tout en préservant leur ordre chronologique.
2. **Valeur d'Adhérence (Point d'Accumulation) :** Un scalaire $a \in E$ est qualifié de *valeur d'adhérence* de la suite $(u_n)_{n \in \mathbb{N}}$ s'il existe une extractrice $\phi$ telle que la sous-suite $(u_{\phi(k)})_{k \in \mathbb{N}}$ converge vers $a$, soit $\lim_{k \to +\infty} u_{\phi(k)} = a$.
3. **Caractérisation Topologique Stricte :** Le scalaire $a$ est une valeur d'adhérence si et seulement si pour tout voisinage $V$ de $a$, il existe une infinité d'indices $n$ tels que $u_n \in V$. Formellement dans un espace métrique : $\forall \epsilon > 0, \forall N \in \mathbb{N}, \exists n \ge N, \|u_n - a\| < \epsilon$.

### B. Exemples de Validation et Contre-exemples
- **Exemple trivial de convergence absolue :** Si $(u_n)$ converge vers $L$, alors l'unique valeur d'adhérence de la suite est $L$, et toute sous-suite de $(u_n)$ converge vers $L$.
- **Exemple d'oscillation régulière :** La suite définie par $u_n = (-1)^n$ admet exactement deux valeurs d'adhérence: $\{-1, 1\}$.
- **Cas pathologique d'une suite non bornée dense :** L'énumération des rationnels dans $[0, 1]$ par une suite $(r_n)$ admet pour ensemble des valeurs d'adhérence l'intervalle $[0, 1]$ tout entier, illustrant un continuum d'adhérence.
- **Cas sans adhérence :** La suite $u_n = n$ diverge vers l'infini et ne possède aucune valeur d'adhérence dans $\mathbb{R}$ (elle s'échappe de tout compact).

### B. Théorèmes, Propositions & Lemmes
> **Théorème de Bolzano-Weierstrass :**
> De toute suite réelle bornée, on peut extraire une sous-suite convergente.
> (Plus généralement : Toute suite dans un ensemble compact admet au moins une valeur d'adhérence).

> **Lien avec la convergence :**
> Une suite bornée converge si et seulement si elle admet une unique valeur d'adhérence.

## 3. Démonstrations

### Démonstration du Théorème Pivot : Bolzano-Weierstrass par dichotomie (méthode de séparation)
Soit $(u_n)$ une suite réelle bornée. Montrons qu'il existe une sous-suite convergente.

1. **Initialisation / Cadre :** 
   - Puisque $(u_n)$ est bornée, il existe un intervalle $[a_0, b_0]$ tel que $\forall n \in \mathbb{N}, u_n \in [a_0, b_0]$.
   - Posons $I_0 = [a_0, b_0]$ et $L_0 = b_0 - a_0$.
   - Nous allons construire par récurrence une suite d'intervalles emboîtés $(I_k)_{k \in \mathbb{N}}$.

2. **Étape 1 : Construction par dichotomie**
   Supposons $I_k = [a_k, b_k]$ construit tel qu'il contient une infinité de termes de la suite $(u_n)$.
   - Soit $m_k = \frac{a_k + b_k}{2}$ le milieu de $I_k$.
   - L'intervalle $I_k$ est l'union de $[a_k, m_k]$ et $[m_k, b_k]$.
   - Puisque $I_k$ contient une infinité de termes, l'un au moins de ces deux sous-intervalles contient aussi une infinité de termes.
   - On choisit $I_{k+1} = [a_{k+1}, b_{k+1}]$ comme étant ce sous-intervalle (si les deux intervalles fermés contiennent une infinité de termes, nous sélectionnons de manière déterministe le sous-intervalle de gauche $[a_k, m_k]$ afin d'assurer l'unicité de la construction de la suite d'intervalles emboîtés).

3. **Étape 2 : Propriétés des suites $(a_k)$ et $(b_k)$**
   - Par construction, $a_k \le a_{k+1}$ (croissante) et $b_{k+1} \le b_k$ (décroissante).
   - De plus, $b_k - a_k = \frac{b_0 - a_0}{2^k} \to 0$ quand $k \to \infty$.
   - D'après le théorème des segments emboîtés, les suites $(a_k)$ et $(b_k)$ convergent vers une limite commune $l$.

4. **Étape 3 : Extraction de la sous-suite**
   - On définit $\phi(0) = 0$.
   - Pour chaque $k \ge 0$, on choisit $\phi(k+1)$ comme étant le plus petit entier tel que $\phi(k+1) > \phi(k)$ et $u_{\phi(k+1)} \in I_{k+1}$. Un tel entier existe car $I_{k+1}$ contient une infinité de termes.
   - On a alors, pour tout $k$ : $a_k \le u_{\phi(k)} \le b_k$.

5. **Conclusion :**
   - Par le théorème des gendarmes, comme $\lim a_k = l$ et $\lim b_k = l$, alors $\lim_{k \to \infty} u_{\phi(k)} = l$.
   - Nous avons extrait une sous-suite convergente. Le théorème est démontré.

## 4. Exercices d'Application

### Exercice 1 : Application Directe (Valeurs d'adhérence)
**Énoncé :** Déterminer les valeurs d'adhérence de la suite $u_n = \sin(n \frac{\pi}{2})$.
**Correction Détaillée :**
1. Étudions les premiers termes :
   - $n=0 \implies \sin(0) = 0$
   - $n=1 \implies \sin(\pi/2) = 1$
   - $n=2 \implies \sin(\pi) = 0$
   - $n=3 \implies \sin(3\pi/2) = -1$
   - $n=4 \implies \sin(2\pi) = 0$ (Cycle de période 4).
2. Définissons des extractions :
   - Pour $n = 2k$ : $u_{2k} = \sin(k\pi) = 0$. La sous-suite $(u_{2k})$ converge vers $0$.
   - Pour $n = 4k+1$ : $u_{4k+1} = \sin(2k\pi + \pi/2) = 1$. La sous-suite $(u_{4k+1})$ converge vers $1$.
   - Pour $n = 4k+3$ : $u_{4k+3} = \sin(2k\pi + 3\pi/2) = -1$. La sous-suite $(u_{4k+3})$ converge vers $-1$.
**Conclusion :** Les valeurs d'adhérence sont $\{ -1, 0, 1 \}$.

### Exercice 2 : Niveau Avancé (Densité)
**Énoncé :** Montrer que l'ensemble des valeurs d'adhérence de la suite $u_n = \cos(n)$ est l'intervalle $[-1, 1]$ tout entier. (Admettre que $\mathbb{Z} + 2\pi\mathbb{Z}$ est dense dans $\mathbb{R}$).
**Correction Détaillée :**
1. Soit $l \in [-1, 1]$. Il existe $\theta \in \mathbb{R}$ tel que $\cos(\theta) = l$.
2. Par densité de $\mathbb{Z} + 2\pi\mathbb{Z}$, pour tout $\epsilon > 0$, il existe $n \in \mathbb{Z}$ et $k \in \mathbb{Z}$ tels que $|n - 2\pi k - \theta| < \epsilon$.
3. Comme la fonction $\cos$ est 1-lipschitzienne ($|\cos(x)-\cos(y)| \le |x-y|$), on a :
   $|\cos(n - 2\pi k) - \cos(\theta)| \le |n - 2\pi k - \theta| < \epsilon$.
4. Or $\cos(n - 2\pi k) = \cos(n)$.
5. Donc $|\cos(n) - l| < \epsilon$. Comme on peut trouver de tels $n$ arbitrairement grands (par la structure de groupe dense), $l$ est une valeur d'adhérence.
**Conclusion :** Chaque point de $[-1, 1]$ est limite d'une sous-suite de $\cos(n)$.

## 5. Application en Intelligence Artificielle
- **Le Pont Théorique :** Le concept de compacité (Bolzano-Weierstrass) est crucial pour garantir l'**existence d'un optimum**. Si on cherche à minimiser une erreur dans un espace de paramètres borné et fermé, Bolzano-Weierstrass nous assure qu'il y a au moins un point d'accumulation où l'erreur est minimale.
- **Exemple Concret :** Dans l'**Initialisation des Poids** des réseaux de neurones, on veut éviter que les signaux ne s'évaporent (Vanishing Gradient) ou n'explosent (Exploding Gradient). On s'assure que la suite des activations à travers les couches reste dans un ensemble compact. Sans cette garantie, l'algorithme d'apprentissage pourrait "diverger" vers l'infini sans jamais rencontrer de valeur d'adhérence (solution stable), rendant l'entraînement impossible.

## 6. Liens Sémantiques
- **Concepts Précédents requis :** [[Jalon 14 (Suites réelles et complexes)]]
- **Concepts Futurs dépendants :** [[Jalon 35 (Caractérisation séquentielle des ouverts)]], [[Jalon 54 (Compacité générale)]], [[Jalon 129 (Optimisation stochastique)]]
