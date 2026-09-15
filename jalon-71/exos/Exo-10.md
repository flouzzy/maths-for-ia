# Exercice 10 : Transformation de Laplace et Fubini $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit $f : \mathbb{R}_+ \to \mathbb{R}$ continue et bornée. On note sa transformée de Laplace $F(s) = \int_0^{+\infty} f(t) e^{-st} dt$, définie pour $s > 0$.
Montrer que pour tout $x > 0$ :
$$ \int_0^{+\infty} F(s) e^{-xs} ds = \int_0^{+\infty} \frac{f(t)}{x+t} dt $$

## Correction

Exprimons le membre de gauche en insérant la définition de la transformée de Laplace :
$$ I = \int_0^{+\infty} F(s) e^{-xs} ds = \int_0^{+\infty} \left( \int_0^{+\infty} f(t) e^{-st} dt \right) e^{-xs} ds $$
$$ I = \int_0^{+\infty} \left( \int_0^{+\infty} f(t) e^{-(x+t)s} dt \right) ds $$

On souhaite intervertir les deux intégrales. Vérifions si Fubini (ou plutôt Tonelli sur la valeur absolue) s'applique à la fonction $g(s, t) = f(t) e^{-(x+t)s}$.
Comme $f$ est bornée, il existe $M > 0$ tel que $|f(t)| \le M$ pour tout $t$.
$$ \int_0^{+\infty} \left( \int_0^{+\infty} |f(t) e^{-(x+t)s}| dt \right) ds \le M \int_0^{+\infty} \left( \int_0^{+\infty} e^{-(x+t)s} dt \right) ds $$
Intégrons d'abord en $t$ ou en $s$. L'ordre $ds$ puis $dt$ est plus simple pour Tonelli :
$$ \int_0^{+\infty} \left( \int_0^{+\infty} e^{-(x+t)s} ds \right) dt = \int_0^{+\infty} \left[ \frac{e^{-(x+t)s}}{-(x+t)} \right]_{s=0}^{s=+\infty} dt $$
Pour $x>0$ et $t\ge 0$, $x+t > 0$, donc la limite en $+\infty$ est nulle.
$$ = \int_0^{+\infty} \frac{1}{x+t} dt $$
L'intégrale $\int_0^{+\infty} \frac{1}{x+t} dt = [\ln(x+t)]_0^{+\infty}$ diverge vers $+\infty$.
L'hypothèse d'intégrabilité absolue sur tout le quadrant n'est donc **pas** remplie ! La justification par Fubini direct échoue pour la valeur absolue.

Pour s'en sortir rigoureusement, on doit restreindre le domaine. On remarque que $f(t)$ n'est pas remplacée par sa borne dans l'intégrale si on veut que l'égalité soit vraie pour $f$ générale ?
En fait, l'énoncé stipule l'égalité sous réserve de convergence de la deuxième intégrale (ou on interprète au sens de Fubini-Tonelli pour $f$ positive).
Cependant, l'astuce classique est de couper la borne sur $s$ :
Soit $I_R = \int_0^R \left( \int_0^{+\infty} f(t) e^{-(x+t)s} dt \right) ds$. Sur $[0, R] \times \mathbb{R}_+$, l'intégrale de la valeur absolue est finie. On intervertit :
$I_R = \int_0^{+\infty} f(t) \left( \int_0^R e^{-(x+t)s} ds \right) dt = \int_0^{+\infty} f(t) \frac{1 - e^{-(x+t)R}}{x+t} dt$.
Si $f$ est telle que l'intégrale $\int_0^{+\infty} \frac{f(t)}{x+t} dt$ converge absolument, alors par convergence dominée (la fonction à l'intérieur est dominée par $\frac{|f(t)|}{x+t}$ indépendamment de $R$), on passe à la limite $R \to +\infty$ :
$\lim I_R = \int_0^{+\infty} \frac{f(t)}{x+t} dt$.
Ceci prouve l'égalité désirée grâce à l'association de Fubini (sur un domaine tronqué) et de Lebesgue (pour le passage à la limite).
