## Exercice 3 : Croissance avec paramètre \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Montrer que $\lim_{n \to \infty} \int_0^1 \frac{n x}{1 + n^2 x^2} dx = 0$ n'est PAS un contre-exemple au théorème de convergence monotone.

**Correction Détaillée :**
1. Posons $f_n(x) = \frac{n x}{1 + n^2 x^2}$ pour $x \in [0, 1]$.
2. Les fonctions $f_n$ sont positives. Calculons la limite simple : pour $x > 0$, $f_n(x) \sim \frac{nx}{n^2x^2} = \frac{1}{nx} \to 0$ quand $n \to \infty$. Pour $x=0$, $f_n(0) = 0$. Donc $f_n(x) \to 0$ ponctuellement, de fonction limite $f(x) = 0$.
3. Calculons l'intégrale : $I_n = \int_0^1 \frac{n x}{1 + n^2 x^2} dx = \frac{1}{2n} [\ln(1 + n^2 x^2)]_0^1 = \frac{\ln(1+n^2)}{2n}$.
4. Lorsque $n \to \infty$, $I_n \to 0$. Ici, la limite des intégrales est égale à l'intégrale de la limite.
5. Cependant, vérifions la condition du théorème de convergence monotone. La dérivée par rapport à $n$ (vu comme variable continue $t$) donne $\partial_t \frac{tx}{1+t^2x^2} = \frac{x(1+t^2x^2) - tx(2tx^2)}{(1+t^2x^2)^2} = \frac{x(1-t^2x^2)}{(1+t^2x^2)^2}$.
6. Cette dérivée est négative dès que $tx > 1$, c'est-à-dire $n > 1/x$. La suite $(f_n(x))$ n'est donc **pas** croissante pour $n$ assez grand. Le théorème de convergence monotone ne s'applique pas, ce qui explique pourquoi ce n'est pas un contre-exemple (les hypothèses ne sont pas vérifiées). (La conclusion est quand même vraie ici, grâce au théorème de convergence dominée).
