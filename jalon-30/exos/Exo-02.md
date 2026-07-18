# Exercice 2 : Décomposition de Dunford évidente (★★)

Soit $B = \begin{pmatrix} 3 & 4 \\ 0 & 3 \end{pmatrix} \in \mathcal{M}_2(\mathbb{R})$.
Trouver la décomposition de Dunford de $B$, $B = D + N$, et justifier rigoureusement son unicité. Calculer ensuite $B^n$ pour tout entier naturel $n$.

### Solution :

**Étape 1 : Construction de la décomposition**
On sépare la matrice $B$ en la somme d'une matrice diagonale et d'une matrice strictement triangulaire.
Soit $D = \begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix} = 3I_2$ et $N = \begin{pmatrix} 0 & 4 \\ 0 & 0 \end{pmatrix}$.
On a évidemment $B = D + N$.
Vérifions les conditions du théorème de Dunford :
1. **$D$ est-elle diagonalisable ?** Oui, $D$ est déjà une matrice diagonale.
2. **$N$ est-elle nilpotente ?** Calculons $N^2$.
   $$ N^2 = \begin{pmatrix} 0 & 4 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 4 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = 0_2 $$
   Donc $N$ est nilpotente d'indice 2.
3. **$D$ et $N$ commutent-elles ?**
   Puisque $D = 3I_2$ est un multiple de la matrice identité, elle commute avec toutes les matrices de $\mathcal{M}_2(\mathbb{R})$.
   Ainsi, $DN = ND = 3N$.

Par le théorème de décomposition de Dunford, puisqu'un tel couple existe, il est unique. Le couple $(D, N)$ est bien **la** décomposition de Dunford de $B$.

**Étape 2 : Calcul de $B^n$**
Puisque $D$ et $N$ commutent ($DN = ND$), nous sommes autorisés à appliquer la formule du binôme de Newton pour calculer $(D+N)^n$.
$$ B^n = (D+N)^n = \sum_{k=0}^{n} \binom{n}{k} D^{n-k} N^k $$
Puisque $N$ est nilpotente d'indice 2 ($N^k = 0$ pour tout $k \geq 2$), la somme s'arrête à $k=1$ (pour $n \geq 1$).
$$ B^n = \binom{n}{0} D^n N^0 + \binom{n}{1} D^{n-1} N^1 = D^n + n D^{n-1} N $$
Calculons les puissances de $D$ :
$D^n = (3I_2)^n = 3^n I_2 = \begin{pmatrix} 3^n & 0 \\ 0 & 3^n \end{pmatrix}$.
$D^{n-1} N = 3^{n-1} I_2 \begin{pmatrix} 0 & 4 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 4 \cdot 3^{n-1} \\ 0 & 0 \end{pmatrix}$.
En sommant ces deux termes, on obtient :
$$ B^n = \begin{pmatrix} 3^n & 0 \\ 0 & 3^n \end{pmatrix} + \begin{pmatrix} 0 & 4n 3^{n-1} \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 3^n & 4n 3^{n-1} \\ 0 & 3^n \end{pmatrix} $$
Cette formule, obtenue formellement, se vérifie aisément pour $n=0$, $n=1$, $n=2$, et reste vraie pour tout $n \in \mathbb{N}$.
