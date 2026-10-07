# Exercice 4 : Génération de la loi exponentielle \quad $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $U$ une variable aléatoire suivant la loi uniforme continue sur $]0, 1[$.
On définit $X = -\frac{1}{\lambda} \ln(1-U)$, avec $\lambda > 0$.
Démontrer pas à pas que $X$ suit la loi exponentielle de paramètre $\lambda$.

## Correction

Pour caractériser la loi de la variable aléatoire $X$, nous allons calculer sa fonction de répartition $F_X(x) = \mathbb{P}(X \leq x)$.

La variable $U$ est à valeurs dans $]0, 1[$, donc $1-U$ est à valeurs dans $]0, 1[$. Le logarithme de $1-U$ est strictement négatif, et par conséquent $X = -\frac{1}{\lambda} \ln(1-U)$ est à valeurs strictement positives.
Ainsi, pour tout $x \leq 0$, $F_X(x) = \mathbb{P}(X \leq x) = 0$.

Soit $x > 0$. Par définition de $X$ :
$$ F_X(x) = \mathbb{P}\left(-\frac{1}{\lambda} \ln(1-U) \leq x\right) $$
Multiplions par $-\lambda$ (qui est strictement négatif, le sens de l'inégalité s'inverse) :
$$ F_X(x) = \mathbb{P}(\ln(1-U) \geq -\lambda x) $$
Composons par la fonction exponentielle, qui est strictement croissante sur $\mathbb{R}$ :
$$ F_X(x) = \mathbb{P}(1-U \geq e^{-\lambda x}) $$
Ce qui équivaut à :
$$ F_X(x) = \mathbb{P}(U \leq 1 - e^{-\lambda x}) $$
Puisque $U$ suit la loi uniforme sur $]0, 1[$, la probabilité $\mathbb{P}(U \leq t)$ vaut $t$ pour tout $t \in [0, 1]$.
Ici, $t = 1 - e^{-\lambda x}$. Comme $x > 0$ et $\lambda > 0$, on a $\lambda x > 0 \implies e^{-\lambda x} \in ]0, 1[$, donc $1 - e^{-\lambda x} \in ]0, 1[$.
Par conséquent :
$$ F_X(x) = 1 - e^{-\lambda x} $$

Bilan analytique :
$$ F_X(x) = \begin{cases} 1 - e^{-\lambda x} & \text{si } x > 0 \\ 0 & \text{si } x \leq 0 \end{cases} $$
En dérivant cette fonction par rapport à $x$ sur $]0, +\infty[$, on obtient la densité :
$$ f_X(x) = \lambda e^{-\lambda x} $$
C'est exactement la densité et la fonction de répartition de la loi exponentielle de paramètre $\lambda$. $\blacksquare$
