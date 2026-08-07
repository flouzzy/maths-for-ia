# Exercice 4 - Niveau $\bigstar\bigstar\bigstar\star\star$

## Énoncé
Démontrer que l'union de deux adhérences est l'adhérence de l'union : $\overline{A \cup B} = \bar{A} \cup \bar{B}$.

## Démonstration
Commençons par montrer l'inclusion $\bar{A} \cup \bar{B} \subset \overline{A \cup B}$.
Puisque $A \subset A \cup B$, alors $\bar{A} \subset \overline{A \cup B}$ (par croissance de l'adhérence).
De même, $B \subset A \cup B$ implique $\bar{B} \subset \overline{A \cup B}$.
Par réunion, $\bar{A} \cup \bar{B} \subset \overline{A \cup B}$.
Montrons l'autre inclusion. Les ensembles $\bar{A}$ et $\bar{B}$ sont fermés.
Une union finie de fermés est fermée, donc $\bar{A} \cup \bar{B}$ est fermé.
De plus, $A \subset \bar{A}$ et $B \subset \bar{B}$, donc $A \cup B \subset \bar{A} \cup \bar{B}$.
Puisque $\overline{A \cup B}$ est le *plus petit* fermé contenant $A \cup B$, et que $\bar{A} \cup \bar{B}$ est un fermé contenant $A \cup B$, nous avons nécessairement :
$\overline{A \cup B} \subset \bar{A} \cup \bar{B}$.
Les deux inclusions démontrent l'égalité.
