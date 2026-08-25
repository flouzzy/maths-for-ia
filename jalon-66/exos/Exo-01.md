## Exercice 1 : Intégrale de la fonction de Dirichlet \quad $\bigstar\star\star\star\star$

**Énoncé :** Calculer l'intégrale de Lebesgue de $f = \mathbf{1}_\mathbb{Q}$ sur $[0, 1]$ pour la mesure de Lebesgue $\lambda$.

**Correction Détaillée :**
1. La fonction $f$ est une fonction simple car elle ne prend que les valeurs 0 et 1 sur l'intervalle $[0, 1]$.
   On peut l'écrire formellement comme $f = 1 \cdot \mathbf{1}_{\mathbb{Q} \cap [0,1]} + 0 \cdot \mathbf{1}_{[0,1] \setminus \mathbb{Q}}$.
2. Par définition de l'intégrale d'une fonction simple pour la mesure de Lebesgue $\lambda$ :
   $$\int_{[0,1]} f d\lambda = 1 \cdot \lambda(\mathbb{Q} \cap [0,1]) + 0 \cdot \lambda([0,1] \setminus \mathbb{Q})$$
3. On sait que l'ensemble des rationnels $\mathbb{Q}$ est dénombrable. La mesure de Lebesgue de tout ensemble dénombrable est nulle, donc $\lambda(\mathbb{Q} \cap [0,1]) = 0$.
4. Par conséquent, l'intégrale est :
   $$\int_{[0,1]} f d\lambda = 1 \cdot 0 + 0 = 0$$
