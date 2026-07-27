---
title: "Exercice 9 : Optimisation sur l'hypercube via Cauchy-Schwarz"
difficulty: 5
---

## Énoncé Formel et Typage Rigoureux
Soit $\mathbb{K}$ un corps commutatif (typiquement $\mathbb{R}$ ou $\mathbb{C}$) et $E$ un $\mathbb{K}$-espace vectoriel. L'enjeu est d'éprouver la consistance algébrique des formes bilinéaires.
Dans $\mathbb{R}^n$, on considère l'hypercube $H_n = [-1, 1]^n$. Soit $v = (v_1, ..., v_n)$ un vecteur fixé de $\mathbb{R}^n$.
On cherche à maximiser la fonction $f(x) = \langle v, x \rangle = \sum_{i=1}^n v_i x_i$ sur $H_n$.
1. Utiliser l'inégalité de Cauchy-Schwarz pour trouver une borne supérieure $M_1$ de $f(x)$.
2. Trouver, par une analyse coordonnée par coordonnée, la vraie valeur maximale $M_2$ de $f(x)$ sur $H_n$.
3. L'inégalité de Cauchy-Schwarz est-elle optimale dans ce cas précis ?

## Preuve Analytique Pas-à-Pas (Zéro Ellipse)
La démarche déductive exige une formalisation intégrale sans ellipse.
**1. Borne via Cauchy-Schwarz :**
Pour tout $x \in H_n$, on a $x = (x_1, ..., x_n)$ avec $x_i \in [-1, 1]$.
Quelle est la norme maximale d'un tel vecteur ?
$\|x\|^2 = \sum x_i^2 \le \sum 1^2 = n$. Donc $\|x\| \le \sqrt{n}$.
Par l'inégalité de Cauchy-Schwarz, nous savons que :
$f(x) = \langle v, x \rangle \le |\langle v, x \rangle| \le \|v\| \|x\|$.
En utilisant notre borne sur $\|x\|$, nous obtenons une première majoration :
$f(x) \le \|v\| \sqrt{n}$.
Soit $M_1 = \|v\| \sqrt{n} = \sqrt{n \sum_{i=1}^n v_i^2}$.

**2. Vraie valeur maximale (Analyse coordonnée par coordonnée) :**
La fonction est une somme de termes indépendants : $f(x) = \sum_{i=1}^n v_i x_i$.
Pour maximiser cette somme, il faut maximiser chaque terme $v_i x_i$ de manière indépendante, en choisissant $x_i \in [-1, 1]$.
- Si $v_i > 0$, alors $v_i x_i$ est maximal pour $x_i = 1$ (et vaut $v_i$).
- Si $v_i < 0$, alors $v_i x_i$ est maximal pour $x_i = -1$ (et vaut $-v_i$).
- Si $v_i = 0$, toute valeur de $x_i$ donne $0$.
De manière générale, le choix optimal est $x_i^* = \text{sgn}(v_i)$ (le signe de $v_i$).
Dans ce cas, $v_i x_i^* = v_i \cdot \text{sgn}(v_i) = |v_i|$.
Le maximum réel de la fonction est donc :
$M_2 = \sum_{i=1}^n |v_i| = \|v\|_1$ (la norme $L^1$ de $v$).

**3. Comparaison :**
A-t-on $M_2 \le M_1$ ? (Heureusement, car $M_1$ est une borne supérieure mathématiquement prouvée).
Vérifions-le analytiquement.
On demande : $\sum_{i=1}^n |v_i| \le \sqrt{n \sum_{i=1}^n v_i^2}$.
En élevant au carré (termes positifs) :
$(\sum_{i=1}^n |v_i|)^2 \le n \sum_{i=1}^n v_i^2$.
Ceci est une application directe de... l'inégalité de Cauchy-Schwarz !
Prenons les vecteurs $U = (|v_1|, ..., |v_n|)$ et $W = (1, 1, ..., 1)$ dans $\mathbb{R}^n$.
$\langle U, W \rangle^2 \le \|U\|^2 \|W\|^2$.
$(\sum |v_i| \cdot 1)^2 \le (\sum |v_i|^2) (\sum 1^2)$.
$(\sum |v_i|)^2 \le (\sum v_i^2) \cdot n$.
Donc l'inégalité est bien vraie.
**Cauchy-Schwarz est-elle optimale pour ce problème d'optimisation (c'est-à-dire $M_1$ est-il atteint) ?**
$M_1$ est atteint si et seulement si l'inégalité de Cauchy-Schwarz sur $v$ et $x$ est une égalité, ce qui signifie (Exercice 5) que $x$ doit être colinéaire à $v$ : $x = \lambda v$.
Or, la solution optimale que nous avons trouvée, $x^* = \text{sgn}(v)$, n'est colinéaire à $v$ que si $|v_1| = |v_2| = ... = |v_n|$ (toutes les coordonnées de $v$ ont même valeur absolue).
Si $v$ est un vecteur arbitraire, par exemple $v = (1, 10, 0)$, $M_1$ est une très mauvaise approximation (trop lâche) par rapport au vrai maximum $M_2$. Cauchy-Schwarz donne une borne sûre, mais géométriquement, l'optimisation sur un hypercube (boule $L^\infty$) n'épouse pas naturellement la sphère Euclidienne (boule $L^2$) utilisée par Cauchy-Schwarz.
