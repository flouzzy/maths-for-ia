# Exercice 3 : Intégrale et mesure de Dirac $\bigstar\bigstar\star\star\star$

**Énoncé :**
On munit $\mathbb{R}$ de la mesure de Dirac en zéro, notée $\delta_0$.
Soit $f : \mathbb{R} \to \mathbb{R}_+$ une fonction mesurable positive quelconque.
Démontrer que $\int_{\mathbb{R}} f \, d\delta_0 = f(0)$.

**Correction Détaillée :**
1. **Cas des fonctions étagées :** Supposons d'abord que $s = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$ est une fonction étagée positive, où les $A_i$ forment une partition de $\mathbb{R}$.
2. Par définition de l'intégrale pour une fonction étagée :
   $$\int_{\mathbb{R}} s \, d\delta_0 = \sum_{i=1}^n a_i \delta_0(A_i)$$
3. Or, par définition de la mesure de Dirac, $\delta_0(A_i) = 1$ si $0 \in A_i$, et $\delta_0(A_i) = 0$ sinon.
4. Comme les $A_i$ forment une partition, le point $0$ appartient à un et un seul des ensembles, disons $A_k$.
   Ainsi, $\delta_0(A_k) = 1$ et pour tout $i \neq k$, $\delta_0(A_i) = 0$.
5. La somme se réduit donc à $a_k$. Mais $a_k$ est précisément la valeur de $s$ sur l'ensemble $A_k$, donc en particulier $a_k = s(0)$.
   Nous avons prouvé que $\int s \, d\delta_0 = s(0)$.
6. **Passage au supremum (fonction mesurable positive quelconque) :**
   Par définition, $\int f \, d\delta_0 = \sup \left\{ \int s \, d\delta_0 \mid s \in \mathcal{E}_+, 0 \le s \le f \right\}$.
7. D'après le point précédent, cela se réécrit :
   $$\int f \, d\delta_0 = \sup \{ s(0) \mid s \in \mathcal{E}_+, 0 \le s \le f \}$$
8. Comme $s \le f$ partout, on a en particulier $s(0) \le f(0)$. Le supremum est donc majoré par $f(0)$.
9. Pour montrer que le supremum est exactement $f(0)$, on peut construire la fonction étagée triviale $\tilde{s}(x) = f(0) \cdot \mathbf{1}_{\{0\}}(x) + 0 \cdot \mathbf{1}_{\mathbb{R} \setminus \{0\}}(x)$.
   On vérifie que $\tilde{s} \in \mathcal{E}_+$ et que $\tilde{s} \le f$ (car sur $\{0\}$, $\tilde{s}(0) = f(0) \le f(0)$, et sur $\mathbb{R} \setminus \{0\}$, $0 \le f(x)$).
   L'intégrale de cette $\tilde{s}$ est $\tilde{s}(0) = f(0)$.
10. Conclusion : Le supremum est atteint et vaut exactement $f(0)$.
