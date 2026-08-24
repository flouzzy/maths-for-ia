# Exercice 3 : Intégrale sur un ensemble de mesure nulle \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $f \in \mathcal{M}_+(\mathbb{R})$ définie par $f(x) = e^{x^2}$. Soit $A = \mathbb{Q}$. Que vaut $\int_A f \, d\lambda$ ?

**Correction :**
Calculons cette intégrale par définition. Intégrer sur $A$ revient à intégrer $f \cdot \mathbf{1}_A$ sur l'espace entier.
1. On cherche à évaluer $I = \int_\mathbb{R} f(x) \mathbf{1}_\mathbb{Q}(x) \, d\lambda(x)$.
2. Observons que $A = \mathbb{Q}$ est un ensemble dénombrable.
3. Pour la mesure de Lebesgue, tout ensemble dénombrable est de mesure nulle, donc $\lambda(\mathbb{Q}) = 0$.
4. Ainsi, la fonction $g(x) = f(x)\mathbf{1}_\mathbb{Q}(x)$ est nulle presque partout ($\lambda$-p.p.).
5. Une proposition du cours stipule que si une fonction est nulle presque partout, son intégrale est nulle. Donc $\int_A f \, d\lambda = 0$.
