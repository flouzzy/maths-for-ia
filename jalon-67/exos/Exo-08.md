## Exercice 8 : Un contre-exemple (Perte de masse à l'infini) \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Considérons la suite de fonctions $f_n(x) = \frac{1}{n} \chi_{[0, n]}(x)$.
1. Montrer que $f_n(x)$ converge ponctuellement vers 0.
2. La suite $(f_n)$ est-elle croissante ?
3. Calculer $\lim \int f_n$ et comparer à $\int \lim f_n$. Conclure.

**Correction Détaillée :**
1. Fixons $x \in \mathbb{R}$. Si $x < 0$, $f_n(x) = 0$ pour tout $n$. Si $x \ge 0$, pour $n > x$, $f_n(x) = 1/n$. Dans tous les cas, $f_n(x) \to 0$ quand $n \to \infty$. Donc $f = 0$.
2. Regardons la monotonie : $f_n(0) = 1/n$ et $f_{n+1}(0) = 1/(n+1)$. Clairement, $f_{n+1}(0) < f_n(0)$. La suite $(f_n)$ n'est donc **pas** croissante.
3. Calculons l'intégrale : $\int_{\mathbb{R}} f_n(x) dx = \int_0^n \frac{1}{n} dx = \frac{n}{n} = 1$.
   Donc $\lim_{n \to \infty} \int f_n = 1$.
   D'autre part, $\int \lim f_n = \int 0 = 0$.
4. On a $\lim \int f_n \neq \int \lim f_n$. Ceci illustre que si l'hypothèse de croissance est absente, l'interversion est en général fausse (la "masse" s'échappe vers l'infini, un phénomène appelé perte de masse ou défaut de tension).
