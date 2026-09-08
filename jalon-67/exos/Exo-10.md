# Exercice 10 : Application aux probabilités \quad $\bigstar$$\bigstar$$\bigstar$$\bigstar$$\bigstar$

**Énoncé :**
Soit $X$ une variable aléatoire réelle positive. Prouver $\mathbb{E}[X] = \int_0^\infty \mathbb{P}(X > t) dt$.

**Correction Détaillée :**
1. On écrit $X = \int_0^X 1 dt = \int_0^\infty \mathbf{1}_{t < X} dt$. Par Fubini (ou Beppo Levi sur une suite discrétisée), on intervertit l'espérance et l'intégrale.
2. Le théorème de convergence monotone est au coeur de la justification formelle.
