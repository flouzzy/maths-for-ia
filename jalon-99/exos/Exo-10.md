\subsection*{Exercice 10 : Non-existence d'hyperplan séparateur \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

Donner un exemple dans un espace vectoriel normé de deux ensembles convexes denses disjoints. (Ainsi ils ne peuvent pas être séparés par un hyperplan fermé).

**Correction :**

1. Soit $E = \ell^2(\mathbb{N})$ l'espace des suites de carré sommable.
2. Soit $F$ le sous-espace dense des suites nulles à partir d'un certain rang.
3. Soit $e = (1, 1/2, 1/3, \dots) \in \ell^2$. On pose $c = e \notin F$.
4. Soit $A = \{ x \in F \mid \sum_{i=1}^n x_i e_i = 0 \text{ pour tout } n \}$ mais prenons plutôt un vrai hyperplan dense.
5. Plus simplement, soit $f$ une forme linéaire discontinue sur $E$. Le noyau $H = \ker f$ est un hyperplan dense de $E$.
6. Soit $x_0 \notin H$. L'ensemble $H' = H + x_0$ est aussi dense dans $E$.
7. $H$ et $H'$ sont des convexes disjoints.
8. Si un hyperplan fermé séparait $H$ et $H'$, il contiendrait $H$ (car $H$ est un espace vectoriel dense) ou en serait disjoint. Mais $H$ étant dense, son adhérence est $E$ tout entier, de même pour $H'$.
9. Toute forme linéaire continue qui serait de signe constant sur $H$ serait de signe constant sur $E$, donc nulle, ce qui est absurde pour un hyperplan séparateur.