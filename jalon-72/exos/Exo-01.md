## Exercice 1 : Divergence KL entre deux variables de Bernoulli \quad $\bigstar\star\star$
### Énoncé
Soient $P$ et $Q$ deux distributions de Bernoulli de paramètres $p$ et $q$.
Démontrez la positivité stricte de $D_{KL}(P||Q)$ pour $p \neq q$.
### Correction
Par définition, $D_{KL}(P||Q) = p \ln\left(\frac{p}{q}\right) + (1-p) \ln\left(\frac{1-p}{1-q}\right)$.
L'inégalité log de Gibbs $x \ln(x/y) \ge x - y$ implique que cette somme est $\ge (p-q) + ((1-p)-(1-q)) = 0$.
L'égalité n'est atteinte que si $p=q$.
