# Exercice 4 : ★★

**Énoncé :**
Fermeture de l'ensemble des matrices orthogonales $\mathcal{O}_n(\mathbb{R})$.

**Correction (Zéro Ellipse) :**
Montrons que $\mathcal{O}_n(\mathbb{R}) = \{ M \in \mathcal{M}_n(\mathbb{R}) \mid M^T M = I_n \}$ est un fermé de $\mathcal{M}_n(\mathbb{R})$.

Soit $(M_k)_{k \in \mathbb{N}}$ une suite de matrices orthogonales convergeant vers une matrice $M \in \mathcal{M}_n(\mathbb{R})$.
Par hypothèse, pour tout $k \in \mathbb{N}$, $M_k^T M_k = I_n$.
L'application de transposition $A \mapsto A^T$ est linéaire en dimension finie, donc continue. Ainsi $M_k^T \to M^T$.
L'application de produit matriciel $(A, B) \mapsto AB$ est bilinéaire en dimension finie, donc continue.
Par conséquent, la suite $(M_k^T M_k)_{k \in \mathbb{N}}$ converge vers $M^T M$.
D'autre part, la suite $(M_k^T M_k)_{k \in \mathbb{N}}$ est constante égale à $I_n$, donc sa limite est $I_n$.
Par unicité de la limite, on a $M^T M = I_n$.
Donc $M \in \mathcal{O}_n(\mathbb{R})$. L'ensemble contient ses points d'accumulation, il est fermé. $\blacksquare$
