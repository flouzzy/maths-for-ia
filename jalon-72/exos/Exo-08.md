## Exercice 8 : Divergence de Jensen-Shannon \quad $\bigstar\bigstar\bigstar$
### Énoncé
Définissez la divergence de Jensen-Shannon et vérifiez sa symétrie.
### Correction
$JSD(P||Q) = \frac{1}{2} D_{KL}(P || M) + \frac{1}{2} D_{KL}(Q || M)$ où $M = \frac{1}{2}(P+Q)$. Par construction, elle est symétrique.
