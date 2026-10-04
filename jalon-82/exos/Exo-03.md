\subsection*{Exercice 3 : Linéarité des distributions singulières \quad $\bigstar\bigstar\star\star\star$}

On définit $T = 3\delta_{-2} - 5\delta_{4}$.
1. Montrer que $T$ est une distribution.
2. Calculer $\langle T, \phi \rangle$ où $\phi(x) = x^2$ restreinte de manière adéquate à un compact.

**Correction Détaillée :**
1. L'espace $\mathcal{D}'(\mathbb{R})$ est un espace vectoriel. Puisque $\delta_{-2}$ et $\delta_{4}$ sont des distributions (le Dirac est une forme linéaire continue), toute combinaison linéaire scalaire l'est également. Ainsi, la somme $T = 3\delta_{-2} - 5\delta_{4}$ est une forme linéaire continue sur $\mathcal{D}(\mathbb{R})$, c'est donc une distribution.
2. Soit $\tilde{\phi}$ une fonction de $\mathcal{D}(\mathbb{R})$ telle que $\tilde{\phi}(x) = x^2$ sur un intervalle compact contenant à la fois $-2$ et $4$, par exemple $[-5, 5]$.
On calcule l'action de $T$ sur $\tilde{\phi}$ par linéarité :
$\langle T, \tilde{\phi} \rangle = \langle 3\delta_{-2} - 5\delta_{4}, \tilde{\phi} \rangle$
$\langle T, \tilde{\phi} \rangle = 3 \langle \delta_{-2}, \tilde{\phi} \rangle - 5 \langle \delta_{4}, \tilde{\phi} \rangle$
En utilisant la définition du Dirac, l'action est l'évaluation au point :
$\langle T, \tilde{\phi} \rangle = 3 \tilde{\phi}(-2) - 5 \tilde{\phi}(4)$
Puisque $\tilde{\phi}(x) = x^2$ en ces points :
$\langle T, \tilde{\phi} \rangle = 3(-2)^2 - 5(4)^2 = 3(4) - 5(16) = 12 - 80 = -68$. $\blacksquare$
