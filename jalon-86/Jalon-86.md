---
uuid: "jalon-86"
title: "Variables aléatoires et Applications mesurables"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/abstraction
prev: "[[Jalon 85 (Axiomes de Kolmogorov).md]]"
next: "[[Jalon 87 (Intégration des variables aléatoires).md]]"
---

# Jalon 86 : Variables aléatoires vues comme des applications mesurables

## 1. Genèse et Intuition Physique

Historiquement, le passage de la théorie de la mesure de Lebesgue aux probabilités axiomatiques par Kolmogorov en 1933 a marqué une rupture fondamentale. Avant cela, une "probabilité" était souvent liée à des jeux de hasard de manière purement combinatoire ou fréquentiste. Le génie de Kolmogorov a été de réaliser qu'une expérience aléatoire complexe (comme le lancer d'un dé, la trajectoire d'une particule brownienne, ou le résultat d'un réseau de neurones) se déroule dans un univers fondamental $\Omega$ souvent insaisissable directement.

Pour pouvoir observer et calculer des statistiques sur cet univers abstrait, il est nécessaire de projeter les résultats d'une expérience (les "issues" ou "événements") dans un espace mathématique connu, comme l'ensemble des réels $\mathbb{R}$. C'est ici qu'intervient la notion de variable aléatoire. Une variable aléatoire $X$ n'est ni une variable, ni intrinsèquement aléatoire ; c'est un traducteur, une fonction déterministe qui associe à chaque événement abstrait $\omega \in \Omega$ une valeur numérique $x = X(\omega) \in \mathbb{R}$.

Cependant, pour que cette traduction ait un sens probabiliste, il faut que l'on puisse affecter une probabilité à des événements tels que "$X$ prend une valeur entre $a$ et $b$". Cela exige que l'ensemble des issues conduisant à un tel résultat, c'est-à-dire l'image réciproque $X^{-1}([a, b])$, soit "mesurable" dans l'univers de départ. Ainsi, le concept de variable aléatoire se formalise rigoureusement comme une application mesurable entre un espace probabilisable et la droite réelle munie de sa tribu de Borel.

## 2. Définitions et Structures

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace probabilisé, où $\Omega$ est l'univers, $\mathcal{F}$ est une tribu (ou $\sigma$-algèbre) sur $\Omega$ (l'ensemble des événements mesurables), et $\mathbb{P}$ est une mesure de probabilité. Soit $(E, \mathcal{E})$ un espace mesurable, souvent $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ où $\mathcal{B}(\mathbb{R})$ est la tribu borélienne.

**Définition 1 (Variable Aléatoire) :**
Une variable aléatoire à valeurs dans $(E, \mathcal{E})$ est une application $X : \Omega \to E$ qui est $\mathcal{F}$-$\mathcal{E}$ mesurable. C'est-à-dire que pour tout sous-ensemble mesurable $B \in \mathcal{E}$, l'image réciproque par $X$ de $B$ appartient à $\mathcal{F}$ :
$$ \forall B \in \mathcal{E}, \quad X^{-1}(B) = \{\omega \in \Omega \mid X(\omega) \in B\} \in \mathcal{F} $$
Dans le cas $E = \mathbb{R}$ et $\mathcal{E} = \mathcal{B}(\mathbb{R})$, $X$ est appelée une variable aléatoire réelle (v.a.r.).

**Exemple Concret 1 :**
Considérons le lancer d'un dé équilibré à 6 faces. L'univers est $\Omega = \{1, 2, 3, 4, 5, 6\}$. La tribu usuelle est l'ensemble des parties de $\Omega$, soit $\mathcal{F} = \mathcal{P}(\Omega)$.
Définissons l'application $X : \Omega \to \mathbb{R}$ par :
$$ X(\omega) = \begin{cases} 1 & \text{si } \omega \text{ est pair} \\ 0 & \text{si } \omega \text{ est impair} \end{cases} $$
Prenons un borélien de $\mathbb{R}$, par exemple $B = \{1\}$.
L'image réciproque $X^{-1}(\{1\}) = \{\omega \in \Omega \mid X(\omega) = 1\} = \{2, 4, 6\}$.
Puisque $\{2, 4, 6\} \in \mathcal{P}(\Omega) = \mathcal{F}$, et qu'il en est de même pour tout sous-ensemble de $\mathbb{R}$ (car toute partie de $\Omega$ est dans $\mathcal{P}(\Omega)$), $X$ est bien une variable aléatoire. Elle indique la parité du lancer.

**Définition 2 (Loi d'une Variable Aléatoire / Mesure Image) :**
Soit $X$ une variable aléatoire de $(\Omega, \mathcal{F}, \mathbb{P})$ dans $(E, \mathcal{E})$. La loi de probabilité de $X$, notée $\mathbb{P}_X$, est la mesure image de $\mathbb{P}$ par $X$, définie sur $(E, \mathcal{E})$ par :
$$ \forall B \in \mathcal{E}, \quad \mathbb{P}_X(B) = \mathbb{P}(X^{-1}(B)) = \mathbb{P}(\{\omega \in \Omega \mid X(\omega) \in B\}) $$
On note souvent abusivement $\mathbb{P}(X \in B)$ pour désigner cette quantité.

**Exemple Concret 2 :**
Reprenons le lancer du dé avec $X$ (parité). Calculons la loi de $X$, $\mathbb{P}_X$.
- $\mathbb{P}_X(\{1\}) = \mathbb{P}(X^{-1}(\{1\})) = \mathbb{P}(\{2, 4, 6\}) = \frac{3}{6} = \frac{1}{2}$.
- $\mathbb{P}_X(\{0\}) = \mathbb{P}(X^{-1}(\{0\})) = \mathbb{P}(\{1, 3, 5\}) = \frac{3}{6} = \frac{1}{2}$.
La loi de probabilité $\mathbb{P}_X$ est donc une loi de Bernoulli de paramètre $p = \frac{1}{2}$. Le concept abstrait s'est projeté en une loi de probabilité standard sur $\mathbb{R}$.

**Définition 3 (Tribu engendrée par une variable aléatoire) :**
La tribu engendrée par une variable aléatoire $X$, notée $\sigma(X)$, est la plus petite tribu sur $\Omega$ rendant $X$ mesurable. Elle est donnée par :
$$ \sigma(X) = \{ X^{-1}(B) \mid B \in \mathcal{E} \} $$
C'est la tribu des événements dont la réalisation peut être connue en observant uniquement la valeur de $X$.

## 3. Théorèmes Fondamentaux et Exemples

**Théorème 1 (Critère de mesurabilité sur les générateurs) :**
Soit $X : \Omega \to E$ une application et supposons que la tribu $\mathcal{E}$ soit engendrée par une classe de sous-ensembles $\mathcal{C}$ (i.e. $\mathcal{E} = \sigma(\mathcal{C})$).
Alors $X$ est mesurable (et donc est une variable aléatoire) si et seulement si :
$$ \forall C \in \mathcal{C}, \quad X^{-1}(C) \in \mathcal{F} $$

**Exemple Concret 3 :**
Pour les variables aléatoires réelles, la tribu borélienne $\mathcal{B}(\mathbb{R})$ est engendrée par les demi-droites de la forme $]-\infty, a]$ pour $a \in \mathbb{R}$. Donc, pour vérifier qu'une application $X : \Omega \to \mathbb{R}$ est une variable aléatoire réelle, il suffit de vérifier que pour tout $a \in \mathbb{R}$ :
$$ \{\omega \in \Omega \mid X(\omega) \leq a\} \in \mathcal{F} $$

**Théorème 2 (Composition d'applications mesurables) :**
Soit $X$ une variable aléatoire de $(\Omega, \mathcal{F}, \mathbb{P})$ vers $(E_1, \mathcal{E}_1)$ et $g : E_1 \to E_2$ une application mesurable de l'espace mesurable $(E_1, \mathcal{E}_1)$ vers $(E_2, \mathcal{E}_2)$.
Alors la composition $Y = g \circ X$ est une variable aléatoire de $(\Omega, \mathcal{F}, \mathbb{P})$ vers $(E_2, \mathcal{E}_2)$.

**Exemple Concret 4 :**
Si $X$ est une variable aléatoire réelle (à valeurs dans $\mathbb{R}$), et $g(x) = x^2$ (qui est continue, donc borélienne mesurable), alors $Y = X^2$ est aussi une variable aléatoire réelle. De la même façon, $\exp(X)$, $\sin(X)$, ou $|X|$ sont des variables aléatoires.

## 4. Démonstrations Rigoureuses

**Démonstration du Théorème 1 (Critère de mesurabilité sur les générateurs) :**
Soit $X : \Omega \to E$. Supposons que $\mathcal{E} = \sigma(\mathcal{C})$.

**Sens direct ($\Rightarrow$) :**
Supposons que $X$ est mesurable. Par définition, pour tout $B \in \mathcal{E}$, on a $X^{-1}(B) \in \mathcal{F}$.
Puisque $\mathcal{C} \subset \sigma(\mathcal{C}) = \mathcal{E}$, il est immédiat que pour tout $C \in \mathcal{C}$, on a $C \in \mathcal{E}$, d'où $X^{-1}(C) \in \mathcal{F}$.

**Sens réciproque ($\Leftarrow$) :**
Supposons que pour tout $C \in \mathcal{C}$, on a $X^{-1}(C) \in \mathcal{F}$.
Considérons la classe d'ensembles de $E$ dont l'image réciproque est dans $\mathcal{F}$ :
$$ \mathcal{M} = \{ B \in \mathcal{E} \mid X^{-1}(B) \in \mathcal{F} \} $$
Montrons que $\mathcal{M}$ est une tribu sur $E$ :
1. $X^{-1}(E) = \Omega \in \mathcal{F}$, donc $E \in \mathcal{M}$.
2. Soit $B \in \mathcal{M}$. Alors $X^{-1}(B) \in \mathcal{F}$. Puisque $\mathcal{F}$ est une tribu, $(X^{-1}(B))^c \in \mathcal{F}$. Or, les propriétés des images réciproques assurent que $(X^{-1}(B))^c = X^{-1}(B^c)$. Ainsi, $X^{-1}(B^c) \in \mathcal{F}$, ce qui implique que $B^c \in \mathcal{M}$.
3. Soit $(B_n)_{n \in \mathbb{N}}$ une suite d'éléments de $\mathcal{M}$. Par définition, pour tout $n$, $X^{-1}(B_n) \in \mathcal{F}$. Comme $\mathcal{F}$ est une tribu, $\bigcup_{n \in \mathbb{N}} X^{-1}(B_n) \in \mathcal{F}$. Les propriétés des images réciproques nous disent que $\bigcup_{n \in \mathbb{N}} X^{-1}(B_n) = X^{-1}\left(\bigcup_{n \in \mathbb{N}} B_n\right)$. Il s'ensuit que $X^{-1}\left(\bigcup_{n \in \mathbb{N}} B_n\right) \in \mathcal{F}$, d'où $\bigcup_{n \in \mathbb{N}} B_n \in \mathcal{M}$.
Donc $\mathcal{M}$ est bien une tribu sur $E$.
Par hypothèse, $\mathcal{C} \subset \mathcal{M}$.
Or, $\mathcal{E} = \sigma(\mathcal{C})$ est par définition la plus petite tribu contenant $\mathcal{C}$.
Par suite, $\mathcal{E} \subset \mathcal{M}$. Mais par construction, $\mathcal{M} \subset \mathcal{E}$. Donc $\mathcal{M} = \mathcal{E}$.
Cela signifie que pour tout $B \in \mathcal{E}$, $X^{-1}(B) \in \mathcal{F}$. Ainsi, $X$ est une application mesurable.
$\blacksquare$

**Démonstration du Théorème 2 (Composition) :**
Soit $B \in \mathcal{E}_2$.
Puisque $g : (E_1, \mathcal{E}_1) \to (E_2, \mathcal{E}_2)$ est mesurable, l'image réciproque de $B$ par $g$, notée $g^{-1}(B)$, appartient à $\mathcal{E}_1$.
Puisque $X : (\Omega, \mathcal{F}) \to (E_1, \mathcal{E}_1)$ est mesurable, l'image réciproque par $X$ de tout élément de $\mathcal{E}_1$ appartient à $\mathcal{F}$.
En particulier, comme $g^{-1}(B) \in \mathcal{E}_1$, on a $X^{-1}(g^{-1}(B)) \in \mathcal{F}$.
Or, $X^{-1}(g^{-1}(B)) = (g \circ X)^{-1}(B) = Y^{-1}(B)$.
Donc, pour tout $B \in \mathcal{E}_2$, $Y^{-1}(B) \in \mathcal{F}$.
Ceci prouve que $Y = g \circ X$ est $\mathcal{F}$-$\mathcal{E}_2$ mesurable, c'est-à-dire que $Y$ est une variable aléatoire.
$\blacksquare$

## 5. Applications en Intelligence Artificielle

### Apprentissage de Représentations et Mesurabilité

Dans l'apprentissage profond (Deep Learning), un réseau de neurones calcule des transformations complexes. Une couche du réseau peut être vue comme une fonction $f : \mathbb{R}^{d_{in}} \to \mathbb{R}^{d_{out}}$. Les données d'entrée $X$ sont modélisées comme des variables aléatoires (avec une distribution inconnue $\mathbb{P}_X$).
Parce que $f$ est continue (généralement composée d'opérations linéaires et d'activations comme ReLU ou Sigmoïde qui sont continues), elle est borélienne mesurable. Ainsi, par le Théorème 2, la représentation latente $Z = f(X)$ est une nouvelle variable aléatoire rigoureusement définie, et on peut parler mathématiquement de sa distribution $\mathbb{P}_Z$. C'est le fondement de méthodes comme les Auto-encodeurs Variationnels (VAE) ou les Normalizing Flows, qui cherchent à modéliser et transformer explicitement cette mesure image pour générer de nouvelles données.
