\subsection*{Exercice 8 : Séparabilité des polyèdres \quad $\bigstar\bigstar\bigstar\bigstar\star$}

Dans $\mathbb{R}^n$, soient $P_1 = \{ x \mid A_1 x \le b_1 \}$ et $P_2 = \{ x \mid A_2 x \le b_2 \}$ deux polyèdres disjoints. Montrer qu'ils peuvent être strictement séparés par un hyperplan.

**Correction :**

1. Les polyèdres sont des intersections finies de demi-espaces fermés, ce sont donc des ensembles convexes fermés.
2. En dimension finie, deux ensembles convexes disjoints peuvent être séparés (Théorème de séparation).
3. Si $P_1$ ou $P_2$ est compact (donc borné), la séparation stricte est immédiate par la 2ème forme de Hahn-Banach.
4. Si les deux sont non bornés, on utilise un argument spécifique à la dimension finie. Les polyèdres disjoints admettent une distance strictement positive ou sont séparés asymptotiquement, mais comme leurs directions de récession doivent être disjointes pour ne pas s'intersecter, on peut trouver un plan.
5. On démontre que la différence de Minkowski $P_1 - P_2$ est fermée en dimension finie pour des polyèdres.
6. Puisque $P_1 \cap P_2 = \emptyset$, $0 \notin P_1 - P_2$.
7. Comme $P_1 - P_2$ est fermé et convexe, on peut séparer strictement $0$ de $P_1 - P_2$.
8. Il existe un vecteur $y$ tel que $\langle y, z \rangle > 0$ pour tout $z \in P_1 - P_2$.
9. Soit $\langle y, x_1 - x_2 \rangle > 0 \implies \langle y, x_1 \rangle > \langle y, x_2 \rangle$. En prenant l'infimum sur $P_1$ et le supremum sur $P_2$, on trouve l'hyperplan séparateur.