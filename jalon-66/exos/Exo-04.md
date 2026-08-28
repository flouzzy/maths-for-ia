# Exercice 4 : Limite de fonctions simples \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f(x) = x$ sur $[0,1]$. Pour tout entier $n \ge 1$, on pose $s_n(x) = \frac{\lfloor nx \rfloor}{n}$. Montrer que $s_n$ est une suite de fonctions simples positives, que $s_n \le f$, et calculer $\lim_{n \to \infty} \int_{[0,1]} s_n \, d\lambda$.

**Correction :**
1. $s_n(x)$ prend un nombre fini de valeurs sur $[0,1]$ : $\frac{0}{n}, \frac{1}{n}, \dots, \frac{n-1}{n}, \frac{n}{n}$. Ce sont des valeurs positives, donc $s_n \in \mathcal{S}_+$.

2. Par définition de la partie entière, $nx - 1 < \lfloor nx \rfloor \le nx$. En divisant par $n > 0$, on obtient $\frac{\lfloor nx \rfloor}{n} \le x$. Donc $s_n(x) \le f(x)$ pour tout $x \in [0,1]$.

3. Calculons l'intégrale de $s_n$ :
$s_n(x) = \frac{k}{n}$ si $x \in [\frac{k}{n}, \frac{k+1}{n}[$ pour $0 \le k \le n-1$, et $s_n(1) = 1$.
$\int_{[0,1]} s_n \, d\lambda = \sum_{k=0}^{n-1} \frac{k}{n} \lambda([\frac{k}{n}, \frac{k+1}{n}[) = \sum_{k=0}^{n-1} \frac{k}{n} \cdot \frac{1}{n} = \frac{1}{n^2} \sum_{k=0}^{n-1} k = \frac{1}{n^2} \frac{(n-1)n}{2} = \frac{n-1}{2n}$.

4. Limite : $\lim_{n \to \infty} \frac{n-1}{2n} = \lim_{n \to \infty} \left( \frac{1}{2} - \frac{1}{2n} \right) = \frac{1}{2}$.

On retrouve bien l'intégrale de Lebesgue (et de Riemann) de $f(x)=x$ sur $[0,1]$ qui est $\frac{1}{2}$.
