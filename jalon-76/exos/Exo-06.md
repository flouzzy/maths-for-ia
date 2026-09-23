## Exercice 6 : L'espace orthogonal d'un sous-espace dense \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $H = L^2(\mathbb{R})$. Soit $M = C_c^\infty(\mathbb{R})$ l'espace des fonctions lisses à support compact. On sait que $M$ est dense dans $H$. Montrer rigoureusement que $M^\perp = \{0\}$.

**Correction Détaillée :**
1. **Définition de l'orthogonal :** $M^\perp = \{ f \in H \mid \forall g \in M, \langle f, g \rangle = 0 \}$.
2. **Hypothèse de densité :** Puisque $M$ est dense dans $H$, pour tout $f \in H$, il existe une suite $(g_n)_{n \in \mathbb{N}}$ d'éléments de $M$ telle que $\lim_{n \to \infty} \|f - g_n\|_2 = 0$.
3. **Soit $f \in M^\perp$.** Montrons que $f = 0$.
   Puisque $f \in H$, prenons une suite $(g_n)$ dans $M$ convergeant vers $f$.
   Par continuité du produit scalaire, on a :
   $$ \|f\|_2^2 = \langle f, f \rangle = \langle f, \lim_{n \to \infty} g_n \rangle = \lim_{n \to \infty} \langle f, g_n \rangle $$
4. **Utilisation de l'orthogonalité :**
   Comme $f \in M^\perp$ et $g_n \in M$ pour tout $n$, on a $\langle f, g_n \rangle = 0$ pour tout $n$.
   Par passage à la limite, $\lim_{n \to \infty} \langle f, g_n \rangle = 0$.
5. **Conclusion :**
   On en déduit que $\|f\|_2^2 = 0$, et par séparation de la norme, $f = 0$ (presque partout). Ainsi $M^\perp = \{0\}$.
