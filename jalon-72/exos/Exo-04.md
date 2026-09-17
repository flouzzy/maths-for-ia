## Exercice 4 : Entropie croisée et divergence KL \quad $\bigstar\bigstar\star$
### Énoncé
Montrez que $H(P, Q) = H(P) + D_{KL}(P||Q)$.
### Correction
$H(P, Q) = -\sum P(x) \ln Q(x) = -\sum P(x) \ln P(x) + \sum P(x) \ln\left(\frac{P(x)}{Q(x)}\right) = H(P) + D_{KL}(P||Q)$.
Minimiser l'entropie croisée revient à minimiser la KL par rapport à $Q$ si $P$ est fixe.
