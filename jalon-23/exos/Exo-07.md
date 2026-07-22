# Exercice 7 : Série solution d'une équation différentielle

**Énoncé :**
Résoudre l'équation différentielle $(1-x)y' - y = 0$ par développement en série entière.

**Correction détaillée :**
On cherche une solution sous la forme d'une série entière $y(x) = \sum_{n=0}^{+\infty} a_n x^n$, de rayon de convergence $R>0$.
Sur $]-R, R[$, on peut dériver terme à terme :
$$ y'(x) = \sum_{n=1}^{+\infty} n a_n x^{n-1} $$
Remplaçons dans l'équation $(1-x)y' - y = 0$ :
$$ (1-x) \sum_{n=1}^{+\infty} n a_n x^{n-1} - \sum_{n=0}^{+\infty} a_n x^n = 0 $$
Développons :
$$ \sum_{n=1}^{+\infty} n a_n x^{n-1} - \sum_{n=1}^{+\infty} n a_n x^n - \sum_{n=0}^{+\infty} a_n x^n = 0 $$
Dans la première somme, posons $k = n-1$, donc $n = k+1$. L'indice $k$ va de 0 à $+\infty$ :
$$ \sum_{k=0}^{+\infty} (k+1) a_{k+1} x^k - \sum_{n=1}^{+\infty} n a_n x^n - \sum_{n=0}^{+\infty} a_n x^n = 0 $$
Regroupons tous les termes en fonction de $x^n$ (en renommant $k$ en $n$) :
Le terme constant ($n=0$) est : $1 \cdot a_1 - a_0$.
Pour $n \geq 1$, le coefficient de $x^n$ est : $(n+1)a_{n+1} - n a_n - a_n = (n+1)a_{n+1} - (n+1)a_n$.
Par unicité du développement en série entière de la fonction nulle, tous les coefficients doivent être nuls :
Pour $n=0 : a_1 = a_0$.
Pour $n \geq 1 : (n+1)a_{n+1} - (n+1)a_n = 0 \iff a_{n+1} = a_n$.
Par récurrence immédiate, on obtient $a_n = a_0$ pour tout $n \in \mathbb{N}$.
La solution est donc :
$$ y(x) = \sum_{n=0}^{+\infty} a_0 x^n = a_0 \sum_{n=0}^{+\infty} x^n = a_0 \frac{1}{1-x} $$
Le rayon de convergence de la série obtenue est $R=1$, ce qui valide l'existence de la solution sur $]-1, 1[$.
