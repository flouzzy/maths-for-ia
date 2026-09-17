# Exercice 9 : Information Mutuelle $\quad \bigstar\bigstar\bigstar\bigstar\bigstar$

\textbf{Énoncé :}
L'information mutuelle $I(X; Y)$ entre deux variables aléatoires est définie comme $D_{KL}(P_{(X,Y)} \| P_X \otimes P_Y)$. Exprimer $I(X; Y)$ en fonction de l'entropie.

\textbf{Correction :}
$$I(X; Y) = \iint P(x, y) \ln\left( \frac{P(x, y)}{P(x)P(y)} \right) dx dy$$
$$= \iint P(x, y) \ln P(x, y) dx dy - \iint P(x, y) \ln P(x) dx dy - \iint P(x, y) \ln P(y) dx dy$$
Le premier terme est $-H(X, Y)$.
Dans le second terme, l'intégrale sur $y$ donne la marginale $P(x)$, donc on obtient $-\int P(x) \ln P(x) dx = H(X)$.
Le troisième terme donne de même $H(Y)$.
Donc $I(X; Y) = H(X) + H(Y) - H(X, Y)$.
L'information mutuelle mesure la réduction de l'incertitude sur $X$ quand $Y$ est connue.
