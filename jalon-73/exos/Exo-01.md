# Exercice 1 : Comparaison de normes sur un ensemble fini

**Difficulté :** $\bigstar\star\star\star\star$

## Énoncé

Soit $X = \{1, 2, 3\}$ muni de la tribu $\mathcal{P}(X)$ et de la mesure de comptage $\mu$ (c'est-à-dire $\mu(\{i\}) = 1$ pour tout $i$).
On considère une fonction $f : X \to \mathbb{R}$ définie par $f(1) = 2, f(2) = -3, f(3) = 1$.

1. L'espace est-il de mesure finie ?
2. Calculer rigoureusement $\|f\|_1, \|f\|_2$ et $\|f\|_\infty$.
3. Vérifier que $\|f\|_\infty \le \|f\|_2 \le \|f\|_1$. Ce résultat est-il général pour la mesure de comptage ?

---

## Correction détaillée

1. **Mesure de l'espace :**
   On a $\mu(X) = \mu(\{1\}) + \mu(\{2\}) + \mu(\{3\}) = 1 + 1 + 1 = 3$. L'espace est donc de mesure finie.

2. **Calcul des normes :**
   - Norme $L^1$ :
     $$ \|f\|_1 = \int_X |f| \, d\mu = |f(1)|\mu(\{1\}) + |f(2)|\mu(\{2\}) + |f(3)|\mu(\{3\}) $$
     $$ \|f\|_1 = |2|\times 1 + |-3|\times 1 + |1|\times 1 = 2 + 3 + 1 = 6 $$
   - Norme $L^2$ :
     $$ \|f\|_2 = \left( \int_X |f|^2 \, d\mu \right)^{1/2} = \left( |2|^2\times 1 + |-3|^2\times 1 + |1|^2\times 1 \right)^{1/2} $$
     $$ \|f\|_2 = \sqrt{4 + 9 + 1} = \sqrt{14} \approx 3.74 $$
   - Norme $L^\infty$ :
     Puisque la mesure de chaque singleton est strictement positive, le supremum essentiel coïncide avec le supremum classique.
     $$ \|f\|_\infty = \max(|2|, |-3|, |1|) = 3 $$

3. **Inégalités :**
   On a bien $3 \le \sqrt{14} \le 6$, c'est-à-dire $\|f\|_\infty \le \|f\|_2 \le \|f\|_1$.
   Cette chaîne d'inégalités est **toujours vraie pour la mesure de comptage** sur un ensemble (les suites $\ell^p$). En effet, pour toute suite, $\sup_i |u_i| \le \left(\sum |u_i|^2\right)^{1/2} \le \sum |u_i|$.
   *Attention :* Ce sens des inclusions est l'inverse de celui des espaces de probabilités !
