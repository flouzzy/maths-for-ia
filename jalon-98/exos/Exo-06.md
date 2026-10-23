# Exercice 6 : Dualité et isométries
$\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
Soit $E$ un espace vectoriel normé. On définit l'injection canonique $J : E \to E^{**}$ par $J(x)(f) = f(x)$ pour tout $f \in E^*$.
Montrer que $J$ est une isométrie, c'est-à-dire $\|J(x)\|_{E^{**}} = \|x\|_E$.

## Correction Détaillée
Par définition, $\|J(x)\|_{E^{**}} = \sup_{f \in E^*, \|f\| \le 1} |J(x)(f)| = \sup_{\|f\| \le 1} |f(x)|$.
Pour tout $f \in E^*$ tel que $\|f\| \le 1$, on a $|f(x)| \le \|f\| \|x\| \le \|x\|$.
Donc $\|J(x)\|_{E^{**}} \le \|x\|$.
D'autre part, un corollaire direct du théorème de Hahn-Banach assure qu'il existe une forme linéaire $f_0 \in E^*$ telle que $\|f_0\| = 1$ et $f_0(x) = \|x\|$.
Pour ce $f_0$, on a $|f_0(x)| = \|x\|$, ce qui prouve que le supremum est atteint et vaut $\|x\|$.
Conclusion : $\|J(x)\|_{E^{**}} = \|x\|$, $J$ est une isométrie de $E$ dans son bidual. $\blacksquare$
