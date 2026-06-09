Mes chers étudiants,

Bienvenue à ce jalon de notre exploration des Processus de Décision de Markov. La rigueur, la précision et la complétude seront nos guides inébranlables tout au long de ce parcours. Voici l'exercice 01, conçu pour vous ancrer fermement dans les fondations de ce domaine crucial. Abordez chaque question avec la plus grande attention aux détails.

---

# Jalon 142 : Processus de décision de Markov
## Exercice 01/10 : Modélisation Initiale d'un Problème de Décision Séquentielle Simple (Difficulté : 01/10)

### Énoncé Rigoureux et Formel

Considérons un système dynamique très simple, par exemple une machine de production ou un composant logiciel, qui peut se trouver dans l'un des deux états suivants :
*   **$s_1$ : Fonctionnel** (le système opère normalement).
*   **$s_2$ : En panne** (le système est défaillant et nécessite une intervention).

À chaque étape de temps discrète, un agent (un opérateur, un programme de maintenance) doit choisir l'une des deux actions possibles :
*   **$a_1$ : Maintenir/Réparer** (effectuer une maintenance préventive ou une réparation si nécessaire).
*   **$a_2$ : Opérer** (laisser le système fonctionner ou tenter de l'opérer).

Les dynamiques de transition d'état et les récompenses immédiates sont définies comme suit :

**Probabilités de Transition d'État ($P(s' | s, a)$)** :
*   **Si le système est fonctionnel ($s_1$) :**
    *   En choisissant l'action $a_1$ (Maintenir) :
        *   Le système reste fonctionnel ($s_1$) avec une probabilité de $0.95$.
        *   Le système tombe en panne ($s_2$) avec une probabilité de $0.05$.
    *   En choisissant l'action $a_2$ (Opérer) :
        *   Le système reste fonctionnel ($s_1$) avec une probabilité de $0.70$.
        *   Le système tombe en panne ($s_2$) avec une probabilité de $0.30$.
*   **Si le système est en panne ($s_2$) :**
    *   En choisissant l'action $a_1$ (Maintenir/Réparer) :
        *   Le système redevient fonctionnel ($s_1$) avec une probabilité de $0.80$.
        *   Le système reste en panne ($s_2$) avec une probabilité de $0.20$.
    *   En choisissant l'action $a_2$ (Opérer) :
        *   Le système redevient fonctionnel ($s_1$) avec une probabilité de $0.00$.
        *   Le système reste en panne ($s_2$) avec une probabilité de $1.00$.

**Récompenses Immédiates ($R(s, a)$)** : Ces récompenses sont obtenues immédiatement après avoir choisi l'action $a$ dans l'état $s$, indépendamment de l'état suivant.
*   **Si le système est fonctionnel ($s_1$) :**
    *   Action $a_1$ (Maintenir) : Récompense de $-2$ (coût de la maintenance).
    *   Action $a_2$ (Opérer) : Récompense de $+10$ (profit généré par l'opération).
*   **Si le système est en panne ($s_2$) :**
    *   Action $a_1$ (Maintenir/Réparer) : Récompense de $-5$ (coût de la réparation).
    *   Action $a_2$ (Opérer) : Récompense de $-1$ (coût ou pénalité minime pour avoir tenté d'opérer un système en panne).

Le facteur d'actualisation est $\gamma = 0.9$.

**Questions :**

1.  Définir formellement l'ensemble des états $\mathcal{S}$ et l'ensemble des actions $\mathcal{A}$ de ce Processus de Décision de Markov (PDM).
2.  Présenter la fonction de transition de probabilités $P(s' | s, a)$ sous forme matricielle pour chaque action $a \in \mathcal{A}$. Les matrices seront de taille $|\mathcal{S}| \times |\mathcal{S}|$.
3.  Présenter la fonction de récompense immédiate $R(s, a)$ sous forme de tableau.
4.  Considérons que le système est dans l'état $s_1$ ("Fonctionnel"). Quelle est la récompense espérée immédiate si l'action $a_1$ ("Maintenir/Réparer") est choisie ?
5.  Considérons que le système est dans l'état $s_1$ ("Fonctionnel"). Quelle est la probabilité que le système soit dans l'état $s_2$ ("En panne") après une étape, si l'action $a_2$ ("Opérer") est choisie ?

### Correction Détaillée

Mes chers étudiants, abordons cette correction avec la rigueur et la clarté attendues pour un fondement solide de votre compréhension. Chaque étape sera explicitée sans aucune omission.

#### Question 1 : Définir formellement l'ensemble des états $\mathcal{S}$ et l'ensemble des actions $\mathcal{A}$.

Nous commençons par identifier les éléments fondamentaux de notre Processus de Décision de Markov.

L'ensemble des états $\mathcal{S}$ représente toutes les situations distinctes dans lesquelles le système peut se trouver. Selon l'énoncé, le système peut être soit "Fonctionnel", soit "En panne". Nous les avons nommés $s_1$ et $s_2$ respectivement.

Ainsi, l'ensemble des états est :
$$ \mathcal{S} = \{s_1, s_2\} $$
où $s_1$ correspond à l'état "Fonctionnel" et $s_2$ correspond à l'état "En panne".

L'ensemble des actions $\mathcal{A}$ représente toutes les décisions que l'agent peut prendre à n'importe quel état. Selon l'énoncé, l'agent peut choisir de "Maintenir/Réparer" ou d'"Opérer". Nous les avons nommés $a_1$ et $a_2$ respectivement.

Ainsi, l'ensemble des actions est :
$$ \mathcal{A} = \{a_1, a_2\} $$
où $a_1$ correspond à l'action "Maintenir/Réparer" et $a_2$ correspond à l'action "Opérer".

#### Question 2 : Présenter la fonction de transition de probabilités $P(s' | s, a)$ sous forme matricielle pour chaque action $a \in \mathcal{A}$.

La fonction de transition de probabilités $P(s' | s, a)$ spécifie la probabilité de passer de l'état $s$ à l'état $s'$ après avoir effectué l'action $a$. Puisque nous avons $|\mathcal{S}| = 2$ états, chaque matrice de transition pour une action donnée sera de taille $2 \times 2$. Nous allons définir une matrice $P_{a}$ pour chaque action $a \in \mathcal{A}$, où l'élément $(i, j)$ de la matrice $P_{a}$ correspond à $P(s_j | s_i, a)$.

**Pour l'action $a_1$ (Maintenir/Réparer) :**

Les probabilités de transition sont les suivantes, d'après l'énoncé :
*   Depuis l'état $s_1$ :
    *   $P(s_1 | s_1, a_1) = 0.95$
    *   $P(s_2 | s_1, a_1) = 0.05$
*   Depuis l'état $s_2$ :
    *   $P(s_1 | s_2, a_1) = 0.80$
    *   $P(s_2 | s_2, a_1) = 0.20$

Nous pouvons donc construire la matrice de transition $P_{a_1}$ comme suit :
$$ P_{a_1} = \begin{pmatrix} P(s_1 | s_1, a_1) & P(s_2 | s_1, a_1) \\ P(s_1 | s_2, a_1) & P(s_2 | s_2, a_1) \end{pmatrix} $$
En substituant les valeurs numériques :
$$ P_{a_1} = \begin{pmatrix} 0.95 & 0.05 \\ 0.80 & 0.20 \end{pmatrix} $$
Les lignes de cette matrice représentent les états de départ ($s_1$, $s_2$) et les colonnes représentent les états d'arrivée ($s_1$, $s_2$).

**Pour l'action $a_2$ (Opérer) :**

Les probabilités de transition sont les suivantes, d'après l'énoncé :
*   Depuis l'état $s_1$ :
    *   $P(s_1 | s_1, a_2) = 0.70$
    *   $P(s_2 | s_1, a_2) = 0.30$
*   Depuis l'état $s_2$ :
    *   $P(s_1 | s_2, a_2) = 0.00$
    *   $P(s_2 | s_2, a_2) = 1.00$

Nous pouvons donc construire la matrice de transition $P_{a_2}$ comme suit :
$$ P_{a_2} = \begin{pmatrix} P(s_1 | s_1, a_2) & P(s_2 | s_1, a_2) \\ P(s_1 | s_2, a_2) & P(s_2 | s_2, a_2) \end{pmatrix} $$
En substituant les valeurs numériques :
$$ P_{a_2} = \begin{pmatrix} 0.70 & 0.30 \\ 0.00 & 1.00 \end{pmatrix} $$
De la même manière, les lignes représentent les états de départ ($s_1$, $s_2$) et les colonnes représentent les états d'arrivée ($s_1$, $s_2$).

#### Question 3 : Présenter la fonction de récompense immédiate $R(s, a)$ sous forme de tableau.

La fonction de récompense immédiate $R(s, a)$ attribue une valeur numérique à chaque paire état-action, représentant le bénéfice ou le coût immédiat de l'exécution de l'action $a$ dans l'état $s$.

D'après l'énoncé, nous avons les récompenses suivantes :
*   Pour l'état $s_1$ (Fonctionnel) :
    *   Avec l'action $a_1$ (Maintenir) : $R(s_1, a_1) = -2$.
    *   Avec l'action $a_2$ (Opérer) : $R(s_1, a_2) = +10$.
*   Pour l'état $s_2$ (En panne) :
    *   Avec l'action $a_1$ (Maintenir/Réparer) : $R(s_2, a_1) = -5$.
    *   Avec l'action $a_2$ (Opérer) : $R(s_2, a_2) = -1$.

Nous pouvons organiser ces récompenses dans un tableau pour une meilleure lisibilité :

| État $\mathcal{S}$ | Action $\mathcal{A}$ | Récompense $R(s, a)$ |
| :----------------: | :------------------: | :------------------: |
|       $s_1$        |       $a_1$          |         $-2$         |
|       $s_1$        |       $a_2$          |         $+10$        |
|       $s_2$        |       $a_1$          |         $-5$         |
|       $s_2$        |       $a_2$          |         $-1$         |

Cette représentation tabulaire synthétise l'ensemble des récompenses immédiates définies pour notre PDM.

#### Question 4 : Considérons que le système est dans l'état $s_1$ ("Fonctionnel"). Quelle est la récompense espérée immédiate si l'action $a_1$ ("Maintenir/Réparer") est choisie ?

La question nous demande de déterminer la récompense espérée immédiate pour une situation spécifique : l'état actuel est $s_1$ et l'action choisie est $a_1$.
Dans la formulation que nous avons adoptée pour ce PDM de difficulté 01/10, la récompense immédiate $R(s, a)$ est une valeur déterministe qui dépend uniquement de l'état $s$ et de l'action $a$. Elle n'est pas stochastique par rapport à l'état suivant $s'$.

Par conséquent, la récompense espérée immédiate $E[R_{t+1} | S_t = s, A_t = a]$ est simplement égale à la valeur $R(s, a)$ lorsque la fonction de récompense ne dépend pas de l'état futur.

Dans notre cas, nous sommes dans l'état $s_1$ et nous choisissons l'action $a_1$.
En consultant la fonction de récompense immédiate $R(s, a)$ établie à la Question 3, nous trouvons la valeur spécifique pour $s=s_1$ et $a=a_1$.

Nous avons :
$$ R(s_1, a_1) = -2 $$

Puisque la récompense immédiate est déterministe pour une paire $(s, a)$ donnée, la récompense espérée immédiate est égale à cette valeur déterministe.

La récompense espérée immédiate si le système est dans l'état $s_1$ et que l'action $a_1$ est choisie est de $\mathbf{-2}$.

#### Question 5 : Considérons que le système est dans l'état $s_1$ ("Fonctionnel"). Quelle est la probabilité que le système soit dans l'état $s_2$ ("En panne") après une étape, si l'action $a_2$ ("Opérer") est choisie ?

Cette question nous demande de trouver une probabilité de transition spécifique : la probabilité de passer de l'état $s_1$ à l'état $s_2$ en exécutant l'action $a_2$.

Formellement, nous cherchons la valeur de $P(s_2 | s_1, a_2)$.

Pour trouver cette valeur, nous nous référons aux probabilités de transition définies dans l'énoncé et présentées sous forme matricielle à la Question 2.
Nous devons consulter la matrice de transition correspondant à l'action $a_2$, que nous avons notée $P_{a_2}$.

La matrice $P_{a_2}$ est la suivante :
$$ P_{a_2} = \begin{pmatrix} P(s_1 | s_1, a_2) & P(s_2 | s_1, a_2) \\ P(s_1 | s_2, a_2) & P(s_2 | s_2, a_2) \end{pmatrix} = \begin{pmatrix} 0.70 & 0.30 \\ 0.00 & 1.00 \end{pmatrix} $$

Nous cherchons l'élément de cette matrice qui correspond à la transition de l'état $s_1$ (première ligne) vers l'état $s_2$ (deuxième colonne).

En examinant la matrice, nous identifions directement la valeur :
$$ P(s_2 | s_1, a_2) = 0.30 $$

Ainsi, la probabilité que le système soit dans l'état $s_2$ ("En panne") après une étape, si le système est actuellement dans l'état $s_1$ ("Fonctionnel") et que l'action $a_2$ ("Opérer") est choisie, est de $\mathbf{0.30}$.