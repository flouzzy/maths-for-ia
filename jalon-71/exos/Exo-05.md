## Exercice 5 : L'intégrale de Dirichlet et l'interversion \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
On veut calculer $I = \int_0^{+\infty} \frac{\sin x}{x} dx$. On utilisera l'identité $\frac{1}{x} = \int_0^{+\infty} e^{-xy} dy$ (pour $x > 0$).

**Correction :**
1. Remplaçons $1/x$ par son expression intégrale :
   $$ I = \int_0^{+\infty} \sin x \left( \int_0^{+\infty} e^{-xy} dy \right) dx = \int_0^{+\infty} \int_0^{+\infty} \sin(x) e^{-xy} dy dx $$
2. Attention, la fonction $f(x, y) = \sin(x) e^{-xy}$ n'est pas de signe constant. Vérifions si elle est Lebesgue-intégrable sur $\mathbb{R}_+^2$ pour appliquer Fubini.
   $$ \iint |f(x,y)| dx dy = \int_0^{+\infty} \left( \int_0^{+\infty} |\sin x| e^{-xy} dy \right) dx = \int_0^{+\infty} |\sin x| \left[ \frac{e^{-xy}}{-x} \right]_0^{+\infty} dx = \int_0^{+\infty} \frac{|\sin x|}{x} dx $$
   Or, on sait que l'intégrale de $|\sin x|/x$ diverge en l'infini. $f$ **n'est pas** intégrable sur le produit ! Fubini usuel échoue.
3. *Astuce :* On tronque le domaine. On calcule d'abord $I_R = \int_0^R \frac{\sin x}{x} dx$.
   $$ I_R = \int_0^R \left( \int_0^{+\infty} \sin(x) e^{-xy} dy \right) dx $$
   Sur $[0, R] \times [0, +\infty[$, la fonction est intégrable (car l'intégrale de la valeur absolue est bornée par $\int_0^R 1/x$ non wait, $|\sin x|/x$ est intégrable sur le segment fini).
4. Fubini s'applique sur ce domaine tronqué :
   $$ I_R = \int_0^{+\infty} \left( \int_0^R \sin(x) e^{-xy} dx \right) dy $$
5. Calculons $J(y) = \int_0^R \sin(x) e^{-xy} dx$ (par double IPP ou en utilisant la partie imaginaire de $\int e^{ix} e^{-xy} dx$) :
   $$ \int_0^R e^{(i-y)x} dx = \left[ \frac{e^{(i-y)x}}{i-y} \right]_0^R = \frac{e^{-yR}e^{iR} - 1}{i-y} = \frac{(e^{-yR}\cos R - 1) + i e^{-yR}\sin R}{-y - i} $$
   En multipliant par le conjugué $-y+i$ au numérateur et dénominateur $y^2+1$, on isole la partie imaginaire, puis on prend la limite $R \to \infty$ en utilisant le théorème de convergence dominée pour conclure.
