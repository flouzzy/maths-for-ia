# Exercice 02 : Critère de Cauchy

## Énoncé
Soit la série de terme général $u_n = \left(\frac{2n+1}{3n+4}\right)^n$, pour $n \in \mathbb{N}$.
Étudier la convergence de la série $\sum u_n$.

## Correction Détaillée
1. **Typage et vérification des hypothèses :**
   Pour tout $n \in \mathbb{N}$, $2n+1 > 0$ et $3n+4 > 0$. Donc $u_n > 0$.
   La série $\sum u_n$ est à termes strictement positifs. On peut appliquer le critère de Cauchy.

2. **Calcul de la racine $n$-ième :**
   $$\sqrt[n]{u_n} = \left(u_n\right)^{\frac{1}{n}} = \left( \left(\frac{2n+1}{3n+4}\right)^n \right)^{\frac{1}{n}} = \frac{2n+1}{3n+4}$$

3. **Passage à la limite :**
   On factorise le numérateur et le dénominateur par le terme de plus haut degré $n$ :
   $$\sqrt[n]{u_n} = \frac{n(2 + \frac{1}{n})}{n(3 + \frac{4}{n})} = \frac{2 + \frac{1}{n}}{3 + \frac{4}{n}}$$
   Or, $\lim_{n \to \infty} \frac{1}{n} = 0$.
   Donc,
   $$\lim_{n \to \infty} \sqrt[n]{u_n} = \frac{2 + 0}{3 + 0} = \frac{2}{3}$$

4. **Conclusion :**
   Soit $L = \frac{2}{3}$. Comme $L < 1$, d'après le critère de Cauchy, la série $\sum u_n$ est convergente.
