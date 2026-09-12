# Exercice 4 : Fatou et fonctions non bornées
$\bigstar\bigstar\star\star\star$

## Énoncé
Soit $f_n(x) = n e^{-nx}$ pour $x \in ]0, 1]$.
1. Déterminer la limite simple de $f_n$.
2. Comparer $\int_0^1 (\liminf f_n) dx$ et $\liminf \int_0^1 f_n dx$.
3. Le théorème de convergence dominée s'applique-t-il ici ?

## Correction
**1. Limite simple :**
Pour un $x \in ]0, 1]$ fixé, $x > 0$.
Par croissances comparées de l'exponentielle et des polynômes, on a $\lim_{n \to \infty} n e^{-nx} = 0$.
Donc $f_n$ converge simplement vers la fonction nulle $f = 0$ sur $]0, 1]$.

**2. Comparaison des intégrales :**
- L'intégrale de la limite est nulle : $\int_0^1 0 dx = 0$.
- Pour $f_n$, calculons :
  $\int_0^1 n e^{-nx} dx = \left[ -e^{-nx} \right]_0^1 = -e^{-n} - (-e^0) = 1 - e^{-n}$.
- Donc $\liminf_{n \to \infty} \int_0^1 f_n dx = \lim_{n \to \infty} (1 - e^{-n}) = 1$.

L'inégalité de Fatou s'écrit $0 \leq 1$, ce qui est vrai et strictement vérifié.
Ici, la perte de masse n'est pas due à une fuite vers l'infini spatial (l'espace est borné, $[0,1]$) mais à une concentration de masse vers $0$ (un pic de hauteur $n$ et de largeur $1/n$ autour de $0$).

**3. Convergence dominée :**
Si le théorème de convergence dominée s'appliquait, on aurait l'égalité des limites, ce qui n'est pas le cas ($0 \neq 1$).
En effet, pour tout $x > 0$, le supremum sur $n$ est $\sup_n n e^{-nx}$. La fonction dominante $g(x) = \sup_n f_n(x)$ n'est pas intégrable.
On peut le voir en posant $g_N = \sup_{n \le N} f_n$. La fonction enveloppe explose près de $0$ de telle sorte que son intégrale diverge, empêchant la domination.
