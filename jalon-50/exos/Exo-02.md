# Exercice 2 - Niveau $\bigstar\bigstar\star\star\star$

## Énoncé
Démontrer que l'opérateur d'adhérence est idempotent : $\overline{\bar{A}} = \bar{A}$.

## Démonstration
Soit $A \subset X$.
Par définition, $\bar{A}$ est l'intersection de tous les fermés contenant $A$.
Une intersection quelconque d'ensembles fermés étant fermée, $\bar{A}$ est lui-même un ensemble fermé.
L'adhérence de $\bar{A}$, notée $\overline{\bar{A}}$, est le plus petit fermé contenant $\bar{A}$.
Puisque $\bar{A}$ est déjà fermé et se contient lui-même ($\bar{A} \subset \bar{A}$), il est le plus petit des fermés le contenant.
Par conséquent, $\overline{\bar{A}} = \bar{A}$.
