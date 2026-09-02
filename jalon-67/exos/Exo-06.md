# Exercice 6 : Lemme d'extraction (Fatou avant l'heure) ★★★

## Énoncé
Soit $(f_n)$ une suite de fonctions mesurables positives convergeant simplement vers $f$. Supposons qu'il existe une fonction $g$ intégrable telle que $f_n \ge g$.
Montrer que $\int f \le \liminf \int f_n$.

## Correction Détaillée
1. **Fonction positive** : Posons $h_n = f_n - g$. Cette fonction est bien positive.
2. **Utilisation d'une suite croissante** : Soit $g_n = \inf_{k \ge n} h_k$. Par définition, $(g_n)$ est une suite croissante.
3. **Convergence de la suite** : $g_n$ converge vers $\liminf h_n = f - g$.
4. **Application du TCM** : Par le théorème de convergence monotone, $\int (f - g) = \lim \int g_n$.
5. **Majoration** : Comme $g_n \le h_k$ pour $k \ge n$, on a $\int g_n \le \int h_k$. Donc $\int g_n \le \inf_{k \ge n} \int h_k$.
6. **Passage à la limite** : $\lim \int g_n \le \liminf \int h_n$.
7. **Conclusion** : En rajoutant $\int g$, on retrouve $\int f \le \liminf \int f_n$.
