# Exercice 2 : Simplification sémantique par l'algèbre de Boole

## Énoncé
Soient $P$ et $Q$ deux variables propositionnelles.
On considère la formule logique suivante :
$$A = \big( P \lor (\neg P \land Q) \big) \land \big( \neg Q \lor (P \land \neg Q) \big)$$

1. Simplifier algébriquement le membre de gauche $L = P \lor (\neg P \land Q)$ en utilisant les axiomes de distributivité et d'absorption.
2. Simplifier algébriquement le membre de droite $R = \neg Q \lor (P \land \neg Q)$ en utilisant la loi d'absorption.
3. En déduire la forme simplifiée finale de la formule $A$.
4. Démontrer le résultat obtenu en dressant la table de vérité de la formule originale $A$.

---

## Correction Détaillée

### Question 1 : Simplification du membre de gauche $L = P \lor (\neg P \land Q)$
Appliquons la règle de **distributivité de la disjonction ($\lor$) par rapport à la conjonction ($\land$)** :
$$L = (P \lor \neg P) \land (P \lor Q)$$

Or, d'après la loi du tiers exclu (complémentarité dans les algèbres de Boole) :
$$P \lor \neg P \equiv 1$$

Substituons cette valeur dans l'expression :
$$L \equiv 1 \land (P \lor Q)$$

Puisque $1$ (Vrai) est l'élément neutre pour la conjonction ($\land$) :
$$L \equiv P \lor Q$$

---

### Question 2 : Simplification du membre de droite $R = \neg Q \lor (P \land \neg Q)$
Nous pouvons appliquer directement la **loi d'absorption** de l'algèbre de Boole.
Rappelons la loi d'absorption générale : pour tous éléments $x$ et $y$, $x \lor (y \land x) \equiv x$.

Ici, posons $x = \neg Q$ et $y = P$. L'expression devient :
$$R = x \lor (y \land x)$$

Par application directe de la loi d'absorption :
$$R \equiv x \equiv \neg Q$$

---

### Question 3 : Simplification finale de la formule $A$
La formule complète s'écrit $A = L \land R$.
Substituons les expressions simplifiées obtenues aux questions 1 et 2 :
$$A \equiv (P \lor Q) \land \neg Q$$

Appliquons la distributivité de la conjonction ($\land$) par rapport à la disjonction ($\lor$) :
$$A \equiv (P \land \neg Q) \lor (Q \land \neg Q)$$

D'après le principe de non-contradiction, $Q \land \neg Q \equiv 0$.
L'expression devient :
$$A \equiv (P \land \neg Q) \lor 0$$

Puisque $0$ (Faux) est l'élément neutre pour la disjonction ($\lor$) :
$$A \equiv P \land \neg Q$$

La formule originale complexe $A$ est donc sémantiquement équivalente à la conjonction simple de $P$ et de la négation de $Q$.

---

### Question 4 : Validation par table de vérité
Construisons la table de vérité pour vérifier l'équivalence $A \equiv P \land \neg Q$.

| $P$ | $Q$ | $\neg P$ | $\neg Q$ | $\neg P \land Q$ | $L = P \lor (\neg P \land Q)$ | $P \land \neg Q$ | $R = \neg Q \lor (P \land \neg Q)$ | $A = L \land R$ | $P \land \neg Q$ (cible) |
| :-: | :-: | :------: | :------: | :--------------: | :---------------------------: | :--------------: | :--------------------------------: | :-------------: | :----------------------: |
|  1  |  1  |    0     |    0     |        0         |               1               |        0         |                 0                  |      **0**      |          **0**           |
|  1  |  0  |    0     |    1     |        0         |               1               |        1         |                 1                  |      **1**      |          **1**           |
|  0  |  1  |    1     |    0     |        1         |               1               |        0         |                 0                  |      **0**      |          **0**           |
|  0  |  0  |    1     |    1     |        0         |               0               |        0         |                 1                  |      **0**      |          **0**           |

Les colonnes $A = L \land R$ (colonne 9) et $P \land \neg Q$ (colonne 10) sont parfaitement identiques pour toutes les lignes $\{0, 1, 0, 0\}$.
L'équivalence logique $A \equiv P \land \neg Q$ est donc rigoureusement démontrée par la méthode sémantique.
