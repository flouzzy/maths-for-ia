# Exercice 03

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit une substance radioactive composée de noyaux indépendants dont la durée de vie suit une loi exponentielle $\mathcal{E}(\lambda)$. On observe $n$ désintégrations et on note $T_i$ la durée de vie du $i$-ème noyau.
On propose l'estimateur $\hat{\lambda}_n = \frac{n}{\sum_{i=1}^n T_i}$.
Montrer que $\hat{\lambda}_n$ converge presque sûrement vers $\lambda$ lorsque $n$ tend vers l'infini.

**Correction :**
1. Les temps de vie $(T_i)$ sont des variables I.I.D. de loi exponentielle $\mathcal{E}(\lambda)$.
L'espérance d'une loi exponentielle de paramètre $\lambda$ est $\mathbb{E}[T_1] = \frac{1}{\lambda}$.
2. Ces variables sont positives, donc intégrables : $\mathbb{E}[|T_1|] = \frac{1}{\lambda} < +\infty$.
3. D'après la Loi Forte des Grands Nombres, la moyenne empirique $\bar{T}_n = \frac{1}{n} \sum_{i=1}^n T_i$ converge presque sûrement vers $\mathbb{E}[T_1] = \frac{1}{\lambda}$.
Donc, $\mathbb{P}\left(\lim_{n \to \infty} \bar{T}_n = \frac{1}{\lambda}\right) = 1$.
4. L'estimateur proposé est $\hat{\lambda}_n = \frac{1}{\bar{T}_n}$.
La fonction $f(x) = \frac{1}{x}$ est continue sur $]0, +\infty[$.
Comme $\frac{1}{\lambda} > 0$, on peut utiliser la continuité pour composer les limites (presque sûrement) :
$\lim_{n \to \infty} \hat{\lambda}_n = \lim_{n \to \infty} f(\bar{T}_n) = f\left(\frac{1}{\lambda}\right) = \lambda$ presque sûrement.
L'estimateur est donc fortement consistant.
