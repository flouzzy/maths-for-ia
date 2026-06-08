# Exercice 5 : VC-dimension des intervalles
**Énoncé :** Soit $\mathcal{X} = \mathbb{R}$. Considérons la classe $\mathcal{H}$ des fonctions indicatrices d'intervalles fermés $[a, b]$, où $a \le b$. Montrer que la VC-dimension de cette classe est égale à 2.

**Correction Détaillée :**
* *Analyse de l'énoncé :* La classe $\mathcal{H} = \{ \mathbb{I}_{[a, b]} \mid a, b \in \mathbb{R}, a \le b \}$. Nous devons prouver d'une part qu'il existe un ensemble de 2 points pouvant être éclaté, et d'autre part qu'aucun ensemble de 3 points ne peut l'être.
* *Résolution pas-à-pas :*
  1. **Étape 1 : Montrer que $\text{VCdim}(\mathcal{H}) \ge 2$**
     - Prenons un ensemble de deux points $x_1 < x_2$ dans $\mathbb{R}$, par exemple $\{0, 1\}$.
     - Pour réaliser l'étiquetage $(0, 0)$, on choisit un intervalle vide, ex: $[2, 3]$.
     - Pour réaliser l'étiquetage $(1, 0)$, on choisit $a=0, b=0.5$ (intervalle $[0, 0.5]$).
     - Pour réaliser l'étiquetage $(0, 1)$, on choisit $a=0.5, b=1$ (intervalle $[0.5, 1]$).
     - Pour réaliser l'étiquetage $(1, 1)$, on choisit $a=0, b=1$ (intervalle $[0, 1]$).
     - L'ensemble $\{0, 1\}$ est donc pulvérisé (éclaté) par $\mathcal{H}$.
  2. **Étape 2 : Montrer que $\text{VCdim}(\mathcal{H}) < 3$**
     - Supposons par l'absurde qu'il existe un ensemble de 3 points $S = \{x_1, x_2, x_3\}$ qui puisse être éclaté par $\mathcal{H}$.
     - Sans perte de généralité, ordonnons ces points : $x_1 < x_2 < x_3$.
     - Puisque l'ensemble est censé être pulvérisé, $\mathcal{H}$ doit pouvoir réaliser tous les $2^3 = 8$ étiquetages possibles.
     - Considérons l'étiquetage spécifique $(1, 0, 1)$, ce qui signifie $x_1 \in [a, b]$, $x_2 \notin [a, b]$, et $x_3 \in [a, b]$.
     - Pour que $x_1 \in [a, b]$, on doit avoir $a \le x_1$.
     - Pour que $x_3 \in [a, b]$, on doit avoir $x_3 \le b$.
     - Ces deux conditions impliquent que l'intervalle $[a, b]$ contient entièrement le segment $[x_1, x_3]$.
     - Or $x_2$ se trouve strictement entre $x_1$ et $x_3$ ($x_1 < x_2 < x_3$).
     - Par convexité des intervalles, si $x_1 \in [a, b]$ et $x_3 \in [a, b]$, alors toute combinaison convexe (tout point entre les deux) doit aussi appartenir à l'intervalle.
     - Par conséquent, il est mathématiquement impossible d'avoir $x_2 \notin [a, b]$. L'étiquetage $(1, 0, 1)$ ne peut pas être réalisé.
  3. **Conclusion :** Aucun ensemble de 3 points ne peut être pulvérisé. Ainsi, $\text{VCdim}(\mathcal{H}) = 2$.
