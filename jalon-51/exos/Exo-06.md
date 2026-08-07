## Exercice 6 : L'espace des fonctions continues et distance de Manhattan \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Sur $E = \mathcal{C}([0, 1], \mathbb{R})$, on pose $d_1(f, g) = \int_0^1 |f(t) - g(t)| dt$.
Démontrer l'axiome de séparation (la difficulté réside dans le fait que l'intégrale d'une fonction positive est nulle).

**Correction :**
Il est évident que si $f=g$, alors $d_1(f,g) = \int_0^1 0 = 0$.
Réciproquement, supposons $d_1(f,g) = 0$. Posons $h(t) = |f(t) - g(t)|$.
La fonction $h$ est continue sur $[0,1]$ et $h(t) \ge 0$ pour tout $t$.
Supposons par l'absurde qu'il existe $t_0 \in [0,1]$ tel que $h(t_0) > 0$. Notons $c = h(t_0)$.
Puisque $h$ est continue, il existe un voisinage ouvert de $t_0$ dans $[0,1]$, disons $[a,b]$ avec $a<b$, sur lequel $h(t) \ge c/2$.
Alors $\int_0^1 h(t) dt \ge \int_a^b h(t) dt \ge \int_a^b \frac{c}{2} dt = (b-a)\frac{c}{2} > 0$.
Cela contredit l'hypothèse $\int_0^1 h(t) dt = 0$.
Donc pour tout $t$, $h(t)=0$, c'est-à-dire $f(t)=g(t)$. L'axiome de séparation est vérifié. $\blacksquare$
