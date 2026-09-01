# Exercice 8 : Intégration terme à terme

**Difficulté :** $\bigstar\bigstar\bigstar\star$

**Énoncé :**
Montrer que $\int_0^1 \frac{x \ln(x)}{1-x} dx = - \sum_{n=1}^\infty \frac{1}{(n+1)^2}$.

**Correction :**
Posons $f(x) = \frac{-x \ln(x)}{1-x}$. Sur $]0,1[$, $f(x) \ge 0$. On a $\frac{1}{1-x} = \sum_{n=0}^\infty x^n$. Donc $f(x) = \sum_{n=0}^\infty -x^{n+1} \ln(x)$. C'est une série de fonctions positives (car $\ln(x)<0$). Par Beppo Levi, $\int_0^1 f(x)dx = \sum_{n=0}^\infty \int_0^1 -x^{n+1} \ln(x) dx$. Une IPP donne $\int_0^1 x^k \ln(x) dx = -\frac{1}{(k+1)^2}$. Donc l'intégrale vaut $\sum_{n=0}^\infty \frac{1}{(n+2)^2} = \sum_{k=1}^\infty \frac{1}{(k+1)^2}$. (La série finale converge). $\blacksquare$
