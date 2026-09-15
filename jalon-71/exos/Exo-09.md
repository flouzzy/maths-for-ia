## Exercice 9 : Produit de Convolution (Fubini) \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soient $f, g \in L^1(\mathbb{R})$. Le produit de convolution est $(f * g)(x) = \int_{\mathbb{R}} f(x-y)g(y) dy$.
Montrer que $f * g \in L^1(\mathbb{R})$ et que $\|f * g\|_{L^1} \le \|f\|_{L^1} \|g\|_{L^1}$.

**Correction :**
1. Calculons la norme $L^1$ de $f * g$ :
   $$ \|f * g\|_{L^1} = \int_{\mathbb{R}} |(f * g)(x)| dx = \int_{\mathbb{R}} \left| \int_{\mathbb{R}} f(x-y)g(y) dy \right| dx $$
2. Par l'inégalité triangulaire (l'intégrale de la valeur absolue majore la valeur absolue de l'intégrale) :
   $$ \|f * g\|_{L^1} \le \int_{\mathbb{R}} \left( \int_{\mathbb{R}} |f(x-y)| |g(y)| dy \right) dx $$
3. La fonction $F(x, y) = |f(x-y)| |g(y)|$ est positive. On peut utiliser le théorème de Tonelli pour intervertir l'ordre :
   $$ \int_{\mathbb{R}} \left( \int_{\mathbb{R}} |f(x-y)| |g(y)| dy \right) dx = \int_{\mathbb{R}} \left( \int_{\mathbb{R}} |f(x-y)| |g(y)| dx \right) dy $$
4. Factorisons le terme $|g(y)|$ qui ne dépend pas de $x$ dans l'intégrale interne :
   $$ = \int_{\mathbb{R}} |g(y)| \left( \int_{\mathbb{R}} |f(x-y)| dx \right) dy $$
5. Faisons le changement de variable $u = x - y$ ($du = dx$ car $y$ est fixé) dans l'intégrale interne :
   $$ \int_{\mathbb{R}} |f(x-y)| dx = \int_{\mathbb{R}} |f(u)| du = \|f\|_{L^1} $$
6. Substituons ce résultat :
   $$ \|f * g\|_{L^1} \le \int_{\mathbb{R}} |g(y)| \|f\|_{L^1} dy = \|f\|_{L^1} \int_{\mathbb{R}} |g(y)| dy = \|f\|_{L^1} \|g\|_{L^1} $$
7. Puisque $\|f\|_{L^1}$ et $\|g\|_{L^1}$ sont finies (car $f, g \in L^1$), la borne est finie, ce qui prouve que $f * g$ est intégrable et conclut la démonstration de l'inégalité de Young pour $L^1$.
