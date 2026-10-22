# Exercice 2

**Difficulté :** $\star\star\☆☆☆$

**Énoncé :**
On considère l'espace $E = \mathcal{C}([0,1], \mathbb{R})$ muni de la norme uniforme $\|f\|_\infty = \sup_{t \in [0,1]} |f(t)|$. Soit l'opérateur $T : E \to E$ défini par $T(f)(x) = \int_0^x f(t)dt$. Montrer que $T$ est un opérateur linéaire continu et calculer sa norme $\|T\|_{\mathcal{L}(E, E)}$.

**Correction Détaillée :**
1. **Linéarité :** L'intégrale est linéaire. Pour toutes fonctions $f, g \in E$ et réels $\alpha, \beta$, $T(\alpha f + \beta g)(x) = \int_0^x (\alpha f(t) + \beta g(t))dt = \alpha \int_0^x f(t)dt + \beta \int_0^x g(t)dt = \alpha T(f)(x) + \beta T(g)(x)$. L'opérateur $T$ est donc linéaire.
2. **Continuité et borne supérieure :** Évaluons $\|T(f)\|_\infty$. Pour tout $x \in [0, 1]$ :
   $$ |T(f)(x)| = \left| \int_0^x f(t)dt \right| \le \int_0^x |f(t)| dt \le \int_0^x \|f\|_\infty dt = x \|f\|_\infty \le 1 \cdot \|f\|_\infty. $$
3. En prenant le supremum sur $x \in [0, 1]$, on obtient $\|T(f)\|_\infty \le \|f\|_\infty$.
4. Cela montre que $T$ est continu, et que sa norme d'opérateur vérifie $\|T\| \le 1$.
5. **Calcul exact de la norme :** Pour montrer que $\|T\| = 1$, trouvons une fonction (ou une suite de fonctions) qui atteint cette borne. Considérons la fonction constante $f(t) = 1$ pour tout $t \in [0,1]$.
6. On a clairement $f \in E$ et $\|f\|_\infty = 1$.
7. Appliquons l'opérateur : $T(f)(x) = \int_0^x 1 dt = x$.
8. La norme de la fonction résultante est $\|T(f)\|_\infty = \sup_{x \in [0,1]} |x| = 1$.
9. Le ratio est $\frac{\|T(f)\|_\infty}{\|f\|_\infty} = \frac{1}{1} = 1$.
10. Par conséquent, la norme de l'opérateur est exactement $\|T\|_{\mathcal{L}(E, E)} = 1$.
