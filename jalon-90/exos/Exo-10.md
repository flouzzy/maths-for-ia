# Exercice 10 : Convergence en loi d'un maximum (Loi de Gumbel)

Niveau : $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soient $U_1, \dots, U_n$ des variables aléatoires i.i.d. de loi exponentielle $\mathcal{E}(1)$.
Posons $M_n = \max(U_1, \dots, U_n)$.
On sait que la loi exponentielle est non bornée, donc $M_n \to +\infty$ p.s.
Cherchons une normalisation. Posons $Y_n = M_n - \ln(n)$.
Montrer que $(Y_n)$ converge en loi vers une variable aléatoire dont on donnera la fonction de répartition. (C'est la distribution de Gumbel, fondamentale en théorie des valeurs extrêmes).

## Correction

**1. Fonction de répartition de $M_n$ :**
Pour un réel $x$, $M_n \le x$ si et seulement si pour tout $i \in \{1, \dots, n\}$, $U_i \le x$.
Comme les $U_i$ sont indépendantes, la probabilité de l'intersection est le produit des probabilités :
$$\mathbb{P}(M_n \le x) = \mathbb{P}(U_1 \le x, \dots, U_n \le x) = \prod_{i=1}^n \mathbb{P}(U_i \le x) = (\mathbb{P}(U_1 \le x))^n$$
La loi exponentielle de paramètre 1 a pour fonction de répartition :
$F_U(x) = 1 - e^{-x}$ si $x \ge 0$, et $0$ sinon.
Ainsi, pour $x \ge 0$, $F_{M_n}(x) = (1 - e^{-x})^n$.

**2. Fonction de répartition de $Y_n$ :**
On cherche $F_{Y_n}(y) = \mathbb{P}(Y_n \le y) = \mathbb{P}(M_n - \ln(n) \le y) = \mathbb{P}(M_n \le y + \ln(n))$.
On applique la formule trouvée à la question 1 pour $x = y + \ln(n)$.
Il faut $y + \ln(n) \ge 0$, ce qui est vrai pour $n$ assez grand ($n \ge e^{-y}$).
$$F_{Y_n}(y) = \left(1 - e^{-(y + \ln(n))}\right)^n = \left(1 - e^{-y} \cdot e^{-\ln(n)}\right)^n = \left(1 - \frac{e^{-y}}{n}\right)^n$$

**3. Limite pour la convergence en loi :**
Pour un $y \in \mathbb{R}$ fixé, passons à la limite quand $n \to +\infty$.
On utilise le développement limité du logarithme naturel :
$$\ln\left(F_{Y_n}(y)\right) = n \ln\left(1 - \frac{e^{-y}}{n}\right)$$
Comme $\frac{e^{-y}}{n} \to 0$, l'équivalent en zéro $\ln(1 - u) \sim -u$ donne :
$$n \ln\left(1 - \frac{e^{-y}}{n}\right) \sim n \left( - \frac{e^{-y}}{n} \right) = -e^{-y}$$
Ainsi, $\lim_{n \to +\infty} \ln(F_{Y_n}(y)) = -e^{-y}$.
Par continuité de l'exponentielle, on déduit :
$$\lim_{n \to +\infty} F_{Y_n}(y) = \exp(-e^{-y})$$
Notons $F(y) = \exp(-e^{-y})$.
Cette fonction $F$ est une fonction de répartition valide (elle est croissante, tend vers 0 en $-\infty$ et vers 1 en $+\infty$, et est continue sur $\mathbb{R}$).
C'est la fonction de répartition de la loi de Gumbel standard.
Puisque $F_{Y_n}(y)$ converge vers $F(y)$ en tout point de continuité de $F$ (ici partout sur $\mathbb{R}$), $Y_n converge en loi vers une variable de Gumbel.
