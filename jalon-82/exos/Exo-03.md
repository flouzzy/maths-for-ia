# Exercice 3 : Translation de la masse de Dirac

\subsection*{Exercice 3 : Translation de la masse de Dirac \quad $\bigstar\bigstar\bigstar\star\star$}

**Énoncé :**
Soit $a \in \mathbb{R}$. Définir la distribution $\delta_a$ et montrer qu'elle correspond à une fonctionnelle linéaire continue d'ordre 0.

**Démonstration pas à pas :**
1. **Définition :** On pose $\langle \delta_a, \phi \rangle = \phi(a)$.
2. **Linéarité :** $\langle \delta_a, \alpha \phi + \beta \psi \rangle = (\alpha \phi + \beta \psi)(a) = \alpha \phi(a) + \beta \psi(a) = \alpha \langle \delta_a, \phi \rangle + \beta \langle \delta_a, \psi \rangle$.
3. **Continuité :** Pour $\phi$ à support dans un compact $K$, $|\langle \delta_a, \phi \rangle| = |\phi(a)| \le \sup_{x \in K} |\phi(x)|$.
   Cela montre la continuité (si $\phi_n \to 0$ uniformément sur $K$, alors $\phi_n(a) \to 0$) et donne directement la majoration de l'ordre :
   $$ |\langle \delta_a, \phi \rangle| \le C \sup_{x \in K} |\phi(x)| $$ avec $C=1$ si $a \in K$ et $C=0$ sinon.
   L'ordre est donc $0$. $\blacksquare$
