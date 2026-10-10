\subsection*{Exercice 2 : Indépendance conditionnelle \quad $\bigstar\star\star\star\star$}

On lance un dé équilibré à 6 faces. On définit les événements :
- $A$ : "Le résultat est pair"
- $B$ : "Le résultat est un multiple de 3"
- $C$ : "Le résultat est inférieur ou égal à 4"
Les événements $A$ et $B$ sont-ils indépendants conditionnellement à $C$ ?

**Correction :**
1. L'univers est $\Omega = \{1, 2, 3, 4, 5, 6\}$.
2. $A = \{2, 4, 6\}$, $B = \{3, 6\}$, $C = \{1, 2, 3, 4\}$.
3. $\mathbb{P}(C) = 4/6 = 2/3$.
4. On calcule la probabilité conditionnelle : $\mathbb{P}_C(X) = \frac{\mathbb{P}(X \cap C)}{\mathbb{P}(C)}$.
5. $A \cap C = \{2, 4\} \implies \mathbb{P}_C(A) = \frac{2/6}{4/6} = 1/2$.
6. $B \cap C = \{3\} \implies \mathbb{P}_C(B) = \frac{1/6}{4/6} = 1/4$.
7. L'intersection $(A \cap B) \cap C = \{6\} \cap \{1, 2, 3, 4\} = \emptyset \implies \mathbb{P}_C(A \cap B) = 0$.
8. $\mathbb{P}_C(A)\mathbb{P}_C(B) = (1/2) \times (1/4) = 1/8 \neq 0$.
9. Les événements ne sont pas indépendants conditionnellement à $C$.