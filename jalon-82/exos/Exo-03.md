# Exercice 3 : Valeur principale de Cauchy : Une distribution singulière d'ordre 1
Difficulté : $\bigstar\bigstar\star\star\star$

**Énoncé :**
La fonction $x \mapsto 1/x$ n'est pas localement intégrable autour de 0 (son intégrale diverge logarithmiquement). On ne peut donc pas définir de distribution régulière directement.
On définit la valeur principale de Cauchy, notée $\text{vp}(1/x)$, par son action sur une fonction test $\varphi \in \mathcal{D}(\mathbb{R})$ :
$$ \langle \text{vp}(1/x), \varphi \rangle = \lim_{\epsilon \to 0^+} \int_{|x| > \epsilon} \frac{\varphi(x)}{x} dx $$
Montrez que cette limite existe bien pour toute $\varphi \in \mathcal{D}(\mathbb{R})$ en utilisant le théorème des accroissements finis ou le développement de Taylor de $\varphi$ en 0.

**Correction Détaillée :**
1. **Isoler la singularité :**
   On fixe une fonction test $\varphi \in \mathcal{D}(\mathbb{R})$ dont le support est inclus dans un compact $[-R, R]$.
   L'intégrale s'écrit pour $\epsilon > 0$ :
   $$ I_\epsilon = \int_{-R}^{-\epsilon} \frac{\varphi(x)}{x} dx + \int_{\epsilon}^{R} \frac{\varphi(x)}{x} dx $$
   En effectuant le changement de variable $x \to -x$ dans la première intégrale :
   $$ \int_{-R}^{-\epsilon} \frac{\varphi(x)}{x} dx = \int_{\epsilon}^{R} \frac{\varphi(-x)}{-x} dx = -\int_{\epsilon}^{R} \frac{\varphi(-x)}{x} dx $$

2. **Regrouper les termes :**
   L'intégrale globale devient :
   $$ I_\epsilon = \int_{\epsilon}^{R} \frac{\varphi(x) - \varphi(-x)}{x} dx $$

3. **Analyse du numérateur au voisinage de 0 :**
   La fonction $\varphi$ est indéfiniment dérivable. Appliquons la formule de Taylor-Lagrange autour de 0 à l'ordre 1 pour $\varphi(x)$ et $\varphi(-x)$ :
   $\varphi(x) = \varphi(0) + x\varphi'(0) + x^2 R_1(x)$
   $\varphi(-x) = \varphi(0) - x\varphi'(0) + x^2 R_2(x)$
   où $R_1, R_2$ sont des fonctions bornées sur le compact $[-R, R]$.

   La différence s'écrit :
   $\varphi(x) - \varphi(-x) = 2x\varphi'(0) + x^2 (R_1(x) - R_2(x))$

4. **Majoration de l'intégrande :**
   Soit $g(x) = \frac{\varphi(x) - \varphi(-x)}{x}$.
   Pour $x \neq 0$, $g(x) = 2\varphi'(0) + x(R_1(x) - R_2(x))$.
   Comme $\varphi \in C^\infty$, par le théorème des accroissements finis, il existe $c \in ]-x, x[$ tel que $\varphi(x) - \varphi(-x) = 2x\varphi'(c)$.
   Donc $|g(x)| = 2|\varphi'(c)| \le 2\sup_{t \in [-R,R]} |\varphi'(t)|$.
   La fonction $g(x)$ est donc prolongable par continuité en 0 et elle est bornée sur le compact $[0, R]$.

5. **Conclusion sur la limite :**
   Puisque l'intégrande $g(x)$ est bornée et continue par morceaux sur $[0, R]$, l'intégrale de Riemann sur $[0, R]$ est bien définie.
   Par conséquent, la limite quand $\epsilon \to 0$ existe et vaut :
   $$ \lim_{\epsilon \to 0^+} \int_{\epsilon}^{R} \frac{\varphi(x) - \varphi(-x)}{x} dx = \int_{0}^{R} \frac{\varphi(x) - \varphi(-x)}{x} dx $$
   Cette limite est un nombre fini bien défini pour toute fonction test. La distribution $\text{vp}(1/x)$ est donc bien définie.
