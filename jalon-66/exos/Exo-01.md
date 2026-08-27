# Exercice 1 : Calcul direct d'intégrale de fonction étagée
$\bigstar\star\star\star\star$

**Énoncé :**
Soit l'espace mesurable $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ muni de la mesure de Lebesgue $\lambda$.
Soit $f : \mathbb{R} \to \mathbb{R}$ définie par $f = 2\mathbf{1}_{[0, 3]} + 5\mathbf{1}_{]2, 4]} + 3\mathbf{1}_{\{5\}}$.
Mettre $f$ sous forme canonique et calculer son intégrale de Lebesgue $\int_{\mathbb{R}} f \, d\lambda$.

**Correction :**
1. Identifions les intervalles disjoints et les valeurs constantes associées pour trouver la forme canonique.
   - Sur $]-\infty, 0[$, $f(x) = 0$.
   - Sur $[0, 2]$, seule l'indicatrice $\mathbf{1}_{[0, 3]}$ est non nulle, $f(x) = 2$.
   - Sur $]2, 3]$, les indicatrices $\mathbf{1}_{[0, 3]}$ et $\mathbf{1}_{]2, 4]}$ sont non nulles. $f(x) = 2 + 5 = 7$.
   - Sur $]3, 4]$, seule l'indicatrice $\mathbf{1}_{]2, 4]}$ est non nulle, $f(x) = 5$.
   - Sur $]4, 5[$, $f(x) = 0$.
   - En $x = 5$, $\mathbf{1}_{\{5\}}$ est non nulle, $f(5) = 3$.
   - Sur $]5, +\infty[$, $f(x) = 0$.
2. La forme canonique de $f$ est donc :
   $f = 2\mathbf{1}_{[0, 2]} + 7\mathbf{1}_{]2, 3]} + 5\mathbf{1}_{]3, 4]} + 3\mathbf{1}_{\{5\}}$
3. Calculons l'intégrale. Par définition de l'intégrale pour une fonction étagée positive sous forme canonique :
   $$\int_{\mathbb{R}} f \, d\lambda = 2\lambda([0, 2]) + 7\lambda(]2, 3]) + 5\lambda(]3, 4]) + 3\lambda(\{5\})$$
4. Calculons la mesure de chaque ensemble :
   - $\lambda([0, 2]) = 2 - 0 = 2$
   - $\lambda(]2, 3]) = 3 - 2 = 1$
   - $\lambda(]3, 4]) = 4 - 3 = 1$
   - $\lambda(\{5\}) = 0$ (un singleton a une mesure de Lebesgue nulle).
5. On obtient :
   $$\int_{\mathbb{R}} f \, d\lambda = 2(2) + 7(1) + 5(1) + 3(0) = 4 + 7 + 5 + 0 = 16$$
