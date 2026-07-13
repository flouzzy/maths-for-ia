---
title: "Exercice 7 : Un critère de convergence absolue (Règle de Raabe-Duhamel)"
difficulty: ★★★★☆
---
# Exercice 7 : Un critère de convergence absolue (Règle de Raabe-Duhamel)

## Énoncé
Soit $\sum u_n$ une série à termes strictement positifs. Si $\frac{u_{n+1}}{u_n} = 1 - \frac{\alpha}{n} + o(\frac{1}{n})$ avec $\alpha > 1$, démontrer que la série $\sum u_n$ converge (absolument).

## Correction

1. **Développement de $\ln(u_{n+1}/u_n)$ :**
   $\ln(\frac{u_{n+1}}{u_n}) = \ln(1 - \frac{\alpha}{n} + o(\frac{1}{n})) = -\frac{\alpha}{n} + o(\frac{1}{n})$.
2. **Comparaison avec une série de Riemann :**
   Soit $v_n = \frac{1}{n^\beta}$ avec $1 < \beta < \alpha$.
   $\ln(\frac{v_{n+1}}{v_n}) = \ln((\frac{n}{n+1})^\beta) = -\beta \ln(1 + 1/n) = -\frac{\beta}{n} + o(\frac{1}{n})$.
3. **Comparaison asymptotique :**
   Ainsi, $\ln(\frac{u_{n+1}}{u_n}) - \ln(\frac{v_{n+1}}{v_n}) = \frac{\beta - \alpha}{n} + o(\frac{1}{n})$.
   Comme $\beta < \alpha$, pour $n$ assez grand, $\ln(\frac{u_{n+1}}{u_n}) - \ln(\frac{v_{n+1}}{v_n}) < 0$, ce qui implique que $\ln(\frac{u_{n+1}/v_{n+1}}{u_n/v_n}) < 0$, ou encore $\frac{u_{n+1}}{v_{n+1}} < \frac{u_n}{v_n}$.
4. **Conclusion :**
   La suite $(u_n/v_n)$ est donc décroissante pour $n$ grand. Elle est minorée par 0, donc elle admet une limite, et par conséquent $u_n = O(v_n)$. Puisque la série $\sum v_n$ converge (Riemann, $\beta > 1$), par le théorème de comparaison, la série (positive donc convergente = absolument convergente) $\sum u_n$ converge.
