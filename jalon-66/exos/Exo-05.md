# Exercice 5 : La fonction indicatrice des nombres constructibles $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $\mathcal{C} \subset \mathbb{R}$ l'ensemble des nombres réels constructibles à la règle et au compas.
Soit $f(x) = e^x \cdot \mathbf{1}_{\mathcal{C}}(x)$ sur $[0, 1]$. Calculer $\int_{[0, 1]} f \, d\lambda$.

**Correction Détaillée :**
1. L'ensemble $\mathcal{C}$ des nombres constructibles est un sous-ensemble du corps des nombres algébriques sur $\mathbb{Q}$.
2. Tout nombre algébrique est racine d'un polynôme à coefficients rationnels. Comme les polynômes à coefficients dans $\mathbb{Q}$ forment un ensemble dénombrable, et que chaque polynôme n'a qu'un nombre fini de racines, l'ensemble des nombres algébriques est dénombrable.
3. Par conséquent, $\mathcal{C}$ est dénombrable.
4. Or, la mesure de Lebesgue de tout ensemble dénombrable est nulle. Donc $\lambda(\mathcal{C}) = 0$.
5. La fonction $f$ s'annule en dehors de $\mathcal{C}$, donc $f(x) = 0$ pour $\lambda$-presque tout $x \in [0, 1]$.
6. Nous avons vu le théorème fondamental stipulant que si $f = 0$ presque partout, alors son intégrale de Lebesgue est nulle.
7. Ainsi, bien que $f$ prenne des valeurs non nulles (et même irrationnelles comme $e^{1/2}$) sur certains points, ces points forment un ensemble négligeable pour la mesure de Lebesgue.
8. Conclusion : $\int_{[0, 1]} f \, d\lambda = 0$.
