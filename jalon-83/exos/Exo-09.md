# Exercice 9 : Espace de Sobolev et discontinuités  \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$


## Énoncé
Soit $f \in L^2(\mathbb{R})$.
On rappelle que $f \in H^1(\mathbb{R})$ si et seulement si sa dérivée distributionnelle $f' \in L^2(\mathbb{R})$.
Soit $f$ une fonction de classe $C^1$ par morceaux sur $\mathbb{R}$, à support compact, présentant au moins un saut de hauteur non nulle $\sigma \neq 0$ en un point $a$.
Montrer rigoureusement que $f \notin H^1(\mathbb{R})$.

## Correction
Par la formule des sauts, la dérivée de $f$ au sens des distributions est de la forme :
$$ f' = \{f'\} + \sigma \delta_a + \dots $$
où $\{f'\}$ est la dérivée classique là où elle est définie, et $\sigma \delta_a$ correspond au saut en $a$.
Pour que $f \in H^1(\mathbb{R})$, il faut que la distribution $f'$ soit une "vraie" fonction de $L^2(\mathbb{R})$.
Supposons par l'absurde que $f' \in L^2(\mathbb{R})$. Cela signifie qu'il existe une fonction $g \in L^2(\mathbb{R})$ telle que la distribution $f'$ agit comme $g$ par intégration.
Dans ce cas, l'action de $f'$ sur n'importe quelle fonction test $\phi \in \mathcal{D}(\mathbb{R})$ s'écrirait :
$$ \langle f', \phi \rangle = \int_{\mathbb{R}} g(x)\phi(x)dx $$
Cependant, nous savons que :
$$ \langle f', \phi \rangle = \int_{\mathbb{R}} \{f'\}(x)\phi(x)dx + \sigma \phi(a) + \dots $$
Considérons une suite de fonctions tests $\phi_n \in \mathcal{D}(\mathbb{R})$ telles que $\text{supp}(\phi_n) \subset [a - \frac{1}{n}, a + \frac{1}{n}]$, $0 \le \phi_n(x) \le 1$, et $\phi_n(a) = 1$.
Par le théorème de convergence dominée (ou l'inégalité de Cauchy-Schwarz), comme l'aire sous $\phi_n$ tend vers 0, l'intégrale contre toute fonction $g \in L^2$ tend vers 0 :
$$ \lim_{n \to \infty} \int_{\mathbb{R}} g(x)\phi_n(x)dx = 0 $$
Ainsi que :
$$ \lim_{n \to \infty} \int_{\mathbb{R}} \{f'\}(x)\phi_n(x)dx = 0 $$
Mais de l'autre côté de l'équation des sauts, le terme lié au Dirac reste constant car $\phi_n(a) = 1$ :
$$ \langle f', \phi_n \rangle = \int_{\mathbb{R}} \{f'\}(x)\phi_n(x)dx + \sigma \phi_n(a) \to 0 + \sigma $$
Nous avons alors $0 = \sigma$, ce qui est absurde puisque par hypothèse le saut est non nul ($\sigma \neq 0$).
Par conséquent, aucune fonction $g \in L^2(\mathbb{R})$ ne peut simuler un Dirac. La distribution $f'$ n'appartient donc pas à $L^2(\mathbb{R})$, ce qui implique $f \notin H^1(\mathbb{R})$.
Les fonctions de $H^1(\mathbb{R})$ ne peuvent donc pas avoir de sauts ; elles sont continues (en dimension 1).
