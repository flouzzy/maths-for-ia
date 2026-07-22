# Exercice 6 : Produit de Cauchy

**Énoncé :**
Montrer que pour tout $x \in \mathbb{R}$, $e^x \cdot e^{-x} = 1$ en utilisant le produit de Cauchy des séries entières.

**Correction détaillée :**
La fonction exponentielle est définie par sa série entière de rayon infini :
$$ e^x = \sum_{n=0}^{+\infty} \frac{x^n}{n!} $$
$$ e^{-x} = \sum_{n=0}^{+\infty} \frac{(-x)^n}{n!} = \sum_{n=0}^{+\infty} \frac{(-1)^n}{n!} x^n $$
Soit $C(x)$ le produit de Cauchy de ces deux séries. Comme elles sont absolument convergentes sur $\mathbb{R}$, leur produit est donné par :
$$ C(x) = \sum_{n=0}^{+\infty} c_n x^n $$
où
$$ c_n = \sum_{k=0}^n \left( \frac{1}{k!} \right) \left( \frac{(-1)^{n-k}}{(n-k)!} \right) $$
Multiplions et divisons par $n!$ :
$$ c_n = \frac{1}{n!} \sum_{k=0}^n \frac{n!}{k!(n-k)!} (-1)^{n-k} = \frac{1}{n!} \sum_{k=0}^n \binom{n}{k} 1^k (-1)^{n-k} $$
Par la formule du binôme de Newton, cette somme vaut $(1 + (-1))^n = 0^n$.
Pour $n > 0$, $0^n = 0$, donc $c_n = 0$.
Pour $n = 0$, $0^0 = 1$ par convention, et $c_0 = \frac{1}{0!} \cdot \frac{(-1)^0}{0!} = 1$.
Ainsi, la série produit n'a qu'un seul terme non nul, celui de rang $n=0$ :
$$ C(x) = c_0 x^0 = 1 $$
On a donc bien $e^x \cdot e^{-x} = 1$ pour tout $x \in \mathbb{R}$.
