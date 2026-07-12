# Exercice 01 : Règle de d'Alembert

## Énoncé
Soit la suite $(u_n)_{n \in \mathbb{N}^*}$ définie par $u_n = \frac{n^3}{3^n}$.
Étudiez la nature de la série $\sum_{n \ge 1} u_n$.

## Correction Détaillée
1. **Typage et vérification des hypothèses :**
   Pour tout $n \in \mathbb{N}^*$, $n^3 > 0$ et $3^n > 0$. Donc $u_n > 0$.
   La série $\sum u_n$ est une série à termes strictement positifs. On peut appliquer la règle de d'Alembert.

2. **Calcul du rapport $\frac{u_{n+1}}{u_n}$ :**
   $$\frac{u_{n+1}}{u_n} = \frac{\frac{(n+1)^3}{3^{n+1}}}{\frac{n^3}{3^n}}$$
   $$\frac{u_{n+1}}{u_n} = \frac{(n+1)^3}{3^{n+1}} \times \frac{3^n}{n^3}$$
   $$\frac{u_{n+1}}{u_n} = \frac{(n+1)^3}{n^3} \times \frac{3^n}{3^n \times 3}$$
   $$\frac{u_{n+1}}{u_n} = \left(\frac{n+1}{n}\right)^3 \times \frac{1}{3}$$
   $$\frac{u_{n+1}}{u_n} = \left(1 + \frac{1}{n}\right)^3 \times \frac{1}{3}$$

3. **Passage à la limite :**
   Lorsque $n \to \infty$, $\lim_{n \to \infty} \left(1 + \frac{1}{n}\right) = 1$.
   Donc, $\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^3 = 1^3 = 1$.
   Il vient alors :
   $$\lim_{n \to \infty} \frac{u_{n+1}}{u_n} = 1 \times \frac{1}{3} = \frac{1}{3}$$

4. **Conclusion :**
   Soit $L = \frac{1}{3}$. Comme $L < 1$, d'après le critère de d'Alembert, la série $\sum_{n \ge 1} \frac{n^3}{3^n}$ est convergente.
