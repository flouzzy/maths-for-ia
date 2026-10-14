# Exercice 3

\subsection*{Exercice 3 : Indépendance deux à deux et mutuelle \quad $\bigstar\bigstar\star\star\star$}

**Énoncé :**
On lance deux dés parfaits indépendants à $6$ faces.
Soit $A$ l'événement "Le résultat du 1er dé est pair".
Soit $B$ l'événement "Le résultat du 2e dé est impair".
Soit $C$ l'événement "La somme des deux dés est impaire".
Montrer que $A, B, C$ sont indépendants deux à deux, mais ne sont pas mutuellement indépendants.

**Correction :**
1. Modélisation : $\Omega = \{1, 2, 3, 4, 5, 6\}^2$, de cardinal $36$. La probabilité est uniforme.
2. Calculons les probabilités marginales :
   - $P(A) = \frac{3 \times 6}{36} = \frac{1}{2}$.
   - $P(B) = \frac{6 \times 3}{36} = \frac{1}{2}$.
   - Pour $C$, la somme est impaire si on a (Pair, Impair) ou (Impair, Pair). $P(C) = \frac{3 \times 3 + 3 \times 3}{36} = \frac{18}{36} = \frac{1}{2}$.
3. Calculons les probabilités des intersections deux à deux :
   - $A \cap B$ : "1er pair ET 2e impair". Il y a $3 \times 3 = 9$ cas favorables. $P(A \cap B) = \frac{9}{36} = \frac{1}{4} = P(A)P(B)$. (Indépendance).
   - $A \cap C$ : "1er pair ET somme impaire". Cela implique que le 2e dé doit être impair. C'est exactement $A \cap B$. $P(A \cap C) = P(A \cap B) = \frac{1}{4} = P(A)P(C)$. (Indépendance).
   - $B \cap C$ : "2e impair ET somme impaire". Cela implique que le 1er dé doit être pair. C'est encore $A \cap B$. $P(B \cap C) = P(A \cap B) = \frac{1}{4} = P(B)P(C)$. (Indépendance).
4. Les événements $A, B$ et $C$ sont donc indépendants deux à deux.
5. Regardons l'intersection totale $A \cap B \cap C$ : "1er pair ET 2e impair ET somme impaire".
   Puisque "1er pair ET 2e impair" implique nécessairement que la somme est impaire, l'événement $A \cap B$ est inclus dans $C$.
   Donc $A \cap B \cap C = A \cap B$.
   Sa probabilité est $P(A \cap B \cap C) = \frac{1}{4}$.
6. Cependant, $P(A)P(B)P(C) = \frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} = \frac{1}{8}$.
7. Comme $P(A \cap B \cap C) \neq P(A)P(B)P(C)$, la famille $\{A, B, C\}$ n'est pas mutuellement indépendante.
