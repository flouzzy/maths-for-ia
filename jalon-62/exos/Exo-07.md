## Exercice 7 : Générateurs de la tribu borélienne \quad $\bigstar\bigstar\bigstar\bigstar\star$


\textbf{Énoncé :}
Démontrer que la tribu de Borel sur $\mathbb{R}$, $\mathcal{B}(\mathbb{R})$, est engendrée par les intervalles ouverts rationnels $]p, q[$ avec $p, q \in \mathbb{Q}$.

\textbf{Correction exhaustive pas-à-pas :}
1. Notons $\mathcal{D} = \{ ]p, q[ \mid p, q \in \mathbb{Q}, p < q \}$. Puisque chaque intervalle $]p, q[$ est un ouvert, il appartient à $\mathcal{B}(\mathbb{R})$. Donc $\sigma(\mathcal{D}) \subset \mathcal{B}(\mathbb{R})$.
2. Pour l'inclusion inverse, il suffit de montrer que tout ouvert de $\mathbb{R}$ appartient à $\sigma(\mathcal{D})$.
3. Tout ouvert de $\mathbb{R}$ peut s'écrire comme une réunion au plus dénombrable d'intervalles ouverts disjoints : $U = \bigcup_{i} ]a_i, b_i[$.
4. Soit un intervalle quelconque $]a, b[$. Par la densité de $\mathbb{Q}$ dans $\mathbb{R}$, on peut trouver deux suites de rationnels $(p_n)$ et $(q_n)$ telles que $p_n \downarrow a$ et $q_n \uparrow b$ avec $p_n < q_n$.
5. On a alors $]a, b[ = \bigcup_{n} ]p_n, q_n[$. Chaque $]p_n, q_n[ \in \mathcal{D} \subset \sigma(\mathcal{D})$, donc l'union dénombrable $]a, b[ \in \sigma(\mathcal{D})$.
6. Ainsi, $U \in \sigma(\mathcal{D})$. Puisque $\mathcal{B}(\mathbb{R})$ est générée par les ouverts, $\mathcal{B}(\mathbb{R}) \subset \sigma(\mathcal{D})$.
7. En conclusion, $\mathcal{B}(\mathbb{R}) = \sigma(\mathcal{D})$.
