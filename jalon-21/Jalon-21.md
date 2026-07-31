---
uuid: "jalon-21"
title: "Suites de fonctions : convergence simple et convergence uniforme"
author: "Professeur Émérite de Mathématiques"
keywords: ["suites de fonctions", "convergence simple", "convergence uniforme", "limite", "continuité", "intégrale", "analyse fonctionnelle", "théorème de Dini", "séries de fonctions", "convergence en norme sup"]
description: "Ce cours explore les concepts fondamentaux de convergence simple et de convergence uniforme pour les suites de fonctions. Il en déduit les implications majeures sur la préservation des propriétés analytiques comme la continuité et l'intégrabilité, et met en lumière leur pertinence dans des domaines avancés, notamment l'intelligence artificielle."
---
# Jalon 21 : Suites de fonctions, étude de la convergence simple et de la convergence uniforme

## 1. Le mirage de la limite point par point

La genèse des suites de fonctions trouve ses racines au cœur de la crise des fondements de l'analyse au XIXe siècle. Les mathématiciens, animés par le désir de manipuler des objets limites avec la même aisance que des polynômes, se sont heurtés à des paradoxes profonds. Lorsqu'on observe une suite de fonctions $(f_n)_{n \in \mathbb{N}}$, l'intuition première est d'étudier la limite de $f_n(x)$ pour chaque point $x$ fixé. Cette approche, purement locale, est séduisante de simplicité. Elle s'apparente à observer le comportement d'une foule en regardant le destin de chaque individu isolément.

Cependant, cette limite, appelée convergence simple, est un mirage analytique. Elle ne préserve aucune des propriétés structurelles des fonctions $f_n$. Une suite de fonctions continues peut tout à fait converger simplement vers une fonction discontinue, déchirant ainsi le tissu continu de l'espace. De même, l'aire sous la courbe limite n'est pas nécessairement la limite des aires sous les courbes $f_n$. Il devenait impératif de forger un concept plus robuste, une convergence "globale" où la fonction entière se rapproche de sa limite uniformément, sans qu'aucun point ne prenne un retard arbitrairement grand. C'est la naissance de la convergence uniforme, une notion topologique sur l'espace des fonctions qui restaure l'harmonie entre limite et opérations analytiques (continuité, intégration, dérivation).

## 2. Convergence Simple et Uniforme

Considérons un ensemble non vide $D \subset \mathbb{R}$ ou $\mathbb{C}$, et $\mathbb{K} = \mathbb{R}$ ou $\mathbb{C}$. Soit $E$ l'espace des fonctions de $D$ dans $\mathbb{K}$.

**Définition 2.1 (Convergence Simple).**
Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de $D$ dans $\mathbb{K}$, et $f: D \to \mathbb{K}$ une fonction.
On dit que la suite de fonctions $(f_n)_{n \in \mathbb{N}}$ converge **simplement** vers $f$ sur $D$ si, et seulement si :
$$\forall x \in D, \quad \lim_{n \to +\infty} f_n(x) = f(x)$$
Formellement, avec des quantificateurs stricts :
$$\forall x \in D, \quad \forall \varepsilon > 0, \quad \exists N(x, \varepsilon) \in \mathbb{N}, \quad \forall n \ge N(x, \varepsilon), \quad |f_n(x) - f(x)| < \varepsilon$$
Ici, le rang de convergence $N$ dépend intrinsèquement du point $x$.

**Définition 2.2 (Convergence Uniforme).**
On dit que la suite $(f_n)_{n \in \mathbb{N}}$ converge **uniformément** vers $f$ sur $D$ si, et seulement si :
$$\forall \varepsilon > 0, \quad \exists N(\varepsilon) \in \mathbb{N}, \quad \forall n \ge N(\varepsilon), \quad \forall x \in D, \quad |f_n(x) - f(x)| < \varepsilon$$
Cette définition exige un rang $N$ universel, indépendant du point $x \in D$. La convergence a lieu "au même rythme" partout.

**Définition 2.3 (Norme de la convergence uniforme).**
Sur l'espace $\mathcal{B}(D, \mathbb{K})$ des fonctions bornées de $D$ dans $\mathbb{K}$, on définit la norme infinie (ou norme du sup) :
$$\|f\|_{\infty, D} = \sup_{x \in D} |f(x)|$$
La convergence uniforme de $(f_n)$ vers $f$ sur $D$ équivaut à la convergence vers $0$ de la suite de nombres réels :
$$\lim_{n \to +\infty} \|f_n - f\|_{\infty, D} = 0$$

## 3. Théorèmes de Transfert : La préservation des structures

Les théorèmes suivants illustrent la puissance de la convergence uniforme pour transmettre les propriétés des $f_n$ à la fonction limite $f$.

**Théorème 3.1 (Transfert de Continuité).**
Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de $D$ dans $\mathbb{K}$ et $a \in D$.
Si pour tout $n \in \mathbb{N}$, $f_n$ est continue en $a$, et si $(f_n)_{n \in \mathbb{N}}$ converge uniformément vers $f$ sur $D$ (ou au moins sur un voisinage de $a$), alors $f$ est continue en $a$.

*Preuve :*
Soit $a \in D$ et $\varepsilon > 0$.
Puisque $(f_n)$ converge uniformément vers $f$ sur $D$, il existe $N \in \mathbb{N}$ tel que :
$$\forall x \in D, \quad |f_N(x) - f(x)| \le \frac{\varepsilon}{3}$$
La fonction $f_N$ étant continue en $a$, il existe $\delta > 0$ tel que pour tout $x \in D$ vérifiant $|x - a| < \delta$ :
$$|f_N(x) - f_N(a)| \le \frac{\varepsilon}{3}$$
Par l'inégalité triangulaire, pour tout $x \in D$ tel que $|x - a| < \delta$ :
$$|f(x) - f(a)| = |f(x) - f_N(x) + f_N(x) - f_N(a) + f_N(a) - f(a)|$$
$$|f(x) - f(a)| \le |f(x) - f_N(x)| + |f_N(x) - f_N(a)| + |f_N(a) - f(a)|$$
$$|f(x) - f(a)| \le \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon$$
La fonction $f$ est donc continue en $a$. La démonstration est complète, sans aucune ellipse.

**Théorème 3.2 (Transfert d'Intégrabilité).**
Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions continues sur un segment $[a, b] \subset \mathbb{R}$ à valeurs dans $\mathbb{K}$.
Si $(f_n)_{n \in \mathbb{N}}$ converge uniformément vers $f$ sur $[a, b]$, alors :
$$\lim_{n \to +\infty} \int_a^b f_n(t) dt = \int_a^b \lim_{n \to +\infty} f_n(t) dt = \int_a^b f(t) dt$$

*Preuve :*
Puisque chaque $f_n$ est continue et que la convergence est uniforme, le théorème de transfert de continuité assure que $f$ est continue sur $[a, b]$, donc Riemann-intégrable.
On évalue la différence :
$$\left| \int_a^b f_n(t) dt - \int_a^b f(t) dt \right| = \left| \int_a^b (f_n(t) - f(t)) dt \right|$$
Par les propriétés de l'intégrale :
$$\left| \int_a^b (f_n(t) - f(t)) dt \right| \le \int_a^b |f_n(t) - f(t)| dt$$
En majorant l'intégrande par son supremum sur $[a, b]$ :
$$\int_a^b |f_n(t) - f(t)| dt \le \int_a^b \|f_n - f\|_{\infty, [a, b]} dt = (b - a) \|f_n - f\|_{\infty, [a, b]}$$
Puisque $f_n \xrightarrow{C.U.} f$ sur $[a, b]$, $\lim_{n \to +\infty} \|f_n - f\|_{\infty, [a, b]} = 0$.
Il s'ensuit que la limite de l'intégrale est l'intégrale de la limite.

**Théorème 3.3 (Théorème de Dini).**
Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions continues d'un espace métrique compact $K$ dans $\mathbb{R}$.
Si $(f_n)$ converge simplement vers une fonction $f$ continue sur $K$, et si pour tout $x \in K$, la suite $(f_n(x))_{n \in \mathbb{N}}$ est monotone (par exemple, croissante), alors la convergence est uniforme sur $K$.

## 4. Exemples et Contre-exemples

**Exemple de convergence simple mais non uniforme (Le drame de la continuité brisée) :**
Soit $f_n : [0, 1] \to \mathbb{R}$ définie par $f_n(x) = x^n$.
- Pour $x \in [0, 1[$, $\lim_{n \to +\infty} x^n = 0$.
- Pour $x = 1$, $f_n(1) = 1$, donc $\lim_{n \to +\infty} f_n(1) = 1$.
La suite converge simplement vers la fonction $f$ définie par $f(x) = 0$ si $0 \le x < 1$ et $f(1) = 1$.
Les $f_n$ sont continues, mais $f$ est discontinue en $x=1$. Selon le théorème de transfert de continuité, la convergence ne peut être uniforme sur $[0, 1]$. En effet, $\sup_{x \in [0, 1]} |f_n(x) - f(x)| = \sup_{x \in [0, 1[} |x^n| = 1 \not\to 0$.

**Exemple de convergence simple mais non transfert d'intégrabilité (La bosse glissante) :**
Soit $f_n : [0, 1] \to \mathbb{R}$ définie par :
$$f_n(x) = \begin{cases}
n^2 x & \text{si } 0 \le x \le \frac{1}{2n} \\
n - n^2(x - \frac{1}{2n}) & \text{si } \frac{1}{2n} \le x \le \frac{1}{n} \\
0 & \text{si } x > \frac{1}{n}
\end{cases}$$
Cette fonction forme un triangle de base $\frac{1}{n}$ et de hauteur $n$. L'aire sous la courbe (l'intégrale) est constante et égale à $\frac{1}{2}$.
Cependant, pour tout $x \in ]0, 1]$, il existe $N \in \mathbb{N}$ tel que pour $n \ge N$, $1/n < x$, donc $f_n(x) = 0$. Ainsi, $f_n(x) \to 0$. Pour $x=0$, $f_n(0) = 0$.
La suite converge simplement vers $f \equiv 0$.
L'intégrale de la limite est $0$, mais la limite des intégrales est $\frac{1}{2} \neq 0$. La convergence n'est donc pas uniforme (la norme infinie est $n \not\to 0$).
