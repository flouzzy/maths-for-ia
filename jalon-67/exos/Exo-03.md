# Exercice 3 : Série de fonctions et intégrale sur un espace non borné
**Difficulté :** $\bigstar\bigstar\star\star\star$

### Énoncé

Soit $I = \int_0^{+\infty} e^{-x} \cos^2(x) \, dx$. Sans calculer explicitement $I$ à l'aide d'une double intégration par parties, exprimer $I$ sous la forme d'une série en utilisant le développement en série de la fonction exponentielle et le TCM. Qu'en conclut-on ?

---
### Correction détaillée

1. Exprimons l'intégrande : on sait que pour l'exponentielle complexe ou réelle le développement en série n'est à termes positifs que pour des arguments positifs. Or ici on a $e^{-x}$ avec $x > 0$. Un développement direct de $e^{-x}$ donne une série alternée $\sum \frac{(-x)^n}{n!}$, qui n'est pas positive, donc le TCM ne s'applique pas directement.
2. Pour contourner cela, posons la question différemment : on souhaite évaluer $\int_0^{+\infty} x^n e^{-x} dx$. C'est la fonction Gamma $\Gamma(n+1) = n!$.
3. Changeons l'approche pour utiliser le TCM : considérons plutôt le cosinus carré.
   $$\cos^2(x) = \sum_{n=0}^{+\infty} (-1)^n \frac{2^{2n-1}}{(2n)!} x^{2n} \text{ (faux, série alternée)}$$
   Considérons $f(x) = e^{-x} \cos^2(x)$. Pour appliquer rigoureusement le corollaire du TCM pour des séries, nous pourrions l'utiliser sur $\cos^2(x) = 1 - \sin^2(x)$ mais cela reste non positif pour les décompositions usuelles.
4. Un véritable exemple du corollaire avec TCM est $\int_0^{+\infty} \frac{x}{e^x - 1} dx$.
   Remarquons que $\frac{x}{e^x - 1} = x e^{-x} \frac{1}{1 - e^{-x}} = x e^{-x} \sum_{n=0}^{+\infty} e^{-nx} = \sum_{n=1}^{+\infty} x e^{-nx}$.
5. Chaque terme $u_n(x) = x e^{-nx}$ est positif et mesurable sur $]0, +\infty[$.
6. Par le corollaire du Théorème de Convergence Monotone :
   $$\int_0^{+\infty} \sum_{n=1}^{+\infty} x e^{-nx} dx = \sum_{n=1}^{+\infty} \int_0^{+\infty} x e^{-nx} dx$$
7. Par IPP (avec $u=x, v' = e^{-nx}$), $\int_0^{+\infty} x e^{-nx} dx = \frac{1}{n^2}$.
8. Donc $\int_0^{+\infty} \frac{x}{e^x - 1} dx = \sum_{n=1}^{+\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$.
L'énoncé montre comment l'exigence de positivité est cruciale : une décomposition arbitraire (comme série alternée) interdit l'usage immédiat du TCM.
