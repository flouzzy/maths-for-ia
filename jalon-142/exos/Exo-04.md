Mes chers étudiants,

Bienvenue à ce jalon de notre exploration. Voici l'exercice 04. La rigueur sera notre guide.

---

# Jalon 142 : Processus de décision de Markov
## Exercice 04/10 : Évaluation d'une Politique Fixe dans un MDP Simple (Difficulté : 04/10)

### Énoncé Rigoureux et Formel

Considérons un Processus de Décision de Markov (PDM) défini par les éléments suivants :

1.  **Ensemble des États ($S$)** : L'espace des états est discret et fini, $S = \{s_1, s_2, s_3\}$.
2.  **Ensemble des Actions ($A$)** : L'espace des actions est discret et fini, $A = \{a_1, a_2\}$.
3.  **Fonction de Transition de Probabilité ($P$)** : Pour chaque état $s \in S$ et chaque action $a \in A$, $P(s'|s,a)$ est la probabilité de passer à l'état $s'$ si l'action $a$ est effectuée dans l'état $s$. Ces probabilités sont définies comme suit :
    *   Depuis l'état $s_1$:
        *   Si l'action $a_1$ est choisie : $P(s_2|s_1,a_1) = 1.0$.
        *   Si l'action $a_2$ est choisie : $P(s_1|s_1,a_2) = 0.5$, $P(s_3|s_1,a_2) = 0.5$.
    *   Depuis l'état $s_2$:
        *   Si l'action $a_1$ est choisie : $P(s_1|s_2,a_1) = 1.0$.
        *   Si l'action $a_2$ est choisie : $P(s_3|s_2,a_2) = 1.0$.
    *   Depuis l'état $s_3$:
        *   Si l'action $a_1$ est choisie : $P(s_2|s_3,a_1) = 1.0$.
        *   Si l'action $a_2$ est choisie : $P(s_3|s_3,a_2) = 1.0$.
    Pour toutes les paires $(s,a)$ et les états $s'$ non mentionnés, la probabilité de transition $P(s'|s,a)$ est nulle.

4.  **Fonction de Récompense ($R$)** : La fonction de récompense immédiate moyenne $R(s,a)$ représente la récompense perçue en effectuant l'action $a$ dans l'état $s$. Elle est définie comme suit :
    *   $R(s_1, a_1) = +10$
    *   $R(s_1, a_2) = -1$
    *   $R(s_2, a_1) = -5$
    *   $R(s_2, a_2) = +2$
    *   $R(s_3, a_1) = +1$
    *   $R(s_3, a_2) = -10$

5.  **Facteur d'Actualisation ($\gamma$)** : Le facteur d'actualisation est fixé à $\gamma = 0.9$.

Nous considérons une politique déterministe fixe $\pi$ définie comme suit :
*   $\pi(s_1) = a_1$
*   $\pi(s_2) = a_2$
*   $\pi(s_3) = a_1$

Votre tâche est de calculer la fonction de valeur $V^\pi(s)$ pour chaque état $s \in S$. La fonction de valeur $V^\pi(s)$ représente la somme actualisée des récompenses futures espérées en partant de l'état $s$ et en suivant la politique $\pi$.

### Correction Détaillée

Pour évaluer la politique donnée $\pi$, nous devons déterminer la fonction de valeur $V^\pi(s)$ pour chaque état $s \in S$. La fonction de valeur pour une politique fixe $\pi$ est donnée par l'équation de Bellman spécifique à cette politique :

$$
V^\pi(s) = R(s, \pi(s)) + \gamma \sum_{s' \in S} P(s'|s, \pi(s)) V^\pi(s') \quad \text{pour tout } s \in S
$$

Développons cette équation pour chacun des états $s_1, s_2, s_3$.

#### 1. Équation de Bellman pour l'état $s_1$:

La politique $\pi$ spécifie que l'action à prendre dans l'état $s_1$ est $a_1$, c'est-à-dire $\pi(s_1) = a_1$.
En substituant dans l'équation de Bellman, nous obtenons :

$$
V^\pi(s_1) = R(s_1, \pi(s_1)) + \gamma \sum_{s' \in S} P(s'|s_1, \pi(s_1)) V^\pi(s')
$$
$$
V^\pi(s_1) = R(s_1, a_1) + \gamma \sum_{s' \in S} P(s'|s_1, a_1) V^\pi(s')
$$

D'après les données de l'énoncé, nous avons $R(s_1, a_1) = +10$.
Pour les probabilités de transition depuis $s_1$ avec l'action $a_1$, nous avons $P(s_2|s_1,a_1) = 1.0$ et $P(s'|s_1,a_1) = 0$ pour $s' \neq s_2$.
En substituant ces valeurs :

$$
V^\pi(s_1) = +10 + \gamma \left( P(s_1|s_1, a_1) V^\pi(s_1) + P(s_2|s_1, a_1) V^\pi(s_2) + P(s_3|s_1, a_1) V^\pi(s_3) \right)
$$
$$
V^\pi(s_1) = +10 + 0.9 \left( (0) V^\pi(s_1) + (1.0) V^\pi(s_2) + (0) V^\pi(s_3) \right)
$$
$$
V^\pi(s_1) = 10 + 0.9 V^\pi(s_2) \quad \text{(Équation 1)}
$$

#### 2. Équation de Bellman pour l'état $s_2$:

La politique $\pi$ spécifie que l'action à prendre dans l'état $s_2$ est $a_2$, c'est-à-dire $\pi(s_2) = a_2$.
En substituant dans l'équation de Bellman, nous obtenons :

$$
V^\pi(s_2) = R(s_2, \pi(s_2)) + \gamma \sum_{s' \in S} P(s'|s_2, \pi(s_2)) V^\pi(s')
$$
$$
V^\pi(s_2) = R(s_2, a_2) + \gamma \sum_{s' \in S} P(s'|s_2, a_2) V^\pi(s')
$$

D'après les données de l'énoncé, nous avons $R(s_2, a_2) = +2$.
Pour les probabilités de transition depuis $s_2$ avec l'action $a_2$, nous avons $P(s_3|s_2,a_2) = 1.0$ et $P(s'|s_2,a_2) = 0$ pour $s' \neq s_3$.
En substituant ces valeurs :

$$
V^\pi(s_2) = +2 + \gamma \left( P(s_1|s_2, a_2) V^\pi(s_1) + P(s_2|s_2, a_2) V^\pi(s_2) + P(s_3|s_2, a_2) V^\pi(s_3) \right)
$$
$$
V^\pi(s_2) = +2 + 0.9 \left( (0) V^\pi(s_1) + (0) V^\pi(s_2) + (1.0) V^\pi(s_3) \right)
$$
$$
V^\pi(s_2) = 2 + 0.9 V^\pi(s_3) \quad \text{(Équation 2)}
$$

#### 3. Équation de Bellman pour l'état $s_3$:

La politique $\pi$ spécifie que l'action à prendre dans l'état $s_3$ est $a_1$, c'est-à-dire $\pi(s_3) = a_1$.
En substituant dans l'équation de Bellman, nous obtenons :

$$
V^\pi(s_3) = R(s_3, \pi(s_3)) + \gamma \sum_{s' \in S} P(s'|s_3, \pi(s_3)) V^\pi(s')
$$
$$
V^\pi(s_3) = R(s_3, a_1) + \gamma \sum_{s' \in S} P(s'|s_3, a_1) V^\pi(s')
$$

D'après les données de l'énoncé, nous avons $R(s_3, a_1) = +1$.
Pour les probabilités de transition depuis $s_3$ avec l'action $a_1$, nous avons $P(s_2|s_3,a_1) = 1.0$ et $P(s'|s_3,a_1) = 0$ pour $s' \neq s_2$.
En substituant ces valeurs :

$$
V^\pi(s_3) = +1 + \gamma \left( P(s_1|s_3, a_1) V^\pi(s_1) + P(s_2|s_3, a_1) V^\pi(s_2) + P(s_3|s_3, a_1) V^\pi(s_3) \right)
$$
$$
V^\pi(s_3) = +1 + 0.9 \left( (0) V^\pi(s_1) + (1.0) V^\pi(s_2) + (0) V^\pi(s_3) \right)
$$
$$
V^\pi(s_3) = 1 + 0.9 V^\pi(s_2) \quad \text{(Équation 3)}
$$

#### 4. Résolution du Système d'Équations Linéaires :

Nous avons maintenant un système de trois équations linéaires avec trois inconnues ($V^\pi(s_1)$, $V^\pi(s_2)$, $V^\pi(s_3)$) :

1.  $V^\pi(s_1) = 10 + 0.9 V^\pi(s_2)$
2.  $V^\pi(s_2) = 2 + 0.9 V^\pi(s_3)$
3.  $V^\pi(s_3) = 1 + 0.9 V^\pi(s_2)$

Nous allons résoudre ce système par substitution.
Commençons par substituer l'Équation 2 dans l'Équation 3, car l'Équation 3 exprime $V^\pi(s_3)$ en fonction de $V^\pi(s_2)$ et l'Équation 2 exprime $V^\pi(s_2)$ en fonction de $V^\pi(s_3)$, créant ainsi une dépendance cyclique entre $V^\pi(s_2)$ et $V^\pi(s_3)$.

Substituons l'expression de $V^\pi(s_2)$ de l'Équation 2 dans l'Équation 3 :
$$
V^\pi(s_3) = 1 + 0.9 \left( 2 + 0.9 V^\pi(s_3) \right)
$$
Distribuons le terme $0.9$ :
$$
V^\pi(s_3) = 1 + (0.9 \times 2) + (0.9 \times 0.9) V^\pi(s_3)
$$
$$
V^\pi(s_3) = 1 + 1.8 + 0.81 V^\pi(s_3)
$$
Combinons les termes constants :
$$
V^\pi(s_3) = 2.8 + 0.81 V^\pi(s_3)
$$
Regroupons les termes $V^\pi(s_3)$ :
$$
V^\pi(s_3) - 0.81 V^\pi(s_3) = 2.8
$$
$$
(1 - 0.81) V^\pi(s_3) = 2.8
$$
$$
0.19 V^\pi(s_3) = 2.8
$$
Divisons pour trouver $V^\pi(s_3)$ :
$$
V^\pi(s_3) = \frac{2.8}{0.19}
$$
Pour travailler avec des fractions exactes :
$$
V^\pi(s_3) = \frac{280}{19}
$$
Soit $V^\pi(s_3) \approx 14.736842$

Maintenant que nous avons $V^\pi(s_3)$, nous pouvons calculer $V^\pi(s_2)$ en utilisant l'Équation 2 :
$$
V^\pi(s_2) = 2 + 0.9 V^\pi(s_3)
$$
Substituons la valeur exacte de $V^\pi(s_3)$ :
$$
V^\pi(s_2) = 2 + 0.9 \times \frac{280}{19}
$$
Multiplions $0.9$ par $280/19$:
$$
V^\pi(s_2) = 2 + \frac{0.9 \times 280}{19}
$$
$$
V^\pi(s_2) = 2 + \frac{252}{19}
$$
Pour additionner, mettons $2$ au même dénominateur :
$$
V^\pi(s_2) = \frac{2 \times 19}{19} + \frac{252}{19}
$$
$$
V^\pi(s_2) = \frac{38}{19} + \frac{252}{19}
$$
$$
V^\pi(s_2) = \frac{38 + 252}{19}
$$
$$
V^\pi(s_2) = \frac{290}{19}
$$
Soit $V^\pi(s_2) \approx 15.263158$

Enfin, nous pouvons calculer $V^\pi(s_1)$ en utilisant l'Équation 1 :
$$
V^\pi(s_1) = 10 + 0.9 V^\pi(s_2)
$$
Substituons la valeur exacte de $V^\pi(s_2)$ :
$$
V^\pi(s_1) = 10 + 0.9 \times \frac{290}{19}
$$
Multiplions $0.9$ par $290/19$:
$$
V^\pi(s_1) = 10 + \frac{0.9 \times 290}{19}
$$
$$
V^\pi(s_1) = 10 + \frac{261}{19}
$$
Pour additionner, mettons $10$ au même dénominateur :
$$
V^\pi(s_1) = \frac{10 \times 19}{19} + \frac{261}{19}
$$
$$
V^\pi(s_1) = \frac{190}{19} + \frac{261}{19}
$$
$$
V^\pi(s_1) = \frac{190 + 261}{19}
$$
$$
V^\pi(s_1) = \frac{451}{19}
$$
Soit $V^\pi(s_1) \approx 23.736842$

#### 5. Vérification des Résultats :

Il est toujours judicieux de vérifier nos solutions en les substituant dans les équations originales.

1.  Pour $V^\pi(s_1) = 10 + 0.9 V^\pi(s_2)$:
    $$
    \frac{451}{19} = 10 + 0.9 \times \frac{290}{19}
    $$
    $$
    \frac{451}{19} = 10 + \frac{261}{19}
    $$
    $$
    \frac{451}{19} = \frac{190}{19} + \frac{261}{19}
    $$
    $$
    \frac{451}{19} = \frac{451}{19} \quad (\text{Vérifié})
    $$

2.  Pour $V^\pi(s_2) = 2 + 0.9 V^\pi(s_3)$:
    $$
    \frac{290}{19} = 2 + 0.9 \times \frac{280}{19}
    $$
    $$
    \frac{290}{19} = 2 + \frac{252}{19}
    $$
    $$
    \frac{290}{19} = \frac{38}{19} + \frac{252}{19}
    $$
    $$
    \frac{290}{19} = \frac{290}{19} \quad (\text{Vérifié})
    $$

3.  Pour $V^\pi(s_3) = 1 + 0.9 V^\pi(s_2)$:
    $$
    \frac{280}{19} = 1 + 0.9 \times \frac{290}{19}
    $$
    $$
    \frac{280}{19} = 1 + \frac{261}{19}
    $$
    $$
    \frac{280}{19} = \frac{19}{19} + \frac{261}{19}
    $$
    $$
    \frac{280}{19} = \frac{280}{19} \quad (\text{Vérifié})
    $$

Toutes les équations sont satisfaites, confirmant l'exactitude des calculs.

#### Conclusion

La fonction de valeur pour la politique $\pi$ spécifiée est :
*   $V^\pi(s_1) = \frac{451}{19} \approx 23.737$
*   $V^\pi(s_2) = \frac{290}{19} \approx 15.263$
*   $V^\pi(s_3) = \frac{280}{19} \approx 14.737$

Ces valeurs représentent l'espérance de la somme actualisée des récompenses que l'agent obtiendra en démarrant dans chaque état respectif et en suivant scrupuleusement la politique $\pi$. Cet exercice démontre la méthode fondamentale d'évaluation d'une politique dans un PDM, un prérequis indispensable avant d'aborder les algorithmes d'optimisation de politiques.