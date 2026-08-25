# Exercice 7 : Lemme d'approximation par troncature

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $f : X \to [0, +\infty]$ mesurable. Démontrer que la suite de fonctions $f_n(x) = \min(f(x), n) \cdot \mathbf{1}_{\{x \in X \mid |x| \leq n\}}$ (sur $\mathbb{R}$) permet d'approcher l'intégrale de $f$, c'est-à-dire que $\lim_{n \to \infty} \int f_n = \int f$.

**Démonstration :**
Considérons la suite de fonctions $(f_n)_{n \in \mathbb{N}}$ définies sur l'espace mesuré $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$.
Ces fonctions sont construites par une double troncature : une troncature en hauteur (par $n$) et une troncature en support (sur $[-n, n]$).
Étudions la monotonie de la suite $(f_n)$. Pour tout $x \in \mathbb{R}$ :
- La hauteur augmente : $\min(f(x), n) \leq \min(f(x), n+1)$.
- Le support s'élargit : $\mathbf{1}_{[-n, n]}(x) \leq \mathbf{1}_{[-n-1, n+1]}(x)$.
Puisque $f$ est à valeurs positives, le produit de ces deux fonctions positives et croissantes donne une suite croissante :
$\forall x \in \mathbb{R}, f_n(x) \leq f_{n+1}(x)$.
Étudions la convergence ponctuelle. Fixons un point $x \in \mathbb{R}$.
Pour $n$ suffisamment grand, spécifiquement pour $n \geq |x|$, le point $x$ appartient à l'intervalle $[-n, n]$, ce qui fixe l'indicatrice à $1$.
Si $f(x) < +\infty$, il existe un rang $N \geq |x|$ tel que $N \geq f(x)$. Pour tout $n \geq N$, $f_n(x) = \min(f(x), n) \cdot 1 = f(x)$.
Si $f(x) = +\infty$, pour tout $n \geq |x|$, $f_n(x) = n \cdot 1 = n$. La limite de $f_n(x)$ est bien $+\infty$.
Dans tous les cas, la suite de fonctions $(f_n)$ converge ponctuellement vers $f$.
Nous sommes en présence d'une suite de fonctions mesurables positives, croissante, convergeant ponctuellement vers $f$.
Les hypothèses du théorème de convergence monotone (Beppo-Levi) sont parfaitement vérifiées.
En appliquant ce théorème, nous inversons la limite et l'intégrale :
$$\lim_{n \to \infty} \int_{\mathbb{R}} f_n \, d\lambda = \int_{\mathbb{R}} \left( \lim_{n \to \infty} f_n \right) \, d\lambda = \int_{\mathbb{R}} f \, d\lambda$$
Cette technique de troncature est fondamentale car elle permet de réduire l'étude d'une fonction arbitraire à celle d'une suite de fonctions bornées et à support compact (ou borné).
