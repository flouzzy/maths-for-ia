# Exercice 9 : Continuité sous le signe intégrale ★★★★★

## Énoncé
Soit $f : \mathbb{R} \times X \to [0, +\infty]$ une fonction mesurable en la deuxième variable pour tout $t$, et continue en la première variable en un point $t_0$.
Peut-on utiliser le TCM pour prouver que $t \mapsto \int_X f(t, x) d\mu(x)$ est continue en $t_0$ ?

## Correction Détaillée
1. **Le problème du TCM** : Le théorème de convergence monotone exige une suite **croissante** de fonctions. La continuité en $t_0$ implique que pour toute suite $t_n \to t_0$, $f(t_n, x) \to f(t_0, x)$. Mais il n'y a aucune raison que la suite de fonctions $f_n(x) = f(t_n, x)$ soit croissante.
2. **Nécessité de la croissance** : Prenons un contre-exemple. $f(t, x) = \frac{t}{t^2 + x^2}$ sur $]0, 1[$. Pour $t \to 0$, $f(t, x) \to 0$ pour tout $x \neq 0$. L'intégrale limite est $0$. Mais $\int_0^1 f(t, x) dx = [\arctan(x/t)]_0^1 = \arctan(1/t) \to \pi/2$ quand $t \to 0^+$. Il n'y a pas continuité de l'intégrale.
3. **Le bon outil** : Pour prouver la continuité sous le signe intégrale sans hypothèse de croissance, on utilise le **Théorème de Convergence Dominée** de Lebesgue (qui fait l'objet du Jalon 69) ou on se ramène à des hypothèses de domination (par exemple $|f(t, x)| \le g(x)$ où $g$ est intégrable).
4. **Leçon** : Le TCM est puissant mais très rigide concernant l'hypothèse de croissance.
