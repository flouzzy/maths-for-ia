### Exercice 6 : Continuité de l'opérateur de translation dans $L^p$ $\bigstar\bigstar\bigstar$

**Énoncé :** Soit $f \in L^p(\mathbb{R})$ avec $p \in [1, +\infty[$. Pour $h \in \mathbb{R}$, on définit la translation $\tau_h f(x) = f(x-h)$. Montrer que $\lim_{h \to 0} \|\tau_h f - f\|_p = 0$.

**Correction Détaillée :**
*Analyse :* Le résultat est vrai pour les fonctions continues à support compact. L'espace $C_c(\mathbb{R})$ étant dense dans $L^p(\mathbb{R})$, on utilise un argument de densité (inégalité en $\epsilon/3$). On a besoin de Minkowski pour séparer les normes.
*Résolution pas-à-pas :*
1. Soit $\epsilon > 0$. Par densité, il existe $g \in C_c(\mathbb{R})$ telle que $\|f - g\|_p \le \epsilon/3$.
2. On écrit $\tau_h f - f = (\tau_h f - \tau_h g) + (\tau_h g - g) + (g - f)$.
3. On applique l'inégalité de Minkowski :
   $$\|\tau_h f - f\|_p \le \|\tau_h (f - g)\|_p + \|\tau_h g - g\|_p + \|g - f\|_p$$
4. Par invariance de la mesure de Lebesgue par translation, $\|\tau_h (f - g)\|_p = \|f - g\|_p \le \epsilon/3$.
5. On a donc $\|\tau_h f - f\|_p \le 2\epsilon/3 + \|\tau_h g - g\|_p$.
6. La fonction $g$ est continue à support compact, donc uniformément continue (théorème de Heine). Pour $h$ assez petit, $|g(x-h) - g(x)|$ est arbitrairement petit pour tout $x$. De plus, toutes ces fonctions ont leur support contenu dans un compact fixe $K$ pour $|h| \le 1$.
7. Ainsi, $\|\tau_h g - g\|_p^p = \int_K |g(x-h) - g(x)|^p dx \to 0$ quand $h \to 0$ par convergence dominée (ou uniforme).
8. Il existe $\delta > 0$ tel que pour $|h| < \delta$, $\|\tau_h g - g\|_p \le \epsilon/3$.
9. Pour $|h| < \delta$, $\|\tau_h f - f\|_p \le \epsilon$, ce qui prouve la limite.
