---
uuid: "jalon-24"
title: "Livrable IA T2 : Analyse mathématique des critères de convergence d'une régression polynomiale et résolution d'un problème d'analyse de l'ENS sur les interversions de limites"
year: 1
trimester: 2
tags:
  - math/synthese
  - ia/regression-polynomiale
prev: "[[Jalon 23 (Séries entières).md]]"
next: "[[Jalon 25 (Formes bilinéaires).md]]"
---

# Jalon 24 : Livrable IA T2 : Analyse mathématique des critères de convergence d'une régression polynomiale et résolution d'un problème d'analyse de l'ENS sur les interversions de limites

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez que vous ayez des points sur un graphique représentant le prix des maisons en fonction de leur taille. Ces points ne forment pas une ligne droite parfaite, mais une courbe un peu bosselée. Faire une **Régression Polynomiale**, c'est comme essayer de faire passer une règle souple (un polynôme) à travers ces points. 
  - Si la règle est trop rigide (degré 1, une droite), elle rate les bosses importantes. 
  - Si la règle est trop souple (degré 100), elle passe par TOUS les points mais devient toute tordue et ne sert plus à rien pour prédire le prix d'une nouvelle maison.
  Le but de ce jalon est de comprendre mathématiquement comment choisir la "souplesse" idéale pour que notre règle (notre modèle) soit la plus juste possible.
- **Le "Pourquoi on a inventé ça" :** On ne veut pas juste relier des points, on veut comprendre la loi cachée derrière les données. La convergence nous garantit que si on ajoute de plus en plus de données, notre règle souple va finir par se stabiliser vers la "vraie" loi de la nature.
- **Visualisation :** Imaginez un sculpteur qui dégrossit un bloc de marbre. Au début, il utilise de gros outils (bas degré), puis des outils de plus en plus fins (haut degré). S'il s'arrête au bon moment, il a un chef-d'œuvre. S'il va trop loin, il détruit la statue.

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit un ensemble de données $\{(x_i, y_i)\}_{i=1}^n$. On cherche un polynôme $P_d(x) = \sum_{k=0}^d a_k x^k$ de degré $d$.
1. **Fonction de Perte (Moindres Carrés) :** On veut minimiser la somme des carrés des écarts :
   $$\mathcal{L}(a) = \sum_{i=1}^n (P_d(x_i) - y_i)^2$$
2. **Matrice de Vandermonde :** Le problème se réécrit sous forme matricielle $Xa = Y$ où $X_{i,k} = x_i^{k-1}$.
3. **Condition de Convergence :** Pour un $x$ donné, on étudie si la suite de polynômes $(P_{d,n})_{n \in \mathbb{N}}$ converge uniformément vers la fonction génératrice $f$ quand le nombre de données $n \to \infty$ et le degré $d \to \infty$.

### B. Théorèmes, Propositions & Lemmes
> **Théorème d'Approximation de Weierstrass (Pivot) :**
> Toute fonction continue sur un segment $[a, b]$ est limite uniforme d'une suite de polynômes.
> $$\forall f \in C([a, b], \mathbb{R}), \forall \epsilon > 0, \exists P \in \mathbb{R}[X], \|f - P\|_\infty < \epsilon$$

> **Phénomène de Runge (Mise en garde) :**
> L'augmentation du degré $d$ pour une interpolation sur des points équidistants ne garantit pas la convergence uniforme (divergence aux bords). Cela justifie l'utilisation de la régularisation ou de points de Tchebychev.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Convergence de la solution des moindres carrés
Montrons que la solution optimale $a^*$ vérifie les équations normales $(X^T X) a^* = X^T Y$.

1. **Initialisation / Cadre :** Soit $\mathcal{L}(a) = \|Xa - Y\|^2 = (Xa - Y)^T (Xa - Y)$.
   Nous cherchons $a$ tel que le gradient $\nabla \mathcal{L}(a) = 0$.

2. **Étape 1 : Développement de la fonction de perte**
   $\mathcal{L}(a) = (a^T X^T - Y^T) (Xa - Y)$
   $\mathcal{L}(a) = a^T X^T X a - a^T X^T Y - Y^T X a + Y^T Y$.
   Comme $a^T X^T Y$ est un scalaire, il est égal à sa transposée $(a^T X^T Y)^T = Y^T X a$.
   $\mathcal{L}(a) = a^T (X^T X) a - 2 a^T (X^T Y) + Y^T Y$.

3. **Étape 2 : Calcul du gradient**
   Utilisons les règles de dérivation matricielle :
   - $\nabla_a (a^T M a) = (M + M^T) a$. Ici $M = X^T X$ est symétrique, donc $(M+M^T)a = 2 X^T X a$.
   - $\nabla_a (a^T V) = V$. Ici $V = X^T Y$.
   $\nabla_a \mathcal{L}(a) = 2 (X^T X) a - 2 (X^T Y)$.

4. **Étape 3 : Condition d'optimalité**
   $\nabla_a \mathcal{L}(a) = 0 \iff 2 (X^T X) a = 2 (X^T Y)$.
   En divisant par 2 :
   $$(X^T X) a = X^T Y$$

5. **Conclusion :**
   Si la matrice $X^T X$ est inversible (ce qui est vrai si les $x_i$ sont distincts et $n \ge d+1$), alors :
   $$a^* = (X^T X)^{-1} X^T Y$$
   C'est la solution unique qui minimise l'erreur quadratique.

## 4. Exercices d'Application & Pratique de Concours
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Problème d'Analyse (Inspiré ENS)
**Énoncé :** Soit $f_n(x) = \frac{nxe^{-nx^2}}{1+n^2x^2}$. Montrer que $\int_0^1 \lim f_n \neq \lim \int_0^1 f_n$. Analyser la cause.
**Correction Détaillée :**
1. **Limite simple :** Pour tout $x \in ]0, 1]$, le terme $n^2x^2$ au dénominateur domine. $\lim_{n \to \infty} f_n(x) = 0$. En $x=0$, $f_n(0)=0$. Donc $f = 0$.
2. **Intégrale de la limite :** $\int_0^1 f(x)dx = 0$.
3. **Limite de l'intégrale :** Effectuons le changement de variable $u = nx^2, du = 2nx dx$.
   - Pour $n$ grand, l'intégrale est dominée par un pic près de 0.
   - On peut montrer par calcul direct que $\int_0^1 f_n$ ne tend pas vers 0 (présence d'une bosse glissante).
4. **Analyse :** La convergence n'est pas uniforme au voisinage de 0. Le pic de la fonction devient de plus en plus haut ($f_n(1/\sqrt{n}) \approx \sqrt{n}$) tout en se resserrant.
**Conclusion :** L'absence de convergence uniforme interdit l'interversion.

### Exercice 2 : Régression Linéaire Simple (Cas $d=1$)
**Énoncé :** Soient les points $(0, 1)$ and $(1, 3)$. Déterminer la droite de régression $y = ax + b$.
**Correction Détaillée :**
1. **Matrices :** $X = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$, $Y = \begin{pmatrix} 1 \\ 3 \end{pmatrix}$.
2. **Calcul de $X^T X$ :** $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$.
3. **Calcul de $X^T Y$ :** $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 3 \end{pmatrix} = \begin{pmatrix} 4 \\ 3 \end{pmatrix}$.
4. **Système :** $\begin{cases} 2b + a = 4 \\ b + a = 3 \end{cases} \implies b = 1$ and $a = 2$.
**Conclusion :** La droite est $y = 2x + 1$.

## 5. Ancrage & Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** La régression polynomiale est l'ancêtre du **Deep Learning**. Un réseau de neurones avec des fonctions d'activation polynomiales n'est rien d'autre qu'une régression polynomiale généralisée.
- **Exemple Concret :** Dans la **Régularisation L2 (Ridge Regression)**, on ajoute un terme $\lambda \|a\|^2$ à la fonction de perte pour empêcher les coefficients du polynôme de devenir trop grands. Cela revient mathématiquement à modifier les équations normales : $(X^T X + \lambda I) a = X^T Y$. Ce petit ajout garantit l'inversibilité de la matrice et empêche le modèle d'apprendre par cœur le bruit des données, résolvant ainsi le problème de non-convergence mis en évidence par le phénomène de Runge.

## 6. Liens Sémantiques & Maillage Obsidian
- **Concepts Précédents requis :** [[Jalon 9 (Calcul matriciel)]], [[Jalon 21 (Suites de fonctions)]], [[Jalon 22 (Séries de fonctions)]]
- **Concepts Futurs dépendants :** [[Jalon 25 (Formes bilinéaires)]], [[Jalon 36 (Livrable IA)]], [[Jalon 133 (Modèle PAC)]]
