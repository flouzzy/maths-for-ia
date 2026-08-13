### Exercice 5 : Arzelà-Ascoli direct \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $(f_n)$ une suite de fonctions continues de $[0, 1]$ dans $\mathbb{R}$. Supposons que :
- $f_n(0) = 0$ pour tout $n$.
- $\forall n, \forall x,y \in [0,1], |f_n(x) - f_n(y)| \le \sqrt{|x-y|}$.
Montrer que $(f_n)$ admet une sous-suite uniformément convergente.

**Correction :**
Nous allons appliquer le théorème d'Arzelà-Ascoli.
1. **Équicontinuïté :** La condition $|f_n(x) - f_n(y)| \le \sqrt{|x-y|}$ implique que pour $\epsilon > 0$, en choisissant $\delta = \epsilon^2$, si $|x-y| \le \delta$ alors $|f_n(x) - f_n(y)| \le \sqrt{\epsilon^2} = \epsilon$. Ceci est valide indépendamment de $n$, la suite est donc équicontinue.
2. **Bornitude ponctuelle :** Pour tout $x \in [0, 1]$, $|f_n(x)| = |f_n(x) - f_n(0)| \le \sqrt{|x-0|} = \sqrt{x} \le 1$. La suite des valeurs est bornée pour tout $x$.
Les conditions du théorème d'Arzelà-Ascoli sont vérifiées. La famille est relativement compacte pour la convergence uniforme. Il existe donc une sous-suite de $(f_n)$ qui converge uniformément sur $[0, 1]$.
