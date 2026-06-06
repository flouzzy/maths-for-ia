# Exercice 4 : Dimension VC des intervalles ouverts
**Énoncé :** Soit $\mathcal{X} = \mathbb{R}$. Montrer que la classe $\mathcal{F} = \{ (a, b) \mid a, b \in \mathbb{R}, a < b \}$ a une dimension VC égale à 2.
**Correction Détaillée :**
* *Analyse de l'énoncé :* On doit pulvériser au moins un ensemble de 2 points, et montrer qu'aucun ensemble de 3 points n'est pulvérisable.
* *Résolution pas-à-pas :*
**Étape 1 : Pulvérisation de deux points.**
Soit $S = \{1, 2\}$.
- Pour $\emptyset$, choisissons l'intervalle $(3, 4)$. $(3, 4) \cap \{1, 2\} = \emptyset$.
- Pour $\{1\}$, choisissons $(0, 1.5)$. $(0, 1.5) \cap \{1, 2\} = \{1\}$.
- Pour $\{2\}$, choisissons $(1.5, 3)$. $(1.5, 3) \cap \{1, 2\} = \{2\}$.
- Pour $\{1, 2\}$, choisissons $(0, 3)$. $(0, 3) \cap \{1, 2\} = \{1, 2\}$.
Donc $VC(\mathcal{F}) \ge 2$.

**Étape 2 : Impossibilité pour trois points.**
Soit $S = \{x_1, x_2, x_3\}$ avec $x_1 < x_2 < x_3$.
Pour pulvériser $S$, nous devons pouvoir isoler le sous-ensemble $T = \{x_1, x_3\}$.
Il faudrait donc trouver $a$ et $b$ tels que $(a, b) \cap \{x_1, x_2, x_3\} = \{x_1, x_3\}$.
Cela implique $x_1 \in (a, b)$ et $x_3 \in (a, b)$, donc $a < x_1$ et $x_3 < b$.
Puisque $x_1 < x_2 < x_3$, on a nécessairement $a < x_1 < x_2 < x_3 < b$.
Par conséquent, $x_2$ doit obligatoirement appartenir à $(a, b)$.
Il est donc mathématiquement impossible de former $\{x_1, x_3\}$ sans y inclure $x_2$.
Aucun ensemble de 3 points ne peut être pulvérisé.
Conclusion : $VC(\mathcal{F}) = 2$. $\blacksquare$
