# Divergence par équivalent en un point fini

**Difficulté :** $\star\star\star\star$

**Énoncé :**
Montrer que l'intégrale suivante est divergente :
$$ Q = \int_0^1 \frac{e^t}{\sin(t)} dt $$

**Correction Zéro Ellipse :**
1. **Typage de l'intégrande :** La fonction $f(t) = \frac{e^t}{\sin(t)}$ est définie et continue sur $]0, 1]$. Sur cet intervalle, $e^t > 0$ et $\sin(t) > 0$, donc la fonction est strictement positive. Le point impropre est 0, où le sinus s'annule, créant une asymptote verticale.
2. **Recherche de l'équivalent en 0 :** Puisque la fonction est de signe constant (positive), nous pouvons utiliser les équivalents.
   - Au numérateur : lorsque $t \to 0$, $e^t \to e^0 = 1$. Donc $e^t \sim_0 1$.
   - Au dénominateur : d'après le développement limité à l'ordre 1 en 0, $\sin(t) \sim_0 t$.
   Par quotient d'équivalents (valide pour les équivalents non nuls), nous obtenons le comportement asymptotique global en 0 :
   $$ f(t) = \frac{e^t}{\sin(t)} \sim_0 \frac{1}{t} $$
3. **Analyse de la fonction de référence :** Considérons la fonction $g(t) = 1/t$. L'intégrale de référence en 0 est :
   $$ \int_0^1 g(t) dt = \int_0^1 \frac{1}{t^1} dt $$
   Il s'agit d'une intégrale de Riemann en 0 de la forme $\int_0^a \frac{1}{t^\alpha} dt$, avec $\alpha = 1$.
   Le théorème stipule que cette intégrale converge si et seulement si $\alpha < 1$. Puisque $\alpha = 1$, l'intégrale de référence $\int_0^1 \frac{1}{t} dt$ est **divergente** (elle vaut $+\infty$).
4. **Conclusion :** D'après le théorème d'équivalence pour les intégrales de fonctions positives de même signe, puisque $f(t) \sim_0 1/t$ et que l'intégrale de $1/t$ sur $[0,1]$ diverge, alors l'intégrale $Q$ diverge également vers $+\infty$.
