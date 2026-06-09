Mes chers étudiants,

Bienvenue à ce jalon de notre exploration. Voici l'exercice 03. La rigueur sera notre guide.

---

# Jalon 142 : Processus de décision de Markov
## Exercice 03/10 : Identification des Composants Fondamentaux d'un MDP et Calcul de Récompense Immédiate (Difficulté : 03/10)

### Énoncé Rigoureux et Formel

Chers étudiants,
Nous allons explorer les fondements des Processus de Décision de Markov (MDP) à travers un cas pratique et structuré. Considérons un robot autonome évoluant dans un environnement unidimensionnel et discret, modélisé par une séquence de cellules. Votre tâche consistera à formaliser les éléments constitutifs de ce système en un MDP et à réaliser un calcul élémentaire de récompense espérée.

Les états du système sont définis par les positions du robot dans les cellules. Nous les désignons formellement par $s_1, s_2, s_3$.
*   $s_1$ représente la cellule la plus à gauche.
*   $s_2$ représente la cellule centrale.
*   $s_3$ représente la cellule la plus à droite.

À chaque étape discrète de temps, le robot peut choisir d'exécuter l'une des deux actions suivantes :
*   $a_R$: Une tentative de déplacement vers la droite.
*   $a_S$: Une décision de rester dans la cellule actuelle.

Les règles de transition d'un état à un autre, dictées par l'action choisie, sont de nature stochastique et sont spécifiées comme suit :

*   **Si le robot est dans l'état $s_1$ :**
    *   S'il choisit l'action $a_R$ : Le robot se déplace vers $s_2$ avec une probabilité $P(s_2|s_1, a_R) = 0.8$. Il peut cependant, avec une probabilité $P(s_1|s_1, a_R) = 0.2$, rester dans la cellule $s_1$ en raison d'une incertitude inhérente au mécanisme de déplacement ou à l'environnement.
    *   S'il choisit l'action $a_S$ : Le robot demeure dans l'état $s_1$ avec une probabilité $P(s_1|s_1, a_S) = 1.0$.

*   **Si le robot est dans l'état $s_2$ :**
    *   S'il choisit l'action $a_R$ : Le robot transite vers $s_3$ avec une probabilité $P(s_3|s_2, a_R) = 0.7$. Alternativement, il peut rester en $s_2$ avec une probabilité $P(s_2|s_2, a_R) = 0.3$.
    *   S'il choisit l'action $a_S$ : Le robot reste dans l'état $s_2$ avec une probabilité $P(s_2|s_2, a_S) = 1.0$.

*   **Si le robot est dans l'état $s_3$ :**
    *   S'il choisit l'action $a_R$ : Le robot, étant à la limite droite de l'environnement, reste dans l'état $s_3$ avec une probabilité $P(s_3|s_3, a_R) = 1.0$.
    *   S'il choisit l'action $a_S$ : Le robot demeure dans l'état $s_3$ avec une probabilité $P(s_3|s_3, a_S) = 1.0$.

Un système de récompenses immédiates est associé à l'atteinte de chaque état. Ces récompenses sont indépendantes de l'action entreprise et de l'état précédent le passage à l'état actuel :
*   Atteindre l'état $s_1$ génère une récompense $R(s_1) = -1$.
*   Atteindre l'état $s_2$ génère une récompense $R(s_2) = -1$.
*   Atteindre l'état $s_3$ génère une récompense $R(s_3) = +10$.

Il vous est demandé d'analyser rigoureusement ce Processus de Décision de Markov en répondant aux questions suivantes :

1.  **Définition de l'Espace des États et de l'Espace des Actions :**
    Formellement, décrivez l'ensemble des états $S$ et l'ensemble des actions $A$ disponibles pour le robot.

2.  **Spécification des Probabilités de Transition :**
    Pour chaque paire (état, action) $(s, a)$, et pour chaque état successeur $s'$, spécifiez la probabilité de transition $P(s'|s,a)$. Veillez à présenter toutes les probabilités pertinentes de manière exhaustive et non ambiguë, en vérifiant que la somme des probabilités pour chaque couple $(s,a)$ est bien égale à 1.

3.  **Spécification de la Fonction de Récompense :**
    Décrivez formellement la fonction de récompense $R(s,a,s')$ pour toutes les combinaisons possibles de $(s,a,s')$, en explicitant comment elle découle des récompenses par état $R(s')$ mentionnées ci-dessus.

4.  **Calcul de la Récompense Immédiate Espérée :**
    Calculez la récompense immédiate espérée, notée $\mathbb{E}[R_{t+1}|S_t=s_1, A_t=a_R]$, pour le scénario où le robot se trouve dans l'état $s_1$ au temps $t$ et décide d'exécuter l'action $a_R$. Détaillez méticuleusement chaque étape de votre calcul, sans aucune ellipse mathématique.

---

### Correction Détaillée

Mes chers étudiants, abordons cette correction avec la rigueur qui sied à notre discipline. Chaque étape doit être explicitée avec la plus grande clarté.

#### 1. Définition de l'Espace des États et de l'Espace des Actions

L'espace des états, noté $S$, représente l'ensemble de toutes les configurations distinctes que le système peut occuper. Dans le contexte de cet exercice, ces configurations correspondent aux positions possibles du robot dans les cellules.
$$ S = \{s_1, s_2, s_3\} $$
où $s_1$ est la cellule la plus à gauche, $s_2$ est la cellule centrale, et $s_3$ est la cellule la plus à droite.

L'espace des actions, noté $A$, est l'ensemble de toutes les décisions distinctes que l'agent (le robot) peut prendre à chaque étape de temps. Pour cet exercice, les actions sont universellement disponibles, c'est-à-dire qu'elles peuvent être entreprises depuis n'importe quel état.
$$ A = \{a_R, a_S\} $$
où $a_R$ désigne l'action "tenter de se déplacer vers la droite" et $a_S$ désigne l'action "rester dans la cellule actuelle". Il est pertinent de noter que, dans des modèles de MDP plus complexes, l'ensemble des actions disponibles pourrait être spécifique à chaque état $s$, et serait alors noté $A(s)$. Ici, $A(s) = A$ pour tout $s \in S$.

#### 2. Spécification des Probabilités de Transition

La fonction de probabilité de transition, $P(s'|s,a)$, est une composante fondamentale d'un MDP. Elle quantifie la probabilité de passer de l'état $s$ à l'état $s'$ au temps $t+1$, sachant que l'action $a$ a été exécutée depuis l'état $s$ au temps $t$. Pour la validité d'une distribution de probabilités, la somme de toutes les probabilités de transition depuis un couple $(s,a)$ donné vers tous les états possibles $s'$ doit être égale à $1$. Autrement dit, $\sum_{s' \in S} P(s'|s,a) = 1$.

Nous allons énumérer ces probabilités pour chaque couple $(s,a)$ :

*   **Depuis l'état $s_1$ :**
    *   **Avec l'action $a_R$ (déplacement vers la droite) :**
        *   La probabilité de transition vers $s_2$ est :
            $$ P(s_2|s_1, a_R) = 0.8 $$
        *   La probabilité de rester dans l'état $s_1$ est :
            $$ P(s_1|s_1, a_R) = 0.2 $$
        *   La probabilité de transition vers l'état $s_3$ est de $0$, car il n'est pas possible de sauter une cellule en un seul pas :
            $$ P(s_3|s_1, a_R) = 0.0 $$
        *   Vérification de la somme des probabilités pour $(s_1, a_R)$ :
            $$ \sum_{s' \in S} P(s'|s_1, a_R) = P(s_1|s_1, a_R) + P(s_2|s_1, a_R) + P(s_3|s_1, a_R) = 0.2 + 0.8 + 0.0 = 1.0 $$

    *   **Avec l'action $a_S$ (rester dans la cellule actuelle) :**
        *   La probabilité de rester dans l'état $s_1$ est :
            $$ P(s_1|s_1, a_S) = 1.0 $$
        *   Les probabilités de transition vers tout autre état ($s_2, s_3$) sont nulles :
            $$ P(s_2|s_1, a_S) = 0.0 $$
            $$ P(s_3|s_1, a_S) = 0.0 $$
        *   Vérification de la somme des probabilités pour $(s_1, a_S)$ :
            $$ \sum_{s' \in S} P(s'|s_1, a_S) = P(s_1|s_1, a_S) + P(s_2|s_1, a_S) + P(s_3|s_1, a_S) = 1.0 + 0.0 + 0.0 = 1.0 $$

*   **Depuis l'état $s_2$ :**
    *   **Avec l'action $a_R$ (déplacement vers la droite) :**
        *   La probabilité de transition vers $s_3$ est :
            $$ P(s_3|s_2, a_R) = 0.7 $$
        *   La probabilité de rester dans l'état $s_2$ est :
            $$ P(s_2|s_2, a_R) = 0.3 $$
        *   La probabilité de transition vers l'état $s_1$ est de $0$ (pas de déplacement vers la gauche avec $a_R$) :
            $$ P(s_1|s_2, a_R) = 0.0 $$
        *   Vérification de la somme des probabilités pour $(s_2, a_R)$ :
            $$ \sum_{s' \in S} P(s'|s_2, a_R) = P(s_1|s_2, a_R) + P(s_2|s_2, a_R) + P(s_3|s_2, a_R) = 0.0 + 0.3 + 0.7 = 1.0 $$

    *   **Avec l'action $a_S$ (rester dans la cellule actuelle) :**
        *   La probabilité de rester dans l'état $s_2$ est :
            $$ P(s_2|s_2, a_S) = 1.0 $$
        *   Les probabilités de transition vers tout autre état ($s_1, s_3$) sont nulles :
            $$ P(s_1|s_2, a_S) = 0.0 $$
            $$ P(s_3|s_2, a_S) = 0.0 $$
        *   Vérification de la somme des probabilités pour $(s_2, a_S)$ :
            $$ \sum_{s' \in S} P(s'|s_2, a_S) = P(s_1|s_2, a_S) + P(s_2|s_2, a_S) + P(s_3|s_2, a_S) = 0.0 + 1.0 + 0.0 = 1.0 $$

*   **Depuis l'état $s_3$ :**
    *   **Avec l'action $a_R$ (déplacement vers la droite) :**
        *   Le robot est déjà dans la cellule la plus à droite. Par conséquent, la probabilité de rester en $s_3$ est :
            $$ P(s_3|s_3, a_R) = 1.0 $$
        *   Les probabilités de transition vers tout autre état ($s_1, s_2$) sont nulles :
            $$ P(s_1|s_3, a_R) = 0.0 $$
            $$ P(s_2|s_3, a_R) = 0.0 $$
        *   Vérification de la somme des probabilités pour $(s_3, a_R)$ :
            $$ \sum_{s' \in S} P(s'|s_3, a_R) = P(s_1|s_3, a_R) + P(s_2|s_3, a_R) + P(s_3|s_3, a_R) = 0.0 + 0.0 + 1.0 = 1.0 $$

    *   **Avec l'action $a_S$ (rester dans la cellule actuelle) :**
        *   La probabilité de rester dans l'état $s_3$ est :
            $$ P(s_3|s_3, a_S) = 1.0 $$
        *   Les probabilités de transition vers tout autre état ($s_1, s_2$) sont nulles :
            $$ P(s_1|s_3, a_S) = 0.0 $$
            $$ P(s_2|s_3, a_S) = 0.0 $$
        *   Vérification de la somme des probabilités pour $(s_3, a_S)$ :
            $$ \sum_{s' \in S} P(s'|s_3, a_S) = P(s_1|s_3, a_S) + P(s_2|s_3, a_S) + P(s_3|s_3, a_S) = 0.0 + 0.0 + 1.0 = 1.0 $$

#### 3. Spécification de la Fonction de Récompense

La fonction de récompense, notée $R(s,a,s')$, attribue une valeur numérique (scalaire) au robot lorsqu'il effectue une transition spécifique, c'est-à-dire en passant de l'état $s$ à l'état $s'$ après avoir choisi l'action $a$. Dans le cadre de cet exercice, l'énoncé stipule que la récompense dépend uniquement de l'état d'arrivée $s'$, et non de l'action $a$ entreprise ou de l'état $s$ précédent. Nous pouvons donc simplifier la notation en $R(s')$.

Les récompenses pour chaque état d'arrivée $s'$ sont définies comme suit :
*   Lorsque le robot atteint l'état $s_1$, la récompense est de $R(s_1) = -1$.
*   Lorsque le robot atteint l'état $s_2$, la récompense est de $R(s_2) = -1$.
*   Lorsque le robot atteint l'état $s_3$, la récompense est de $R(s_3) = +10$.

Par conséquent, pour toute transition $(s, a, s')$, la fonction de récompense peut être exprimée formellement par une fonction par morceaux :
$$ R(s,a,s') = R(s') = \begin{cases}
    -1 & \text{si } s' = s_1 \\
    -1 & \text{si } s' = s_2 \\
    +10 & \text{si } s' = s_3
\end{cases} $$
Cette formalisation met en évidence que la récompense perçue par le robot est une fonction directe de la cellule dans laquelle il se trouve après la transition, indépendamment de la manière dont il y est parvenu.

#### 4. Calcul de la Récompense Immédiate Espérée

Il nous est demandé de calculer la récompense immédiate espérée, $\mathbb{E}[R_{t+1}|S_t=s_1, A_t=a_R]$, ce qui représente la valeur moyenne de la récompense que le robot anticipe recevoir au prochain pas de temps, sachant qu'il est actuellement dans l'état $s_1$ et qu'il exécute l'action $a_R$.

La formule générale pour la récompense immédiate espérée pour un état $s$ et une action $a$ est donnée par :
$$ \mathbb{E}[R_{t+1}|S_t=s, A_t=a] = \sum_{s' \in S} P(s'|s,a) R(s,a,s') $$

Dans notre cas spécifique, nous devons substituer $s = s_1$ et $a = a_R$ dans cette formule. En utilisant la simplification $R(s,a,s') = R(s')$ établie à la Section 3, l'expression devient :
$$ \mathbb{E}[R_{t+1}|S_t=s_1, A_t=a_R] = P(s_1|s_1, a_R) R(s_1) + P(s_2|s_1, a_R) R(s_2) + P(s_3|s_1, a_R) R(s_3) $$

Nous allons maintenant remplacer les termes par les valeurs numériques que nous avons rigoureusement spécifiées dans les sections précédentes :

*   Les probabilités de transition depuis l'état $s_1$ avec l'action $a_R$ (d'après la Section 2) sont :
    *   $P(s_1|s_1, a_R) = 0.2$
    *   $P(s_2|s_1, a_R) = 0.8$
    *   $P(s_3|s_1, a_R) = 0.0$

*   Les récompenses associées à l'atteinte des états (d'après la Section 3) sont :
    *   $R(s_1) = -1$
    *   $R(s_2) = -1$
    *   $R(s_3) = +10$

Substituons ces valeurs dans l'équation de l'espérance :
$$ \mathbb{E}[R_{t+1}|S_t=s_1, A_t=a_R] = (0.2) \times (-1) + (0.8) \times (-1) + (0.0) \times (+10) $$

Nous procédons ensuite aux multiplications individuelles :
$$ (0.2) \times (-1) = -0.2 $$
$$ (0.8) \times (-1) = -0.8 $$
$$ (0.0) \times (+10) = 0.0 $$

En remplaçant ces résultats dans l'équation, nous obtenons :
$$ \mathbb{E}[R_{t+1}|S_t=s_1, A_t=a_R] = -0.2 + (-0.8) + 0.0 $$

Enfin, nous effectuons l'addition pour obtenir le résultat final :
$$ \mathbb{E}[R_{t+1}|S_t=s_1, A_t=a_R] = -1.0 $$

Par conséquent, la récompense immédiate espérée pour le robot s'il est dans l'état $s_1$ et exécute l'action $a_R$ est de $-1.0$. Ce résultat indique que, en moyenne, cette action particulière depuis cet état spécifique conduit à une petite pénalité immédiate pour le robot.