\subsection*{Exercice 9 : Minimum de lois exponentielles \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

Soient $X_1, \ldots, X_n$ des variables aléatoires indépendantes, où $X_i$ suit une loi exponentielle $\mathcal{E}(\lambda_i)$.
On pose $M = \min(X_1, \ldots, X_n)$.
1. Exprimer la fonction de répartition de $M$.
2. En déduire la loi de $M$.

**Correction :**
1. Soit $x \ge 0$. La fonction de répartition de $M$ est $F_M(x) = \mathbb{P}(M \le x)$.
2. Il est plus simple de passer par le complémentaire : $\mathbb{P}(M > x) = 1 - F_M(x)$.
3. Le minimum de variables est supérieur à $x$ si et seulement si toutes les variables sont supérieures à $x$ :
   $\{M > x\} = \bigcap_{i=1}^n \{X_i > x\}$.
4. Par l'indépendance des $X_i$ :
   $\mathbb{P}(M > x) = \mathbb{P}\left(\bigcap_{i=1}^n \{X_i > x\}\right) = \prod_{i=1}^n \mathbb{P}(X_i > x)$.
5. Pour une loi exponentielle $\mathcal{E}(\lambda_i)$, $\mathbb{P}(X_i > x) = e^{-\lambda_i x}$.
6. Donc $\mathbb{P}(M > x) = \prod_{i=1}^n e^{-\lambda_i x} = e^{-(\sum_{i=1}^n \lambda_i) x}$.
7. On en déduit $F_M(x) = 1 - e^{-(\sum_{i=1}^n \lambda_i) x}$ pour $x \ge 0$, qui est exactement la fonction de répartition d'une loi exponentielle de paramètre $\Lambda = \sum_{i=1}^n \lambda_i$.
8. Conclusion : le minimum de lois exponentielles indépendantes suit une loi exponentielle dont le paramètre est la somme des paramètres.