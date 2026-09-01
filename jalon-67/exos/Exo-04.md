---
title: "Exercice 4 : Convergence vers l'infini"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 4 : Convergence vers l'infini

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $f_n(x) = \frac{n \sqrt{x}}{1 + n^2 x^2}$ sur $]0, 1]$. Calculer $\lim_{n \to \infty} \int_0^1 f_n(x) dx$. Le théorème de Beppo Levi s'applique-t-il directement ?

## Correction Détaillée

1. Calculons d'abord la limite simple de $f_n(x)$.
   Pour $x \in ]0, 1]$ fixé :
   $$f_n(x) = \frac{n \sqrt{x}}{n^2(1/n^2 + x^2)} = \frac{\sqrt{x}}{n(1/n^2 + x^2)}$$
   Quand $n \to \infty$, le numérateur est constant et le dénominateur tend vers l'infini (car $x > 0$). Donc $\lim_{n \to \infty} f_n(x) = 0$.
2. Supposons (par l'absurde) que le théorème de Beppo Levi ou le théorème de convergence dominée s'applique. On aurait :
   $$\lim_{n \to \infty} \int_0^1 f_n(x) dx = \int_0^1 0 dx = 0$$
3. Calculons explicitement l'intégrale pour vérifier :
   $$\int_0^1 \frac{n \sqrt{x}}{1 + n^2 x^2} dx$$
   Effectuons le changement de variable $u = nx \implies du = n dx$. Pour $x=0, u=0$ et pour $x=1, u=n$.
   $$\int_0^1 f_n(x) dx = \int_0^n \frac{\sqrt{u/n}}{1 + u^2} du = \frac{1}{\sqrt{n}} \int_0^n \frac{\sqrt{u}}{1 + u^2} du$$
4. L'intégrale $\int_0^{+\infty} \frac{\sqrt{u}}{1+u^2} du$ est convergente (en $0$, $\approx \sqrt{u}$, intégrable ; en $+\infty$, $\approx u^{-3/2}$, intégrable). Notons sa valeur $I > 0$.
5. Ainsi, $\int_0^1 f_n(x) dx \sim \frac{I}{\sqrt{n}}$ quand $n \to \infty$.
   La limite de l'intégrale est donc bien $0$.
6. L'égalité $\lim \int f_n = \int \lim f_n$ est vraie.
7. *Le TCM s'applique-t-il ?* Non. La suite $(f_n)$ **n'est pas croissante**. En effet, calculons la dérivée par rapport à $n$ (en considérant $n$ continu pour simplifier) de $g(n) = \frac{n\sqrt{x}}{1+n^2x^2}$.
   $g'(n) = \frac{\sqrt{x}(1+n^2x^2) - n\sqrt{x}(2nx)}{(1+n^2x^2)^2} = \frac{\sqrt{x}(1-n^2x^2)}{(1+n^2x^2)^2}$.
   Pour $n > 1/x$, $g'(n) < 0$. La suite finit par décroître. Donc Beppo Levi ne s'applique pas. (Ici, c'est la convergence dominée qui permettrait de conclure sans calcul exact).
