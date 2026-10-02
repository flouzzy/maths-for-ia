# Exercice 9 : Produit $\alpha(x) \delta_0$

\subsection*{Exercice 9 : Produit $\alpha(x) \delta_0$ \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

**Énoncé :**
Montrer que si $\alpha \in C^\infty(\mathbb{R})$, alors $\alpha(x) \delta_0 = \alpha(0) \delta_0$. En déduire l'équation $x T = 0$.

**Démonstration pas à pas :**
1. **Le produit avec le Dirac :** Pour $\phi \in \mathcal{D}(\mathbb{R})$ :
   $$ \langle \alpha \delta_0, \phi \rangle = \langle \delta_0, \alpha \phi \rangle = (\alpha \phi)(0) = \alpha(0) \phi(0) = \alpha(0) \langle \delta_0, \phi \rangle = \langle \alpha(0) \delta_0, \phi \rangle $$
   On a bien $\alpha(x) \delta_0 = \alpha(0) \delta_0$.
2. **Conséquence de l'équation $x T = 0$ :** Si $T = c \delta_0$, alors $x \cdot (c \delta_0) = c (0) \delta_0 = 0$.
   Réciproquement, soit $T$ solution de $xT = 0$. Pour $\phi \in \mathcal{D}(\mathbb{R})$ vérifiant $\phi(0) = 0$, il existe (par la formule de Taylor avec reste intégral) une fonction $\psi \in \mathcal{D}(\mathbb{R})$ telle que $\phi(x) = x \psi(x)$.
   Alors $\langle T, \phi \rangle = \langle T, x \psi \rangle = \langle xT, \psi \rangle = 0$.
   La distribution $T$ est donc proportionnelle au Dirac : on peut montrer que toute distribution annulée par des fonctions s'annulant en 0 est de la forme $c \delta_0$. $\blacksquare$
