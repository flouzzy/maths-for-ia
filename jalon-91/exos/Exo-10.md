# Exercice 10 : Inégalité de Bennett et comparaison avec Chernoff

$\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
L'inégalité de Bennett affine la borne de Hoeffding en intégrant la connaissance de la variance réelle, très utile si celle-ci est petite.
Soit $X_1, \dots, X_n$ indépendantes centrées, $X_i \le 1$ p.s., et posons $\sigma^2 = \frac{1}{n} \sum_{i=1}^n \text{Var}(X_i)$.
La borne de Bennett affirme pour $S_n = \sum X_i$ et $t > 0$ :
$$ \mathbb{P}(S_n \ge nt) \le \exp\left( -n \sigma^2 h\left(\frac{t}{\sigma^2}\right) \right) \quad \text{où } h(u) = (1+u)\ln(1+u) - u $$
Montrer par une étude analytique locale que pour des petites déviations $u = \frac{t}{\sigma^2} \approx 0$, l'exposant correspond à la décroissance gaussienne de Tchebychev/Chernoff $-nt^2/(2\sigma^2)$.

**Correction :**
Étudions le développement limité de la fonction $h(u) = (1+u)\ln(1+u) - u$ au voisinage de $u = 0$.
Rappelons le développement limité du logarithme népérien au voisinage de 1 :
$$ \ln(1+u) = u - \frac{u^2}{2} + o(u^2) $$
Remplaçons dans l'expression de $h(u)$ :
$$ h(u) = (1+u)\left(u - \frac{u^2}{2} + o(u^2)\right) - u $$
Développons le produit :
$$ h(u) = u - \frac{u^2}{2} + u^2 + o(u^2) - u $$
Les termes en $u$ s'annulent ($u - u = 0$) :
$$ h(u) = \frac{u^2}{2} + o(u^2) $$
L'exposant de l'inégalité de Bennett s'écrit $-n \sigma^2 h(u)$ avec $u = \frac{t}{\sigma^2}$.
Pour $t$ petit devant $\sigma^2$ (i.e. $u \to 0$), on a $h(t/\sigma^2) \approx \frac{1}{2} \left(\frac{t}{\sigma^2}\right)^2 = \frac{t^2}{2\sigma^4}$.
L'exposant de Bennett est alors approximativement :
$$ -n \sigma^2 h\left(\frac{t}{\sigma^2}\right) \approx -n \sigma^2 \frac{t^2}{2\sigma^4} = - \frac{nt^2}{2\sigma^2} $$
Ainsi, la borne de Bennett asymptotique s'écrit :
$$ \mathbb{P}\left(\frac{S_n}{n} \ge t\right) = \mathbb{P}(S_n \ge nt) \le \exp\left( - \frac{n t^2}{2\sigma^2} \right) $$
C'est exactement la décroissance exponentielle sub-gaussienne que l'on attendrait par le Théorème Central Limite, validant la puissance de la borne de Bennett pour les petites déviations où elle capture fidèlement la variance de l'échantillon, contrairement à Hoeffding qui borne paresseusement par la plage $(b-a)^2$.
