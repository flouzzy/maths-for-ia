# Exercice 7 - Niveau $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
Démontrer que l'intérieur d'une intersection finie est l'intersection des intérieurs : $\text{Int}(A \cap B) = \text{Int}(A) \cap \text{Int}(B)$.

## Démonstration
Puisque $A \cap B \subset A$, la monotonie de l'intérieur implique $\text{Int}(A \cap B) \subset \text{Int}(A)$.
De même, $\text{Int}(A \cap B) \subset \text{Int}(B)$.
Par intersection, $\text{Int}(A \cap B) \subset \text{Int}(A) \cap \text{Int}(B)$.
Pour l'inclusion inverse : $\text{Int}(A)$ est ouvert et contenu dans $A$. $\text{Int}(B)$ est ouvert et contenu dans $B$.
L'intersection finie d'ouverts est ouverte, donc $\text{Int}(A) \cap \text{Int}(B)$ est un ouvert.
De plus, cet ouvert est manifestement contenu dans $A \cap B$.
Étant un ouvert contenu dans $A \cap B$, il est contenu dans le *plus grand* ouvert contenu dans $A \cap B$, c'est-à-dire son intérieur.
Ainsi, $\text{Int}(A) \cap \text{Int}(B) \subset \text{Int}(A \cap B)$.
La double inclusion prouve l'égalité.
