# Changement de variable dans une intégrale généralisée

**Difficulté :** $\star\star\star\star\star$

**Énoncé :**
Prouver la convergence et calculer la valeur de l'intégrale de Gauss (sur $\mathbb{R}^+$) :
$$ R = \int_0^{+\infty} e^{-t^2} dt $$
*Indication : On admettra le résultat classique $\int_0^{+\infty} e^{-x^2} dx = \frac{\sqrt{\pi}}{2}$. On demande ici de calculer $\int_0^{+\infty} \frac{e^{-u}}{\sqrt{u}} du$ par changement de variable pour démontrer un lien avec la fonction Gamma.*

**Correction Zéro Ellipse :**
1. **Typage :** Soit $I = \int_0^{+\infty} \frac{e^{-u}}{\sqrt{u}} du$. L'intégrande $f(u) = u^{-1/2}e^{-u}$ est continu et positif sur $]0, +\infty[$. L'intégrale est doublement impropre : en $0$ et en $+\infty$. Nous devons prouver la convergence sur $]0, 1]$ et sur $[1, +\infty[$.
   - **En 0 :** $f(u) \sim_0 u^{-1/2}$. $\int_0^1 \frac{1}{u^{1/2}} du$ converge (Riemann, $\alpha = 1/2 < 1$). Par équivalence, $\int_0^1 f(u) du$ converge.
   - **En $+\infty$ :** $\lim_{u \to +\infty} u^2 f(u) = \lim_{u \to +\infty} u^{3/2}e^{-u} = 0$. Donc pour $u$ grand, $f(u) < \frac{1}{u^2}$. Par comparaison, $\int_1^{+\infty} f(u) du$ converge. L'intégrale globale $I$ converge.
2. **Théorème de Changement de variable :** Soit un paramètre d'intégration fini $X > 0$. On pose $I(X) = \int_{\epsilon}^X \frac{e^{-u}}{\sqrt{u}} du$ (avec $\epsilon \to 0$ puis $X \to +\infty$).
   Effectuons le changement de variable $u = t^2$.
   - La fonction $t \mapsto t^2$ est un difféomorphisme (bijection de classe $C^1$ dont la dérivée ne s'annule pas) de $]0, +\infty[$ sur $]0, +\infty[$.
   - Différentielle : $du = 2t dt$.
   - Bornes : si $u \to 0^+$, alors $t = \sqrt{u} \to 0^+$. Si $u \to +\infty$, alors $t \to +\infty$.
3. **Application sur un intervalle fini :**
   $$ \int_{\epsilon}^X \frac{e^{-u}}{\sqrt{u}} du = \int_{\sqrt{\epsilon}}^{\sqrt{X}} \frac{e^{-t^2}}{\sqrt{t^2}} (2t dt) = \int_{\sqrt{\epsilon}}^{\sqrt{X}} \frac{e^{-t^2}}{t} (2t) dt = 2 \int_{\sqrt{\epsilon}}^{\sqrt{X}} e^{-t^2} dt $$
4. **Passage à la limite simultané :**
   Lorsque $\epsilon \to 0^+$ et $X \to +\infty$, l'égalité des intégrales partielles se conserve pour les limites, puisque nous avons prouvé a priori la convergence.
   $$ \int_0^{+\infty} \frac{e^{-u}}{\sqrt{u}} du = 2 \int_0^{+\infty} e^{-t^2} dt $$
5. **Conclusion :** D'après le résultat admis pour l'intégrale de Gauss $\int_0^{+\infty} e^{-t^2} dt = \frac{\sqrt{\pi}}{2}$, nous déduisons que :
   $$ \int_0^{+\infty} \frac{e^{-u}}{\sqrt{u}} du = 2 \times \frac{\sqrt{\pi}}{2} = \sqrt{\pi} $$
   Cette intégrale correspond à la valeur de la fonction Gamma en $1/2$ : $\Gamma(1/2) = \sqrt{\pi}$.
