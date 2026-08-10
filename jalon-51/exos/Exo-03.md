## Exercice 3 : L'espace des suites bornées \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $l^\infty$ l'espace vectoriel des suites réelles bornées $u = (u_n)_{n \in \mathbb{N}}$.
On pose $d(u, v) = \sup_{n \in \mathbb{N}} |u_n - v_n|$.
Montrer que $d$ définit bien une distance sur $l^\infty$.

**Correction :**
L'application $d$ est bien à valeurs dans $\mathbb{R}_+$ car la différence de deux suites bornées est bornée, donc le supremum existe et est fini et positif.
1. **Séparation :**
   Si $d(u, v) = 0$, alors $\sup_{n} |u_n - v_n| = 0$. Puisque $|u_n - v_n| \ge 0$ pour tout $n$, cela impose $\forall n, |u_n - v_n| = 0$, soit $u_n = v_n$. Donc $u = v$.
2. **Symétrie :**
   $d(u, v) = \sup_{n} |u_n - v_n| = \sup_{n} |-(v_n - u_n)| = \sup_{n} |v_n - u_n| = d(v, u)$.
3. **Inégalité triangulaire :**
   Soient $u, v, w \in l^\infty$. Pour tout $n \in \mathbb{N}$ :
   $|u_n - w_n| = |u_n - v_n + v_n - w_n| \le |u_n - v_n| + |v_n - w_n|$.
   Par définition du supremum, $|u_n - v_n| \le d(u, v)$ et $|v_n - w_n| \le d(v, w)$.
   Ainsi, pour tout $n$ :
   $|u_n - w_n| \le d(u, v) + d(v, w)$.
   Puisque cette inégalité est vraie pour tout $n$, le terme de droite est un majorant de l'ensemble $\{|u_n - w_n| \mid n \in \mathbb{N}\}$. Le supremum étant le plus petit des majorants :
   $\sup_{n} |u_n - w_n| \le d(u, v) + d(v, w)$, soit $d(u, w) \le d(u, v) + d(v, w)$. $\blacksquare$
