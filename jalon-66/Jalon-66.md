# Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives

## 1. La quête de l'aire sous la courbe : De Riemann à Lebesgue

Le concept d'intégration trouve son origine dans le problème millénaire de la quadrature, c'est-à-dire le calcul de l'aire sous une courbe géométrique. L'intégrale de Riemann a apporté une première formalisation rigoureuse en découpant le domaine de départ (l'axe des abscisses) en petits intervalles, puis en encadrant la fonction par des fonctions en escalier.

Cependant, cette approche se heurte rapidement à des limites physiques et computationnelles : l'intégrale de Riemann est impuissante face à des fonctions très oscillantes ou très discontinues (comme la fonction indicatrice des rationnels, qui vaut 1 sur les rationnels et 0 ailleurs). De plus, l'espace des fonctions Riemann-intégrables n'est pas complet : une limite de fonctions intégrables n'est pas nécessairement intégrable.

C'est ici qu'intervient le coup de génie d'Henri Lebesgue en 1901. Plutôt que de découper le domaine de départ, Lebesgue propose de découper l'espace d'arrivée (l'axe des ordonnées). L'idée est de regrouper les points $x$ qui partagent la même valeur $f(x)$ ou des valeurs proches. Ce changement de perspective permet de s'affranchir de l'ordre géométrique des points sur l'axe des abscisses et d'utiliser la puissance de la théorie de la mesure.

Pour construire l'intégrale de Lebesgue, nous procédons en deux étapes fondamentales :
1.  Nous définissons d'abord l'intégrale pour des fonctions très simples, dites **fonctions étagées positives**.
2.  Nous étendons ensuite cette définition à toute fonction mesurable positive, par un processus de passage à la limite (approximation par des suites de fonctions étagées).

Cette construction, à la fois algébrique (pour les fonctions étagées) et topologique (pour le passage à la limite), est le socle sur lequel repose toute l'analyse fonctionnelle moderne et la théorie des probabilités (axiomatisation de Kolmogorov).

## 2. Intégration des fonctions étagées positives

### 2.1 Définition et construction

Considérons un espace mesuré $(X, \mathcal{A}, \mu)$. Une fonction étagée positive est une fonction $s : X \to \mathbb{R}^+$ qui ne prend qu'un nombre fini de valeurs et qui est mesurable. Toute fonction étagée positive peut s'écrire sous forme canonique.

**Définition (Intégrale d'une fonction étagée positive)**
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et $s : X \to \mathbb{R}^+$ une fonction étagée positive mesurable. Si l'on écrit $s$ sous la forme de sa représentation canonique :
$$
s = \sum_{i=1}^n \alpha_i \mathbb{1}_{A_i}
$$
où les $\alpha_i \geq 0$ sont les valeurs distinctes prises par $s$, et les $A_i = s^{-1}(\{\alpha_i\}) \in \mathcal{A}$ forment une partition mesurable de $X$.

L'intégrale de $s$ par rapport à la mesure $\mu$, notée $\int_X s \, d\mu$, est définie par :
$$
\int_X s \, d\mu = \sum_{i=1}^n \alpha_i \mu(A_i)
$$
Dans cette formule, nous adoptons la convention $0 \times (+\infty) = 0$, ce qui garantit qu'un ensemble de mesure nulle n'apporte aucune contribution, même si la fonction y prend une valeur infinie.

**Exemple concret immédiat :**
Plaçons-nous sur $X = \mathbb{R}$ muni de la tribu de Borel $\mathcal{B}(\mathbb{R})$ et de la mesure de Lebesgue $\lambda$.
Soit la fonction étagée $s(x)$ définie par :
- $s(x) = 2$ pour $x \in [0, 1]$
- $s(x) = 5$ pour $x \in [2, 3]$
- $s(x) = 0$ ailleurs.

La représentation canonique est $s = 2 \cdot \mathbb{1}_{[0,1]} + 5 \cdot \mathbb{1}_{[2,3]} + 0 \cdot \mathbb{1}_{\mathbb{R} \setminus ([0,1] \cup [2,3])}$.
Son intégrale vaut :
$$
\int_{\mathbb{R}} s \, d\lambda = 2 \cdot \lambda([0,1]) + 5 \cdot \lambda([2,3]) + 0 \cdot \lambda(\mathbb{R} \setminus \dots)
$$
$$
\int_{\mathbb{R}} s \, d\lambda = 2 \cdot (1 - 0) + 5 \cdot (3 - 2) + 0 = 2(1) + 5(1) = 7
$$
Le calcul se réduit à une simple combinaison linéaire des mesures (les longueurs ici) des ensembles de niveau.

### 2.2 Propriétés fondamentales (Cas étagé)

L'intégrale sur l'espace des fonctions étagées positives, noté $\mathcal{E}^+$, possède des propriétés algébriques et d'ordre cruciales.

**Proposition (Linéarité et monotonie sur $\mathcal{E}^+$)**
Soient $s, t \in \mathcal{E}^+$ et $c \geq 0$.
1.  **Linéarité :** $\int_X (cs + t) \, d\mu = c \int_X s \, d\mu + \int_X t \, d\mu$
2.  **Monotonie :** Si $s \leq t$ sur $X$, alors $\int_X s \, d\mu \leq \int_X t \, d\mu$

*Remarque sur les cas limites :* La linéarité n'est vraie que pour des coefficients positifs. L'introduction de coefficients négatifs forcerait à considérer des fonctions de signe quelconque, ce qui nécessite une extension ultérieure de la théorie.

## 3. Extension aux fonctions mesurables positives

Nous passons maintenant des fonctions "simples" (étagées) aux fonctions plus générales.

**Théorème fondamental de l'approximation (Rappel)**
Pour toute fonction mesurable $f : X \to [0, +\infty]$, il existe une suite croissante $(s_n)_{n \in \mathbb{N}}$ de fonctions étagées positives ($s_n \in \mathcal{E}^+$) telle que $s_n \leq s_{n+1}$ pour tout $n$, et $s_n(x)$ converge ponctuellement vers $f(x)$ pour tout $x \in X$ lorsque $n \to +\infty$.

C'est ce théorème qui fonde la définition de l'intégrale pour une fonction mesurable positive quelconque par la méthode du "Supremum".

**Définition (Intégrale de Lebesgue d'une fonction mesurable positive)**
Soit $f : X \to [0, +\infty]$ une fonction mesurable positive. L'intégrale de $f$ par rapport à $\mu$ est définie comme le supremum des intégrales de toutes les fonctions étagées positives qui sont minorantes de $f$ :
$$
\int_X f \, d\mu = \sup \left\{ \int_X s \, d\mu \ \middle| \ s \in \mathcal{E}^+ \text{ et } 0 \leq s \leq f \text{ sur } X \right\}
$$
L'intégrale $\int_X f \, d\mu$ prend ses valeurs dans $[0, +\infty]$.

**Exemple concret immédiat :**
Considérons l'espace mesuré $(]0, 1], \mathcal{B}(]0,1]), \lambda)$. Soit la fonction $f(x) = \frac{1}{\sqrt{x}}$. $f$ est continue donc mesurable et positive.
Considérons une suite de fonctions étagées $s_n$ minorant $f$. Puisque $\lim_{x \to 0} \frac{1}{\sqrt{x}} = +\infty$, l'intégrale de Riemann classique est impropre, mais au sens de Lebesgue, nous avons directement :
$$
\int_{]0,1]} \frac{1}{\sqrt{x}} \, d\lambda = \lim_{n \to \infty} \int_{]0,1]} s_n \, d\lambda = \left[ 2\sqrt{x} \right]_0^1 = 2
$$
Ici, l'intégrale de Lebesgue coïncide avec la limite de l'intégrale de Riemann, mais la construction est intrinsèquement liée à la mesure $\lambda$.

### 3.1 Monotonie (Cas général)

La propriété de monotonie est préservée par le passage au supremum.

**Proposition (Monotonie générale)**
Si $f$ et $g$ sont deux fonctions mesurables positives telles que $f \leq g$ sur $X$, alors :
$$
\int_X f \, d\mu \leq \int_X g \, d\mu
$$

*Démonstration:*
Soit $s \in \mathcal{E}^+$ telle que $0 \leq s \leq f$. Puisque $f \leq g$, nous avons $0 \leq s \leq g$.
Par conséquent, $s$ fait partie de l'ensemble sur lequel on prend le supremum pour définir $\int_X g \, d\mu$.
Ainsi, pour toute fonction étagée $s \leq f$, $\int_X s \, d\mu \leq \int_X g \, d\mu$.
En prenant le supremum sur toutes ces fonctions $s$, on obtient :
$$
\sup_{s \leq f} \int_X s \, d\mu \leq \int_X g \, d\mu
$$
Ce qui est exactement la définition de $\int_X f \, d\mu \leq \int_X g \, d\mu$.

## 4. Démonstrations : Additivité et Lemme de Fatou (Prélude)

L'une des propriétés les plus importantes (et délicates à démontrer rigoureusement par le supremum) est la linéarité, en particulier l'additivité $\int (f+g) = \int f + \int g$.

*Preuve de l'additivité (Esquisse rigoureuse)*
Soient $f, g$ mesurables positives.
1.  **Inégalité directe :** Si $s \leq f$ et $t \leq g$ sont des fonctions étagées, alors $s+t \leq f+g$ est une fonction étagée.
    Par additivité sur $\mathcal{E}^+$, $\int (s+t) = \int s + \int t \leq \int (f+g)$.
    En prenant le supremum indépendamment sur $s$ puis sur $t$, on obtient :
    $\int f + \int g \leq \int (f+g)$.
2.  **Inégalité inverse :** L'inégalité $\int (f+g) \leq \int f + \int g$ nécessite le puissant **Théorème de convergence monotone** (qui sera vu au jalon suivant). Si $(s_n)$ et $(t_n)$ sont des suites étagées croissant vers $f$ et $g$, alors $s_n+t_n$ croît vers $f+g$. En admettant que l'on peut inverser limite et intégrale pour des suites croissantes, on conclut :
    $\int (f+g) = \lim \int (s_n+t_n) = \lim (\int s_n + \int t_n) = \int f + \int g$.

Ce chaînage logique montre la nécessité absolue d'établir des théorèmes de passage à la limite sous le signe intégral (Convergence Monotone, Fatou, Convergence Dominée) pour rendre l'intégrale de Lebesgue véritablement opérationnelle.

## 5. Applications en Physique, Logique et IA

La théorie de l'intégration de Lebesgue n'est pas qu'un raffinement purement esthétique ; elle est l'infrastructure mathématique de la science moderne.

1.  **Théorie des Probabilités et IA (Espérance mathématique) :** L'espérance d'une variable aléatoire positive $X$ sur un espace probabilisé $(\Omega, \mathcal{F}, P)$ est par définition son intégrale de Lebesgue : $\mathbb{E}[X] = \int_\Omega X \, dP$. Cette formulation unifie le cas des variables discrètes (sommes) et continues (intégrales à densité). En Machine Learning, la fonction de coût empirique converge vers l'espérance du risque théorique, justifiée par la loi forte des grands nombres (une conséquence directe de la théorie de la mesure de Lebesgue).
2.  **Mécanique Quantique (Espaces de Hilbert $L^2$) :** Les états quantiques d'une particule sont décrits par des fonctions d'onde appartenant à l'espace $L^2(\mathbb{R}^3, \lambda)$ des fonctions de carré Lebesgue-intégrables. La complétude de cet espace (le fait que toute suite de Cauchy converge) est garantie par l'intégrale de Lebesgue, ce qui est faux avec Riemann. La construction de la mesure est donc vitale pour garantir que les limites d'états physiques restent des états physiques valides.
3.  **Théorie de l'Information (Entropie de Shannon différentielle) :** L'entropie différentielle d'une densité de probabilité continue est définie par une intégrale de Lebesgue : $h(f) = -\int f(x) \ln(f(x)) dx$. La convergence des algorithmes d'optimisation entropique (comme dans les Variational Autoencoders - VAE) s'appuie fondamentalement sur le passage à la limite sous ces intégrales.