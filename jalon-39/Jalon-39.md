---
uuid: "jalon-39"
title: "Intégrales généralisées sur un intervalle quelconque"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/probabilites
prev: "[[Jalon 38 (Théorème fondamental de l'analyse).md]]"
next: "[[Jalon 40 (Intégrales dépendant d'un paramètre).md]]"
---

# Jalon 39 : Intégrales généralisées sur un intervalle quelconque

## 1. Genèse et Motivation (L'Échafaudage Cognitif)

L'intégrale de Riemann, telle qu'introduite par Bernhard Riemann au milieu du XIXe siècle, constituait une avancée majeure dans la formalisation de l'analyse réelle. Cependant, sa définition stricte reposait sur deux piliers inébranlables : le domaine d'intégration devait être un segment fermé et borné $[a, b]$, et la fonction intégrée se devait d'être bornée sur ce segment.

Historiquement, cette rigidité est rapidement devenue un obstacle. Les physiciens et les probabilistes se heurtaient sans cesse à des problèmes où l'espace ne se limitait pas à une boîte finie. Comment calculer le travail d'une force s'exerçant d'un point jusqu'à l'infini stellaire ? Comment évaluer l'aire sous la courbe en cloche de la loi normale, qui s'étend sur tout l'axe réel $\mathbb{R}$ ? De plus, en électromagnétisme, le potentiel créé par une charge ponctuelle en son centre divergeait vers l'infini (une asymptote verticale en zéro, comme la fonction $1/x$).

La communauté mathématique, notamment Augustin-Louis Cauchy, a dû étendre le concept d'intégrale pour franchir ces singularités et embrasser l'infini. Plutôt que de redéfinir l'intégrale de zéro, l'idée lumineuse fut d'utiliser un outil naissant mais puissant : la limite. On intègre d'abord sur un domaine fini et bien sage, disons $[a, X]$, où les règles de Riemann s'appliquent. Puis, on fait tendre $X$ vers l'infini, ou vers le point singulier. Si la limite de cette aire dynamique se stabilise vers une valeur finie, on déclare l'intégrale convergente. Ce passage à la limite permet de quantifier avec une rigueur absolue ce qui, géométriquement, s'apparente à une "peinture infinie qui s'affine tellement vite qu'un seul pot suffit".

Voici une illustration géométrique du phénomène de convergence vers une asymptote infinie :

```latex
\begin{tikzpicture}[scale=1.5]
\draw[->] (-0.5,0) -- (5,0) node[right] {$x$};
\draw[->] (0,-0.5) -- (0,3) node[above] {$y$};
\draw[domain=1:4.5, smooth, variable=\x, blue, thick] plot ({\x}, {2/(\x*\x)});
\fill[blue, opacity=0.2] (1,0) -- plot[domain=1:4, smooth] (\x, {2/(\x*\x)}) -- (4,0) -- cycle;
\draw[dashed] (1,0) -- (1,2) node[above right] {Début de l'intégration};
\draw[dashed] (4,0) -- (4,0.125) node[above right] {$X \to +\infty$};
\node at (2.5, 0.4) {$\int_1^X \frac{C}{t^\alpha} dt$};
\end{tikzpicture}
```

## 2. Formalisation et Algèbre des Intégrales Généralisées

### A. Énoncé Symbolique Strict

Soit $I$ un intervalle de la forme $[a, b[$, où $a \in \mathbb{R}$ et $b \in \mathbb{R} \cup \{+\infty\}$, avec $a < b$. Soit $f : [a, b[ \to \mathbb{K}$ (où $\mathbb{K} = \mathbb{R}$ ou $\mathbb{C}$) une application localement intégrable sur $[a, b[$.

L'intégrale généralisée $\int_a^b f(t) dt$ est définie par la limite :
$$ \int_a^b f(t) dt = \lim_{X \to b^-} \int_a^X f(t) dt $$
lorsque cette limite existe et est finie.

### B. Anatomie et Typage Chirurgical

- L'intervalle **$[a, b[$** : Le point $a$ est un réel fini où la fonction ne pose aucun problème. Le point $b$ est la "borne à problème". Il peut s'agir de l'infini ($b = +\infty$), ou d'un point fini $b$ où la fonction $f$ n'est pas définie ou n'est pas bornée (par exemple, une asymptote verticale).
- La condition de **locale intégrabilité** : $f$ doit être Riemann-intégrable sur tout sous-segment fermé $[a, X] \subset [a, b[$. Cela garantit que l'intégrale partielle $\int_a^X f(t) dt$ est toujours une quantité mathématiquement bien définie avant de passer à la limite.
- L'opérateur **$\lim_{X \to b^-}$** : Il s'agit de la limite usuelle d'une fonction d'une variable réelle $X$. Si $b = +\infty$, on étudie $\lim_{X \to +\infty}$.
- La valeur de l'intégrale : Si la limite est un scalaire $L \in \mathbb{K}$, on dit que l'intégrale **converge** et vaut $L$. Si la limite est infinie ou n'existe pas, on dit que l'intégrale **diverge**.

### C. Exemples de Validation

**Exemple Trivial (Convergence sur intervalle infini) :**
Considérons l'intégrale $\int_1^{+\infty} \frac{1}{t^2} dt$.
Pour tout $X > 1$, la fonction $t \mapsto 1/t^2$ est continue (donc Riemann-intégrable) sur $[1, X]$.
Calculons l'intégrale partielle :
$$ \int_1^X \frac{1}{t^2} dt = \left[ -\frac{1}{t} \right]_1^X = -\frac{1}{X} - (-1) = 1 - \frac{1}{X} $$
Passage à la limite :
$$ \lim_{X \to +\infty} \left( 1 - \frac{1}{X} \right) = 1 - 0 = 1 $$
La limite existe et est finie (valant 1). Donc l'intégrale converge et $\int_1^{+\infty} \frac{1}{t^2} dt = 1$.

**Exemple Complexe (Divergence oscillatoire) :**
Analysons $\int_0^{+\infty} \cos(t) dt$.
La fonction cosinus est continue sur $\mathbb{R}$, donc localement intégrable sur $[0, +\infty[$.
L'intégrale partielle est :
$$ \int_0^X \cos(t) dt = \left[ \sin(t) \right]_0^X = \sin(X) - \sin(0) = \sin(X) $$
Lorsque $X \to +\infty$, la fonction $X \mapsto \sin(X)$ oscille perpétuellement entre -1 et 1 sans jamais admettre de limite. L'intégrale généralisée diverge.

### D. Cas Pathologiques et Contre-exemples

**Le mirage de la valeur principale de Cauchy :**
Soit l'intégrale $\int_{-\infty}^{+\infty} t dt$. On pourrait être tenté de regrouper les termes de manière symétrique en intégrant sur $[-X, X]$.
$$ \lim_{X \to +\infty} \int_{-X}^X t dt = \lim_{X \to +\infty} \left[ \frac{t^2}{2} \right]_{-X}^X = \lim_{X \to +\infty} \left( \frac{X^2}{2} - \frac{(-X)^2}{2} \right) = 0 $$
Ce calcul est **faux** dans le cadre des intégrales généralisées de Riemann. Par définition stricte, une intégrale de $-\infty$ à $+\infty$ converge si et seulement si les deux intégrales $\int_0^{+\infty} t dt$ et $\int_{-\infty}^0 t dt$ convergent indépendamment.
Or, $\int_0^X t dt = X^2/2 \to +\infty$. L'intégrale sur $\mathbb{R}$ diverge donc, même si l'aire compensée semble nulle.

## 3. Démonstrations "Zéro Ellipse"

### Preuve 1 : Critères de Riemann sur $[1, +\infty[$

> **Théorème (Intégrales de Riemann) :** L'intégrale $\int_1^{+\infty} \frac{1}{t^\alpha} dt$ converge si et seulement si $\alpha > 1$.

**Démonstration pas-à-pas :**
Soit $f(t) = \frac{1}{t^\alpha}$ pour $t \ge 1$. La fonction $f$ est continue sur $[1, +\infty[$.
Soit un réel $X > 1$. Nous allons étudier l'intégrale partielle $I(X) = \int_1^X \frac{1}{t^\alpha} dt$ selon la valeur du paramètre $\alpha$.

**Cas 1 : $\alpha = 1$**
La fonction à intégrer est $1/t$. Sa primitive usuelle sur $]0, +\infty[$ est $\ln(t)$.
$$ I(X) = \int_1^X \frac{1}{t} dt = \left[ \ln(t) \right]_1^X = \ln(X) - \ln(1) = \ln(X) $$
Nous devons évaluer la limite lorsque $X \to +\infty$. Par les théorèmes de croissances comparées de base, la fonction logarithme népérien tend vers $+\infty$ en l'infini.
$$ \lim_{X \to +\infty} \ln(X) = +\infty $$
La limite n'est pas finie. Donc pour $\alpha = 1$, l'intégrale diverge.

**Cas 2 : $\alpha \neq 1$**
La fonction à intégrer s'écrit $t^{-\alpha}$. Puisque $-\alpha \neq -1$, sa primitive est $\frac{t^{-\alpha + 1}}{-\alpha + 1} = \frac{t^{1-\alpha}}{1-\alpha}$.
$$ I(X) = \int_1^X t^{-\alpha} dt = \left[ \frac{t^{1-\alpha}}{1-\alpha} \right]_1^X = \frac{X^{1-\alpha}}{1-\alpha} - \frac{1^{1-\alpha}}{1-\alpha} = \frac{X^{1-\alpha} - 1}{1-\alpha} $$
Nous devons maintenant examiner le comportement de $X^{1-\alpha}$ lorsque $X \to +\infty$. L'exposant $1-\alpha$ détermine le comportement asymptotique.

*Sous-cas 2a : $\alpha < 1$*
Si $\alpha < 1$, alors $1-\alpha > 0$. Posons $k = 1-\alpha > 0$.
L'expression devient $X^k$. Comme $k > 0$, la limite est infinie : $\lim_{X \to +\infty} X^k = +\infty$.
En divisant par $1-\alpha > 0$, on obtient une divergence vers $+\infty$. L'intégrale diverge.

*Sous-cas 2b : $\alpha > 1$*
Si $\alpha > 1$, alors $1-\alpha < 0$. Posons $k = \alpha - 1 > 0$, de sorte que $1-\alpha = -k$.
L'expression est $X^{-k} = \frac{1}{X^k}$. Comme $k > 0$, $\lim_{X \to +\infty} X^k = +\infty$, ce qui implique par inverse :
$$ \lim_{X \to +\infty} \frac{1}{X^k} = 0 $$
Revenons à $I(X)$ :
$$ \lim_{X \to +\infty} \frac{X^{1-\alpha} - 1}{1-\alpha} = \frac{0 - 1}{1-\alpha} = \frac{1}{\alpha - 1} $$
La limite existe et est une constante réelle finie. Donc l'intégrale converge.

**Conclusion :** La réunion exhaustive de tous les cas démontre rigoureusement que l'intégrale ne converge que sous la condition stricte $\alpha > 1$.

### Preuve 2 : Absolue convergence implique convergence

> **Théorème :** Si l'intégrale $\int_a^b |f(t)| dt$ converge, alors l'intégrale $\int_a^b f(t) dt$ converge également.

**Démonstration pas-à-pas :**
Considérons une fonction $f : [a, b[ \to \mathbb{R}$ localement intégrable, telle que $\int_a^b |f(t)| dt$ converge.
Nous allons utiliser le puissant **Critère de Cauchy** pour l'existence d'une limite.

Définissons la fonction $F(X) = \int_a^X f(t) dt$ pour $X \in [a, b[$. L'intégrale converge si et seulement si $F(X)$ admet une limite finie quand $X \to b$.
De même, définissons $G(X) = \int_a^X |f(t)| dt$. Par hypothèse de convergence absolue, $\lim_{X \to b} G(X) = L$ (finie).

Puisque $G(X)$ admet une limite finie en $b$, la fonction $G$ respecte le critère de Cauchy en $b$ :
$$ \forall \epsilon > 0, \exists B \in [a, b[, \quad \forall (x, y) \in [B, b[^2, \quad |G(y) - G(x)| \le \epsilon $$
Supposons, sans perte de généralité, que $x \le y$. Alors :
$$ |G(y) - G(x)| = \left| \int_a^y |f(t)| dt - \int_a^x |f(t)| dt \right| = \int_x^y |f(t)| dt $$
Ainsi, pour tout $\epsilon > 0$, il existe $B$ tel que pour $y \ge x \ge B$, on a $\int_x^y |f(t)| dt \le \epsilon$.

Maintenant, appliquons ce résultat à la fonction originelle $F(X)$. Nous voulons évaluer $|F(y) - F(x)|$ pour $y \ge x \ge B$.
$$ |F(y) - F(x)| = \left| \int_a^y f(t) dt - \int_a^x f(t) dt \right| = \left| \int_x^y f(t) dt \right| $$
Par l'inégalité triangulaire continue pour les intégrales de Riemann sur le segment $[x, y]$ :
$$ \left| \int_x^y f(t) dt \right| \le \int_x^y |f(t)| dt $$
En combinant les inégalités, nous obtenons que pour ce même seuil $B$ :
$$ |F(y) - F(x)| \le \int_x^y |f(t)| dt \le \epsilon $$
La fonction $F$ vérifie donc rigoureusement la définition de Cauchy au voisinage de $b$. L'espace $\mathbb{R}$ (et $\mathbb{C}$) étant complet, toute fonction satisfaisant le critère de Cauchy au voisinage d'un point admet une limite finie en ce point. Par conséquent, $\lim_{X \to b} F(X)$ existe, ce qui signifie que l'intégrale $\int_a^b f(t) dt$ converge.
