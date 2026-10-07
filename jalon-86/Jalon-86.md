---
uuid: "jalon-86"
title: "Variables aléatoires et Applications mesurables"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/abstraction
prev: "[[jalon-85/Jalon-85.md|Jalon 85 : Axiomes de Kolmogorov]]"
next: "[[Jalon 87 (Intégration des variables aléatoires).md]]"
---

# Jalon 86 : Variables aléatoires et Applications mesurables

## 1. Genèse et Intuition Physique

Historiquement, le passage de l'événement abstrait à la variable aléatoire est une révolution conceptuelle. Imaginez l'étude d'un gaz composé de milliards de molécules. L'espace fondamental $\Omega$ représente l'ensemble de tous les états microscopiques possibles du gaz (positions et vitesses de chaque molécule). Cet espace est d'une complexité vertigineuse.
Toutefois, en tant que physicien, ce ne sont pas les trajectoires individuelles qui nous intéressent, mais des grandeurs macroscopiques : la température, la pression, ou l'énergie cinétique totale.

Une **variable aléatoire** agit précisément comme un instrument de mesure : c'est une "lunette" mathématique qui projette la complexité de l'espace abstrait $\Omega$ vers l'espace beaucoup plus familier et ordonné des nombres réels $\mathbb{R}$. Elle prend un état du monde $\omega$ (le tirage d'un dé, la position d'une particule, le pixel d'une image) et lui associe un nombre réel $X(\omega)$.

Cependant, pour que cette association soit cohérente avec le calcul des probabilités, il ne suffit pas de lier n'importe quel état à n'importe quel nombre. Andreï Kolmogorov, dans son approche axiomatique de 1933, impose une condition stricte : si l'on se pose la question "Le résultat numérique est-il inférieur à une certaine valeur $x$ ?", l'ensemble des états originaux $\omega$ qui satisfont cette condition doit être mesurable, c'est-à-dire qu'on doit pouvoir lui attribuer une probabilité. C'est la naissance de la notion d'application mesurable, véritable clef de voûte de la théorie moderne des probabilités et fondation indispensable pour toute l'intelligence artificielle.

## 2. Définitions et Théorèmes Fondamentaux

### A. La notion de Variable Aléatoire Réelle

> **Définition 1 (Variable Aléatoire Réelle) :**
> Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace probabilisé et $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ l'espace mesurable des réels muni de la tribu borélienne.
> Une application $X : \Omega \to \mathbb{R}$ est appelée **variable aléatoire réelle** (v.a.r) si elle est $\mathcal{F}/\mathcal{B}(\mathbb{R})$-mesurable.
> Cela signifie que pour tout ensemble borélien $B \in \mathcal{B}(\mathbb{R})$, l'image réciproque de $B$ par $X$ appartient à la tribu $\mathcal{F}$ :
> $$ \forall B \in \mathcal{B}(\mathbb{R}), \quad X^{-1}(B) = \{ \omega \in \Omega \mid X(\omega) \in B \} \in \mathcal{F} $$

**Exemple Concret Immédiat : Le double lancer de pile ou face**
Soit l'expérience de deux lancers de pièce indépendants.
L'univers est $\Omega = \{(P,P), (P,F), (F,P), (F,F)\}$.
La tribu $\mathcal{F}$ est l'ensemble des parties de $\Omega$, soit $\mathcal{P}(\Omega)$ (qui contient $2^4 = 16$ événements).
Définissons la variable aléatoire $X$ comme "le nombre de 'Pile' obtenus".
- $X((P,P)) = 2$
- $X((P,F)) = 1$
- $X((F,P)) = 1$
- $X((F,F)) = 0$

Prenons le borélien $B = [1, 3]$. L'événement associé à $X \in [1,3]$ est l'image réciproque :
$X^{-1}([1, 3]) = \{ \omega \in \Omega \mid X(\omega) \in [1, 3] \} = \{ (P,P), (P,F), (F,P) \}$.
Cet ensemble appartient bien à $\mathcal{P}(\Omega)$, donc $X$ est bien une variable aléatoire mesurable.

---

### B. Caractérisation simplifiée de la mesurabilité

Vérifier la mesurabilité pour tout borélien $B \in \mathcal{B}(\mathbb{R})$ est en pratique impossible car la tribu borélienne est extrêmement riche. Le théorème suivant offre un critère fondamental et opératoire.

> **Théorème 1 (Caractérisation de la mesurabilité par les générateurs) :**
> Soit $X : \Omega \to \mathbb{R}$ une application et $\mathcal{C}$ une classe de parties de $\mathbb{R}$ qui engendre la tribu borélienne, c'est-à-dire $\sigma(\mathcal{C}) = \mathcal{B}(\mathbb{R})$.
> L'application $X$ est mesurable si et seulement si :
> $$ \forall C \in \mathcal{C}, \quad X^{-1}(C) \in \mathcal{F} $$
> En particulier, en choisissant $\mathcal{C} = \{ ]-\infty, x] \mid x \in \mathbb{R} \}$, $X$ est une variable aléatoire si et seulement si pour tout réel $x$, l'événement $\{X \leq x\}$ appartient à $\mathcal{F}$.

**Exemple Concret Immédiat : Fonction indicatrice**
Soit $A \subset \Omega$. On définit la fonction indicatrice $\mathbf{1}_A : \Omega \to \mathbb{R}$ par :
$$ \mathbf{1}_A(\omega) = \begin{cases} 1 & \text{si } \omega \in A \\ 0 & \text{si } \omega \notin A \end{cases} $$
Étudions la pré-image des intervalles $]-\infty, x]$ :
- Si $x < 0$ : $\mathbf{1}_A^{-1}(]-\infty, x]) = \emptyset$ (car $\mathbf{1}_A$ ne prend que les valeurs 0 et 1).
- Si $0 \leq x < 1$ : $\mathbf{1}_A^{-1}(]-\infty, x]) = A^c$ (car seule la valeur 0 est incluse).
- Si $x \geq 1$ : $\mathbf{1}_A^{-1}(]-\infty, x]) = \Omega$.
Pour que $\mathbf{1}_A$ soit une variable aléatoire, il faut et il suffit que $\emptyset, A^c, \Omega \in \mathcal{F}$. Par définition d'une tribu, $\emptyset$ et $\Omega$ y sont toujours. Il reste la condition $A^c \in \mathcal{F}$, ce qui équivaut à $A \in \mathcal{F}$.
Ainsi, $\mathbf{1}_A$ est une variable aléatoire mesurable si et seulement si l'ensemble $A$ est un événement mesurable de $\mathcal{F}$.

**Cas limites et contre-exemples : L'ensemble de Vitali**
Dans l'espace $\Omega = [0, 1]$ muni de la mesure de Lebesgue et de la tribu borélienne, il existe des sous-ensembles non mesurables, comme l'ensemble de Vitali $V$.
Si l'on définit la fonction $X = \mathbf{1}_V$, alors pour $x \in [0, 1[$, l'ensemble $\{ \omega \in \Omega \mid X(\omega) \leq x \} = V^c$.
Comme $V$ n'est pas mesurable, $V^c$ ne l'est pas non plus, donc l'image réciproque n'appartient pas à la tribu borélienne. La fonction indicatrice de l'ensemble de Vitali n'est pas une variable aléatoire. Elle est pathologique.

---

### C. Mesure de Probabilité Image : La Loi d'une Variable Aléatoire

Une fois la mesurabilité établie, nous pouvons transférer la mesure de probabilité originelle $\mathbb{P}$ de l'espace abstrait vers l'espace réel.

> **Définition 2 (Loi d'une Variable Aléatoire) :**
> Soit $X : (\Omega, \mathcal{F}, \mathbb{P}) \to (\mathbb{R}, \mathcal{B}(\mathbb{R}))$ une variable aléatoire.
> La **loi de probabilité** (ou mesure image) de $X$, notée $\mathbb{P}_X$, est la mesure de probabilité sur l'espace d'arrivée $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ définie par :
> $$ \forall B \in \mathcal{B}(\mathbb{R}), \quad \mathbb{P}_X(B) = \mathbb{P}(X^{-1}(B)) = \mathbb{P}(\{\omega \in \Omega \mid X(\omega) \in B\}) = \mathbb{P}(X \in B) $$

**Exemple Concret Immédiat : Poussée vers l'espace Réel**
Reprenons le double lancer de pile ou face avec une pièce équilibrée. $\mathbb{P}$ attribue la probabilité $1/4$ à chaque élément de $\Omega$.
$X$ compte le nombre de "Pile". Les valeurs possibles sont $\{0, 1, 2\}$.
Calculons la loi de $X$, $\mathbb{P}_X$, sur des ensembles de $\mathbb{R}$ :
- $\mathbb{P}_X(\{2\}) = \mathbb{P}(X^{-1}(\{2\})) = \mathbb{P}(\{(P,P)\}) = 1/4$.
- $\mathbb{P}_X(\{1\}) = \mathbb{P}(X^{-1}(\{1\})) = \mathbb{P}(\{(P,F), (F,P)\}) = 1/4 + 1/4 = 1/2$.
- $\mathbb{P}_X(\{0\}) = \mathbb{P}(X^{-1}(\{0\})) = \mathbb{P}(\{(F,F)\}) = 1/4$.
- $\mathbb{P}_X([1.5, 5]) = \mathbb{P}(X \in [1.5, 5]) = \mathbb{P}_X(\{2\}) = 1/4$.
La mesure de probabilité a été entièrement transportée (ou poussée, *push-forward measure*) sur $\mathbb{R}$.

## 3. Démonstrations Rigoureuses

**Démonstration du Théorème 1 (Caractérisation de la mesurabilité par les générateurs)**

Nous devons montrer l'équivalence entre :
(i) Pour tout $B \in \mathcal{B}(\mathbb{R})$, $X^{-1}(B) \in \mathcal{F}$
(ii) Pour tout $C \in \mathcal{C}$ (où $\sigma(\mathcal{C}) = \mathcal{B}(\mathbb{R})$), $X^{-1}(C) \in \mathcal{F}$

**Étape 1 : (i) implique (ii)**
L'implication est directe. Par hypothèse, $\mathcal{C}$ est une sous-famille de $\mathcal{B}(\mathbb{R})$.
Si l'image réciproque de tout ensemble de $\mathcal{B}(\mathbb{R})$ appartient à $\mathcal{F}$, c'est *a fortiori* vrai pour tout ensemble de $\mathcal{C}$.

**Étape 2 : (ii) implique (i)**
Supposons que pour tout $C \in \mathcal{C}$, $X^{-1}(C) \in \mathcal{F}$.
Nous devons prouver que cette propriété s'étend à toute la tribu borélienne.
Considérons la classe d'ensembles :
$$ \mathcal{A} = \{ B \in \mathcal{B}(\mathbb{R}) \mid X^{-1}(B) \in \mathcal{F} \} $$
Notre but est de montrer que $\mathcal{A} = \mathcal{B}(\mathbb{R})$.
Pour cela, montrons d'abord que $\mathcal{A}$ est une tribu sur $\mathbb{R}$.

1. **La classe $\mathcal{A}$ contient l'ensemble vide :**
   $X^{-1}(\emptyset) = \{ \omega \in \Omega \mid X(\omega) \in \emptyset \} = \emptyset$.
   Or, par définition d'une tribu, $\emptyset \in \mathcal{F}$. Donc $\emptyset \in \mathcal{A}$.

2. **La classe $\mathcal{A}$ est stable par passage au complémentaire :**
   Soit $B \in \mathcal{A}$. Par définition, $X^{-1}(B) \in \mathcal{F}$.
   Considérons l'image réciproque du complémentaire $B^c = \mathbb{R} \setminus B$ :
   $$ X^{-1}(B^c) = \{ \omega \in \Omega \mid X(\omega) \notin B \} = \Omega \setminus \{ \omega \in \Omega \mid X(\omega) \in B \} = (X^{-1}(B))^c $$
   Puisque $\mathcal{F}$ est une tribu, elle est stable par passage au complémentaire. Ainsi, comme $X^{-1}(B) \in \mathcal{F}$, on a $(X^{-1}(B))^c \in \mathcal{F}$.
   Cela signifie que $X^{-1}(B^c) \in \mathcal{F}$, donc $B^c \in \mathcal{A}$.

3. **La classe $\mathcal{A}$ est stable par union dénombrable :**
   Soit $(B_n)_{n \in \mathbb{N}}$ une suite d'ensembles appartenant à $\mathcal{A}$.
   Par définition, pour tout $n \in \mathbb{N}$, $X^{-1}(B_n) \in \mathcal{F}$.
   Considérons l'image réciproque de l'union :
   $$ X^{-1}\left( \bigcup_{n=0}^{\infty} B_n \right) = \left\{ \omega \in \Omega \mid X(\omega) \in \bigcup_{n=0}^{\infty} B_n \right\} $$
   Un élément $\omega$ appartient à cette union si et seulement s'il existe au moins un $n$ tel que $X(\omega) \in B_n$, c'est-à-dire $\omega \in X^{-1}(B_n)$.
   Donc :
   $$ X^{-1}\left( \bigcup_{n=0}^{\infty} B_n \right) = \bigcup_{n=0}^{\infty} X^{-1}(B_n) $$
   Puisque chaque $X^{-1}(B_n) \in \mathcal{F}$ et que $\mathcal{F}$ est une tribu (stable par union dénombrable), l'union $\bigcup_{n=0}^{\infty} X^{-1}(B_n)$ appartient à $\mathcal{F}$.
   Ainsi, $\bigcup_{n=0}^{\infty} B_n \in \mathcal{A}$.

Nous avons prouvé que $\mathcal{A}$ est une tribu.
De plus, par notre hypothèse (ii), $\mathcal{A}$ contient la classe $\mathcal{C}$.
Or, la plus petite tribu contenant $\mathcal{C}$ est, par définition, la tribu engendrée $\sigma(\mathcal{C})$.
Puisque $\mathcal{A}$ est une tribu contenant $\mathcal{C}$, on a nécessairement :
$$ \sigma(\mathcal{C}) \subset \mathcal{A} $$
Comme on a supposé que $\sigma(\mathcal{C}) = \mathcal{B}(\mathbb{R})$ et que $\mathcal{A} \subset \mathcal{B}(\mathbb{R})$ par définition, nous concluons que :
$$ \mathcal{A} = \mathcal{B}(\mathbb{R}) $$
Cela signifie exactement que pour tout $B \in \mathcal{B}(\mathbb{R})$, $X^{-1}(B) \in \mathcal{F}$, ce qui achève la démonstration. $\blacksquare$

## 4. Applications en Physique, Logique & Intelligence Artificielle

### A. IA : Vecteurs Gaussiens et Espaces Latents (Auto-encodeurs)
Dans les architectures d'apprentissage profond, notamment les Auto-Encodeurs Variationnels (VAE) ou les modèles de diffusion, les données brutes (les images, de très haute dimension) sont compressées vers un espace latent $Z$ de plus basse dimension.
Chaque coordonnée du vecteur latent $Z$ est rigoureusement traitée comme une variable aléatoire mesurable. Lorsqu'un réseau de neurones (l'encodeur) prend une image $X$ et applique des couches denses non linéaires (fonctions d'activation ReLU, Sigmoïde), il applique une fonction continue. Le théorème fondamental de la mesurabilité stipule que la composition d'une application continue par une application mesurable reste mesurable. Ainsi, si les "bruits" initiaux en entrée du réseau sont des variables aléatoires bien définies, les activations dans les couches profondes et la sortie du réseau le sont également, garantissant que la fonction de coût peut être optimisée en espérance.

### B. Physique Statistique : Mesurabilité des observables macroscopiques
En physique statistique, l'espace des phases $\Omega$ d'un système à $N$ particules est doté de la tribu des ensembles mesurables au sens de Liouville. L'énergie totale $H(q,p)$ du système, où $q$ et $p$ sont les positions et les quantités de mouvement, est une variable aléatoire (une observable). L'équivalence entre l'ensemble microcanonique et canonique repose fondamentalement sur la possibilité de mesurer les volumes de l'espace des phases pour lesquels $E \leq H(q,p) \leq E + \Delta E$. La mesurabilité de la fonction hamiltonienne assure que ces volumes sont mathématiquement bien définis, permettant d'établir le lien fondamental entre l'entropie de Boltzmann ($S = k_B \ln \Omega$) et la probabilité des états.

### C. Logique : Transformation des propositions en variables de Boole
Dans le cadre de la logique formelle modélisée par l'informatique théorique, une proposition abstraite (vraie ou fausse) associée à des événements peut être modélisée par une variable aléatoire indicatrice (prenant des valeurs dans $\{0, 1\}$). Les opérations logiques de base se traduisent par des opérations algébriques sur des variables aléatoires mesurables :
- La négation $\text{NON}(A)$ devient $1 - \mathbf{1}_A$
- La conjonction $(A \text{ ET } B)$ devient $\mathbf{1}_A \times \mathbf{1}_B = \min(\mathbf{1}_A, \mathbf{1}_B)$
- La disjonction $(A \text{ OU } B)$ devient $\mathbf{1}_A + \mathbf{1}_B - \mathbf{1}_A \mathbf{1}_B = \max(\mathbf{1}_A, \mathbf{1}_B)$
L'espace mesurable fournit ainsi le terreau rigoureux permettant de développer la logique probabiliste, fondation des réseaux bayésiens et de l'inférence par passage de messages en intelligence artificielle.
