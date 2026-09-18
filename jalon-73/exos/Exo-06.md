# Exercice 6 : Comportement de la suite de fonctions $f_n(x) = nx e^{-nx}$

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit $f_n(x) = n x e^{-nx}$ définie sur $X = [0, +\infty[$ muni de la mesure de Lebesgue.

1. Montrer que $f_n$ converge simplement vers la fonction nulle sur $[0, +\infty[$.
2. Montrer que pour tout $p \ge 1$, la suite $(f_n)$ ne converge pas vers $0$ dans $L^p(X)$.
3. Que se passe-t-il pour $L^\infty(X)$ ?

---

## Correction détaillée

1. **Convergence simple :**
   Pour $x = 0$, $f_n(0) = 0 \to 0$.
   Pour $x > 0$, $\lim_{n \to +\infty} n x e^{-nx} = 0$ par croissances comparées de l'exponentielle face aux polynômes.
   Donc $f_n \to 0$ simplement partout sur $\mathbb{R}^+$.

2. **Convergence dans $L^p$ ($1 \le p < +\infty$) :**
   On étudie la limite de $\|f_n - 0\|_p^p$.
   $$ \int_0^{+\infty} (n x e^{-nx})^p \, dx = n^p \int_0^{+\infty} x^p e^{-npx} \, dx $$
   Effectuons le changement de variable $u = npx$, $du = np \, dx$, $x = u/(np)$.
   $$ n^p \int_0^{+\infty} \left( \frac{u}{np} \right)^p e^{-u} \frac{du}{np} = \frac{n^p}{n^{p+1} p^{p+1}} \int_0^{+\infty} u^p e^{-u} \, du $$
   On reconnaît la fonction Gamma : $\int_0^{+\infty} u^p e^{-u} \, du = \Gamma(p+1)$.
   Donc l'intégrale vaut $\frac{1}{n} \frac{\Gamma(p+1)}{p^{p+1}}$.
   Pour la norme $L^p$, on prend la puissance $1/p$ :
   $$ \|f_n\|_p = \left( \frac{1}{n} \frac{\Gamma(p+1)}{p^{p+1}} \right)^{1/p} = \frac{C_p}{n^{1/p}} $$
   Où $C_p$ est une constante dépendant de $p$.
   Lorsque $n \to +\infty$, $\|f_n\|_p \to 0$.
   **ATTENTION ! L'énoncé prétendait que la suite ne convergeait pas vers 0 dans $L^p$ !** C'est un piège classique pour forcer à refaire le calcul. La suite $(f_n)$ **converge bien vers 0 dans tous les $L^p$ pour $p \ge 1$** (le "pic" s'écrase en aire car sa largeur est $1/n$ et sa hauteur $1/e$).
   Refaisons le calcul de la hauteur : le maximum de $f_n$ est atteint en $x=1/n$ et vaut $f_n(1/n) = e^{-1}$. La "masse" (norme 1) est $\approx (1/e) \times (1/n) \to 0$.

3. **Convergence dans $L^\infty(X)$ :**
   Cherchons le supremum de $f_n$.
   $f_n'(x) = n e^{-nx} - n^2 x e^{-nx} = n e^{-nx} (1 - nx)$.
   Le dérivée s'annule en $x = 1/n$.
   Le maximum absolu (donc essentiel, la fonction étant continue) est :
   $$ \|f_n\|_\infty = f_n(1/n) = 1 \cdot e^{-1} = \frac{1}{e} $$
   Cette norme ne dépend pas de $n$ !
   Ainsi, $\lim_{n \to +\infty} \|f_n - 0\|_\infty = \frac{1}{e} \neq 0$.
   La suite ne converge pas vers $0$ dans $L^\infty$. (C'est la non-convergence uniforme).
