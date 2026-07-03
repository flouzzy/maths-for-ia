---
title: "Exercice 3 : Théorème de réarrangement de Riemann (cas particulier)"
difficulty: ★★☆☆☆
---
# Exercice 3 : Théorème de réarrangement de Riemann (cas particulier)

## Énoncé
Soit la série harmonique alternée $\sum_{n=1}^\infty \frac{(-1)^{n+1}}{n}$, dont on sait qu'elle converge vers $\ln(2)$.
En réarrangeant les termes pour prendre deux termes positifs puis un terme négatif ($1 + \frac{1}{3} - \frac{1}{2} + \frac{1}{5} + \frac{1}{7} - \frac{1}{4} + \dots$), démontrer rigoureusement que la nouvelle série converge vers une limite différente (précisément $\frac{3}{2}\ln(2)$).

## Correction
Soit $S$ la somme de la série harmonique alternée : $S = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \frac{1}{6} + \dots = \ln(2)$.
1. On considère la demi-série $S/2 = \frac{1}{2} - \frac{1}{4} + \frac{1}{6} - \frac{1}{8} + \frac{1}{10} - \frac{1}{12} + \dots$.
2. On insère des zéros entre chaque terme de cette série modifiée : $0 + \frac{1}{2} + 0 - \frac{1}{4} + 0 + \frac{1}{6} + 0 - \frac{1}{8} + \dots$.
Cette nouvelle série converge évidemment vers $S/2 = \frac{1}{2}\ln(2)$.
3. On additionne terme à terme la série harmonique alternée initiale et cette nouvelle série (ce qui est justifié puisque les deux convergent) :
   Terme 1 : $1 + 0 = 1$
   Terme 2 : $-\frac{1}{2} + \frac{1}{2} = 0$
   Terme 3 : $\frac{1}{3} + 0 = \frac{1}{3}$
   Terme 4 : $-\frac{1}{4} - \frac{1}{4} = -\frac{1}{2}$
   Terme 5 : $\frac{1}{5} + 0 = \frac{1}{5}$
   Terme 6 : $-\frac{1}{6} + \frac{1}{6} = 0$
   Terme 7 : $\frac{1}{7} + 0 = \frac{1}{7}$
   Terme 8 : $-\frac{1}{8} - \frac{1}{8} = -\frac{1}{4}$
4. En omettant les zéros (ce qui ne change pas la convergence ni la limite), on obtient la série :
   $1 + \frac{1}{3} - \frac{1}{2} + \frac{1}{5} + \frac{1}{7} - \frac{1}{4} + \dots$
   qui est exactement le réarrangement de l'énoncé. La somme de cette nouvelle série est donc $S + S/2 = \frac{3}{2}S = \frac{3}{2}\ln(2)$.
5. **Conclusion :** Un réarrangement des termes d'une série semi-convergente modifie sa somme (ou peut la faire diverger), illustrant que l'associativité et la commutativité infinies requièrent la convergence absolue.
