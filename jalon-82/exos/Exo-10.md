\subsection*{Exercice 10 : L'équation différentielle $x T' = 0$ \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

(Exercice d'ouverture vers le Jalon 83).
Déterminer toutes les distributions $T \in \mathcal{D}'(\mathbb{R})$ telles que $x T' = 0$, sachant que par définition l'action de $T'$ est $\langle T', \phi \rangle = - \langle T, \phi' \rangle$.

**Correction Détaillée :**
D'après l'exercice 6, si $S \in \mathcal{D}'$ vérifie $xS = 0$, alors $S = c \delta_0$ pour une constante $c$.
Ici on a $x T' = 0$, donc $T' = c_1 \delta_0$.
Il faut alors chercher les primitives de la distribution de Dirac.
Par définition de la dérivée, on veut : $\langle T, -\phi' \rangle = c_1 \phi(0)$ pour toute fonction test.
Soit $\psi$ une fonction test qui s'écrit sous la forme d'une dérivée : $\psi = \phi'$ pour une certaine $\phi \in \mathcal{D}(\mathbb{R})$.
Une fonction test $\psi$ est la dérivée d'une fonction test $\phi$ (i.e. $\phi(x) = \int_{-\infty}^x \psi(t)dt \in \mathcal{D}(\mathbb{R})$) si et seulement si l'intégrale totale de $\psi$ est nulle : $\int_{-\infty}^{+\infty} \psi(t) dt = 0$.
On sait d'autre part (Exercice 1) que la dérivée de la fonction de Heaviside est le Dirac. Prouvons-le rigoureusement : $\langle H', \phi \rangle = - \langle H, \phi' \rangle = - \int_0^{+\infty} \phi'(x) dx = - (0 - \phi(0)) = \phi(0) = \langle \delta_0, \phi \rangle$.
Donc $H$ est UNE solution.
Par linéarité de la dérivation, la solution générale sera de la forme $c_1 H + c_2$ (une constante). Une distribution constante est la distribution régulière associée à une fonction constante $f(x) = c_2$.
Vérifions : $T = c_1 T_H + c_2 T_1$.
$\langle (c_1 T_H + c_2 T_1)', \phi \rangle = -c_1 \langle T_H, \phi' \rangle - c_2 \int 1 \cdot \phi'(x) dx$.
L'intégrale de $\phi'$ est nulle car $\phi$ est à support compact.
On a bien $(c_1 T_H + c_2 T_1)' = c_1 \delta_0$.
Puis $x(c_1 \delta_0) = 0$.
L'ensemble des distributions solutions est donc l'ensemble des formes $T = c_1 T_H + c_2 T_1$, c'est-à-dire des "marches d'escalier" dont le saut est en 0. $\blacksquare$
