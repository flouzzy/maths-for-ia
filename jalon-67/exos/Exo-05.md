# Exercice 5 : Densité et série

**Difficulté :** $\bigstar\star$

**Énoncé :**
Soit $f$ mesurable positive. Montrer que $\int_0^\infty f(x) dx = \sum_{n=0}^\infty \int_n^{n+1} f(x) dx$.

**Correction :**
Posons $u_n(x) = f(x) \mathbb{I}_{[n, n+1[}(x)$. Les $u_n$ sont positives et $f(x) = \sum_{n=0}^\infty u_n(x)$ pour tout $x \ge 0$. Par le corollaire du TCM sur les séries à termes positifs (ou en posant $S_N = \sum_0^N u_n$ qui croît vers $f$), $\int \sum u_n = \sum \int u_n$. Donc $\int_0^\infty f(x) dx = \sum_{n=0}^\infty \int_{[n, n+1[} f(x) dx$. $\blacksquare$
