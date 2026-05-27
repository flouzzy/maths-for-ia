---
uuid: "jalon-131"
title: "Algorithmes d'optimisation de second ordre en grande dimension"
year: 3
trimester: 11
tags:
  - math/optimisation
  - ia/machine-learning
prev: "[[Jalon 130 (Regularisation implicite de la descente de gradient dans les modeles sur-parametres).md]]"
next: "[[Jalon 132 (Livrable IA).md]]"
---

# Algorithmes d'optimisation de second ordre en grande dimension

## 1. L'Intuition Première (Niveau 12 ans)

**La Métaphore :**
Imagine que tu as les yeux bandés et que tu essaies de descendre au fond d'une vallée pour trouver le point le plus bas. L'approche la plus simple (la "descente de gradient") consiste à tâter le sol avec ton pied, à sentir dans quelle direction la pente descend le plus fort, et à faire un petit pas dans cette direction. Ça marche, mais si la vallée a une forme un peu bizarre, comme un long ravin très étroit et légèrement en pente, tu vas faire des zigzags en rebondissant d'un bord à l'autre, et tu mettras un temps fou à arriver en bas.

Maintenant, imagine que tu as un super-pouvoir : non seulement tu sens la pente sous ton pied, mais tu ressens aussi la "courbure" du sol sur plusieurs mètres autour de toi. Tu sais si le sol se creuse comme un bol ou s'il s'aplatit. Avec cette information, tu peux te diriger directement vers le fond du bol d'un seul grand pas, sans faire de zigzags. C'est ça, la méthode de Newton (une méthode dite du "second ordre").

**Le "Pourquoi on a inventé ça" :**
Le problème de ce super-pouvoir mathématique, c'est qu'il demande de calculer et de stocker énormément d'informations. Si ton paysage a des millions de dimensions (ce qui est courant en intelligence artificielle), la "carte de la courbure" (la matrice Hessienne) devient gigantesque : un million de lignes et un million de colonnes. C'est impossible à faire tenir dans la mémoire d'un ordinateur. Les mathématiciens ont donc inventé les méthodes "quasi-Newton" (comme l'algorithme L-BFGS). Ces méthodes sont très astucieuses : au lieu d'exiger la carte complète de la courbure, elles reconstruisent une *approximation* de cette carte uniquement en observant l'historique de tes derniers pas et de la façon dont la pente a changé. Tu obtiens presque le super-pouvoir, mais sans avoir besoin d'une mémoire infinie !

**Visualisation :**
Graphiquement, la descente de gradient simple approxime le terrain localement par un plan incliné. La méthode de Newton approxime le terrain localement par un paraboloïde (une forme de bol). Les méthodes quasi-Newton déforment progressivement un bol initial au fur et à mesure qu'elles explorent le terrain, en le "moulant" sur la vraie forme de la vallée pour trouver son fond le plus rapidement possible.

## 2. Formalisation & Rigueur Académique

Nous nous plaçons dans le cadre de l'optimisation non linéaire sans contraintes en dimension $n$.

### A. Définitions Formelles

**Espace ambiant et fonction objectif :**
Soit $E = \mathbb{R}^n$ un espace vectoriel réel de dimension finie, muni de son produit scalaire euclidien canonique $\langle \cdot, \cdot \rangle$ et de la norme associée $\|\cdot\|$.
Soit $f : \mathbb{R}^n \to \mathbb{R}$ une fonction de classe $\mathcal{C}^2(\mathbb{R}^n, \mathbb{R})$. L'objectif est de trouver un minimum local (voire global si $f$ est convexe) $x^* \in \mathbb{R}^n$ tel que :
$$ x^* \in \arg\min_{x \in \mathbb{R}^n} f(x) $$

**Gradient et Hessienne :**
Pour tout $x \in \mathbb{R}^n$ :
- Le **gradient** de $f$ en $x$, noté $\nabla f(x) \in \mathbb{R}^n$, est le vecteur colonne composé des dérivées partielles premières : $(\nabla f(x))_i = \frac{\partial f}{\partial x_i}(x)$.
- La **matrice Hessienne** de $f$ en $x$, notée $\nabla^2 f(x) \in \mathcal{M}_n(\mathbb{R})$, est la matrice carrée symétrique (d'après le théorème de Schwarz) composée des dérivées partielles secondes : $(\nabla^2 f(x))_{i,j} = \frac{\partial^2 f}{\partial x_i \partial x_j}(x)$.

**Méthode de Newton :**
La méthode de Newton consiste à approcher $f$ au voisinage de l'itéré courant $x_k$ par son développement de Taylor à l'ordre 2 :
$$ f(x_k + p) \approx f(x_k) + \langle \nabla f(x_k), p \rangle + \frac{1}{2} \langle p, \nabla^2 f(x_k) p \rangle $$
Si $\nabla^2 f(x_k)$ est définie positive, le minimum de ce modèle quadratique est atteint pour un pas de Newton $p_k$ tel que :
$$ \nabla^2 f(x_k) p_k = -\nabla f(x_k) $$
L'itération de Newton pure est donc : $x_{k+1} = x_k - (\nabla^2 f(x_k))^{-1} \nabla f(x_k)$.

### B. Théorèmes, Propositions & Lemmes

> **Définition (Méthodes de quasi-Newton) :**
> Une méthode de quasi-Newton génère une suite d'itérés $(x_k)_{k \in \mathbb{N}}$ par la récurrence :
> $$ x_{k+1} = x_k + \alpha_k p_k $$
> où $\alpha_k > 0$ est le pas (déterminé par une recherche linéaire satisfaisant les conditions de Wolfe), et la direction de descente $p_k$ est obtenue en résolvant le système linéaire :
> $$ B_k p_k = -\nabla f(x_k) $$
> La matrice $B_k \in \mathcal{M}_n(\mathbb{R})$ est symétrique définie positive et se veut être une approximation de la Hessienne $\nabla^2 f(x_k)$.

Pour construire $B_{k+1}$ à partir de $B_k$, on exploite la variation de gradient entre l'étape $k$ et l'étape $k+1$. Posons :
- La variation de position : $s_k = x_{k+1} - x_k$
- La variation de gradient : $y_k = \nabla f(x_{k+1}) - \nabla f(x_k)$

> **Proposition (L'équation sécante) :**
> Pour que le modèle quadratique approché à l'itération $k+1$ coïncide avec le gradient observé à l'itération $k$, la nouvelle approximation de la Hessienne $B_{k+1}$ doit satisfaire l'équation sécante :
> $$ B_{k+1} s_k = y_k $$

> **Théorème de l'actualisation BFGS (Broyden-Fletcher-Goldfarb-Shanno) :**
> Sous la condition de courbure stricte $\langle y_k, s_k \rangle > 0$, parmi toutes les matrices $B$ symétriques définies positives satisfaisant l'équation sécante $B s_k = y_k$, celle qui est la "plus proche" de $B_k$ (au sens d'une norme de Frobenius pondérée) est donnée par la formule de mise à jour BFGS :
> $$ B_{k+1} = B_k - \frac{B_k s_k s_k^T B_k}{\langle s_k, B_k s_k \rangle} + \frac{y_k y_k^T}{\langle y_k, s_k \rangle} $$

*Remarque pratique :* En optimisation, on cherche $p_k = -B_k^{-1} \nabla f(x_k)$. Il est donc plus efficace de maintenir une approximation directe de l'inverse de la Hessienne, notée $H_k = B_k^{-1}$.

> **Formule de mise à jour BFGS Inverse (Formule de Sherman-Morrison-Woodbury appliquée) :**
> La séquence d'approximations de l'inverse de la Hessienne $(H_k)_{k \in \mathbb{N}}$ est donnée par :
> $$ H_{k+1} = \left( I_n - \rho_k s_k y_k^T \right) H_k \left( I_n - \rho_k y_k s_k^T \right) + \rho_k s_k s_k^T $$
> avec $\rho_k = \frac{1}{\langle y_k, s_k \rangle}$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration de l'actualisation de la Hessienne inverse par l'identité de Sherman-Morrison-Woodbury

Nous allons prouver rigoureusement le passage de la formule de mise à jour de la Hessienne $B_k$ (formule directe) à celle de son inverse $H_k = B_k^{-1}$ (formule inverse).

1. **Initialisation / Cadre :**
Rappelons la mise à jour directe BFGS pour $B_{k+1}$ :
$$ B_{k+1} = B_k - \frac{B_k s_k s_k^T B_k}{s_k^T B_k s_k} + \frac{y_k y_k^T}{y_k^T s_k} $$
(Ici, par commodité d'écriture matricielle, nous notons le produit scalaire $\langle u, v \rangle$ par $u^T v$ ou $v^T u$).

Le Lemme de Sherman-Morrison stipule que pour une matrice inversible $A$ et des vecteurs colonnes $u, v$ :
$$ (A + u v^T)^{-1} = A^{-1} - \frac{A^{-1} u v^T A^{-1}}{1 + v^T A^{-1} u} $$
Nous allons appliquer ce lemme deux fois de suite.

2. **Étape 1 : Première application de Sherman-Morrison**
Posons $A_1 = B_k - \frac{B_k s_k s_k^T B_k}{s_k^T B_k s_k}$.
Ainsi, $B_{k+1} = A_1 + \frac{y_k y_k^T}{y_k^T s_k} = A_1 + u_1 v_1^T$, en choisissant $u_1 = y_k$ et $v_1 = \frac{y_k}{y_k^T s_k}$.
Pour pouvoir inverser cela, nous avons d'abord besoin de l'inverse de $A_1$. Or, on ne peut pas appliquer directement Sherman-Morrison sur $B_k$ pour trouver $A_1^{-1}$ car la matrice de rang 1 ajoutée annule la direction $s_k$.
Il faut donc ruser et considérer la formule inverse de BFGS directement construite à partir de l'équation sécante duale.

Une approche plus constructive est de formuler le problème d'optimisation sur $H$ lui-même.
On cherche $H_{k+1}$ comme solution du problème :
$$ \min_H \| H - H_k \|_W $$
sous les contraintes $H = H^T$ et l'équation sécante $H y_k = s_k$.
La norme pondérée choisie est $\|A\|_W = \|W^{1/2} A W^{1/2}\|_F$ avec $W$ une matrice symétrique définie positive vérifiant l'équation sécante $W s_k = y_k$ (par exemple $W = B_{k+1}$ en considérant le problème théorique, mais en pratique on utilise la décomposition intégrale).

3. **Étape 2 : Construction algébrique de la mise à jour**
On cherche une mise à jour de rang 2 de la forme :
$$ H_{k+1} = H_k + a u u^T + b v v^T $$
Imposons l'équation sécante $H_{k+1} y_k = s_k$ :
$$ H_k y_k + a (u^T y_k) u + b (v^T y_k) v = s_k $$
Pour que cela s'arrange élégamment, on choisit les vecteurs $u$ et $v$ parmi les directions connues du problème : $s_k$ et $H_k y_k$.
Posons $u = s_k$ et $v = H_k y_k$. L'équation devient :
$$ H_k y_k + a (s_k^T y_k) s_k + b ((H_k y_k)^T y_k) H_k y_k = s_k $$
En réarrangeant les termes selon les vecteurs $s_k$ et $H_k y_k$ :
$$ [ a (s_k^T y_k) - 1 ] s_k + [ 1 + b (y_k^T H_k y_k) ] H_k y_k = 0 $$
Pour que cette égalité vectorielle soit vraie indépendamment de l'indépendance linéaire de $s_k$ et $H_k y_k$, on annule les coefficients :
$$ a (s_k^T y_k) - 1 = 0 \implies a = \frac{1}{s_k^T y_k} = \frac{1}{\langle y_k, s_k \rangle} $$
$$ 1 + b (y_k^T H_k y_k) = 0 \implies b = -\frac{1}{y_k^T H_k y_k} $$

En substituant $a$ et $b$ dans notre forme (qui correspond à l'actualisation DFP, la "duale" de BFGS) :
$$ H_{k+1}^{DFP} = H_k + \frac{s_k s_k^T}{y_k^T s_k} - \frac{H_k y_k y_k^T H_k}{y_k^T H_k y_k} $$

Pour obtenir BFGS, on échange les rôles de $B$ et $H$, et de $s$ et $y$ (Dualité de Broyden). L'actualisation DFP pour $B$ est :
$$ B_{k+1}^{DFP} = \left( I - \frac{y_k s_k^T}{y_k^T s_k} \right) B_k \left( I - \frac{s_k y_k^T}{y_k^T s_k} \right) + \frac{y_k y_k^T}{y_k^T s_k} $$
Par dualité, la formule BFGS pour $H$ s'obtient en échangeant $B \leftrightarrow H$ et $s \leftrightarrow y$ :
$$ H_{k+1}^{BFGS} = \left( I_n - \frac{s_k y_k^T}{s_k^T y_k} \right) H_k \left( I_n - \frac{y_k s_k^T}{s_k^T y_k} \right) + \frac{s_k s_k^T}{s_k^T y_k} $$

4. **Étape 3 : Développement complet de la forme classique**
Posons $\rho_k = \frac{1}{s_k^T y_k} = \frac{1}{y_k^T s_k}$ (puisque le produit scalaire euclidien est commutatif).
$$ H_{k+1} = (I_n - \rho_k s_k y_k^T) H_k (I_n - \rho_k y_k s_k^T) + \rho_k s_k s_k^T $$
Développons le premier terme :
$$ = (H_k - \rho_k s_k y_k^T H_k) (I_n - \rho_k y_k s_k^T) + \rho_k s_k s_k^T $$
$$ = H_k - \rho_k H_k y_k s_k^T - \rho_k s_k y_k^T H_k + \rho_k^2 s_k y_k^T H_k y_k s_k^T + \rho_k s_k s_k^T $$
Comme $y_k^T H_k y_k$ est un scalaire, on peut le factoriser :
$$ = H_k - \frac{H_k y_k s_k^T + s_k y_k^T H_k}{y_k^T s_k} + \frac{(y_k^T H_k y_k) s_k s_k^T}{(y_k^T s_k)^2} + \frac{s_k s_k^T}{y_k^T s_k} $$
$$ = H_k - \frac{H_k y_k s_k^T + s_k y_k^T H_k}{y_k^T s_k} + \left[ \frac{y_k^T H_k y_k}{(y_k^T s_k)^2} + \frac{y_k^T s_k}{(y_k^T s_k)^2} \right] s_k s_k^T $$
$$ = H_k + \frac{(s_k^T y_k + y_k^T H_k y_k)}{(s_k^T y_k)^2} s_k s_k^T - \frac{H_k y_k s_k^T + s_k y_k^T H_k}{s_k^T y_k} $$

5. **Conclusion :**
La formule obtenue pour $H_{k+1}$ est symétrique (si $H_k$ l'est) et préserve la propriété définie positive sous la condition de courbure stricte $y_k^T s_k > 0$. Elle est l'outil fondamental de l'algorithme BFGS, permettant de calculer $p_k = -H_k \nabla f(x_k)$ par un simple produit matrice-vecteur (coût $O(n^2)$), évitant ainsi la résolution d'un système linéaire complet (coût $O(n^3)$).

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Condition de courbure de Wolfe
**Énoncé :**
Lors de la recherche linéaire pour déterminer le pas $\alpha_k$ dans l'itération $x_{k+1} = x_k + \alpha_k p_k$, on impose la deuxième condition de Wolfe forte :
$$ |\nabla f(x_{k+1})^T p_k| \le c_2 |\nabla f(x_k)^T p_k| $$
avec $c_2 \in (0, 1)$. En supposant que $p_k$ est une direction de descente ($\nabla f(x_k)^T p_k < 0$), démontrer que cette condition garantit l'inégalité de courbure stricte $\langle y_k, s_k \rangle > 0$, essentielle pour que l'actualisation BFGS préserve la définition positive de la Hessienne approchée.

**Correction Détaillée :**
* *Analyse de l'énoncé :* On doit analyser le produit scalaire $\langle y_k, s_k \rangle$. Par définition, $s_k = x_{k+1} - x_k = \alpha_k p_k$ et $y_k = \nabla f(x_{k+1}) - \nabla f(x_k)$. La condition porte sur les projections du gradient sur la direction $p_k$.

* *Résolution pas-à-pas :*
1. Écrivons le produit scalaire :
   $$ \langle y_k, s_k \rangle = y_k^T s_k = (\nabla f(x_{k+1}) - \nabla f(x_k))^T (\alpha_k p_k) $$
   $$ \langle y_k, s_k \rangle = \alpha_k [ \nabla f(x_{k+1})^T p_k - \nabla f(x_k)^T p_k ] $$

2. Exploitation de la condition de Wolfe. La condition forte donne :
   $$ -c_2 |\nabla f(x_k)^T p_k| \le \nabla f(x_{k+1})^T p_k \le c_2 |\nabla f(x_k)^T p_k| $$
   Or, par hypothèse, $p_k$ est une direction de descente, donc $\nabla f(x_k)^T p_k < 0$, ce qui implique $|\nabla f(x_k)^T p_k| = -\nabla f(x_k)^T p_k$.
   L'inégalité de gauche de la condition forte s'écrit alors :
   $$ \nabla f(x_{k+1})^T p_k \ge c_2 \nabla f(x_k)^T p_k $$

3. Substituons cette minoration dans l'expression de la courbure :
   $$ \nabla f(x_{k+1})^T p_k - \nabla f(x_k)^T p_k \ge c_2 \nabla f(x_k)^T p_k - \nabla f(x_k)^T p_k $$
   $$ \nabla f(x_{k+1})^T p_k - \nabla f(x_k)^T p_k \ge (c_2 - 1) \nabla f(x_k)^T p_k $$

4. Conclusion sur le signe :
   Puisque $\nabla f(x_k)^T p_k < 0$ et $c_2 \in (0, 1)$ implique $(c_2 - 1) < 0$, le produit de ces deux termes strictement négatifs est strictement positif :
   $$ (c_2 - 1) \nabla f(x_k)^T p_k > 0 $$
   De plus, le pas $\alpha_k$ est un scalaire strictement positif. Ainsi :
   $$ \langle y_k, s_k \rangle \ge \alpha_k (c_2 - 1) \nabla f(x_k)^T p_k > 0 $$
   La condition de courbure stricte $\langle y_k, s_k \rangle > 0$ est donc garantie de manière inconditionnelle.

### Exercice 2 : L'astuce L-BFGS (Limited-memory) et coût algorithmique
**Énoncé :**
Si $n$ est de l'ordre de $10^8$ (cas du Deep Learning), la matrice $H_k \in \mathcal{M}_n(\mathbb{R})$ requiert environ 40 Pétaoctets de RAM. L'algorithme L-BFGS propose de ne jamais former la matrice $H_k$. Au lieu de cela, on stocke uniquement les $m$ derniers couples de vecteurs $(s_i, y_i)$ pour $i = k-m, \dots, k-1$ (avec $m \ll n$, typiquement $m \approx 10$).
En posant $H_k^{(0)} = \gamma_k I_n$ (une approximation scalaire initiale), démontrer par récurrence que le calcul de la direction $p_k = -H_k \nabla f(x_k)$ en utilisant la boucle à deux passes (two-loop recursion) de L-BFGS a une complexité spatiale en $\mathcal{O}(m n)$ et temporelle en $\mathcal{O}(m n)$.

**Correction Détaillée :**
* *Analyse de l'énoncé :* La matrice $H_k$ de BFGS est issue de l'application successive de $m$ mises à jour à partir d'une matrice initiale $H_k^{(0)}$. L-BFGS consiste à déplier la formule de mise à jour récursivement pour l'appliquer à un vecteur sans jamais instancier la matrice pleine.

* *Résolution pas-à-pas :*
1. Rappel de la mise à jour inverse BFGS, en posant $V_i = I_n - \rho_i y_i s_i^T$ :
   $$ H_{i+1} = V_i^T H_i V_i + \rho_i s_i s_i^T $$

2. Déploiement récursif sur $m$ étapes. Si on l'applique sur une fenêtre de mémoire allant de $k-m$ à $k-1$ :
   $$ H_k = V_{k-1}^T H_{k-1} V_{k-1} + \rho_{k-1} s_{k-1} s_{k-1}^T $$
   $$ H_k = V_{k-1}^T (V_{k-2}^T H_{k-2} V_{k-2} + \rho_{k-2} s_{k-2} s_{k-2}^T) V_{k-1} + \rho_{k-1} s_{k-1} s_{k-1}^T $$
   $$ H_k = V_{k-1}^T V_{k-2}^T \dots V_{k-m}^T H_k^{(0)} V_{k-m} \dots V_{k-2} V_{k-1} $$
   $$ \quad + \sum_{j=k-m}^{k-1} \rho_j (V_{k-1}^T \dots V_{j+1}^T) s_j s_j^T (V_{j+1} \dots V_{k-1}) $$

3. Calcul du produit matrice-vecteur $p_k = -H_k \nabla f(x_k)$. Posons $q = -\nabla f(x_k)$. L'algorithme "two-loop recursion" calcule $H_k q$ en appliquant séquentiellement les opérateurs depuis la droite.
   - **Boucle 1 (Backward pass) :** Pour $i = k-1$ décroissant jusqu'à $k-m$ :
     On doit appliquer les $V_i = I_n - \rho_i y_i s_i^T$ au vecteur courant.
     À l'étape $i$, le vecteur courant est noté $q_{i+1}$.
     $$ q_i = V_i q_{i+1} = (I_n - \rho_i y_i s_i^T) q_{i+1} = q_{i+1} - \rho_i (s_i^T q_{i+1}) y_i $$
     Soit $\alpha_i = \rho_i s_i^T q_{i+1}$. Le calcul de ce scalaire prend $\mathcal{O}(n)$ opérations (produit scalaire de taille $n$).
     Puis $q_i = q_{i+1} - \alpha_i y_i$ prend aussi $\mathcal{O}(n)$ opérations.
     Total pour la boucle arrière (exécutée $m$ fois) : $\mathcal{O}(m n)$ opérations temporelles.

   - **Étape centrale :**
     On a atteint $q_{k-m}$. On le multiplie par l'approximation initiale diagonale :
     $$ r_{k-m} = H_k^{(0)} q_{k-m} = \gamma_k I_n q_{k-m} = \gamma_k q_{k-m} $$
     Complexité : $\mathcal{O}(n)$.

   - **Boucle 2 (Forward pass) :** Pour $i = k-m$ croissant jusqu'à $k-1$ :
     On doit appliquer les $V_i^T = I_n - \rho_i s_i y_i^T$ et ajouter le terme $\rho_i s_i s_i^T$ au vecteur courant $r_i$.
     En factorisant $s_i$, l'opération équivalente est :
     $$ \beta_i = \rho_i y_i^T r_i \quad \text{ (coût } \mathcal{O}(n) \text{)} $$
     $$ r_{i+1} = r_i + s_i (\alpha_i - \beta_i) \quad \text{ (coût } \mathcal{O}(n) \text{)} $$
     Total pour la boucle avant (exécutée $m$ fois) : $\mathcal{O}(m n)$ opérations temporelles.

4. **Conclusion :**
   La complexité temporelle totale est de l'ordre de $4mn$, ce qui est linéaire en la dimension $n$.
   La complexité spatiale nécessite uniquement de stocker la mémoire L-BFGS, soit $m$ vecteurs $s_i$, $m$ vecteurs $y_i$ et $m$ scalaires $\rho_i$, de taille $n$, et le vecteur courant $q$. Soit $2m + \mathcal{O}(1)$ vecteurs de taille $n$. L'espace requis est strictement en $\mathcal{O}(m n)$. Le problème de la Hessienne géante en $\mathcal{O}(n^2)$ est ainsi contourné.

## 5. Ancrage & Application en Intelligence Artificielle

**Le Pont Théorique :**
En Machine Learning et Deep Learning, l'apprentissage consiste à minimiser une fonction de perte empirique (Loss function) de très grande dimension (parfois des dizaines de milliards de paramètres $n$). La descente de gradient stochastique (SGD) est reine en raison de son faible coût par itération, mais elle souffre cruellement du mauvais conditionnement du problème (le fait que la vallée soit un ravin étroit). Les algorithmes du second ordre comme Newton convergeraient beaucoup plus vite en termes d'itérations, car ils s'adaptent naturellement à la géométrie de la vallée, rendant l'algorithme invariant par transformations affines du système de coordonnées.

**Exemple Concret :**
Bien que l'optimisation des très grands réseaux de neurones profonds (ResNet, Transformers) utilise massivement des algorithmes d'optimisation de premier ordre adaptatifs (comme Adam, qui utilise une approximation diagonale très grossière de la Hessienne via la variance des gradients), **L-BFGS** reste l'algorithme d'élite pour certaines sous-classes de problèmes en IA :
- **Régression logistique à grande échelle** ou les Modèles Linéaires Généralisés (GLM) avec régularisation, où l'objectif est fortement convexe, lisse, déterministe (full-batch) et extrêmement mal conditionné. La bibliothèque `scikit-learn` utilise L-BFGS par défaut pour `LogisticRegression`.
- **PINNs (Physics-Informed Neural Networks)** : L-BFGS est le standard de l'industrie pour fine-tuner les réseaux de neurones informés par la physique (résolution d'EDP). Une fois qu'Adam a amené les poids dans la bonne vallée, on bascule sur L-BFGS qui garantit une convergence quasi-quadratique vers la solution avec une précision d'ingénierie que les algorithmes de gradient stochastique peinent à atteindre à cause du bruit inhérent au mini-batching.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 45 (Différentiabilité)]], [[Jalon 47 (Dérivées partielles d'ordre deux)]], [[Jalon 121 (Ensembles convexes)]], [[Jalon 130 (Regularisation implicite de la descente de gradient dans les modeles sur-parametres)]]
- **Concepts Futurs dépendants :** [[Jalon 131 (Algorithmes d'optimisation de second ordre en grande dimension)]], [[Jalon 132 (Livrable IA)]], [[Jalon 144 (Le phénomène de double descente)]]
