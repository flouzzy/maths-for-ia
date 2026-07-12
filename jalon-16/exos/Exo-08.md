# Exercice 08 : Un critère de condensation

## Énoncé
Soit $(u_n)$ une suite décroissante de réels positifs. Démontrer que la série $\sum_{n=1}^\infty u_n$ converge si et seulement si la série condensée $\sum_{k=0}^\infty 2^k u_{2^k}$ converge.

## Correction Détaillée
1. **Introduction et Hypothèses :**
   On suppose $(u_n)$ positive et décroissante. Cela garantit que toutes les sommations et majorations sont légitimes dans $\overline{\mathbb{R}^+}$.
   Soit $S_N = \sum_{n=1}^N u_n$ et $T_K = \sum_{k=0}^K 2^k u_{2^k}$.

2. **Étape 1 : Majoration par la série condensée (Si T converge alors S converge)**
   Regroupons les termes de $S_N$ par paquets de tailles $2^k$.
   Considérons la somme partielle jusqu'à $N < 2^{K+1}-1$ :
   $$S_N \le S_{2^{K+1}-1} = u_1 + (u_2 + u_3) + (u_4 + \dots + u_7) + \dots + (u_{2^K} + \dots + u_{2^{K+1}-1})$$
   Comme la suite est décroissante :
   $u_2 + u_3 \le u_2 + u_2 = 2u_2$
   $u_4 + u_5 + u_6 + u_7 \le 4u_4$
   De manière générale, le k-ième groupe a $2^k$ termes, tous majorés par le premier terme du groupe $u_{2^k}$.
   $$S_{2^{K+1}-1} \le u_1 + 2u_2 + 4u_4 + \dots + 2^K u_{2^K} = \sum_{k=0}^K 2^k u_{2^k} = T_K$$
   Ainsi $S_N \le T_K$. Si $(T_K)$ est majorée (i.e. la série condensée converge), alors $(S_N)$ est majorée. Donc $\sum u_n$ converge.

3. **Étape 2 : Minoration par la série condensée (Si S converge alors T converge)**
   Cette fois, on minore chaque paquet.
   $u_2 + u_3 \ge u_4 + u_4 = 2u_4$
   $u_4 + u_5 + u_6 + u_7 \ge 4u_8$
   $S_N \ge u_1 + u_2 + (u_3 + u_4) + (u_5 + \dots + u_8) \dots$
   En généralisant :
   $$S_{2^K} = u_1 + \sum_{k=0}^{K-1} \sum_{j=2^k+1}^{2^{k+1}} u_j \ge u_1 + \sum_{k=0}^{K-1} 2^k u_{2^{k+1}} = u_1 + \frac{1}{2} \sum_{k=0}^{K-1} 2^{k+1} u_{2^{k+1}}$$
   Posons $m = k+1$ :
   $$S_{2^K} \ge u_1 + \frac{1}{2} \sum_{m=1}^{K} 2^m u_{2^m} = u_1 + \frac{1}{2} (T_K - u_1)$$
   $$T_K \le 2S_{2^K} - u_1$$
   Ainsi, si $(S_N)$ converge (est majorée), alors $(T_K)$ est majorée.

4. **Conclusion :**
   Les deux suites de sommes partielles sont mutuellement bornées l'une par l'autre. Elles ont donc la même nature.
