\subsection*{Exercice 1 : Action d'une distribution sur une fonction test de base \quad $\bigstar\star\star\star\star$}

Soit la distribution de Dirac $\delta_1$ et la fonction test $\phi(x) = \exp(-x^2)$.
1. Vérifier que $\phi$ n'est pas strictement dans $\mathcal{D}(\mathbb{R})$. Quelle restriction appliquer pour que $\langle \delta_1, \phi \rangle$ ait un sens rigoureux ?
2. Calculer l'action de $\delta_1$ sur une fonction test modifiée $\tilde{\phi}$ qui coïncide avec $\phi$ sur $[-2, 2]$ et est nulle en dehors de $[-3, 3]$.

**Correction Détaillée :**
1. La fonction $\phi(x) = \exp(-x^2)$ est infiniment dérivable sur $\mathbb{R}$ car la fonction exponentielle et les polynômes le sont (composition de fonctions $\mathcal{C}^\infty$). Cependant, $\phi(x) > 0$ pour tout $x \in \mathbb{R}$. Son support n'est donc pas compact, ce n'est pas une fonction test de $\mathcal{D}(\mathbb{R})$. $\delta_1$ étant une distribution, elle agit par définition sur $\mathcal{D}(\mathbb{R})$.
2. On définit une nouvelle fonction test $\tilde{\phi} \in \mathcal{D}(\mathbb{R})$ telle que $\tilde{\phi}(x) = \exp(-x^2)$ pour $x \in [-2, 2]$. L'action de la distribution de Dirac en $1$ sur une fonction test est l'évaluation de cette fonction au point $1$.
Puisque $1 \in [-2, 2]$, on a $\tilde{\phi}(1) = \exp(-1^2) = e^{-1}$.
Par conséquent, $\langle \delta_1, \tilde{\phi} \rangle = e^{-1}$. $\blacksquare$
