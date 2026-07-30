---
title: "Exercice 10 : Analyse asymptotique par la méthode de Laplace"
difficulty: "$\star$$\star$$\star$$\star$$\star$"
---
# Exercice 10 : Analyse asymptotique par la méthode de Laplace ($\star$$\star$$\star$$\star$$\star$)

**Énoncé :**
Soit $I(x) = \int_a^b e^{x f(t)} g(t) dt$ avec $f$ admettant un unique maximum global strict en $c \in ]a, b[$ avec $f''(c) < 0$.
Donner, en justifiant sommairement l'application des théorèmes de majoration sous l'intégrale, l'équivalent asymptotique de $I(x)$ quand $x \to +\infty$.

**Démonstration pas-à-pas :**
1. L'idée fondamentale de la méthode de Laplace est que pour $x$ très grand, l'exponentielle $e^{x f(t)}$ est massivement concentrée autour du point maximum $t=c$.
2. On écrit le développement de Taylor de $f$ autour de $c$ :
   $f(t) = f(c) + \frac{1}{2} f''(c) (t-c)^2 + o((t-c)^2)$. (Le terme d'ordre 1 est nul car on est en un extremum local).
3. On effectue le changement de variable $u = \sqrt{-x f''(c)} (t-c)$ de sorte que $(t-c)^2 = \frac{u^2}{-x f''(c)}$.
4. En ramenant l'intervalle étendu vers $]-\infty, +\infty[$ pour $x \to +\infty$ (les bords ne contribuant que de manière exponentiellement faible, justifié par domination sur le reste), l'intégrale devient :
   $I(x) \sim e^{x f(c)} g(c) \int_{-\infty}^{+\infty} e^{-u^2 / 2} \frac{1}{\sqrt{-x f''(c)}} du$.
5. L'intégrale de Gauss donne $\sqrt{2\pi}$. Ainsi l'équivalent final est :
   $I(x) \sim e^{x f(c)} g(c) \sqrt{\frac{2\pi}{-x f''(c)}}$.
