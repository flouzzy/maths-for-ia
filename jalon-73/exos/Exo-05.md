# Exercice 5 : Calcul explicite de la norme $L^\infty$ \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f : \mathbb{R} \to \mathbb{R}$ définie par $f(x) = e^{-|x|} + 10 \cdot 1_{\{0\}}(x) + 5 \cdot 1_{\mathbb{Q} \cap [1, 2]}(x)$.
Calculer la norme $\|f\|_\infty$ dans l'espace $L^\infty(\mathbb{R}, \lambda)$.

**Correction :**
La norme essentielle supremum est définie par :
$\|f\|_\infty = \inf \{ C \ge 0 \mid \lambda(\{x \in \mathbb{R} \mid |f(x)| > C\}) = 0 \}$.

Analysons les termes de $f$ :
- $g(x) = e^{-|x|}$ est continue et son maximum est atteint en $x=0$, $g(0) = 1$. Son supremum est $1$.
- Le terme $10 \cdot 1_{\{0\}}(x)$ ne modifie $f$ qu'en un seul point $x=0$, ce qui est un ensemble de mesure nulle ($\lambda(\{0\}) = 0$).
- Le terme $5 \cdot 1_{\mathbb{Q} \cap [1, 2]}(x)$ ne modifie $f$ que sur un sous-ensemble des rationnels, qui est également dénombrable et de mesure nulle.

Donc, $f(x) = e^{-|x|}$ presque partout (sur $\mathbb{R} \setminus ( \{0\} \cup (\mathbb{Q} \cap [1,2]) )$).
Le supremum essentiel de $f$ est donc le supremum de $g(x) = e^{-|x|}$ sur l'ensemble où ils coïncident.
Puisque $g$ est continue et bornée par $1$, et atteint des valeurs arbitrairement proches de 1 (par exemple pour $x \to 0$, $x \neq 0$), on a $\|f\|_\infty = 1$.

Les pics isolés (en 0 et sur les rationnels) n'affectent pas la norme $L^\infty$ grâce au passage au quotient.
