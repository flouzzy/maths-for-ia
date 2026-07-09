# Exercice 9 : Intégration sur un intervalle non compact

**Difficulté :** $\star\star\star\star\star$

**Énoncé :**
Montrer que $\int_0^{+\infty} e^{-x} \cos(\sqrt{x}) dx = \sum_{n=0}^\infty \frac{(-1)^n n!}{(2n)!}$.
*(Indication : utiliser le développement en série entière de cosinus)*

**Démonstration :**
1. **Développement de la fonction intégrée :**
   On sait que pour tout $u \in \mathbb{R}$, $\cos(u) = \sum_{n=0}^\infty \frac{(-1)^n u^{2n}}{(2n)!}$.
   En posant $u = \sqrt{x}$, pour $x \ge 0$, $\cos(\sqrt{x}) = \sum_{n=0}^\infty \frac{(-1)^n x^n}{(2n)!}$.
   Donc l'intégrande s'écrit : $f(x) = e^{-x} \cos(\sqrt{x}) = \sum_{n=0}^\infty \frac{(-1)^n x^n e^{-x}}{(2n)!}$.
2. **Utilisation du théorème d'intégration d'une série de fonctions sur un intervalle quelconque :**
   Posons $u_n(x) = \frac{(-1)^n x^n e^{-x}}{(2n)!}$.
   Les fonctions $u_n$ sont continues et intégrables sur $[0, +\infty[$.
   Leur intégrale absolue est :
   $$ \int_0^{+\infty} |u_n(x)| dx = \int_0^{+\infty} \frac{x^n e^{-x}}{(2n)!} dx $$
   On reconnaît l'intégrale Gamma d'Euler : $\int_0^{+\infty} x^n e^{-x} dx = \Gamma(n+1) = n!$.
   Ainsi, $\int_0^{+\infty} |u_n(x)| dx = \frac{n!}{(2n)!}$.
3. **Convergence de la série des intégrales absolues :**
   Il faut montrer que la série $\sum \frac{n!}{(2n)!}$ converge pour justifier l'interversion.
   Utilisons le critère de d'Alembert pour $v_n = \frac{n!}{(2n)!}$ :
   $$ \frac{v_{n+1}}{v_n} = \frac{(n+1)!}{(2n+2)!} \frac{(2n)!}{n!} = \frac{n+1}{(2n+2)(2n+1)} = \frac{1}{2(2n+1)} $$
   La limite quand $n \to \infty$ est $0 < 1$. Donc la série converge.
4. **Conclusion par le théorème de convergence dominée pour les séries :**
   Puisque la série des intégrales absolues converge, on peut intervertir série et intégrale sur $]0, +\infty[$ :
   $$ \int_0^{+\infty} \left( \sum_{n=0}^\infty u_n(x) \right) dx = \sum_{n=0}^\infty \int_0^{+\infty} u_n(x) dx $$
   Calculons l'intégrale sans valeur absolue :
   $$ \int_0^{+\infty} u_n(x) dx = \frac{(-1)^n}{(2n)!} \int_0^{+\infty} x^n e^{-x} dx = \frac{(-1)^n n!}{(2n)!} $$
   Ce qui donne exactement :
   $$ \int_0^{+\infty} e^{-x} \cos(\sqrt{x}) dx = \sum_{n=0}^\infty \frac{(-1)^n n!}{(2n)!} $$
$\blacksquare$
