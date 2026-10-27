# Exercice 1 : Opérateurs Multiplication (Bornitude)
$\star\star\star\star\star$
**Énoncé :**
Soit $E = \ell^1(\mathbb{N})$ l'espace des suites absolument sommables muni de la norme $\| x \|_1 = \sum |x_n|$.
Soit $a = (a_n)$ une suite de nombres réels. Pour tout $n \in \mathbb{N}$, on définit $T_n(x) = a_n x_n$.
On suppose que pour tout $x \in E$, la suite $(T_n(x))_{n \in \mathbb{N}}$ est bornée dans $\mathbb{R}$.
Montrer que la suite $(a_n)$ est bornée en utilisant le théorème de Banach-Steinhaus.

**Correction :**
1. Pour chaque $n \in \mathbb{N}$, l'application $T_n : E \to \mathbb{R}$ définie par $T_n(x) = a_n x_n$ est linéaire.
2. Continuité de $T_n$ :
   $|T_n(x)| = |a_n x_n| \le |a_n| |x_n| \le |a_n| \sum_{k=0}^{\infty} |x_k| = |a_n| \|x\|_1$.
   Donc $T_n$ est continu sur $E$, et $\|T_n\|_{\mathcal{L}(E, \mathbb{R})} = |a_n|$. En effet, si $e_n$ est la suite valant $1$ à l'indice $n$ et $0$ ailleurs, on a $\|e_n\|_1 = 1$ et $|T_n(e_n)| = |a_n|$.
3. Hypothèse de bornitude ponctuelle :
   Par hypothèse, pour tout $x \in E$, il existe $M_x > 0$ tel que $\forall n \in \mathbb{N}, |T_n(x)| \le M_x$.
   La famille $(T_n)$ est donc ponctuellement bornée.
4. Application du théorème de Banach-Steinhaus :
   L'espace $E = \ell^1(\mathbb{N})$ est un espace de Banach (complet). Les opérateurs $T_n$ sont linéaires, continus de $E$ vers $\mathbb{R}$ (espace vectoriel normé).
   D'après le théorème de Banach-Steinhaus, la famille des normes $(\|T_n\|)_{n \in \mathbb{N}}$ est bornée.
5. Conclusion :
   Il existe $M > 0$ tel que $\forall n \in \mathbb{N}, \|T_n\| \le M$.
   Or on a vu que $\|T_n\| = |a_n|$.
   Donc $\forall n \in \mathbb{N}, |a_n| \le M$. La suite $(a_n)$ est bien bornée.