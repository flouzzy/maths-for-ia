---
uuid: "jalon-20-exo-08"
title: "Exercice 08 : ★★★★☆"
---
# Exercice 08

## Énoncé
Développement asymptotique de la suite $u_n = (1 + \frac{1}{n})^n$. Trouver un équivalent de $u_n - e$.

## Correction
1. Exprimons $u_n$ sous forme exponentielle : $u_n = \exp(n \ln(1 + \frac{1}{n}))$.
2. DL de $\ln(1 + x)$ en 0 : $\ln(1+x) = x - \frac{x^2}{2} + o(x^2)$.
3. Posons $x = \frac{1}{n}$, qui tend vers 0 quand $n \to \infty$ :
   $\ln(1 + \frac{1}{n}) = \frac{1}{n} - \frac{1}{2n^2} + o(\frac{1}{n^2})$.
4. Multiplions par $n$ :
   $n \ln(1 + \frac{1}{n}) = 1 - \frac{1}{2n} + o(\frac{1}{n})$.
5. Passons à l'exponentielle :
   $u_n = \exp(1 - \frac{1}{2n} + o(\frac{1}{n})) = e \cdot \exp(-\frac{1}{2n} + o(\frac{1}{n}))$.
6. DL de $e^X$ en $0$ avec $X = -\frac{1}{2n} + o(\frac{1}{n})$ :
   $e^X = 1 + X + o(X) = 1 - \frac{1}{2n} + o(\frac{1}{n})$.
7. Remplaçons dans $u_n$ :
   $u_n = e \left( 1 - \frac{1}{2n} + o(\frac{1}{n}) \right) = e - \frac{e}{2n} + o(\frac{1}{n})$.
8. L'erreur est $u_n - e = -\frac{e}{2n} + o(\frac{1}{n})$.
9. L'équivalent de $u_n - e$ est donc le premier terme non nul :
   $u_n - e \sim -\frac{e}{2n}$. $\blacksquare$