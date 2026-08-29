# Exercice 5 : Dérivabilité sous l'intégrale via TCM $\bigstar\bigstar\bigstar\star\star$

## Énoncé
Soit $f : \mathbb{R}_+ \to \mathbb{R}_+$ une fonction mesurable. On suppose que pour tout $t \ge 0$, la fonction $x \mapsto f(x)e^{-tx}$ est intégrable.
On pose $F(t) = \int_0^\infty f(x) e^{-tx} dx$.
Prouver rigoureusement, sans utiliser le théorème de convergence dominée, que $F$ est décroissante et dérivable, avec $F'(t) = -\int_0^\infty x f(x) e^{-tx} dx$. (Indication : écrire le taux d'accroissement et utiliser le TCM en observant une certaine croissance).

## Correction Détaillée
1. Soit $h > 0$. Le taux d'accroissement de $F$ entre $t$ et $t+h$ est :
   $$ \frac{F(t+h) - F(t)}{h} = \int_0^\infty f(x) \frac{e^{-(t+h)x} - e^{-tx}}{h} dx = -\int_0^\infty f(x) e^{-tx} \frac{1 - e^{-hx}}{h} dx $$
2. Posons $g_h(x) = f(x) e^{-tx} \frac{1 - e^{-hx}}{h}$. C'est une fonction positive.
3. Étudions la monotonie de $h \mapsto \frac{1 - e^{-hx}}{h}$ lorsque $h$ décroît vers $0$.
   La fonction $\phi(u) = \frac{1 - e^{-u}}{u}$ est décroissante pour $u > 0$ (sa dérivée est $\frac{e^{-u}(1+u) - 1}{u^2} < 0$).
   Donc quand $h_n \searrow 0$, la suite de fonctions $g_{h_n}(x)$ est *croissante*.
4. La limite ponctuelle de $g_{h_n}(x)$ quand $h_n \to 0$ est, par définition de la dérivée de l'exponentielle en 0, $f(x) e^{-tx} x$.
5. Par le Théorème de Convergence Monotone :
   $$ \lim_{n \to \infty} \int_0^\infty g_{h_n}(x) dx = \int_0^\infty x f(x) e^{-tx} dx $$
6. Ce qui implique que la dérivée à droite de $F$ en $t$ existe et vaut $-\int_0^\infty x f(x) e^{-tx} dx$. (Un raisonnement similaire montre l'égalité à gauche).
