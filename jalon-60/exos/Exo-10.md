# Exercice 10 : Mesure de Radon $\bigstar\bigstar\bigstar\bigstar\bigstar$
Soit $I_n$ compact. Si $\int_{I_n} f(x) d\mu(x) = 0$ pour toute $f \in \mathcal{C}(I_n)$, démontrer que la mesure de Radon signée $\mu$ est nulle, en invoquant le théorème de représentation de Riesz.

\textbf{Correction détaillée}
Le théorème de représentation de Riesz-Markov-Kakutani énonce que pour tout espace localement compact séparé $X$ (ici $I_n$ compact, donc localement compact), il existe un isomorphisme isométrique entre l'espace dual $C_0(X)^*$ (ici $\mathcal{C}(I_n)^*$ car $I_n$ compact) et l'espace des mesures de Radon régulières signées finies sur $X$, noté $\mathcal{M}(X)$, muni de la norme en variation totale.
Soit l'opérateur $T : \mathcal{M}(I_n) \to \mathcal{C}(I_n)^*$ défini par $T(\mu)(f) = \int_{I_n} f d\mu$.
Le fait que $T$ soit une isométrie implique que $\|T(\mu)\|_{C^*} = \|\mu\|_{TV}$.
L'hypothèse indique que pour toute $f \in \mathcal{C}(I_n)$, $T(\mu)(f) = 0$.
Donc la forme linéaire $T(\mu)$ est la forme identiquement nulle dans $\mathcal{C}(I_n)^*$.
Par l'isométrie, $\|\mu\|_{TV} = \|0\|_{C^*} = 0$.
Une mesure dont la variation totale est nulle est identiquement nulle sur tous les boréliens. Donc $\mu = 0$.
