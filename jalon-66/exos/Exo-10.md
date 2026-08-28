# Inégalité de Tchebychev-Markov

**Difficulté :** $\star\star\star\star\star$

## Énoncé

Soit $f \geq 0$ une fonction mesurable sur $(X, \mathcal{A}, \mu)$. Pour tout $\alpha > 0$, prouvez l'inégalité fondamentale : $\mu(\{x \in X \mid f(x) \geq \alpha\}) \leq \frac{1}{\alpha} \int_X f \, d\mu$.

---

## Correction détaillée

Soit $A_\alpha = \{x \in X \mid f(x) \geq \alpha\}$. L'ensemble $A_\alpha$ est mesurable car $f$ est une fonction mesurable.
Considérons la fonction étagée $s = \alpha \mathbb{1}_{A_\alpha}$.
Pour tout $x \in X$ :
- Si $x \in A_\alpha$, alors $f(x) \geq \alpha = s(x)$.
- Si $x \notin A_\alpha$, alors $f(x) \geq 0 = s(x)$ (car $f$ est positive).
Dans tous les cas, on a $0 \leq s \leq f$.
Par définition de l'intégrale (propriété de monotonie) :
$$ \int_X s \, d\mu \leq \int_X f \, d\mu $$
Or, $\int_X s \, d\mu = \int_X \alpha \mathbb{1}_{A_\alpha} \, d\mu = \alpha \mu(A_\alpha)$.
Donc : $\alpha \mu(A_\alpha) \leq \int_X f \, d\mu$.
Comme $\alpha > 0$, en divisant par $\alpha$, on obtient le résultat escompté : $\mu(A_\alpha) \leq \frac{1}{\alpha} \int_X f \, d\mu$.
