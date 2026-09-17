## Exercice 2 : Asymétrie de la divergence KL \quad $\bigstar\star\star$
### Énoncé
Avec $P \sim \mathcal{B}(0.1)$ et $Q \sim \mathcal{B}(0.9)$, calculez $D_{KL}(P||Q)$ et $D_{KL}(Q||P)$.
### Correction
$D_{KL}(P||Q) = 0.1 \ln(1/9) + 0.9 \ln(9) \approx -0.22 + 1.97 = 1.75$.
$D_{KL}(Q||P) = 0.9 \ln(9) + 0.1 \ln(1/9) \approx 1.75$, ici la symétrie est accidentelle due à $p = 1-q$.
Prenons $P \sim \mathcal{B}(0.2), Q \sim \mathcal{B}(0.5)$ :
$D_{KL}(P||Q) = 0.2 \ln(0.4) + 0.8 \ln(1.6) \approx -0.18 + 0.37 = 0.19$.
$D_{KL}(Q||P) = 0.5 \ln(2.5) + 0.5 \ln(0.625) \approx 0.45 - 0.23 = 0.22$.
L'asymétrie est claire.
