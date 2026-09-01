# Exercice 6 : Lemme de Borel-Cantelli 1

**Difficulté :** $\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(A_n)$ une suite d'événements telle que $\sum \mathbb{P}(A_n) < \infty$. Montrer via le TCM que $\mathbb{P}(\limsup A_n) = 0$.

**Correction :**
Soit $N(x) = \sum_{n \ge 0} \mathbb{I}_{A_n}(x)$. Les termes sont positifs. Par le TCM (séries), $\mathbb{E}[N] = \int N d\mathbb{P} = \sum \mathbb{P}(A_n) < \infty$. Donc la fonction $N(x)$ est presque partout finie. L'événement $\limsup A_n$ correspond exactement aux $x$ qui appartiennent à une infinité de $A_n$, c'est-à-dire $N(x) = +\infty$. Puisque l'intégrale est finie, cet événement est de mesure nulle : $\mathbb{P}(\limsup A_n) = 0$. $\blacksquare$
