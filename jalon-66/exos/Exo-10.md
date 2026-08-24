# Exercice 10 : Inégalité de Tchebychev-Markov \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $f \in \mathcal{M}_+(X, \mu)$ intégrable. Pour tout $a > 0$, démontrer de manière autonome et rigoureuse que $\mu(\{x \in X \mid f(x) \ge a\}) \le \frac{1}{a} \int_X f \, d\mu$.

**Correction :**
Ceci est la pierre angulaire des probabilités, dérivée directement de la croissance de l'intégrale.
1. Posons $A = \{x \in X \mid f(x) \ge a\}$. Cet ensemble est mesurable car $f \in \mathcal{M}_+$.
2. Considérons la fonction simple (étagée) $s(x) = a \cdot \mathbf{1}_A(x)$.
3. Pour tout $x \in X$, comparons $s(x)$ et $f(x)$ :
   - Si $x \notin A$, $s(x) = 0$. Comme $f \ge 0$, on a bien $s(x) \le f(x)$.
   - Si $x \in A$, par définition de $A$, $f(x) \ge a$. Or $s(x) = a$. Donc $s(x) \le f(x)$.
4. Ainsi, sur tout $X$, on a l'inégalité $s \le f$.
5. Par croissance de l'intégrale : $\int_X s \, d\mu \le \int_X f \, d\mu$.
6. Or, par définition de l'intégrale d'une fonction simple, $\int_X s \, d\mu = a \cdot \mu(A)$.
7. On en déduit $a \cdot \mu(A) \le \int_X f \, d\mu$. Comme $a > 0$, on divise par $a$ pour obtenir $\mu(A) \le \frac{1}{a} \int_X f \, d\mu$.
