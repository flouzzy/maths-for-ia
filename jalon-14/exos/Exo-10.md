---
uuid: "jalon-14-exo-10"
title: "Exercice 10 : Convergence Quadratique et Critère de Cauchy pour une Suite Complexe"
tags: ["math/analyse", "suites", "exercice"]
---
# Exercice 10 : Convergence Quadratique et Critère de Cauchy pour une Suite Complexe
## Énoncé
Soit la suite de nombres complexes $(z_n)_{n \in \mathbb{N}}$ définie par $z_0 \in \mathbb{C}$ et la relation de récurrence :
$$z_{n+1} = \frac{1}{2} z_n + \frac{1}{z_n^2+1}$$
On suppose que le terme initial $z_0$ est choisi tel que $|z_0 - 1| \le \frac{1}{2}$.

1.  Montrer que pour tout $n \in \mathbb{N}$, $z_n \neq -i$ et $z_n \neq i$.
2.  Démontrer que si $|z_n - 1| \le \frac{1}{2}$, alors $|z_{n+1} - 1| \le |z_n - 1|^2$. En déduire que pour tout $n \in \mathbb{N}$, $|z_n - 1| \le \left(\frac{1}{2}\right)^{2^n}$.
3.  Utiliser le critère de Cauchy pour prouver que la suite $(z_n)_{n \in \mathbb{N}}$ converge.
4.  Déterminer la limite de la suite $(z_n)_{n \in \mathbb{N}}$.

## Correction Détaillée
### Question 1 : Montrer que pour tout $n \in \mathbb{N}$, $z_n \neq -i$ et $z_n \neq i$.

Pour que la suite $(z_n)$ soit bien définie, il est impératif que le dénominateur $z_n^2+1$ ne s'annule jamais. Les valeurs de $z$ pour lesquelles $z^2+1=0$ sont $z=i$ et $z=-i$. Nous devons donc démontrer que $z_n \neq i$ et $z_n \neq -i$ pour tout $n \in \mathbb{N}$.

L'hypothèse initiale est que $|z_0 - 1| \le \frac{1}{2}$. Cela signifie que $z_0$ appartient au disque fermé de centre $1$ et de rayon $\frac{1}{2}$, noté $D(1, \frac{1}{2})$.

Calculons la distance du point $i$ au centre du disque $1$ :
$|i - 1| = \sqrt{(\text{Re}(i-1))^2 + (\text{Im}(i-1))^2} = \sqrt{(-1)^2 + (1)^2} = \sqrt{1+1} = \sqrt{2}$.
De même, pour le point $-i$ :
$|-i - 1| = \sqrt{(\text{Re}(-i-1))^2 + (\text{Im}(-i-1))^2} = \sqrt{(-1)^2 + (-1)^2} = \sqrt{1+1} = \sqrt{2}$.

Puisque $\sqrt{2} \approx 1.414$, et que le rayon du disque est $\frac{1}{2} = 0.5$, nous avons $\sqrt{2} > \frac{1}{2}$.
Cela implique que les points $i$ et $-i$ ne sont pas contenus dans le disque $D(1, \frac{1}{2})$. Par conséquent, $z_0 \neq i$ et $z_0 \neq -i$.

Pour les termes suivants de la suite, nous allons utiliser le résultat de la question 2 (que nous démontrerons rigoureusement par la suite). Ce résultat établit que si $|z_n - 1| \le \frac{1}{2}$, alors $|z_{n+1} - 1| \le |z_n - 1|^2$.
Par une application répétée de cette inégalité, en partant de $|z_0 - 1| \le \frac{1}{2}$, nous obtenons par récurrence que $|z_n - 1| \le \left(\frac{1}{2}\right)^{2^n}$ pour tout $n \in \mathbb{N}$.
Puisque $2^n \ge 1$ pour tout $n \in \mathbb{N}$, nous avons $\left(\frac{1}{2}\right)^{2^n} \le \frac{1}{2}$.
Cela signifie que pour tout $n \in \mathbb{N}$, $|z_n - 1| \le \frac{1}{2}$.
Ainsi, tous les termes $z_n$ de la suite restent confinés dans le disque $D(1, \frac{1}{2})$.
Comme nous l'avons montré, les points $i$ et $-i$ ne sont pas dans ce disque. Par conséquent, pour tout $n \in \mathbb{N}$, $z_n \neq i$ et $z_n \neq -i$.
La suite est donc bien définie pour tout $n \in \mathbb{N}$.

### Question 2 : Démontrer que si $|z_n - 1| \le \frac{1}{2}$, alors $|z_{n+1} - 1| \le |z_n - 1|^2$. En déduire que pour tout $n \in \mathbb{N}$, $|z_n - 1| \le \left(\frac{1}{2}\right)^{2^n}$.

Soit $z_n$ un terme de la suite tel que $|z_n - 1| \le \frac{1}{2}$. Nous souhaitons évaluer l'expression $z_{n+1} - 1$.
Nous partons de la relation de récurrence :
$$z_{n+1} = \frac{1}{2} z_n + \frac{1}{z_n^2+1}$$
Soustrayons $1$ des deux côtés :
$$z_{n+1} - 1 = \left(\frac{1}{2} z_n + \frac{1}{z_n^2+1}\right) - 1$$
Pour simplifier, mettons les termes sur un dénominateur commun $2(z_n^2+1)$ :
$$z_{n+1} - 1 = \frac{z_n(z_n^2+1) + 2 - 2(z_n^2+1)}{2(z_n^2+1)}$$
Développons le numérateur :
$$z_{n+1} - 1 = \frac{z_n^3 + z_n + 2 - 2z_n^2 - 2}{2(z_n^2+1)}$$
Regroupons les termes du numérateur :
$$z_{n+1} - 1 = \frac{z_n^3 - 2z_n^2 + z_n}{2(z_n^2+1)}$$
Nous pouvons factoriser le numérateur par $z_n$ :
$$z_{n+1} - 1 = \frac{z_n(z_n^2 - 2z_n + 1)}{2(z_n^2+1)}$$
Le terme entre parenthèses au numérateur est un carré parfait : $(z_n - 1)^2$.
Ainsi, nous obtenons l'expression fondamentale :
$$z_{n+1} - 1 = \frac{z_n(z_n - 1)^2}{2(z_n^2+1)}$$
Maintenant, prenons le module de cette expression. En utilisant la propriété $|AB/C| = |A||B|/|C|$ :
$$|z_{n+1} - 1| = \frac{|z_n| |z_n - 1|^2}{2|z_n^2+1|}$$
Nous devons maintenant trouver des bornes pour $|z_n|$ et $|z_n^2+1|$ en utilisant l'hypothèse $|z_n - 1| \le \frac{1}{2}$.
1.  **Borne supérieure pour $|z_n|$** :
    En utilisant l'inégalité triangulaire $|A+B| \le |A|+|B|$ :
    $|z_n| = |(z_n - 1) + 1| \le |z_n - 1| + |1|$.
    Puisque $|z_n - 1| \le \frac{1}{2}$, nous avons :
    $|z_n| \le \frac{1}{2} + 1 = \frac{3}{2}$.

2.  **Borne inférieure pour $|z_n^2+1|$** :
    Nous utilisons l'inégalité triangulaire inversée $|A+B| \ge ||A|-|B||$.
    $|z_n^2+1| = |(z_n-1+1)^2+1| = |(z_n-1)^2+2(z_n-1)+1+1| = |(z_n-1)^2+2(z_n-1)+2|$.
    Soit $h = z_n-1$. Par hypothèse, $|h| \le \frac{1}{2}$.
    Alors $|z_n^2+1| = |h^2+2h+2|$.
    Appliquons l'inégalité triangulaire inversée :
    $|h^2+2h+2| \ge |2 - |2h| - |h^2||$.
    Puisque $|h| \le \frac{1}{2}$, nous avons :
    $|2h| \le 2 \cdot \frac{1}{2} = 1$.
    $|h^2| = |h|^2 \le \left(\frac{1}{2}\right)^2 = \frac{1}{4}$.
    Donc :
    $|z_n^2+1| \ge 2 - 1 - \frac{1}{4} = 1 - \frac{1}{4} = \frac{3}{4}$.

Maintenant, substituons ces bornes dans l'expression de $|z_{n+1} - 1|$ :
$$|z_{n+1} - 1| \le \frac{\frac{3}{2} |z_n - 1|^2}{2 \cdot \frac{3}{4}}$$
$$|z_{n+1} - 1| \le \frac{\frac{3}{2} |z_n - 1|^2}{\frac{3}{2}}$$
$$|z_{n+1} - 1| \le |z_n - 1|^2$$
Ceci démontre la première partie de la question.

Passons à la déduction par récurrence de l'inégalité $|z_n - 1| \le \left(\frac{1}{2}\right)^{2^n}$ pour tout $n \in \mathbb{N}$.
**Initialisation (n=0)** : Par hypothèse de l'énoncé, $|z_0 - 1| \le \frac{1}{2}$. L'inégalité à prouver pour $n=0$ est $|z_0 - 1| \le \left(\frac{1}{2}\right)^{2^0} = \left(\frac{1}{2}\right)^1 = \frac{1}{2}$. L'initialisation est donc vérifiée.

**Hypothèse de récurrence** : Supposons que pour un certain entier $n \ge 0$, l'inégalité $|z_n - 1| \le \left(\frac{1}{2}\right)^{2^n}$ est vraie.

**Étape de récurrence** : Nous devons montrer que l'inégalité est également vraie pour $n+1$, c'est-à-dire $|z_{n+1} - 1| \le \left(\frac{1}{2}\right)^{2^{n+1}}$.
D'après l'hypothèse de récurrence, $|z_n - 1| \le \left(\frac{1}{2}\right)^{2^n}$.
Puisque $2^n \ge 1$ pour tout $n \ge 0$, nous avons $\left(\frac{1}{2}\right)^{2^n} \le \frac{1}{2}$.
L'hypothèse $|z_n - 1| \le \frac{1}{2}$ est donc satisfaite. Nous pouvons appliquer le résultat que nous venons de démontrer :
$$|z_{n+1} - 1| \le |z_n - 1|^2$$
En utilisant l'hypothèse de récurrence dans cette inégalité :
$$|z_{n+1} - 1| \le \left(\left(\frac{1}{2}\right)^{2^n}\right)^2$$
$$|z_{n+1} - 1| \le \left(\frac{1}{2}\right)^{2^n \cdot 2}$$
$$|z_{n+1} - 1| \le \left(\frac{1}{2}\right)^{2^{n+1}}$$
L'inégalité est donc vérifiée pour $n+1$.
Par le principe d'induction mathématique, l'inégalité $|z_n - 1| \le \left(\frac{1}{2}\right)^{2^n}$ est vraie pour tout $n \in \mathbb{N}$.

### Question 3 : Utiliser le critère de Cauchy pour prouver que la suite $(z_n)_{n \in \mathbb{N}}$ converge.

Le critère de Cauchy pour une suite de nombres complexes $(z_n)$ stipule que la suite converge si et seulement si elle est une suite de Cauchy. Une suite $(z_n)$ est de Cauchy si pour tout $\epsilon > 0$, il existe un entier $N \in \mathbb{N}$ tel que pour tous entiers $p, q$ vérifiant $p > N$ et $q > N$, on a $|z_p - z_q| < \epsilon$.

Nous avons établi à la question précédente que pour tout $n \in \mathbb{N}$, $|z_n - 1| \le \left(\frac{1}{2}\right)^{2^n}$.
Soit $\epsilon > 0$ un nombre réel strictement positif. Nous devons trouver un entier $N$ approprié.
Considérons deux indices $p$ et $q$ tels que $p > N$ et $q > N$.
En utilisant l'inégalité triangulaire pour les nombres complexes :
$$|z_p - z_q| = |(z_p - 1) - (z_q - 1)| \le |z_p - 1| + |z_q - 1|$$
En appliquant la borne que nous avons démontrée :
$$|z_p - z_q| \le \left(\frac{1}{2}\right)^{2^p} + \left(\frac{1}{2}\right)^{2^q}$$
Puisque $p > N$ et $q > N$, et que la fonction $x \mapsto 2^x$ est strictement croissante, nous avons $2^p > 2^N$ et $2^q > 2^N$.
De plus, la fonction $y \mapsto \left(\frac{1}{2}\right)^y$ est strictement décroissante. Donc :
$\left(\frac{1}{2}\right)^{2^p} < \left(\frac{1}{2}\right)^{2^N}$ et $\left(\frac{1}{2}\right)^{2^q} < \left(\frac{1}{2}\right)^{2^N}$.
En substituant ces inégalités :
$$|z_p - z_q| < \left(\frac{1}{2}\right)^{2^N} + \left(\frac{1}{2}\right)^{2^N} = 2 \cdot \left(\frac{1}{2}\right)^{2^N}$$
Nous voulons que cette quantité soit inférieure à $\epsilon$. Il suffit donc de trouver $N$ tel que $2 \cdot \left(\frac{1}{2}\right)^{2^N} < \epsilon$.
Ceci est équivalent à $\left(\frac{1}{2}\right)^{2^N} < \frac{\epsilon}{2}$.

Pour trouver $N$, nous prenons le logarithme (par exemple en base 2) des deux côtés.
Si $\epsilon \ge 2$, alors $\frac{\epsilon}{2} \ge 1$. Dans ce cas, $\left(\frac{1}{2}\right)^{2^N} < 1$ est toujours vrai pour $N \ge 0$ (car $2^N \ge 1$), donc n'importe quel $N \ge 0$ convient. Nous pouvons choisir $N=0$.
Si $0 < \epsilon < 2$, alors $0 < \frac{\epsilon}{2} < 1$.
$\log_2\left(\left(\frac{1}{2}\right)^{2^N}\right) < \log_2\left(\frac{\epsilon}{2}\right)$
$2^N \log_2\left(\frac{1}{2}\right) < \log_2\left(\frac{\epsilon}{2}\right)$
$-2^N < \log_2\left(\frac{\epsilon}{2}\right)$
Multiplions par $-1$ et inversons l'inégalité :
$2^N > -\log_2\left(\frac{\epsilon}{2}\right)$
$2^N > \log_2\left(\frac{2}{\epsilon}\right)$
Prenons à nouveau le logarithme en base 2 :
$N > \log_2\left(\log_2\left(\frac{2}{\epsilon}\right)\right)$
Puisque $\epsilon < 2$, $\frac{2}{\epsilon} > 1$, donc $\log_2\left(\frac{2}{\epsilon}\right) > 0$. Le logarithme est bien défini.
Nous pouvons choisir $N$ comme le plus petit entier supérieur à $\log_2\left(\log_2\left(\frac{2}{\epsilon}\right)\right)$. Par exemple, $N = \max(0, \lceil \log_2(\log_2(\frac{2}{\epsilon})) \rceil)$.

Pour un tel $N$ (choisi en fonction de $\epsilon$), si $p > N$ et $q > N$, alors $|z_p - z_q| < \epsilon$.
Par conséquent, la suite $(z_n)$ est une suite de Cauchy.
Puisque l'ensemble des nombres complexes $\mathbb{C}$ est un espace complet (toute suite de Cauchy y converge), nous pouvons conclure que la suite $(z_n)_{n \in \mathbb{N}}$ converge.

### Question 4 : Déterminer la limite de la suite $(z_n)_{n \in \mathbb{N}}$.

Nous avons prouvé à la question 3 que la suite $(z_n)$ converge. Soit $L$ sa limite.
La fonction $f(z) = \frac{1}{2}z + \frac{1}{z^2+1}$ est une fonction continue sur son domaine de définition (où $z^2+1 \neq 0$). Nous avons montré à la question 1 que $z_n^2+1 \neq 0$ pour tout $n$, et donc $L^2+1 \neq 0$ (car si $L^2+1=0$, alors $L=i$ ou $L=-i$, mais la suite reste dans $D(1, 1/2)$ et $i, -i$ n'y sont pas).
Par conséquent, nous pouvons passer à la limite dans la relation de récurrence $z_{n+1} = \frac{1}{2} z_n + \frac{1}{z_n^2+1}$ :
$$\lim_{n \to \infty} z_{n+1} = \frac{1}{2} \lim_{n \to \infty} z_n + \frac{1}{(\lim_{n \to \infty} z_n)^2+1}$$
$$L = \frac{1}{2} L + \frac{1}{L^2+1}$$
Maintenant, nous résolvons cette équation pour trouver $L$ :
$$L - \frac{1}{2} L = \frac{1}{L^2+1}$$
$$\frac{1}{2} L = \frac{1}{L^2+1}$$
Multiplions par $2(L^2+1)$ (qui est non nul) :
$$L(L^2+1) = 2$$
$$L^3 + L = 2$$
$$L^3 + L - 2 = 0$$
Nous cherchons les racines de ce polynôme de degré 3. Nous pouvons tester des valeurs entières simples.
Pour $L=1$ : $1^3 + 1 - 2 = 1 + 1 - 2 = 0$. Donc $L=1$ est une racine.
Puisque $L=1$ est une racine, $(L-1)$ est un facteur du polynôme $L^3+L-2$. Nous pouvons effectuer une division polynomiale ou une factorisation :
$L^3 + L - 2 = (L-1)(L^2+L+2)$.
Les autres racines sont données par l'équation quadratique $L^2+L+2=0$.
Calculons le discriminant $\Delta$ de cette équation :
$\Delta = b^2 - 4ac = 1^2 - 4(1)(2) = 1 - 8 = -7$.
Puisque $\Delta < 0$, les deux autres racines sont complexes et non réelles :
$L = \frac{-1 \pm \sqrt{-7}}{2} = \frac{-1 \pm i\sqrt{7}}{2}$.
Les trois solutions possibles pour la limite $L$ sont donc :
$L_1 = 1$
$L_2 = -\frac{1}{2} + i\frac{\sqrt{7}}{2}$
$L_3 = -\frac{1}{2} - i\frac{\sqrt{7}}{2}$

Pour déterminer laquelle de ces valeurs est la limite de notre suite, nous utilisons le résultat de la question 2 :
Pour tout $n \in \mathbb{N}$, nous avons $|z_n - 1| \le \left(\frac{1}{2}\right)^{2^n}$.
Lorsque $n \to \infty$, $2^n \to \infty$, et donc $\left(\frac{1}{2}\right)^{2^n} \to 0$.
Par le théorème des gendarmes (ou par la définition même de la limite), nous avons :
$$\lim_{n \to \infty} |z_n - 1| = 0$$
Ceci signifie que la distance entre $z_n$ et $1$ tend vers zéro lorsque $n$ tend vers l'infini. Par définition de la limite d'une suite, cela implique que $\lim_{n \to \infty} z_n = 1$.

Par conséquent, la limite de la suite $(z_n)_{n \in \mathbb{N}}$ est $L=1$.
