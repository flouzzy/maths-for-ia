# Exercice 10 : Non-unicité de la représentation

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
On a vu que $x \delta_0 = 0$. Plus généralement, résoudre l'équation $x T = 0$ dans l'espace des distributions $\mathcal{D}'(\mathbb{R})$. (On se contentera de la démonstration pour l'ordre 0, où on suppose que $T$ s'applique à une fonction test via $\phi(0)$).

**Correction Détaillée :**
1. **La condition nécessaire :**
   Supposons $T$ solution de $xT = 0$. Cela signifie que $\forall \phi \in \mathcal{D}(\mathbb{R})$, $\langle xT, \phi \rangle = \langle T, x\phi \rangle = 0$.
   L'application s'annule sur toute fonction de la forme $\psi(x) = x \phi(x)$.
2. **Caractérisation de ces fonctions :**
   Une fonction test $\psi$ peut s'écrire $x\phi(x)$ avec $\phi \in \mathcal{D}(\mathbb{R})$ si et seulement si $\psi(0) = 0$.
   En effet, si $\psi(0)=0$, on définit $\phi(x) = \psi(x)/x$ pour $x \neq 0$ et $\phi(0) = \psi'(0)$. Par la formule de Taylor, $\phi$ est bien $\mathcal{C}^\infty$ et garde un support compact.
3. **Conclusion sur T :**
   Donc $T$ annule le sous-espace $H = \{ \psi \in \mathcal{D}(\mathbb{R}) \mid \psi(0) = 0 \}$.
   $H$ est le noyau de la forme linéaire non nulle $\delta_0$.
   D'après un théorème d'algèbre linéaire, si une forme linéaire $T$ s'annule sur le noyau d'une forme linéaire $L$, alors $T$ est proportionnelle à $L$.
   Donc il existe une constante $C \in \mathbb{C}$ telle que $T = C \delta_0$.
   Les solutions sont exactement les distributions de la forme $C \delta_0$.
