# Exercice 6 : Convergence de la série de Fourier dans H $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Dans un espace de Hilbert $H$, soit $(e_n)_{n \in \mathbb{N}}$ une famille orthonormée infinie.
1. Soit $(c_n)_{n \in \mathbb{N}}$ une suite de nombres complexes. Montrer que la série $\sum c_n e_n$ converge dans $H$ si et seulement si la suite $(c_n)$ appartient à $\ell^2(\mathbb{N})$ (c'est-à-dire $\sum |c_n|^2 < \infty$).
2. Si $(e_n)$ est une base hilbertienne et $x \in H$, montrer que la série $\sum \langle x, e_n \rangle e_n$ converge vers $x$ dans $H$.

**Correction détaillée :**
1. Soit $S_N = \sum_{n=0}^N c_n e_n$ la suite des sommes partielles. L'espace $H$ étant complet, la suite $(S_N)$ converge dans $H$ si et seulement si c'est une suite de Cauchy.
   Pour $M > N$, la norme de la différence est :
   $\|S_M - S_N\|^2 = \left\| \sum_{n=N+1}^M c_n e_n \right\|^2$
   Par le théorème de Pythagore (les vecteurs $e_n$ étant deux à deux orthogonaux) :
   $\|S_M - S_N\|^2 = \sum_{n=N+1}^M \|c_n e_n\|^2 = \sum_{n=N+1}^M |c_n|^2 \|e_n\|^2 = \sum_{n=N+1}^M |c_n|^2$
   La condition pour que $(S_N)$ soit de Cauchy dans $H$ (le membre de gauche tend vers 0 quand $N, M \to \infty$) est donc exactement que la suite des sommes partielles $\sum_{n=0}^N |c_n|^2$ soit de Cauchy dans $\mathbb{R}$, ce qui équivaut à la convergence de la série $\sum |c_n|^2$, i.e., $(c_n) \in \ell^2(\mathbb{N})$.

2. Soit $x \in H$. D'après l'inégalité de Bessel (Exercice 5), $\sum_{n=0}^\infty |\langle x, e_n \rangle|^2 \leq \|x\|^2 < \infty$.
   Donc la suite des coefficients de Fourier $c_n = \langle x, e_n \rangle$ est dans $\ell^2(\mathbb{N})$.
   D'après la question 1, la série $y = \sum_{n=0}^\infty \langle x, e_n \rangle e_n$ converge dans $H$.
   Montrons que $y = x$.
   Pour un indice $k$ fixé, considérons le produit scalaire $\langle x - y, e_k \rangle$ :
   Par continuité du produit scalaire par rapport à la deuxième variable :
   $\langle y, e_k \rangle = \langle \lim_{N \to \infty} \sum_{n=0}^N \langle x, e_n \rangle e_n, e_k \rangle = \lim_{N \to \infty} \sum_{n=0}^N \langle x, e_n \rangle \langle e_n, e_k \rangle$
   Pour $N \geq k$, le terme $\langle e_n, e_k \rangle$ est nul sauf si $n=k$, auquel cas il vaut 1. Donc :
   $\langle y, e_k \rangle = \langle x, e_k \rangle$.
   Ainsi, $\langle x - y, e_k \rangle = 0$ pour tout $k \in \mathbb{N}$.
   Le vecteur $x - y$ est orthogonal à tous les éléments de la base $(e_n)$. Or, puisque c'est une base hilbertienne, son orthogonal est réduit à $\{0\}$ (cf. Exercice 4).
   Par conséquent, $x - y = 0$, soit $x = y$. La série converge bien vers $x$.
