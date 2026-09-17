## Exercice 6 : KL pour des lois exponentielles \quad $\bigstar\bigstar\star$
### Énoncé
Calculez $D_{KL}(Exp(\lambda_1) || Exp(\lambda_2))$.
### Correction
$\int_0^\infty \lambda_1 e^{-\lambda_1 x} \ln\left(\frac{\lambda_1 e^{-\lambda_1 x}}{\lambda_2 e^{-\lambda_2 x}}\right) dx$.
$= \ln(\frac{\lambda_1}{\lambda_2}) + \frac{\lambda_2 - \lambda_1}{\lambda_1}$.
