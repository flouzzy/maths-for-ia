---
title: "Exercice 8 : Produit de convolution (inégalité de Young pour la convolution)"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 8 : Inégalité de Young pour la convolution

## Énoncé
Soient $p, q, r \ge 1$ tels que $\frac{1}{p} + \frac{1}{q} = 1 + \frac{1}{r}$. Si $f \in L^p(\mathbb{R})$ et $g \in L^q(\mathbb{R})$, montrer que $f \ast g \in L^r(\mathbb{R})$ et $\|f \ast g\|_r \le \|f\|_p \|g\|_q$.
(Donner la preuve pour le cas simple $r=\infty$, où $p$ et $q$ sont conjugués).

## Corrigé
Considérons le cas simple $r = \infty$. La condition devient $\frac{1}{p} + \frac{1}{q} = 1$, $p$ et $q$ sont conjugués.
Le produit de convolution est $(f \ast g)(x) = \int_{\mathbb{R}} f(y) g(x-y) dy$.
On fixe $x$. Appliquons l'inégalité de Hölder aux fonctions $y \mapsto f(y)$ (dans $L^p$) et $y \mapsto g(x-y)$ (dans $L^q$).
$$ |(f \ast g)(x)| \le \int_{\mathbb{R}} |f(y)| |g(x-y)| dy \le \|f\|_p \| g(x-\cdot) \|_q $$
Par invariance par translation de la mesure de Lebesgue, $\| g(x-\cdot) \|_q = \|g\|_q$.
Donc pour tout $x$, $|(f \ast g)(x)| \le \|f\|_p \|g\|_q$.
Ceci signifie que la fonction $f \ast g$ est essentiellement bornée, donc dans $L^\infty$, et $\|f \ast g\|_\infty \le \|f\|_p \|g\|_q$.
Pour le cas général $r < \infty$, la démonstration rigoureuse s'effectue en écrivant $|f(y)g(x-y)| = \left(|f(y)|^{\frac{p}{r}} |g(x-y)|^{\frac{q}{r}}\right) \cdot |f(y)|^{1-\frac{p}{r}} \cdot |g(x-y)|^{1-\frac{q}{r}}$, puis en appliquant l'inégalité de Hölder généralisée à ces trois facteurs avec les exposants conjugués adéquats, suivi du théorème de Fubini pour intégrer sur $x$.
