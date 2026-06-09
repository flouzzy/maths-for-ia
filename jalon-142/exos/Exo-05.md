Mes chers étudiants,

Bienvenue à ce jalon de notre exploration. Voici l'exercice 05. La rigueur sera notre guide.

---

# Jalon 142 : Processus de décision de Markov
## Exercice 05/10 : Itération de la Valeur pour un MDP Discret: Gestion d'une Ligne de Production (Difficulté : 05/10)

### Énoncé Rigoureux et Formel

Considérons un Processus de Décision de Markov (PDM) discret à horizon infini, modélisant la gestion d'une ligne de production simplifiée. L'objectif est d'optimiser les décisions pour maximiser le retour total actualisé.

Le PDM est défini par les éléments suivants :

1.  **Ensemble des États ($S$) :** Deux états discrets, représentant l'état opérationnel de la ligne :
    *   $S_1$ : "En attente" (la ligne est inactive, attendant des instructions ou une réparation).
    *   $S_2$ : "En production" (la ligne est active et produit).

2.  **Ensemble des Actions ($A$) :** Deux actions possibles dans chaque état :
    *   $A_1$ : "Maintenance légère" (une intervention rapide et peu coûteuse).
    *   $A_2$ : "Optimisation complète" (une intervention plus coûteuse mais potentiellement plus efficace ou stable).

3.  **Fonction de Récompense Immédiate ($R(s, a)$) :** Les récompenses moyennes perçues immédiatement après avoir exécuté l'action $a$ dans l'état $s$ sont définies comme suit :
    *   $R(S_1, A_1) = -2$ (Coût de la maintenance légère en attente).
    *   $R(S_1, A_2) = -10$ (Coût élevé de l'optimisation complète en attente).
    *   $R(S_2, A_1) = +5$ (Bénéfice modéré de la maintenance légère en production).
    *   $R(S_2, A_2) = +8$ (Bénéfice élevé de l'optimisation complète en production).

4.  **Probabilités de Transition ($P(s' | s, a)$) :** Les probabilités de passer de l'état $s$ à l'état $s'$ en exécutant l'action $a$ sont données par le tableau suivant :

    *   **Depuis l'état $S_1$ ("En attente") :**
        *   Action $A_1$ ("Maintenance légère") :
            *   $P(S_1 | S_1, A_1) = 0.6$
            *   $P(S_2 | S_1, A_1) = 0.4$
        *   Action $A_2$ ("Optimisation complète") :
            *   $P(S_1 | S_1, A_2) = 0.1$
            *   $P(S_2 | S_1, A_2) = 0.9$

    *   **Depuis l'état $S_2$ ("En production") :**
        *   Action $A_1$ ("Maintenance légère") :
            *   $P(S_1 | S_2, A_1) = 0.3$
            *   $P(S_2 | S_2, A_1) = 0.7$
        *   Action $A_2$ ("Optimisation complète") :
            *   $P(S_1 | S_2, A_2) = 0.1$
            *   $P(S_2 | S_2, A_2) = 0.9$

5.  **Facteur d'Actualisation ($\gamma$) :** $\gamma = 0.9$.

**Question :**

Votre tâche est d'appliquer l'algorithme d'itération de la valeur pour déterminer la fonction de valeur optimale $V^*(s)$ et la politique optimale $\pi^*(s)$. Pour cet exercice, vous devrez calculer explicitement les fonctions de valeur $V_k(s)$ et les politiques associées $\pi_k(s)$ pour $k=0, 1, 2, \text{ et } 3$.

*   Initialisez la fonction de valeur à $V_0(s) = 0$ pour tous les états $s \in S$.
*   Détaillez chaque étape de calcul pour chaque état et chaque action.
*   Présentez clairement les résultats intermédiaires ($Q_k(s, a)$) et finaux ($V_k(s)$ et $\pi_k(s)$) pour chaque itération $k$.

### Correction Détaillée

Chers étudiants, abordons avec la plus grande rigueur cet exercice fondamental. L'itération de la valeur est un pilier de la résolution des PDM. Chaque étape doit être explicitée avec une précision chirurgicale.

L'opérateur de Bellman pour l'itération de la valeur est défini par la relation de récurrence suivante pour la fonction de valeur $V_k(s)$ et la fonction d'action-valeur $Q_k(s, a)$ :
$$ Q_{k+1}(s, a) = R(s, a) + \gamma \sum_{s' \in S} P(s' | s, a) V_k(s') $$
$$ V_{k+1}(s) = \max_{a \in A} Q_{k+1}(s, a) $$
La politique optimale $\pi_{k+1}(s)$ à l'itération $k+1$ est l'action qui maximise $Q_{k+1}(s, a)$ pour chaque état $s$ :
$$ \pi_{k+1}(s) = \arg\max_{a \in A} Q_{k+1}(s, a) $$

Nous commençons avec l'initialisation spécifiée.

#### Étape d'Initialisation ($k=0$)

Nous initialisons la fonction de valeur à zéro pour tous les états, ce qui est une pratique courante pour un horizon infini.

$$ V_0(S_1) = 0 $$
$$ V_0(S_2) = 0 $$

La politique $\pi_0(s)$ n'est pas définie à ce stade, car il n'y a pas encore eu d'évaluation des actions.

#### Première Itération ($k=1$)

Nous allons calculer $V_1(s)$ en utilisant $V_0(s)$. La formule est :
$$ Q_1(s, a) = R(s, a) + \gamma \sum_{s' \in S} P(s' | s, a) V_0(s') $$
Puisque $V_0(s') = 0$ pour tout $s' \in S$, le terme de la somme s'annule :
$$ \sum_{s' \in S} P(s' | s, a) V_0(s') = P(S_1 | s, a) \cdot 0 + P(S_2 | s, a) \cdot 0 = 0 $$
Ainsi, pour la première itération, la fonction d'action-valeur $Q_1(s, a)$ est simplement la récompense immédiate $R(s, a)$.

**Pour l'état $S_1$ :**

*   **Action $A_1$ :**
    $$ Q_1(S_1, A_1) = R(S_1, A_1) + \gamma \left( P(S_1 | S_1, A_1) V_0(S_1) + P(S_2 | S_1, A_1) V_0(S_2) \right) $$
    $$ Q_1(S_1, A_1) = -2 + 0.9 \left( 0.6 \cdot 0 + 0.4 \cdot 0 \right) $$
    $$ Q_1(S_1, A_1) = -2 + 0.9 \cdot (0) $$
    $$ Q_1(S_1, A_1) = -2 $$

*   **Action $A_2$ :**
    $$ Q_1(S_1, A_2) = R(S_1, A_2) + \gamma \left( P(S_1 | S_1, A_2) V_0(S_1) + P(S_2 | S_1, A_2) V_0(S_2) \right) $$
    $$ Q_1(S_1, A_2) = -10 + 0.9 \left( 0.1 \cdot 0 + 0.9 \cdot 0 \right) $$
    $$ Q_1(S_1, A_2) = -10 + 0.9 \cdot (0) $$
    $$ Q_1(S_1, A_2) = -10 $$

    Nous déterminons $V_1(S_1)$ en prenant le maximum des $Q_1(S_1, a)$ :
    $$ V_1(S_1) = \max(Q_1(S_1, A_1), Q_1(S_1, A_2)) $$
    $$ V_1(S_1) = \max(-2, -10) $$
    $$ V_1(S_1) = -2 $$
    La politique $\pi_1(S_1)$ est l'action qui a donné ce maximum :
    $$ \pi_1(S_1) = A_1 $$

**Pour l'état $S_2$ :**

*   **Action $A_1$ :**
    $$ Q_1(S_2, A_1) = R(S_2, A_1) + \gamma \left( P(S_1 | S_2, A_1) V_0(S_1) + P(S_2 | S_2, A_1) V_0(S_2) \right) $$
    $$ Q_1(S_2, A_1) = 5 + 0.9 \left( 0.3 \cdot 0 + 0.7 \cdot 0 \right) $$
    $$ Q_1(S_2, A_1) = 5 + 0.9 \cdot (0) $$
    $$ Q_1(S_2, A_1) = 5 $$

*   **Action $A_2$ :**
    $$ Q_1(S_2, A_2) = R(S_2, A_2) + \gamma \left( P(S_1 | S_2, A_2) V_0(S_1) + P(S_2 | S_2, A_2) V_0(S_2) \right) $$
    $$ Q_1(S_2, A_2) = 8 + 0.9 \left( 0.1 \cdot 0 + 0.9 \cdot 0 \right) $$
    $$ Q_1(S_2, A_2) = 8 + 0.9 \cdot (0) $$
    $$ Q_1(S_2, A_2) = 8 $$

    Nous déterminons $V_1(S_2)$ en prenant le maximum des $Q_1(S_2, a)$ :
    $$ V_1(S_2) = \max(Q_1(S_2, A_1), Q_1(S_2, A_2)) $$
    $$ V_1(S_2) = \max(5, 8) $$
    $$ V_1(S_2) = 8 $$
    La politique $\pi_1(S_2)$ est l'action qui a donné ce maximum :
    $$ \pi_1(S_2) = A_2 $$

**Récapitulatif pour $k=1$ :**
$$ V_1 = \{ V_1(S_1) = -2, V_1(S_2) = 8 \} $$
$$ \pi_1 = \{ \pi_1(S_1) = A_1, \pi_1(S_2) = A_2 \} $$

#### Deuxième Itération ($k=2$)

Nous allons calculer $V_2(s)$ en utilisant $V_1(s)$. La formule est :
$$ Q_2(s, a) = R(s, a) + \gamma \sum_{s' \in S} P(s' | s, a) V_1(s') $$
Rappel des valeurs de $V_1$: $V_1(S_1) = -2$ et $V_1(S_2) = 8$.

**Pour l'état $S_1$ :**

*   **Action $A_1$ :**
    $$ Q_2(S_1, A_1) = R(S_1, A_1) + \gamma \left( P(S_1 | S_1, A_1) V_1(S_1) + P(S_2 | S_1, A_1) V_1(S_2) \right) $$
    $$ Q_2(S_1, A_1) = -2 + 0.9 \left( 0.6 \cdot (-2) + 0.4 \cdot 8 \right) $$
    $$ Q_2(S_1, A_1) = -2 + 0.9 \left( -1.2 + 3.2 \right) $$
    $$ Q_2(S_1, A_1) = -2 + 0.9 \cdot (2.0) $$
    $$ Q_2(S_1, A_1) = -2 + 1.8 $$
    $$ Q_2(S_1, A_1) = -0.2 $$

*   **Action $A_2$ :**
    $$ Q_2(S_1, A_2) = R(S_1, A_2) + \gamma \left( P(S_1 | S_1, A_2) V_1(S_1) + P(S_2 | S_1, A_2) V_1(S_2) \right) $$
    $$ Q_2(S_1, A_2) = -10 + 0.9 \left( 0.1 \cdot (-2) + 0.9 \cdot 8 \right) $$
    $$ Q_2(S_1, A_2) = -10 + 0.9 \left( -0.2 + 7.2 \right) $$
    $$ Q_2(S_1, A_2) = -10 + 0.9 \cdot (7.0) $$
    $$ Q_2(S_1, A_2) = -10 + 6.3 $$
    $$ Q_2(S_1, A_2) = -3.7 $$

    Nous déterminons $V_2(S_1)$ :
    $$ V_2(S_1) = \max(Q_2(S_1, A_1), Q_2(S_1, A_2)) $$
    $$ V_2(S_1) = \max(-0.2, -3.7) $$
    $$ V_2(S_1) = -0.2 $$
    La politique $\pi_2(S_1)$ :
    $$ \pi_2(S_1) = A_1 $$

**Pour l'état $S_2$ :**

*   **Action $A_1$ :**
    $$ Q_2(S_2, A_1) = R(S_2, A_1) + \gamma \left( P(S_1 | S_2, A_1) V_1(S_1) + P(S_2 | S_2, A_1) V_1(S_2) \right) $$
    $$ Q_2(S_2, A_1) = 5 + 0.9 \left( 0.3 \cdot (-2) + 0.7 \cdot 8 \right) $$
    $$ Q_2(S_2, A_1) = 5 + 0.9 \left( -0.6 + 5.6 \right) $$
    $$ Q_2(S_2, A_1) = 5 + 0.9 \cdot (5.0) $$
    $$ Q_2(S_2, A_1) = 5 + 4.5 $$
    $$ Q_2(S_2, A_1) = 9.5 $$

*   **Action $A_2$ :**
    $$ Q_2(S_2, A_2) = R(S_2, A_2) + \gamma \left( P(S_1 | S_2, A_2) V_1(S_1) + P(S_2 | S_2, A_2) V_1(S_2) \right) $$
    $$ Q_2(S_2, A_2) = 8 + 0.9 \left( 0.1 \cdot (-2) + 0.9 \cdot 8 \right) $$
    $$ Q_2(S_2, A_2) = 8 + 0.9 \left( -0.2 + 7.2 \right) $$
    $$ Q_2(S_2, A_2) = 8 + 0.9 \cdot (7.0) $$
    $$ Q_2(S_2, A_2) = 8 + 6.3 $$
    $$ Q_2(S_2, A_2) = 14.3 $$

    Nous déterminons $V_2(S_2)$ :
    $$ V_2(S_2) = \max(Q_2(S_2, A_1), Q_2(S_2, A_2)) $$
    $$ V_2(S_2) = \max(9.5, 14.3) $$
    $$ V_2(S_2) = 14.3 $$
    La politique $\pi_2(S_2)$ :
    $$ \pi_2(S_2) = A_2 $$

**Récapitulatif pour $k=2$ :**
$$ V_2 = \{ V_2(S_1) = -0.2, V_2(S_2) = 14.3 \} $$
$$ \pi_2 = \{ \pi_2(S_1) = A_1, \pi_2(S_2) = A_2 \} $$

#### Troisième Itération ($k=3$)

Nous allons calculer $V_3(s)$ en utilisant $V_2(s)$. La formule est :
$$ Q_3(s, a) = R(s, a) + \gamma \sum_{s' \in S} P(s' | s, a) V_2(s') $$
Rappel des valeurs de $V_2$: $V_2(S_1) = -0.2$ et $V_2(S_2) = 14.3$.

**Pour l'état $S_1$ :**

*   **Action $A_1$ :**
    $$ Q_3(S_1, A_1) = R(S_1, A_1) + \gamma \left( P(S_1 | S_1, A_1) V_2(S_1) + P(S_2 | S_1, A_1) V_2(S_2) \right) $$
    $$ Q_3(S_1, A_1) = -2 + 0.9 \left( 0.6 \cdot (-0.2) + 0.4 \cdot 14.3 \right) $$
    $$ Q_3(S_1, A_1) = -2 + 0.9 \left( -0.12 + 5.72 \right) $$
    $$ Q_3(S_1, A_1) = -2 + 0.9 \cdot (5.60) $$
    $$ Q_3(S_1, A_1) = -2 + 5.04 $$
    $$ Q_3(S_1, A_1) = 3.04 $$

*   **Action $A_2$ :**
    $$ Q_3(S_1, A_2) = R(S_1, A_2) + \gamma \left( P(S_1 | S_1, A_2) V_2(S_1) + P(S_2 | S_1, A_2) V_2(S_2) \right) $$
    $$ Q_3(S_1, A_2) = -10 + 0.9 \left( 0.1 \cdot (-0.2) + 0.9 \cdot 14.3 \right) $$
    $$ Q_3(S_1, A_2) = -10 + 0.9 \left( -0.02 + 12.87 \right) $$
    $$ Q_3(S_1, A_2) = -10 + 0.9 \cdot (12.85) $$
    $$ Q_3(S_1, A_2) = -10 + 11.565 $$
    $$ Q_3(S_1, A_2) = 1.565 $$

    Nous déterminons $V_3(S_1)$ :
    $$ V_3(S_1) = \max(Q_3(S_1, A_1), Q_3(S_1, A_2)) $$
    $$ V_3(S_1) = \max(3.04, 1.565) $$
    $$ V_3(S_1) = 3.04 $$
    La politique $\pi_3(S_1)$ :
    $$ \pi_3(S_1) = A_1 $$

**Pour l'état $S_2$ :**

*   **Action $A_1$ :**
    $$ Q_3(S_2, A_1) = R(S_2, A_1) + \gamma \left( P(S_1 | S_2, A_1) V_2(S_1) + P(S_2 | S_2, A_1) V_2(S_2) \right) $$
    $$ Q_3(S_2, A_1) = 5 + 0.9 \left( 0.3 \cdot (-0.2) + 0.7 \cdot 14.3 \right) $$
    $$ Q_3(S_2, A_1) = 5 + 0.9 \left( -0.06 + 10.01 \right) $$
    $$ Q_3(S_2, A_1) = 5 + 0.9 \cdot (9.95) $$
    $$ Q_3(S_2, A_1) = 5 + 8.955 $$
    $$ Q_3(S_2, A_1) = 13.955 $$

*   **Action $A_2$ :**
    $$ Q_3(S_2, A_2) = R(S_2, A_2) + \gamma \left( P(S_1 | S_2, A_2) V_2(S_1) + P(S_2 | S_2, A_2) V_2(S_2) \right) $$
    $$ Q_3(S_2, A_2) = 8 + 0.9 \left( 0.1 \cdot (-0.2) + 0.9 \cdot 14.3 \right) $$
    $$ Q_3(S_2, A_2) = 8 + 0.9 \left( -0.02 + 12.87 \right) $$
    $$ Q_3(S_2, A_2) = 8 + 0.9 \cdot (12.85) $$
    $$ Q_3(S_2, A_2) = 8 + 11.565 $$
    $$ Q_3(S_2, A_2) = 19.565 $$

    Nous déterminons $V_3(S_2)$ :
    $$ V_3(S_2) = \max(Q_3(S_2, A_1), Q_3(S_2, A_2)) $$
    $$ V_3(S_2) = \max(13.955, 19.565) $$
    $$ V_3(S_2) = 19.565 $$
    La politique $\pi_3(S_2)$ :
    $$ \pi_3(S_2) = A_2 $$

**Récapitulatif pour $k=3$ :**
$$ V_3 = \{ V_3(S_1) = 3.04, V_3(S_2) = 19.565 \} $$
$$ \pi_3 = \{ \pi_3(S_1) = A_1, \pi_3(S_2) = A_2 \} $$

#### Synthèse des Résultats

Les itérations de la valeur montrent une convergence progressive de la fonction de valeur et de la politique :

| Itération $k$ | $V_k(S_1)$ | $V_k(S_2)$ | $\pi_k(S_1)$ | $\pi_k(S_2)$ |
| :------------ | :--------- | :--------- | :------------ | :------------ |
| 0             | $0$        | $0$        | non définie   | non définie   |
| 1             | $-2$       | $8$        | $A_1$         | $A_2$         |
| 2             | $-0.2$     | $14.3$     | $A_1$         | $A_2$         |
| 3             | $3.04$     | $19.565$   | $A_1$         | $A_2$         |

On observe que la politique optimale s'est stabilisée dès la première itération ($k=1$) dans ce cas précis, sélectionnant l'action $A_1$ ("Maintenance légère") lorsque la ligne est "En attente" ($S_1$), et l'action $A_2$ ("Optimisation complète") lorsque la ligne est "En production" ($S_2$). Cependant, les valeurs $V_k(s)$ continuent d'évoluer, ce qui est attendu tant que la convergence n'est pas atteinte pour la fonction de valeur elle-même. La poursuite de l'itération de la valeur permettrait d'obtenir des estimations de plus en plus précises des valeurs optimales $V^*(s)$.

Cette exploration nous rappelle la puissance des méthodes itératives pour démêler la complexité des processus décisionnels stochastiques. Chaque calcul, même le plus minime, contribue à la compréhension globale du système.