# Exercice 2 : Indicatrice des rationnels dilatée $\bigstar\star\star\star\star$

**Énoncé :**
Soit $f(x) = 10 \cdot \mathbf{1}_{\mathbb{Q}}(x) + 5 \cdot \mathbf{1}_{\mathbb{R} \setminus \mathbb{Q}}(x)$ définie sur le segment $[0, 4]$.
Calculer son intégrale de Lebesgue par rapport à la mesure de Lebesgue $\lambda$.

**Correction Détaillée :**
1. Nous reconnaissons $f$ comme une fonction étagée positive sur le domaine restreint $[0, 4]$.
2. Les ensembles de niveau sont $A_1 = \mathbb{Q} \cap [0, 4]$ (où $f=10$) et $A_2 = (\mathbb{R} \setminus \mathbb{Q}) \cap [0, 4]$ (où $f=5$).
3. Par définition :
   $$\int_{[0, 4]} f \, d\lambda = 10 \cdot \lambda(\mathbb{Q} \cap [0, 4]) + 5 \cdot \lambda((\mathbb{R} \setminus \mathbb{Q}) \cap [0, 4])$$
4. La mesure de Lebesgue des rationnels est nulle : $\lambda(\mathbb{Q} \cap [0, 4]) = 0$.
5. Par additivité de la mesure, $\lambda([0, 4]) = \lambda(\mathbb{Q} \cap [0, 4]) + \lambda((\mathbb{R} \setminus \mathbb{Q}) \cap [0, 4])$.
   Donc $4 - 0 = 0 + \lambda((\mathbb{R} \setminus \mathbb{Q}) \cap [0, 4])$, d'où l'ensemble des irrationnels de ce segment a pour mesure $4$.
6. Le calcul donne :
   $$\int_{[0, 4]} f \, d\lambda = 10 \times 0 + 5 \times 4 = 20$$
