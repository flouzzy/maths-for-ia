---
title: "Exercice 10 : Une curiosité sur la constante d'Euler (Niveau X/ENS)"
difficulty: ★★★★★
---
# Exercice 10 : Une curiosité sur la constante d'Euler (Niveau X/ENS)

## Énoncé
Démontrer que la série $\sum_{n=1}^\infty (\frac{1}{n} - \ln(1+\frac{1}{n}))$ converge, et exprimer sa limite en fonction de la constante d'Euler $\gamma$.

## Correction
1. **Développement asymptotique du terme général :**
   $u_n = \frac{1}{n} - \ln(1+\frac{1}{n}) = \frac{1}{n} - (\frac{1}{n} - \frac{1}{2n^2} + o(\frac{1}{n^2})) = \frac{1}{2n^2} + o(\frac{1}{n^2})$.
2. **Convergence :**
   $u_n \sim \frac{1}{2n^2}$. Comme la série de Riemann $\sum \frac{1}{n^2}$ converge, et que $u_n > 0$, la série $\sum u_n$ converge absolument.
3. **Calcul de la somme partielle :**
   $S_N = \sum_{n=1}^N (\frac{1}{n} - (\ln(n+1) - \ln(n)))$.
   $S_N = (\sum_{n=1}^N \frac{1}{n}) - \sum_{n=1}^N (\ln(n+1) - \ln(n))$.
   La deuxième somme est télescopique : $\sum_{n=1}^N (\ln(n+1) - \ln(n)) = \ln(N+1) - \ln(1) = \ln(N+1)$.
   Donc $S_N = (\sum_{n=1}^N \frac{1}{n}) - \ln(N+1)$.
4. **Lien avec la constante d'Euler :**
   Par définition, la constante d'Euler-Mascheroni est $\gamma = \lim_{N\to\infty} ((\sum_{n=1}^N \frac{1}{n}) - \ln(N))$.
   On remarque que $S_N = (\sum_{n=1}^N \frac{1}{n}) - \ln(N) + \ln(N) - \ln(N+1) = ((\sum_{n=1}^N \frac{1}{n}) - \ln(N)) - \ln(1 + 1/N)$.
   Comme $\ln(1+1/N) \to 0$, la limite de $S_N$ est $\gamma - 0 = \gamma$.
5. **Conclusion :** La série converge vers $\gamma$.
