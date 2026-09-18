# Exercice 10 : Divergence de Jensen-Shannon $\quad \bigstar\bigstar\bigstar\bigstar\bigstar$

\textbf{Énoncé :}
La divergence de Jensen-Shannon est définie par :
$JSD(P \| Q) = \frac{1}{2} D_{KL}(P \| M) + \frac{1}{2} D_{KL}(Q \| M)$, où $M = \frac{P+Q}{2}$.
Prouver que $0 \le JSD(P \| Q) \le \ln(2)$.

\textbf{Correction :}
1. $JSD \ge 0$ car elle est la somme de deux divergences KL, qui sont toutes deux positives (Inégalité de Gibbs).
2. Pour la borne supérieure :
$$D_{KL}(P \| M) = \int p \ln\left( \frac{p}{(p+q)/2} \right) = \int p \ln\left( \frac{2p}{p+q} \right) = \ln(2) + \int p \ln\left( \frac{p}{p+q} \right)$$
On a $\frac{p}{p+q} \le 1$, donc $\ln\left( \frac{p}{p+q} \right) \le 0$.
Ainsi $D_{KL}(P \| M) \le \ln(2)$.
De même, $D_{KL}(Q \| M) \le \ln(2)$.
Donc $JSD \le \frac{1}{2}\ln(2) + \frac{1}{2}\ln(2) = \ln(2)$.
La divergence de Jensen-Shannon est toujours bornée, symétrique, et sa racine carrée est une vraie métrique.
