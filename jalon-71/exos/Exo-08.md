## Exercice 8 : Changement de l'ordre d'intégration \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
L'intégrale $\int_0^1 \int_{\sqrt{y}}^1 e^{x^3} dx dy$ ne peut pas être calculée avec des fonctions élémentaires dans cet ordre, car la primitive de $e^{x^3}$ n'est pas exprimable simplement. Utiliser Fubini pour la calculer.

**Correction :**
1. La fonction $f(x,y) = e^{x^3}$ est positive et continue sur le domaine. Tonelli autorise l'interversion.
2. Identifions le domaine $D$ d'intégration.
   Les bornes de $y$ sont $0 \le y \le 1$.
   Les bornes de $x$ (à $y$ fixé) sont $\sqrt{y} \le x \le 1$.
   Le domaine est donc délimité par $y=0$, $x=1$ et la parabole $x = \sqrt{y} \iff y = x^2$.
3. Modifions l'ordre d'intégration : nous projetons d'abord sur l'axe des $x$.
   Les valeurs extrêmes pour $x$ sur $D$ sont $0 \le x \le 1$.
   Pour un $x$ fixé, $y$ varie de la droite $y=0$ jusqu'à la parabole $y=x^2$.
   Donc, $0 \le y \le x^2$.
4. La nouvelle intégrale s'écrit :
   $$ I = \int_0^1 \left( \int_0^{x^2} e^{x^3} dy \right) dx $$
5. L'intégration interne par rapport à $y$ est maintenant triviale ($x$ est constant) :
   $$ \int_0^{x^2} e^{x^3} dy = e^{x^3} [y]_0^{x^2} = x^2 e^{x^3} $$
6. L'intégration externe devient facile car $x^2$ est proportionnel à la dérivée de $x^3$ :
   $$ I = \int_0^1 x^2 e^{x^3} dx = \left[ \frac{1}{3} e^{x^3} \right]_0^1 = \frac{1}{3}(e^1 - e^0) = \frac{e-1}{3} $$
