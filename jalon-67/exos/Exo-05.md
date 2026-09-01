---
title: "Exercice 5 : Interversion complexe avec sinus"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 5 : Interversion complexe avec sinus

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Montrer que la fonction $f(x) = \frac{\sin x}{e^x - 1}$ est intégrable sur $]0, +\infty[$. Peut-on utiliser Beppo Levi ?

## Correction Détaillée

1. La fonction $f$ n'est pas de signe constant, car $\sin x$ change de signe. Le théorème de Beppo Levi ne concerne **que** les suites (ou séries) de fonctions positives. On ne peut donc pas l'appliquer directement à $f$.
2. Cependant, pour montrer que $f$ est *intégrable* au sens de Lebesgue, il faut montrer que $\int_0^{+\infty} |f(x)| dx < +\infty$.
3. On pose $|f(x)| = \frac{|\sin x|}{e^x - 1} = |\sin x| \frac{e^{-x}}{1 - e^{-x}}$.
4. On développe à nouveau en série :
   $$|f(x)| = |\sin x| \sum_{n=1}^\infty e^{-nx} = \sum_{n=1}^\infty |\sin x| e^{-nx}$$
5. Posons $u_n(x) = |\sin x| e^{-nx}$. Cette fois, la série est à termes **positifs**. On peut appliquer le corollaire du théorème de Beppo Levi !
   $$\int_0^{+\infty} |f(x)| dx = \int_0^{+\infty} \left( \sum_{n=1}^\infty |\sin x| e^{-nx} \right) dx = \sum_{n=1}^\infty \int_0^{+\infty} |\sin x| e^{-nx} dx$$
6. On peut majorer chaque terme pour vérifier la finitude :
   $$\int_0^{+\infty} |\sin x| e^{-nx} dx \le \int_0^{+\infty} x e^{-nx} dx = \frac{1}{n^2}$$
   (En utilisant $|\sin x| \le x$ sur $\mathbb{R}_+$. Ou même plus brutalement $|\sin x| \le 1 \implies \int \le 1/n$).
7. Puisque la série $\sum \frac{1}{n^2}$ converge, on conclut que $\int_0^{+\infty} |f(x)| dx < +\infty$.
8. La fonction $f$ est donc bien intégrable. (Le calcul exact de l'intégrale sans valeur absolue se ferait alors par théorème de convergence dominée pour justifier l'interversion sur la série non absolue).
