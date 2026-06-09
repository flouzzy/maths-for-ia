Mes chers étudiants,

Bienvenue à ce jalon de notre exploration. Voici l'exercice 02. La rigueur sera notre guide.

---

# Jalon 142 : Processus de décision de Markov
## Exercice 02/10 : Composants fondamentaux et espérance de récompense immédiate dans un MDP (Difficulté : 02/10)

### Énoncé Rigoureux et Formel
Considérons un agent opérant dans un environnement simple modélisé par un Processus de Décision de Markov (MDP). Cet environnement est composé de deux états distincts et l'agent dispose de deux actions possibles. Notre objectif est de consolider votre compréhension des définitions primordiales et des calculs d'espérance de récompense immédiate.

1.  **Ensemble d'États $\mathcal{S}$**:
    *   $s_1$: L'agent est dans la "Zone de Départ".
    *   $s_2$: L'agent est dans la "Zone Cible".
    Ainsi, $\mathcal{S} = \{s_1, s_2\}$.

2.  **Ensemble d'Actions $\mathcal{A}$**:
    *   $a_1$: Tenter de "Se Déplacer vers $s_1$".
    *   $a_2$: Tenter de "Se Déplacer vers $s_2$".
    Ainsi, $\mathcal{A} = \{a_1, a_2\}$.

3.  **Fonction de Récompense $R(s, a, s')$**: La récompense immédiate perçue par l'agent dépend uniquement de l'état dans lequel il arrive, quel que soit l'état de départ $s$ et l'action choisie $a$.
    *   Si l'agent arrive dans l'état $s_1$, la récompense est de $0$.
    *   Si l'agent arrive dans l'état $s_2$, la récompense est de $+10$.
    Formellement, nous définissons $r(s') := R(s, a, s')$ où $r(s_1) = 0$ et $r(s_2) = 10$.

4.  **Probabilités de Transition $P(s' | s, a)$**: Les probabilités de transition décrivent la dynamique stochastique de l'environnement, c'est-à-dire la probabilité d'atteindre un état $s'$ en partant d'un état $s$ et en exécutant une action $a$.

    *   **Depuis l'état $s_1$ (Zone de Départ)**:
        *   Si l'agent choisit l'action $a_1$ (Tenter de se déplacer vers $s_1$):
            *   L'agent reste dans $s_1$ avec une probabilité de $1.0$.
            *   $P(s_1 | s_1, a_1) = 1.0$
            *   $P(s_2 | s_1, a_1) = 0.0$
        *   Si l'agent choisit l'action $a_2$ (Tenter de se déplacer vers $s_2$):
            *   L'agent se déplace vers $s_2$ avec une probabilité de $0.9$.
            *   L'agent reste dans $s_1$ (échec partiel de l'action) avec une probabilité de $0.1$.
            *   $P(s_1 | s_1, a_2) = 0.1$
            *   $P(s_2 | s_1, a_2) = 0.9$

    *   **Depuis l'état $s_2$ (Zone Cible)**:
        *   Si l'agent choisit l'action $a_1$ (Tenter de se déplacer vers $s_1$):
            *   L'agent se déplace vers $s_1$ avec une probabilité de $0.8$.
            *   L'agent reste dans $s_2$ (échec partiel de l'action) avec une probabilité de $0.2$.
            *   $P(s_1 | s_2, a_1) = 0.8$
            *   $P(s_2 | s_2, a_1) = 0.2$
        *   Si l'agent choisit l'action $a_2$ (Tenter de se déplacer vers $s_2$):
            *   L'agent reste dans $s_2$ avec une probabilité de $1.0$.
            *   $P(s_1 | s_2, a_2) = 0.0$
            *   $P(s_2 | s_2, a_2) = 1.0$

**Questions à résoudre avec une rigueur absolue :**

1.  **Énumération des paires (état, action) :** Déterminez l'ensemble $\mathcal{S} \times \mathcal{A}$ de toutes les paires (état, action) possibles dans cet MDP.
2.  **Calcul de la récompense immédiate espérée pour une paire spécifique :** Calculez la récompense immédiate espérée $\mathbb{E}[R_{t+1} | S_t=s_1, A_t=a_2]$ lorsque l'agent est dans l'état $s_1$ et choisit l'action $a_2$.
3.  **Calcul des récompenses immédiates espérées pour toutes les paires (état, action) :** Calculez la récompense immédiate espérée $\mathbb{E}[R_{t+1} | S_t=s, A_t=a]$ pour toutes les paires $(s, a) \in \mathcal{S} \times \mathcal{A}$.

### Correction Détaillée

Chers étudiants, abordons cette correction avec la précision qui caractérise toute démarche scientifique rigoureuse. Chaque étape doit être explicitée, chaque calcul détaillé.

#### 1. Énumération des paires (état, action)

L'ensemble des états est défini par $\mathcal{S} = \{s_1, s_2\}$.
L'ensemble des actions est défini par $\mathcal{A} = \{a_1, a_2\}$.

L'ensemble de toutes les paires (état, action) possibles est le produit cartésien de l'ensemble des états et de l'ensemble des actions, noté $\mathcal{S} \times \mathcal{A}$. Un élément $(s, a)$ de cet ensemble représente la situation où l'agent se trouve dans l'état $s$ et choisit d'exécuter l'action $a$.

La définition du produit cartésien $\mathcal{S} \times \mathcal{A}$ est la suivante :
$$ \mathcal{S} \times \mathcal{A} = \{ (s, a) \mid s \in \mathcal{S} \text{ et } a \in \mathcal{A} \} $$

En substituant les éléments de $\mathcal{S}$ et $\mathcal{A}$, nous obtenons :
$$ \mathcal{S} \times \mathcal{A} = \{ (s_1, a_1), (s_1, a_2), (s_2, a_1), (s_2, a_2) \} $$

Il y a donc $2 \times 2 = 4$ paires (état, action) possibles dans cet MDP.

#### 2. Calcul de la récompense immédiate espérée pour une paire spécifique

Nous devons calculer la récompense immédiate espérée $\mathbb{E}[R_{t+1} | S_t=s_1, A_t=a_2]$.
La formule générale pour la récompense immédiate espérée, étant donné un état $S_t=s$ et une action $A_t=a$, est définie par :
$$ \mathbb{E}[R_{t+1} | S_t=s, A_t=a] = \sum_{s' \in \mathcal{S}} P(s'|s,a) \cdot r(s') $$
où $r(s')$ est la récompense perçue en arrivant dans l'état $s'$.

Dans notre cas spécifique, nous avons $s = s_1$ et $a = a_2$.
La somme s'effectuera sur tous les états possibles $s'$ de l'ensemble $\mathcal{S} = \{s_1, s_2\}$.

Les probabilités de transition pertinentes pour $(s_1, a_2)$ sont :
*   $P(s_1 | s_1, a_2) = 0.1$
*   $P(s_2 | s_1, a_2) = 0.9$

Les récompenses pour les états d'arrivée sont :
*   $r(s_1) = 0$
*   $r(s_2) = 10$

Substituons ces valeurs dans la formule :
$$ \mathbb{E}[R_{t+1} | S_t=s_1, A_t=a_2] = P(s_1|s_1,a_2) \cdot r(s_1) + P(s_2|s_1,a_2) \cdot r(s_2) $$
$$ \mathbb{E}[R_{t+1} | S_t=s_1, A_t=a_2] = (0.1) \cdot (0) + (0.9) \cdot (10) $$
Effectuons les multiplications :
$$ \mathbb{E}[R_{t+1} | S_t=s_1, A_t=a_2] = 0 + 9 $$
Effectuons l'addition :
$$ \mathbb{E}[R_{t+1} | S_t=s_1, A_t=a_2] = 9 $$
La récompense immédiate espérée lorsque l'agent est dans l'état $s_1$ et choisit l'action $a_2$ est de $9$.

#### 3. Calcul des récompenses immédiates espérées pour toutes les paires (état, action)

Nous allons calculer $\mathbb{E}[R_{t+1} | S_t=s, A_t=a]$ pour chacune des quatre paires $(s, a) \in \mathcal{S} \times \mathcal{A}$.

La formule générale reste :
$$ \mathbb{E}[R_{t+1} | S_t=s, A_t=a] = \sum_{s' \in \mathcal{S}} P(s'|s,a) \cdot r(s') $$
avec $r(s_1) = 0$ et $r(s_2) = 10$.

##### a) Pour la paire $(s_1, a_1)$ :
L'agent est dans l'état $s_1$ et choisit l'action $a_1$.
Les probabilités de transition sont :
*   $P(s_1 | s_1, a_1) = 1.0$
*   $P(s_2 | s_1, a_1) = 0.0$

Substituons dans la formule :
$$ \mathbb{E}[R_{t+1} | S_t=s_1, A_t=a_1] = P(s_1|s_1,a_1) \cdot r(s_1) + P(s_2|s_1,a_1) \cdot r(s_2) $$
$$ \mathbb{E}[R_{t+1} | S_t=s_1, A_t=a_1] = (1.0) \cdot (0) + (0.0) \cdot (10) $$
Effectuons les multiplications :
$$ \mathbb{E}[R_{t+1} | S_t=s_1, A_t=a_1] = 0 + 0 $$
Effectuons l'addition :
$$ \mathbb{E}[R_{t+1} | S_t=s_1, A_t=a_1] = 0 $$

##### b) Pour la paire $(s_1, a_2)$ :
Ce calcul a déjà été effectué dans la question précédente.
L'agent est dans l'état $s_1$ et choisit l'action $a_2$.
Les probabilités de transition sont :
*   $P(s_1 | s_1, a_2) = 0.1$
*   $P(s_2 | s_1, a_2) = 0.9$

Substituons dans la formule :
$$ \mathbb{E}[R_{t+1} | S_t=s_1, A_t=a_2] = P(s_1|s_1,a_2) \cdot r(s_1) + P(s_2|s_1,a_2) \cdot r(s_2) $$
$$ \mathbb{E}[R_{t+1} | S_t=s_1, A_t=a_2] = (0.1) \cdot (0) + (0.9) \cdot (10) $$
Effectuons les multiplications :
$$ \mathbb{E}[R_{t+1} | S_t=s_1, A_t=a_2] = 0 + 9 $$
Effectuons l'addition :
$$ \mathbb{E}[R_{t+1} | S_t=s_1, A_t=a_2] = 9 $$

##### c) Pour la paire $(s_2, a_1)$ :
L'agent est dans l'état $s_2$ et choisit l'action $a_1$.
Les probabilités de transition sont :
*   $P(s_1 | s_2, a_1) = 0.8$
*   $P(s_2 | s_2, a_1) = 0.2$

Substituons dans la formule :
$$ \mathbb{E}[R_{t+1} | S_t=s_2, A_t=a_1] = P(s_1|s_2,a_1) \cdot r(s_1) + P(s_2|s_2,a_1) \cdot r(s_2) $$
$$ \mathbb{E}[R_{t+1} | S_t=s_2, A_t=a_1] = (0.8) \cdot (0) + (0.2) \cdot (10) $$
Effectuons les multiplications :
$$ \mathbb{E}[R_{t+1} | S_t=s_2, A_t=a_1] = 0 + 2 $$
Effectuons l'addition :
$$ \mathbb{E}[R_{t+1} | S_t=s_2, A_t=a_1] = 2 $$

##### d) Pour la paire $(s_2, a_2)$ :
L'agent est dans l'état $s_2$ et choisit l'action $a_2$.
Les probabilités de transition sont :
*   $P(s_1 | s_2, a_2) = 0.0$
*   $P(s_2 | s_2, a_2) = 1.0$

Substituons dans la formule :
$$ \mathbb{E}[R_{t+1} | S_t=s_2, A_t=a_2] = P(s_1|s_2,a_2) \cdot r(s_1) + P(s_2|s_2,a_2) \cdot r(s_2) $$
$$ \mathbb{E}[R_{t+1} | S_t=s_2, A_t=a_2] = (0.0) \cdot (0) + (1.0) \cdot (10) $$
Effectuons les multiplications :
$$ \mathbb{E}[R_{t+1} | S_t=s_2, A_t=a_2] = 0 + 10 $$
Effectuons l'addition :
$$ \mathbb{E}[R_{t+1} | S_t=s_2, A_t=a_2] = 10 $$

En résumé, les récompenses immédiates espérées pour toutes les paires (état, action) sont :
*   $\mathbb{E}[R_{t+1} | S_t=s_1, A_t=a_1] = 0$
*   $\mathbb{E}[R_{t+1} | S_t=s_1, A_t=a_2] = 9$
*   $\mathbb{E}[R_{t+1} | S_t=s_2, A_t=a_1] = 2$
*   $\mathbb{E}[R_{t+1} | S_t=s_2, A_t=a_2] = 10$

Félicitations pour avoir mené à bien cet exercice fondamental. La maîtrise de ces concepts élémentaires est la pierre angulaire de notre parcours. Continuez à appliquer cette même rigueur dans vos travaux futurs.