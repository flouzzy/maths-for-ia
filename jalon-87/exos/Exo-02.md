# Exercice 2 : Espérance d'une loi uniforme continue

**Difficulté :** $\bigstar\star\star\star\star$

Soit $U$ une variable aléatoire suivant une loi uniforme continue sur le segment $[a, b]$, avec $a < b$. Sa densité de probabilité est donnée par $f_U(x) = \frac{1}{b-a}\mathbf{1}_{[a, b]}(x)$.
1. Montrer que $\mathbb{E}[U] = \frac{a+b}{2}$.
2. Calculer la variance $\mathrm{Var}(U)$.

### Correction détaillée

1. L'espérance est définie par l'intégrale de la variable pondérée par la densité :
   $$ \mathbb{E}[U] = \int_{-\infty}^{+\infty} x f_U(x) \, \mathrm{d}x = \int_{a}^{b} x \frac{1}{b-a} \, \mathrm{d}x $$
   Par linéarité de l'intégrale, on sort la constante :
   $$ \mathbb{E}[U] = \frac{1}{b-a} \int_{a}^{b} x \, \mathrm{d}x = \frac{1}{b-a} \left[ \frac{x^2}{2} \right]_a^b $$
   $$ \mathbb{E}[U] = \frac{1}{b-a} \left( \frac{b^2 - a^2}{2} \right) $$
   Grâce à l'identité remarquable $b^2 - a^2 = (b-a)(b+a)$, on simplifie :
   $$ \mathbb{E}[U] = \frac{1}{b-a} \frac{(b-a)(b+a)}{2} = \frac{a+b}{2} $$
   Physiquement, l'espérance est exactement au milieu du segment, ce qui correspond au centre géométrique d'un segment homogène.

2. On calcule d'abord le moment d'ordre 2, $\mathbb{E}[U^2]$ :
   $$ \mathbb{E}[U^2] = \int_{a}^{b} x^2 \frac{1}{b-a} \, \mathrm{d}x = \frac{1}{b-a} \left[ \frac{x^3}{3} \right]_a^b = \frac{b^3 - a^3}{3(b-a)} $$
   On factorise $b^3 - a^3 = (b-a)(b^2 + ab + a^2)$ :
   $$ \mathbb{E}[U^2] = \frac{b^2 + ab + a^2}{3} $$
   On applique la formule de Koenig-Huygens pour la variance :
   $$ \mathrm{Var}(U) = \mathbb{E}[U^2] - (\mathbb{E}[U])^2 = \frac{b^2 + ab + a^2}{3} - \left(\frac{a+b}{2}\right)^2 $$
   $$ \mathrm{Var}(U) = \frac{b^2 + ab + a^2}{3} - \frac{a^2 + 2ab + b^2}{4} $$
   On met au même dénominateur (12) :
   $$ \mathrm{Var}(U) = \frac{4b^2 + 4ab + 4a^2 - 3a^2 - 6ab - 3b^2}{12} = \frac{b^2 - 2ab + a^2}{12} $$
   Ce qui donne :
   $$ \mathrm{Var}(U) = \frac{(b-a)^2}{12} $$
