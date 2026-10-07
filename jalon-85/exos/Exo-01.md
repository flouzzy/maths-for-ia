## Exercice 1 : Événements incompatibles et probabilités simples
$\bigstar\star\star\star\star$

### Énoncé

On lance un dé équilibré à $6$ faces. Soit l'univers $\Omega = \{1, 2, 3, 4, 5, 6\}$.
On considère les événements suivants :
$A$ : « Obtenir un résultat pair »
$B$ : « Obtenir un multiple de $3$ »
$C$ : « Obtenir un $5$ »

1. Décrire de manière ensembliste les événements $A$, $B$ et $C$.
2. Les événements $A$ et $B$ sont-ils incompatibles ? Justifier avec l'intersection ensembliste.
3. Calculer $\mathbb{P}(A)$, $\mathbb{P}(B)$ et $\mathbb{P}(A \cup B)$ en utilisant la formule de l'union. Vérifier que la formule donne bien le même résultat qu'un dénombrement direct.


### Correction Détaillée

1. **Description ensembliste :**
$A = \{2, 4, 6\}$
$B = \{3, 6\}$
$C = \{5\}$

2. **Incompatibilité de $A$ et $B$ :**
Deux événements sont incompatibles si et seulement si leur intersection est vide.
$A \cap B = \{2, 4, 6\} \cap \{3, 6\} = \{6\}$.
Puisque $A \cap B \neq \emptyset$, les événements $A$ et $B$ ne sont pas incompatibles. Ils peuvent se réaliser simultanément (si le dé tombe sur $6$).

3. **Calcul des probabilités :**
L'univers $\Omega$ contient $6$ issues équiprobables. Ainsi, pour tout événement $E$, $\mathbb{P}(E) = \frac{\text{Card}(E)}{\text{Card}(\Omega)}$.
- $\mathbb{P}(A) = \frac{3}{6} = \frac{1}{2}$
- $\mathbb{P}(B) = \frac{2}{6} = \frac{1}{3}$
- $\mathbb{P}(A \cap B) = \frac{1}{6}$

D'après la formule de l'union :
$\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B) = \frac{3}{6} + \frac{2}{6} - \frac{1}{6} = \frac{4}{6} = \frac{2}{3}$.

**Vérification par dénombrement direct :**
L'événement $A \cup B$ est « Obtenir un résultat pair ou un multiple de $3$ ».
$A \cup B = \{2, 3, 4, 6\}$.
Donc $\mathbb{P}(A \cup B) = \frac{4}{6} = \frac{2}{3}$. Les résultats correspondent.
