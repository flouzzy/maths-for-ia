## Exercice 6 : Intégrale d'une fonction simple sur les rationnels \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :** Considérons la fonction $f(x) = x^2$ définie sur l'intervalle $[0, 2]$. Calculer l'intégrale de Lebesgue de $g = f \cdot \mathbf{1}_{\mathbb{Q} \cap [0,2]}$ par rapport à la mesure de Lebesgue $\lambda$.

**Correction Détaillée :**
1. La fonction $g$ prend la valeur $x^2$ si $x \in \mathbb{Q} \cap [0, 2]$ et la valeur $0$ si $x \in [0, 2] \setminus \mathbb{Q}$.
2. Les rationnels de $[0, 2]$ forment un ensemble de mesure de Lebesgue nulle : $\lambda(\mathbb{Q} \cap [0, 2]) = 0$.
3. La fonction $g$ est donc nulle en dehors d'un ensemble de mesure nulle. Autrement dit, $g = 0$ presque partout sur $[0, 2]$.
4. D'après l'exercice précédent, si deux fonctions sont égales presque partout, leurs intégrales de Lebesgue sont égales.
5. Soit $h(x) = 0$ pour tout $x \in [0, 2]$. On a $g = h$ presque partout, et $\int_{[0, 2]} h d\lambda = 0$.
6. Par conséquent, $\int_{[0, 2]} g d\lambda = 0$.
