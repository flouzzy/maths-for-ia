# Exercice 10 : Slutsky et l'arithmétique asymptotique
$\bigstar\bigstar\bigstar\bigstar\bigstar$


Le théorème de Slutsky est un outil indispensable de la statistique inférentielle. Il affirme que si $X_n \xrightarrow{\mathcal{L}} X$ et $Y_n \xrightarrow{\mathbb{P}} c$ (une constante fixée), alors $X_n + Y_n \xrightarrow{\mathcal{L}} X + c$.
On considère $T_n$ une variable aléatoire suivant une loi de Student à $n$ degrés de liberté. On sait que $T_n = \frac{Z}{\sqrt{V_n / n}}$ où $Z \sim \mathcal{N}(0,1)$ et $V_n \sim \chi^2(n)$.
Il est un fait admis que $\frac{V_n}{n} \xrightarrow{\mathbb{P}} 1$.
Démontrez de façon rigoureuse, en utilisant le théorème de Slutsky, la convergence de la loi de Student vers la loi normale.

**Correction :**
1. L'énoncé est construit à partir d'un rapport de variables aléatoires. Nous devons analyser le comportement du dénominateur.
2. Posons $W_n = \sqrt{\frac{V_n}{n}}$. Puisque l'application racine carrée $g(x) = \sqrt{x}$ est continue sur $\mathbb{R}_+^*$, par le théorème de l'application continue (Continuous Mapping Theorem), la convergence en probabilité de l'argument implique la convergence en probabilité de l'image.
Donc $W_n \xrightarrow{\mathbb{P}} \sqrt{1} = 1$.
3. Nous appliquons le Théorème de Slutsky dans sa version du produit/quotient. Il stipule que si une suite de variables ($Z$) converge en loi vers une variable (ici $Z \sim \mathcal{N}(0,1)$, de façon triviale une variable constante est une suite qui converge vers elle-même en loi) et qu'une autre suite ($W_n$) converge en probabilité vers une constante non nulle (ici $c = 1$), alors le rapport de ces variables converge en loi vers le rapport des limites.
4. Concrètement :
$$ \frac{Z}{W_n} \xrightarrow{\mathcal{L}} \frac{Z}{1} $$
5. En remplaçant les termes par la définition de l'énoncé :
$$ T_n = \frac{Z}{\sqrt{V_n / n}} \xrightarrow{\mathcal{L}} Z \sim \mathcal{N}(0, 1) $$
Ceci est la preuve formelle fondamentale justifiant l'utilisation des tables statistiques normales en lieu et place des tables de Student dès que la taille de l'échantillon $n$ dépasse 30.
