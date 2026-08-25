## Exercice 2 : Intégrale par rapport à la mesure de comptage \quad $\bigstar\bigstar\star\star\star$

**Énoncé :** Soit $\mu$ la mesure de comptage sur $\mathbb{N}$ (c'est-à-dire $\mu(A) = \text{card}(A)$ pour tout $A \subset \mathbb{N}$). Montrer que pour toute fonction $f : \mathbb{N} \to \mathbb{R}_+$, son intégrale de Lebesgue par rapport à $\mu$ coïncide avec la somme de la série de terme général $f(n)$.

**Correction Détaillée :**
1. Pour tout entier $N$, définissons la fonction simple $s_N$ sur $\mathbb{N}$ par :
   $$s_N(n) = \begin{cases} f(n) & \text{si } n \le N \\ 0 & \text{si } n > N \end{cases}$$
   Cette fonction s'écrit $s_N = \sum_{n=0}^N f(n) \mathbf{1}_{\{n\}}$.
2. L'intégrale de cette fonction simple par rapport à la mesure de comptage $\mu$ est :
   $$\int_\mathbb{N} s_N d\mu = \sum_{n=0}^N f(n) \mu(\{n\}) = \sum_{n=0}^N f(n) \cdot 1 = \sum_{n=0}^N f(n)$$
3. La suite de fonctions $(s_N)_{N \in \mathbb{N}}$ est une suite croissante de fonctions mesurables positives qui converge simplement vers $f$ sur $\mathbb{N}$.
4. Par définition de l'intégrale de Lebesgue (ou par application du théorème de convergence monotone que l'on verra au jalon suivant), l'intégrale de $f$ est le supremum des intégrales des fonctions simples minorantes :
   $$\int_\mathbb{N} f d\mu = \sup_N \int_\mathbb{N} s_N d\mu = \sup_N \sum_{n=0}^N f(n) = \sum_{n=0}^\infty f(n)$$
