---
uuid: "jalon-25"
title: "Formes bilinéaires, formes sesquilinéaires, produit scalaire et inégalité de Cauchy-Schwarz"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/similarite
prev: "[[Jalon-24.md]]"
next: "[[Jalon 26 (Espaces euclidiens).md]]"
---

# Jalon 25 : Formes bilinéaires, formes sesquilinéaires, produit scalaire et inégalité de Cauchy-Schwarz

## 1. L'Aube d'une Géométrie Abstraite : Mesurer l'Invisible

Avant d'aborder les structures formelles, il convient de s'imprégner de la genèse de ces concepts. Depuis les Grecs anciens, la notion de distance et d'angle était intrinsèquement liée à la géométrie euclidienne tridimensionnelle, régie par le théorème de Pythagore. Cependant, à mesure que l'algèbre linéaire s'est développée aux XIXe et XXe siècles, sous l'impulsion de mathématiciens comme Hermann Grassmann et David Hilbert, le besoin de généraliser ces notions géométriques à des espaces abstraits s'est fait sentir.

Comment mesurer un "angle" entre deux fonctions continues ? Comment évaluer la "distance" entre deux matrices ? C'est ici qu'intervient la forme bilinéaire. Une forme bilinéaire agit comme une lentille mathématique qui, à partir de deux objets d'un espace vectoriel, produit un scalaire permettant d'évaluer leur corrélation. Le produit scalaire en est l'incarnation la plus pure, offrant une symétrie parfaite et une mesure de positivité définie. Ce concept fondamental transcende la simple géométrie : en intelligence artificielle, par exemple, la similarité cosinus, directement issue du produit scalaire abstrait, permet de quantifier la proximité sémantique entre deux textes plongés dans un espace latent de très grande dimension.

## 2. Définitions et Structures Algébriques

### 2.1 Formes Bilinéaires et Sesquilinaires

Soit $\mathbb{K}$ un corps commutatif (typiquement $\mathbb{R}$ ou $\mathbb{C}$) et $E$ un $\mathbb{K}$-espace vectoriel.

**Définition (Forme bilinéaire) :**
Une application $B : E \times E \to \mathbb{K}$ est appelée forme bilinéaire si elle est linéaire par rapport à chacune de ses variables. Formellement, pour tout $x, y, z \in E$ et tout $\lambda \in \mathbb{K}$ :
1. Linéarité à gauche : $B(\lambda x + y, z) = \lambda B(x, z) + B(y, z)$
2. Linéarité à droite : $B(x, \lambda y + z) = \lambda B(x, y) + B(x, z)$

**Définition (Forme symétrique et antisymétrique) :**
- $B$ est symétrique si pour tout $x, y \in E$, $B(x, y) = B(y, x)$.
- $B$ est antisymétrique si pour tout $x, y \in E$, $B(x, y) = -B(y, x)$.

Lorsque le corps de base est $\mathbb{C}$, la stricte bilinéarité s'avère inadaptée pour définir des notions de distance (notamment pour garantir qu'un "carré" soit un réel positif). On introduit alors la notion de forme sesquilinéaire.

**Définition (Forme sesquilinéaire) :**
Une application $\phi : E \times E \to \mathbb{C}$ est sesquilinéaire si elle est linéaire à droite et semi-linéaire (ou antilinéaire) à gauche :
1. $\phi(\lambda x + y, z) = \bar{\lambda} \phi(x, z) + \phi(y, z)$ pour tout $\lambda \in \mathbb{C}$
2. $\phi(x, \lambda y + z) = \lambda \phi(x, y) + \phi(x, z)$ pour tout $\lambda \in \mathbb{C}$

*(Note : Dans la littérature française, la convention peut être semi-linéaire à gauche, tandis que dans la littérature anglo-saxonne, elle est souvent semi-linéaire à droite.)*

**Définition (Forme hermitienne) :**
Une forme sesquilinéaire $\phi$ est dite hermitienne (ou à symétrie hermitienne) si pour tout $x, y \in E$, $\phi(x, y) = \overline{\phi(y, x)}$.

### 2.2 Formes Quadratiques et Identité de Polarisation

À toute forme bilinéaire symétrique $B$ sur $E$, on associe une forme quadratique $q : E \to \mathbb{K}$ définie par $q(x) = B(x, x)$.
L'identité de polarisation permet, réciproquement, de retrouver la forme bilinéaire symétrique à partir de sa forme quadratique. Si la caractéristique de $\mathbb{K}$ est différente de $2$, on a :
$$B(x, y) = \frac{1}{4} \left( q(x + y) - q(x - y) \right)$$
Ou de manière équivalente :
$$B(x, y) = \frac{1}{2} \left( q(x + y) - q(x) - q(y) \right)$$

### 2.3 Produit Scalaire et Espaces Préhilbertiens

**Définition (Produit scalaire) :**
Un produit scalaire sur un $\mathbb{R}$-espace vectoriel $E$ est une forme bilinéaire $\langle \cdot , \cdot \rangle : E \times E \to \mathbb{R}$ qui est :
1. **Symétrique :** $\langle x, y \rangle = \langle y, x \rangle$
2. **Positive :** Pour tout $x \in E$, $\langle x, x \rangle \ge 0$
3. **Définie :** Pour tout $x \in E$, $\langle x, x \rangle = 0 \iff x = 0$
Un espace vectoriel réel muni d'un produit scalaire est appelé **espace préhilbertien réel**.

La quantité $\|x\| = \sqrt{\langle x, x \rangle}$ définit alors une norme sur $E$, appelée norme euclidienne associée au produit scalaire.

## 3. L'Inégalité Fondamentale de Cauchy-Schwarz

Ce théorème est la clé de voûte de toute l'analyse hilbertienne. Il formalise l'intuition que la projection orthogonale d'un vecteur sur un autre ne peut excéder la longueur du vecteur initial.

**Théorème (Inégalité de Cauchy-Schwarz) :**
Soit $E$ un espace vectoriel muni d'un produit scalaire $\langle \cdot , \cdot \rangle$. Pour tout couple $(x, y) \in E^2$, on a :
$$|\langle x, y \rangle| \le \|x\| \cdot \|y\|$$
De plus, il y a égalité si et seulement si les vecteurs $x$ et $y$ sont colinéaires.

**Démonstration Complète et Rigoureuse :**
Soient $x, y \in E$. Si $y = 0$, l'inégalité devient $|0| \le \|x\| \cdot 0$, ce qui est trivialement vrai $0 \le 0$, et les vecteurs sont bien colinéaires (car $y = 0 \cdot x$).

Supposons désormais $y \neq 0$.
Considérons la fonction polynomiale $P : \mathbb{R} \to \mathbb{R}$ définie pour tout $t \in \mathbb{R}$ par :
$$P(t) = \|x + ty\|^2$$
Par définition de la norme issue du produit scalaire, on a :
$$P(t) = \langle x + ty, x + ty \rangle$$
En développant par bilinéarité et en utilisant la symétrie du produit scalaire, on obtient :
$$P(t) = \langle x, x \rangle + t\langle x, y \rangle + t\langle y, x \rangle + t^2\langle y, y \rangle$$
$$P(t) = \|x\|^2 + 2t\langle x, y \rangle + t^2\|y\|^2$$

Cette fonction est un polynôme du second degré en $t$. Puisque $\|x + ty\|^2 \ge 0$ par la positivité du produit scalaire, on a $P(t) \ge 0$ pour tout réel $t$. Un polynôme du second degré, à coefficients réels, qui garde un signe constant positif ou nul sur $\mathbb{R}$, possède un discriminant réduit $\Delta'$ négatif ou nul.
Calculons ce discriminant réduit. Le trinôme s'écrit $at^2 + 2b't + c$ avec $a = \|y\|^2$, $b' = \langle x, y \rangle$, et $c = \|x\|^2$.
$$\Delta' = (b')^2 - ac = \langle x, y \rangle^2 - \|y\|^2 \|x\|^2$$
La condition $\Delta' \le 0$ se traduit par :
$$\langle x, y \rangle^2 - \|y\|^2 \|x\|^2 \le 0$$
$$\langle x, y \rangle^2 \le \|x\|^2 \|y\|^2$$
En prenant la racine carrée de part et d'autre, on obtient l'inégalité de Cauchy-Schwarz :
$$|\langle x, y \rangle| \le \|x\| \cdot \|y\|$$

**Étude du cas d'égalité :**
L'égalité $|\langle x, y \rangle| = \|x\| \cdot \|y\|$ équivaut à $\Delta' = 0$.
Or, $\Delta' = 0$ signifie que le polynôme $P(t)$ admet une unique racine réelle $t_0$.
Ainsi, il existe un $t_0 \in \mathbb{R}$ tel que $P(t_0) = 0$, soit $\|x + t_0 y\|^2 = 0$.
Par le caractère défini du produit scalaire, cela implique $x + t_0 y = 0$, donc $x = -t_0 y$.
Les vecteurs $x$ et $y$ sont donc colinéaires. Réciproquement, si $x = \lambda y$, le calcul direct donne $|\langle \lambda y, y \rangle| = |\lambda| \|y\|^2 = \|\lambda y\| \|y\| = \|x\| \|y\|$, ce qui clôt la démonstration.

## 4. Conséquence : L'Inégalité Triangulaire (Minkowski)

À partir de l'inégalité de Cauchy-Schwarz, on peut démontrer que la fonction $x \mapsto \sqrt{\langle x, x \rangle}$ satisfait les axiomes d'une norme, en particulier l'inégalité triangulaire.

**Théorème :**
Pour tout $x, y \in E$, $\|x + y\| \le \|x\| + \|y\|$.

**Démonstration :**
Calculons le carré de la norme de la somme :
$$\|x + y\|^2 = \langle x + y, x + y \rangle = \|x\|^2 + 2\langle x, y \rangle + \|y\|^2$$
Puisque pour tout réel $a$, $a \le |a|$, on a $\langle x, y \rangle \le |\langle x, y \rangle|$. En utilisant l'inégalité de Cauchy-Schwarz $|\langle x, y \rangle| \le \|x\| \cdot \|y\|$, on majore :
$$\|x + y\|^2 \le \|x\|^2 + 2|\langle x, y \rangle| + \|y\|^2$$
$$\|x + y\|^2 \le \|x\|^2 + 2\|x\| \cdot \|y\| + \|y\|^2$$
Le terme de droite est un produit remarquable :
$$\|x + y\|^2 \le (\|x\| + \|y\|)^2$$
Puisque les quantités en jeu sont positives, la croissance de la fonction racine carrée sur $\mathbb{R}^+$ permet de conclure :
$$\|x + y\| \le \|x\| + \|y\|$$
