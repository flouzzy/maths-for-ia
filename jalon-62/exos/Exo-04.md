## Exercice 4 : Propriétés de l'opérateur $\sigma$ \quad $\bigstar\bigstar\bigstar\star\star$


\textbf{Énoncé :}
Soient $\mathcal{C}_1$ et $\mathcal{C}_2$ deux familles de parties de $X$. Montrer que :
1. Si $\mathcal{C}_1 \subset \mathcal{C}_2$, alors $\sigma(\mathcal{C}_1) \subset \sigma(\mathcal{C}_2)$.
2. $\sigma(\sigma(\mathcal{C}_1)) = \sigma(\mathcal{C}_1)$.

\textbf{Correction exhaustive pas-à-pas :}
1. $\sigma(\mathcal{C}_2)$ est une tribu qui contient $\mathcal{C}_2$. Puisque $\mathcal{C}_1 \subset \mathcal{C}_2$, on a $\mathcal{C}_1 \subset \sigma(\mathcal{C}_2)$.
   Or $\sigma(\mathcal{C}_1)$ est l'intersection de toutes les tribus contenant $\mathcal{C}_1$. Comme $\sigma(\mathcal{C}_2)$ est l'une de ces tribus, on a nécessairement $\sigma(\mathcal{C}_1) \subset \sigma(\mathcal{C}_2)$.
2. Posons $\mathcal{T} = \sigma(\mathcal{C}_1)$. $\mathcal{T}$ est une tribu. L'opérateur $\sigma$ associe à une famille la plus petite tribu la contenant. Puisque $\mathcal{T}$ est déjà une tribu, la plus petite tribu contenant $\mathcal{T}$ est $\mathcal{T}$ elle-même.
   Ainsi, $\sigma(\sigma(\mathcal{C}_1)) = \sigma(\mathcal{T}) = \mathcal{T} = \sigma(\mathcal{C}_1)$.
