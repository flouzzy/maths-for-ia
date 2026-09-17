# Exercice 1 : KL de Bernoulli $\quad \bigstar\star\star\star\star$

\textbf{Énoncé :}
Soient $P$ et $Q$ deux lois de Bernoulli de paramètres respectifs $p=0.8$ et $q=0.2$.
Calculer $D_{KL}(P \| Q)$ et $D_{KL}(Q \| P)$. Que constatez-vous ?

\textbf{Correction :}
1. Calcul de $D_{KL}(P \| Q)$ :
   $$D_{KL}(P \| Q) = p \ln\left(\frac{p}{q}\right) + (1-p) \ln\left(\frac{1-p}{1-q}\right)$$
   $$D_{KL}(P \| Q) = 0.8 \ln\left(\frac{0.8}{0.2}\right) + 0.2 \ln\left(\frac{0.2}{0.8}\right)$$
   $$D_{KL}(P \| Q) = 0.8 \ln(4) + 0.2 \ln(0.25) = 0.8(1.386) + 0.2(-1.386) = 1.386(0.6) = 0.831$$
2. Calcul de $D_{KL}(Q \| P)$ :
   $$D_{KL}(Q \| P) = q \ln\left(\frac{q}{p}\right) + (1-q) \ln\left(\frac{1-q}{1-p}\right)$$
   $$D_{KL}(Q \| P) = 0.2 \ln(0.25) + 0.8 \ln(4) = 0.831$$
Pour ce cas symétrique ($p = 1-q$), les deux divergences sont égales, mais ce n'est pas le cas général.
