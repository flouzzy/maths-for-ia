---
uuid: "jalon-96"
title: "Livrable IA T8 : Convergence de la Cross-Entropy vers l'Entropie de Shannon"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/theorie-information
prev: "[[Jalon 95 (Vecteurs gaussiens).md]]"
next: "[[Jalon 97 (Espaces de Banach).md]]"
---
# Jalon 96 : Convergence de la Cross-Entropy vers l'Entropie de Shannon

### Introduction aux fondements théoriques

L'étude de l'information constitue une pierre angulaire des mathématiques contemporaines et de leurs applications technologiques. Le concept d'information, quantifié pour la première fois avec une rigueur mathématique par Claude Shannon en 1948, a transformé notre compréhension de la communication, du codage et de la transmission de données. Initialement développée pour résoudre des problèmes d'ingénierie des télécommunications, la théorie de l'information a rapidement démontré sa pertinence dans des domaines aussi divers que la physique statistique, la logique et, plus récemment, l'intelligence artificielle.

Dans le contexte des modèles de langage, notamment les grands modèles de langage (LLM), l'objectif fondamental de l'entraînement consiste à permettre au modèle d'apprendre la distribution de probabilité sous-jacente des séquences de texte. Pour ce faire, une fonction de perte est employée, la plus courante étant l'entropie croisée. La convergence de cette fonction de perte empirique vers l'entropie théorique de Shannon, ou plus précisément vers l'entropie de la source de données, représente un jalon crucial dans la compréhension des performances et des limites de ces systèmes. Cet exposé détaillera les définitions fondamentales, les preuves rigoureuses de cette convergence et ses implications profondes dans les applications modernes.

### Définitions et Théorèmes fondamentaux

Nous établissons ici les définitions formelles des concepts d'entropie de Shannon, d'entropie croisée et de divergence de Kullback-Leibler, outils indispensables à notre analyse. Chaque définition sera suivie d'un exemple numérique concret pour en illustrer l'application.

#### Entropie de Shannon

Soit $X$ une variable aléatoire discrète prenant ses valeurs dans un ensemble fini $\mathcal{X} = \{x_1, x_2, \ldots, x_k\}$, et soit $P$ la distribution de probabilité associée, telle que $P(X=x_i) = p_i$ pour $i=1, \ldots, k$, avec $\sum_{i=1}^k p_i = 1$.

L'entropie de Shannon de la variable aléatoire $X$, notée $H(X)$, mesure l'incertitude intrinsèque ou la quantité moyenne d'information contenue dans la variable $X$. Elle est définie par:

\begin{equation}
H(X) = -\sum_{i=1}^k p_i \log_2(p_i)
\end{equation}

où le logarithme est généralement pris en base 2, exprimant l'entropie en bits. Par convention, si $p_i=0$, alors $p_i \log_2(p_i) = 0$.

**Exemple numérique :**
Considérons une variable aléatoire $X$ représentant le résultat d'un lancer de dé à six faces.
1.  **Dé équilibré :** La probabilité de chaque face est $p_i = 1/6$ pour $i=1, \ldots, 6$.
    L'entropie est :
    \begin{align*}
    H(X) &= -\sum_{i=1}^6 \frac{1}{6} \log_2\left(\frac{1}{6}\right) \\
    &= -6 \cdot \frac{1}{6} \log_2\left(\frac{1}{6}\right) \\
    &= -\log_2\left(\frac{1}{6}\right) \\
    &= \log_2(6) \approx 2.585 \text{ bits}
    \end{align*}
    Cette valeur indique le nombre moyen de bits nécessaires pour coder le résultat d'un lancer de dé équilibré.
2.  **Dé truqué :** Supposons que le dé soit truqué et ne puisse jamais tomber sur "1". Les probabilités sont alors $P(X=1) = 0$, et $P(X=i) = 1/5$ pour $i=2, \ldots, 6$.
    L'entropie est :
    \begin{align*}
    H(X) &= -0 \cdot \log_2(0) - \sum_{i=2}^6 \frac{1}{5} \log_2\left(\frac{1}{5}\right) \\
    &= -0 + (-5) \cdot \frac{1}{5} \log_2\left(\frac{1}{5}\right) \\
    &= -\log_2\left(\frac{1}{5}\right) \\
    &= \log_2(5) \approx 2.322 \text{ bits}
    \end{align*}
    L'incertitude est réduite car une des possibilités est éliminée, ce qui est reflété par une entropie plus faible.

#### Entropie Croisée

Soient $P$ et $Q$ deux distributions de probabilité discrètes sur le même ensemble fini $\mathcal{X}$. $P$ représente la distribution "vraie" ou observée, tandis que $Q$ représente une distribution "prédite" ou modélisée.

L'entropie croisée de $P$ par rapport à $Q$, notée $H(P, Q)$, est une mesure de la quantité moyenne de bits nécessaires pour identifier un événement tiré de $P$ en utilisant un code optimisé pour la distribution $Q$. Elle est définie par:

\begin{equation}
H(P, Q) = -\sum_{i=1}^k p_i \log_2(q_i)
\end{equation}

où $p_i = P(X=x_i)$ et $q_i = Q(X=x_i)$. Il est essentiel que $q_i > 0$ pour tout $x_i$ tel que $p_i > 0$. Si $q_i=0$ et $p_i > 0$, l'entropie croisée est infinie.

**Exemple numérique :**
Considérons une classification binaire où la vraie distribution des classes pour un échantillon donné est $P = [1, 0]$ (la classe 1 est la vraie, la classe 0 est fausse).
1.  **Prédiction parfaite :** Le modèle prédit $Q = [1, 0]$.
    L'entropie croisée est :
    \begin{align*}
    H(P, Q) &= - (1 \cdot \log_2(1) + 0 \cdot \log_2(0)) \\
    &= - (1 \cdot 0 + 0) \\
    &= 0 \text{ bits}
    \end{align*}
    Une entropie croisée de 0 indique une prédiction parfaite.
2.  **Prédiction imparfaite :** Le modèle prédit $Q = [0.8, 0.2]$.
    L'entropie croisée est :
    \begin{align*}
    H(P, Q) &= - (1 \cdot \log_2(0.8) + 0 \cdot \log_2(0.2)) \\
    &= - \log_2(0.8) \\
    &\approx - (-0.322) \\
    &\approx 0.322 \text{ bits}
    \end{align*}
    Une valeur positive indique une certaine divergence entre la vraie distribution et la prédiction.
3.  **Prédiction erronée :** Le modèle prédit $Q = [0.2, 0.8]$.
    L'entropie croisée est :
    \begin{align*}
    H(P, Q) &= - (1 \cdot \log_2(0.2) + 0 \cdot \log_2(0.8)) \\
    &= - \log_2(0.2) \\
    &\approx - (-2.322) \\
    &\approx 2.322 \text{ bits}
    \end{align*}
    Une erreur de prédiction conduit à une entropie croisée plus élevée.

#### Divergence de Kullback-Leibler (KL)

La divergence de Kullback-Leibler, ou divergence KL, notée $D_{KL}(P || Q)$, est une mesure de la différence entre deux distributions de probabilité $P$ et $Q$. Elle quantifie la perte d'information lorsque $Q$ est utilisée pour approximer $P$.

La divergence KL est définie par:

\begin{equation}
D_{KL}(P || Q) = \sum_{i=1}^k p_i \log_2\left(\frac{p_i}{q_i}\right)
\end{equation}

La divergence KL n'est pas symétrique ($D_{KL}(P || Q) \neq D_{KL}(Q || P)$ en général) et n'est pas une métrique au sens strict. Cependant, elle est toujours non-négative : $D_{KL}(P || Q) \ge 0$, et $D_{KL}(P || Q) = 0$ si et seulement si $P=Q$.

Un lien fondamental entre l'entropie de Shannon, l'entropie croisée et la divergence KL est donné par la relation suivante :

\begin{equation}
D_{KL}(P || Q) = H(P, Q) - H(P)
\end{equation}

Cette relation montre que minimiser l'entropie croisée $H(P, Q)$ revient à minimiser la divergence KL $D_{KL}(P || Q)$ si l'entropie $H(P)$ de la vraie distribution $P$ est constante et indépendante du modèle $Q$.

**Exemple numérique :**
Reprenons l'exemple de classification binaire avec la vraie distribution $P = [1, 0]$.
1.  **Modèle $Q = [0.8, 0.2]$ :**
    Nous avons $H(P) = -(1 \log_2 1 + 0 \log_2 0) = 0$.
    Nous avons $H(P, Q) \approx 0.322$.
    La divergence KL est :
    \begin{align*}
    D_{KL}(P || Q) &= \sum_{i=1}^2 p_i \log_2\left(\frac{p_i}{q_i}\right) \\
    &= 1 \cdot \log_2\left(\frac{1}{0.8}\right) + 0 \cdot \log_2\left(\frac{0}{0.2}\right) \\
    &= \log_2(1.25) \\
    &\approx 0.322 \text{ bits}
    \end{align*}
    On vérifie bien que $D_{KL}(P || Q) = H(P, Q) - H(P) \approx 0.322 - 0 = 0.322$.

2.  **Modèle $Q = [0.2, 0.8]$ :**
    Nous avons $H(P) = 0$.
    Nous avons $H(P, Q) \approx 2.322$.
    La divergence KL est :
    \begin{align*}
    D_{KL}(P || Q) &= 1 \cdot \log_2\left(\frac{1}{0.2}\right) + 0 \cdot \log_2\left(\frac{0}{0.8}\right) \\
    &= \log_2(5) \\
    &\approx 2.322 \text{ bits}
    \end{align*}
    On vérifie à nouveau que $D_{KL}(P || Q) = H(P, Q) - H(P) \approx 2.322 - 0 = 2.322$.

Ces exemples illustrent la quantification de l'information et de la divergence par ces fonctions fondamentales.

### Démonstrations de la convergence

Nous allons démontrer la convergence de l'entropie croisée empirique, utilisée comme fonction de perte lors de l'entraînement, vers son espérance théorique, qui se réduit à l'entropie de Shannon lorsque le modèle apprend parfaitement la distribution de la source. La démonstration s'appuie sur la Loi Forte des Grands Nombres.

#### Cadre de la démonstration

Soit $\mathcal{D} = \{(x_1, y_1), (x_2, y_2), \ldots, (x_N, y_N)\}$ un ensemble d'observations (un "dataset") où chaque $(x_i, y_i)$ est un couple d'entrée-sortie tiré indépendamment et identiquement distribué (i.i.d.) selon une distribution de probabilité jointe vraie $P(X, Y)$. Pour les modèles de langage, $x_i$ peut être le contexte précédent et $y_i$ le mot suivant à prédire.

Soit $Q_{\theta}(Y | X)$ la distribution de probabilité conditionnelle prédite par notre modèle, paramétrée par $\theta$. L'objectif de l'entraînement est de trouver un $\theta$ qui minimise la fonction de perte. La fonction de perte pour une unique observation $(x_i, y_i)$ est donnée par l'entropie croisée du label réel $y_i$ et de la distribution prédite $Q_{\theta}(Y | x_i)$. Puisqu'il s'agit d'un seul point, cela se simplifie en $-\log Q_{\theta}(y_i | x_i)$.

La fonction de perte d'entropie croisée empirique, $L_N(\theta)$, sur l'ensemble de données $\mathcal{D}$ est la moyenne de ces pertes individuelles :

\begin{equation}
L_N(\theta) = -\frac{1}{N} \sum_{i=1}^N \log Q_{\theta}(y_i | x_i)
\end{equation}

L'entropie croisée théorique (ou vraie) de la distribution $P(Y|X)$ par rapport à la distribution $Q_{\theta}(Y|X)$ est définie comme l'espérance de la perte d'un échantillon unique sous la vraie distribution $P(X,Y)$ :

\begin{equation}
H(P, Q_{\theta}) = \mathbb{E}_{(X,Y) \sim P}[-\log Q_{\theta}(Y | X)]
\end{equation}

#### Première étape : Convergence de l'entropie croisée empirique vers l'entropie croisée théorique

Considérons la séquence de variables aléatoires $Z_i = -\log Q_{\theta}(Y_i | X_i)$ pour $i=1, \ldots, N$.
Chaque $Z_i$ est une variable aléatoire car $(X_i, Y_i)$ est un échantillon aléatoire.
Par construction, les échantillons $(X_i, Y_i)$ sont i.i.d., ce qui implique que les variables $Z_i$ sont également i.i.d.
L'espérance de $Z_i$ est donnée par :
\begin{equation}
\mathbb{E}[Z_i] = \mathbb{E}_{(X,Y) \sim P}[-\log Q_{\theta}(Y | X)] = H(P, Q_{\theta})
\end{equation}
Nous supposons que cette espérance existe et est finie, ce qui est généralement le cas pour des modèles bien définis où $Q_{\theta}(y|x) > 0$ pour tous les $y$ ayant une probabilité non nulle sous $P(y|x)$.
La fonction de perte empirique peut être réécrite comme la moyenne arithmétique de ces variables aléatoires $Z_i$:
\begin{equation}
L_N(\theta) = \frac{1}{N} \sum_{i=1}^N Z_i
\end{equation}
Nous pouvons maintenant appliquer la Loi Forte des Grands Nombres (LFGN). Une formulation de la LFGN (par Kolmogorov) stipule que si $Z_1, Z_2, \ldots$ sont des variables aléatoires indépendantes et identiquement distribuées avec une espérance finie $\mathbb{E}[Z_1] = \mu$, alors la moyenne empirique converge presque sûrement vers cette espérance :
\begin{equation}
\lim_{N \to \infty} \frac{1}{N} \sum_{i=1}^N Z_i = \mu \quad \text{presque sûrement}
\end{equation}
En appliquant la LFGN à notre cas, avec $\mu = H(P, Q_{\theta})$, nous obtenons :
\begin{equation}
\lim_{N \to \infty} L_N(\theta) = H(P, Q_{\theta}) \quad \text{presque sûrement}
\end{equation}
Cette démonstration établit rigoureusement que l'entropie croisée empirique calculée sur un ensemble de données d'entraînement suffisamment grand converge presque sûrement vers l'entropie croisée théorique, c'est-à-dire l'espérance de la perte sous la vraie distribution des données.

#### Deuxième étape : Convergence de l'entropie croisée théorique vers l'entropie de Shannon

La première étape a montré que l'entraînement minimise $H(P, Q_{\theta})$. L'objectif ultime d'un modèle est d'apprendre la vraie distribution des données, c'est-à-dire de faire en sorte que $Q_{\theta}(Y | X)$ soit aussi proche que possible de $P(Y | X)$.

Considérons le scénario idéal où le modèle a atteint une performance optimale et que la distribution qu'il a apprise, $Q_{\theta^*}$, est identique à la vraie distribution conditionnelle $P(Y | X)$ de la source. C'est-à-dire, pour tout $(x, y)$:
\begin{equation}
Q_{\theta^*}(y | x) = P(y | x)
\end{equation}
Dans ce cas de correspondance parfaite, l'entropie croisée théorique devient :
\begin{align*}
H(P, Q_{\theta^*}) &= \mathbb{E}_{(X,Y) \sim P}[-\log Q_{\theta^*}(Y | X)] \\
&= \mathbb{E}_{(X,Y) \sim P}[-\log P(Y | X)]
\end{align*}
Par la définition de l'espérance sur une distribution jointe $P(X,Y)$:
\begin{align*}
\mathbb{E}_{(X,Y) \sim P}[-\log P(Y | X)] &= \sum_x \sum_y P(x, y) (-\log P(y | x)) \\
&= \sum_x \sum_y P(x)P(y | x) (-\log P(y | x)) \\
&= \sum_x P(x) \left( -\sum_y P(y | x) \log P(y | x) \right)
\end{align*}
L'expression entre parenthèses, $-\sum_y P(y | x) \log P(y | x)$, est précisément l'entropie conditionnelle $H(Y | X=x)$ pour une valeur donnée de $X=x$. Par conséquent, l'expression entière est l'espérance de l'entropie conditionnelle, qui est par définition l'entropie conditionnelle moyenne $H(Y | X)$:
\begin{equation}
H(Y | X) = \sum_x P(x) H(Y | X=x) = \mathbb{E}_X[H(Y | X)]
\end{equation}
Donc, lorsque $Q_{\theta^*}(Y | X) = P(Y | X)$, l'entropie croisée théorique converge vers l'entropie conditionnelle de la source :
\begin{equation}
H(P, Q_{\theta^*}) = H(Y | X)
\end{equation}
L'entropie $H(Y | X)$ représente l'incertitude résiduelle sur $Y$ une fois que $X$ est connu, qui est la quantité minimale d'information nécessaire pour spécifier $Y$ étant donné $X$. C'est l'entropie de Shannon de la variable cible $Y$ conditionnée par la variable d'entrée $X$.

**Conclusion de la convergence :**
En combinant les deux étapes, nous constatons que l'entraînement d'un modèle de langage à l'aide de la fonction de perte d'entropie croisée vise à minimiser une quantité empirique qui converge vers l'entropie conditionnelle de Shannon de la source de données $H(Y | X)$. Plus précisément, si un modèle est capable d'apprendre la distribution de probabilité vraie $P(Y|X)$, sa perte d'entropie croisée sur un ensemble de données infini convergera vers $H(Y|X)$. Cette convergence démontre le lien intrinsèque entre l'entraînement des modèles probabilistes et les fondements de la théorie de l'information.

### Applications en Physique, Logique & Intelligence Artificielle

Les concepts d'entropie et d'information ont transcendé les frontières de la théorie de la communication, s'implantant profondément dans diverses disciplines scientifiques et technologiques.

#### Physique

En physique statistique, l'entropie est une mesure fondamentale du désordre ou de l'incertitude d'un système. L'entropie de Boltzmann ($S = k \log W$) et l'entropie de Gibbs ($\sum_i p_i \log p_i$) sont des concepts qui prédatent les travaux de Shannon mais partagent une forme mathématique similaire et une interprétation conceptuelle liée à l'incertitude sur l'état microscopique d'un système. La maximisation de l'entropie, par exemple, est un principe clé pour dériver les distributions de probabilité d'équilibre en physique statistique, en supposant que le système se trouve dans l'état le plus désordonné compatible avec les contraintes connues. Ce principe est directement lié à la théorie de l'information, où maximiser l'entropie signifie choisir la distribution la moins informative (la plus incertaine) qui respecte les données observées. Le lien entre l'information et l'énergie, comme dans le démon de Maxwell, ou entre l'information et la thermodynamique des trous noirs (entropie de Bekenstein-Hawking), souligne la portée universelle de ces principes.

#### Logique

En logique et en théorie de la décision, l'entropie de Shannon offre un moyen de quantifier l'information contenue dans des propositions ou des ensembles de faits. Dans un arbre de décision, par exemple, l'information gagnée (réduction de l'entropie) est utilisée pour sélectionner le meilleur attribut de division. Le principe du minimum de description de longueur (MDL) est également ancré dans la théorie de l'information, stipulant que la meilleure théorie pour expliquer des données est celle qui permet la description la plus courte des données et de la théorie elle-même. Cela revient à minimiser la somme du coût de codage du modèle et du coût de codage des données à l'aide du modèle, ce qui est directement lié à la divergence KL et à l'entropie croisée. La logique inductive et la modélisation statistique s'appuient sur ces notions pour inférer des structures à partir de données en quantifiant la complexité et l'information.

#### Intelligence Artificielle (Spécifiquement l'entraînement des LLM)

Dans le domaine de l'intelligence artificielle, et plus particulièrement pour l'entraînement des grands modèles de langage (LLM), la fonction de perte d'entropie croisée est prépondérante. Son rôle est multiple et fondamental :

1.  **Fonction d'objectif :** La minimisation de l'entropie croisée est équivalente à la maximisation de la vraisemblance des données d'entraînement. Pour un LLM qui prédit le prochain jeton $y_t$ étant donné les jetons précédents $y_{<t}$, la vraisemblance d'une séquence $Y = (y_1, \ldots, y_T)$ est $P(Y) = \prod_{t=1}^T P(y_t | y_{<t})$. La perte d'entropie croisée moyenne sur la séquence est $-\frac{1}{T} \sum_{t=1}^T \log P(y_t | y_{<t})$, qui est la moyenne du logarithme négatif des probabilités. Minimiser cette quantité revient à maximiser $\sum_{t=1}^T \log P(y_t | y_{<t})$, et donc à maximiser $\log \prod_{t=1}^T P(y_t | y_{<t})$, ce qui maximise la vraisemblance des données sous le modèle.

2.  **Mesure de performance :** La valeur de l'entropie croisée, en particulier l'entropie croisée empirique moyenne sur un ensemble de validation ou de test, est directement liée à la **perplexité**. La perplexité est définie comme $2^{H(P,Q)}$ et constitue une mesure intuitive de la qualité d'un modèle de langage. Une perplexité plus faible indique qu'un modèle assigne une probabilité plus élevée aux séquences observées dans les données, signifiant qu'il est "moins perplexe" quant à la suite des mots. Lors de l'entraînement d'un LLM, l'objectif est de réduire cette perplexité, ce qui correspond à minimiser l'entropie croisée.

3.  **Convergence vers l'entropie de Shannon :** Comme démontré précédemment, au fur et à mesure que l'entraînement progresse sur un ensemble de données suffisamment vaste, l'entropie croisée empirique de la fonction de perte converge vers l'entropie conditionnelle $H(Y | X)$ de la source de données réelle. Cette valeur $H(Y | X)$ représente la limite inférieure théorique de la perplexité que tout modèle pourrait atteindre. Aucun modèle ne peut prédire avec une meilleure perplexité que l'entropie de la source elle-même, car cela impliquerait qu'il connaît la source mieux que la source ne se connaît elle-même. Cette convergence fournit un cadre théorique solide pour évaluer les performances ultimes d'un LLM et comprendre jusqu'où il peut apprendre la structure intrinsèque d'une langue.

4.  **Implications pratiques :** Le fait que l'entropie croisée converge vers l'entropie de Shannon a des implications directes pour l'évaluation et la conception des LLM. Les chercheurs peuvent comparer la perplexité de leurs modèles avec des estimations de l'entropie de diverses langues pour comprendre l'écart entre la performance actuelle et la limite théorique. Cela guide également le développement de techniques d'optimisation, de stratégies d'augmentation de données et d'architectures de modèles, car le but est de permettre au modèle d'approcher cette borne inférieure d'information avec la plus grande fidélité possible, malgré les contraintes de ressources computatielles et de taille finie des données d'entraînement. La capacité du modèle à "compresser" l'information présente dans le texte est directement mesurée par cette valeur d'entropie croisée.