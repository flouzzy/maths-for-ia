# Exercice 8 : Borne de concentration exponentielle sub-Gaussienne

$\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Une variable aléatoire $X$ d'espérance nulle est dite sub-Gaussienne de paramètre $\sigma^2$ si, pour tout $t \in \mathbb{R}$, on a $\mathbb{E}[e^{tX}] \le e^{\frac{\sigma^2 t^2}{2}}$.
Soit $X$ sub-Gaussienne de paramètre $\sigma^2$. Montrer que pour tout $a > 0$ :
$$ \mathbb{P}(X \ge a) \le \exp\left(-\frac{a^2}{2\sigma^2}\right) $$

**Correction :**
La preuve repose sur l'optimisation standard de la méthode de Chernoff.
Pour un $t > 0$, l'inégalité de Markov appliquée à la variable positive $e^{tX}$ donne :
$$ \mathbb{P}(X \ge a) = \mathbb{P}(e^{tX} \ge e^{ta}) \le \frac{\mathbb{E}[e^{tX}]}{e^{ta}} $$
En utilisant l'hypothèse de la propriété sub-Gaussienne pour le numérateur :
$$ \mathbb{P}(X \ge a) \le \frac{e^{\frac{\sigma^2 t^2}{2}}}{e^{ta}} = \exp\left( \frac{\sigma^2 t^2}{2} - ta \right) $$
Posons $g(t) = \frac{\sigma^2 t^2}{2} - ta$. On veut trouver le $t > 0$ qui minimise $g(t)$.
Dérivons $g$ par rapport à $t$ :
$$ g'(t) = \sigma^2 t - a $$
La dérivée s'annule lorsque $t^* = \frac{a}{\sigma^2}$. Puisque $a > 0$ et $\sigma^2 > 0$, $t^*$ est strictement positif.
Injectons $t^*$ dans $g(t)$ :
$$ g(t^*) = \frac{\sigma^2}{2} \left( \frac{a}{\sigma^2} \right)^2 - a \left( \frac{a}{\sigma^2} \right) = \frac{\sigma^2 a^2}{2 \sigma^4} - \frac{a^2}{\sigma^2} $$
$$ g(t^*) = \frac{a^2}{2 \sigma^2} - \frac{a^2}{\sigma^2} = - \frac{a^2}{2\sigma^2} $$
Ainsi, la borne devient :
$$ \mathbb{P}(X \ge a) \le \exp\left( -\frac{a^2}{2\sigma^2} \right) $$
Cette décroissance exponentielle en $a^2$ caractérise le comportement des queues sub-Gaussiennes, imitant les queues d'une vraie loi normale.
