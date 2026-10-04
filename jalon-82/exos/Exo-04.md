\subsection*{Exercice 4 : Translation d'une distribution régulière \quad $\bigstar\bigstar\star\star\star$}

Soit $f \in L^1_{loc}(\mathbb{R})$ et $T_f$ sa distribution régulière associée. On définit la fonction translatée $\tau_a f(x) = f(x - a)$ pour $a \in \mathbb{R}$.
1. Calculer l'action de $T_{\tau_a f}$ sur une fonction test $\phi$.
2. En déduire une définition générale pour la translatée d'une distribution quelconque $\tau_a T$, et l'appliquer à $\delta_0$.

**Correction Détaillée :**
1. L'action de la distribution régulière associée à $f(x-a)$ est :
$\langle T_{\tau_a f}, \phi \rangle = \int_{-\infty}^{+\infty} f(x - a) \phi(x) dx$
Effectuons le changement de variable affine (donc bijectif et $\mathcal{C}^\infty$) $y = x - a$. On a $dx = dy$ :
$\langle T_{\tau_a f}, \phi \rangle = \int_{-\infty}^{+\infty} f(y) \phi(y + a) dy$
On peut réécrire cette intégrale en utilisant l'action de $T_f$ :
$\langle T_{\tau_a f}, \phi \rangle = \langle T_f, \phi(\cdot + a) \rangle$.
Ou en posant $\tau_{-a}\phi(y) = \phi(y+a)$ :
$\langle T_{\tau_a f}, \phi \rangle = \langle T_f, \tau_{-a}\phi \rangle$.
2. Cette formule n'utilise plus explicitement d'intégrale de Lebesgue, elle dépend uniquement de l'action de la distribution sur la fonction test translatée (qui est toujours dans $\mathcal{D}(\mathbb{R})$). On peut donc généraliser et définir la translatée d'une distribution $T$ par :
$\langle \tau_a T, \phi \rangle = \langle T, \tau_{-a}\phi \rangle$
Appliquons cela à $\delta_0$ :
$\langle \tau_a \delta_0, \phi \rangle = \langle \delta_0, \phi(\cdot + a) \rangle$
L'action de $\delta_0$ sur une fonction est l'évaluation de cette fonction en $0$ :
$\langle \tau_a \delta_0, \phi \rangle = \phi(0 + a) = \phi(a)$
Or $\phi(a) = \langle \delta_a, \phi \rangle$.
On conclut que la translatée de $\delta_0$ par un vecteur $a$ est $\delta_a$ : $\tau_a \delta_0 = \delta_a$. $\blacksquare$
