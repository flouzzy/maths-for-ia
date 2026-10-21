Niveau de difficulté : $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Montrez que la divergence de Kullback-Leibler $D_{KL}(P || Q)$ est toujours positive ou nulle, en utilisant l'inégalité de Jensen. Déduisez-en que $H(P, Q) \ge H(P)$.

**Corrigé :**
La divergence de Kullback-Leibler est définie par :
$$D_{KL}(P || Q) = \sum_{x \in \mathcal{X}} P(x) \log \left(\frac{P(x)}{Q(x)}\right)$$
On peut réécrire cette expression sous la forme d'une espérance :
$$D_{KL}(P || Q) = \mathbb{E}_{X \sim P}\left[ -\log \left(\frac{Q(X)}{P(X)}\right) \right]$$
La fonction $-\log(t)$ est une fonction strictement convexe pour $t > 0$. L'inégalité de Jensen stipule que pour une fonction convexe $\varphi$ et une variable aléatoire $Z$, on a $\mathbb{E}[\varphi(Z)] \ge \varphi(\mathbb{E}[Z])$.
Appliquons cela avec $\varphi(t) = -\log(t)$ et $Z = \frac{Q(X)}{P(X)}$ :
$$D_{KL}(P || Q) = \mathbb{E}_{X \sim P}\left[ -\log \left(\frac{Q(X)}{P(X)}\right) \right] \ge -\log \left( \mathbb{E}_{X \sim P}\left[ \frac{Q(X)}{P(X)} \right] \right)$$
Évaluons l'espérance interne :
$$\mathbb{E}_{X \sim P}\left[ \frac{Q(X)}{P(X)} \right] = \sum_{x \in \mathcal{X}} P(x) \frac{Q(x)}{P(x)} = \sum_{x \in \mathcal{X}} Q(x) = 1$$
En remplaçant cette valeur dans l'inégalité de Jensen, on obtient :
$$D_{KL}(P || Q) \ge -\log(1) = 0$$
Donc $D_{KL}(P || Q) \ge 0$.
Sachant que $H(P, Q) = H(P) + D_{KL}(P || Q)$, il en découle directement que :
$$H(P, Q) \ge H(P)$$
L'égalité est atteinte si et seulement si $P = Q$ presque partout.
