# Exercice 2

## Exercice 2 : Toute suite fortement convergente est faiblement convergente \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $E$ un espace vectoriel normé et $(x_n)_{n \ge 1}$ une suite de $E$. Montrer que si $(x_n)$ converge fortement vers $x$, alors elle converge faiblement vers $x$. Montrer par un exemple que la réciproque est fausse en dimension infinie.

**Correction :**
*Analyse de l'énoncé :* La première partie est une simple application de la continuité des formes linéaires. La seconde partie requiert de se placer dans un espace de dimension infinie, par exemple un espace de Hilbert.
*Résolution pas-à-pas :*
1. **Étape 1 : Forte implique faible.**
   Supposons que $\lim_{n \to \infty} \|x_n - x\| = 0$. Soit $f \in E^*$. Comme $f$ est continue, elle conserve les limites.
   On a $|f(x_n) - f(x)| = |f(x_n - x)| \le \|f\|_{E^*} \|x_n - x\|$.
   Puisque $\|x_n - x\| \to 0$, on a $|f(x_n) - f(x)| \to 0$. Donc $f(x_n) \to f(x)$ pour tout $f \in E^*$.
   Cela signifie exactement que $x_n \rightharpoonup x$.
2. **Étape 2 : Contre-exemple pour la réciproque.**
   Considérons $E = \ell^2(\mathbb{N})$, l'espace des suites de carré sommable, avec la base canonique $(e_n)_{n \ge 0}$.
   Pour tout élément $y = (y_k)_{k \ge 0} \in \ell^2$, le produit scalaire $\langle y, e_n \rangle = y_n$.
   Comme la série $\sum |y_k|^2$ converge, on a nécessairement $\lim_{n \to \infty} y_n = 0$.
   Par le théorème de représentation de Riesz, toute forme $f \in E^*$ s'écrit $f(x) = \langle y, x \rangle$ pour un certain $y \in \ell^2$.
   Donc $\lim_{n \to \infty} f(e_n) = 0$. Ainsi $e_n \rightharpoonup 0$ faiblement.
   Pourtant, $\|e_n - 0\| = \|e_n\| = 1$ ne tend pas vers 0. La suite $(e_n)$ ne converge pas fortement vers 0.
