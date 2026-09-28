# Exercice 10 : Égalité de Wirtinger (Inégalité Isopérimétrique) $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $f : \mathbb{R} \to \mathbb{R}$ de classe $C^1$, $2\pi$-périodique, de moyenne nulle ($\int_0^{2\pi} f(t)dt = 0$).
Démontrer en utilisant Fourier que :
$$ \int_0^{2\pi} (f(t))^2 dt \le \int_0^{2\pi} (f'(t))^2 dt $$
À quelle condition a-t-on l'égalité ?

**Correction Détaillée :**
1. **Coefficients de $f'$ :**
Soit $c_n(f)$ les coefficients de Fourier de $f$.
Puisque $f$ est $C^1$, par IPP, on sait que $c_n(f') = in \cdot c_n(f)$.
La moyenne est nulle, donc $c_0(f) = 0$.

2. **Application de Parseval :**
Pour $f$ : $\frac{1}{2\pi} \int_0^{2\pi} |f(t)|^2 dt = \sum_{n=-\infty}^{+\infty} |c_n(f)|^2$.
Comme $c_0 = 0$, la somme exclut 0 :
$$ = \sum_{n \neq 0} |c_n(f)|^2 $$
Pour $f'$ : $\frac{1}{2\pi} \int_0^{2\pi} |f'(t)|^2 dt = \sum_{n=-\infty}^{+\infty} |c_n(f')|^2 = \sum_{n \neq 0} |in c_n(f)|^2 = \sum_{n \neq 0} n^2 |c_n(f)|^2$.

3. **Comparaison :**
Pour tout $n \neq 0$, on a $n \in \mathbb{Z} \setminus \{0\}$, donc $n^2 \ge 1$.
Il s'ensuit que pour tout $n$, $n^2 |c_n(f)|^2 \ge |c_n(f)|^2$.
En sommant :
$$ \sum_{n \neq 0} |c_n(f)|^2 \le \sum_{n \neq 0} n^2 |c_n(f)|^2 $$
En remultipliant par $2\pi$, l'inégalité annoncée est prouvée.

4. **Cas d'égalité :**
L'égalité est atteinte si et seulement si pour tout $n$, $(n^2 - 1)|c_n(f)|^2 = 0$.
Cela implique que $c_n(f) = 0$ pour tous les $|n| > 1$.
Les seuls coefficients non nuls possibles sont donc $c_1(f)$ et $c_{-1}(f)$.
La fonction $f$ doit donc être de la forme $f(t) = a \cos(t) + b \sin(t)$.
