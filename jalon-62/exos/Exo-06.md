## Exercice 6 : Atomes d'une tribu \quad $\bigstar\bigstar\bigstar\bigstar\star$


\textbf{Énoncé :}
Soit $X$ un ensemble et $\mathcal{F}$ une tribu engendrée par une partition dénombrable $\{E_n\}_{n \in \mathbb{N}}$ de $X$ ($E_n \neq \emptyset$, disjoints, réunion vaut $X$). Montrer que tout élément de $\mathcal{F}$ est une union (éventuellement vide ou dénombrable) d'éléments $E_n$.

\textbf{Correction exhaustive pas-à-pas :}
1. Soit $\mathcal{T}$ l'ensemble des unions, finies, dénombrables ou vides, des éléments $E_n$.
2. Montrons que $\mathcal{T}$ est une tribu.
   - $\emptyset \in \mathcal{T}$ (union vide). $X \in \mathcal{T}$ car $X = \bigcup E_n$.
   - Stabilité par complémentaire : Soit $A \in \mathcal{T}$, $A = \bigcup_{n \in J} E_n$ où $J \subset \mathbb{N}$. Le complémentaire de $A$ est $X \setminus A = \bigcup_{n \notin J} E_n$ (puisque les $E_n$ forment une partition). Cette union appartient bien à $\mathcal{T}$.
   - Stabilité par union dénombrable : Une union dénombrable d'unions dénombrables d'éléments $E_n$ reste une union dénombrable d'éléments $E_n$.
3. $\mathcal{T}$ est donc une tribu. De plus, chaque $E_k \in \mathcal{T}$, donc $\mathcal{T}$ contient la partition.
4. Comme $\mathcal{F}$ est la plus petite tribu contenant la partition, on a $\mathcal{F} \subset \mathcal{T}$.
5. D'autre part, toute tribu contenant les $E_n$ doit contenir leurs unions dénombrables, donc $\mathcal{T} \subset \mathcal{F}$.
6. Par conséquent, $\mathcal{F} = \mathcal{T}$. Les $E_n$ sont appelés les atomes de cette tribu.
