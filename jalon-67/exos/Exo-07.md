# Exercice 7 : Intégrale de Fresnel via série de fonctions

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\☆$

## Énoncé

Étudier l'interversion pour l'intégrale $\int_0^\infty e^{-ax} \sin(bx) dx$ avec $a>0$. Expliquer pourquoi le corollaire direct de Beppo-Levi échoue et comment adapter par séparation partie positive/négative.

## Démonstration rigoureuse pas à pas

La fonction $x \mapsto e^{-ax} \sin(bx)$ n'est pas de signe constant. Pour appliquer Beppo-Levi aux séries, on doit vérifier la sommabilité absolue, soit $\int |e^{-ax} \sin(bx)| dx < \infty$. En majorant $|\sin(bx)| \le 1$, l'intégrale de $|e^{-ax}|$ vaut $1/a < \infty$. La fonction est donc dans $L^1$. L'interversion d'une série associée (par exemple un développement de Taylor du sinus) requerrait d'appliquer le théorème de Lebesgue (Convergence Dominée) ou de séparer $f = f^+ - f^-$ et d'appliquer Beppo-Levi sur chaque partie, qui sont des fonctions positives croissantes dans leurs sommes partielles respectives.
