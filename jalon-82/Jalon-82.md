---
uuid: "jalon-82"
title: "Introduction aux distributions de Schwartz"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 81 (Transformée de Fourier dans L2).md]]"
next: "[[Jalon 83 (Dérivation au sens des distributions).md]]"
---

# Introduction aux distributions de Schwartz

## 1. Introduction historique et genèse physique

La notion de fonction, bien qu'extraordinairement utile en mathématiques classiques, a montré ses limites au début du XXe siècle, particulièrement en physique. Comment décrire mathématiquement une force ponctuelle (un coup de marteau), une charge électrique ponctuelle, ou encore une source lumineuse infiniment petite mais d'intensité finie ?

Si l'on tente d'utiliser une fonction classique $f(x)$ pour modéliser un "pic" à l'origine (par exemple une masse ponctuelle unitaire en $0$), cette fonction devrait satisfaire $f(x) = 0$ pour tout $x \neq 0$ et $\int_{-\infty}^{+\infty} f(x) dx = 1$. Or, d'après la théorie de l'intégration de Lebesgue, une fonction nulle presque partout a une intégrale nulle. Il y a donc une contradiction fondamentale.

C'est Laurent Schwartz (médaille Fields en 1950) qui a rigoureusement formalisé ces objets, appelés **distributions**. L'idée géniale de Schwartz est de ne plus regarder un objet mathématique par ses "valeurs ponctuelles" $f(x)$ (qui peuvent ne pas avoir de sens), mais par sa "réaction" lorsqu'on le teste avec des fonctions très régulières, appelées **fonctions tests**.

\begin{tikzpicture}[scale=1]
  \draw[->] (-3,0) -- (3,0) node[right] {$x$};
  \draw[->] (0,-0.5) -- (0,3) node[above] {$y$};
  \draw[thick, blue] (-2.5,0) -- (-0.5,0) -- (0, 2.5) -- (0.5, 0) -- (2.5,0);
  \node at (0, -0.3) {$0$};
  \node at (2, 2) {Approximation de $\delta_0$};
\end{tikzpicture}

## 2. Définitions, Théorèmes et Exemples

### A. L'espace des fonctions tests $\mathcal{D}(\mathbb{R})$

Pour définir une distribution, nous devons d'abord définir l'espace des fonctions qui vont servir à "tester" ou "sondes" ces distributions.

> **Définition 1 (Espace des fonctions tests $\mathcal{D}(\mathbb{R})$) :**
> L'espace $\mathcal{D}(\mathbb{R})$ (aussi noté $C_c^\infty(\mathbb{R})$) est l'ensemble des fonctions $\phi : \mathbb{R} \to \mathbb{C}$ qui satisfont simultanément deux conditions :
> 1. Elles sont infiniment dérivables sur $\mathbb{R}$ ($\phi \in C^\infty(\mathbb{R})$).
> 2. Elles sont à support compact, c'est-à-dire qu'il existe un segment borné $[-A, A]$ en dehors duquel la fonction est identiquement nulle.

**Exemple 1 : La fonction "bosse" (bump function)**
Considérons la fonction :
$$\phi(x) = \begin{cases} \exp\left(-\frac{1}{1-x^2}\right) & \text{si } |x| < 1 \\ 0 & \text{si } |x| \ge 1 \end{cases}$$
Calculons ses dérivées. Pour $x \in (-1, 1)$, $\phi'(x) = -\frac{2x}{(1-x^2)^2} \exp\left(-\frac{1}{1-x^2}\right)$. Lorsque $x \to 1^-$ ou $x \to -1^+$, l'exponentielle l'emporte sur toute fraction rationnelle, donc toutes les dérivées tendent vers $0$. La fonction se recolle de manière $C^\infty$ avec la constante $0$ sur $|x| \ge 1$. Son support est exactement $[-1, 1]$. C'est une fonction test typique.

**Exemple 2 : Une fonction non test**
La fonction gaussienne $f(x) = e^{-x^2}$ est bien infiniment dérivable, mais son support est $\mathbb{R}$ tout entier (elle ne s'annule jamais). Donc $f \notin \mathcal{D}(\mathbb{R})$.

### B. Notion de convergence dans $\mathcal{D}(\mathbb{R})$

Pour pouvoir définir des formes linéaires *continues* (qui seront nos distributions), il faut doter $\mathcal{D}(\mathbb{R})$ d'une notion de convergence.

> **Définition 2 (Convergence dans $\mathcal{D}(\mathbb{R})$) :**
> Soit $(\phi_n)_{n \in \mathbb{N}}$ une suite de fonctions de $\mathcal{D}(\mathbb{R})$ et $\phi \in \mathcal{D}(\mathbb{R})$. On dit que $\phi_n \to \phi$ dans $\mathcal{D}(\mathbb{R})$ si :
> 1. Il existe un compact (un intervalle fermé borné) $K \subset \mathbb{R}$ qui contient le support de toutes les $\phi_n$ ainsi que celui de $\phi$.
> 2. Pour tout entier $k \ge 0$, la suite des dérivées d'ordre $k$, $(\phi_n^{(k)})_{n \in \mathbb{N}}$, converge uniformément vers $\phi^{(k)}$ sur $K$.

### C. Définition des Distributions

> **Définition 3 (Distribution de Schwartz) :**
> Une **distribution** sur $\mathbb{R}$ est une application linéaire continue de $\mathcal{D}(\mathbb{R})$ dans $\mathbb{C}$. L'espace vectoriel de toutes les distributions est noté $\mathcal{D}'(\mathbb{R})$.
> Si $T \in \mathcal{D}'(\mathbb{R})$ et $\phi \in \mathcal{D}(\mathbb{R})$, l'image de $\phi$ par $T$ est souvent notée par le crochet de dualité $\langle T, \phi \rangle$ au lieu de $T(\phi)$.

Dire que $T$ est linéaire et continue signifie :
1. **Linéarité :** $\langle T, \lambda \phi + \mu \psi \rangle = \lambda \langle T, \phi \rangle + \mu \langle T, \psi \rangle$.
2. **Continuité (séquentielle) :** Si $\phi_n \to \phi$ dans $\mathcal{D}(\mathbb{R})$, alors la suite de nombres complexes $\langle T, \phi_n \rangle$ converge vers le nombre $\langle T, \phi \rangle$ dans $\mathbb{C}$.

### D. Distributions régulières et singulières

**1. Distributions régulières**

Toute fonction $f$ "raisonnable" peut être identifiée à une distribution. Une fonction est raisonnable si on peut l'intégrer localement.

> **Définition 4 (Fonction localement intégrable) :**
> Une fonction $f : \mathbb{R} \to \mathbb{C}$ (mesurable) est dite localement intégrable (noté $f \in L^1_{loc}(\mathbb{R})$) si pour tout segment compact $[a, b]$, l'intégrale $\int_a^b |f(x)| dx < +\infty$.

> **Proposition 1 :**
> À toute fonction $f \in L^1_{loc}(\mathbb{R})$, on associe canoniquement une distribution $T_f$ définie par :
> $$\langle T_f, \phi \rangle = \int_{-\infty}^{+\infty} f(x) \phi(x) dx \quad \text{pour tout } \phi \in \mathcal{D}(\mathbb{R})$$
> Une telle distribution est appelée **distribution régulière**.

**Exemple 3 : Distribution associée à la fonction constante**
Soit $f(x) = 1$ pour tout $x$. C'est une fonction $L^1_{loc}$. La distribution associée est :
$$\langle T_1, \phi \rangle = \int_{-\infty}^{+\infty} 1 \cdot \phi(x) dx = \int_{\text{supp}(\phi)} \phi(x) dx$$

**Exemple 4 : La fonction d'Heaviside**
La fonction d'Heaviside (échelon unité) est définie par $H(x) = 1$ si $x > 0$, et $H(x) = 0$ si $x \le 0$. C'est une fonction localement intégrable. La distribution associée agit ainsi :
$$\langle T_H, \phi \rangle = \int_{-\infty}^{+\infty} H(x) \phi(x) dx = \int_0^{+\infty} \phi(x) dx$$

**2. Distributions singulières**

Une distribution est dite **singulière** s'il n'existe aucune fonction $f \in L^1_{loc}$ telle que $T = T_f$.

> **Définition 5 (La distribution de Dirac) :**
> Pour tout $a \in \mathbb{R}$, on définit la distribution de Dirac en $a$, notée $\delta_a$, par :
> $$\langle \delta_a, \phi \rangle = \phi(a) \quad \text{pour tout } \phi \in \mathcal{D}(\mathbb{R})$$
> En particulier, pour $a = 0$, $\langle \delta_0, \phi \rangle = \phi(0)$.

**Exemple 5 : Combinaison de Diracs**
Soit $T = 3\delta_1 - 2\delta_{-1}$. Son action sur une fonction test $\phi$ est :
$$\langle T, \phi \rangle = 3\phi(1) - 2\phi(-1)$$

## 3. Démonstrations

### Démonstration 1 : $\delta_0$ est bien une distribution

Nous devons prouver que l'application $\phi \mapsto \phi(0)$ est linéaire et continue sur $\mathcal{D}(\mathbb{R})$.

**Étape 1 : Linéarité**
Soient $\phi, \psi \in \mathcal{D}(\mathbb{R})$ et $\lambda, \mu \in \mathbb{C}$.
$\langle \delta_0, \lambda\phi + \mu\psi \rangle = (\lambda\phi + \mu\psi)(0) = \lambda\phi(0) + \mu\psi(0) = \lambda\langle \delta_0, \phi \rangle + \mu\langle \delta_0, \psi \rangle$.
La linéarité est immédiate.

**Étape 2 : Continuité**
Soit $(\phi_n)_{n \in \mathbb{N}}$ une suite de fonctions de $\mathcal{D}(\mathbb{R})$ convergeant vers $\phi$ dans $\mathcal{D}(\mathbb{R})$.
Par définition de la convergence dans $\mathcal{D}(\mathbb{R})$, la suite $(\phi_n)_{n \in \mathbb{N}}$ converge uniformément vers $\phi$ sur un certain compact $K$.
La convergence uniforme implique la convergence simple, en particulier au point $x=0$.
Donc $\lim_{n \to \infty} \phi_n(0) = \phi(0)$, ce qui se réécrit :
$\lim_{n \to \infty} \langle \delta_0, \phi_n \rangle = \langle \delta_0, \phi \rangle$.
L'application est donc continue séquentiellement. $\delta_0$ est bien une distribution.

### Démonstration 2 : Le caractère singulier de $\delta_0$ (Le Dirac n'est pas une fonction)

Nous allons démontrer rigoureusement par l'absurde qu'il n'existe aucune fonction $f \in L^1_{loc}(\mathbb{R})$ telle que $T_f = \delta_0$.

**Étape 1 : Hypothèse absurde**
Supposons qu'il existe une fonction $f \in L^1_{loc}(\mathbb{R})$ telle que pour tout $\phi \in \mathcal{D}(\mathbb{R})$, on ait :
$$\int_{-\infty}^{+\infty} f(x) \phi(x) dx = \phi(0)$$

**Étape 2 : Construction d'une suite de fonctions tests**
Soit $\psi \in \mathcal{D}(\mathbb{R})$ une fonction "bosse" (comme celle de l'Exemple 1) vérifiant :
1. $\psi(x) \ge 0$ pour tout $x$.
2. $\psi(0) = 1$.
3. Le support de $\psi$ est inclus dans $[-1, 1]$.

Pour chaque entier $n \ge 1$, on définit $\phi_n(x) = \psi(nx)$.
Propriétés de $\phi_n$ :
- $\phi_n \in \mathcal{D}(\mathbb{R})$.
- $\phi_n(0) = \psi(0) = 1$.
- Le support de $\phi_n$ est inclus dans $[-1/n, 1/n]$.
- $0 \le \phi_n(x) \le \max(\psi)$ pour tout $x$. Posons $M = \max(\psi) = 1$.

**Étape 3 : Évaluation par la distribution supposée**
D'une part, par notre hypothèse absurde :
$$\langle T_f, \phi_n \rangle = \phi_n(0) = 1 \quad \text{pour tout } n \ge 1$$
Donc la limite de $\langle T_f, \phi_n \rangle$ quand $n \to \infty$ est $1$.

**Étape 4 : Majoration de l'intégrale**
D'autre part, évaluons l'intégrale correspondante :
$$\langle T_f, \phi_n \rangle = \int_{-\infty}^{+\infty} f(x) \phi_n(x) dx = \int_{-1/n}^{1/n} f(x) \phi_n(x) dx$$
Prenons la valeur absolue :
$$|\langle T_f, \phi_n \rangle| \le \int_{-1/n}^{1/n} |f(x)| |\phi_n(x)| dx \le \int_{-1/n}^{1/n} |f(x)| \cdot 1 dx$$
Puisque $f \in L^1_{loc}(\mathbb{R})$, la fonction $|f|$ est intégrable. Par le théorème de convergence dominée de Lebesgue (ou la continuité absolue de l'intégrale de Lebesgue), l'intégrale d'une fonction intégrable sur un domaine de mesure tendant vers 0 tend vers 0.
Ainsi, $\lim_{n \to \infty} \int_{-1/n}^{1/n} |f(x)| dx = 0$.

**Étape 5 : Contradiction**
Nous avons d'un côté $\lim_{n \to \infty} \langle T_f, \phi_n \rangle = 1$ et de l'autre $|\langle T_f, \phi_n \rangle| \to 0$.
C'est une contradiction flagrante ($1 = 0$). L'hypothèse de départ est donc fausse. La distribution de Dirac ne peut pas être représentée par une fonction localement intégrable.

## 4. Applications en Physique, Logique et Intelligence Artificielle

**Physique (Mécanique et Électromagnétisme)**
La distribution de Dirac est fondamentale pour décrire les charges ponctuelles. La densité de charge $\rho(x)$ d'une particule de charge $q$ située en $x=a$ est précisément $q \delta_a$. De même, une force impulsionnelle (un choc d'une fraction de seconde) se modélise par $F(t) = P \delta(t-t_0)$ où $P$ est la variation de quantité de mouvement.

**Traitement du signal et Analyse Spectrale**
Le Dirac permet d'étendre la transformée de Fourier aux fonctions périodiques. La transformée de Fourier de la fonction constante $f(t) = 1$ n'a pas de sens avec l'intégrale classique de Lebesgue, mais au sens des distributions, $\mathcal{F}(1) = 2\pi \delta_0$. Un signal pur (une sinusoïde de fréquence $\nu_0$) possède un spectre composé de deux pics de Dirac en $\pm \nu_0$.

**Intelligence Artificielle et Mesures Empiriques**
Dans l'apprentissage automatique, lorsqu'on dispose d'un jeu de données fini de $N$ points $x_1, \dots, x_N$, on modélise souvent la distribution de probabilité des données par la mesure empirique :
$$\hat{p}(x) = \frac{1}{N} \sum_{i=1}^N \delta_{x_i}(x)$$
Cette "densité de probabilité" est une distribution de Schwartz. Les fonctions de perte (comme la Negative Log-Likelihood) calculées sur ce jeu de données reviennent mathématiquement à évaluer des fonctions tests (les prédictions du modèle) contre cette distribution empirique de Diracs.
