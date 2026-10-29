# Exercice 3

## Exercice 3 : Convergence faible et opérateurs compacts \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soient $E$ et $F$ des espaces de Banach, et $T : E \to F$ un opérateur linéaire compact. Montrer que si une suite $(x_n)_{n \ge 1}$ converge faiblement vers $x$ dans $E$, alors la suite $(T(x_n))_{n \ge 1}$ converge fortement vers $T(x)$ dans $F$.

**Correction :**
*Analyse de l'énoncé :* Un opérateur compact transforme une suite faiblement convergente (qui est nécessairement bornée) en une suite admettant une sous-suite fortement convergente.
*Résolution pas-à-pas :*
1. **Étape 1 : Bornitude de la suite.**
   Puisque $x_n \rightharpoonup x$, par le théorème de Banach-Steinhaus, la suite $(x_n)$ est bornée en norme : il existe $M > 0$ tel que $\|x_n\| \le M$.
2. **Étape 2 : Compacité de l'image.**
   L'opérateur $T$ étant compact, l'image de toute suite bornée admet une sous-suite convergente. Donc la suite $(T(x_n))$ a ses valeurs dans un ensemble relativement compact de $F$.
3. **Étape 3 : Convergence faible de l'image.**
   Montrons que $T(x_n) \rightharpoonup T(x)$ faiblement dans $F$. Soit $g \in F^*$. Alors $g \circ T \in E^*$.
   Puisque $x_n \rightharpoonup x$, on a $(g \circ T)(x_n) \to (g \circ T)(x)$, soit $g(T(x_n)) \to g(T(x))$.
   Ceci prouve que $T(x_n) \rightharpoonup T(x)$ faiblement.
4. **Étape 4 : Passage de la convergence faible à la convergence forte dans un compact.**
   Raisonnons par l'absurde. Supposons que $T(x_n)$ ne converge pas fortement vers $T(x)$.
   Alors il existe $\epsilon > 0$ et une sous-suite $(x_{\phi(n)})$ telle que $\|T(x_{\phi(n)}) - T(x)\| \ge \epsilon$ pour tout $n$.
   La sous-suite $(x_{\phi(n)})$ est toujours bornée. Par compacité de $T$, la suite $(T(x_{\phi(n)}))$ possède une sous-suite $(T(x_{\psi(n)}))$ qui converge fortement vers un point $y \in F$.
   Mais la convergence forte implique la convergence faible. Donc $T(x_{\psi(n)}) \rightharpoonup y$.
   Or, nous savons par l'étape 3 que toute sous-suite de $T(x_n)$ converge faiblement vers $T(x)$. Par unicité de la limite faible, $y = T(x)$.
   Mais ceci contredit le fait que $\|T(x_{\psi(n)}) - T(x)\| \ge \epsilon$.
   La supposition initiale était donc fausse : $T(x_n)$ converge fortement vers $T(x)$.
