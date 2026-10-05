# Exercice 8 : Opérateur de projection sur la bande de base
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit $B_W = \{f \in L^2(\mathbb{R}) \mid \hat{f}(\xi) = 0 \text{ pour } |\xi| > W\}$. C'est l'espace des fonctions à bande limitée.
Soit $P_W$ l'opérateur défini par $\mathcal{F}(P_W f)(\xi) = \hat{f}(\xi) \mathbf{1}_{[-W, W]}(\xi)$.
Montrer que $P_W$ est un projecteur orthogonal sur $B_W$ dans $L^2$.

**Correction :**
1. **$P_W$ est un projecteur :** $P_W(P_W f)$ a pour transformée $\hat{f}(\xi) \mathbf{1}_{[-W, W]}(\xi) \mathbf{1}_{[-W, W]}(\xi) = \hat{f}(\xi) \mathbf{1}_{[-W, W]}(\xi)$, ce qui est la transformée de $P_W f$. Comme l'opérateur de Fourier est injectif sur $L^2$, $P_W^2 = P_W$.
2. **L'image de $P_W$ est $B_W$ :** Par définition de $\mathbf{1}_{[-W, W]}$, la transformée de toute fonction $P_W f$ est nulle en dehors de $[-W, W]$.
3. **Orthogonalité :** Il faut montrer que pour $f \in L^2$, $f - P_W f$ est orthogonal à tout $g \in B_W$.
$\langle f - P_W f, g \rangle = \frac{1}{2\pi} \langle \mathcal{F}(f - P_W f), \mathcal{F}(g) \rangle$ (Parseval)
$= \frac{1}{2\pi} \int (\hat{f}(\xi) - \hat{f}(\xi)\mathbf{1}_{[-W, W]}(\xi)) \overline{\hat{g}(\xi)} d\xi$
$= \frac{1}{2\pi} \int_{|\xi|>W} \hat{f}(\xi) \overline{\hat{g}(\xi)} d\xi$.
Comme $g \in B_W$, $\hat{g}(\xi) = 0$ sur le domaine $|\xi| > W$. L'intégrale est donc nulle. Le projecteur est bien orthogonal.
