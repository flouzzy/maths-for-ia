---
uuid: "jalon-46"
title: "Matrice jacobienne et Règle de la chaîne"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/backpropagation
prev: "[[Jalon 45 (Différentiabilité).md]]"
next: "[[Jalon 47 (Dérivées partielles d'ordre deux).md]]"
---

# Jalon 46 : Matrice jacobienne et Règle de la chaîne

## 1. Genèse et Intuition Géométrique

La matrice jacobienne généralise la notion de dérivée aux fonctions vectorielles de plusieurs variables. Historiquement, Carl Gustav Jacob Jacobi a formalisé ce concept au XIXe siècle pour étudier les changements de variables dans les intégrales multiples et les équations différentielles.

Si l'on considère une transformation $f : \mathbb{R}^n \to \mathbb{R}^m$, elle déforme un domaine de l'espace de départ. Localement, au voisinage d'un point $a$, cette déformation non-linéaire peut être approchée par une transformation affine. La partie linéaire de cette transformation est précisément représentée par la matrice jacobienne $J_f(a)$. Elle indique comment une petite perturbation $\delta x$ autour de $a$ se traduit par une perturbation $\delta y \approx J_f(a) \delta x$ autour de $f(a)$.

En apprentissage profond (Deep Learning), la règle de la chaîne (Chain Rule) est le cœur du calcul du gradient par rétropropagation (backpropagation). Un réseau de neurones n'est autre qu'une gigantesque composition de fonctions, et la dérivée de cette composition requiert le produit ordonné des matrices jacobiennes de chaque couche.

## 2. Définitions et Théorèmes

### La Matrice Jacobienne

Soit $U$ un ouvert de $\mathbb{R}^n$ et $f : U \to \mathbb{R}^m$ une application différentiable en un point $a \in U$.
On note les composantes de $f$ par $f(x) = (f_1(x), \dots, f_m(x))^T$, où chaque $f_i : U \to \mathbb{R}$.

**Définition** : La matrice jacobienne de $f$ en $a$, notée $J_f(a)$ ou $\mathrm{Mat}(df_a)$, est la matrice de taille $m \times n$ dont le coefficient à la $i$-ème ligne et $j$-ème colonne est la dérivée partielle de $f_i$ par rapport à $x_j$, évaluée en $a$ :
$$
J_f(a) = \begin{pmatrix}
\frac{\partial f_1}{\partial x_1}(a) & \frac{\partial f_1}{\partial x_2}(a) & \dots & \frac{\partial f_1}{\partial x_n}(a) \\
\frac{\partial f_2}{\partial x_1}(a) & \frac{\partial f_2}{\partial x_2}(a) & \dots & \frac{\partial f_2}{\partial x_n}(a) \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial f_m}{\partial x_1}(a) & \frac{\partial f_m}{\partial x_2}(a) & \dots & \frac{\partial f_m}{\partial x_n}(a)
\end{pmatrix}
$$

**Notations et Précisions** :
- **$m$** : dimension de l'espace d'arrivée (nombre de lignes).
- **$n$** : dimension de l'espace de départ (nombre de colonnes).
- La ligne $i$ correspond au vecteur gradient $\nabla f_i(a)^T$.

**Exemples** :
Soit $f: \mathbb{R}^2 \to \mathbb{R}^3$ définie par $f(x,y) = (x^2y, \sin(x+y), e^{xy})^T$.
$$
J_f(x,y) = \begin{pmatrix}
2xy & x^2 \\
\cos(x+y) & \cos(x+y) \\
y e^{xy} & x e^{xy}
\end{pmatrix}
$$
En $a = (0, \pi)$, $J_f(0, \pi) = \begin{pmatrix} 0 & 0 \\ -1 & -1 \\ \pi & 0 \end{pmatrix}$.

### Règle de la Chaîne (Chain Rule)

Soit $U$ un ouvert de $\mathbb{R}^n$, $V$ un ouvert de $\mathbb{R}^p$.
Soit $f : U \to V$ et $g : V \to \mathbb{R}^m$.

**Théorème** : Si $f$ est différentiable en $a \in U$ et $g$ est différentiable en $f(a) \in V$, alors la fonction composée $h = g \circ f$ est différentiable en $a$. De plus, sa différentielle est la composition des différentielles :
$$ d(g \circ f)_a = dg_{f(a)} \circ df_a $$
Matriciellement, cela se traduit par le produit des matrices jacobiennes :
$$ J_{g \circ f}(a) = J_g(f(a)) \times J_f(a) $$

**Notations et Précisions** :
- **Compatibilité des tailles** : $J_g(f(a))$ est de taille $m \times p$ et $J_f(a)$ est de taille $p \times n$. Le produit est bien de taille $m \times n$, ce qui correspond à la matrice jacobienne de $h : \mathbb{R}^n \to \mathbb{R}^m$.
- L'ordre de multiplication est strictement de la gauche vers la droite par rapport à la composition (de l'extérieur vers l'intérieur).

**Exemples** :
Si $f(t) = (t, t^2)^T$ (courbe de $\mathbb{R} \to \mathbb{R}^2$) et $g(x,y) = x^2 + y^2$ (fonction de $\mathbb{R}^2 \to \mathbb{R}$).
$J_f(t) = \begin{pmatrix} 1 \\ 2t \end{pmatrix}$. $J_g(x,y) = \begin{pmatrix} 2x & 2y \end{pmatrix}$.
Alors $J_{g \circ f}(t) = J_g(t, t^2) J_f(t) = \begin{pmatrix} 2t & 2t^2 \end{pmatrix} \begin{pmatrix} 1 \\ 2t \end{pmatrix} = 2t + 4t^3$.
On vérifie : $h(t) = t^2 + t^4$, d'où $h'(t) = 2t + 4t^3$.

**Cas particuliers et contre-exemples** :
Si $f$ ou $g$ admet des dérivées partielles mais n'est pas différentiable, la formule de la chaîne peut tomber en défaut. La différentiabilité (existence d'un plan tangent approchant) est cruciale, la simple dérivabilité directionnelle ne suffit pas.

## 3. Démonstrations

### Preuve de la Règle de la Chaîne

**Objectif** : Démontrer que $d(g \circ f)_a = dg_{f(a)} \circ df_a$.

**Preuve pas-à-pas** :
1. Par définition de la différentiabilité de $f$ en $a$ :
   Pour tout accroissement $h \in \mathbb{R}^n$,
   $$ f(a+h) = f(a) + df_a(h) + \|h\|\epsilon_1(h) $$
   avec $\lim_{h \to 0} \epsilon_1(h) = 0$.
   Posons $k(h) = df_a(h) + \|h\|\epsilon_1(h)$. Notons que $f(a+h) = f(a) + k(h)$ et que $k(h) \to 0$ lorsque $h \to 0$.

2. Par définition de la différentiabilité de $g$ en $b = f(a)$ :
   Pour tout accroissement $k \in \mathbb{R}^p$,
   $$ g(b+k) = g(b) + dg_b(k) + \|k\|\epsilon_2(k) $$
   avec $\lim_{k \to 0} \epsilon_2(k) = 0$. On pose conventionnellement $\epsilon_2(0) = 0$ pour prolonger par continuité.

3. Substituons $k(h)$ dans le développement de $g$ :
   $$ (g \circ f)(a+h) = g(f(a+h)) = g(f(a) + k(h)) $$
   $$ (g \circ f)(a+h) = g(f(a)) + dg_{f(a)}(k(h)) + \|k(h)\|\epsilon_2(k(h)) $$

4. Exploitons la linéarité de $dg_{f(a)}$ pour développer $dg_{f(a)}(k(h))$ :
   $$ dg_{f(a)}(k(h)) = dg_{f(a)}(df_a(h) + \|h\|\epsilon_1(h)) = dg_{f(a)}(df_a(h)) + \|h\| dg_{f(a)}(\epsilon_1(h)) $$

5. Regroupons les termes pour former le développement limité de $g \circ f$ :
   $$ (g \circ f)(a+h) = (g \circ f)(a) + (dg_{f(a)} \circ df_a)(h) + R(h) $$
   où le reste est $R(h) = \|h\| dg_{f(a)}(\epsilon_1(h)) + \|k(h)\|\epsilon_2(k(h))$.

6. Montrons que $R(h) = o(\|h\|)$ (c'est-à-dire $\lim_{h \to 0} \frac{R(h)}{\|h\|} = 0$) :
   $$ \frac{R(h)}{\|h\|} = dg_{f(a)}(\epsilon_1(h)) + \frac{\|k(h)\|}{\|h\|} \epsilon_2(k(h)) $$
   - Comme $\epsilon_1(h) \to 0$ et que l'application linéaire $dg_{f(a)}$ est continue (en dimension finie), $dg_{f(a)}(\epsilon_1(h)) \to 0$.
   - Majorons la norme de l'accroissement $k(h)$ :
     $$ \|k(h)\| = \|df_a(h) + \|h\|\epsilon_1(h)\| \le \|df_a\| \cdot \|h\| + \|h\| \|\epsilon_1(h)\| = \|h\| (\|df_a\| + \|\epsilon_1(h)\|) $$
     Ainsi, le ratio $\frac{\|k(h)\|}{\|h\|}$ est borné au voisinage de $0$.
   - Puisque $k(h) \to 0$ lorsque $h \to 0$, on a $\epsilon_2(k(h)) \to 0$.
   Le produit d'une fonction bornée et d'une fonction tendant vers 0 tend vers 0.

7. Conclusion :
   $$ (g \circ f)(a+h) = (g \circ f)(a) + (dg_{f(a)} \circ df_a)(h) + o(\|h\|) $$
   L'application $L = dg_{f(a)} \circ df_a$ est linéaire continue (composée de deux linéaires continues), elle satisfait l'équation de différentiabilité. Par unicité, la différentielle de la composée est la composée des différentielles. $\blacksquare$

## 4. Application en IA : Rétropropagation

La Rétropropagation (Backpropagation) repose fondamentalement sur le calcul vectoriel de la Règle de la Chaîne. Un réseau de neurones multicouche est une fonction :
$$ F(x) = (\sigma_L \circ W_L \circ \sigma_{L-1} \circ W_{L-1} \dots \circ \sigma_1 \circ W_1)(x) $$
Où $W_l$ est l'application linéaire (poids de la couche) et $\sigma_l$ la fonction d'activation non linéaire.

Pour optimiser les poids $W_l$, on doit évaluer le gradient de la fonction de perte $L(F(x), y)$ par rapport à ces paramètres. La Jacobienne totale s'écrirait comme un immense produit matriciel de Jacobiennes locales. Pour éviter de calculer et stocker des matrices géantes, l'algorithme procède à des **Vecteur-Jacobian Products (VJP)**. On commence par la fin (la perte est un scalaire, son gradient est un vecteur) et on multiplie itérativement ce vecteur par la transposée de la jacobienne de la couche précédente :
$$ \delta_l = \left( J_{\sigma_l} \right)^T \cdot W_{l+1}^T \cdot \delta_{l+1} $$
L'élégance de cette propagation arrière des erreurs tient entièrement à l'associativité du produit matriciel issu de la différentielle des fonctions composées.
