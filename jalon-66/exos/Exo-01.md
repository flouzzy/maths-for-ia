### Intégrale de la fonction de Dirichlet (Mesure de Lebesgue) \quad $\bigstar\star\star\star\star$

**Énoncé :**
Calculer l'intégrale de Lebesgue de $f = \mathbf{1}_\mathbb{Q}$ sur l'intervalle $[0, 1]$ muni de la mesure de Lebesgue $\lambda$.

**Correction Détaillée :**
**Étape 1 : Typage de la fonction.**
La fonction $f = \mathbf{1}_\mathbb{Q}$ est une fonction simple, car elle ne prend qu'un nombre fini de valeurs : $1$ si $x \in \mathbb{Q}$ et $0$ si $x \notin \mathbb{Q}$.
Elle s'écrit sous la forme standard :
$$f = 1 \cdot \mathbf{1}_{\mathbb{Q} \cap [0,1]} + 0 \cdot \mathbf{1}_{[0,1] \setminus \mathbb{Q}}$$

**Étape 2 : Application de la définition.**
Par définition de l'intégrale d'une fonction simple :
$$\int_{[0,1]} f d\lambda = 1 \cdot \lambda(\mathbb{Q} \cap [0,1]) + 0 \cdot \lambda([0,1] \setminus \mathbb{Q})$$

**Étape 3 : Évaluation des mesures.**
L'ensemble $\mathbb{Q}$ est dénombrable. On peut l'écrire comme $\mathbb{Q} = \bigcup_{n=0}^\infty \{q_n\}$.
Par $\sigma$-additivité de la mesure de Lebesgue :
$$\lambda(\mathbb{Q}) = \sum_{n=0}^\infty \lambda(\{q_n\})$$
Or, la mesure de Lebesgue d'un singleton est nulle : $\lambda(\{q_n\}) = 0$.
Donc $\lambda(\mathbb{Q}) = 0$, et a fortiori $\lambda(\mathbb{Q} \cap [0,1]) = 0$.

**Étape 4 : Calcul final.**
En remplaçant dans la formule :
$$\int_{[0,1]} f d\lambda = 1 \cdot 0 + 0 \cdot 1 = 0$$

**Conclusion :**
L'intégrale de Lebesgue de la fonction indicatrice des rationnels sur $[0,1]$ est nulle. Remarquons que cette fonction n'est pas intégrable au sens de Riemann, illustrant la supériorité de la construction de Lebesgue.
