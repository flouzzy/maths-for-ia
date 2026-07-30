---
title: "Exercice 5 : Continuité délicate en une borne"
difficulty: "$\star$$\star$$\star$$\circ$$\circ$"
---
# Exercice 5 : Continuité délicate en une borne ($\star$$\star$$\star$$\circ$$\circ$)

**Énoncé :**
Soit la fonction $F(x) = \int_0^{+\infty} \frac{\sin(xt)}{t(1+t^2)} dt$.
1. Montrer que $F$ est bien définie et continue sur $\mathbb{R}$.
2. Étudier la parité de $F$.
3. Est-il possible d'appliquer le théorème de dérivation sous le signe intégral pour $F'(x)$ sur $\mathbb{R}$ entier ?

**Démonstration pas-à-pas :**
1. Pour tout $x \in \mathbb{R}$, on a $|\frac{\sin(xt)}{t}| \le |x|$. En l'infini, $\frac{1}{t(1+t^2)} \sim \frac{1}{t^3}$. La fonction $f(x,t)$ est donc intégrable sur $]0, +\infty[$.
   Pour la continuité, soit $K = [-a, a]$ un segment quelconque. Pour $x \in K$, on a :
   Pour $t \in [0,1]$, $|f(x,t)| \le \frac{|x|t}{t(1+t^2)} \le a$.
   Pour $t > 1$, $|f(x,t)| \le \frac{1}{t^3}$.
   La fonction $\varphi(t) = a \mathbf{1}_{[0,1]} + \frac{1}{t^3} \mathbf{1}_{]1, +\infty[}$ est intégrable, ce qui assure la domination locale sur $\mathbb{R}$ et donc la continuité globale.
2. $F(-x) = \int_0^{+\infty} \frac{\sin(-xt)}{t(1+t^2)} dt = - \int_0^{+\infty} \frac{\sin(xt)}{t(1+t^2)} dt = -F(x)$. $F$ est impaire.
3. Si on dérive formellement sous l'intégrale : $\frac{\partial f}{\partial x} = \frac{\cos(xt)}{1+t^2}$.
   On cherche à dominer $|\frac{\cos(xt)}{1+t^2}| \le \frac{1}{1+t^2}$. Or $\frac{1}{1+t^2}$ est intégrable sur $]0, +\infty[$.
   La domination est même globale sur $\mathbb{R}$. On peut donc affirmer que $F$ est de classe $\mathcal{C}^1$ sur $\mathbb{R}$ entier et $F'(x) = \int_0^{+\infty} \frac{\cos(xt)}{1+t^2} dt$.
