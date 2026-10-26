# Exercice 3
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Dans l'espace des suites réelles sommables $E = \ell^1(\mathbb{N})$, on considère le cône positif $P = \{ u = (u_n)_{n \in \mathbb{N}} \in \ell^1 \mid \forall n, u_n \ge 0 \}$.
Montrer que $P$ est un convexe fermé.
On pose $x_0$ la suite définie par $x_0^{(0)} = -1$ et $x_0^{(n)} = 0$ pour tout $n \ge 1$.
Construire explicitement la forme linéaire continue qui sépare strictement $x_0$ de $P$.

**Correction :**
1. **Convexité et Fermeture de $P$ :**
   Soient $u, v \in P$ et $t \in [0,1]$. Pour tout $n \in \mathbb{N}$, $(tu + (1-t)v)_n = t u_n + (1-t) v_n \ge 0$ car $u_n, v_n, t, (1-t)$ sont tous positifs. Donc $P$ est convexe.
   Pour la fermeture, soit $(u^{(k)})_{k \ge 0}$ une suite d'éléments de $P$ convergeant vers $u \in \ell^1$ pour la norme $\|\cdot\|_1$.
   Pour tout $n$, $|u_n^{(k)} - u_n| \le \|u^{(k)} - u\|_1$. Comme la norme tend vers zéro, la suite des composantes converge : $u_n = \lim_{k \to \infty} u_n^{(k)}$.
   Comme $u_n^{(k)} \ge 0$ pour tout $k$, un passage à la limite donne $u_n \ge 0$. Donc $u \in P$, ce qui prouve que $P$ est fermé.
2. **Disjonction :**
   $x_0^{(0)} = -1 < 0$, donc $x_0 \notin P$. Le point et le convexe fermé sont disjoints.
3. **Construction de la forme linéaire :**
   Le dual topologique de $\ell^1$ s'identifie isométriquement à $\ell^\infty$ (les suites bornées).
   Toute forme linéaire continue $f$ sur $\ell^1$ s'écrit $f(u) = \sum_{n=0}^\infty a_n u_n$ avec $a \in \ell^\infty$.
   Nous voulons $f(x_0) < \alpha \le \inf_{u \in P} f(u)$.
   Évaluons $f(x_0) = a_0 (-1) = -a_0$.
   Pour que $\inf_{u \in P} f(u)$ ne soit pas $-\infty$, il est nécessaire que $a_n \ge 0$ pour tout $n$. En effet, si $a_{n_0} < 0$, en prenant la suite $u \in P$ telle que $u_{n_0} = M$ et $0$ ailleurs, $f(u) = M a_{n_0} \to -\infty$ quand $M \to +\infty$.
   Si on impose $a_n \ge 0$ pour tout $n$, alors $\inf_{u \in P} f(u) = 0$ (atteint en la suite nulle qui est dans $P$).
   Nous voulons donc $-a_0 < 0$, ce qui implique $a_0 > 0$.
   Choisissons simplement la forme linéaire correspondant à la projection sur la première coordonnée : $a = (1, 0, 0, \ldots) \in \ell^\infty$.
   La forme linéaire est $f(u) = u_0$. C'est bien continu.
   Pour tout $u \in P$, $f(u) = u_0 \ge 0$.
   Pour le point $x_0$, $f(x_0) = -1 < 0$.
   L'hyperplan affine $H = \{ u \in \ell^1 \mid u_0 = -1/2 \}$ sépare strictement le cône $P$ et le point $x_0$.
