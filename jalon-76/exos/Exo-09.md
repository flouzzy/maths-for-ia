# Exercice 9 : Espace $L^2$ (★★★★★)

**Énoncé (Théorème de Riesz-Fischer partiel) :**
Soit $(e_n)_{n \ge 1}$ une base hilbertienne de $L^2([0, 1])$. Soit $f \in L^2$. On note $c_n = \langle f, e_n \rangle$ ses coefficients de Fourier généralisés.
Prouver l'inégalité de Bessel : $\sum_{n=1}^\infty |c_n|^2 \le \|f\|^2$.

**Correction Détaillée :**
*Analyse de l'énoncé :* On considère une somme partielle $S_N = \sum_{n=1}^N c_n e_n$. On va utiliser l'orthogonalité de $f - S_N$ avec l'espace engendré par les $e_n$.

*Résolution pas-à-pas :*
Soit $N \ge 1$ un entier. Posons $S_N = \sum_{n=1}^N c_n e_n$.
Évaluons la norme au carré du reste $R_N = f - S_N$ :
$$ 0 \le \|f - S_N\|^2 = \langle f - S_N, f - S_N \rangle $$
$$ = \|f\|^2 - \langle f, S_N \rangle - \langle S_N, f \rangle + \|S_N\|^2 $$

Calculons les termes impliquant $S_N$ :
$$ \langle f, S_N \rangle = \left\langle f, \sum_{n=1}^N c_n e_n \right\rangle = \sum_{n=1}^N \overline{c_n} \langle f, e_n \rangle = \sum_{n=1}^N \overline{c_n} c_n = \sum_{n=1}^N |c_n|^2 $$
Par symétrie hermitienne, $\langle S_N, f \rangle = \sum_{n=1}^N |c_n|^2$.

Pour $\|S_N\|^2$, on utilise le théorème de Pythagore car la famille $(e_n)$ est orthonormale :
$$ \|S_N\|^2 = \left\| \sum_{n=1}^N c_n e_n \right\|^2 = \sum_{n=1}^N \|c_n e_n\|^2 = \sum_{n=1}^N |c_n|^2 \|e_n\|^2 = \sum_{n=1}^N |c_n|^2 $$

En remettant tout dans l'équation de départ :
$$ 0 \le \|f\|^2 - \sum_{n=1}^N |c_n|^2 - \sum_{n=1}^N |c_n|^2 + \sum_{n=1}^N |c_n|^2 $$
$$ 0 \le \|f\|^2 - \sum_{n=1}^N |c_n|^2 $$
$$ \sum_{n=1}^N |c_n|^2 \le \|f\|^2 $$

Cette majoration est vraie pour tout $N$. La suite des sommes partielles (qui est croissante car les termes sont positifs) est majorée, donc elle converge. Par passage à la limite quand $N \to \infty$ :
$$ \sum_{n=1}^\infty |c_n|^2 \le \|f\|^2 $$
Ce qui démontre l'inégalité de Bessel.
