---
uuid: "jalon-78"
title: "Séries de Fourier"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/traitement-du-signal
prev: "[[Jalon 77 (Densité des fonctions simples).md]]"
next: "[[Jalon 79 (Convergence en moyenne quadratique des séries de Fourier et identité de Parseval.).md]]"
---

# Séries de Fourier

## Introduction historique et physique

Joseph Fourier, dans son étude sur la propagation de la chaleur (1822), a conjecturé que toute fonction périodique pouvait être décomposée en une somme (éventuellement infinie) de fonctions sinus et cosinus. Cette idée révolutionnaire, initialement mal accueillie par Lagrange et Laplace pour son manque de rigueur apparent, est devenue le fondement de l'analyse harmonique harmonique moderne.

Physiquement, cela correspond à analyser un signal complexe (comme le son d'un violon) en ses "harmoniques" pures (les ondes sinusoïdales élémentaires).

## Espaces de fonctions et coefficients de Fourier

Soit $T > 0$. On note $\omega = \frac{2\pi}{T}$ la pulsation fondamentale. Considérons les fonctions $T$-périodiques, à valeurs complexes, de carré intégrable sur une période, c'est-à-dire appartenant à l'espace de Hilbert $L^2_{per}([0, T])$.

Le produit scalaire naturel sur cet espace est donné par :
$$ \langle f, g \rangle = \frac{1}{T} \int_0^T \overline{f(t)}g(t) dt $$

**Théorème et Définition (Famille orthonormée fondamentale) :**
La famille de fonctions $(e_n)_{n \in \mathbb{Z}}$ définie par $e_n(t) = e^{in\omega t}$ forme une famille orthonormée pour ce produit scalaire.

*Preuve :*
Pour $n = m$, $\langle e_n, e_n \rangle = \frac{1}{T} \int_0^T e^{-in\omega t}e^{in\omega t} dt = \frac{1}{T} \int_0^T 1 dt = 1$.
Pour $n \neq m$, $\langle e_n, e_m \rangle = \frac{1}{T} \int_0^T e^{-in\omega t}e^{im\omega t} dt = \frac{1}{T} \int_0^T e^{i(m-n)\omega t} dt = \frac{1}{T} \left[ \frac{e^{i(m-n)\omega t}}{i(m-n)\omega} \right]_0^T$.
Puisque $\omega T = 2\pi$ et $e^{i2k\pi} = 1$ pour $k \in \mathbb{Z}$, le crochet s'annule.

**Définition (Coefficients de Fourier) :**
Pour toute fonction $f \in L^1_{per}([0, T])$, on définit son $n$-ième coefficient de Fourier exponentiel par :
$$ c_n(f) = \frac{1}{T} \int_0^T f(t) e^{-in\omega t} dt $$
Si $f$ est à valeurs réelles, on utilise souvent les coefficients réels :
$$ a_n(f) = \frac{2}{T} \int_0^T f(t) \cos(n\omega t) dt \quad \text{pour } n \ge 0 $$
$$ b_n(f) = \frac{2}{T} \int_0^T f(t) \sin(n\omega t) dt \quad \text{pour } n \ge 1 $$
Avec la relation : $c_n = \frac{a_n - i b_n}{2}$ pour $n > 0$ et $c_{-n} = \frac{a_n + i b_n}{2}$. $c_0 = \frac{a_0}{2}$.

### Exemples fondamentaux de calcul

**Exemple 1 : Le signal carré (Onde carrée impaire)**
Soit $f$ la fonction $2\pi$-périodique définie sur $]-\pi, \pi]$ par $f(t) = -1$ si $t \in ]-\pi, 0[$ et $f(t) = 1$ si $t \in ]0, \pi[$.
Ici $T = 2\pi$, $\omega = 1$. La fonction est impaire, donc tous les $a_n$ sont nuls.
Calculons les $b_n$ pour $n \ge 1$ :
$$ b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(t) \sin(nt) dt = \frac{2}{\pi} \int_0^{\pi} 1 \cdot \sin(nt) dt = \frac{2}{\pi} \left[ -\frac{\cos(nt)}{n} \right]_0^{\pi} = \frac{2}{n\pi} (1 - (-1)^n) $$
Si $n$ est pair ($n=2k$), $b_{2k} = 0$.
Si $n$ est impair ($n=2k+1$), $b_{2k+1} = \frac{4}{(2k+1)\pi}$.
La série de Fourier associée est donc :
$$ S(f)(t) = \frac{4}{\pi} \sum_{k=0}^{+\infty} \frac{\sin((2k+1)t)}{2k+1} $$

**Exemple 2 : Le signal dent de scie**
Soit $f(t) = t$ sur $]-\pi, \pi]$, prolongée par $2\pi$-périodicité.
Fonction impaire, $a_n = 0$.
$$ b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} t \sin(nt) dt = \frac{2}{\pi} \int_0^{\pi} t \sin(nt) dt $$
Par intégration par parties :
$$ \int_0^{\pi} t \sin(nt) dt = \left[ -t\frac{\cos(nt)}{n} \right]_0^{\pi} - \int_0^{\pi} -\frac{\cos(nt)}{n} dt = -\pi\frac{(-1)^n}{n} + 0 $$
Donc $b_n = \frac{2}{\pi} \left( -\pi\frac{(-1)^n}{n} \right) = 2 \frac{(-1)^{n+1}}{n}$.
$$ S(f)(t) = 2 \sum_{n=1}^{+\infty} \frac{(-1)^{n+1}}{n} \sin(nt) $$

**Exemple 3 : Fonction valeur absolue (Signal triangle continu)**
Soit $f(t) = |t|$ sur $]-\pi, \pi]$, prolongée par $2\pi$-périodicité.
Fonction paire, $b_n = 0$.
$a_0 = \frac{2}{\pi} \int_0^{\pi} t dt = \frac{2}{\pi} [\frac{t^2}{2}]_0^{\pi} = \pi$.
Pour $n \ge 1$ :
$$ a_n = \frac{2}{\pi} \int_0^{\pi} t \cos(nt) dt = \frac{2}{\pi} \left( \left[ t\frac{\sin(nt)}{n} \right]_0^{\pi} - \int_0^{\pi} \frac{\sin(nt)}{n} dt \right) $$
$$ a_n = \frac{2}{\pi} \left( 0 - \left[ -\frac{\cos(nt)}{n^2} \right]_0^{\pi} \right) = \frac{2}{n^2\pi}(\cos(n\pi) - 1) = \frac{2}{n^2\pi}((-1)^n - 1) $$
Si $n=2k$, $a_{2k} = 0$. Si $n=2k+1$, $a_{2k+1} = -\frac{4}{\pi(2k+1)^2}$.
$$ S(f)(t) = \frac{\pi}{2} - \frac{4}{\pi} \sum_{k=0}^{+\infty} \frac{\cos((2k+1)t)}{(2k+1)^2} $$

**Exemple 4 : La fonction $f(t) = t^2$ sur $]-\pi, \pi]$**
C'est une fonction paire, $b_n = 0$.
$a_0 = \frac{2}{\pi} \int_0^{\pi} t^2 dt = \frac{2\pi^2}{3}$.
Pour $n \ge 1$, double intégration par parties :
$$ a_n = \frac{2}{\pi} \int_0^{\pi} t^2 \cos(nt) dt = \frac{4(-1)^n}{n^2} $$
Série : $S(f)(t) = \frac{\pi^2}{3} + 4 \sum_{n=1}^{+\infty} \frac{(-1)^n}{n^2} \cos(nt)$.
En évaluant en $t=\pi$, on trouve $\pi^2 = \frac{\pi^2}{3} + 4 \sum \frac{1}{n^2}$, d'où on déduit $\sum \frac{1}{n^2} = \frac{\pi^2}{6}$ (Problème de Bâle).

**Exemple 5 : Signal impulsion de Dirac régularisée**
Considérons pour $0 < \alpha < \pi$ un créneau centré en $0$ de largeur $2\alpha$ et hauteur $\frac{1}{2\alpha}$.
$f(t) = \frac{1}{2\alpha}$ pour $t \in [-\alpha, \alpha]$, $0$ ailleurs sur $]-\pi, \pi]$.
$f$ est paire, $b_n = 0$.
$a_0 = \frac{2}{\pi} \int_0^{\alpha} \frac{1}{2\alpha} dt = \frac{1}{\pi}$.
Pour $n \ge 1$ : $a_n = \frac{2}{\pi} \int_0^{\alpha} \frac{1}{2\alpha} \cos(nt) dt = \frac{2}{\pi \cdot 2\alpha} [\frac{\sin(nt)}{n}]_0^{\alpha} = \frac{\sin(n\alpha)}{n\alpha \pi}$.
Remarquons que lorsque $\alpha \to 0$, $a_n \to \frac{1}{\pi}$ (les coefficients de Fourier du peigne de Dirac sont constants).

## Théorèmes de convergence ponctuelle

La grande question est : la série de Fourier $S(f)(t) = \sum_{n \in \mathbb{Z}} c_n(f) e^{in\omega t}$ converge-t-elle vers $f(t)$ ?

**Définition (Noyau de Dirichlet) :**
La somme partielle d'ordre $N$ s'écrit :
$$ S_N(f)(t) = \sum_{n=-N}^N c_n(f) e^{in\omega t} = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) D_N(t-x) dx = (f * D_N)(t) $$
avec $D_N(u) = \sum_{n=-N}^N e^{inu} = \frac{\sin((N+1/2)u)}{\sin(u/2)}$.
(Preuve : somme d'une suite géométrique de raison $e^{iu}$).

**Théorème de Dirichlet :**
Si $f$ est $2\pi$-périodique, continue par morceaux, et possède en tout point une dérivée à droite et une dérivée à gauche, alors la série de Fourier de $f$ converge ponctuellement en tout point $t \in \mathbb{R}$ vers la moyenne de ses limites à gauche et à droite :
$$ \lim_{N \to +\infty} S_N(f)(t) = \frac{f(t^+) + f(t^-)}{2} $$
En particulier, si $f$ est continue en $t$, la série converge vers $f(t)$.

*Preuve (Esquisse pour un point $t$ où $f$ est dérivable et $f(t)=0$) :*
On veut montrer $\int_{-\pi}^{\pi} f(t-x) D_N(x) dx \to 0$.
Puisque $f$ est dérivable en $t$, la fonction $g(x) = \frac{f(t-x)}{\sin(x/2)}$ est continue et bornée près de $x=0$.
L'intégrale devient $\int_{-\pi}^{\pi} g(x) \sin((N+1/2)x) dx$.
Par le Lemme de Riemann-Lebesgue, le coefficient de Fourier d'une fonction intégrable tend vers 0 à l'infini, donc cette intégrale tend vers 0.

## Propriétés analytiques des coefficients de Fourier

**Lemme de Riemann-Lebesgue :**
Si $f \in L^1_{per}$, alors $\lim_{|n| \to +\infty} c_n(f) = 0$.

**Lien avec la régularité :**
Plus une fonction est régulière (dérivable un grand nombre de fois), plus ses coefficients de Fourier décroissent vite.
Si $f$ est de classe $C^k$, alors $c_n(f^{(k)}) = (in)^k c_n(f)$.
Puisque $c_n(f^{(k)}) \to 0$, on a $c_n(f) = o(\frac{1}{|n|^k})$.
À l'inverse, une décroissance rapide des coefficients garantit la régularité de la fonction (convergence normale des séries dérivées).

**Théorème (Convergence normale) :**
Si $f$ est $2\pi$-périodique, continue, et de classe $C^1$ par morceaux, alors sa série de Fourier converge normalement (donc uniformément) vers $f$ sur $\mathbb{R}$.

## Phénomène de Gibbs

Aux points de discontinuité d'une fonction (comme pour le signal carré), la somme partielle $S_N(f)$ présente des "dépassements" par rapport à la valeur limite, appelés phénomène de Gibbs. Même lorsque $N \to +\infty$, l'amplitude maximale de cet "overshoot" ne tend pas vers 0, mais vers une constante d'environ $9\%$ du saut de la fonction. Cela montre que la convergence n'est pas uniforme près d'une discontinuité.
