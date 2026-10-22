# Exercice 3

**Difficulté :** $\star\star\star\☆☆$

**Énoncé :**
Montrer que l'espace $c_0$ des suites réelles qui convergent vers 0, muni de la norme $\|u\|_\infty = \sup_{n \in \mathbb{N}} |u_n|$, est un sous-espace fermé de l'espace de Banach $\ell^\infty$ des suites bornées, et par suite, est lui-même un espace de Banach.

**Correction Détaillée :**
1. **Sous-espace vectoriel :** L'ensemble $c_0$ est un sous-espace vectoriel de $\ell^\infty$. En effet, la suite nulle converge vers 0. Si $(u_n)$ et $(v_n)$ convergent vers 0, toute combinaison linéaire $(\alpha u_n + \beta v_n)$ converge aussi vers 0 par les propriétés usuelles des limites. Toute suite convergente étant bornée, $c_0 \subset \ell^\infty$.
2. **Fermeture :** Soit $(u^{(k)})_{k \in \mathbb{N}}$ une suite d'éléments de $c_0$ qui converge vers une limite $u \in \ell^\infty$ pour la norme $\|\cdot\|_\infty$. Il s'agit de montrer que $u \in c_0$, c'est-à-dire que $\lim_{n \to \infty} u_n = 0$.
3. Fixons $\varepsilon > 0$. Puisque $u^{(k)} \to u$ dans $\ell^\infty$, il existe un entier $K$ tel que $\|u^{(K)} - u\|_\infty < \frac{\varepsilon}{2}$.
4. Ceci implique que pour tout indice $n \in \mathbb{N}$, on a $|u_n^{(K)} - u_n| \le \|u^{(K)} - u\|_\infty < \frac{\varepsilon}{2}$.
5. Or, la suite particulière $u^{(K)}$ appartient à $c_0$, ce qui signifie que $\lim_{n \to \infty} u_n^{(K)} = 0$. Il existe donc un rang $N$ tel que pour tout $n \ge N$, $|u_n^{(K)}| < \frac{\varepsilon}{2}$.
6. Considérons un entier $n \ge N$. En utilisant l'inégalité triangulaire, nous pouvons majorer $|u_n|$ :
   $$ |u_n| = |u_n - u_n^{(K)} + u_n^{(K)}| \le |u_n - u_n^{(K)}| + |u_n^{(K)}| $$
7. En substituant les majorations obtenues aux étapes 4 et 5 :
   $$ |u_n| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon. $$
8. Nous avons montré que pour tout $\varepsilon > 0$, il existe un rang $N$ tel que $n \ge N \implies |u_n| < \varepsilon$. Donc la suite $u$ converge vers 0, c'est-à-dire $u \in c_0$.
9. **Conclusion :** L'espace $c_0$ est un fermé du sous-espace métrique complet $\ell^\infty$. Or, tout sous-espace fermé d'un espace de Banach est complet. Ainsi, $c_0$ est un espace de Banach.
