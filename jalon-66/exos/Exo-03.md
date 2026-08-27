# Exercice 3 : Intégrale nulle implique fonction nulle presque partout
$\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et $f \in \mathcal{M}^+(X)$.
Démontrer que : $\int_X f \, d\mu = 0 \iff \mu(\{x \in X \mid f(x) > 0\}) = 0$.
*(Autrement dit, $f$ est nulle presque partout).*

**Correction :**
Nous devons démontrer une équivalence en prouvant les deux implications successives.
Notons $A = \{x \in X \mid f(x) > 0\}$.

1. **Sens $\impliedby$ :** Supposons $\mu(A) = 0$.
   La fonction $f$ ne prend des valeurs strictement positives que sur l'ensemble $A$.
   Considérons la fonction $g(x) = +\infty \cdot \mathbf{1}_A(x)$. On a $0 \le f(x) \le g(x)$ pour tout $x$.
   L'intégrale de $g$ est par définition $(+\infty) \cdot \mu(A) = (+\infty) \cdot 0 = 0$.
   Par croissance de l'intégrale, $0 \le \int_X f \, d\mu \le \int_X g \, d\mu = 0$.
   Donc $\int_X f \, d\mu = 0$.

2. **Sens $\implies$ :** Supposons $\int_X f \, d\mu = 0$.
   Pour isoler l'ensemble où $f$ est strictement positive, on le décompose selon des seuils de hauteur.
   Posons $A_n = \{x \in X \mid f(x) \ge \frac{1}{n}\}$ pour $n \in \mathbb{N}^*$.
   Remarquons que la suite $(A_n)_{n \ge 1}$ est croissante pour l'inclusion et que $A = \bigcup_{n=1}^\infty A_n$.
   Sur $X$, on a toujours l'inégalité $f \ge \frac{1}{n} \mathbf{1}_{A_n}$.
   Par croissance de l'intégrale :
   $$0 = \int_X f \, d\mu \ge \int_X \frac{1}{n} \mathbf{1}_{A_n} \, d\mu = \frac{1}{n} \mu(A_n)$$
   Puisque $\frac{1}{n} > 0$ et $\mu(A_n) \ge 0$, cette inégalité impose $\mu(A_n) = 0$ pour tout $n \ge 1$.
   Par la propriété de sous-additivité dénombrable de la mesure $\mu$ :
   $$\mu(A) = \mu\left(\bigcup_{n=1}^\infty A_n\right) \le \sum_{n=1}^\infty \mu(A_n) = \sum_{n=1}^\infty 0 = 0$$
   Comme la mesure est positive, $\mu(A) = 0$. La fonction $f$ est bien nulle presque partout.
