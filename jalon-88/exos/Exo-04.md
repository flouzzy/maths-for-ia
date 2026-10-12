# Exercice 4 : L'indépendance deux à deux n'implique pas l'indépendance mutuelle

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
On lance deux pièces de monnaie équilibrées, de manière indépendante. L'univers de cette expérience aléatoire est $\Omega = \{(P, P), (P, F), (F, P), (F, F)\}$, avec la probabilité uniforme.
On définit les trois événements suivants :
- $A$ : "La première pièce donne Pile"
- $B$ : "La seconde pièce donne Pile"
- $C$ : "Les deux pièces donnent le même résultat"

1. Expliciter sous forme d'ensembles les événements $A$, $B$ et $C$, et calculer leurs probabilités respectives.
2. Démontrer que les événements $A$, $B$ et $C$ sont indépendants deux à deux.
3. Démontrer que les événements $A$, $B$ et $C$ ne sont pas mutuellement indépendants.

---
**Correction détaillée :**

**Question 1 : Explicitation et probabilités**
Puisque la probabilité est uniforme sur les 4 éléments de $\Omega$, chaque issue a une probabilité de $\frac{1}{4}$.
- $A = \{(P, P), (P, F)\}$. Donc $\mathbb{P}(A) = \frac{2}{4} = \frac{1}{2}$.
- $B = \{(P, P), (F, P)\}$. Donc $\mathbb{P}(B) = \frac{2}{4} = \frac{1}{2}$.
- $C = \{(P, P), (F, F)\}$. Donc $\mathbb{P}(C) = \frac{2}{4} = \frac{1}{2}$.

**Question 2 : Indépendance deux à deux**
Nous devons calculer la probabilité de toutes les paires d'intersections.
- Intersection $A \cap B$ : Les issues où la première pièce est Pile ET la seconde pièce est Pile.
  $A \cap B = \{(P, P)\}$.
  Donc $\mathbb{P}(A \cap B) = \frac{1}{4}$.
  Vérification : $\mathbb{P}(A) \times \mathbb{P}(B) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4} = \mathbb{P}(A \cap B)$. Les événements $A$ et $B$ sont indépendants.
- Intersection $A \cap C$ : Les issues où la première pièce est Pile ET les deux pièces donnent le même résultat.
  $A \cap C = \{(P, P)\}$.
  Donc $\mathbb{P}(A \cap C) = \frac{1}{4}$.
  Vérification : $\mathbb{P}(A) \times \mathbb{P}(C) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4} = \mathbb{P}(A \cap C)$. Les événements $A$ et $C$ sont indépendants.
- Intersection $B \cap C$ : Les issues où la seconde pièce est Pile ET les deux pièces donnent le même résultat.
  $B \cap C = \{(P, P)\}$.
  Donc $\mathbb{P}(B \cap C) = \frac{1}{4}$.
  Vérification : $\mathbb{P}(B) \times \mathbb{P}(C) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4} = \mathbb{P}(B \cap C)$. Les événements $B$ et $C$ sont indépendants.
Conclusion : $A, B$ et $C$ sont bien indépendants deux à deux.

**Question 3 : Indépendance mutuelle**
L'indépendance mutuelle d'un triplet exige que $\mathbb{P}(A \cap B \cap C) = \mathbb{P}(A)\mathbb{P}(B)\mathbb{P}(C)$.
Calculons l'intersection des trois événements : $A \cap B \cap C$. C'est l'ensemble des issues où la première pièce est Pile, la seconde est Pile, et les deux sont identiques.
$A \cap B \cap C = \{(P, P)\}$.
Donc $\mathbb{P}(A \cap B \cap C) = \frac{1}{4}$.
Or, le produit des probabilités individuelles est :
$$ \mathbb{P}(A) \times \mathbb{P}(B) \times \mathbb{P}(C) = \frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} = \frac{1}{8} $$
Nous avons clairement $\frac{1}{4} \neq \frac{1}{8}$, c'est-à-dire :
$$ \mathbb{P}(A \cap B \cap C) \neq \mathbb{P}(A) \times \mathbb{P}(B) \times \mathbb{P}(C) $$
Les événements ne sont donc **pas** mutuellement indépendants. Ce contre-exemple classique (dû à Bernstein) montre la subtilité de la définition d'indépendance de familles d'événements. $\blacksquare$
