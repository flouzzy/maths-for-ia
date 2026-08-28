# Fonction de Dirichlet

**Difficulté :** $\star\star\star\star☆$

## Énoncé

Soit $X = [0, 1]$ muni de $\lambda$. Soit $f(x) = 1$ si $x \in \mathbb{Q}$, et $0$ sinon. Calculez $\int_X f \, d\lambda$.

---

## Correction détaillée

La fonction $f$ est la fonction indicatrice de l'ensemble des rationnels de $[0, 1]$, noté $A = \mathbb{Q} \cap [0, 1]$.
L'ensemble $\mathbb{Q}$ est dénombrable. On peut l'écrire comme une union dénombrable de singletons : $A = \bigcup_{n \in \mathbb{N}} \{q_n\}$. La mesure de Lebesgue étant $\sigma$-additive, on a :
$$ \lambda(A) = \sum_{n \in \mathbb{N}} \lambda(\{q_n\}) = \sum 0 = 0 $$
La fonction $f$ est étagée (elle ne prend que les valeurs $0$ et $1$). Son intégrale est donc directement :
$$ \int_{[0,1]} f \, d\lambda = 1 \times \lambda(A) + 0 \times \lambda([0,1] \setminus A) = 1 \times 0 + 0 \times 1 = 0 $$
