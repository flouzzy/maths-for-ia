# Exercice 5 : Défaut de convergence sans domination

**Difficulté :** $\bigstar\bigstar\bigstar\☆☆$

## Énoncé

Montrer par un contre-exemple que si $(f_n)$ n'est ni positive ni croissante, le théorème d'interversion peut échouer.

## Démonstration rigoureuse pas à pas

Prenons la suite $f_n(x) = n^2 x e^{-nx}$ sur $]0, 1[$. Pour $x>0$ fixé, $f_n(x) \to 0$ (par croissance comparée de l'exponentielle). Mais l'intégrale vaut $\int_0^1 n^2 x e^{-nx} dx$. Avec le changement de variable $u = nx$, $dx = du/n$, on a $\int_0^n u e^{-u} du$. Quand $n \to \infty$, cette intégrale tend vers $\int_0^\infty u e^{-u} du = \Gamma(2) = 1$. L'intégrale de la limite est $\int 0 = 0 \neq 1$. La suite n'est pas croissante, empêchant l'application de Beppo-Levi.
