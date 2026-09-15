# Exercice 8 : Transformation intégrale et convolution $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soient $f, g \in L^1(\mathbb{R})$. Le produit de convolution est défini par :
$$ (f * g)(x) = \int_{\mathbb{R}} f(t) g(x - t) \, dt $$
Montrer, en utilisant les théorèmes de Tonelli et Fubini, que :
1. $(f * g)(x)$ est défini pour presque tout $x \in \mathbb{R}$.
2. $f * g \in L^1(\mathbb{R})$ et $\|f * g\|_1 \le \|f\|_1 \|g\|_1$.

## Correction

**1. Utilisation de Tonelli :**
Considérons la fonction $F(x, t) = |f(t)| |g(x-t)|$. C'est une fonction mesurable et positive sur $\mathbb{R}^2$.
Appliquons le théorème de Tonelli pour évaluer son intégrale double par rapport à la mesure de Lebesgue sur $\mathbb{R}^2$ :
$$ I = \int_{\mathbb{R}} \left( \int_{\mathbb{R}} |f(t)| |g(x-t)| \, dx \right) dt $$
À $t$ fixé, on effectue le changement de variable $u = x - t$. L'élément de mesure est $du = dx$ et les bornes restent inchangées ($-\infty$ à $+\infty$).
$$ \int_{\mathbb{R}} |g(x-t)| \, dx = \int_{\mathbb{R}} |g(u)| \, du = \|g\|_1 $$
Cette quantité est finie par hypothèse ($g \in L^1$).
On remplace dans l'intégrale extérieure :
$$ I = \int_{\mathbb{R}} |f(t)| \|g\|_1 \, dt = \|g\|_1 \int_{\mathbb{R}} |f(t)| \, dt = \|g\|_1 \|f\|_1 < +\infty $$
Ainsi, la fonction conjointe $(x,t) \mapsto f(t)g(x-t)$ est absolument intégrable sur $\mathbb{R}^2$.

**2. Utilisation de Fubini et conclusion :**
Puisque $F \in L^1(\mathbb{R}^2)$, le théorème de Fubini affirme que :
- L'intégrale par rapport à $t$, à savoir $\int_{\mathbb{R}} f(t) g(x-t) dt = (f*g)(x)$, existe et est finie pour presque tout $x \in \mathbb{R}$. (Cela prouve le point 1).
- La fonction $x \mapsto (f*g)(x)$ est intégrable (donc dans $L^1(\mathbb{R})$).
- On peut majorer sa norme $L^1$ :
$$ \|f * g\|_1 = \int_{\mathbb{R}} \left| \int_{\mathbb{R}} f(t)g(x-t) dt \right| dx \le \int_{\mathbb{R}} \left( \int_{\mathbb{R}} |f(t)| |g(x-t)| dt \right) dx $$
Par Tonelli, on vient de calculer que cette double intégrale vaut $\|f\|_1 \|g\|_1$.
Donc $\|f * g\|_1 \le \|f\|_1 \|g\|_1$. C'est l'inégalité de Young pour la convolution $L^1 * L^1$.
