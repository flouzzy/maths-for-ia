## Exercice 5 : Intégrale de Dirichlet sur $\mathbb{R}$ \quad $$\bigstar\bigstar\star$$

**Énoncé :**
Calculer l'intégrale de Lebesgue $I = \int_{\mathbb{R}} \mathbf{1}_{\mathbb{Q}} \, d\lambda$ où $\lambda$ est la mesure de Lebesgue sur $\mathbb{R}$.
Montrer que cette intégrale vaut 0 bien que le domaine d'intégration soit de mesure infinie.

**Correction :**
1. La fonction $f = \mathbf{1}_{\mathbb{Q}}$ est une fonction mesurable car $\mathbb{Q}$ est un borélien (union dénombrable de singletons).
2. De plus, $f$ est une fonction étagée puisqu'elle ne prend que les valeurs 0 et 1.
3. Son écriture canonique sur la partition $(\mathbb{Q}, \mathbb{R} \setminus \mathbb{Q})$ est $f = 1 \cdot \mathbf{1}_{\mathbb{Q}} + 0 \cdot \mathbf{1}_{\mathbb{R} \setminus \mathbb{Q}}$.
4. Par définition de l'intégrale d'une fonction étagée :
   $$I = 1 \cdot \lambda(\mathbb{Q}) + 0 \cdot \lambda(\mathbb{R} \setminus \mathbb{Q})$$
5. La mesure de Lebesgue d'un ensemble dénombrable est nulle, donc $\lambda(\mathbb{Q}) = 0$.
6. L'ensemble des irrationnels $\mathbb{R} \setminus \mathbb{Q}$ est de mesure infinie ($\lambda(\mathbb{R} \setminus \mathbb{Q}) = \infty$), mais par la convention stricte $0 \cdot \infty = 0$, le deuxième terme s'annule.
7. Ainsi, $I = 1 \cdot 0 + 0 = 0$.
