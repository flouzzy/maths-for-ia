# Critère d'équivalence en l'infini

**Difficulté :** $\star\star\star$

**Énoncé :**
Déterminer la nature de l'intégrale :
$$ K = \int_1^{+\infty} \frac{t^2 + 2t + 5}{t^4 + t^2 + 1} dt $$

**Correction Zéro Ellipse :**
1. **Typage de l'intégrande :** Soit $f(t) = \frac{t^2 + 2t + 5}{t^4 + t^2 + 1}$. Le dénominateur $t^4 + t^2 + 1$ est strictement positif pour tout $t \in \mathbb{R}$. La fonction $f$ est donc définie, continue et strictement positive sur $[1, +\infty[$. L'intégrale est impropre uniquement en $+\infty$.
2. **Méthodologie :** Comme $f$ est une fonction positive, nous pouvons appliquer le théorème d'équivalence pour les intégrales généralisées de fonctions positives.
3. **Recherche de l'équivalent en $+\infty$ :**
   - Au numérateur, le terme de plus haut degré domine : $t^2 + 2t + 5 \sim_{+\infty} t^2$.
   - Au dénominateur, le terme de plus haut degré domine : $t^4 + t^2 + 1 \sim_{+\infty} t^4$.
   Par quotient d'équivalents (ce qui est une opération valide), on a :
   $$ f(t) \sim_{+\infty} \frac{t^2}{t^4} = \frac{1}{t^2} $$
4. **Utilisation de l'intégrale de référence :** Posons $g(t) = \frac{1}{t^2}$. L'intégrale $\int_1^{+\infty} g(t) dt$ est une intégrale de Riemann de la forme $\int_1^{+\infty} \frac{1}{t^\alpha} dt$ avec $\alpha = 2$.
5. **Conclusion théorique :** Puisque $\alpha = 2 > 1$, l'intégrale de Riemann $\int_1^{+\infty} \frac{1}{t^2} dt$ est convergente.
   D'après le théorème d'équivalence pour les fonctions positives ($f(t) \sim g(t) > 0$), les intégrales $\int_1^{+\infty} f(t) dt$ et $\int_1^{+\infty} g(t) dt$ sont de même nature.
   L'intégrale $K$ est donc convergente.
