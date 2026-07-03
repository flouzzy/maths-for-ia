---
uuid: "jalon-11"
title: "Formes linéaires, hyperplans, espace dual et orthogonalité en dimension finie"
year: 1
trimester: 1
tags:
  - math/algebre-lineaire
  - ia/dualite
prev: "[[Jalon 10 (Changements de base).md]]"
next: "[[Jalon 12 (Livrable IA).md]]"
---
# Jalon 11 : Formes linéaires, hyperplans, espace dual et orthogonalité en dimension finie

## 1. Présentation du concept clé

La genèse des formes linéaires trouve son origine dans le désir fondamental des mathématiciens de quantifier et de mesurer les objets géométriques et algébriques. Historiquement, l'étude des espaces vectoriels s'est d'abord concentrée sur la structure interne des vecteurs, vus comme des entités indépendantes munies d'opérations d'addition et de dilatation. Cependant, la mathématique de la fin du dix-neuvième siècle, sous l'impulsion de géomètres comme Hermann Grassmann et d'algébristes tels qu'Arthur Cayley, a révélé qu'un espace vectoriel ne prend sa pleine mesure que lorsqu'il est confronté aux instruments capables de l'évaluer.

Un vecteur abstrait, isolé, manque de repères extrinsèques. Pour comprendre sa nature profonde, il est nécessaire de le soumettre à des "tests" ou des "instruments de mesure" qui renvoient une valeur scalaire. Ces instruments, par essence, doivent respecter la structure linéaire de l'espace : la mesure d'une somme d'objets doit correspondre à la somme des mesures, et l'amplification d'un objet doit amplifier sa mesure de manière proportionnelle. C'est précisément cette idée qui donne naissance aux formes linéaires. Elles constituent des observations parfaites, des sondes mathématiques qui projettent la richesse multidimensionnelle d'un espace vectoriel sur la droite des réels ou sur un corps abstrait.

De cette notion d'instrument de mesure émerge une structure géométrique capitale : l'hyperplan. Lorsqu'un observateur regarde un paysage, l'horizon représente la frontière exacte où la hauteur perçue s'annule. Mathématiquement, un hyperplan est le noyau d'une forme linéaire non nulle. Il divise l'espace en deux demi-espaces stricts, imposant une séparation fondamentale. La dualité s'établit alors comme un changement de paradigme. Au lieu d'étudier les points de l'espace de manière intrinsèque, nous étudions l'espace de toutes les formes linéaires possibles, c'est-à-dire l'espace dual. Cette inversion de perspective permet de caractériser des sous-espaces par les équations qui les annulent, ouvrant la voie à l'orthogonalité au sens dual, et jetant les bases des théories d'optimisation modernes.

## 2. Formalisation

### A. Espace Dual et Formes Linéaires

Soit $\mathbb{K}$ un corps commutatif (typiquement $\mathbb{R}$ ou $\mathbb{C}$) et $E$ un $\mathbb{K}$-espace vectoriel.

**Définition (Forme linéaire) :**
Une application $\varphi : E \to \mathbb{K}$ est appelée une forme linéaire si elle est un morphisme d'espaces vectoriels, c'est-à-dire si elle vérifie :
$$ \forall (x, y) \in E^2, \forall \lambda \in \mathbb{K}, \quad \varphi(\lambda x + y) = \lambda \varphi(x) + \varphi(y) $$

**Définition (Espace dual) :**
L'ensemble des formes linéaires sur $E$, noté $E^*$, est appelé l'espace dual de $E$. Il s'identifie à l'espace des applications linéaires $\mathcal{L}(E, \mathbb{K})$. Muni de l'addition des fonctions et de la multiplication par un scalaire, $E^*$ est lui-même un $\mathbb{K}$-espace vectoriel.

**Exemple de validation :**
Dans $\mathbb{R}^n$, l'application $\varphi(x_1, \dots, x_n) = x_1$ (projection sur la première coordonnée) est une forme linéaire. En revanche, l'application $\psi(x_1, \dots, x_n) = x_1^2$ ne l'est pas, car $\psi(2x) = 4\psi(x) \neq 2\psi(x)$.

### B. Hyperplans

**Définition (Hyperplan) :**
Un sous-espace vectoriel $H$ de $E$ est un hyperplan s'il existe une forme linéaire non nulle $\varphi \in E^*$ telle que $H = \ker(\varphi)$.
De manière équivalente, $H$ est un hyperplan si et seulement si $H \oplus \text{Vect}(v) = E$ pour tout vecteur $v \in E \setminus H$.

**Exemple de validation :**
Dans $\mathbb{R}^3$, le plan d'équation $x + y + z = 0$ est le noyau de la forme linéaire $\varphi(x, y, z) = x + y + z$. C'est un hyperplan de $\mathbb{R}^3$. Le vecteur $v = (1, 0, 0)$ n'appartient pas à ce plan, et on a bien $\mathbb{R}^3 = H \oplus \text{Vect}(v)$.

### C. Base Duale et Bidual

Soit $E$ un espace vectoriel de dimension finie $n$, et soit $\mathcal{B} = (e_1, \dots, e_n)$ une base de $E$.

**Définition (Base duale) :**
Pour tout $i \in \{1, \dots, n\}$, on définit la forme linéaire $e_i^* : E \to \mathbb{K}$ comme l'unique forme linéaire prenant la valeur $1$ sur $e_i$ et $0$ sur les $e_j$ pour $j \neq i$. Formellement :
$$ \forall j \in \{1, \dots, n\}, \quad e_i^*(e_j) = \delta_{i,j} $$
où $\delta_{i,j}$ est le symbole de Kronecker. La famille $\mathcal{B}^* = (e_1^*, \dots, e_n^*)$ constitue une base de $E^*$, appelée base duale de $\mathcal{B}$.

**Définition (Bidual) :**
Le bidual de $E$, noté $E^{**}$, est l'espace dual de l'espace dual $E^*$, c'est-à-dire $E^{**} = (E^*)^*$.

**Cas pathologique et dimension infinie :**
L'isomorphisme entre un espace et son bidual est strictement canonique (indépendant du choix d'une base) uniquement en dimension finie. En dimension infinie, l'application canonique de $E$ vers $E^{**}$ est injective mais jamais surjective : l'espace n'est pas réflexif algébriquement.

### D. Orthogonalité au sens de la dualité

**Définition (Orthogonal) :**
Soit $A$ une partie de $E$. L'orthogonal de $A$, noté $A^\circ$ (ou parfois $A^\perp$ par abus de notation), est l'ensemble des formes linéaires qui s'annulent sur $A$ :
$$ A^\circ = \{ \varphi \in E^* \mid \forall x \in A, \varphi(x) = 0 \} $$
C'est un sous-espace vectoriel de $E^*$.

De manière duale, pour une partie $B$ de $E^*$, son orthogonal dans $E$ est :
$$ B^\circ = \{ x \in E \mid \forall \varphi \in B, \varphi(x) = 0 \} $$

## 3. Démonstrations

### Démonstration 1 : Dimension de l'espace dual
**Théorème :** Si $E$ est un espace vectoriel de dimension finie $n$, alors son dual $E^*$ est également de dimension $n$.

**Démonstration pas-à-pas :**
1. Soit $\mathcal{B} = (e_1, \dots, e_n)$ une base de $E$. Nous allons montrer que la famille $\mathcal{B}^* = (e_1^*, \dots, e_n^*)$ construite précédemment est une base de $E^*$.
2. **Indépendance linéaire :** Soient $\lambda_1, \dots, \lambda_n \in \mathbb{K}$ tels que $\sum_{i=1}^n \lambda_i e_i^* = 0_{E^*}$.
3. La fonction nulle $0_{E^*}$ évalue tout vecteur à zéro. En particulier, pour tout $j \in \{1, \dots, n\}$ :
   $$ \left( \sum_{i=1}^n \lambda_i e_i^* \right)(e_j) = 0 $$
4. Par linéarité, la somme devient :
   $$ \sum_{i=1}^n \lambda_i e_i^*(e_j) = 0 $$
5. Or, par définition de la base duale, $e_i^*(e_j) = \delta_{i,j}$. La somme se réduit au seul terme où $i = j$ :
   $$ \lambda_j \cdot 1 = 0 \implies \lambda_j = 0 $$
6. Ce résultat étant vrai pour tout $j$, la famille $(e_1^*, \dots, e_n^*)$ est libre.
7. **Caractère générateur :** Soit $\varphi \in E^*$. Posons $\mu_i = \varphi(e_i)$ pour $i \in \{1, \dots, n\}$.
8. Considérons la forme linéaire $\psi = \sum_{i=1}^n \mu_i e_i^*$.
9. Pour tout vecteur de base $e_j$, nous avons :
   $$ \psi(e_j) = \sum_{i=1}^n \mu_i e_i^*(e_j) = \mu_j \cdot 1 = \mu_j = \varphi(e_j) $$
10. Deux applications linéaires qui coïncident sur une base coïncident sur tout l'espace. Par conséquent, $\varphi = \psi = \sum_{i=1}^n \mu_i e_i^*$.
11. La famille $\mathcal{B}^*$ engendre $E^*$.
12. Étant libre et génératrice, $\mathcal{B}^*$ est une base de $E^*$, qui possède $n$ éléments. Ainsi, $\dim(E^*) = n$.

### Démonstration 2 : Isomorphisme canonique avec le bidual
**Théorème :** En dimension finie, l'application $\Psi : E \to E^{**}$ définie par $\Psi(x)(\varphi) = \varphi(x)$ est un isomorphisme canonique.

**Démonstration pas-à-pas :**
1. **Linéarité de $\Psi$ :** Soient $x, y \in E$ et $\lambda \in \mathbb{K}$. Pour toute forme $\varphi \in E^*$ :
   $$ \Psi(\lambda x + y)(\varphi) = \varphi(\lambda x + y) $$
2. Par linéarité de la forme $\varphi$, on obtient :
   $$ \varphi(\lambda x + y) = \lambda \varphi(x) + \varphi(y) = \lambda \Psi(x)(\varphi) + \Psi(y)(\varphi) = (\lambda \Psi(x) + \Psi(y))(\varphi) $$
3. Cette égalité est vraie pour toute $\varphi$, d'où $\Psi(\lambda x + y) = \lambda \Psi(x) + \Psi(y)$. L'application $\Psi$ est bien linéaire.
4. **Injectivité de $\Psi$ :** Supposons qu'il existe $x \in E$ tel que $\Psi(x) = 0_{E^{**}}$.
5. Cela signifie que pour toute forme $\varphi \in E^*$, on a $\Psi(x)(\varphi) = 0$, donc $\varphi(x) = 0$.
6. Procédons par l'absurde et supposons que $x \neq 0_E$.
7. Comme $x$ est un vecteur non nul, on peut le compléter pour former une base $\mathcal{B} = (x, e_2, \dots, e_n)$ de $E$ (théorème de la base incomplète).
8. Considérons la forme coordonnée $x^*$ issue de la base duale de $\mathcal{B}$. Par définition, $x^*(x) = 1$.
9. Nous avons trouvé une forme linéaire $x^* \in E^*$ qui ne s'annule pas sur $x$, ce qui contredit l'hypothèse $\varphi(x) = 0$ pour toute $\varphi$.
10. Par conséquent, $x$ doit être le vecteur nul, $x = 0_E$. Le noyau de $\Psi$ est réduit à $\{0_E\}$, donc $\Psi$ est injective.
11. **Surjectivité par dimension :** Nous savons que $\dim(E) = n$. Par le théorème précédent, $\dim(E^*) = n$, et de nouveau, $\dim(E^{**}) = \dim(E^*) = n$.
12. $\Psi$ est une application linéaire injective entre deux espaces vectoriels de même dimension finie $n$. Le théorème du rang garantit alors qu'elle est un isomorphisme.

## 4. Exercices d'Application

*(Les exercices d'application et leurs démonstrations complètes sont développés dans les fichiers dédiés `Exo-01.md` à `Exo-10.md` de ce jalon.)*

## 5. Application en Intelligence Artificielle

Dans le cadre du Machine Learning, les hyperplans sont l'ossature algorithmique des méthodes de classification linéaire. Le concept de forme linéaire modélise la projection d'un vecteur de caractéristiques multidimensionnel (par exemple, les pixels d'une image ou les pondérations d'un texte) vers une variable de décision scalaire.

Un Support Vector Machine (SVM) cherche l'hyperplan optimal qui sépare deux classes de données. L'équation de cet hyperplan séparateur est $H = \{ x \in E \mid \varphi(x) + b = 0 \}$, où $\varphi \in E^*$ est la forme linéaire associée aux poids du modèle, et $b$ est le biais.

Plus profondément, la résolution analytique du SVM fait appel à la dualité de l'optimisation convexe (Dualité de Lagrange). Le problème primal, formulé dans l'espace des données $E$, implique de minimiser la norme des pondérations sous contraintes. Le problème dual, formulé par l'intermédiaire de l'espace dual $E^*$, convertit cette recherche complexe en une maximisation sur les variables duales (les multiplicateurs de Lagrange). Seuls les vecteurs support – ceux qui se situent sur les marges de l'hyperplan – posséderont des multiplicateurs non nuls. Cette transformation permet, grâce à l'isomorphisme et aux propriétés d'orthogonalité, de traiter des données en dimension infinie via l'astuce du noyau (kernel trick), révolutionnant ainsi l'apprentissage statistique.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 7 (Espaces vectoriels abstraits)]], [[Jalon 8 (Applications linéaires, noyau (ker), image (Im) et démonstration du théorème du rang)]]
- **Concepts Futurs dépendants :** [[Jalon 12 (Livrable IA)]], [[Jalon 121 (Ensembles convexes)]], [[Jalon 123 (Problèmes d'optimisation sous contraintes)]]
