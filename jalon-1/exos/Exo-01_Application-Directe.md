# Exercice 1 : Construction et interprétation de tables de vérité

## Énoncé
Soient $P$, $Q$ et $R$ trois variables propositionnelles indépendantes.
On considère la formule propositionnelle complexe suivante, notée $F$ :
$$F = \big( (P \Rightarrow Q) \land (Q \Rightarrow R) \big) \Rightarrow (P \Rightarrow R)$$

1. Expliquer pourquoi le nombre de lignes de la table de vérité pour cette formule est égal à $8$.
2. Construire pas-à-pas la table de vérité complète de la formule $F$, en détaillant chaque colonne intermédiaire.
3. Déduire de la table de vérité la nature de la formule $F$ (satisfaisable, tautologie ou contradiction).

---

## Correction Détaillée

### Question 1 : Nombre de lignes de la table de vérité
Chaque variable propositionnelle ($P$, $Q$, $R$) peut prendre de manière indépendante deux valeurs de vérité distinctes : $1$ (Vrai) ou $0$ (Faux).
Puisqu'il y a $3$ variables propositionnelles distinctes, l'ensemble de toutes les configurations possibles (valuations) correspond au produit cartésien $\{0, 1\}^3$.
Le nombre cardinal de cet ensemble est :
$$\text{Cardinal}(\{0, 1\}^3) = 2^3 = 8$$
Il y a donc exactement $8$ valuations distinctes à analyser, ce qui se traduit par $8$ lignes dans notre table de vérité.

### Question 2 : Construction de la table de vérité
Nous allons définir les colonnes de notre tableau dans l'ordre d'évaluation des sous-formules :
- Colonnes 1, 2, 3 : Variables de base $P$, $Q$, $R$.
- Colonne 4 : $P \Rightarrow Q$ (vaut $0$ uniquement si $P=1$ et $Q=0$).
- Colonne 5 : $Q \Rightarrow R$ (vaut $0$ uniquement si $Q=1$ et $R=0$).
- Colonne 6 : $(P \Rightarrow Q) \land (Q \Rightarrow R)$ (conjonction des colonnes 4 et 5 ; vaut $1$ si et seulement si les deux valent $1$).
- Colonne 7 : $P \Rightarrow R$ (vaut $0$ uniquement si $P=1$ et $R=0$).
- Colonne 8 : $F = \text{Col } 6 \Rightarrow \text{Col } 7$ (vaut $0$ uniquement si la colonne 6 vaut $1$ et la colonne 7 vaut $0$).

Dressons le tableau exhaustif :

| Ligne | $P$ | $Q$ | $R$ | $P \Rightarrow Q$ | $Q \Rightarrow R$ | $(P \Rightarrow Q) \land (Q \Rightarrow R)$ | $P \Rightarrow R$ | $F$ |
| :---: | :-: | :-: | :-: | :---------------: | :---------------: | :-----------------------------------------: | :---------------: | :-: |
|   1   |  1  |  1  |  1  |         1         |         1         |                      1                      |         1         |  **1**  |
|   2   |  1  |  1  |  0  |         1         |         0         |                      0                      |         0         |  **1**  |
|   3   |  1  |  0  |  1  |         0         |         1         |                      0                      |         1         |  **1**  |
|   4   |  1  |  0  |  0  |         0         |         1         |                      0                      |         0         |  **1**  |
|   5   |  0  |  1  |  1  |         1         |         1         |                      1                      |         1         |  **1**  |
|   6   |  0  |  1  |  0  |         1         |         0         |                      0                      |         1         |  **1**  |
|   7   |  0  |  0  |  1  |         1         |         1         |                      1                      |         1         |  **1**  |
|   8   |  0  |  0  |  0  |         1         |         1         |                      1                      |         1         |  **1**  |

Vérifions pas-à-pas la ligne 2 :
- $P=1, Q=1, R=0$.
- $P \Rightarrow Q = 1 \Rightarrow 1 = 1$.
- $Q \Rightarrow R = 1 \Rightarrow 0 = 0$.
- Conjonction : $1 \land 0 = 0$.
- $P \Rightarrow R = 1 \Rightarrow 0 = 0$.
- Implication principale : $0 \Rightarrow 0 = 1$. La ligne 2 est correcte.

Vérifions pas-à-pas la ligne 6 :
- $P=0, Q=1, R=0$.
- $P \Rightarrow Q = 0 \Rightarrow 1 = 1$.
- $Q \Rightarrow R = 1 \Rightarrow 0 = 0$.
- Conjonction : $1 \land 0 = 0$.
- $P \Rightarrow R = 0 \Rightarrow 0 = 1$.
- Implication principale : $0 \Rightarrow 1 = 1$. La ligne 6 est correcte.

### Question 3 : Analyse du résultat
La colonne finale associée à la formule $F$ ne contient que des valeurs de vérité $1$ (Vrai) pour l'ensemble des $8$ lignes.
Cela signifie que pour toute valuation $v \in \{0, 1\}^3$, nous avons :
$$v(F) = 1$$
Par définition, la formule $F$ est donc une **tautologie** (notée $\models F$). Elle est sémantiquement universellement valide. De plus, étant toujours vraie, elle est également satisfaisable.
Il s'agit de la loi de transitivité de l'implication logique (ou syllogisme hypothétique).
