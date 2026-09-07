# Exercice 8 : La formule de l'aire sous une limite de fonctions étagées

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $f : [0, 1] \to \mathbb{R}^+$ une fonction mesurable. On définit une suite de fonctions simples (étagées) approchant $f$ par le bas de manière canonique (méthode de Lebesgue) :
$$f_n(x) = \sum_{k=0}^{n 2^n - 1} \frac{k}{2^n} \mathbf{1}_{\{ \frac{k}{2^n} \le f(x) < \frac{k+1}{2^n} \}}(x) + n \mathbf{1}_{\{ f(x) \ge n \}}(x)$$
Montrer que $(f_n)$ est une suite croissante qui converge simplement vers $f$, et conclure que $\int f = \lim \int f_n$.

**Solution Détaillée :**
1. **Croissance de la suite :**
Pour passer de $f_n$ à $f_{n+1}$, on double la résolution : chaque intervalle $[\frac{k}{2^n}, \frac{k+1}{2^n}[$ de longueur $\frac{1}{2^n}$ est subdivisé en deux intervalles de longueur $\frac{1}{2^{n+1}}$.
Si $f(x)$ tombe dans l'intervalle original, $f_n(x)$ prenait la valeur plancher $\frac{k}{2^n}$.
Dans $f_{n+1}$, la valeur plancher sera soit $\frac{2k}{2^{n+1}} = \frac{k}{2^n}$ (si $f(x)$ est dans la première moitié), soit $\frac{2k+1}{2^{n+1}} > \frac{k}{2^n}$ (si dans la seconde moitié).
Dans tous les cas, $f_{n+1}(x) \ge f_n(x)$.
Pour le seuillage supérieur : on coupe l'excédent au-dessus de $n$. Dans $f_{n+1}$, ce plafond passe à $n+1 > n$, préservant la croissance. Donc $(f_n)$ est croissante positive.

2. **Convergence simple :**
- Si $f(x) < +\infty$, il existe $N$ tel que $n \ge N \implies f(x) < n$. Pour ces $n$, le terme de seuillage est nul. Par définition des sous-intervalles, $f_n(x) \le f(x) < f_n(x) + \frac{1}{2^n}$. En faisant tendre $n \to \infty$, $f_n(x) \to f(x)$.
- Si $f(x) = +\infty$, alors $f_n(x) = n \to +\infty$.

3. **Application du TCM :**
Puisque $(f_n)$ est une suite croissante de fonctions mesurables positives convergeant vers $f$, le théorème de Beppo Levi garantit que :
$$\int f d\mu = \lim_{n \to \infty} \int f_n d\mu$$
Cela montre la consistance de la construction canonique de l'intégrale de Lebesgue via des fonctions simples : le supremum sur l'ensemble abstrait de toutes les fonctions simples minorantes est en réalité atteint par la limite de cette suite explicite particulièrement bien choisie.
