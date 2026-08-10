# Exercice 6 : Réfutation et résolution de clauses

## Énoncé
En logique propositionnelle, la **résolution** est une règle d'inférence syntaxique qui opère sur des clauses. La règle de résolution s'énonce ainsi :
$$\text{De } A \lor B \quad \text{et} \quad \neg A \lor C, \quad \text{on déduit} \quad B \lor C$$
La clause $B \lor C$ est appelée la **résolvante** des deux clauses parentes. La variable $A$ est la variable pivot.
Si l'une des clauses est réduite à un littéral unique (par exemple $A$) et l'autre à sa négation (par exemple $\neg A$), la résolvante est la **clause vide**, notée $\square$ (ou $\bot$), qui représente une contradiction.

Considérons la base de connaissances $\Sigma$ composée des quatre clauses suivantes :
1. $C_1 = P \lor Q$
2. $C_2 = \neg P \lor Q$
3. $C_3 = P \lor \neg Q$
4. $C_4 = \neg P \lor \neg Q$

1. Expliquer le principe de la **démonstration par réfutation** (preuve par l'absurde à l'aide de la résolution).
2. Utiliser la méthode de réfutation par résolution pour démontrer que la base de connaissances $\Sigma$ est incompatible (c'est-à-dire non satisfaisable). On construira pour cela un arbre de résolution menant à la clause vide $\square$.

---

## Correction Détaillée

### Question 1 : Principe de la démonstration par réfutation
La démonstration par réfutation s'appuie sur le théorème logique suivant : un ensemble de formules $\Sigma$ implique logiquement une formule $A$ (noté $\Sigma \models A$) si et seulement si l'ensemble $\Sigma \cup \{\neg A\}$ est insatisfaisable (c'est-à-dire contradictoire).

En résolution, pour démontrer qu'une base de connaissances est insatisfaisable, on applique de manière répétée la règle d'inférence de résolution sur les clauses disponibles dans $\Sigma$. Si l'on parvient à déduire la clause vide $\square$, cela signifie que la base de connaissances contient une contradiction sémantique sous-jacente. Comme la règle de résolution est **correcte** (si elle produit $\square$, alors l'ensemble est insatisfaisable) et **complète pour la réfutation** (si l'ensemble est insatisfaisable, il existe toujours une suite d'applications de la résolution menant à $\square$), l'obtention de la clause vide constitue une preuve irréfutable d'insatisfaisabilité.

---

### Question 2 : Réfutation par résolution sur $\Sigma$
Notre but est de déduire la clause vide $\square$ à partir de notre ensemble de clauses de départ :
$$\Sigma = \{ P \lor Q, \quad \neg P \lor Q, \quad P \lor \neg Q, \quad \neg P \lor \neg Q \}$$

Appliquons la règle de résolution pas-à-pas en choisissant judicieusement les pivots :

1. **Étape 1 : Résolution sur le pivot $P$ (première paire de clauses)**
   Considérons les clauses parentes :
   - $C_1 = P \lor Q$
   - $C_2 = \neg P \lor Q$
   
   La variable pivot est $P$. La règle de résolution élimine $P$ et $\neg P$ pour former la disjonction des littéraux restants :
   $$C_5 = \text{Res}(C_1, C_2) = Q \lor Q$$
   Par la règle d'idempotence de la disjonction ($Q \lor Q \equiv Q$), nous obtenons le littéral unitaire :
   $$C_5 = Q$$

2. **Étape 2 : Résolution sur le pivot $P$ (seconde paire de clauses)**
   Considérons les clauses parentes :
   - $C_3 = P \lor \neg Q$
   - $C_4 = \neg P \lor \neg Q$
   
   La variable pivot est $P$. La résolution produit :
   $$C_6 = \text{Res}(C_3, C_4) = \neg Q \lor \neg Q$$
   Par la règle d'idempotence, nous obtenons le littéral unitaire :
   $$C_6 = \neg Q$$

3. **Étape 3 : Déduction de la contradiction (clause vide)**
   Considérons désormais les deux clauses dérivées unitaires :
   - $C_5 = Q$
   - $C_6 = \neg Q$
   
   Appliquons la règle de résolution sur le pivot $Q$. Puisqu'il n'y a plus aucun autre littéral dans les clauses, nous déduisons la clause vide :
   $$C_7 = \text{Res}(C_5, C_6) = \square$$

L'arbre de résolution menant à la clause vide $\square$ est donc construit avec succès. La base de connaissances $\Sigma$ est incompatible et non satisfaisable.

---

### Représentation graphique de l'arbre de résolution

```text
       C1: P v Q     C2: ~P v Q           C3: P v ~Q    C4: ~P v ~Q
          \           /                      \           /
           \         /                        \         /
            \       /                          \       /
             C5: Q                              C6: ~Q
               \                                  /
                \                                /
                 \                              /
                  \                            /
                         C7: [Clause vide]
```
