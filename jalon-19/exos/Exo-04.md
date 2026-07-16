---
titre: "Exercice 4 : Dérivabilité"
difficulte: "★★☆☆☆"
---

# Exercice 4 : Pratique et maîtrise conceptuelle

**Énoncé :**
Soit $f$ une fonction dérivable sur $[0,1]$ telle que $f(0)=0$ et $f(1)=1$. Montrer qu'il existe des points distincts $x_1, \dots, x_n$ dans $]0,1[$ tels que $\sum_{i=1}^n \frac{1}{f'(x_i)} = n$.

**Résolution Zéro Ellipse :**
1. Subdivisons l'intervalle $[0,1]$ de l'axe des ordonnées en $n$ sous-intervalles de longueur égale $1/n$ : posons $y_k = \frac{k}{n}$ pour $k \in \llbracket 0, n \rrbracket$.
2. Le théorème des valeurs intermédiaires (TVI), applicable car $f$ est dérivable donc continue, assure l'existence de points pré-images.
3. Puisque $f(0) = 0$ et $f(1) = 1$, pour chaque $k \in \llbracket 0, n \rrbracket$, l'ensemble $f^{-1}(\{y_k\})$ est non vide.
4. Pour garantir l'ordre et définir des intervalles de TAF, définissons $a_k = \inf \{ x \in [0,1] \mid f(x) = y_k \}$. Par continuité de $f$ et compacité de $[0,1]$, le minimum est atteint, donc $f(a_k) = y_k$.
5. Par construction de la suite des valeurs cibles $y_k$, nous avons une séquence strictement croissante de valeurs : $f(a_0) < f(a_1) < \dots < f(a_n)$.
6. Ce qui implique nécessairement $a_0 < a_1 < \dots < a_n$, définissant ainsi une subdivision canonique de l'intervalle source $[0,1]$.
7. Sur chaque sous-intervalle $[a_{k-1}, a_k]$ (pour $k \in \llbracket 1, n \rrbracket$), $f$ est continue et dérivable sur l'ouvert correspondant.
8. Le Théorème des Accroissements Finis s'applique : il existe au moins un point $x_k \in ]a_{k-1}, a_k[$ tel que :
   $$ f(a_k) - f(a_{k-1}) = f'(x_k)(a_k - a_{k-1}) $$
9. Or, par définition des cibles, l'incrément vertical est constant : $f(a_k) - f(a_{k-1}) = y_k - y_{k-1} = \frac{k}{n} - \frac{k-1}{n} = \frac{1}{n}$.
10. Nous pouvons alors isoler la quantité d'intérêt (en supposant $f'(x_k) \neq 0$, ce qui est garanti par l'équation puisque l'incrément vertical est strictement positif) :
    $$ \frac{1}{n} = f'(x_k)(a_k - a_{k-1}) \implies \frac{1}{f'(x_k)} = n(a_k - a_{k-1}) $$
11. Sommons ces identités sur l'ensemble des intervalles $k$ de $1$ à $n$ :
    $$ \sum_{k=1}^n \frac{1}{f'(x_k)} = \sum_{k=1}^n n(a_k - a_{k-1}) = n \sum_{k=1}^n (a_k - a_{k-1}) $$
12. La somme résultante est une somme télescopique parfaite :
    $$ \sum_{k=1}^n (a_k - a_{k-1}) = (a_n - a_{n-1}) + (a_{n-1} - a_{n-2}) + \dots + (a_1 - a_0) = a_n - a_0 $$
13. Or, par définition des conditions aux limites, $a_0 = 0$ et $a_n = 1$. L'amplitude totale est donc $1$.
14. Par substitution finale, l'identité devient $\sum_{k=1}^n \frac{1}{f'(x_k)} = n(1 - 0) = n$.
15. Les points $x_k$ étant isolés dans des intervalles disjoints $]a_{k-1}, a_k[$, ils sont rigoureusement distincts. La proposition est démontrée. $\blacksquare$
