# Indépendance deux à deux ne garantit pas l'indépendance mutuelle

**Difficulté :** $\bigstar\bigstar\star\star\star$

Soit $\Omega = \{1, 2, 3, 4\}$ muni de la probabilité uniforme $\mathbb{P}$.
Considérons les événements suivants :
$A = \{1, 2\}$, $B = \{1, 3\}$, et $C = \{1, 4\}$.
1. Calculer $\mathbb{P}(A)$, $\mathbb{P}(B)$ et $\mathbb{P}(C)$.
2. Les événements $A, B, C$ sont-ils indépendants deux à deux ?
3. Les événements $A, B, C$ sont-ils mutuellement indépendants ? Conclure.

### Correction

Soit $\Omega = \{1, 2, 3, 4\}$. La probabilité étant uniforme sur l'univers, la probabilité de chaque événement élémentaire est de $1/4$.

**1. Calcul des probabilités marginales**
L'événement $A = \{1, 2\}$ est composé de 2 événements élémentaires. $\mathbb{P}(A) = 2/4 = 1/2$.
L'événement $B = \{1, 3\}$ est composé de 2 événements élémentaires. $\mathbb{P}(B) = 2/4 = 1/2$.
L'événement $C = \{1, 4\}$ est composé de 2 événements élémentaires. $\mathbb{P}(C) = 2/4 = 1/2$.

**2. Indépendance deux à deux**
Vérifions les intersections deux à deux :
$A \cap B = \{1, 2\} \cap \{1, 3\} = \{1\}$. Donc $\mathbb{P}(A \cap B) = 1/4$.
Or, $\mathbb{P}(A)\mathbb{P}(B) = (1/2) \times (1/2) = 1/4$. Donc $\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)$. $A$ et $B$ sont indépendants.
De même, $A \cap C = \{1\}$. $\mathbb{P}(A \cap C) = 1/4 = \mathbb{P}(A)\mathbb{P}(C)$. $A$ et $C$ sont indépendants.
De même, $B \cap C = \{1\}$. $\mathbb{P}(B \cap C) = 1/4 = \mathbb{P}(B)\mathbb{P}(C)$. $B$ et $C$ sont indépendants.
La famille d'événements $\{A, B, C\}$ est donc indépendante deux à deux.

**3. Indépendance mutuelle**
Pour que la famille soit mutuellement indépendante, il faut aussi vérifier la condition sur l'intersection globale :
$A \cap B \cap C = \{1, 2\} \cap \{1, 3\} \cap \{1, 4\} = \{1\}$.
Donc $\mathbb{P}(A \cap B \cap C) = 1/4$.
D'autre part, calculons le produit des probabilités :
$\mathbb{P}(A)\mathbb{P}(B)\mathbb{P}(C) = (1/2) \times (1/2) \times (1/2) = 1/8$.
On constate de manière frappante que $1/4 \neq 1/8$, soit $\mathbb{P}(A \cap B \cap C) \neq \mathbb{P}(A)\mathbb{P}(B)\mathbb{P}(C)$.
**Conclusion :** La famille $\{A, B, C\}$ n'est pas mutuellement indépendante. Cet exemple de Bernstein démontre que l'indépendance mutuelle est une propriété strictement plus forte que l'indépendance deux à deux.
