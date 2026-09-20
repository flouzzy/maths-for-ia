# Exercice 5 : Inégalité arithmético-géométrique via Jensen

**Difficulté :** ★★★☆☆


## Énoncé
Utiliser l'inégalité de Jensen pour démontrer l'inégalité arithmético-géométrique pour $n$ réels strictement positifs $x_1, \dots, x_n$ :
$$ (x_1 x_2 \dots x_n)^{1/n} \le \frac{x_1 + \dots + x_n}{n} $$

## Correction Détaillée
Soit $I = ]0, +\infty[$ et $\varphi(t) = -\ln(t)$. La fonction $\varphi$ est strictement convexe sur $I$ car sa dérivée seconde $\varphi''(t) = \frac{1}{t^2} > 0$.
Soit $X$ une variable aléatoire discrète qui prend les valeurs $x_i$ de manière équiprobable, c'est-à-dire avec $\mathbb{P}(X = x_i) = \frac{1}{n}$.
Appliquons l'inégalité de Jensen : $\varphi(\mathbb{E}[X]) \le \mathbb{E}[\varphi(X)]$.
1. Calcul de $\varphi(\mathbb{E}[X])$ :
$$ \mathbb{E}[X] = \frac{1}{n}\sum_{i=1}^n x_i \quad \implies \quad \varphi(\mathbb{E}[X]) = -\ln\left( \frac{1}{n}\sum_{i=1}^n x_i \right) $$
2. Calcul de $\mathbb{E}[\varphi(X)]$ :
$$ \mathbb{E}[\varphi(X)] = \sum_{i=1}^n \frac{1}{n} \varphi(x_i) = \frac{1}{n} \sum_{i=1}^n (-\ln(x_i)) = -\frac{1}{n} \ln\left( \prod_{i=1}^n x_i \right) = -\ln\left( \left(\prod_{i=1}^n x_i\right)^{1/n} \right) $$
L'inégalité de Jensen donne donc :
$$ -\ln\left( \frac{1}{n}\sum_{i=1}^n x_i \right) \le -\ln\left( \left(\prod_{i=1}^n x_i\right)^{1/n} \right) $$
En multipliant par $-1$ (ce qui inverse le sens de l'inégalité) :
$$ \ln\left( \frac{1}{n}\sum_{i=1}^n x_i \right) \ge \ln\left( \left(\prod_{i=1}^n x_i\right)^{1/n} \right) $$
La fonction exponentielle étant strictement croissante, on compose par l'exponentielle des deux côtés pour obtenir :
$$ \frac{x_1 + \dots + x_n}{n} \ge (x_1 x_2 \dots x_n)^{1/n} $$
Ce qui achève la démonstration.
