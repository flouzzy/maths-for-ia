---
uuid: "jalon-132"
title: "Livrable IA T11 : Solveur proximal sous contraintes KKT pour le pruning"
year: 3
trimester: 11
tags:
  - math/optimisation-convexe
  - ia/pruning
prev: "[[Jalon 131 (Algorithmes d'optimisation de second ordre en grande dimension).md]]"
next: "[[Jalon 133 (Modèle PAC).md]]"
---

# Livrable IA T11 : Solveur Proximal sous Contraintes KKT pour l'Élagage Théorique de Réseaux Profonds

## 1. Présentation du concept clé
*Cette section rend le concept métaphorique sans utiliser de formalisme complexe.*

**La Métaphore du Sculpteur et du Tuteur :**
Imagine que tu es un sculpteur. Tu as devant toi un énorme bloc de glaise (notre réseau de neurones avec des millions de connexions), et on te donne deux consignes apparemment contradictoires.
La première : "Modèle une statue magnifique et précise" (c'est l'entraînement classique, on veut que le réseau performe bien).
La seconde : "Retire le maximum de matière, coupe tous les fils inutiles, pour que la statue tienne debout avec le strict minimum" (c'est l'élagage, ou *pruning*).
Et en prime, on te rajoute une règle stricte : "La statue ne doit pas dépasser une certaine hauteur exacte à cet endroit précis" (ce sont nos contraintes, comme des murs de verre autour de l'œuvre).

**Le "Pourquoi on a inventé ça" :**
Les intelligences artificielles modernes (comme ChatGPT ou Midjourney) sont gigantesques. Elles consomment énormément de mémoire et d'électricité. L'idée géniale des mathématiciens a été de se dire : "Ne peut-on pas couper 80% des connexions du "cerveau" de l'IA, sans qu'elle ne devienne bête ?". Pour y arriver de façon propre et mathématiquement garantie (sans faire ça au hasard), on utilise des outils appelés "opérateurs proximaux" et on s'assure qu'on respecte des règles de l'art très précises appelées "Conditions KKT".

**Visualisation :**
C'est comme descendre une montagne dans le brouillard en cherchant le point le plus bas (la descente de gradient), mais avec un sol gluant qui "tire" tes chaussures vers l'origine (l'opérateur proximal qui force les poids à s'annuler), tout en ayant des barrières infranchissables autour de toi (les contraintes KKT). À chaque pas, tu avances vers la vallée, puis un élastique géant (le proximal) te ramène violemment vers le zéro, "tuant" au passage les petits pas inutiles, te laissant sur un chemin minimaliste, juste au bord des barrières.

## 2. Formalisation
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles

**Cadre de l'espace hilbertien :**
Soit $\mathcal{H}$ un espace de Hilbert réel de dimension finie $d$, typiquement l'espace des paramètres $\mathbb{R}^d$ muni du produit scalaire canonique $\langle \cdot, \cdot \rangle$ et de la norme induite $\| \cdot \|_2$.

**Problème d'optimisation composite sous contraintes :**
Nous cherchons à minimiser une fonctionnelle objectif composite, modélisant le problème d'élagage (pruning) de réseaux de neurones, sous des contraintes d'inégalité et d'égalité :
$$ \min_{x \in \mathbb{R}^d} F(x) := f(x) + g(x) $$
Sous les contraintes :
$$ c_i(x) \leq 0, \quad \forall i \in \{1, \dots, m\} $$
$$ h_j(x) = 0, \quad \forall j \in \{1, \dots, p\} $$

Où :
- $f : \mathbb{R}^d \to \mathbb{R}$ est la **fonction de perte empirique** (Empirical Risk). Nous supposerons $f$ convexe, de classe $\mathcal{C}^1$, et de gradient $L$-lipschitzien : $\| \nabla f(x) - \nabla f(y) \|_2 \leq L \| x - y \|_2$ pour tout $x, y \in \mathbb{R}^d$.
- $g : \mathbb{R}^d \to \mathbb{R} \cup \{+\infty\}$ est la **fonction de régularisation non-lisse** (typiquement la norme $\ell_1$ pour induire la parcimonie, $g(x) = \lambda \|x\|_1$). On suppose $g$ convexe, propre et semi-continue inférieurement.
- $c_i : \mathbb{R}^d \to \mathbb{R}$ sont des fonctions convexes de classe $\mathcal{C}^1$ (les contraintes d'inégalité).
- $h_j : \mathbb{R}^d \to \mathbb{R}$ sont des fonctions affines de la forme $h_j(x) = a_j^\top x - b_j$ (les contraintes d'égalité).

**Lagrangien du problème :**
Le lagrangien $\mathcal{L} : \mathbb{R}^d \times \mathbb{R}_+^m \times \mathbb{R}^p \to \mathbb{R}$ associé au sous-problème lisse est défini par :
$$ \mathcal{L}(x, \mu, \nu) = f(x) + \sum_{i=1}^m \mu_i c_i(x) + \sum_{j=1}^p \nu_j h_j(x) $$

**Opérateur proximal :**
Pour un paramètre de pas $\gamma > 0$, l'opérateur proximal associé à la fonction non-lisse $g$ est l'application $\text{prox}_{\gamma g} : \mathbb{R}^d \to \mathbb{R}^d$ définie par le problème d'optimisation strictement convexe :
$$ \text{prox}_{\gamma g}(v) = \arg\min_{x \in \mathbb{R}^d} \left\{ g(x) + \frac{1}{2\gamma} \|x - v\|_2^2 \right\} $$

### B. Théorèmes, Propositions & Lemmes

> **Théorème (Conditions d'optimalité de Karush-Kuhn-Tucker généralisées) :**
> Sous les hypothèses précédentes et en supposant la condition de qualification de Slater vérifiée (il existe $x_0 \in \text{int}(\text{dom}(g))$ tel que $c_i(x_0) < 0$ pour tout $i$), un point $x^* \in \mathbb{R}^d$ est une solution optimale globale du problème si et seulement s'il existe des multiplicateurs de Lagrange optimaux $\mu^* \in \mathbb{R}_+^m$ et $\nu^* \in \mathbb{R}^p$ tels que les quatre conditions suivantes sont vérifiées simultanément :
> 1. **Faisabilité primale :** $c_i(x^*) \leq 0, \forall i$ et $h_j(x^*) = 0, \forall j$.
> 2. **Faisabilité duale :** $\mu_i^* \geq 0, \forall i$.
> 3. **Complémentarité :** $\mu_i^* c_i(x^*) = 0, \forall i$.
> 4. **Stationnarité (Inclusion différentielle) :**
>    $$ 0 \in \nabla f(x^*) + \sum_{i=1}^m \mu_i^* \nabla c_i(x^*) + \sum_{j=1}^p \nu_j^* \nabla h_j(x^*) + \partial g(x^*) $$
> Où $\partial g(x^*)$ désigne le sous-différentiel de $g$ en $x^*$.

> **Lemme (Caractérisation proximale de la stationnarité) :**
> L'inclusion différentielle de la stationnarité KKT est rigoureusement équivalente à l'équation de point fixe suivante pour tout pas $\gamma > 0$ :
> $$ x^* = \text{prox}_{\gamma g} \left( x^* - \gamma \left( \nabla f(x^*) + \sum_{i=1}^m \mu_i^* \nabla c_i(x^*) + \sum_{j=1}^p \nu_j^* \nabla h_j(x^*) \right) \right) $$

## 3. Démonstrations

### Démonstration du Lemme (Caractérisation proximale de la stationnarité)

1. **Initialisation / Cadre :**
   Nous procédons par équivalences logiques successives, en utilisant la définition fondamentale du sous-différentiel de l'Analyse Convexe, introduite par Rockafellar et Moreau.
   Posons, pour alléger les notations, le gradient du Lagrangien lisse par rapport à $x$ :
   $$ \nabla_x \mathcal{L}(x^*, \mu^*, \nu^*) = \nabla f(x^*) + \sum_{i=1}^m \mu_i^* \nabla c_i(x^*) + \sum_{j=1}^p \nu_j^* \nabla h_j(x^*) $$

2. **Étape 1 : Réécriture de l'inclusion de stationnarité**
   La condition KKT de stationnarité s'écrit :
   $$ 0 \in \nabla_x \mathcal{L}(x^*, \mu^*, \nu^*) + \partial g(x^*) $$
   Soustrayons $\nabla_x \mathcal{L}(x^*, \mu^*, \nu^*)$ de chaque côté de l'inclusion :
   $$ -\nabla_x \mathcal{L}(x^*, \mu^*, \nu^*) \in \partial g(x^*) $$

3. **Étape 2 : Introduction du pas de descente $\gamma$**
   Soit un scalaire strictement positif arbitraire $\gamma > 0$. Multiplions l'inclusion par $\gamma$ (le sous-différentiel d'un cône convexe préserve cette opération) :
   $$ -\gamma \nabla_x \mathcal{L}(x^*, \mu^*, \nu^*) \in \partial (\gamma g)(x^*) $$
   Ajoutons trivialement $x^*$ de part et d'autre (et puisque $x^* \in x^* + \{0\}$) :
   $$ x^* - \gamma \nabla_x \mathcal{L}(x^*, \mu^*, \nu^*) \in x^* + \partial (\gamma g)(x^*) $$
   Cette ligne est fondamentale. Soit $I$ l'opérateur identité. Nous pouvons réécrire le membre de droite :
   $$ x^* - \gamma \nabla_x \mathcal{L}(x^*, \mu^*, \nu^*) \in (I + \partial (\gamma g))(x^*) $$

4. **Étape 3 : Application de la résolvante du sous-différentiel**
   L'opérateur sous-différentiel $\partial (\gamma g)$ est un opérateur monotone maximal. D'après le Théorème de Minty, l'opérateur $(I + \partial (\gamma g))$ est surjectif, et surtout, son inverse (appelé résolvante) est univalué et partout défini sur $\mathbb{R}^d$.
   Appliquons la résolvante $(I + \partial (\gamma g))^{-1}$ à gauche et à droite de l'inclusion :
   $$ (I + \partial (\gamma g))^{-1} \left( x^* - \gamma \nabla_x \mathcal{L}(x^*, \mu^*, \nu^*) \right) = x^* $$

5. **Étape 4 : Identification avec l'opérateur proximal**
   Or, par la définition de Moreau, la résolvante du sous-différentiel d'une fonction convexe propre semi-continue inférieurement n'est autre que son opérateur proximal :
   $$ (I + \partial (\gamma g))^{-1} = \text{prox}_{\gamma g} $$
   En substituant cette identité analytique dans l'équation de l'étape 3, nous obtenons la forme annoncée :
   $$ \text{prox}_{\gamma g} \left( x^* - \gamma \nabla_x \mathcal{L}(x^*, \mu^*, \nu^*) \right) = x^* $$

6. **Conclusion :**
   Nous avons ainsi démontré rigoureusement que la stationnarité d'un problème composite sous contraintes est équivalente à un point fixe de la composée entre une étape de descente de gradient sur le Lagrangien lisse et une étape d'opérateur proximal pour la fonction non-lisse. Cette preuve est la clé de voûte de l'algorithme "Proximal Gradient Descent". $\blacksquare$

## 4. Exercices d'Application

### Exercice 1 : Calcul de l'Opérateur Proximal de la Norme L1 (Soft-Thresholding)
**Énoncé :**
Démontrer que l'opérateur proximal associé à la fonction $g(x) = \lambda \|x\|_1$ dans $\mathbb{R}^d$ (pour $\lambda > 0$ et un pas $\gamma > 0$) est l'opérateur de seuillage doux (Soft-Thresholding) composante par composante. Précisez sa forme analytique exacte.

**Correction Détaillée :**
* *Analyse de l'énoncé :* La fonction $g(x) = \lambda \sum_{i=1}^d |x_i|$ est séparable. L'opérateur proximal se découple donc sur chaque dimension $i$. Nous nous ramenons à la dimension 1 : on cherche $\text{prox}_{\gamma \lambda |\cdot|}(v_i)$ pour $v_i \in \mathbb{R}$.
* *Résolution pas-à-pas :*
Le problème 1D s'écrit :
$$ x_i^* = \arg\min_{x_i \in \mathbb{R}} \left\{ \lambda |x_i| + \frac{1}{2\gamma} (x_i - v_i)^2 \right\} $$
La fonctionnelle à minimiser, notons-la $J(x_i)$, est strictement convexe et coercive, elle admet donc un unique minimum caractérisé par $0 \in \partial J(x_i^*)$.
Calculons ce sous-différentiel :
$$ \partial J(x_i) = \lambda \partial |x_i| + \frac{1}{\gamma} (x_i - v_i) $$
Le sous-différentiel de la valeur absolue est bien connu : $\partial |x_i| = \{1\}$ si $x_i > 0$, $\{-1\}$ si $x_i < 0$, et $[-1, 1]$ si $x_i = 0$.
Analysons les trois cas mutuellement exclusifs pour la condition $0 \in \lambda \partial |x_i^*| + \frac{1}{\gamma} (x_i^* - v_i)$ :
1. **Cas $x_i^* > 0$ :** $\partial |x_i^*| = 1$. L'équation devient $0 = \lambda (1) + \frac{1}{\gamma}(x_i^* - v_i)$, soit $x_i^* = v_i - \lambda\gamma$. Pour que ce cas soit consistant (i.e. $x_i^* > 0$), il faut impérativement que $v_i - \lambda\gamma > 0$, donc $v_i > \lambda\gamma$.
2. **Cas $x_i^* < 0$ :** $\partial |x_i^*| = -1$. L'équation devient $0 = \lambda (-1) + \frac{1}{\gamma}(x_i^* - v_i)$, soit $x_i^* = v_i + \lambda\gamma$. Pour la consistance ($x_i^* < 0$), il faut que $v_i + \lambda\gamma < 0$, donc $v_i < -\lambda\gamma$.
3. **Cas $x_i^* = 0$ :** $\partial |x_i^*| = [-1, 1]$. L'inclusion devient $0 \in \lambda [-1, 1] + \frac{1}{\gamma}(0 - v_i)$. Cela implique que $\frac{v_i}{\gamma} \in [-\lambda, \lambda]$, et par suite $-\lambda\gamma \leq v_i \leq \lambda\gamma$, ce qui correspond précisément à $|v_i| \leq \lambda\gamma$.

Nous synthétisons ces trois cas dans une fonction unique, l'opérateur de seuillage doux $S_{\gamma\lambda}(v_i)$ :
$$ [\text{prox}_{\gamma\lambda \|\cdot\|_1}(v)]_i = S_{\gamma\lambda}(v_i) = \text{sign}(v_i) \max(|v_i| - \lambda\gamma, 0) $$
Ce résultat montre sans équivoque comment la norme $\ell_1$ force mathématiquement les poids $v_i$ de faible amplitude (ceux dans la bande $[-\lambda\gamma, \lambda\gamma]$) à tomber exactement à $0$ (propriété de sparsité ou pruning).

### Exercice 2 : Résolution KKT d'un réseau linéaire sous contrainte d'énergie (Niveau X / MIT)
**Énoncé :**
Considérons l'entraînement d'un perceptron minimaliste dans $\mathbb{R}^2$ avec pour perte quadratique empirique $f(w) = \frac{1}{2}\|Xw - y\|_2^2$, où $X = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$ et $y = \begin{pmatrix} 1 \\ 4 \end{pmatrix}$. Nous imposons une pénalité d'élagage $g(w) = \lambda \|w\|_1$ avec $\lambda = 1$.
De plus, nous imposons une contrainte matérielle sur la consommation énergétique du réseau (représentée par la somme des poids) : $c(w) = w_1 + w_2 - 2 \leq 0$.
Caractérisez analytiquement le point optimal $w^* = (w_1^*, w_2^*)$ en résolvant le système de Karush-Kuhn-Tucker.

**Correction Détaillée :**
* *Analyse de l'énoncé :* Le problème est strictement convexe. $f$ est différentiable, $g$ est non-lisse (norme $\ell_1$), et la contrainte $c(w)$ est affine. Nous cherchons $w^*$ et le multiplicateur de Lagrange $\mu^* \geq 0$.

* *Résolution pas-à-pas :*
1. **Écriture de la condition de stationnarité KKT :**
   Le Lagrangien lisse est $\mathcal{L}(w, \mu) = \frac{1}{2}\|Xw - y\|_2^2 + \mu (w_1 + w_2 - 2)$.
   Son gradient par rapport à $w$ est :
   $$ \nabla_w \mathcal{L}(w, \mu) = X^\top(Xw - y) + \mu \begin{pmatrix} 1 \\ 1 \end{pmatrix} $$
   Calculons $X^\top(Xw - y)$ :
   $Xw = \begin{pmatrix} w_1 \\ 2w_2 \end{pmatrix}$, donc $Xw - y = \begin{pmatrix} w_1 - 1 \\ 2w_2 - 4 \end{pmatrix}$.
   $X^\top = X$, donc $\nabla f(w) = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} \begin{pmatrix} w_1 - 1 \\ 2w_2 - 4 \end{pmatrix} = \begin{pmatrix} w_1 - 1 \\ 4w_2 - 8 \end{pmatrix}$.
   L'inclusion de stationnarité s'écrit $0 \in \nabla_w \mathcal{L}(w^*, \mu^*) + \lambda \partial \|w^*\|_1$, avec $\lambda = 1$ :
   $$ 0 \in \begin{pmatrix} w_1^* - 1 \\ 4w_2^* - 8 \end{pmatrix} + \mu^* \begin{pmatrix} 1 \\ 1 \end{pmatrix} + \begin{pmatrix} \partial |w_1^*| \\ \partial |w_2^*| \end{pmatrix} $$

2. **Évaluation du problème sans contrainte et sans régularisation (pour se guider) :**
   Si $\mu = 0$ et $\lambda = 0$, $w_{OLS} = (1, 2)^\top$. On constate que $c(w_{OLS}) = 1 + 2 - 2 = 1 > 0$. La contrainte est violée.
   D'après le théorème du complémentarité KKT, la contrainte sera active à l'optimum : $c(w^*) = 0 \implies w_1^* + w_2^* = 2$, et $\mu^* > 0$.

3. **Hypothèse sur le support actif (Pruning) :**
   Supposons que le réseau ne soit pas élagué, c'est-à-dire $w_1^* > 0$ et $w_2^* > 0$.
   Alors $\partial |w_1^*| = 1$ et $\partial |w_2^*| = 1$.
   Le système de stationnarité devient :
   (Eq1) $w_1^* - 1 + \mu^* + 1 = 0 \implies w_1^* = -\mu^*$
   (Eq2) $4w_2^* - 8 + \mu^* + 1 = 0 \implies 4w_2^* = 7 - \mu^* \implies w_2^* = \frac{7 - \mu^*}{4}$
   Or, nous savons que la contrainte est active : $w_1^* + w_2^* = 2$.
   Substituons : $-\mu^* + \frac{7 - \mu^*}{4} = 2$.
   Multiplions par 4 : $-4\mu^* + 7 - \mu^* = 8 \implies -5\mu^* = 1 \implies \mu^* = -1/5$.
   **Contradiction fatale :** Le multiplicateur dual doit satisfaire $\mu^* \geq 0$ (faisabilité duale). L'hypothèse de non-élagage est fausse.

4. **Deuxième hypothèse : Pruning de la dimension 1 :**
   Tentons $w_1^* = 0$. Puisque $w_1^* + w_2^* = 2$, alors nécessairement $w_2^* = 2 > 0$.
   Si $w_2^* = 2$, alors $\partial |w_2^*| = 1$.
   Regardons la deuxième équation de stationnarité (Eq2) :
   $4(2) - 8 + \mu^* + 1 = 0 \implies 8 - 8 + \mu^* + 1 = 0 \implies \mu^* = -1$.
   Encore une contradiction avec $\mu^* \geq 0$.

5. **Troisième hypothèse : Pruning de la dimension 2 :**
   Tentons $w_2^* = 0$. Alors, via la contrainte, $w_1^* = 2 > 0$.
   Regardons l'équation (Eq1) pour $w_1^* = 2$, sachant que $\partial |w_1^*| = 1$ :
   $2 - 1 + \mu^* + 1 = 0 \implies 2 + \mu^* = 0 \implies \mu^* = -2$.
   Toujours une contradiction.

*Remarque critique d'Analyse Convexe :*
Si toutes nos hypothèses échouent, c'est qu'il n'existe pas de solution satisfaisant la contrainte avec $\mu^* \geq 0$.
Revérifions le Lagrangien avec la norme L1 absolue. Le problème posé est $\min \frac{1}{2}(w_1-1)^2 + 2(w_2-2)^2 + |w_1| + |w_2|$ sous contrainte $w_1+w_2 \leq 2$.
Reprenons le cas où la contrainte est **inactive** ($\mu^* = 0$). Cela impliquerait $c(w^*) < 0$.
Résolvons l'inclusion non contrainte :
(Eq1) $w_1^* - 1 + \partial|w_1^*| \ni 0 \implies w_1^* \in \text{prox}_1(1) = \max(|1|-1, 0)\text{sign}(1) = 0$.
(Eq2) $4w_2^* - 8 + \partial|w_2^*| \ni 0 \implies 4w_2^* - 8 + \text{sign}(w_2^*) = 0$ (si on suppose $w_2^* > 0$).
$4w_2^* = 7 \implies w_2^* = 7/4 = 1.75$.
Vérifions la contrainte pour cette solution proximale "libre" :
$c(0, 1.75) = 0 + 1.75 - 2 = -0.25 < 0$.
**Eureka !**
La solution proximale "libre" vérifie STRICTEMENT la contrainte KKT (Faisabilité primale satisfaite).
D'après les conditions de complémentarité ($\mu_i^* c_i(x^*) = 0$), puisque $c(w^*) < 0$, alors on a l'obligation stricte que $\mu^* = 0$.
*Le système est alors consistant.*

**Conclusion :** La solution globale est $w_1^* = 0$ et $w_2^* = 1.75$. Le multiplicateur de Lagrange optimal est $\mu^* = 0$. Ce cas est sublime : l'élagage structurel (Pruning via $\ell_1$) a été si agressif qu'il a naturellement repoussé la solution dans l'intérieur de l'ensemble de contraintes ($w_1+w_2 \leq 2$), rendant la contrainte d'énergie "inactive" à l'optimum. Le neurone 1 a été "pruné" ($w_1 = 0$).

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :**
L'entraînement moderne de réseaux profonds massifs (Large Language Models, ResNets) produit des matrices de poids sur-paramétrées (des milliards de paramètres). Pour déployer ces modèles sur des smartphones (Edge AI) ou réduire leur empreinte carbone, nous appliquons un **"Sparse Learning"**. Mathématiquement, c'est l'introduction de la pénalité $g(x) = \lambda \|x\|_1$ (régularisation LASSO) et potentiellement de contraintes mémoire (budget FLOPs modélisé par $c_i(x) \leq 0$). La Descente de Gradient Proximal (Proximal Gradient Descent ou algorithme FISTA) permet, via l'opérateur de Soft-Thresholding, de ramener *exactement* à zéro des millions de poids à chaque itération d'optimisation. Contrairement à une descente de gradient classique (SGD) qui produit des petits poids ($w_i \approx 10^{-5}$), le proximal garantit le *zéro machine* strict, permettant une compression physique du tenseur en mémoire.

- **Exemple Concret :**
Dans un algorithme d'élagage en ligne pour un réseau convolutif, si l'on veut contraindre une couche $l$ à n'utiliser qu'un budget énergétique fini $E_{max}$, on pose la contrainte affine $\mathbf{1}^\top |W^{(l)}| \leq E_{max}$. Le solveur Proximal KKT alternera entre une étape d'adaptation des poids aux données d'entraînement (Gradient sur la Cross-Entropy), un seuillage (Opérateur Proximal) pour "tuer" les filtres redondants, et une projection sur le demi-espace défini par $E_{max}$ via l'activation dynamique d'un multiplicateur dual $\mu^*$.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 45 (Différentiabilité).md]], [[Jalon 122 (Notion de sous-gradient).md]], [[Jalon 124 (Conditions de Karush-Kuhn-Tucker).md]], [[Jalon 125 (Opérateurs proximaux).md]]
- **Concepts Futurs dépendants :** [[Jalon 133 (Modèle PAC).md]]
