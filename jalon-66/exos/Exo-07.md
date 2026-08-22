# Intégrabilité et finitude

**Difficulté :** $\star\star\star\star\star$

## Énoncé

Soit $f \geq 0$ mesurable. On suppose que $\int_X f \, d\mu < +\infty$. Montrez que l'ensemble $E = \{x \in X \mid f(x) = +\infty\}$ est de mesure nulle : $\mu(E) = 0$.

---

## Correction détaillée

Considérons pour tout entier $n \geq 1$ la fonction étagée $s_n = n \mathbb{1}_E$.
Puisque pour $x \in E$, $f(x) = +\infty > n$, et pour $x \notin E$, $s_n(x) = 0 \leq f(x)$, on a toujours $0 \leq s_n \leq f$.
Par définition de l'intégrale de Lebesgue via le supremum sur $\mathcal{E}^+$, on a :
$$ \int_X f \, d\mu \geq \int_X s_n \, d\mu = n \mu(E) $$
Ceci est vrai pour tout $n \geq 1$. Supposons par l'absurde que $\mu(E) > 0$.
Alors la limite de $n \mu(E)$ quand $n \to +\infty$ est $+\infty$.
Cela impliquerait que $\int_X f \, d\mu = +\infty$, ce qui contredit l'hypothèse de l'énoncé.
Par conséquent, on doit nécessairement avoir $\mu(E) = 0$. On dit que $f$ est finie *presque partout*.
