---
uuid: "jalon-93"
title: "Fonctions caractéristiques"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/abstraction
prev: "[[Jalon 92 (Loi forte des grands nombres (LFGN)).md]]"
next: "[[Jalon 94 (Démonstration du théorème central limite).md]]"
---

# Jalon 93 : Fonctions caractéristiques

## 1. Introduction

La naissance de la notion de fonction caractéristique s'inscrit dans la quête d'une simplification radicale des opérations sur les variables aléatoires. Historiquement, l'étude des sommes de variables aléatoires indépendantes se heurtait à un obstacle calculatoire majeur : la densité de la somme de deux variables indépendantes est donnée par le produit de convolution de leurs densités respectives. Cette opération intégrale, bien que rigoureuse, devient rapidement inexploitable, analytiquement et numériquement, lorsqu'on itère le processus sur de grandes sommes.

Des mathématiciens comme Pierre-Simon Laplace et Joseph Fourier, confrontés à l'analyse harmonique et à l'étude des équations de la chaleur, ont jeté les bases d'un passage du domaine spatial (ou temporel) au domaine fréquentiel. L'intuition fulgurante d'Aleksandr Lyapunov puis d'Andreï Kolmogorov fut d'adapter cette transformée de Fourier aux mesures de probabilité. L'idée physique sous-jacente est que toute loi de probabilité peut être décomposée en un spectre d'oscillations complexes. Analyser les "fréquences" de cette distribution au lieu de ses "valeurs" permet de contourner la convolution : dans le domaine des fonctions caractéristiques, la convolution de mesures se métamorphose en une simple multiplication algébrique de fonctions.

Géométriquement, l'espérance $\mathbb{E}[e^{itX}]$ représente le barycentre d'une distribution de masse enroulée autour du cercle unité dans le plan complexe. La vitesse à laquelle ce barycentre s'éloigne du bord du cercle lorsque la fréquence $t$ varie encode de manière univoque toutes les propriétés statistiques (moments, queues de distribution, comportement asymptotique) de la variable $X$.

## 2. Définitions et structures fondamentales

> **Définition (Fonction caractéristique) :**
> Soit $(\Omega, \mathcal{F}, P)$ un espace probabilisé et $X : \Omega \to \mathbb{R}$ une variable aléatoire réelle.
> La fonction caractéristique de $X$, notée $\phi_X$, est l'application $\phi_X : \mathbb{R} \to \mathbb{C}$ définie par :
> $$\forall t \in \mathbb{R}, \quad \phi_X(t) = \mathbb{E}\left[e^{itX}\right] = \int_{\Omega} e^{itX(\omega)} dP(\omega)$$
> Si $X$ admet une loi de probabilité $P_X$ sur $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$, on peut écrire, d'après le théorème de transfert :
> $$\forall t \in \mathbb{R}, \quad \phi_X(t) = \int_{\mathbb{R}} e^{itx} dP_X(x)$$

**Exemple concret calculatoire : La loi de Bernoulli**
Prenons une variable $X \sim \mathcal{B}(p)$ avec $p \in [0, 1]$.
Par définition, $X$ prend la valeur $1$ avec probabilité $p$ et la valeur $0$ avec probabilité $q = 1-p$.
Appliquons la définition de la fonction caractéristique pour un réel $t$ fixé :
$\phi_X(t) = \mathbb{E}[e^{itX}] = p e^{it \cdot 1} + q e^{it \cdot 0}$
$\phi_X(t) = p e^{it} + (1-p) \cdot 1 = 1 - p + p e^{it}$
Pour $p = 0.5$, $\phi_X(t) = 0.5 + 0.5 e^{it} = e^{it/2}\cos(t/2)$. Géométriquement, l'image de $\mathbb{R}$ par $\phi_X$ est un cercle dans $\mathbb{C}$ centré en $1-p$ et de rayon $p$.

> **Théorème (Régularité et bornitude) :**
> Pour toute variable aléatoire $X$, la fonction caractéristique $\phi_X$ vérifie :
> 1. $\phi_X(0) = 1$
> 2. $\forall t \in \mathbb{R}, \quad |\phi_X(t)| \le 1$
> 3. $\phi_X$ est uniformément continue sur $\mathbb{R}$.
> 4. $\forall t \in \mathbb{R}, \quad \phi_X(-t) = \overline{\phi_X(t)}$

> **Théorème (Caractérisation de l'indépendance) :**
> Soient $X$ et $Y$ deux variables aléatoires réelles indépendantes. Alors la fonction caractéristique de leur somme $S = X + Y$ est donnée par le produit de leurs fonctions caractéristiques respectives :
> $$\forall t \in \mathbb{R}, \quad \phi_{X+Y}(t) = \phi_X(t) \cdot \phi_Y(t)$$

**Exemple concret calculatoire : Somme de deux variables de Poisson indépendantes**
Soient $X \sim \mathcal{P}(\lambda_1)$ et $Y \sim \mathcal{P}(\lambda_2)$ indépendantes.
Calculons d'abord $\phi_X(t)$ :
$\phi_X(t) = \sum_{k=0}^{\infty} e^{itk} e^{-\lambda_1} \frac{\lambda_1^k}{k!} = e^{-\lambda_1} \sum_{k=0}^{\infty} \frac{(\lambda_1 e^{it})^k}{k!} = e^{-\lambda_1} e^{\lambda_1 e^{it}} = e^{\lambda_1(e^{it} - 1)}$
De même, $\phi_Y(t) = e^{\lambda_2(e^{it} - 1)}$.
D'après le théorème précédent, la fonction caractéristique de $Z = X+Y$ est :
$\phi_Z(t) = \phi_X(t) \phi_Y(t) = e^{\lambda_1(e^{it} - 1)} e^{\lambda_2(e^{it} - 1)} = e^{(\lambda_1 + \lambda_2)(e^{it} - 1)}$
On reconnaît exactement l'expression de la fonction caractéristique d'une variable de loi de Poisson de paramètre $\lambda_1 + \lambda_2$. Le théorème d'injectivité (énoncé plus bas) permet de conclure rigoureusement que $X+Y \sim \mathcal{P}(\lambda_1 + \lambda_2)$.

> **Théorème (Lien avec les moments d'ordre supérieur) :**
> Soit $X$ une variable aléatoire réelle. Si $X$ admet un moment absolu d'ordre $n$, c'est-à-dire si $\mathbb{E}[|X|^n] < \infty$ pour un entier $n \ge 1$, alors la fonction caractéristique $\phi_X$ est de classe $C^n$ sur $\mathbb{R}$ et l'on a :
> $$\forall k \in \{1, \dots, n\}, \quad \phi_X^{(k)}(0) = i^k \mathbb{E}[X^k]$$
> En particulier, on obtient le développement limité suivant au voisinage de zéro :
> $$\phi_X(t) = \sum_{k=0}^n \frac{(it)^k}{k!} \mathbb{E}[X^k] + o(t^n)$$

> **Théorème (Théorème d'inversion de Fourier-Lévy et Injectivité) :**
> L'application qui, à une mesure de probabilité $P_X$, associe sa fonction caractéristique $\phi_X$, est injective. Deux variables aléatoires ont la même fonction caractéristique si et seulement si elles ont même loi.
> De plus, si $\phi_X$ est intégrable sur $\mathbb{R}$ par rapport à la mesure de Lebesgue (i.e. $\int_{\mathbb{R}} |\phi_X(t)| dt < \infty$), alors la variable $X$ admet une densité $f_X$ continue, bornée, donnée par la formule d'inversion :
> $$\forall x \in \mathbb{R}, \quad f_X(x) = \frac{1}{2\pi} \int_{\mathbb{R}} e^{-itx} \phi_X(t) dt$$

## 3. Démonstrations

### Démonstration de la continuité uniforme de la fonction caractéristique

Soit $X$ une variable aléatoire réelle, et $\phi_X$ sa fonction caractéristique.
Nous voulons montrer que $\forall \epsilon > 0, \exists \delta > 0, \forall t, h \in \mathbb{R}, |h| < \delta \implies |\phi_X(t+h) - \phi_X(t)| < \epsilon$.

Soient $t, h \in \mathbb{R}$. Considérons la différence absolue :
$|\phi_X(t+h) - \phi_X(t)| = \left| \mathbb{E}[e^{i(t+h)X}] - \mathbb{E}[e^{itX}] \right|$
Par linéarité de l'espérance, on factorise :
$|\phi_X(t+h) - \phi_X(t)| = \left| \mathbb{E}[e^{itX} (e^{ihX} - 1)] \right|$
En appliquant l'inégalité triangulaire pour l'espérance (le module de l'intégrale est majoré par l'intégrale du module) :
$|\phi_X(t+h) - \phi_X(t)| \le \mathbb{E}\left[ \left| e^{itX} (e^{ihX} - 1) \right| \right]$
Puisque $|e^{itX}| = 1$, il vient :
$|\phi_X(t+h) - \phi_X(t)| \le \mathbb{E}\left[ |e^{ihX} - 1| \right]$
Cette dernière expression est indépendante de $t$, ce qui est la clé pour obtenir la continuité *uniforme*. Il reste à montrer que cette espérance tend vers 0 lorsque $h \to 0$.

Définissons la variable aléatoire $Y_h = |e^{ihX} - 1|$.
Pour chaque $\omega \in \Omega$, lorsque $h \to 0$, $ihX(\omega) \to 0$, donc par continuité de l'exponentielle complexe, $e^{ihX(\omega)} \to 1$. Ainsi, $Y_h \to 0$ presque sûrement.
De plus, par inégalité triangulaire, $|Y_h| = |e^{ihX} - 1| \le |e^{ihX}| + 1 = 2$.
La variable $Y_h$ est donc dominée par la constante $2$, qui est trivialement intégrable (espérance finie valant $2$) sur tout espace probabilisé de masse totale 1.
Par le Théorème de Convergence Dominée de Lebesgue, on peut intervertir la limite et l'espérance :
$\lim_{h \to 0} \mathbb{E}[Y_h] = \mathbb{E}\left[ \lim_{h \to 0} Y_h \right] = \mathbb{E}[0] = 0$.
Ainsi, $\forall \epsilon > 0$, il existe $\delta > 0$ tel que pour tout $h$ avec $|h| < \delta$, $\mathbb{E}[|e^{ihX} - 1|] < \epsilon$.
On en déduit que pour tout $t$, $|\phi_X(t+h) - \phi_X(t)| < \epsilon$, ce qui prouve la continuité uniforme sur $\mathbb{R}$.

### Démonstration du théorème de régularité (lien avec les moments d'ordre 1)

Supposons que $\mathbb{E}[|X|] < \infty$. Montrons que $\phi_X$ est dérivable et que $\phi_X'(0) = i \mathbb{E}[X]$.
Le taux d'accroissement de $\phi_X$ en $t$ est :
$\frac{\phi_X(t+h) - \phi_X(t)}{h} = \mathbb{E}\left[ \frac{e^{i(t+h)X} - e^{itX}}{h} \right] = \mathbb{E}\left[ e^{itX} \frac{e^{ihX} - 1}{h} \right]$
Considérons la variable aléatoire sous l'espérance : $Z_h = e^{itX} \frac{e^{ihX} - 1}{h}$.
Pour tout $\omega$ fixé, on sait que $\lim_{h \to 0} \frac{e^{ihX(\omega)} - 1}{h} = iX(\omega)$, car c'est la dérivée de $u \mapsto e^{iuX}$ évaluée en $0$.
Donc, presque sûrement, $Z_h \xrightarrow{h \to 0} i X e^{itX}$.
Pour appliquer à nouveau le théorème de convergence dominée, il nous faut majorer $|Z_h|$ indépendamment de $h$.
On utilise l'inégalité classique des accroissements finis sur le cercle trigonométrique : $|e^{ia} - e^{ib}| \le |a - b|$ pour tous réels $a, b$.
En prenant $a = hX$ et $b = 0$, on obtient $|e^{ihX} - 1| \le |hX|$.
Ainsi, $|Z_h| = \left| \frac{e^{ihX} - 1}{h} \right| \le \frac{|hX|}{|h|} = |X|$.
L'hypothèse $\mathbb{E}[|X|] < \infty$ nous garantit que la fonction majorante $|X|$ est intégrable.
Le Théorème de Convergence Dominée s'applique et donne :
$\lim_{h \to 0} \mathbb{E}[Z_h] = \mathbb{E}\left[ \lim_{h \to 0} Z_h \right] = \mathbb{E}[i X e^{itX}]$
Ce qui démontre que la dérivée existe et vaut $\phi'_X(t) = i \mathbb{E}[X e^{itX}]$.
En évaluant en $t = 0$, on trouve $\phi'_X(0) = i \mathbb{E}[X]$.

### Démonstration de la fonction caractéristique de la loi Normale Standard

Soit $X \sim \mathcal{N}(0, 1)$. Par définition, sa densité est $f_X(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$.
$\phi_X(t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{+\infty} e^{itx} e^{-x^2/2} dx$
Cette intégrale pose un défi : on intègre sur l'axe réel une fonction complexe.
L'exposant global est : $itx - \frac{x^2}{2} = - \frac{1}{2} \left( x^2 - 2itx \right)$.
On force l'apparition d'un carré parfait :
$x^2 - 2itx = x^2 - 2itx + (it)^2 - (it)^2 = (x-it)^2 - (-t^2) = (x-it)^2 + t^2$
En réinjectant dans l'exponentielle :
$\exp\left( -\frac{1}{2}(x^2 - 2itx) \right) = \exp\left( -\frac{1}{2}( (x-it)^2 + t^2 ) \right) = e^{-t^2/2} e^{-(x-it)^2/2}$
On sort le terme constant de l'intégrale (par rapport à $x$) :
$\phi_X(t) = e^{-t^2/2} \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{+\infty} e^{-(x-it)^2/2} dx$
La fonction $z \mapsto e^{-z^2/2}$ est entière sur $\mathbb{C}$. L'intégration sur la droite complexe $\{x - it \mid x \in \mathbb{R}\}$ parallèle à l'axe réel peut être reliée à l'intégrale sur l'axe réel standard par le théorème intégral de Cauchy. L'intégrale sur l'axe translaté coïncide donc parfaitement avec l'intégrale gaussienne classique sur $\mathbb{R}$ :
$\int_{-\infty}^{+\infty} e^{-(x-it)^2/2} dx = \int_{-\infty}^{+\infty} e^{-u^2/2} du = \sqrt{2\pi}$
En substituant dans notre expression initiale :
$\phi_X(t) = e^{-t^2/2} \frac{1}{\sqrt{2\pi}} \sqrt{2\pi} = e^{-t^2/2}$
La loi normale $\mathcal{N}(0, 1)$ est ainsi "autoduale" (invariante par sa propre transformée de Fourier).

## 4. Applications en Physique, Logique & Intelligence Artificielle

L'importance théorique et pratique des fonctions caractéristiques s'étend bien au-delà de la théorie des probabilités pure.

Dans l'architecture de l'Intelligence Artificielle et de l'optimisation stochastique :
La régularisation des réseaux de neurones profonds repose fondamentalement sur la compréhension des gradients. L'algorithme de descente de gradient stochastique (SGD) peut être modélisé comme une marche aléatoire. La stabilité d'apprentissage est conditionnée par les "queues" de la distribution des gradients. Les fonctions caractéristiques permettent d'analyser de manière élégante si une somme de gradients indépendants converge vers une distribution gaussienne (Théorème Central Limite) ou vers des distributions aux queues lourdes (Levy $\alpha$-stable distributions), ce qui influence drastiquement les stratégies de *gradient clipping* ou l'utilisation d'optimiseurs adaptatifs comme Adam.

En Théorie du Signal et Analyse des Données (Kernel Methods) :
La comparaison de deux distributions (par exemple lors de l'entraînement de Generative Adversarial Networks, GANs, avec des métriques comme le Maximum Mean Discrepancy, MMD) peut être conceptualisée en projetant les distributions dans un Espace de Hilbert à Noyau Reproduisant (RKHS). Mathématiquement, le théorème de Bochner relie les noyaux définis positifs, qui fondent les machines à vecteurs de support (SVM), aux transformées de Fourier de mesures finies, c'est-à-dire précisément aux fonctions caractéristiques. Ainsi, maximiser la distance entre deux distributions dans un RKHS stationnaire équivaut intimement à maximiser l'écart pondéré de leurs fonctions caractéristiques respectives.
