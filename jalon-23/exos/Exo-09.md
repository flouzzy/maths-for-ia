# Exercice 9 : Comportement au bord (Théorème d'Abel)

**Énoncé :**
Soit $f(x) = \sum_{n=1}^{+\infty} \frac{(-1)^{n-1}}{n} x^n = \ln(1+x)$ pour $|x|<1$. Montrer que la série converge en $x=1$ et en déduire la somme de la série harmonique alternée.

**Correction détaillée :**
On évalue la série en $x=1$, ce qui donne la série numérique :
$$ \sum_{n=1}^{+\infty} \frac{(-1)^{n-1}}{n} $$
Cette série est la série harmonique alternée. Elle converge d'après le critère spécial des séries alternées : la suite $u_n = 1/n$ est décroissante, positive, et de limite nulle en $+\infty$.
Notons $S$ sa somme.
Puisque la série entière converge en $x=1$, le théorème d'Abel affirme que la fonction somme radiale $f(x)$ admet une limite lorsque $x \to 1^-$ et que cette limite vaut la somme de la série en $x=1$.
$$ \lim_{x \to 1^-} f(x) = \sum_{n=1}^{+\infty} \frac{(-1)^{n-1}}{n} $$
Or, pour $x \in ]-1, 1[$, on sait que $f(x) = \ln(1+x)$.
La fonction $x \mapsto \ln(1+x)$ est continue en $x=1$.
Donc $\lim_{x \to 1^-} \ln(1+x) = \ln(1+1) = \ln(2)$.
Par identification, on obtient :
$$ \sum_{n=1}^{+\infty} \frac{(-1)^{n-1}}{n} = \ln(2) $$
