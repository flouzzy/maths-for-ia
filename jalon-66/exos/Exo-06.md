### Intégrale sur une réunion disjointe \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f \in \mathcal{M}_+$. Soient $A, B \in \mathcal{F}$ deux ensembles disjoints ($A \cap B = \emptyset$).
On note $\int_E f d\mu := \int_X (f \mathbf{1}_E) d\mu$.
Montrer que $\int_{A \cup B} f d\mu = \int_A f d\mu + \int_B f d\mu$.

**Correction Détaillée :**
**Étape 1 : Réécriture de l'indicatrice.**
Puisque $A$ et $B$ sont disjoints, la fonction indicatrice de leur réunion est la somme des fonctions indicatrices :
$$\mathbf{1}_{A \cup B} = \mathbf{1}_A + \mathbf{1}_B$$
Par conséquent, la fonction à intégrer est :
$$f \mathbf{1}_{A \cup B} = f (\mathbf{1}_A + \mathbf{1}_B) = f \mathbf{1}_A + f \mathbf{1}_B$$

**Étape 2 : Cas des fonctions simples.**
Si $f$ est une fonction simple positive, disons $s$, alors $s \mathbf{1}_A$ et $s \mathbf{1}_B$ sont aussi des fonctions simples.
Par linéarité de l'intégrale sur les fonctions simples :
$$\int_X s \mathbf{1}_{A \cup B} d\mu = \int_X (s \mathbf{1}_A + s \mathbf{1}_B) d\mu = \int_X s \mathbf{1}_A d\mu + \int_X s \mathbf{1}_B d\mu$$

**Étape 3 : Généralisation (esquisse, car le théorème complet de linéarité requiert Beppo-Levi).**
Par définition, $\int_{A \cup B} f d\mu = \sup \{ \int_X s d\mu \mid 0 \le s \le f \mathbf{1}_{A \cup B}, s \text{ simple} \}$.
Toute fonction simple $s$ majorée par $f \mathbf{1}_{A \cup B}$ peut se décomposer en $s = s \mathbf{1}_A + s \mathbf{1}_B = s_A + s_B$.
Ici, $s_A \le f \mathbf{1}_A$ et $s_B \le f \mathbf{1}_B$.
L'intégrale devient le supremum des sommes $\int s_A d\mu + \int s_B d\mu$.
Le supremum de sommes d'ensembles indépendants (car à support disjoint) est la somme des supremums :
$$\sup (\int s_A d\mu + \int s_B d\mu) = \sup (\int s_A d\mu) + \sup (\int s_B d\mu)$$
Ce qui donne bien $\int_A f d\mu + \int_B f d\mu$.
