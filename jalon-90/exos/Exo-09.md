\subsection*{Exercice 9 : Théorème de représentation de Skorokhod \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

On suppose que des variables aléatoires réelles $X_n$ convergent en loi vers $X$.
Énoncer le théorème de représentation de Skorokhod et l'utiliser pour prouver le Continuous Mapping Theorem (Si $X_n \xrightarrow{\mathcal{L}} X$ et $g$ continue, alors $g(X_n) \xrightarrow{\mathcal{L}} g(X)$).

**Correction :**
Le théorème de représentation de Skorokhod affirme que si $X_n \xrightarrow{\mathcal{L}} X$, alors il existe un espace probabilisé unifié $(\Omega, \mathcal{F}, \mathbb{P})$ et des variables aléatoires $Y_n, Y$ définies sur cet espace, telles que :
1. $Y_n$ a la même loi que $X_n$ pour tout $n$.
2. $Y$ a la même loi que $X$.
3. $Y_n \xrightarrow{p.s.} Y$.
Prouvons le Continuous Mapping Theorem avec ce puissant outil.
Soit $g : \mathbb{R} \to \mathbb{R}$ une fonction continue.
Puisque $Y_n \xrightarrow{p.s.} Y$, pour presque tout $\omega \in \Omega$, la limite de la suite $Y_n(\omega)$ est $Y(\omega)$.
Par continuité numérique usuelle de la fonction $g$, nous avons pour ces mêmes $\omega$ : $\lim_{n \to \infty} g(Y_n(\omega)) = g(Y(\omega))$.
Cela signifie précisément que $g(Y_n) \xrightarrow{p.s.} g(Y)$.
D'après la hiérarchie des convergences, la convergence presque sûre implique la convergence en probabilité, qui elle-même implique la convergence en loi.
Donc $g(Y_n) \xrightarrow{\mathcal{L}} g(Y)$.
Enfin, puisque $Y_n \sim X_n$, alors par substitution stricte des lois, $g(Y_n) \sim g(X_n)$. De même, $g(Y) \sim g(X)$.
Il en découle trivialement que $g(X_n) \xrightarrow{\mathcal{L}} g(X)$. Le théorème de continuité (Continuous Mapping Theorem) est démontré.
