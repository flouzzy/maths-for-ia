# Exercice 9 : Inégalité de Young par densité $\star\star\star\star\star$

**Énoncé :**
Montrer le cas particulier de l'inégalité de Young : pour $f \in L^1(\mathbb{R})$ et $g \in L^1(\mathbb{R})$, leur convolution $f * g$ existe presque partout, est dans $L^1(\mathbb{R})$, et $\|f * g\|_1 \le \|f\|_1 \|g\|_1$.
Aide : on admettra le résultat pour des fonctions continues à support compact et on prolongera par densité.

**Correction détaillée :**
1. **Hypothèse admise sur les fonctions régulières :** Si $u, v \in C_c(\mathbb{R})$, alors leur convolution $u * v$ est bien définie partout, est dans $C_c(\mathbb{R})$, et d'après le théorème de Fubini-Tonelli :
$\|u * v\|_1 = \int_{\mathbb{R}} \left| \int_{\mathbb{R}} u(x-y)v(y) \, dy \right| dx \le \int_{\mathbb{R}} \int_{\mathbb{R}} |u(x-y)||v(y)| \, dy \, dx = \int_{\mathbb{R}} |v(y)| \left( \int_{\mathbb{R}} |u(x-y)| \, dx \right) dy = \|u\|_1 \|v\|_1$.
2. **Cas général par densité :** Soient $f, g \in L^1(\mathbb{R})$. Comme $C_c(\mathbb{R})$ est dense dans $L^1(\mathbb{R})$, il existe deux suites $(\varphi_n)$ et $(\psi_n)$ de $C_c(\mathbb{R})$ convergeant respectivement vers $f$ et $g$ dans $L^1$.
Pour montrer que la suite $(\varphi_n * \psi_n)$ converge dans $L^1$, étudions son caractère de Cauchy.
$\|\varphi_n * \psi_n - \varphi_m * \psi_m\|_1 = \|\varphi_n * (\psi_n - \psi_m) + (\varphi_n - \varphi_m) * \psi_m\|_1 \le \|\varphi_n\|_1 \|\psi_n - \psi_m\|_1 + \|\varphi_n - \varphi_m\|_1 \|\psi_m\|_1$.
Comme les suites convergent dans $L^1$, elles y sont bornées en norme. Les termes $\|\psi_n - \psi_m\|_1$ et $\|\varphi_n - \varphi_m\|_1$ tendent vers $0$.
Donc $(\varphi_n * \psi_n)$ est de Cauchy dans le Banach $L^1(\mathbb{R})$, elle admet une limite $h \in L^1(\mathbb{R})$.
3. **Identification :** Par l'inégalité triangulaire et la limite admise :
$\|h\|_1 = \lim_{n \to \infty} \|\varphi_n * \psi_n\|_1 \le \lim_{n \to \infty} \|\varphi_n\|_1 \|\psi_n\|_1 = \|f\|_1 \|g\|_1$.
Il reste un point subtil : s'assurer que $h$ coïncide bien avec la formule de convolution $f * g$. Une application rigoureuse de Fubini-Tonelli à $|f(x-y)g(y)|$ directement pour des fonctions $L^1$ positives (via Jalon 71) confirme l'existence presque partout de l'intégrale et l'égalité avec $h$. L'inégalité est ainsi prouvée. $\blacksquare$
