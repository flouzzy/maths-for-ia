# Exercice 7 : Continuité absolue et KL $\quad \bigstar\bigstar\bigstar\bigstar\star$

\textbf{Énoncé :}
Soit $P \sim \mathcal{U}([0, 1])$ (uniforme) et $Q \sim \mathcal{N}(0, 1)$. Calculer $D_{KL}(P \| Q)$ et $D_{KL}(Q \| P)$.

\textbf{Correction :}
1. $D_{KL}(P \| Q)$ :
   $p(x) = 1$ sur $[0, 1]$, $0$ ailleurs. $q(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2} > 0$ partout.
   Ici $p(x) > 0 \implies q(x) > 0$. L'hypothèse de continuité absolue $P \ll Q$ est vérifiée.
   $$D_{KL}(P \| Q) = \int_0^1 1 \ln\left( \frac{1}{\frac{1}{\sqrt{2\pi}} e^{-x^2/2}} \right) dx = \int_0^1 \left( \ln\sqrt{2\pi} + x^2/2 \right) dx$$
   $$= \ln\sqrt{2\pi} + \left[\frac{x^3}{6}\right]_0^1 = \frac{1}{2}\ln(2\pi) + \frac{1}{6}$$
2. $D_{KL}(Q \| P)$ :
   Ici $Q$ n'est pas absolument continue par rapport à $P$. Par exemple, pour $x=2$, $q(2) > 0$ mais $p(2) = 0$.
   Dans l'intégrale, on aurait une valeur divisée par zéro.
   Par définition formelle de l'extension de la mesure de Radon-Nikodym, si $Q \not\ll P$, $D_{KL}(Q \| P) = +\infty$.
