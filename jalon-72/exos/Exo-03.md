# Exercice 3 : L'Entropie Croisée $\quad \bigstar\bigstar\star\star\star$

\textbf{Énoncé :}
Montrer que minimiser la Cross-Entropy $H(P, Q) = -\int p(x) \ln q(x) dx$ est équivalent à minimiser $D_{KL}(P \| Q)$ si la distribution $P$ (les données) est fixe.

\textbf{Correction :}
Par définition :
$$D_{KL}(P \| Q) = \int p(x) \ln\left( \frac{p(x)}{q(x)} \right) dx$$
$$D_{KL}(P \| Q) = \int p(x) \ln p(x) dx - \int p(x) \ln q(x) dx$$
Le premier terme est l'entropie négative de $P$ : $-H(P)$.
Le second terme est l'entropie croisée : $H(P, Q)$.
Ainsi, $D_{KL}(P \| Q) = -H(P) + H(P, Q)$.
Comme $P$ est fixe, $H(P)$ est constant. Donc, minimiser $D_{KL}(P \| Q)$ par rapport aux paramètres de $Q$ revient exactement à minimiser l'entropie croisée $H(P, Q)$.
