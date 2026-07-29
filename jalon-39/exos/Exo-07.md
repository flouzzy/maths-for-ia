# Convergence absolue impliquant convergence

**Difficulté :** $\star\star\star\star$

**Énoncé :**
Étudier la convergence de l'intégrale oscillante suivante :
$$ P = \int_1^{+\infty} \frac{\cos(t)}{t^2} dt $$

**Correction Zéro Ellipse :**
1. **Typage :** La fonction $f(t) = \frac{\cos(t)}{t^2}$ est continue sur $[1, +\infty[$. Elle n'est **pas** de signe constant car le cosinus oscille indéfiniment entre -1 et 1. Nous ne pouvons donc pas utiliser directement les critères d'équivalence ou de comparaison classiques.
2. **Passage à la valeur absolue :** Nous allons étudier la convergence absolue de l'intégrale, c'est-à-dire l'intégrale de la valeur absolue de la fonction :
   $$ P_{abs} = \int_1^{+\infty} \left| \frac{\cos(t)}{t^2} \right| dt = \int_1^{+\infty} \frac{|\cos(t)|}{t^2} dt $$
3. **Majoration de la valeur absolue :** La fonction $t \mapsto \frac{|\cos(t)|}{t^2}$ est désormais strictement positive sur $[1, +\infty[$. Nous pouvons utiliser le critère de majoration.
   Pour tout $t \in \mathbb{R}$, on sait que $|\cos(t)| \le 1$.
   En divisant par $t^2$ (strictement positif sur $[1, +\infty[$) :
   $$ 0 \le \frac{|\cos(t)|}{t^2} \le \frac{1}{t^2} $$
4. **Analyse du majorant :** L'intégrale du majorant, $\int_1^{+\infty} \frac{1}{t^2} dt$, est une intégrale de Riemann de paramètre $\alpha = 2 > 1$. Elle est donc convergente.
5. **Conclusion sur la convergence absolue :** D'après le théorème de majoration pour les fonctions positives, puisque le majorant a une intégrale convergente, l'intégrale $\int_1^{+\infty} \frac{|\cos(t)|}{t^2} dt$ converge. L'intégrale $P$ est donc **absolument convergente**.
6. **Conclusion finale :** Un théorème fondamental de l'analyse affirme que toute intégrale absolument convergente est convergente (démontré via le critère de Cauchy). Par conséquent, l'intégrale $P$ converge.
