## Exercice 2 : Densité et limite en moyenne quadratique \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $f \in L^2([0,1])$. Sachant que les polynômes sont denses dans $C([0,1])$ (Théorème de Weierstrass) et que $C([0,1])$ est dense dans $L^2([0,1])$, montrer que pour tout $\epsilon > 0$, il existe un polynôme $P$ tel que $\|f - P\|_2 < \epsilon$.

**Correction :**
Fixons $\epsilon > 0$.
Puisque $C([0,1])$ est dense dans $L^2([0,1])$, il existe une fonction continue $g \in C([0,1])$ telle que :
$\| f - g \|_2 < \frac{\epsilon}{2}$

Par le théorème d'approximation de Weierstrass, l'ensemble des polynômes est dense dans $C([0,1])$ pour la norme uniforme $\| \cdot \|_\infty$.
Ainsi, il existe un polynôme $P$ tel que pour tout $x \in [0,1]$, $|g(x) - P(x)| < \frac{\epsilon}{2}$.
Cela implique que $\| g - P \|_\infty < \frac{\epsilon}{2}$.

Or, sur l'intervalle $[0,1]$ de mesure finie (égale à 1), la norme $L^2$ est dominée par la norme uniforme :
$\| g - P \|_2 = \left( \int_0^1 |g(x) - P(x)|^2 dx \right)^{1/2} \le \left( \int_0^1 \left(\frac{\epsilon}{2}\right)^2 dx \right)^{1/2} = \frac{\epsilon}{2}$.

Par l'inégalité triangulaire dans $L^2$ :
$\| f - P \|_2 \le \| f - g \|_2 + \| g - P \|_2 < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$.
Le polynôme $P$ répond donc au problème posé, prouvant la densité des polynômes dans $L^2([0,1])$.
