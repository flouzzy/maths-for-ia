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

# Jalon 86 : Variables aléatoires et Applications mesurables

## 1. Introduction : Genèse physique et intuition géométrique

L'étude des probabilités dans un cadre rigoureux repose sur l'abstraction des expériences aléatoires. Intuitivement, une expérience aléatoire (comme le lancer d'un dé ou la mesure du bruit thermique dans un circuit) produit un résultat brut, noté $\omega$, appartenant à un univers fondamental $\Omega$. Cependant, ces résultats bruts sont souvent de nature qualitative ou abstraite. Pour appliquer les outils de l'analyse mathématique, il est indispensable de les "traduire" en grandeurs numériques.

C'est ici qu'intervient la notion de variable aléatoire. Historiquement formalisée par Andrey Kolmogorov en 1933, une variable aléatoire n'a en réalité rien d'"aléatoire" dans sa définition intrinsèque, et n'est pas non plus une "variable" au sens habituel, mais bien une **fonction déterministe**. Elle associe à chaque issue $\omega \in \Omega$ un nombre réel $X(\omega) \in \mathbb{R}$.

Pour que cette traduction soit cohérente avec la théorie de la mesure, cette fonction ne peut pas être quelconque. Si nous souhaitons nous poser des questions probabilistes légitimes telles que "Quelle est la probabilité que $X$ soit supérieur à 5 ?", l'ensemble des issues $\{ \omega \in \Omega \mid X(\omega) > 5 \}$ doit impérativement être un événement mesurable (c'est-à-dire appartenir à la tribu $\mathcal{F}$ de notre espace de probabilité). Ainsi, la mesurabilité devient la clé de voûte permettant de transférer une mesure de probabilité abstraite depuis $\Omega$ vers l'espace bien connu des réels $\mathbb{R}$.

## 2. Définitions, Théorèmes & Exemples

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace de probabilité. L'espace d'arrivée $\mathbb{R}$ est systématiquement muni de sa tribu borélienne $\mathcal{B}(\mathbb{R})$, engendrée par les intervalles ouverts.

> **Définition 1 : Variable Aléatoire Réelle (V.A.R.)**
> Une fonction $X : \Omega \to \mathbb{R}$ est appelée **variable aléatoire réelle** si elle est mesurable de $(\Omega, \mathcal{F})$ dans $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$.
> Formellement, pour tout ensemble borélien $B \in \mathcal{B}(\mathbb{R})$, son image réciproque appartient à la tribu $\mathcal{F}$ :
> $$X^{-1}(B) = \{ \omega \in \Omega \mid X(\omega) \in B \} \in \mathcal{F}$$

**Exemple Concret 1 : Lancer d'une pièce**
Considérons le lancer d'une pièce : $\Omega = \{\text{Pile}, \text{Face}\}$. La tribu triviale maximale est $\mathcal{F} = \mathcal{P}(\Omega) = \{\emptyset, \{\text{Pile}\}, \{\text{Face}\}, \Omega\}$.
Soit le jeu suivant : on gagne 10€ si Pile, on perd 5€ si Face.
La variable aléatoire $X$ est définie par $X(\text{Pile}) = 10$ et $X(\text{Face}) = -5$.
Vérifions la mesurabilité pour un intervalle $B = [0, 20]$.
L'image réciproque est $X^{-1}([0, 20]) = \{ \omega \in \Omega \mid X(\omega) \in [0, 20] \} = \{\text{Pile}\}$.
Or, $\{\text{Pile}\} \in \mathcal{F}$. Cette fonction est bien une variable aléatoire.

**Exemple Concret 2 : Fonction non mesurable (Pathologie)**
Considérons $\Omega = \{a, b, c, d\}$ et une tribu restreinte $\mathcal{F} = \{\emptyset, \{a, b\}, \{c, d\}, \Omega\}$.
Définissons une fonction $Y : \Omega \to \mathbb{R}$ telle que $Y(a)=1, Y(b)=2, Y(c)=3, Y(d)=4$.
Prenons le borélien $B = \{1\}$.
L'image réciproque est $Y^{-1}(\{1\}) = \{a\}$.
Cependant, $\{a\} \notin \mathcal{F}$. Ainsi, $Y$ n'est **pas** une variable aléatoire pour cet espace de probabilité : l'espace n'est pas "assez fin" pour observer la différence entre l'issue $a$ et l'issue $b$.

> **Théorème 1 : Critère de mesurabilité sur les générateurs**
> Soit $\mathcal{C}$ une classe de sous-ensembles de $\mathbb{R}$ qui engendre la tribu borélienne, c'est-à-dire $\sigma(\mathcal{C}) = \mathcal{B}(\mathbb{R})$.
> Une fonction $X : \Omega \to \mathbb{R}$ est une variable aléatoire si et seulement si :
> $$\forall C \in \mathcal{C}, \quad X^{-1}(C) \in \mathcal{F}$$

En pratique, on choisit souvent $\mathcal{C} = \{ ]-\infty, x] \mid x \in \mathbb{R} \}$. Il suffit donc de vérifier que pour tout $x \in \mathbb{R}$, l'ensemble $\{ \omega \in \Omega \mid X(\omega) \leq x \}$ est dans $\mathcal{F}$.

> **Définition 2 : Loi de Probabilité et Mesure Image**
> Soit $X$ une V.A.R. sur $(\Omega, \mathcal{F}, \mathbb{P})$. L'application $X$ permet de transférer la mesure de probabilité $\mathbb{P}$ sur $\mathbb{R}$.
> On définit la **loi de probabilité** de $X$, notée $\mathbb{P}_X$, comme la mesure image sur $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ donnée par :
> $$\forall B \in \mathcal{B}(\mathbb{R}), \quad \mathbb{P}_X(B) = \mathbb{P}(X^{-1}(B)) = \mathbb{P}(\{ \omega \in \Omega \mid X(\omega) \in B \})$$
> On note souvent abusivement $\mathbb{P}(X \in B)$.

**Exemple Concret 3 : Calcul explicite d'une loi image**
Soit un dé équilibré $\Omega = \{1, 2, 3, 4, 5, 6\}$, $\mathcal{F} = \mathcal{P}(\Omega)$ et $\mathbb{P}$ la mesure uniforme ($\mathbb{P}(\{\omega\}) = 1/6$).
Définissons la variable aléatoire $X(\omega) = \omega \pmod 2$ (parité).
Calculons la loi de $X$, $\mathbb{P}_X$ sur $\mathbb{R}$.
$X$ prend les valeurs 0 ou 1.
Pour $B = \{0\}$, $\mathbb{P}_X(\{0\}) = \mathbb{P}(X^{-1}(\{0\})) = \mathbb{P}(\{2, 4, 6\}) = \frac{3}{6} = \frac{1}{2}$.
Pour $B = \{1\}$, $\mathbb{P}_X(\{1\}) = \mathbb{P}(X^{-1}(\{1\})) = \mathbb{P}(\{1, 3, 5\}) = \frac{3}{6} = \frac{1}{2}$.
Ainsi, la loi $\mathbb{P}_X$ est une loi de Bernoulli de paramètre $p=1/2$.

> **Définition 3 : Fonction de Répartition**
> Toute loi de probabilité sur $\mathbb{R}$ est entièrement caractérisée par sa **fonction de répartition** $F_X : \mathbb{R} \to [0, 1]$, définie par :
> $$F_X(x) = \mathbb{P}_X( ]-\infty, x] ) = \mathbb{P}(X \leq x)$$
> $F_X$ possède les propriétés fondamentales suivantes :
> 1. Croissante : Si $x \leq y$, alors $F_X(x) \leq F_X(y)$.
> 2. Continue à droite : $\lim_{h \to 0, h>0} F_X(x+h) = F_X(x)$.
> 3. Limites aux bornes : $\lim_{x \to -\infty} F_X(x) = 0$ et $\lim_{x \to +\infty} F_X(x) = 1$.

**Exemple Concret 4 : Fonction de répartition d'une variable uniforme**
Soit $X$ suivant une loi uniforme sur l'intervalle $[a, b]$, notée $\mathcal{U}([a, b])$.
Par définition, la probabilité de tomber dans un sous-intervalle $[c, d] \subset [a, b]$ est proportionnelle à sa longueur : $\frac{d-c}{b-a}$.
Calculons $F_X(x) = \mathbb{P}(X \leq x)$ pas-à-pas :
- Si $x < a$ : L'événement $\{X \leq x\}$ est impossible (ensemble vide), donc $F_X(x) = 0$.
- Si $a \leq x \leq b$ : L'événement correspond à l'intervalle $[a, x]$. Ainsi, $F_X(x) = \frac{x-a}{b-a}$.
- Si $x > b$ : L'événement $\{X \leq x\}$ est certain (contient tout le support $[a, b]$), donc $F_X(x) = 1$.
C'est une fonction affine croissante sur $[a, b]$, recollée continuement en $0$ et $1$.

> **Théorème 2 : Stabilité par composition**
> Si $X$ est une variable aléatoire réelle sur $(\Omega, \mathcal{F})$, et si $g : \mathbb{R} \to \mathbb{R}$ est une fonction mesurable au sens de Borel, alors la composée $Y = g(X) = g \circ X$ est également une variable aléatoire réelle.

**Exemple Concret 5 : Loi d'une variable transformée géométriquement**
Soit $X \sim \mathcal{U}([-1, 1])$. Déterminons la loi de $Y = X^2$.
On note que $g(x) = x^2$ est continue, donc borélienne. $Y$ est donc une V.A.R.
Calculons la fonction de répartition $F_Y(y)$ :
- Si $y < 0$ : $Y$ étant un carré, $Y \geq 0$, donc $F_Y(y) = \mathbb{P}(Y \leq y) = 0$.
- Si $y \in [0, 1]$ :
  $$F_Y(y) = \mathbb{P}(X^2 \leq y) = \mathbb{P}(-\sqrt{y} \leq X \leq \sqrt{y})$$
  Comme $X \sim \mathcal{U}([-1, 1])$, sa densité est constante égale à $\frac{1}{1 - (-1)} = \frac{1}{2}$.
  La probabilité est donc la longueur de l'intervalle multipliée par la densité :
  $$F_Y(y) = \frac{\sqrt{y} - (-\sqrt{y})}{2} = \frac{2\sqrt{y}}{2} = \sqrt{y}$$
- Si $y > 1$ : L'événement $X^2 \leq y$ est certain car $X \in [-1, 1]$, donc $F_Y(y) = 1$.
Par dérivation, on obtient la densité de $Y$ sur $]0, 1[ : f_Y(y) = \frac{d}{dy}(\sqrt{y}) = \frac{1}{2\sqrt{y}}$. On observe une divergence en 0, caractéristique de cette transformation de mesure.



> **Théorème 3 : L'Indicatrice d'un événement**
> Soit $A \subset \Omega$. La fonction indicatrice $\mathbf{1}_A : \Omega \to \mathbb{R}$ définie par $\mathbf{1}_A(\omega) = 1$ si $\omega \in A$ et $\mathbf{1}_A(\omega) = 0$ sinon, est une variable aléatoire réelle si et seulement si $A \in \mathcal{F}$ (c'est-à-dire si $A$ est un événement mesurable).

**Exemple Concret 6 : L'indicatrice d'un jet de dé pair**
Considérons $\Omega = \{1, 2, 3, 4, 5, 6\}$ avec $\mathcal{F} = \mathcal{P}(\Omega)$.
Soit l'événement $A = \{2, 4, 6\}$ "le résultat est pair".
Définissons $X = \mathbf{1}_A$. $X(\omega)$ vaut $1$ si $\omega \in A$ et $0$ sinon.
Vérifions la mesurabilité. Prenons un intervalle $B = ]0.5, 1.5[$.
L'image réciproque est $X^{-1}(]0.5, 1.5[) = \{ \omega \in \Omega \mid X(\omega) = 1 \} = A = \{2, 4, 6\}$.
Puisque $A \in \mathcal{F}$, la condition est satisfaite sur ce borélien. Comme cela est vrai pour tout borélien, $X$ est une variable aléatoire.

**Exemple Concret 7 : Loi d'une variable transformée affine**
Soit $X$ une variable aléatoire suivant une loi normale standard $\mathcal{N}(0, 1)$. Sa densité est $f_X(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$.
Définissons une transformation affine $Y = \sigma X + \mu$ avec $\sigma > 0$. $Y$ est mesurable par stabilité de la composition avec des fonctions continues.
Calculons la fonction de répartition de $Y$ :
$$F_Y(y) = \mathbb{P}(Y \leq y) = \mathbb{P}(\sigma X + \mu \leq y) = \mathbb{P}\left(X \leq \frac{y - \mu}{\sigma}\right) = F_X\left(\frac{y - \mu}{\sigma}\right)$$
Pour trouver la densité $f_Y$, on dérive cette fonction par rapport à $y$ :
$$f_Y(y) = \frac{d}{dy} \left[ F_X\left(\frac{y - \mu}{\sigma}\right) \right] = \frac{1}{\sigma} f_X\left(\frac{y - \mu}{\sigma}\right) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(y - \mu)^2}{2\sigma^2}}$$
On retrouve ainsi explicitement la densité de la loi $\mathcal{N}(\mu, \sigma^2)$, montrant la puissance du calcul sur les variables aléatoires.

## 3. Démonstrations

### Démonstration 1 : Le critère de mesurabilité sur les générateurs (Théorème 1)

Nous voulons prouver que si $\mathcal{C}$ engendre $\mathcal{B}(\mathbb{R})$ (i.e. $\sigma(\mathcal{C}) = \mathcal{B}(\mathbb{R})$) et si $\forall C \in \mathcal{C}, X^{-1}(C) \in \mathcal{F}$, alors $X$ est mesurable.

1. **Condition Nécessaire :**
   Si $X$ est mesurable, alors pour tout borélien $B \in \mathcal{B}(\mathbb{R})$, $X^{-1}(B) \in \mathcal{F}$. Puisque $\mathcal{C} \subset \mathcal{B}(\mathbb{R})$, il est évident que pour tout $C \in \mathcal{C}$, on a bien $X^{-1}(C) \in \mathcal{F}$.

2. **Condition Suffisante :**
   Supposons que $\forall C \in \mathcal{C}, X^{-1}(C) \in \mathcal{F}$.
   Considérons la classe d'ensembles $\mathcal{A}$ définie par l'image directe dans l'espace d'arrivée qui se comporte bien vis-à-vis de la tribu de départ :
   $$\mathcal{A} = \{ B \subset \mathbb{R} \mid X^{-1}(B) \in \mathcal{F} \}$$

   Montrons que $\mathcal{A}$ est une tribu sur $\mathbb{R}$ :
   - **Ensemble total :** $X^{-1}(\mathbb{R}) = \Omega \in \mathcal{F}$, donc $\mathbb{R} \in \mathcal{A}$.
   - **Stabilité par complémentation :** Soit $B \in \mathcal{A}$. Considérons son complémentaire $B^c = \mathbb{R} \setminus B$.
     Par propriété de l'image réciproque, $X^{-1}(B^c) = \Omega \setminus X^{-1}(B) = (X^{-1}(B))^c$.
     Comme $\mathcal{F}$ est une tribu et que $X^{-1}(B) \in \mathcal{F}$, son complémentaire est aussi dans $\mathcal{F}$.
     Ainsi, $X^{-1}(B^c) \in \mathcal{F}$, donc $B^c \in \mathcal{A}$.
   - **Stabilité par union dénombrable :** Soit $(B_n)_{n \in \mathbb{N}}$ une suite d'éléments de $\mathcal{A}$.
     On a $X^{-1}\left( \bigcup_{n \in \mathbb{N}} B_n \right) = \bigcup_{n \in \mathbb{N}} X^{-1}(B_n)$.
     Par hypothèse, chaque $X^{-1}(B_n) \in \mathcal{F}$. Comme $\mathcal{F}$ est une tribu, elle est stable par union dénombrable.
     Donc $\bigcup X^{-1}(B_n) \in \mathcal{F}$, d'où $\bigcup_{n \in \mathbb{N}} B_n \in \mathcal{A}$.

   Nous avons établi que $\mathcal{A}$ est une tribu sur $\mathbb{R}$.
   Par hypothèse initiale, $\mathcal{C} \subset \mathcal{A}$.
   Puisque $\mathcal{A}$ est une tribu contenant $\mathcal{C}$, elle contient nécessairement la plus petite tribu contenant $\mathcal{C}$, qui n'est autre que $\sigma(\mathcal{C})$.
   Or, $\sigma(\mathcal{C}) = \mathcal{B}(\mathbb{R})$. Donc $\mathcal{B}(\mathbb{R}) \subset \mathcal{A}$.
   Ceci implique que pour tout $B \in \mathcal{B}(\mathbb{R})$, $B \in \mathcal{A}$, c'est-à-dire $X^{-1}(B) \in \mathcal{F}$.
   La fonction $X$ est donc mesurable. La preuve est achevée.

### Démonstration 2 : Stabilité par composition (Théorème 2)

Nous souhaitons montrer que si $X$ est $\mathcal{F}$-mesurable et $g$ est borélienne, alors $g \circ X$ est $\mathcal{F}$-mesurable.

1. Soit $B \in \mathcal{B}(\mathbb{R})$ un borélien quelconque de l'espace d'arrivée de $g$.
2. Nous devons examiner l'image réciproque de $B$ par l'application composée $Y = g \circ X$ :
   $$Y^{-1}(B) = (g \circ X)^{-1}(B)$$
3. Par les propriétés élémentaires des applications, l'image réciproque par une composée est la composée des images réciproques :
   $$(g \circ X)^{-1}(B) = X^{-1}(g^{-1}(B))$$
4. Puisque $g$ est une fonction mesurable au sens de Borel (de $\mathbb{R}$ dans $\mathbb{R}$), et que $B$ est un borélien, l'image réciproque $g^{-1}(B)$ est, par définition, un ensemble borélien de $\mathbb{R}$. Notons $B' = g^{-1}(B) \in \mathcal{B}(\mathbb{R})$.
5. Il reste alors à évaluer $X^{-1}(B')$. Puisque $X$ est une variable aléatoire mesurable, et que $B'$ est un borélien, $X^{-1}(B') \in \mathcal{F}$.
6. En conclusion, $Y^{-1}(B) \in \mathcal{F}$ pour tout borélien $B$, ce qui démontre rigoureusement que la composée $Y = g \circ X$ est une variable aléatoire réelle.


### Démonstration 3 : L'Indicatrice d'un événement (Théorème 3)

Nous voulons prouver que la fonction indicatrice $\mathbf{1}_A : \Omega \to \mathbb{R}$ est une variable aléatoire si et seulement si $A \in \mathcal{F}$.

1. **Condition Nécessaire :**
   Supposons que $\mathbf{1}_A$ soit une variable aléatoire. Cela signifie que pour tout borélien $B \in \mathcal{B}(\mathbb{R})$, l'image réciproque $\mathbf{1}_A^{-1}(B)$ appartient à $\mathcal{F}$.
   Prenons le borélien $B = \{1\}$.
   Calculons $\mathbf{1}_A^{-1}(\{1\}) = \{ \omega \in \Omega \mid \mathbf{1}_A(\omega) = 1 \} = A$.
   Puisque l'image réciproque de tout borélien doit être dans $\mathcal{F}$, on a immédiatement que $A \in \mathcal{F}$.

2. **Condition Suffisante :**
   Supposons que $A \in \mathcal{F}$. Nous devons montrer que pour tout borélien $B \in \mathcal{B}(\mathbb{R})$, l'image réciproque $\mathbf{1}_A^{-1}(B)$ est dans $\mathcal{F}$.
   La fonction $\mathbf{1}_A$ ne peut prendre que les valeurs $0$ et $1$. Ainsi, pour un borélien quelconque $B$, il n'y a que quatre cas possibles :
   - Cas 1 : $1 \in B$ et $0 \notin B$. Alors $\mathbf{1}_A^{-1}(B) = \{ \omega \in \Omega \mid \mathbf{1}_A(\omega) = 1 \} = A$. Or $A \in \mathcal{F}$ par hypothèse.
   - Cas 2 : $0 \in B$ et $1 \notin B$. Alors $\mathbf{1}_A^{-1}(B) = \{ \omega \in \Omega \mid \mathbf{1}_A(\omega) = 0 \} = A^c$. Puisque $A \in \mathcal{F}$ et que $\mathcal{F}$ est une tribu, son complémentaire $A^c$ est aussi dans $\mathcal{F}$.
   - Cas 3 : $0 \in B$ et $1 \in B$. Alors $\mathbf{1}_A^{-1}(B) = \Omega$. Et $\Omega \in \mathcal{F}$ par définition d'une tribu.
   - Cas 4 : $0 \notin B$ et $1 \notin B$. Alors $\mathbf{1}_A^{-1}(B) = \emptyset$. Et $\emptyset \in \mathcal{F}$ par définition d'une tribu.

   Dans tous les cas possibles, $\mathbf{1}_A^{-1}(B) \in \mathcal{F}$. La fonction $\mathbf{1}_A$ est donc bien une variable aléatoire.

## 4. Applications en Physique, Logique, & AI

### Application à l'Intelligence Artificielle et l'Apprentissage Profond

Le formalisme des applications mesurables est l'échine dorsale théorique de l'apprentissage automatique moderne.

1. **Variables Aléatoires Multi-Dimensionnelles et Tenseurs :** En apprentissage profond, une image, un son, ou un texte vectorisé n'est rien d'autre qu'une réalisation complexe d'un vecteur aléatoire $\mathbf{X}$ (variable aléatoire à valeurs dans $\mathbb{R}^d$). La loi de probabilité abstraite du monde réel (ex: "la distribution des images de chats") est transférée par l'application mesurable de capture (les capteurs CCD de l'appareil photo) vers une mesure image dans $\mathbb{R}^d$.

2. **Transformations Non-Linéaires (Fonctions d'Activation) :** Le théorème de stabilité par composition garantit que si notre tenseur d'entrée suit une certaine loi de probabilité, toute transformation mathématique appliquée par une couche de réseau de neurones engendre une nouvelle variable aléatoire valide.
   Prenons la fonction ReLU : $g(x) = \max(0, x)$. Cette fonction est continue, donc borélienne. Par conséquent, si $Z$ est l'activation linéaire de la couche ($Z = WX+b$), la sortie de la couche $A = \text{ReLU}(Z)$ est une application mesurable stricte. Ce passage crée un "atome" de probabilité (une masse de Dirac) en $0$ car $\mathbb{P}(A=0) = \mathbb{P}(Z \leq 0)$, transformant ainsi une distribution continue en une distribution mixte, parfaitement gérable grâce à la rigueur de la théorie de la mesure.

3. **Modèles Génératifs (GANs et Diffusion) :** Les architectures génératives exploitent directement le transport de mesure. Dans un réseau antagoniste génératif (GAN), on se donne un bruit latent $Z$ de loi simple (ex: Normale univariée) sur $\mathbb{R}^k$. Le générateur est modélisé par un réseau de neurones $G_\theta : \mathbb{R}^k \to \mathbb{R}^d$. D'après les théorèmes démontrés, $G_\theta$ étant une composition de fonctions continues, c'est une application mesurable. L'objectif entier du réseau est de déformer l'espace pour que la loi image (le *pushforward measure* noté $(G_\theta)_{\#}\mathbb{P}_Z$) coïncide asymptotiquement avec la mesure empirique des données d'apprentissage $\mathbb{P}_{data}$.
