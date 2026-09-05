# Exercice 3 : L'intégrale d'une fonction nulle presque partout \quad $\bigstar\bigstar\bigstar\star\star$

Soit $(q_n)_{n \in \mathbb{N}}$ une énumération des rationnels de $[0, 1]$.
On pose $f_n(x) = \begin{cases} 1 & \text{si } x \in \{q_0, q_1, \dots, q_n\} \\ 0 & \text{sinon} \end{cases}$.

**Question :** Montrer que $\int_{0}^{1} \lim_{n \to \infty} f_n(x) dx = 0$ par convergence monotone.

**Solution Détaillée :**
1. Chaque fonction $f_n$ est la fonction indicatrice d'un ensemble fini $A_n = \{q_0, \dots, q_n\}$. $A_n$ étant fini, il est dénombrable, et sa mesure de Lebesgue est $\lambda(A_n) = 0$.
2. Par définition, l'intégrale d'une fonction simple positive est la somme pondérée des mesures. Donc $\int_{0}^{1} f_n d\lambda = 1 \cdot \lambda(A_n) = 0$.
3. La suite d'ensembles $(A_n)$ est croissante ($A_n \subset A_{n+1}$), donc la suite de fonctions $(f_n)$ est croissante : $0 \le f_n \le f_{n+1}$.
4. Appliquons le théorème de convergence monotone :
   $$ \int_{0}^{1} \lim_{n \to \infty} f_n d\lambda = \lim_{n \to \infty} \int_{0}^{1} f_n d\lambda = \lim_{n \to \infty} 0 = 0 $$
5. La fonction limite $f = \lim f_n$ est la fonction indicatrice de $\mathbb{Q} \cap [0, 1]$ (la fonction de Dirichlet sur $[0, 1]$).
6. Le théorème confirme donc que l'intégrale de la fonction de Dirichlet (qui est nulle presque partout) vaut exactement $0$.
