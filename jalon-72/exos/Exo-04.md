# Exercice 4 : KL de variables indépendantes $\quad \bigstar\bigstar\bigstar\star\star$

\textbf{Énoncé :}
Soit $P(x,y) = P_1(x)P_2(y)$ et $Q(x,y) = Q_1(x)Q_2(y)$.
Montrer que $D_{KL}(P \| Q) = D_{KL}(P_1 \| Q_1) + D_{KL}(P_2 \| Q_2)$.

\textbf{Correction :}
Par définition (via Fubini-Tonelli pour intégrer sur $\mathcal{X} \times \mathcal{Y}$) :
$$D_{KL}(P \| Q) = \iint P_1(x)P_2(y) \ln\left( \frac{P_1(x)P_2(y)}{Q_1(x)Q_2(y)} \right) dx dy$$
On sépare le log : $\ln(A B) = \ln(A) + \ln(B)$ :
$$= \iint P_1(x)P_2(y) \left[ \ln\left( \frac{P_1(x)}{Q_1(x)} \right) + \ln\left( \frac{P_2(y)}{Q_2(y)} \right) \right] dx dy$$
$$= \iint P_1(x)P_2(y) \ln\left( \frac{P_1(x)}{Q_1(x)} \right) dx dy + \iint P_1(x)P_2(y) \ln\left( \frac{P_2(y)}{Q_2(y)} \right) dx dy$$
L'intégrale sur $y$ dans le 1er terme donne 1 (car $P_2$ est une densité), l'intégrale sur $x$ dans le 2ème terme donne 1 :
$$= \int P_1(x) \ln\left( \frac{P_1(x)}{Q_1(x)} \right) dx + \int P_2(y) \ln\left( \frac{P_2(y)}{Q_2(y)} \right) dy$$
$$= D_{KL}(P_1 \| Q_1) + D_{KL}(P_2 \| Q_2)$$
