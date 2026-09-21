---
uuid: jalon-74
title: "Jalon 74 : Inégalités fondamentales de l'analyse fonctionnelle"
tags: [analyse, fonctionnelle, lebesgue, holder, minkowski, lp]
---

# 1. Introduction

À la fin du XIXe siècle et au début du XXe siècle, les mathématiciens cherchent à généraliser les notions de longueur et de distance à des espaces géométriques de plus en plus abstraits, notamment les espaces de fonctions. L'intégration de Lebesgue, nouvellement formulée, offre un cadre robuste. Cependant, pour mesurer la "taille" d'une fonction et comparer la proximité de deux fonctions, il faut des outils algébriques et analytiques fins.

C'est dans ce contexte que les mathématiciens Otto Hölder (en 1889) et Hermann Minkowski (en 1896) développent des inégalités fondamentales. L'inégalité de Hölder généralise l'inégalité de Cauchy-Schwarz et révèle une dualité profonde entre les exposants conjugués. L'inégalité de Minkowski, quant à elle, démontre que la "norme" $L^p$ vérifie l'inégalité triangulaire, dotant ainsi ces espaces de fonctions d'une véritable structure géométrique. Ces inégalités constituent la clé de voûte de l'analyse fonctionnelle moderne et de l'étude des espaces $L^p$.

# 2. Définitions et Inégalités Fondamentales

## Inégalité de Young

Avant d'énoncer le théorème de Hölder, il est crucial d'établir l'inégalité de Young, un lemme d'une puissance redoutable reposant sur la convexité.

Soit $p \in (1, \infty)$ et $q \in (1, \infty)$ tels que $\frac{1}{p} + \frac{1}{q} = 1$. On dit que $p$ et $q$ sont des **exposants conjugués**.

**Théorème (Inégalité de Young) :**
Pour tous nombres réels positifs $a, b \ge 0$, on a :
$$ a b \le \frac{a^p}{p} + \frac{b^q}{q} $$
L'égalité a lieu si et seulement si $a^p = b^q$.

**Exemple immédiat :**
Prenons $p=2, q=2$ (qui sont bien conjugués car $1/2 + 1/2 = 1$).
L'inégalité devient $a b \le \frac{a^2}{2} + \frac{b^2}{2}$, ce qui est équivalent à $(a-b)^2 \ge 0$.
Si $a = 3$ et $b = 4$, on a $3 \times 4 = 12 \le \frac{9}{2} + \frac{16}{2} = 12.5$.
Si $a = 4$ et $b = 4$, on a $4 \times 4 = 16 \le \frac{16}{2} + \frac{16}{2} = 16$.

## Inégalité de Hölder

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré.
Pour une fonction mesurable $f : X \to \mathbb{R}$ (ou $\mathbb{C}$), et $1 \le p < \infty$, on définit la norme $L^p$ par :
$$ \|f\|_p = \left( \int_X |f|^p \, d\mu \right)^{\frac{1}{p}} $$

**Théorème (Inégalité de Hölder) :**
Soient $p, q \in [1, \infty]$ des exposants conjugués (avec la convention $1/\infty = 0$).
Si $f \in L^p(X)$ et $g \in L^q(X)$, alors le produit $fg$ appartient à $L^1(X)$, et :
$$ \int_X |f g| \, d\mu \le \|f\|_p \|g\|_q $$

**Exemple immédiat :**
Soit $X = \{1, 2\}$, avec la mesure de comptage. $L^p$ correspond à $\mathbb{R}^2$.
Prenons $p=1, q=\infty$. $f = (x_1, x_2)$, $g = (y_1, y_2)$.
$\|f\|_1 = |x_1| + |x_2|$, $\|g\|_\infty = \max(|y_1|, |y_2|)$.
$|x_1 y_1 + x_2 y_2| \le |x_1| |y_1| + |x_2| |y_2| \le |x_1| \|g\|_\infty + |x_2| \|g\|_\infty = ( |x_1| + |x_2| ) \|g\|_\infty = \|f\|_1 \|g\|_\infty$.
Concrètement, $f=(2, -3)$ et $g=(4, 1)$. $|2\times 4 + (-3)\times 1| = 5$. $\|f\|_1 = 5$, $\|g\|_\infty = 4$. $5 \le 5 \times 4 = 20$.

**Cas limites :**
Si $\|f\|_p = 0$, $f = 0$ presque partout, donc $fg = 0$ pp et l'inégalité est triviale $0 \le 0$. L'égalité a lieu s'il existe des constantes non nulles $\alpha, \beta$ telles que $\alpha |f|^p = \beta |g|^q$ presque partout.

## Inégalité de Minkowski

**Théorème (Inégalité de Minkowski) :**
Soit $1 \le p \le \infty$. Si $f, g \in L^p(X)$, alors $f + g \in L^p(X)$ et on a :
$$ \|f + g\|_p \le \|f\|_p + \|g\|_p $$
Cela démontre que l'application $f \mapsto \|f\|_p$ vérifie l'inégalité triangulaire, ce qui est essentiel pour en faire une norme.

**Exemple immédiat :**
Encore dans $\mathbb{R}^2$ avec $p=2$ (norme euclidienne).
Soit $f = (3, 4)$ et $g = (5, 12)$.
$f+g = (8, 16)$. $\|f+g\|_2 = \sqrt{64 + 256} = \sqrt{320} \approx 17.88$.
$\|f\|_2 = \sqrt{9+16} = 5$. $\|g\|_2 = \sqrt{25+144} = 13$.
On a bien $17.88 \le 5 + 13 = 18$.

# 3. Démonstrations

## Démonstration de l'inégalité de Young

La fonction logarithme est strictement concave sur $(0, \infty)$.
Soit $a > 0$ et $b > 0$. Les réels $1/p$ et $1/q$ vérifient $\frac{1}{p} + \frac{1}{q} = 1$ avec $1/p, 1/q \in (0,1)$.
Par concavité de la fonction logarithme, pour tout $x, y > 0$,
$$ \ln( \alpha x + (1-\alpha) y ) \ge \alpha \ln(x) + (1-\alpha) \ln(y) $$
Appliquons ceci avec $x = a^p$, $y = b^q$, $\alpha = 1/p$ et $1-\alpha = 1/q$ :
$$ \ln\left( \frac{1}{p} a^p + \frac{1}{q} b^q \right) \ge \frac{1}{p} \ln(a^p) + \frac{1}{q} \ln(b^q) = \ln(a) + \ln(b) = \ln(ab) $$
En passant à l'exponentielle (qui est strictement croissante), on obtient :
$$ \frac{a^p}{p} + \frac{b^q}{q} \ge ab $$
Si $a=0$ ou $b=0$, l'inégalité est triviale.

## Démonstration de l'inégalité de Hölder

Si $\|f\|_p = 0$ ou $\|g\|_q = 0$, alors $f=0$ ou $g=0$ presque partout. Donc $fg = 0$ pp et l'intégrale est nulle, l'inégalité $0 \le 0$ est vérifiée.
Si $p=1, q=\infty$, on a $|f(x)g(x)| \le |f(x)| \|g\|_\infty$ presque partout. En intégrant, $\int |fg| d\mu \le \|g\|_\infty \int |f| d\mu = \|f\|_1 \|g\|_\infty$.
On suppose désormais $1 < p < \infty$ et $\|f\|_p, \|g\|_q \in (0, \infty)$.
Posons pour tout $x \in X$,
$$ a(x) = \frac{|f(x)|}{\|f\|_p} \quad \text{et} \quad b(x) = \frac{|g(x)|}{\|g\|_q} $$
D'après l'inégalité de Young, pour tout $x \in X$ :
$$ a(x)b(x) \le \frac{a(x)^p}{p} + \frac{b(x)^q}{q} $$
Ce qui s'écrit :
$$ \frac{|f(x)g(x)|}{\|f\|_p \|g\|_q} \le \frac{1}{p} \frac{|f(x)|^p}{\|f\|_p^p} + \frac{1}{q} \frac{|g(x)|^q}{\|g\|_q^q} $$
En intégrant cette inégalité sur $X$, on obtient :
$$ \frac{\int_X |f(x)g(x)| d\mu}{\|f\|_p \|g\|_q} \le \frac{1}{p \|f\|_p^p} \int_X |f(x)|^p d\mu + \frac{1}{q \|g\|_q^q} \int_X |g(x)|^q d\mu $$
Or, par définition, $\int_X |f(x)|^p d\mu = \|f\|_p^p$ et $\int_X |g(x)|^q d\mu = \|g\|_q^q$.
L'inégalité devient :
$$ \frac{\int_X |f(x)g(x)| d\mu}{\|f\|_p \|g\|_q} \le \frac{1}{p} \times 1 + \frac{1}{q} \times 1 = 1 $$
En multipliant par $\|f\|_p \|g\|_q$, on obtient l'inégalité de Hölder :
$$ \int_X |f g| d\mu \le \|f\|_p \|g\|_q $$

## Démonstration de l'inégalité de Minkowski

Pour $p=1$, par l'inégalité triangulaire classique sur les réels ou complexes, on a pour tout $x \in X$, $|f(x)+g(x)| \le |f(x)|+|g(x)|$. L'intégration de cette inégalité donne directement $\int_X |f+g| d\mu \le \int_X |f| d\mu + \int_X |g| d\mu$, ce qui prouve le résultat.
Pour $p=\infty$, par définition du supremum essentiel, $|f(x)| \le \|f\|_\infty$ et $|g(x)| \le \|g\|_\infty$ presque partout. Ainsi, $|f(x)+g(x)| \le \|f\|_\infty + \|g\|_\infty$ presque partout. Par passage au supremum essentiel, on obtient $\|f+g\|_\infty \le \|f\|_\infty + \|g\|_\infty$.
Supposons $1 < p < \infty$. On remarque d'abord que $f+g \in L^p(X)$ car $|f+g|^p \le (2\max(|f|,|g|))^p \le 2^p (|f|^p + |g|^p)$.
On écrit :
$$ |f+g|^p = |f+g| \cdot |f+g|^{p-1} \le (|f| + |g|) |f+g|^{p-1} = |f| |f+g|^{p-1} + |g| |f+g|^{p-1} $$
On intègre sur $X$ :
$$ \int_X |f+g|^p d\mu \le \int_X |f| |f+g|^{p-1} d\mu + \int_X |g| |f+g|^{p-1} d\mu $$
On applique l'inégalité de Hölder à chaque terme de la somme à droite. Soit $q$ l'exposant conjugué de $p$, tel que $(p-1)q = p$.
Pour le premier terme avec $f$ et $|f+g|^{p-1}$ :
$$ \int_X |f| |f+g|^{p-1} d\mu \le \|f\|_p \left( \int_X \left( |f+g|^{p-1} \right)^q d\mu \right)^{1/q} = \|f\|_p \left( \int_X |f+g|^p d\mu \right)^{1/q} = \|f\|_p \|f+g\|_p^{p/q} $$
De même pour le second terme :
$$ \int_X |g| |f+g|^{p-1} d\mu \le \|g\|_p \|f+g\|_p^{p/q} $$
En sommant :
$$ \|f+g\|_p^p = \int_X |f+g|^p d\mu \le \left( \|f\|_p + \|g\|_p \right) \|f+g\|_p^{p/q} $$
Si $\|f+g\|_p = 0$, l'inégalité de Minkowski est évidente. Si $\|f+g\|_p > 0$, on divise par $\|f+g\|_p^{p/q}$ :
$$ \|f+g\|_p^{p - p/q} \le \|f\|_p + \|g\|_p $$
Or $p - p/q = p(1 - 1/q) = p(1/p) = 1$. On conclut :
$$ \|f+g\|_p \le \|f\|_p + \|g\|_p $$

# 4. Applications en Physique, Logique & Intelligence Artificielle

Ces inégalités dépassent largement le cadre de l'analyse pure.

**En Physique Mathématique (Mécanique Quantique et Espaces de Fock) :**
La structure de Hilbert ($L^2$, obtenue pour $p=2$) est la base mathématique de la mécanique quantique (états purs). L'inégalité de Cauchy-Schwarz (Hölder pour $p=q=2$) donne le principe d'incertitude d'Heisenberg. Plus généralement, les espaces $L^p$ (souvent pour $1 \le p \le \infty$) interviennent dans l'étude des gaz de bosons/fermions, la thermodynamique statistique, et les équations aux dérivées partielles (comme l'équation de la chaleur où des normes $L^p$ décroissent au cours du temps).

**En Traitement du Signal (Analyse Harmonique) :**
L'inégalité de Hausdorff-Young, qui lie la norme $L^p$ d'une fonction à la norme $L^q$ de sa transformée de Fourier, repose fondamentalement sur ces résultats et des principes d'interpolation. Cela permet de borner l'énergie spectrale d'un signal à partir de ses caractéristiques temporelles.

**En Intelligence Artificielle (Deep Learning et Régularisation) :**
Les normes $L^p$ (surtout $L^1$ et $L^2$) sont omniprésentes en apprentissage automatique. L'inégalité de Minkowski garantit que ces pénalités forment des normes valides (ce qui est crucial pour la convexité de l'optimisation). L'inégalité de Hölder permet de majorer des erreurs complexes (comme dans l'analyse des Generative Adversarial Networks (GANs), via les distances de Wasserstein ou la dualité de Kantorovich-Rubinstein). La pénalité $L^1$ induit la sparsité des poids, tandis que $L^2$ réduit le sur-apprentissage (weight decay).
