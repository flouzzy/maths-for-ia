## Exercice 6 : Le Paradoxe des Anniversaires (Probabilité d'un complémentaire)
$\bigstar\bigstar\bigstar\star\star$

### Énoncé

Dans une classe de $k$ étudiants, on s'intéresse à la probabilité $P_k$ qu'au moins deux étudiants partagent la même date d'anniversaire (en supposant $365$ jours par an, équiprobables et indépendants).
1. Au lieu de calculer directement $P_k$, définir rigoureusement l'événement complémentaire $E_k^c$ et calculer sa probabilité.
2. En déduire la formule de $P_k$ en fonction de $k$.
3. Vérifier numériquement que pour $k=23$, $P_{23} \approx 0.507$ (plus de $50\%$).


### Correction Détaillée

1. **Définition de l'événement complémentaire :**
L'événement $E_k$ est : "Au moins deux étudiants ont la même date d'anniversaire".
Le complémentaire $E_k^c$ est : "Aucun étudiant ne partage sa date d'anniversaire avec un autre". Autrement dit, tous les $k$ étudiants ont des dates d'anniversaire distinctes.

**Calcul de $\mathbb{P}(E_k^c)$ :**
Il y a $365^k$ issues possibles au total (chaque étudiant peut naître n'importe lequel des $365$ jours). C'est le cardinal de l'univers $\Omega$.
Pour compter le nombre d'issues favorables à $E_k^c$ :
- Le 1er étudiant a $365$ choix possibles.
- Le 2ème étudiant doit naître un jour différent, il a $364$ choix.
- Le 3ème étudiant doit naître un jour différent des deux premiers, il a $363$ choix.
- ...
- Le $k$-ième étudiant a $365 - (k - 1) = 365 - k + 1$ choix.
Le nombre total de configurations où tout le monde est né un jour différent est donné par le produit (arrangements) : $A_{365}^k = 365 \times 364 \times \dots \times (365 - k + 1)$.
La probabilité est le ratio :
$\mathbb{P}(E_k^c) = \frac{365 \times 364 \times \dots \times (365 - k + 1)}{365^k}$.
Cette formule peut aussi s'écrire de manière plus compacte avec des factorielles :
$\mathbb{P}(E_k^c) = \frac{365!}{(365-k)! \cdot 365^k}$.

2. **Formule pour $P_k$ :**
Par l'axiome fondamental des probabilités, la somme de la probabilité d'un événement et de son complémentaire vaut $1$.
$P_k = \mathbb{P}(E_k) = 1 - \mathbb{P}(E_k^c)$.
$P_k = 1 - \frac{365 \times 364 \times \dots \times (365 - k + 1)}{365^k}$.
On peut aussi l'écrire comme un produit de fractions :
$P_k = 1 - \left( \frac{365}{365} \cdot \frac{364}{365} \cdot \frac{363}{365} \dots \frac{365 - k + 1}{365} \right) = 1 - \prod_{i=0}^{k-1} \left(1 - \frac{i}{365}\right)$.

3. **Vérification pour $k=23$ :**
$P_{23} = 1 - \left(1 \times \frac{364}{365} \times \frac{363}{365} \times \dots \times \frac{343}{365} \right)$.
En effectuant le calcul produit terme à terme :
$\mathbb{P}(E_{23}^c) \approx 0.4927$.
Donc $P_{23} = 1 - 0.4927 = 0.5073$.
Il y a donc plus d'une chance sur deux (environ $50.7\%$) que deux étudiants soient nés le même jour dans une classe de $23$ élèves.
