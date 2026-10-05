# Exercice 3 : Distribution engendrée par la fonction signe
**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé
Soit $sgn(x)$ la fonction signe, définie par $sgn(x) = 1$ si $x > 0$, $-1$ si $x < 0$, et $0$ si $x = 0$. Montrer que $sgn \in L^1_{loc}(\mathbb{R})$ et exprimer son action sur $\varphi \in \mathcal{D}(\mathbb{R})$.

## Correction Détaillée
1. Montrons d'abord que $sgn$ est localement intégrable. Soit $K = [a, b]$ un compact arbitraire de $\mathbb{R}$.
2. L'intégrale de la valeur absolue sur ce compact est :
   $$ \int_a^b |sgn(x)| \,dx $$
3. Puisque $|sgn(x)| = 1$ pour tout $x \neq 0$ (qui est un ensemble de mesure nulle), l'intégrale devient :
   $$ \int_a^b 1 \,dx = b - a $$
4. Comme $b - a < +\infty$, l'intégrale est finie sur tout compact, donc $sgn \in L^1_{loc}(\mathbb{R})$.
5. $sgn$ définit par conséquent une distribution régulière $T_{sgn}$. Son action sur une fonction test $\varphi$ est :
   $$ \langle T_{sgn}, \varphi \rangle = \int_{\mathbb{R}} sgn(x)\varphi(x) \,dx $$
6. L'intégrale sur $\mathbb{R}$ se coupe en deux parties (car $sgn$ change de valeur en 0) :
   $$ \int_{\mathbb{R}} sgn(x)\varphi(x) \,dx = \int_{-\infty}^{0} (-1)\varphi(x) \,dx + \int_{0}^{+\infty} (1)\varphi(x) \,dx $$
7. On obtient finalement l'expression :
   $$ \langle T_{sgn}, \varphi \rangle = \int_{0}^{+\infty} \varphi(x) \,dx - \int_{-\infty}^{0} \varphi(x) \,dx $$
