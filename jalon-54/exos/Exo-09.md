## Exercice 9 : Compacité et valeurs d'adhérence \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :** Soit $X$ un espace métrique compact. Démontrer qu'une suite $(x_n)_{n \in \mathbb{N}}$ d'éléments de $X$ converge si et seulement si elle possède une unique valeur d'adhérence.

**Correction Détaillée :**
$(\implies)$ Si $(x_n)$ converge vers $l \in X$, alors toute sous-suite converge également vers $l$. L'unique valeur d'adhérence est donc $l$. Ceci est vrai dans tout espace topologique séparé.
$(\impliedby)$ C'est ici qu'intervient la compacité. Supposons que $(x_n)$ admette une unique valeur d'adhérence $l \in X$. Montrons que la suite converge vers $l$.
Raisonnons par l'absurde en supposant que la suite ne converge pas vers $l$.
Cela signifie qu'il existe un voisinage ouvert $V$ de $l$ et une sous-suite $(x_{\phi(n)})$ telle que, pour tout $n$, $x_{\phi(n)} \notin V$.
Considérons cette sous-suite $(x_{\phi(n)})$ évoluant dans le fermé $F = X \setminus V$.
Le fermé $F$ est un sous-espace fermé du compact $X$, il est donc lui-même compact.
La suite $(x_{\phi(n)})$ évoluant dans le compact $F$, elle admet (par compacité séquentielle) une sous-suite convergente vers une limite $l' \in F$.
Cette double extraction de sous-suite est toujours une sous-suite de la suite originelle $(x_n)$.
Donc la limite $l'$ est une valeur d'adhérence de la suite initiale $(x_n)$.
Or, par construction, $l' \in F = X \setminus V$, et comme $l \in V$, on a nécessairement $l' \neq l$.
Nous avons ainsi trouvé une seconde valeur d'adhérence $l'$ distincte de $l$, ce qui contredit l'hypothèse de l'unicité de la valeur d'adhérence.
L'hypothèse que la suite ne convergeait pas vers $l$ est donc fausse. La suite converge bien vers $l$.