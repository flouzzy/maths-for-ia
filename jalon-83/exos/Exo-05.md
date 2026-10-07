# Exercice 5 : Dérivée de $x \delta_0$  \quad $\bigstar\bigstar\bigstar\star\star$


## Énoncé
1. Démontrer que pour toute distribution de Dirac en $0$, on a $x \delta_0 = 0$.
2. En utilisant la règle de Leibniz pour les distributions (démontrée dans l'exercice 4), en déduire une relation liant $\delta_0$ et $x \delta_0'$.

## Correction
1. Soit $\phi \in \mathcal{D}(\mathbb{R})$.
Calculons l'action de $x \delta_0$ sur $\phi$ :
$$ \langle x \delta_0, \phi \rangle = \langle \delta_0, x \phi(x) \rangle $$
Par définition de $\delta_0$, cela vaut la fonction test évaluée en $0$ :
$$ \langle x \delta_0, \phi \rangle = (0 \cdot \phi(0)) = 0 $$
Ceci est vrai pour toute $\phi$, donc $x \delta_0 = 0$ au sens des distributions.

2. On sait que $x \delta_0 = 0$.
Dérivons cette égalité des deux côtés au sens des distributions :
$$ (x \delta_0)' = 0' = 0 $$
Appliquons la règle de Leibniz $(\alpha T)' = \alpha' T + \alpha T'$ avec $\alpha(x) = x$ et $T = \delta_0$ :
$$ (x \delta_0)' = (x)' \delta_0 + x \delta_0' $$
Or $(x)' = 1$, donc :
$$ (x \delta_0)' = 1 \cdot \delta_0 + x \delta_0' = \delta_0 + x \delta_0' $$
Puisque $(x \delta_0)' = 0$, on obtient l'égalité :
$$ \delta_0 + x \delta_0' = 0 \implies x \delta_0' = - \delta_0 $$
Cette relation remarquable est typique du calcul avec les distributions.
