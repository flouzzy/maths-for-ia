# Exercice 9 : Généralisation : Contraction de Rakotch-Boyd
**Niveau :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $(X, d)$ un espace complet. Soit $\phi : [0, \infty[ \to [0, \infty[$ une fonction croissante, continue à droite, avec $\phi(t) < t$ pour $t > 0$.
Si $f$ vérifie $d(f(x), f(y)) \leq \phi(d(x, y))$, prouver que $f$ a un point fixe unique.

**Démonstration pas à pas :**
1. Pour l'unicité, si $x^*, y^*$ sont des points fixes, et $d = d(x^*, y^*) > 0$, alors $d \leq \phi(d) < d$, contradiction.
2. Posons $u_n = d(x_n, x_{n+1})$. $u_n = d(f(x_{n-1}), f(x_n)) \leq \phi(u_{n-1}) < u_{n-1}$. La suite $(u_n)$ est décroissante, minorée par 0, elle converge vers $L \ge 0$.
3. Par continuité à droite de $\phi$, $L = \lim u_n \leq \lim \phi(u_{n-1}) = \phi(L)$. Si $L > 0$, $\phi(L) < L$, contradiction, donc $L=0$.
4. Pour montrer que c'est de Cauchy, supposons le contraire. Il existerait $\epsilon > 0$ et des indices $m_k > n_k \ge k$ tels que $d(x_{m_k}, x_{n_k}) \ge \epsilon$. On peut choisir $m_k$ minimal, de sorte que $d(x_{m_k-1}, x_{n_k}) < \epsilon$.
5. $d(x_{m_k}, x_{n_k}) \leq d(x_{m_k}, x_{m_k-1}) + d(x_{m_k-1}, x_{n_k}) \leq u_{m_k-1} + \epsilon \to \epsilon$.
   Par ailleurs, $d(x_{m_k}, x_{n_k}) \leq d(x_{m_k}, x_{m_k+1}) + d(x_{m_k+1}, x_{n_k+1}) + d(x_{n_k+1}, x_{n_k})$.
   En passant à la limite $k \to \infty$, on obtiendrait $\epsilon \leq 0 + \phi(\epsilon) + 0 = \phi(\epsilon) < \epsilon$.
   Ceci est une contradiction formelle.
6. La suite $(x_n)$ est de Cauchy, et par le même raisonnement que précédemment (continuité de $f$), la limite est l'unique point fixe.
