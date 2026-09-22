\subsection*{Exercice 4 : Densité des fonctions continues à support compact \quad $\bigstar\bigstar\star$}
**Énoncé :**
Soit $f \in L^p(\mathbb{R})$ pour $1 \le p < \infty$. On sait que l'espace des fonctions étagées est dense dans $L^p$.
Montrer rigoureusement que l'espace $C_c(\mathbb{R})$ des fonctions continues à support compact est dense dans $L^p(\mathbb{R})$.

**Correction détaillée :**
1. Toute fonction $f \in L^p$ peut être approchée à $\varepsilon$ près par une fonction étagée $\phi \in L^p$ (par définition de la mesurabilité et construction de l'intégrale de Lebesgue).
2. Toute fonction étagée de $L^p$ s'écrit $\phi = \sum_{i=1}^n c_i \mathbf{1}_{A_i}$ avec $\mu(A_i) < \infty$. Il suffit donc de montrer qu'on peut approcher la fonction caractéristique $\mathbf{1}_A$ d'un ensemble de mesure finie par une fonction continue à support compact.
3. Par régularité de la mesure de Lebesgue, pour tout $A$ de mesure finie et $\varepsilon > 0$, il existe un ouvert $U$ contenant $A$ tel que $\mu(U \setminus A) < \varepsilon/2$ et un compact $K \subset A$ tel que $\mu(A \setminus K) < \varepsilon/2$.
4. Par le Lemme d'Urysohn, il existe une fonction continue $g : \mathbb{R} \to [0,1]$ telle que $g(x) = 1$ sur $K$ et $g(x) = 0$ sur le complémentaire de $U$ (donc $g$ est à support compact inclus dans $U$).
5. Évaluons l'erreur $L^p$ :
   $\|\mathbf{1}_A - g\|_p^p = \int |\mathbf{1}_A - g|^p \le \int_{U \setminus K} 1 \, d\mu = \mu(U \setminus K)$.
   Or $U \setminus K = (U \setminus A) \cup (A \setminus K)$, donc $\mu(U \setminus K) \le \varepsilon/2 + \varepsilon/2 = \varepsilon$.
6. On peut donc rendre $\|\mathbf{1}_A - g\|_p \le \varepsilon^{1/p}$ arbitrairement petit. Par linéarité, l'espace $C_c(\mathbb{R})$ est dense dans $L^p(\mathbb{R})$. \qed
