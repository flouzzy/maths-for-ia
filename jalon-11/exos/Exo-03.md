# Exercice 3: Orthogonal d'un sous-espace
## Énoncé
Soit $E = \mathbb{R}_2[X]$ l'espace vectoriel des polynômes de degré inférieur ou égal à 2.
Soit la base canonique $\mathcal{B} = (1, X, X^2)$. On définit les formes linéaires suivantes sur $E$ :
$\varphi_1(P) = P(0)$
$\varphi_2(P) = P'(0)$
$\varphi_3(P) = \frac{1}{2}P''(0)$
Montrer que la famille $(\varphi_1, \varphi_2, \varphi_3)$ est exactement la base duale $\mathcal{B}^*$.


## Correction détaillée
1. **Définition de l'application restriction :** On considère l'application linéaire $\rho : E^* \to F^*$ définie par $\rho(\phi) = \phi_{|F}$, c'est-à-dire que pour toute forme linéaire $\phi$ sur $E$, $\rho(\phi)$ est sa restriction au sous-espace $F$.
2. **Étude du noyau de $\rho$ :** Par définition,
   $$\ker \rho = \{ \phi \in E^* \mid \rho(\phi) = 0 \} = \{ \phi \in E^* \mid \forall x \in F, \phi(x) = 0 \}$$
   Or, l'ensemble des formes linéaires qui s'annulent sur $F$ est exactement la définition de l'orthogonal $F^\perp$. Donc $\ker \rho = F^\perp$.
3. **Étude de l'image de $\rho$ :** L'application $\rho$ est surjective. En effet, soit $\psi \in F^*$. On peut compléter une base $(e_1, \dots, e_p)$ de $F$ en une base $(e_1, \dots, e_p, e_{p+1}, \dots, e_n)$ de $E$. On définit alors une forme $\phi \in E^*$ par $\phi(e_i) = \psi(e_i)$ pour $1 \le i \le p$ et $\phi(e_i) = 0$ pour $i > p$. Ainsi $\phi_{|F} = \psi$.
   Donc $\text{Im}(\rho) = F^*$.
4. **Application du théorème du rang :** Le théorème du rang appliqué à $\rho : E^* \to F^*$ donne :
   $$\dim E^* = \dim \ker \rho + \dim \text{Im}(\rho)$$
5. **Substitutions des dimensions :**
   - $\dim E^* = \dim E = n$
   - $\dim \ker \rho = \dim F^\perp$
   - $\dim \text{Im}(\rho) = \dim F^* = \dim F$
   On obtient : $n = \dim F^\perp + \dim F$.
6. **Conclusion :** L'égalité $\dim F + \dim F^\perp = n$ est rigoureusement démontrée.

$\blacksquare$
