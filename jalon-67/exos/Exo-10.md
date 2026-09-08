# Exercice 10 : Preuve de complétude des espaces $L^1$ via Beppo-Levi

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Utiliser le théorème de convergence monotone pour prouver le théorème de Riesz-Fischer : l'espace $L^1(\mu)$ est un espace de Banach (complet).

## Démonstration rigoureuse pas à pas

Soit $(f_n)$ une suite de Cauchy dans $L^1$. Il existe une sous-suite $(f_{\phi(k)})$ telle que $\| f_{\phi(k+1)} - f_{\phi(k)} \|_1 \le 2^{-k}$. Posons $g_k = |f_{\phi(k+1)} - f_{\phi(k)}|$ et $g = \sum_{k=1}^\infty g_k$. Les sommes partielles $S_N = \sum_{k=1}^N g_k$ forment une suite croissante de fonctions positives. Par Beppo-Levi, $\int \lim S_N d\mu = \lim \int S_N d\mu \le \sum 2^{-k} = 1$. Donc $g \in L^1$, et $g$ est finie presque partout. Cela implique que la série de terme général $f_{\phi(k+1)} - f_{\phi(k)}$ converge p.p., donc la sous-suite $(f_{\phi(k)})$ converge p.p. vers une limite $f$. Par le Lemme de Fatou (conséquence de Beppo-Levi), on montre ensuite que $f_n$ converge vers $f$ dans $L^1$, prouvant la complétude.
