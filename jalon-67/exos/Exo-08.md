## Exercice 8 : Passage à la limite avec poids \quad $\bigstar\bigstar\bigstar\bigstar\star$

Soit $(f_n)$ une suite croissante de fonctions positives vers $f$. Soit $g$ une fonction mesurable positive.
**Question :** Démontrer que $\int f_n g d\mu \to \int fg d\mu$.

**Solution :**
1. Puisque $g \ge 0$, la multiplication par $g$ préserve la croissance : $f_n g \le f_{n+1} g$.
2. La suite $(f_n g)$ est mesurable et positive.
3. Sa limite simple est $fg$.
4. D'après Beppo Levi appliqué à la suite $(f_n g)$, $\lim \int (f_n g) d\mu = \int (\lim f_n g) d\mu = \int fg d\mu$.
5. Ce résultat sert souvent en théorie de la mesure pour construire des mesures à densité (Théorème de Radon-Nikodym). $\blacksquare$
