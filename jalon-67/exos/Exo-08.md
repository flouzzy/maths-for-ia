# Exercice 08 : Application aux transformées de Laplace ($\bigstar$$\bigstar$$\bigstar$$\bigstar$$\star$)

## Énoncé

Soit $\mu$ une mesure finie sur $[0, +\infty[$. Montrer que l'application $L(s) = \int_0^\infty e^{-sx} \,d\mu(x)$ est de classe $C^\infty$ sur $]0, +\infty[$ et calculer ses dérivées.

## Correction Détaillée

1. **Approche par Beppo Levi (séries entières) :** Développons $e^{-sx}$ en série. Fixons $s_0 > 0$. Pour $h$ tel que $|h| < s_0$,
   $$ L(s_0 + h) = \int_0^\infty e^{-(s_0 + h)x} \,d\mu(x) = \int_0^\infty e^{-s_0 x} e^{-hx} \,d\mu(x) = \int_0^\infty e^{-s_0 x} \sum_{n=0}^\infty \frac{(-hx)^n}{n!} \,d\mu(x) $$
2. **Interversion :** Pour appliquer les théorèmes d'interversion, on regarde la somme des valeurs absolues :
   $$ \sum_{n=0}^\infty \int_0^\infty e^{-s_0 x} \frac{|h|^n x^n}{n!} \,d\mu(x) = \int_0^\infty e^{-s_0 x} \sum_{n=0}^\infty \frac{|h|^n x^n}{n!} \,d\mu(x) = \int_0^\infty e^{-(s_0 - |h|)x} \,d\mu(x) $$
   La deuxième égalité est justifiée par Beppo Levi (fonctions positives). Puisque $s_0 - |h| > 0$, la fonction $x \mapsto e^{-(s_0 - |h|)x}$ est bornée par 1 sur $[0, +\infty[$. Comme $\mu$ est finie, cette intégrale est finie.
3. **Conséquence :** Par le théorème de Fubini pour les sommes/intégrales (ou le théorème de convergence dominée pour la série), on peut intervertir la sommation sans valeurs absolues :
   $$ L(s_0 + h) = \sum_{n=0}^\infty \frac{(-h)^n}{n!} \int_0^\infty x^n e^{-s_0 x} \,d\mu(x) $$
4. **Dérivabilité :** Ceci exprime $L$ comme la somme d'une série entière convergente au voisinage de $s_0$. Elle est donc analytique (et donc $C^\infty$) sur $]0, +\infty[$, et ses dérivées s'obtiennent par dérivation terme à terme (ce qui revient à dériver sous l'intégrale) :
   $$ L^{(n)}(s) = \int_0^\infty (-x)^n e^{-sx} \,d\mu(x) $$
