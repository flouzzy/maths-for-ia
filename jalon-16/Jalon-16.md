---
uuid: "jalon-16"
title: "Séries numériques à termes positifs, critères de comparaison, de d'Alembert et de Cauchy"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/sommation-infinie
prev: "[[Jalon 15 (Sous-suites).md]]"
next: "[[Jalon 17 (Séries absolument convergentes).md]]"
---
# Jalon 16 : Séries numériques à termes positifs, critères de comparaison, de d'Alembert et de Cauchy

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez que vous voulez construire une tour infiniment haute avec des briques de plus en plus fines. Si la première brique fait 1 mètre, la deuxième 50 cm, la troisième 25 cm, et ainsi de suite (on divise par 2 à chaque fois), votre tour ne dépassera jamais les 2 mètres de haut, même si vous ajoutez une infinité de briques ! C'est ce qu'on appelle une **série convergente**. Par contre, si vous ajoutez des briques de taille constante, ou même des briques qui diminuent trop lentement (comme 1/2, 1/3, 1/4...), votre tour finira par toucher les étoiles. C'est une **série divergente**.
- **Le "Pourquoi on a inventé ça" :** On a souvent besoin d'additionner une infinité de petites contributions (en probabilités, en physique, ou pour calculer des aires). Les critères de convergence sont les "tests de sécurité" qui nous disent si le total final est un nombre bien précis ou s'il explose vers l'infini.
- **Visualisation :** Imaginez un sablier. Si les grains de sable tombent de plus en plus lentement selon une règle mathématique précise, le tas de sable dans le réceptacle peut se stabiliser à une hauteur finie.

## 2. Formalisation
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $(u_n)_{n \in \mathbb{N}}$ une suite réelle.
1. **Série numérique :** On appelle série de terme général $u_n$ la suite $(S_N)_{N \in \mathbb{N}}$ des sommes partielles définie par $S_N = \sum_{n=0}^N u_n$.
2. **Convergence :** La série $\sum u_n$ converge si la suite $(S_N)$ admet une limite finie $S = \sum_{n=0}^\infty u_n$.
3. **Série à termes positifs :** $\forall n \in \mathbb{N}, u_n \ge 0$. Dans ce cas, la suite $(S_N)$ est croissante. Elle converge si et seulement si elle est majorée.

### B. Théorèmes, Propositions & Lemmes
> **Critère de Comparaison :**
> Soient $0 \le u_n \le v_n$ à partir d'un certain rang.
> - Si $\sum v_n$ converge, alors $\sum u_n$ converge.
> - Si $\sum u_n$ diverge, alors $\sum v_n$ diverge.

> **Règle de d'Alembert :**
> Soit $u_n > 0$. Si $\lim_{n \to \infty} \frac{u_{n+1}}{u_n} = L$ :
> - Si $L < 1$, la série converge.
> - Si $L > 1$, la série diverge.
> - Si $L = 1$, on ne peut pas conclure.

> **Règle de Cauchy :**
> Soit $u_n \ge 0$. Si $\lim_{n \to \infty} \sqrt[n]{u_n} = L$ :
> - Si $L < 1$, la série converge.
> - Si $L > 1$, la série diverge.

## 3. Démonstrations
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Convergence de la série géométrique $\sum q^n$ pour $0 \le q < 1$
Démontrons que la somme partielle converge et calculons sa limite.

1. **Initialisation / Cadre :** Soit $S_N = \sum_{n=0}^N q^n = 1 + q + q^2 + ... + q^N$.
   Nous supposons $q \in [0, 1[$.

2. **Étape 1 : Astuce algébrique (télescopage)**
   Calculons $S_N - q S_N$ :
   $$S_N = 1 + q + q^2 + \dots + q^N$$
   $$q S_N = q + q^2 + \dots + q^N + q^{N+1}$$
   $$(1-q) S_N = (1 + q + \dots + q^N) - (q + q^2 + \dots + q^{N+1})$$
   Tous les termes centraux s'annulent (somme télescopique) :
   $$(1-q) S_N = 1 - q^{N+1}$$

3. **Étape 2 : Expression de la somme partielle**
   Puisque $q < 1$, alors $1-q \neq 0$. On peut diviser :
   $$S_N = \frac{1 - q^{N+1}}{1 - q}$$

4. **Étape 3 : Passage à la limite**
   Étudions la limite de $q^{N+1}$ quand $N \to \infty$.
   Comme $|q| < 1$, par les propriétés des suites géométriques, $\lim_{N \to \infty} q^{N+1} = 0$.
   Ainsi :
   $$\lim_{N \to \infty} S_N = \lim_{N \to \infty} \frac{1 - q^{N+1}}{1 - q} = \frac{1 - 0}{1 - q}$$

5. **Conclusion :**
   La série $\sum q^n$ converge et sa somme est :
   $$\sum_{n=0}^\infty q^n = \frac{1}{1 - q}$$

## 4. Exercices d'Application
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Application de la règle de d'Alembert
**Énoncé :** Étudier la convergence de la série $\sum \frac{n^2}{2^n}$.
**Correction Détaillée :**
1. Posons $u_n = \frac{n^2}{2^n}$. On a $u_n > 0$.
2. Calculons le rapport $\frac{u_{n+1}}{u_n}$ :
   $$\frac{u_{n+1}}{u_n} = \frac{(n+1)^2}{2^{n+1}} \times \frac{2^n}{n^2} = \frac{(n+1)^2}{n^2} \times \frac{2^n}{2^{n+1}} = \left( \frac{n+1}{n} \right)^2 \times \frac{1}{2}.$$
3. $$\frac{u_{n+1}}{u_n} = \left( 1 + \frac{1}{n} \right)^2 \times \frac{1}{2}.$$
4. Étudions la limite : $\lim_{n \to \infty} (1 + 1/n) = 1$, donc $\lim_{n \to \infty} (1 + 1/n)^2 = 1^2 = 1$.
5. On en déduit $\lim_{n \to \infty} \frac{u_{n+1}}{u_n} = 1 \times \frac{1}{2} = \frac{1}{2}$.
6. Comme $L = 1/2 < 1$, d'après le critère de d'Alembert, la série converge.
**Conclusion :** La série $\sum \frac{n^2}{2^n}$ est convergente.

### Exercice 2 : Niveau Avancé (Série de Riemann et comparaison)
**Énoncé :** Étudier la convergence de $\sum \frac{1}{n^2 + \sqrt{n}}$.
**Correction Détaillée :**
1. Terme général $u_n = \frac{1}{n^2 + \sqrt{n}}$. Il est positif.
2. Cherchons un équivalent ou une majoration simple.
3. Pour tout $n \ge 1$, $n^2 + \sqrt{n} > n^2$.
4. En prenant l'inverse (la fonction $x \mapsto 1/x$ est décroissante sur $\mathbb{R}^{+*}$) :
   $$0 < \frac{1}{n^2 + \sqrt{n}} < \frac{1}{n^2}.$$
5. Or la série $\sum \frac{1}{n^2}$ est une série de Riemann de paramètre $\alpha = 2$.
6. Comme $\alpha > 1$, la série $\sum \frac{1}{n^2}$ converge.
7. Par le critère de comparaison des séries à termes positifs, la série $\sum u_n$ est majorée par une série convergente.
**Conclusion :** La série $\sum \frac{1}{n^2 + \sqrt{n}}$ converge.

## 5. Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** En IA, les séries numériques apparaissent dans le calcul des **Espérances** (moyennes pondérées) pour des variables aléatoires discrètes infinies (comme la loi de Poisson). Elles servent aussi à définir les **Fonctions d'Activation** par leurs développements en série (ex: Softmax, Sigmoïde).
- **Exemple Concret :** Dans l'**Apprentissage par Renforcement (Reinforcement Learning)**, on calcule la "Récompense Totale Escomptée" (Discounted Return) : $G = \sum_{t=0}^\infty \gamma^t R_{t+1}$. Ici, $\gamma$ est un facteur d'escompte compris entre 0 et 1. C'est exactement une **série géométrique** pondérée par les récompenses $R_t$. La convergence de cette série (garantie par $\gamma < 1$) est ce qui permet à l'agent de ne pas avoir une récompense infinie, rendant ainsi le problème d'optimisation mathématiquement bien posé.

## 6. Liens Sémantiques
- **Concepts Précédents requis :** [[Jalon 13 (Structure de R)]], [[Jalon 14 (Suites réelles et complexes)]]
- **Concepts Futurs dépendants :** [[Jalon 17 (Séries absolument convergentes)]], [[Jalon 22 (Séries de fonctions)]], [[Jalon 23 (Séries entières)]], [[Jalon 85 (Axiomes de Kolmogorov)]]
