## Exercice 9 : Fonction mesurable d'intégrale nulle \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :** Retrouver la preuve vue en cours, que pour toute fonction $f \in \mathcal{M}_+$, si $\int f d\mu = 0$ alors $f = 0$ presque partout, en utilisant l'inégalité de Markov pour $f$.

**Correction Détaillée :**
1. L'inégalité de Markov (vue pour les fonctions simples dans l'exercice précédent et qui s'étend aux fonctions de $\mathcal{M}_+$ par passage au supremum) stipule que pour tout $\alpha > 0$, $\mu(\{f \ge \alpha\}) \le \frac{1}{\alpha} \int f d\mu$.
2. Supposons que $\int f d\mu = 0$. Alors pour tout $\alpha > 0$, on a $\mu(\{f \ge \alpha\}) \le \frac{0}{\alpha} = 0$.
   Donc $\mu(\{f \ge \alpha\}) = 0$.
3. On veut montrer que l'ensemble $A = \{x \in X \mid f(x) > 0\}$ a une mesure nulle.
4. On peut écrire $A$ comme une union dénombrable d'ensembles :
   $$A = \{f > 0\} = \bigcup_{n=1}^\infty \left\{f \ge \frac{1}{n}\right\}$$
5. Par $\sigma$-sous-additivité de la mesure $\mu$, on a :
   $$\mu(A) = \mu\left( \bigcup_{n=1}^\infty \left\{f \ge \frac{1}{n}\right\} \right) \le \sum_{n=1}^\infty \mu\left(\left\{f \ge \frac{1}{n}\right\}\right)$$
6. D'après l'étape 2, $\mu(\{f \ge 1/n\}) = 0$ pour tout entier $n \ge 1$.
7. On obtient donc :
   $$\mu(A) \le \sum_{n=1}^\infty 0 = 0$$
8. Comme une mesure est positive, $\mu(A) = 0$. Ainsi, $f = 0$ presque partout.
