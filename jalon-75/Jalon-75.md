---
uuid: "jalon-75"
title: "Complétude des espaces Lp (Riesz-Fischer)"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/convergence
prev: "[[Jalon 74 (Inégalités fondamentales de l'analyse fonctionnelle).md]]"
next: "[[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L2).md]]"
---

# Jalon 75 : Complétude des espaces $L^p$ (Théorème de Riesz-Fischer)

## 1. Genèse et Motivation

La théorie de l'intégration de Riemann, bien qu'intuitive, souffre d'un défaut structurel majeur : l'espace des fonctions intégrables au sens de Riemann n'est pas complet pour la métrique induite par l'intégrale. Concrètement, une suite de fonctions régulières dont les graphes convergent raisonnablement peut admettre pour limite une fonction qui échappe totalement à l'intégration de Riemann (telle que la fonction de Dirichlet).

La théorie de Lebesgue, fondée sur la théorie de la mesure, vient combler cette lacune. Le théorème de Riesz-Fischer, établi indépendamment par Frigyes Riesz et Ernst Sigismund Fischer en 1907, garantit que les espaces $L^p$ sont des espaces de Banach (espaces vectoriels normés complets). Ce résultat fondamental permet d'importer toute la puissance de la géométrie et de l'analyse fonctionnelle dans l'étude des espaces de fonctions, rendant possible des opérations telles que la projection orthogonale dans $L^2$.

## 2. Définitions, Théorèmes et Exemples

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### A. Définition des espaces $L^p$
Pour $1 \le p < \infty$, l'espace $L^p(X, \mu)$ est l'ensemble des classes d'équivalence de fonctions mesurables $f : X \to \mathbb{C}$ (ou $\mathbb{R}$) telles que :
$$ \int_X |f|^p \, d\mu < \infty $$
muni de la norme $\|f\|_p = \left( \int_X |f|^p \, d\mu \right)^{1/p}$. L'identification de fonctions égales presque partout (p.p.) est cruciale pour que $\|f\|_p = 0 \implies f = 0$ et obtenir ainsi une vraie norme.

### B. Le Théorème de Riesz-Fischer
> **Théorème de Riesz-Fischer :**
> Pour tout $p \in [1, +\infty]$, l'espace vectoriel normé $(L^p(\mu), \|\cdot\|_p)$ est complet. C'est donc un **espace de Banach**. De plus, si $(f_n)$ est une suite convergeant vers $f$ dans $L^p$, alors il existe une sous-suite $(f_{\phi(n)})$ qui converge vers $f$ presque partout.

**Exemples Concrets :**
1. **Convergence dans $L^1$ sans convergence presque partout :** Considérons la suite des indicatrices des intervalles ("bosses glissantes") sur $[0,1]$:
   $f_1 = \mathbf{1}_{[0,1]}$, $f_2 = \mathbf{1}_{[0,1/2]}$, $f_3 = \mathbf{1}_{[1/2,1]}$, $f_4 = \mathbf{1}_{[0,1/3]}$, $\dots$
   La suite de leurs normes $\|f_n\|_1$ tend vers $0$, donc $f_n \to 0$ dans $L^1$. Cependant, pour tout $x \in [0,1]$, la suite $(f_n(x))$ oscille entre 0 et 1 une infinité de fois, ne convergeant donc en aucun point. Toutefois, la sous-suite $f_1, f_2, f_4, f_7, \dots$ qui donne les indicatrices du début des segments (de longueurs $1, 1/2, 1/3, \dots$) ne suffit pas; il faut prendre une sous-suite dont la largeur décroît très vite (ex: $\mathbf{1}_{[0, 1/2^k]}$) pour obtenir une convergence p.p. vers $0$ (sauf en $0$).

2. **Complétude sur $\mathbb{N}$ (espaces $\ell^p$) :** Si $X = \mathbb{N}$ muni de la mesure de comptage, alors $L^p$ devient l'espace de suites $\ell^p$. La complétude de $\ell^p$ signifie que si une suite de suites $(u^{(n)})_{n \ge 0}$ est de Cauchy dans $\ell^p$, elle converge terme à terme vers une suite $u \in \ell^p$, et l'erreur $\|u^{(n)} - u\|_p \to 0$.

3. **Complétude de $L^2$ (L'espace de Hilbert) :** Pour $p=2$, $L^2$ est muni du produit scalaire $\langle f, g \rangle = \int f \bar{g}$. La complétude de cet espace (espace de Hilbert) est l'essence même de l'analyse de Fourier (convergence en moyenne quadratique des séries de Fourier) et de la mécanique quantique (espace des états).

4. **Série absolument convergente dans $L^1$ :** Soit $f_n(x) = \frac{\sin(n x)}{n^2}$ sur $[0, \pi]$.
   $\|f_n\|_1 = \int_0^\pi \left|\frac{\sin(nx)}{n^2}\right| \, dx \le \frac{\pi}{n^2}$.
   Puisque $\sum \frac{\pi}{n^2} < \infty$, la série $\sum f_n$ converge absolument dans $L^1$. Le théorème garantit que la somme $F(x) = \sum_{n=1}^\infty \frac{\sin(nx)}{n^2}$ définit bien une fonction de $L^1([0, \pi])$.

5. **Lien $L^p$ et $L^q$ sur espace de mesure finie :** Sur un espace mesurable compact comme $[0, 1]$ muni de la mesure de Lebesgue, si une suite converge dans $L^2$, elle converge aussi dans $L^1$ car $\|f\|_1 \le \|f\|_2 \sqrt{\mu([0,1])}$ (par Cauchy-Schwarz). La limite est la même.

**Figures TikZ (Géométrie des convergences) :**

```latex
\begin{center}
\begin{tikzpicture}[scale=1.5]
  % Axe X
  \draw[->] (-0.5, 0) -- (4, 0) node[right] {$x$};
  % Axe Y
  \draw[->] (0, -0.5) -- (0, 2) node[above] {$f(x)$};

  % Courbes de Cauchy s'écrasant
  \draw[domain=0.5:3.5, smooth, variable=\x, blue, thick] plot ({\x}, {1/(\x) + 0.5*sin(500*\x)/(10*\x)});
  \draw[domain=0.5:3.5, smooth, variable=\x, blue, thick, opacity=0.6] plot ({\x}, {1/(\x) + 0.3*sin(800*\x)/(10*\x)});
  \draw[domain=0.5:3.5, smooth, variable=\x, blue, thick, opacity=0.3] plot ({\x}, {1/(\x) + 0.1*sin(1200*\x)/(10*\x)});

  % Fonction limite
  \draw[domain=0.5:3.5, smooth, variable=\x, red, very thick] plot ({\x}, {1/(\x)}) node[right] {$f \in L^p$};

  \node at (2, 1.5) [blue] {Suite de Cauchy $(f_n)$};
\end{tikzpicture}
\end{center}
```
*L'espace étant complet, la suite de fonctions "se stabilise" vers une fonction mesurable de limite bien définie, appartenant à la même classe $L^p$.*

```latex
\begin{center}
\begin{tikzpicture}[scale=1]
  \draw[thick, ->] (0,0) -- (6,0) node[right] {$x$};
  \draw[thick, ->] (0,0) -- (0,2);

  \fill[blue!30] (1,0) rectangle (2,1);
  \draw[thick, blue] (1,0) -- (1,1) -- (2,1) -- (2,0);
  \node[blue] at (1.5, 1.2) {$f_n(x)$};

  \fill[red!30] (3,0) rectangle (3.5,1);
  \draw[thick, red] (3,0) -- (3,1) -- (3.5,1) -- (3.5,0);
  \node[red] at (3.25, 1.2) {$f_{n+1}(x)$};

  \node[align=center] at (3, -1) {Phénomène de bosse glissante: \\ $\|f_n\|_p \to 0$ mais aucune convergence p.p. sans extraire une sous-suite};
\end{tikzpicture}
\end{center}
```

## 3. Démonstrations

La preuve du théorème de Riesz-Fischer repose sur le critère de complétude des espaces vectoriels normés : un EVN est de Banach si et seulement si toute série absolument convergente est convergente.

**Étape 1 : Hypothèse d'absolue convergence.**
Soit $(f_n)$ une suite d'éléments de $L^p$ (pour $1 \le p < \infty$) telle que la série de terme général $\|f_n\|_p$ est convergente, i.e.,
$$ \sum_{n=1}^\infty \|f_n\|_p = M < +\infty $$
Il faut montrer que la série $\sum f_n$ converge dans $L^p$. On suppose sans perte de généralité que les fonctions $f_n$ sont à valeurs dans $\mathbb{R}$. Posons pour tout entier $k \ge 1$ :
$$ g_k(x) = \sum_{n=1}^k |f_n(x)| \quad \text{et} \quad g(x) = \sum_{n=1}^\infty |f_n(x)| \in [0, +\infty] $$

**Étape 2 : Application du Théorème de Convergence Monotone.**
La suite $(g_k)$ est une suite de fonctions mesurables, positives et croissante vers $g$.
D'après l'inégalité de Minkowski, pour tout $k \ge 1$,
$$ \|g_k\|_p \le \sum_{n=1}^k \|f_n\|_p \le M $$
Ce qui implique que $\int_X (g_k)^p \, d\mu \le M^p$.
Par le théorème de convergence monotone (Beppo-Levi), puisque $(g_k)^p$ croît vers $g^p$, on obtient :
$$ \int_X g^p \, d\mu = \lim_{k \to \infty} \int_X (g_k)^p \, d\mu \le M^p < +\infty $$

**Étape 3 : Convergence presque partout.**
Puisque l'intégrale de $g^p$ est finie, la fonction $g$ est finie presque partout sur $X$.
Cela signifie que pour presque tout $x \in X$, la série $\sum |f_n(x)|$ converge. Ainsi, la série réelle $\sum f_n(x)$ est absolument convergente donc convergente presque partout.
Notons $S(x) = \sum_{n=1}^\infty f_n(x)$ là où la série converge, et $S(x) = 0$ ailleurs.
On a bien $|S(x)| \le g(x)$ presque partout, d'où $S \in L^p(\mu)$.

**Étape 4 : Application du Théorème de Convergence Dominée (Convergence dans $L^p$).**
Soit $S_k(x) = \sum_{n=1}^k f_n(x)$ la somme partielle.
On a $S_k \to S$ presque partout, et
$$ |S_k(x) - S(x)|^p \le (|S_k(x)| + |S(x)|)^p \le (2g(x))^p $$
La fonction $(2g)^p = 2^p g^p$ est intégrable.
Par conséquent, on peut appliquer le théorème de convergence dominée de Lebesgue :
$$ \lim_{k \to \infty} \int_X |S_k - S|^p \, d\mu = 0 $$
Ainsi, la somme partielle $S_k$ converge vers $S$ dans $L^p(\mu)$.

**Étape 5 : Extraction de sous-suite pour une suite de Cauchy.**
Si $(h_m)$ est une suite de Cauchy dans $L^p$, on peut en extraire une sous-suite $(h_{\phi(n)})$ telle que $\|h_{\phi(n+1)} - h_{\phi(n)}\|_p \le 2^{-n}$. En posant $f_n = h_{\phi(n+1)} - h_{\phi(n)}$, la série $\sum f_n$ converge absolument dans $L^p$, donc elle converge vers une fonction $S$ dans $L^p$ et presque partout (d'après les étapes précédentes). Or, $h_{\phi(n)} = h_{\phi(1)} + \sum_{k=1}^{n-1} f_k$, donc la sous-suite $(h_{\phi(n)})$ converge presque partout et dans $L^p$ vers une limite $h$. Enfin, comme la suite $(h_m)$ entière est de Cauchy, elle converge tout entière vers $h$ dans $L^p$. \qed

## 4. Applications en Physique, Logique et Intelligence Artificielle

**Physique (Mécanique Quantique) :**
L'espace de Hilbert $L^2$ est le cadre naturel de la mécanique quantique. Une particule est décrite par une fonction d'onde $\psi \in L^2(\mathbb{R}^3)$ telle que $\|\psi\|_2 = 1$. L'évolution temporelle de $\psi$ selon l'équation de Schrödinger exige que la fonction reste dans cet espace de carré sommable. La complétude assure que les limites de suites d'états physiquement acceptables restent des états acceptables (pas d'échappement vers l'infini avec perte d'énergie), garantissant la conservation de la probabilité à tout instant.

**Analyse de Fourier et Traitement du Signal :**
Le théorème de Riesz-Fischer implique (via Riesz-Representation) qu'un signal d'énergie finie (dans $L^2$) peut être représenté parfaitement et réversiblement par sa série ou transformée de Fourier, dont les composantes forment une base de Hilbert complète. Cela permet la compression (JPEG, MP3) et le filtrage (suppression des hautes fréquences) par projection sur des sous-espaces de $L^2$, avec la certitude que la reconstruction ne produira pas de "trous" fonctionnels (propriété de complétude).

**Intelligence Artificielle (Fonctionnelles de coût et RKHS) :**
Lors de l'apprentissage par descente de gradient dans des espaces infinis (par exemple l'apprentissage de processus gaussiens ou la résolution d'EDP par PINNs - Physics-Informed Neural Networks), les réseaux de neurones approchent une fonction de transfert. La fonction de perte empirique agit comme une norme empirique $L^p$ (souvent $L^2$ pour l'erreur quadratique moyenne MSE, ou $L^1$ pour la robustesse aux outliers). La complétude de $L^2$ (et des espaces de Sobolev associés) garantit mathématiquement que, sous des conditions appropriées, l'algorithme d'optimisation converge bien vers un minimum de la fonctionnelle de risque au sein même de la classe de fonctions étudiée, justifiant rigoureusement le théorème d'approximation universelle des réseaux profonds (Universal Approximation Theorem).
