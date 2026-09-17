# Exercice 5 : Inégalité de Pinsker (introduction) $\quad \bigstar\bigstar\bigstar\star\star$

\textbf{Énoncé :}
Montrer que pour deux distributions $P$ et $Q$, si $D_{KL}(P \| Q) = 0$, alors la distance en variation totale est nulle.

\textbf{Correction :}
L'inégalité de Pinsker stipule que $\delta(P, Q) \le \sqrt{\frac{1}{2} D_{KL}(P \| Q)}$ où $\delta(P, Q) = \sup_{A} |P(A) - Q(A)|$.
Ainsi, si $D_{KL}(P \| Q) = 0$, on a $\delta(P, Q) \le 0$, donc la distance est strictement nulle, ce qui implique $P = Q$ (au sens de la mesure).
L'inégalité de Pinsker est l'un des outils qui relie la théorie de l'information (KL) aux distances topologiques fortes des probabilités.
