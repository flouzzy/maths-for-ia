---
uuid: "jalon-44"
title: "Fonctions de plusieurs variables"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/topologie
prev: "[[Jalon 43 (Systèmes différentiels linéaires d'ordre 1 et calcul de l'exponentielle de matrice.).md]]"
next: "[[Jalon 45 (Différentiabilité).md]]"
---

# Jalon 44 : Fonctions de plusieurs variables

## 1. Genèse et Intuition Géométrique

Les mathématiques unidimensionnelles, bien que puissantes, se heurtent rapidement à une limite fondamentale lorsqu'il s'agit de décrire la réalité. Une trajectoire sur une ligne ne suffit pas à capturer le mouvement d'un fluide, la propagation d'une onde électromagnétique, ou la variation de température dans une pièce. La physique, la géométrie, et plus récemment les sciences computationnelles, nous obligent à considérer des phénomènes dont l'état dépend simultanément de plusieurs paramètres.

Historiquement, l'étude des fonctions de plusieurs variables émerge avec les travaux de mathématiciens comme Leonhard Euler, Augustin-Louis Cauchy et Carl Friedrich Gauss, qui cherchaient à formuler mathématiquement la mécanique céleste et la géométrie des surfaces. L'intuition géométrique devient alors cruciale : là où une fonction d'une variable se visualise comme une courbe dans un plan bidimensionnel, une fonction de deux variables $f(x, y)$ se représente comme une surface (une nappe) tridimensionnelle, semblable au relief d'un paysage naturel, et l'évaluation en un point $(x,y)$ correspond à l'altitude en ce point.

Lorsque le nombre de variables dépasse trois, la représentation visuelle directe échappe à nos sens, mais la structure topologique et algébrique demeure. C'est le triomphe de la formalisation mathématique d'Andrey Kolmogorov et d'autres figures de l'école analytique, qui ont permis d'étendre la notion de proximité, de voisinage et de continuité à des espaces de dimension quelconque, $\mathbb{R}^n$.

## 2. Espace de Départ et Voisinages dans $\mathbb{R}^n$

Pour étudier les fonctions définies sur plusieurs variables, il faut au préalable structurer l'espace de départ $\mathbb{R}^n$.

### Définition 2.1 : Structure et Norme sur $\mathbb{R}^n$
L'espace $\mathbb{R}^n$ est l'ensemble des $n$-uplets $x = (x_1, x_2, \ldots, x_n)$ où chaque $x_i \in \mathbb{R}$.
On le munit classiquement de la norme euclidienne, définie pour tout $x \in \mathbb{R}^n$ par :
$$ \|x\| = \sqrt{x_1^2 + x_2^2 + \ldots + x_n^2} = \left( \sum_{i=1}^n x_i^2 \right)^{1/2} $$
Cette norme induit une distance $d(x,y) = \|x - y\|$, qui permet de définir la notion de boule ouverte.
La boule ouverte de centre $a \in \mathbb{R}^n$ et de rayon $r > 0$ est l'ensemble :
$$ B(a, r) = \{ x \in \mathbb{R}^n \mid \|x - a\| < r \} $$

**Exemple Concret 1 :**
Dans $\mathbb{R}^2$, considérons le point $a = (1, 2)$ et un rayon $r = 1$.
La boule ouverte $B(a, 1)$ est l'ensemble des points $(x,y)$ tels que :
$$ \sqrt{(x - 1)^2 + (y - 2)^2} < 1 \implies (x - 1)^2 + (y - 2)^2 < 1 $$
Il s'agit de l'intérieur strict du disque centré en $(1,2)$ de rayon $1$. Un point comme $(1.5, 2)$ appartient à cette boule car $\sqrt{(0.5)^2 + 0^2} = 0.5 < 1$. Par contre, $(2, 2)$ n'y appartient pas.

## 3. Limites de Fonctions de Plusieurs Variables

### Définition 3.1 : Limite en un point
Soit $D \subset \mathbb{R}^n$ un ouvert, $a \in D$ (ou $a$ adhérent à $D$), et $f : D \setminus \{a\} \to \mathbb{R}^p$.
On dit que $f$ admet une limite $L \in \mathbb{R}^p$ en $a$ si et seulement si :
$$ \forall \varepsilon > 0, \exists \delta > 0, \forall x \in D, \quad (0 < \|x - a\| < \delta \implies \|f(x) - L\| < \varepsilon) $$

*Remarque essentielle :* Contrairement à la dimension 1 où l'on ne peut s'approcher de $a$ que par la gauche ou la droite, dans $\mathbb{R}^n$ il y a une infinité de directions, de chemins rectilignes, courbés ou en spirale pour s'approcher de $a$. Pour que la limite existe, elle doit être **la même indépendamment de la trajectoire**.

### Théorème 3.1 : Opérations sur les limites
Si $\lim_{x \to a} f(x) = L_1$ et $\lim_{x \to a} g(x) = L_2$ avec $f, g : D \to \mathbb{R}$, alors :
1. $\lim_{x \to a} (f(x) + g(x)) = L_1 + L_2$
2. $\lim_{x \to a} (f(x)g(x)) = L_1 L_2$
3. Si $L_2 \neq 0$, $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{L_1}{L_2}$

**Exemple Concret 2 (Calcul de limite directe) :**
Soit $f(x, y) = x^2 y + 2x - y$. Cherchons la limite en $(1, -1)$.
Puisque $f$ est une fonction polynomiale, elle est bien définie et on peut substituer directement (nous verrons que c'est lié à sa continuité) :
$$ f(1, -1) = (1)^2(-1) + 2(1) - (-1) = -1 + 2 + 1 = 2 $$
La limite de $f$ en $(1, -1)$ est donc $2$.

**Contre-exemple (Configuration pathologique des chemins différents) :**
Considérons $f(x, y) = \frac{xy}{x^2 + y^2}$ définie sur $\mathbb{R}^2 \setminus \{(0,0)\}$. Cherchons la limite en $(0,0)$.
- Approchons l'origine le long de l'axe des abscisses (la droite $y = 0$). Pour $x \neq 0$ :
  $$ f(x, 0) = \frac{x \cdot 0}{x^2 + 0^2} = 0 $$
  La limite sur ce chemin est $0$.
- Approchons l'origine le long de la diagonale principale (la droite $y = x$). Pour $x \neq 0$ :
  $$ f(x, x) = \frac{x \cdot x}{x^2 + x^2} = \frac{x^2}{2x^2} = \frac{1}{2} $$
  La limite sur ce chemin est $\frac{1}{2}$.
Puisque les limites diffèrent selon le chemin, **$f$ n'admet pas de limite en $(0,0)$**.

## 4. Continuité et Prolongement

### Définition 4.1 : Continuité
Soit $D \subset \mathbb{R}^n$, $a \in D$, et $f : D \to \mathbb{R}^p$.
L'application $f$ est continue en $a$ si et seulement si :
$$ \lim_{x \to a} f(x) = f(a) $$
En d'autres termes :
$$ \forall \varepsilon > 0, \exists \delta > 0, \forall x \in D, \quad (\|x - a\| < \delta \implies \|f(x) - f(a)\| < \varepsilon) $$

Une fonction est continue sur $D$ si elle est continue en tout point de $D$.

### Théorème 4.1 : Continuité par passage aux coordonnées polaires
Pour une fonction $f(x, y)$ définie au voisinage de l'origine de $\mathbb{R}^2$, on peut introduire les coordonnées polaires $x = r \cos \theta$ et $y = r \sin \theta$.
S'il existe une fonction $g(r)$ telle que pour tout $\theta$ et pour un rayon $r$ suffisamment petit,
$$ |f(r\cos\theta, r\sin\theta) - L| \leq g(r) \quad \text{avec} \quad \lim_{r \to 0^+} g(r) = 0 $$
Alors $\lim_{(x,y) \to (0,0)} f(x, y) = L$.

**Exemple Concret 3 (Étude de continuité) :**
Soit $h(x, y) = \frac{x^3 + y^3}{x^2 + y^2}$ pour $(x, y) \neq (0,0)$ et $h(0,0) = 0$.
Vérifions si $h$ est continue en $(0,0)$.
Passons en polaires : $x = r\cos\theta$, $y = r\sin\theta$ (avec $r>0$).
$$ h(r\cos\theta, r\sin\theta) = \frac{r^3 \cos^3\theta + r^3 \sin^3\theta}{r^2(\cos^2\theta + \sin^2\theta)} = \frac{r^3(\cos^3\theta + \sin^3\theta)}{r^2} = r(\cos^3\theta + \sin^3\theta) $$
On a alors la majoration :
$$ |h(x, y) - 0| = r|\cos^3\theta + \sin^3\theta| \leq r (|\cos^3\theta| + |\sin^3\theta|) \leq r (1 + 1) = 2r $$
Puisque $\lim_{r \to 0^+} 2r = 0$, la limite de $h(x, y)$ en $(0,0)$ est bien $0 = h(0,0)$.
La fonction $h$ est donc continue à l'origine.

## 5. Démonstrations Fondamentales

### Démonstration : Unicité de la limite dans $\mathbb{R}^n$
Nous allons démontrer formellement qu'une limite, si elle existe, est unique.
Soit $f : D \setminus \{a\} \to \mathbb{R}^p$. Supposons, par l'absurde, que $f$ admet deux limites distinctes $L_1$ et $L_2$ en $a$.
On a donc $L_1 \neq L_2$, ce qui implique que $\|L_1 - L_2\| > 0$.
Prenons $\varepsilon = \frac{\|L_1 - L_2\|}{3} > 0$.
- Puisque $\lim_{x \to a} f(x) = L_1$, il existe $\delta_1 > 0$ tel que si $0 < \|x - a\| < \delta_1$, on a $\|f(x) - L_1\| < \varepsilon$.
- Puisque $\lim_{x \to a} f(x) = L_2$, il existe $\delta_2 > 0$ tel que si $0 < \|x - a\| < \delta_2$, on a $\|f(x) - L_2\| < \varepsilon$.

Soit $\delta = \min(\delta_1, \delta_2) > 0$. Puisque tout ouvert non trivial de $\mathbb{R}^n$ contient une infinité de points, il existe un point $x \in D$ tel que $0 < \|x - a\| < \delta$.
Pour ce $x$, les deux inégalités sont vérifiées simultanément.
Utilisons l'inégalité triangulaire de la norme sur $\|L_1 - L_2\|$ :
$$ \|L_1 - L_2\| = \|L_1 - f(x) + f(x) - L_2\| $$
$$ \|L_1 - L_2\| \leq \|L_1 - f(x)\| + \|f(x) - L_2\| $$
$$ \|L_1 - L_2\| = \|f(x) - L_1\| + \|f(x) - L_2\| $$
En substituant les majorations de limite :
$$ \|L_1 - L_2\| < \varepsilon + \varepsilon = 2\varepsilon = \frac{2\|L_1 - L_2\|}{3} $$
On arrive à la conclusion absurde que $\|L_1 - L_2\| < \frac{2}{3}\|L_1 - L_2\|$ alors que $\|L_1 - L_2\| > 0$.
L'hypothèse d'existence de deux limites est donc fausse. La limite est unique.

## 6. Applications en Physique, Logique et Intelligence Artificielle

L'analyse à plusieurs variables ne relève pas de la spéculation mathématique désincarnée, c'est le langage structurel fondamental de notre époque.

**En Physique Théorique :**
Dans la mécanique des fluides et la thermodynamique, on travaille constamment avec des fonctions d'état. La température d'un espace dépend du point de coordonnées $(x,y,z)$ et du temps $t$, soit $T(x,y,z,t)$, ce qui est une fonction scalaire de quatre variables. Les propriétés topologiques, notamment la continuité de ces champs, sont les conditions sine qua non à la validité des équations de Navier-Stokes.

**En Apprentissage Profond (Intelligence Artificielle) :**
La pierre angulaire de l'Intelligence Artificielle moderne (Deep Learning) repose sur l'optimisation d'une fonction de plusieurs variables, appelée **fonction de coût** ou *Loss Function* $\mathcal{L}(\theta_1, \theta_2, \ldots, \theta_n)$.
Un réseau de neurones moderne peut posséder de quelques centaines à plusieurs centaines de milliards de paramètres (variables $\theta_i$). La continuité et, comme nous le verrons dans les prochains jalons, la différentiabilité de cette fonction $\mathcal{L} : \mathbb{R}^n \to \mathbb{R}$, sont nécessaires pour que l'algorithme de descente de gradient puisse trouver une direction vers un minimum local.
L'étude de la surface de l'erreur dans un espace de très grande dimension fait directement appel aux outils de continuité multi-variables, où la probabilité d'avoir des directions de stagnation (plateaux) ou des cols (points-selles) devient dominante face aux minima stricts.
