# Exercice 8 : Fonction non intégrable mais finie p.p. \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Donner un exemple d'une fonction $f \in \mathcal{M}_+$ sur $]0, 1]$ (avec la mesure de Lebesgue) telle que $f(x) < +\infty$ pour tout $x$, mais $\int_{]0,1]} f \, d\lambda = +\infty$.

**Correction :**
Prenons la fonction $f(x) = \frac{1}{x}$.

1. $f$ est continue sur $]0, 1]$, donc mesurable. Elle est positive.
2. Pour tout $x \in ]0, 1]$, $f(x) = \frac{1}{x} < +\infty$. La fonction est donc finie partout.
3. Calculons son intégrale. Pour tout entier $n > 1$, soit $f_n(x) = f(x) \mathbf{1}_{[1/n, 1]}(x)$.
Les fonctions $f_n$ sont bornées sur des intervalles fermés bornés, donc intégrables au sens de Riemann, et leurs intégrales de Lebesgue coïncident.

$\int_{]0,1]} f_n \, d\lambda = \int_{1/n}^1 \frac{1}{x} dx = [\ln x]_{1/n}^1 = \ln(1) - \ln(1/n) = \ln(n)$.

Comme $f_n \le f$ sur $]0,1]$, on a par croissance de l'intégrale :
$\int_{]0,1]} f \, d\lambda \ge \int_{]0,1]} f_n \, d\lambda = \ln(n)$ pour tout $n$.

En faisant tendre $n \to \infty$, on obtient $\int_{]0,1]} f \, d\lambda = +\infty$.
$f$ n'est donc pas intégrable de Lebesgue.
