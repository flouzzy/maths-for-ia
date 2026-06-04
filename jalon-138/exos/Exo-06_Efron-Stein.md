# Exercice 6 : Inégalité d'Efron-Stein et contrôle de la variance (Niveau 6)

## Énoncé
Soient $X_1, \dots, X_n$ des variables aléatoires indépendantes à valeurs dans des ensembles $\mathcal{X}_1, \dots, \mathcal{X}_n$.
Soit $f : \prod_{i=1}^n \mathcal{X}_i \to \mathbb{R}$ une fonction mesurable carrée intégrable par rapport à la loi conjointe.
Soient $X'_1, \dots, X'_n$ des copies indépendantes des variables $X_1, \dots, X_n$ (échantillon fantôme).
On note $Z = f(X_1, \dots, X_n)$ et pour tout $i \in \{1, \dots, n\}$, on note :
$$Z'_i = f(X_1, \dots, X_{i-1}, X'_i, X_{i+1}, \dots, X_n)$$
L'inégalité d'Efron-Stein (1981) permet de borner la variance de $Z$ :
$$\text{Var}(Z) \le \frac{1}{2} \sum_{i=1}^n \mathbb{E}\big[(Z - Z'_i)^2\big]$$
1. Démontrer cette inégalité dans le cas simple $n=2$.
2. En utilisant ce résultat, en déduire une borne pour la variance d'une fonction satisfaisant la propriété des différences bornées de McDiarmid.

---

## Correction Détaillée

### 1. Démonstration pour $n=2$
Soit $Z = f(X_1, X_2)$. Notons $\mathbb{E}_1$ l'espérance conditionnelle par rapport à $X_2$ (intégration par rapport à $X_1$) et $\mathbb{E}_2$ par rapport à $X_1$ (intégration par rapport à $X_2$).
Rappelons que pour toute variable aléatoire $Y$ :
$$\text{Var}(Y) = \mathbb{E}[Y^2] - (\mathbb{E}[Y])^2 = \mathbb{E}\big[\text{Var}(Y \mid \mathcal{G})\big] + \text{Var}\big(\mathbb{E}[Y \mid \mathcal{G}]\big)$$
Appliquons cette décomposition de la variance (formule de la variance totale) à $Z = f(X_1, X_2)$ conditionnellement à $X_2$ :
$$\text{Var}(Z) = \mathbb{E}[\text{Var}(Z \mid X_2)] + \text{Var}(\mathbb{E}[Z \mid X_2])$$

- Étudions le premier terme $\mathbb{E}[\text{Var}(Z \mid X_2)]$. 
Puisque $X'_1$ est une copie indépendante de $X_1$, la variance conditionnelle de $Z$ sachant $X_2$ s'écrit comme la demi-différence au carré :
$$\text{Var}(Z \mid X_2) = \frac{1}{2} \mathbb{E}_1 \big[ (Z - Z'_1)^2 \mid X_2 \big]$$
En prenant l'espérance globale :
$$\mathbb{E}[\text{Var}(Z \mid X_2)] = \frac{1}{2} \mathbb{E}\big[(Z - Z'_1)^2\big]$$

- Étudions maintenant le second terme $\text{Var}(\mathbb{E}[Z \mid X_2])$. 
Notons $g(X_2) = \mathbb{E}[Z \mid X_2] = \mathbb{E}_1[f(X_1, X_2)]$. C'est une fonction de la seule variable aléatoire indépendante $X_2$.
Sa variance s'écrit de la même façon en introduisant la copie indépendante $X'_2$ :
$$\text{Var}(g(X_2)) = \frac{1}{2} \mathbb{E}\big[(g(X_2) - g(X'_2))^2\big]$$

Par l'inégalité de Jensen appliquée à l'espérance conditionnelle par rapport à $X_1, X'_1$ (qui est un opérateur linéaire de moyenne de norme 1 dans $L^2$) :
$$(g(X_2) - g(X'_2))^2 = \Big( \mathbb{E}[ f(X_1, X_2) - f(X_1, X'_2) \mid X_2, X'_2 ] \Big)^2 \le \mathbb{E}\big[ (f(X_1, X_2) - f(X_1, X'_2))^2 \mid X_2, X'_2 \big]$$
En prenant l'espérance globale :
$$\text{Var}(\mathbb{E}[Z \mid X_2]) \le \frac{1}{2} \mathbb{E}\big[(Z - Z'_2)^2\big]$$

En combinant les deux termes, nous obtenons :
$$\text{Var}(Z) \le \frac{1}{2} \mathbb{E}\big[(Z - Z'_1)^2\big] + \frac{1}{2} \mathbb{E}\big[(Z - Z'_2)^2\big] = \frac{1}{2} \sum_{i=1}^2 \mathbb{E}\big[(Z - Z'_i)^2\big]$$
L'inégalité d'Efron-Stein est démontrée pour $n=2$.

### 2. Borne sur la variance d'une fonction Lipschitzienne (McDiarmid)
Supposons que $f$ satisfasse la propriété des différences bornées avec les constantes $c_1, \dots, c_n$.
Par définition, pour tout $i \in \{1, \dots, n\}$, et pour tout choix de variables :
$$|Z - Z'_i| = |f(X_1, \dots, X_i, \dots, X_n) - f(X_1, \dots, X'_i, \dots, X_n)| \le c_i \quad \text{presque sûrement.}$$

En élevant au carré et en prenant l'espérance :
$$\mathbb{E}\big[(Z - Z'_i)^2\big] \le c_i^2$$

Par application directe de l'inégalité d'Efron-Stein :
$$\text{Var}(Z) \le \frac{1}{2} \sum_{i=1}^n \mathbb{E}\big[(Z - Z'_i)^2\big] \le \frac{1}{2} \sum_{i=1}^n c_i^2$$

### Conclusion
Ce résultat montre que pour toute fonction satisfaisant l'hypothèse de McDiarmid, sa variance est toujours majorée par $\frac{1}{2} \sum_{i=1}^n c_i^2$. 
C'est une information très précieuse car cela donne un contrôle immédiat du second moment. Si l'on combine ce contrôle de la variance avec l'inégalité de Bienaymé-Tchebychev, on obtiendrait une concentration de la forme $\mathcal{O}(1/t^2)$. McDiarmid va plus loin en fournissant une concentration exponentielle, mais Efron-Stein permet de borner la variance de manière extrêmement directe et robuste.
