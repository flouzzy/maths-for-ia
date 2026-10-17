# Exercice 10 : LFGN pour l'entropie empirique et loi de Shannon-McMillan-Breiman \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Soit $(X_n)$ une suite i.i.d. à valeurs dans un alphabet fini $\mathcal{A}$, de loi de probabilité $P(X_1 = a) = p(a) > 0$.
On définit la probabilité empirique d'un mot $X_1\dots X_n$ par $p_n(X_1, \dots, X_n) = \prod_{i=1}^n p(X_i)$.
Montrer que $-\frac{1}{n} \log p_n(X_1, \dots, X_n) \xrightarrow{p.s.} H(X)$, où $H(X) = -\sum_{a \in \mathcal{A}} p(a) \log p(a)$ est l'entropie de Shannon.

## Correction Détaillée
### Étape 1 : Transformation logarithmique
Le produit $p_n(X_1, \dots, X_n) = \prod_{i=1}^n p(X_i)$ est la probabilité théorique de réaliser exactement la séquence qui a été tirée.
Prenons le logarithme de cette quantité. Le log transforme un produit en somme :
$$ \log p_n(X_1, \dots, X_n) = \sum_{i=1}^n \log p(X_i) $$
Divisons par $-n$ :
$$ -\frac{1}{n} \log p_n(X_1, \dots, X_n) = -\frac{1}{n} \sum_{i=1}^n \log p(X_i) $$

### Étape 2 : Définition des variables i.i.d.
Posons $Y_i = -\log p(X_i)$. Puisque les $X_i$ sont i.i.d., les variables $Y_i$ obtenues par la fonction déterministe $f(x) = -\log p(x)$ sont également i.i.d.
L'espace d'état $\mathcal{A}$ est fini, et pour tout $a \in \mathcal{A}$, $p(a) > 0$. Ainsi, la variable $Y_1$ ne prend qu'un nombre fini de valeurs finies. Elle est donc évidemment intégrable ($\mathbb{E}[|Y_1|] < \infty$).

### Étape 3 : Calcul de l'espérance théorique
L'espérance de la variable $Y_1$ se calcule directement par le théorème de transfert :
$$ \mathbb{E}[Y_1] = \mathbb{E}[-\log p(X_1)] = \sum_{a \in \mathcal{A}} P(X_1 = a) (-\log p(a)) = -\sum_{a \in \mathcal{A}} p(a) \log p(a) $$
On reconnaît exactement l'expression mathématique de l'entropie de Shannon $H(X)$.

### Étape 4 : Application de la LFGN
Nous avons une moyenne empirique de variables i.i.d. intégrables :
$$ \frac{1}{n} \sum_{i=1}^n Y_i $$
Par le théorème de la loi forte des grands nombres de Kolmogorov, cette moyenne empirique converge presque sûrement vers son espérance théorique $\mathbb{E}[Y_1]$.
Ainsi :
$$ -\frac{1}{n} \log p_n(X_1, \dots, X_n) \xrightarrow{p.s.} H(X) $$

### Remarque d'information théorique
Ce résultat, connu sous le nom de théorème de la propriété d'équipartition asymptotique (AEP) ou forme simple du théorème de Shannon-McMillan-Breiman, est fondamental en théorie de l'information. Il démontre que, presque sûrement, la probabilité d'une séquence typique de longueur $n$ se concentre autour de $2^{-n H(X)}$, ce qui permet de définir le taux limite de compression de données sans perte. $\blacksquare$
