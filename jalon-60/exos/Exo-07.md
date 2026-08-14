# Absence de garantie sur les dérivées

### Énoncé $\quad \bigstar\bigstar\bigstar\bigstar\star$

Montrer par un contre-exemple que si un réseau de neurones approche $f \in \mathcal{C}^1$ avec une erreur $\epsilon$ en norme uniforme, son gradient (si existant) n'approche pas nécessairement le gradient de $f$.

### Démonstration Détaillée

Soit $f(x) = 0$ sur $[0,1]$ ($f' \equiv 0$). On peut construire un réseau $g(x) = \epsilon \sin(Nx)$ (approché par des activations). On a $\|f - g\|_\infty \le \epsilon$. Cependant, $g'(x) = N\epsilon \cos(Nx)$. Si on choisit $N$ grand, $\|f' - g'\|_\infty = N\epsilon$ peut être arbitrairement grand. L'approximation uniforme des fonctions n'implique aucune régularité sur les dérivées, sauf si on utilise des topologiques de Sobolev adaptées.
