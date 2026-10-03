# Exercice 7 : Continuité de la masse de Dirac
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
Prouver rigoureusement que la forme linéaire définie par $\delta_0 : \varphi \mapsto \varphi(0)$ satisfait la condition de continuité séquentielle sur $\mathcal{D}(\mathbb{R})$.

## Correction Détaillée
1. Il faut montrer que si une suite $(\varphi_n)$ converge vers $0$ dans $\mathcal{D}(\mathbb{R})$, alors la suite de nombres complexes $\langle \delta_0, \varphi_n \rangle$ converge vers 0 dans $\mathbb{C}$.
2. Soit $(\varphi_n)$ une suite convergeant vers $0$ dans $\mathcal{D}(\mathbb{R})$. Par définition de cette topologie, deux conditions sont remplies :
   - (A) Il existe un compact fixe $K$ contenant le support de tous les $\varphi_n$.
   - (B) Pour tout $k \ge 0$, la suite des dérivées $\varphi_n^{(k)}$ converge uniformément vers 0 sur $K$.
3. Evaluons l'action de $\delta_0$ sur $\varphi_n$ :
   $$ \langle \delta_0, \varphi_n \rangle = \varphi_n(0) $$
4. Nous devons prouver que $\varphi_n(0) \to 0$ lorsque $n \to +\infty$.
5. Utilisons la condition (B) avec $k = 0$ (la fonction elle-même). La convergence uniforme sur $K$ implique que :
   $$ \lim_{n \to \infty} \sup_{x \in K} |\varphi_n(x)| = 0 $$
6. Or, $| \varphi_n(0) | \le \sup_{x \in K} |\varphi_n(x)|$. (Même si $0 \notin K$, alors $\varphi_n(0) = 0$ et l'inégalité est vérifiée trivialement).
7. Par le théorème d'encadrement (gendarmes), puisque la norme infinie de la suite tend vers 0, on a inéluctablement :
   $$ \lim_{n \to \infty} |\varphi_n(0)| = 0 $$
8. Par conséquent, $\lim_{n \to \infty} \langle \delta_0, \varphi_n \rangle = 0$. La forme linéaire $\delta_0$ est bien continue, c'est une authentique distribution.
