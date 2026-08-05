---
uuid: "jalon-47"
title: "Dérivées partielles d'ordre deux et Hessienne"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/optimisation
prev: "[[Jalon 46 (Matrice jacobienne).md]]"
next: "[[Jalon 48 (Livrable IA).md]]"
---

# Jalon 47 : Dérivées partielles d'ordre deux et Matrice Hessienne

## 1. Origines et Nécessité Géométrique

Lorsque l'on étudie les variations d'une fonction de plusieurs variables, le gradient (les dérivées partielles premières) nous indique la pente locale, c'est-à-dire la direction de plus forte croissance. Cependant, ce renseignement est purement linéaire. Si le gradient s'annule, la fonction admet un point critique, mais s'agit-il d'un sommet de colline, du fond d'une vallée ou d'un col de montagne ?
Pour trancher, il est indispensable de mesurer la variation du gradient lui-même. Historiquement, des mathématiciens comme Euler et Cauchy, puis Ludwig Otto Hesse au XIXe siècle, ont formalisé l'étude de la courbure locale des surfaces. La matrice hessienne, introduite par Hesse, capture l'ensemble des dérivées secondes croisées, fournissant l'équivalent multidimensionnel de la dérivée seconde scalaire. C'est l'outil fondamental de l'optimisation locale.

## 2. Définitions, Théorèmes et Caractérisations Locales

### Dérivées partielles secondes

Soit $U$ un ouvert de $\mathbb{R}^n$ et $f : U \to \mathbb{R}$ une fonction. Si les dérivées partielles premières $\frac{\partial f}{\partial x_i}$ existent et sont différentiables, on peut définir les dérivées secondes.

> **Définition (Dérivées partielles d'ordre 2) :**
> La dérivée partielle seconde de $f$ par rapport à $x_j$ puis à $x_i$ est donnée par :
> $$\frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{\partial}{\partial x_i} \left( \frac{\partial f}{\partial x_j} \right)$$
> Typage : $x_i, x_j \in \mathbb{R}$, $f \in \mathcal{C}^2(U, \mathbb{R})$.

**Exemple d'évaluation :**
Considérons $f(x, y) = x^3 y^2$.
- $\frac{\partial f}{\partial x} = 3x^2 y^2$.
- En dérivant ensuite par rapport à $y$, on obtient $\frac{\partial^2 f}{\partial y \partial x} = \frac{\partial}{\partial y}(3x^2 y^2) = 6x^2 y$.
- Réciproquement, $\frac{\partial f}{\partial y} = 2x^3 y$, d'où $\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial}{\partial x}(2x^3 y) = 6x^2 y$. On remarque la symétrie.

### Théorème de Schwarz

> **Théorème de Schwarz (Symétrie des dérivées croisées) :**
> Si $f : U \subset \mathbb{R}^n \to \mathbb{R}$ est de classe $\mathcal{C}^2$ sur $U$, alors pour tout point $a \in U$ et tout couple d'indices $i, j \in \llbracket 1, n \rrbracket$ :
> $$\frac{\partial^2 f}{\partial x_i \partial x_j}(a) = \frac{\partial^2 f}{\partial x_j \partial x_i}(a)$$

**Cas pathologique :**
Si $f$ n'est pas $\mathcal{C}^2$, la symétrie peut être mise en défaut. Par exemple, la fonction $f(x, y) = \frac{xy(x^2 - y^2)}{x^2 + y^2}$ prolongée par $0$ en $(0,0)$ admet des dérivées partielles secondes en l'origine, mais $\frac{\partial^2 f}{\partial x \partial y}(0,0) = -1 \neq 1 = \frac{\partial^2 f}{\partial y \partial x}(0,0)$.

### Matrice Hessienne

> **Définition (Matrice Hessienne) :**
> Soit $f \in \mathcal{C}^2(U, \mathbb{R})$. Pour $a \in U$, la matrice hessienne $H_f(a)$ (ou $\nabla^2 f(a)$) est la matrice symétrique $n \times n$ dont les coefficients sont les dérivées secondes croisées évaluées en $a$ :
> $$H_f(a) = \left( \frac{\partial^2 f}{\partial x_i \partial x_j}(a) \right)_{1 \leq i, j \leq n}$$

## 3. Démonstrations et Développement de Taylor

L'intérêt central de la hessienne réside dans son apparition dans la formule de Taylor à l'ordre 2, permettant d'approcher localement $f$ par une paraboloïde.

**Démonstration (Formule de Taylor-Young à l'ordre 2) :**
Soit $f \in \mathcal{C}^2(U, \mathbb{R})$ et $a \in U$. Considérons un vecteur $h \in \mathbb{R}^n$ tel que $a+h \in U$. Posons la fonction scalaire $g(t) = f(a + th)$ pour $t \in [0, 1]$.
La règle de la chaîne nous donne :
$$g'(t) = \sum_{i=1}^n h_i \frac{\partial f}{\partial x_i}(a + th) = \langle \nabla f(a+th), h \rangle$$
En dérivant une seconde fois, on obtient :
$$g''(t) = \sum_{i=1}^n \sum_{j=1}^n h_i h_j \frac{\partial^2 f}{\partial x_j \partial x_i}(a + th) = h^T H_f(a+th) h$$
L'application de la formule de Taylor-Maclaurin scalaire à l'ordre 2 pour $g$ en $t=0$ :
$g(1) = g(0) + g'(0) + \frac{1}{2} g''(0) + o(1)$ se réécrit :
$$f(a+h) = f(a) + \langle \nabla f(a), h \rangle + \frac{1}{2} h^T H_f(a) h + o(\|h\|^2)$$

**Conséquence sur la classification des points critiques :**
En un point critique $a$, le gradient s'annule : $\nabla f(a) = 0$.
L'approximation devient $f(a+h) - f(a) \approx \frac{1}{2} h^T H_f(a) h$.
Le signe de cette différence, indiquant si on monte ou on descend autour de $a$, est donné par la forme quadratique associée à $H_f(a)$.
1. Si $H_f(a)$ est définie positive (toutes les valeurs propres sont $> 0$), alors $h^T H_f(a) h > 0$ pour $h \neq 0$. C'est un **minimum local strict**.
2. Si $H_f(a)$ est définie négative, c'est un **maximum local strict**.
3. Si $H_f(a)$ admet des valeurs propres de signes stricts opposés, c'est un **point selle**.

## 4. Applications en Optimisation et Intelligence Artificielle

Dans l'entraînement des réseaux de neurones profonds, la fonction de perte $\mathcal{L}(\theta)$ dépend de millions de paramètres. La matrice hessienne $H_{\mathcal{L}}(\theta)$ caractérise la courbure locale du paysage de perte.
1. **Conditionnement :** Le rapport entre la plus grande et la plus petite valeur propre de la hessienne (le nombre de conditionnement) dicte la vitesse de convergence de la descente de gradient. Si ce rapport est immense, la trajectoire d'optimisation oscille dramatiquement (ravins étroits).
2. **Méthodes du second ordre :** La méthode de Newton met à jour les paramètres via $\theta_{t+1} = \theta_t - H_{\mathcal{L}}(\theta_t)^{-1} \nabla \mathcal{L}(\theta_t)$, compensant directement la courbure. Cependant, l'inversion d'une matrice $N \times N$ avec $N \sim 10^7$ est impossible en pratique, motivant les algorithmes Quasi-Newton (L-BFGS) qui approchent l'inverse de la hessienne.
3. **Optimiseurs modernes :** Adam et RMSprop estiment implicitement la diagonale de la matrice hessienne (en utilisant la variance des gradients historiques) pour adapter le taux d'apprentissage de chaque paramètre de façon autonome.
