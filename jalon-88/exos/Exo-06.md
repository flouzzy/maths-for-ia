# Exercice 6 : Covariance nulle n'implique pas l'indépendance \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**

Soit $X$ une variable aléatoire suivant une loi normale centrée réduite $\mathcal{N}(0,1)$.
Soit $Y = X^2$.
1. Calculer la covariance entre $X$ et $Y$, $\text{Cov}(X,Y)$.
2. Les variables aléatoires $X$ et $Y$ sont-elles indépendantes ? Justifier rigoureusement.

**Correction Détaillée :**

1. **Calcul de la covariance :**
   - La covariance est définie par $\text{Cov}(X,Y) = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]$.
   - Puisque $X \sim \mathcal{N}(0,1)$, son espérance est nulle : $\mathbb{E}[X] = 0$.
   - Le produit des espérances est donc nul : $\mathbb{E}[X]\mathbb{E}[Y] = 0 \cdot \mathbb{E}[X^2] = 0$.
   - Il reste à calculer $\mathbb{E}[XY]$. Substituons $Y = X^2$ : $\mathbb{E}[XY] = \mathbb{E}[X \cdot X^2] = \mathbb{E}[X^3]$.
   - $X$ suit une loi normale centrée, sa fonction de densité $f(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ est paire ($f(-x) = f(x)$).
   - L'espérance du cube est donnée par l'intégrale $\int_{-\infty}^{\infty} x^3 f(x) dx$. L'intégrande $x \mapsto x^3 f(x)$ est le produit d'une fonction impaire ($x^3$) et d'une fonction paire ($f(x)$), c'est donc une fonction impaire.
   - L'intégrale d'une fonction impaire sur un domaine symétrique par rapport à l'origine (ici de $-\infty$ à $+\infty$) est nulle (sous réserve d'intégrabilité absolue, ce qui est le cas ici grâce à la décroissance exponentielle rapide de la Gaussienne).
   - Ainsi, $\mathbb{E}[X^3] = 0$.
   - En conclusion, $\text{Cov}(X,Y) = 0 - 0 = 0$. Les variables $X$ et $Y$ sont dites décorrélées.
2. **Examen de l'indépendance :**
   - Par définition, $X$ et $Y$ sont indépendantes si pour tous boréliens $A, B$, $\mathbb{P}(X \in A, Y \in B) = \mathbb{P}(X \in A)\mathbb{P}(Y \in B)$.
   - Considérons des événements spécifiques pour trouver un contre-exemple. Soit l'événement $\{X \in [1, 2]\}$. Si cet événement est réalisé, alors nécessairement $Y = X^2 \in [1, 4]$.
   - Considérons alors l'événement contradictoire pour $Y$ : $\{Y \in [5, 6]\}$.
   - Calculons la probabilité jointe : $\mathbb{P}(X \in [1, 2] \text{ et } Y \in [5, 6])$. Il est impossible que $X$ soit entre $1$ et $2$ tandis que son carré $X^2$ soit entre $5$ et $6$. Donc cette probabilité est $0$.
   - Calculons le produit des probabilités marginales :
     - $\mathbb{P}(X \in [1, 2]) > 0$ car l'intervalle est de longueur non nulle et la densité gaussienne est strictement positive partout.
     - $\mathbb{P}(Y \in [5, 6]) = \mathbb{P}(X^2 \in [5, 6]) = \mathbb{P}(X \in [\sqrt{5}, \sqrt{6}] \cup [-\sqrt{6}, -\sqrt{5}]) > 0$.
   - Le produit des probabilités marginales est donc strictement positif ($>0$), tandis que la probabilité de l'intersection est nulle ($=0$).
   - Ces deux valeurs étant différentes, la relation d'indépendance n'est pas satisfaite.
   - **Conclusion :** $X$ et $Y$ ne sont pas indépendantes. Cet exercice prouve qu'une covariance nulle n'implique pas l'indépendance (sauf dans le cas très particulier des vecteurs gaussiens, ce qui n'est pas le cas du couple $(X, X^2)$).
