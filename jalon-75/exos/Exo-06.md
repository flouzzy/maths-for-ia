# Exercice 6 : Lemme de Fatou et Complétude
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Montrer que si on n'utilise pas le théorème de convergence monotone, on peut démontrer la complétude de $L^p$ ($1 \le p < \infty$) en utilisant le lemme de Fatou.

**Correction :**
On reprend la preuve avec la série $\sum u_n$ t.q. $\sum \|u_n\|_p < \infty$.
Posons $S_N = \sum_{n=0}^N |u_n|$. On sait que $\|S_N\|_p \le \sum_{n=0}^N \|u_n\|_p \le M$.
Donc $\int S_N^p d\mu \le M^p$.
La suite $(S_N)$ converge simplement partout vers une limite (finie ou infinie) $S = \sum_{n=0}^\infty |u_n|$.
Par le lemme de Fatou appliqué à la suite de fonctions positives $(S_N^p)$ :
$\int \liminf_{N \to \infty} S_N^p d\mu \le \liminf_{N \to \infty} \int S_N^p d\mu$
Puisque $S_N \to S$, $\liminf S_N^p = S^p$.
Donc $\int S^p d\mu \le \liminf_{N} \|S_N\|_p^p \le M^p < +\infty$.
Cela prouve que $S \in L^p$, et en particulier $S < +\infty$ presque partout, ce qui est le nœud central de la preuve de Riesz-Fischer. La complétude découle donc fondamentalement du Lemme de Fatou.
