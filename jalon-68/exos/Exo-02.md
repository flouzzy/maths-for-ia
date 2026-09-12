# Exercice 2 : Lemme de Fatou et perte de masse
$\bigstar\star\star\star\star$

## Énoncé
On munit $\mathbb{R}$ de la tribu borélienne et de la mesure de Lebesgue $\lambda$. Soit la suite de fonctions $f_n(x) = \frac{1}{n} \mathbf{1}_{[0, n]}(x)$.
1. Montrer que la suite $(f_n)_{n \in \mathbb{N}^*}$ converge simplement vers une fonction $f$ à déterminer.
2. Évaluer $\int_{\mathbb{R}} f d\lambda$ et $\liminf_{n \to \infty} \int_{\mathbb{R}} f_n d\lambda$.
3. Le Lemme de Fatou est-il vérifié ? L'inégalité est-elle stricte ? Pourquoi ?

## Correction
**1. Convergence simple :**
Pour un $x \in \mathbb{R}$ fixé :
- Si $x < 0$, $f_n(x) = 0$ pour tout $n$, donc $\lim f_n(x) = 0$.
- Si $x \geq 0$, il existe un rang $N$ tel que pour tout $n \geq N$, $n > x$. Alors $f_n(x) = \frac{1}{n}$. Or $\lim_{n \to \infty} \frac{1}{n} = 0$.
Donc, pour tout $x \in \mathbb{R}$, $\lim_{n \to \infty} f_n(x) = 0$. La suite converge simplement vers la fonction nulle $f = 0$.

**2. Calcul des intégrales :**
- L'intégrale de la limite : $\int_{\mathbb{R}} f d\lambda = \int_{\mathbb{R}} 0 d\lambda = 0$.
- L'intégrale des $f_n$ : $\int_{\mathbb{R}} f_n d\lambda = \int_0^n \frac{1}{n} dx = \frac{1}{n} \times n = 1$.
- Donc $\liminf_{n \to \infty} \int_{\mathbb{R}} f_n d\lambda = \liminf_{n \to \infty} 1 = 1$.

**3. Analyse par le Lemme de Fatou :**
Les fonctions $f_n$ sont positives et mesurables. Le lemme énonce que :
$\int_{\mathbb{R}} \liminf f_n d\lambda \leq \liminf \int_{\mathbb{R}} f_n d\lambda$.
Ici on a bien $0 \leq 1$. L'inégalité est stricte.
Cela s'explique par un phénomène de **fuite de masse vers l'infini**. La masse totale de chaque fonction est $1$, mais elle s'étale tellement (sur la largeur $n$ avec une hauteur $\frac{1}{n}$) qu'en chaque point précis, la densité s'évanouit, ce qui donne une limite ponctuelle nulle et engendre une perte de masse lors du passage à la limite sous l'intégrale.
