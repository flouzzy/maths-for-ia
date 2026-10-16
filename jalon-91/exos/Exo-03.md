# Exercice 3 : Borne de Markov unilatérale (Inégalité de Cantelli)

$\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $X$ une variable aléatoire réelle de carré intégrable, d'espérance $\mu = 0$ et de variance $\sigma^2 > 0$.
Montrer que pour tout $a > 0$ :
$$ \mathbb{P}(X \ge a) \le \frac{\sigma^2}{\sigma^2 + a^2} $$
*Indice : Appliquer l'inégalité de Markov à la variable $(X + t)^2$ pour un réel $t > 0$ judicieusement choisi.*

**Correction :**
Soit $t > 0$ un réel paramétrique.
L'événement $\{X \ge a\}$ implique que $X + t \ge a + t$. Puisque $a + t > 0$, la fonction carré préserve l'inégalité :
$$ X \ge a \implies (X + t)^2 \ge (a + t)^2 $$
Donc $\{X \ge a\} \subset \{(X + t)^2 \ge (a + t)^2\}$.
Ainsi, la probabilité du premier événement est majorée par celle du second :
$$ \mathbb{P}(X \ge a) \le \mathbb{P}((X + t)^2 \ge (a + t)^2) $$
La variable $(X + t)^2$ est positive. Par l'inégalité de Markov :
$$ \mathbb{P}((X + t)^2 \ge (a + t)^2) \le \frac{\mathbb{E}[(X + t)^2]}{(a + t)^2} $$
Développons l'espérance au numérateur :
$$ \mathbb{E}[(X + t)^2] = \mathbb{E}[X^2 + 2tX + t^2] = \mathbb{E}[X^2] + 2t\mathbb{E}[X] + t^2 $$
Puisque $\mathbb{E}[X] = 0$, on a $\mathbb{E}[X^2] = \text{Var}(X) = \sigma^2$. Donc :
$$ \mathbb{E}[(X + t)^2] = \sigma^2 + t^2 $$
On obtient donc pour tout $t > 0$ :
$$ \mathbb{P}(X \ge a) \le \frac{\sigma^2 + t^2}{(a + t)^2} $$
Pour obtenir la borne la plus fine, nous devons minimiser la fonction $f(t) = \frac{\sigma^2 + t^2}{(a + t)^2}$ par rapport à $t > 0$.
Calculons la dérivée de $f$ :
$$ f'(t) = \frac{2t(a + t)^2 - 2(a + t)(\sigma^2 + t^2)}{(a + t)^4} = \frac{2(a + t) [ t(a + t) - (\sigma^2 + t^2) ]}{(a + t)^4} $$
En simplifiant le crochet :
$$ t(a + t) - (\sigma^2 + t^2) = at + t^2 - \sigma^2 - t^2 = at - \sigma^2 $$
La dérivée s'annule lorsque $at - \sigma^2 = 0$, soit pour $t^* = \frac{\sigma^2}{a}$.
Puisque $\sigma^2 > 0$ et $a > 0$, on a bien $t^* > 0$.
Injectons $t^*$ dans $f(t)$ :
$$ f(t^*) = \frac{\sigma^2 + \left(\frac{\sigma^2}{a}\right)^2}{\left(a + \frac{\sigma^2}{a}\right)^2} = \frac{\sigma^2 \left(1 + \frac{\sigma^2}{a^2}\right)}{\left( \frac{a^2 + \sigma^2}{a} \right)^2} = \frac{\sigma^2 \left(\frac{a^2 + \sigma^2}{a^2}\right)}{\frac{(a^2 + \sigma^2)^2}{a^2}} $$
Les termes $a^2$ se simplifient :
$$ f(t^*) = \frac{\sigma^2 (a^2 + \sigma^2)}{(a^2 + \sigma^2)^2} = \frac{\sigma^2}{a^2 + \sigma^2} $$
D'où le résultat final de l'inégalité de Cantelli :
$$ \mathbb{P}(X \ge a) \le \frac{\sigma^2}{\sigma^2 + a^2} $$
Cette borne unilatérale est souvent meilleure que la borne de Tchebychev symétrique pour les événements à une seule queue.
