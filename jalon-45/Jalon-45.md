---
uuid: "jalon-45"
title: "Différentiabilité et Gradient"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/optimisation
prev: "[[Jalon 44 (Fonctions de plusieurs variables).md]]"
next: "[[Jalon 46 (Matrice jacobienne).md]]"
---
# Jalon 45 : Différentiabilité et Gradient

## 1. Genèse et fondations géométriques

L'étude des fonctions d'une variable réelle a permis de comprendre les variations et la notion de tangence via la dérivée. Cependant, lorsque l'on considère une fonction définie sur un ouvert $U \subset \mathbb{R}^n$, la géométrie du problème se complexifie considérablement. Le graphe d'une fonction $f : U \to \mathbb{R}$ n'est plus une simple courbe, mais une hypersurface dans $\mathbb{R}^{n+1}$. La question se pose alors : comment caractériser l'inclinaison de ce terrain multidimensionnel en un point donné ?

Historiquement, des mathématiciens comme Euler et Lagrange se sont penchés sur la variation d'une fonction de plusieurs variables lorsqu'on perturbe uniquement l'une d'entre elles, introduisant ainsi les dérivées partielles. Néanmoins, Cauchy et plus tard Fréchet ont mis en évidence qu'une simple combinaison de dérivées selon les axes canoniques ne suffit pas pour garantir une approximation affine globale valide. L'impasse géométrique est la suivante : une fonction peut admettre des dérivées dans toutes les directions en un point, et même être continue le long de chaque axe, tout en présentant une « brisure » fondamentale, l'empêchant d'admettre un véritable hyperplan tangent.

C'est ainsi qu'est née la notion stricte de différentiabilité. Elle exige l'existence d'une approximation linéaire uniforme autour du point d'étude. Si cette approximation existe, le terrain est localement plat, et la direction de sa plus forte pente est alors donnée par un vecteur unique, que l'on nomme le gradient. Ce concept est la pierre angulaire de l'analyse multivariée et le moteur fondamental de tous les processus d'optimisation modernes.

## 2. Définitions et Théorèmes Fondamentaux

Considérons un espace euclidien $\mathbb{R}^n$ muni de son produit scalaire canonique $\langle \cdot, \cdot \rangle$ et de la norme euclidienne associée $\| \cdot \|$. Soit $U$ un sous-ensemble ouvert de $\mathbb{R}^n$ et $f : U \to \mathbb{R}$ une application.

### Dérivées partielles et différentielle

**Définition 1 (Dérivée partielle).** Soit $a = (a_1, \dots, a_n) \in U$. Pour tout $i \in \{1, \dots, n\}$, on appelle $i$-ème dérivée partielle de $f$ en $a$, notée $\frac{\partial f}{\partial x_i}(a)$, la limite (lorsqu'elle existe) du taux d'accroissement dans la direction du vecteur de base $e_i$ :
$$ \frac{\partial f}{\partial x_i}(a) = \lim_{t \to 0} \frac{f(a + t e_i) - f(a)}{t} $$

Cette quantité mesure la pente de la fonction le long de l'axe $x_i$.

**Définition 2 (Différentiabilité).** L'application $f$ est dite différentiable au point $a \in U$ s'il existe une application linéaire $L : \mathbb{R}^n \to \mathbb{R}$ telle que, pour tout vecteur d'accroissement $h \in \mathbb{R}^n$ vérifiant $a+h \in U$, on ait le développement limité à l'ordre 1 :
$$ f(a+h) = f(a) + L(h) + \|h\| \epsilon(h) $$
où $\epsilon : V \to \mathbb{R}$ est une fonction définie sur un voisinage de $0$ telle que $\lim_{h \to 0} \epsilon(h) = 0$.
L'application linéaire $L$, si elle existe, est unique. Elle est appelée la différentielle de $f$ en $a$ et est notée $df_a$.

**Exemple concret immédiat.**
Soit $f : \mathbb{R}^2 \to \mathbb{R}$ définie par $f(x,y) = x^2 y$. Montrons que $f$ est différentiable en $a = (x_0, y_0)$ et calculons sa différentielle.
Soit $h = (h_1, h_2) \in \mathbb{R}^2$.
$$ f(x_0+h_1, y_0+h_2) = (x_0+h_1)^2 (y_0+h_2) = (x_0^2 + 2x_0h_1 + h_1^2)(y_0+h_2) $$
$$ f(x_0+h_1, y_0+h_2) = x_0^2 y_0 + x_0^2 h_2 + 2x_0y_0h_1 + 2x_0h_1h_2 + h_1^2 y_0 + h_1^2 h_2 $$
On identifie $f(a) = x_0^2 y_0$. Posons l'application linéaire $L(h_1, h_2) = 2x_0y_0 h_1 + x_0^2 h_2$.
Le reste est $R(h) = 2x_0h_1h_2 + y_0h_1^2 + h_1^2h_2$.
Montrons que $\frac{|R(h)|}{\|h\|} \to 0$ lorsque $h \to 0$.
Puisque $|h_1| \le \|h\|$ et $|h_2| \le \|h\|$, on a :
$$ |R(h)| \le 2|x_0| \|h\|^2 + |y_0| \|h\|^2 + \|h\|^3 = \|h\|^2 (2|x_0| + |y_0| + \|h\|) $$
Ainsi, $\frac{|R(h)|}{\|h\|} \le \|h\| (2|x_0| + |y_0| + \|h\|)$, ce qui tend bien vers $0$ quand $\|h\| \to 0$.
Donc $f$ est différentiable en $(x_0, y_0)$ et $df_{(x_0,y_0)}(h) = 2x_0y_0 h_1 + x_0^2 h_2$.

### Gradient et lien avec la différentielle

Si $f$ est différentiable en $a$, il découle du théorème de représentation de Riesz (ou simplement de la structure des formes linéaires en dimension finie) qu'il existe un unique vecteur, appelé **gradient** de $f$ en $a$ et noté $\nabla f(a)$, tel que pour tout $h \in \mathbb{R}^n$ :
$$ df_a(h) = \langle \nabla f(a), h \rangle $$
Dans la base canonique, les composantes du gradient sont exactement les dérivées partielles :
$$ \nabla f(a) = \left( \frac{\partial f}{\partial x_1}(a), \dots, \frac{\partial f}{\partial x_n}(a) \right)^T $$

**Théorème 1 (Classe $\mathcal{C}^1$).** Si $f$ admet des dérivées partielles par rapport à toutes ses variables sur $U$, et si ces dérivées partielles sont continues en un point $a \in U$, alors $f$ est différentiable en $a$.

**Cas pathologique.** La simple existence des dérivées partielles en un point n'assure ni la continuité ni la différentiabilité.
Soit $f(x,y) = \frac{xy}{x^2+y^2}$ pour $(x,y) \neq (0,0)$ et $f(0,0)=0$.
Les dérivées partielles en $(0,0)$ valent $0$. Pourtant $f$ n'est pas continue en $(0,0)$ car $f(t,t) = \frac{1}{2} \neq 0$. Ainsi, $f$ n'est pas différentiable.

## 3. Démonstrations rigoureuses

**Théorème 2.** Si $f : U \to \mathbb{R}$ est différentiable en $a \in U$, alors $f$ est continue en $a$.

*Démonstration.*
Par hypothèse de différentiabilité, pour tout $h$ tel que $a+h \in U$, on a :
$$ f(a+h) = f(a) + df_a(h) + \|h\|\epsilon(h) $$
où $\lim_{h \to 0} \epsilon(h) = 0$.
L'application différentielle $df_a : \mathbb{R}^n \to \mathbb{R}$ est une application linéaire définie sur un espace de dimension finie, elle est donc nécessairement continue. Ainsi, $\lim_{h \to 0} df_a(h) = 0$.
De plus, le terme de reste $\|h\|\epsilon(h)$ tend trivialement vers $0$ lorsque $h \to 0$.
En passant à la limite dans l'équation du développement limité, on obtient :
$$ \lim_{h \to 0} f(a+h) = f(a) + \lim_{h \to 0} df_a(h) + \lim_{h \to 0} \|h\|\epsilon(h) = f(a) + 0 + 0 = f(a) $$
Ce qui caractérise exactement la continuité de $f$ au point $a$. $\blacksquare$

**Propriété de la plus forte pente.**
Soit $f$ différentiable en $a$. La dérivée directionnelle de $f$ dans la direction d'un vecteur unitaire $u \in \mathbb{R}^n$ (tel que $\|u\|=1$) est donnée par $df_a(u) = \langle \nabla f(a), u \rangle$.
Par l'inégalité de Cauchy-Schwarz :
$$ |\langle \nabla f(a), u \rangle| \le \|\nabla f(a)\| \|u\| = \|\nabla f(a)\| $$
L'égalité est atteinte si et seulement si $u$ est colinéaire et de même sens que $\nabla f(a)$, c'est-à-dire $u = \frac{\nabla f(a)}{\|\nabla f(a)\|}$ (à condition que le gradient soit non nul).
Ainsi, le gradient indique précisément la direction dans laquelle la fonction croît le plus rapidement.

## 4. Applications en Physique et Intelligence Artificielle

En physique mathématique, le concept de gradient est omniprésent. Dans le cadre de la théorie du potentiel (électrostatique ou gravitationnelle), le champ de force conservatif $\vec{F}$ dérive toujours d'un potentiel scalaire $V$ tel que $\vec{F} = -\nabla V$. Le fluide ou la particule cherchera naturellement à suivre la direction opposée au gradient pour minimiser son énergie potentielle.

En Intelligence Artificielle, cette propriété géométrique est le cœur algorithmique de l'apprentissage automatique, à travers la méthode de descente de gradient (Gradient Descent).
Lors de l'entraînement d'un réseau de neurones paramétré par un vecteur très grande dimension $\theta \in \mathbb{R}^p$, on définit une fonction de coût $\mathcal{L}(\theta) : \mathbb{R}^p \to \mathbb{R}$ mesurant l'écart entre les prédictions du modèle et la réalité. L'objectif est de trouver le point minimisant cette hypersurface complexe.
À chaque itération d'apprentissage, on calcule le gradient $\nabla \mathcal{L}(\theta)$, qui concentre toutes les dérivées partielles du coût par rapport à chaque poids synaptique, et l'on met à jour les paramètres dans la direction de la plus forte descente :
$$ \theta_{t+1} = \theta_t - \eta \nabla \mathcal{L}(\theta_t) $$
où $\eta > 0$ représente le pas d'apprentissage (learning rate). La différentiabilité de la fonction de coût, assurée notamment par l'usage de fonctions d'activation régulières ou différentiables presque partout (comme ReLU), est la condition _sine qua non_ qui permet à l'algorithme de converger vers un optimum local de la fonction de perte.
