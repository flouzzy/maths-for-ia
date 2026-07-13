# Exercice 03 : Équivalent et règle de comparaison

## Énoncé
Étudier la nature de la série $\sum u_n$ de terme général $u_n = \ln\left(1 + \frac{1}{n^2}\right)$ pour $n \ge 1$.

## Correction Détaillée
1. **Typage et vérification des hypothèses :**
   Pour tout $n \ge 1$, $\frac{1}{n^2} > 0$. Comme la fonction $x \mapsto \ln(1+x)$ est strictement positive sur $]0, +\infty[$, on a $u_n > 0$.
   Les séries sont à termes positifs.

2. **Recherche d'un équivalent :**
   On sait que le développement limité usuel du logarithme au voisinage de $0$ est $\ln(1+x) \sim_0 x$.
   Ici, posons $x_n = \frac{1}{n^2}$. On a bien $\lim_{n \to \infty} x_n = 0$.
   Donc, par composition des limites :
   $$u_n = \ln\left(1 + \frac{1}{n^2}\right) \sim_{+\infty} \frac{1}{n^2}$$

3. **Nature de la série de comparaison :**
   Soit $v_n = \frac{1}{n^2}$.
   La série $\sum v_n$ est une série de Riemann de paramètre $\alpha = 2$.
   Puisque $\alpha = 2 > 1$, la série $\sum v_n$ converge.

4. **Conclusion par le théorème de comparaison :**
   Puisque $u_n \sim v_n$ avec $u_n > 0$ et $v_n > 0$, les deux séries sont de même nature.
   La série de Riemann convergente entraîne donc que la série $\sum \ln\left(1 + \frac{1}{n^2}\right)$ est convergente.
