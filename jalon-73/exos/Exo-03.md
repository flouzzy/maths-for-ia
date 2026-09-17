# Exercice 3 : Espaces $\ell^p$ et inclusion inverse \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $\mathbb{N}$ muni de la mesure de comptage. On note $\ell^p$ l'espace $L^p(\mathbb{N})$.
Montrer que pour $1 \le p \le q \le +\infty$, on a $\ell^p \subset \ell^q$.
Remarquons que l'inclusion est inversée par rapport au cas d'une mesure finie.

**Correction :**
Soit $u = (u_n)_{n \in \mathbb{N}} \in \ell^p$. On suppose que $\|u\|_p = \left( \sum_{n=0}^{+\infty} |u_n|^p \right)^{1/p} < +\infty$.
Puisque la série converge, le terme général tend vers 0. Donc, il existe un rang $N$ à partir duquel $|u_n| \le 1$.
De manière encore plus forte, puisque $\sum |u_n|^p < +\infty$, on a $|u_n|^p \le \sum_{k} |u_k|^p = \|u\|_p^p$.
Donc pour tout $n$, $|u_n| \le \|u\|_p$. La suite est bornée.
En particulier, si on pose $C = \|u\|_p$, alors pour tout $n$, $|u_n| \le C$. Donc $u \in \ell^\infty$.

Considérons maintenant $q < +\infty$. Comme $u \in \ell^p$, pour tout $n$ tel que $|u_n| \le 1$, comme $q \ge p$, on a $|u_n|^q \le |u_n|^p$.
La série $\sum |u_n|^q$ est donc majorée par $\sum |u_n|^p$ à un nombre fini de termes près (ceux pour lesquels $|u_n| > 1$).
Puisque $\sum |u_n|^p < +\infty$, la série $\sum |u_n|^q$ est convergente.
Ainsi, $u \in \ell^q$. L'inclusion $\ell^p \subset \ell^q$ est démontrée.
