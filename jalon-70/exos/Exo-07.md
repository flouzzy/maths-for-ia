## Exercice 7 : Génération de la tribu produit \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Montrer que si $\mathcal{C}_1$ engendre $\mathcal{F}_1$ et $\mathcal{C}_2$ engendre $\mathcal{F}_2$, et s'il existe des suites d'ensembles de $\mathcal{C}_i$ qui recouvrent $X_i$, alors l'ensemble des rectangles $C_1 \times C_2$ (avec $C_i \in \mathcal{C}_i$) engendre la tribu produit $\mathcal{F}_1 \otimes \mathcal{F}_2$.

**Correction :**
1. Soit $\mathcal{G}$ la tribu engendrée par les rectangles $C_1 \times C_2$. Il est clair que $\mathcal{G} \subset \mathcal{F}_1 \otimes \mathcal{F}_2$ car $C_1 \times C_2 \in \mathcal{F}_1 \otimes \mathcal{F}_2$.
2. Montrons l'inclusion inverse. Pour un $C_2 \in \mathcal{C}_2$ fixé, considérons $\mathcal{H}_1 = \{ A \in \mathcal{F}_1 \mid A \times C_2 \in \mathcal{G} \}$.
3. $\mathcal{H}_1$ contient $\mathcal{C}_1$ par définition. De plus, on vérifie facilement que $\mathcal{H}_1$ est une tribu (passage au complémentaire, union dénombrable).
4. Donc $\mathcal{H}_1 = \mathcal{F}_1$. Ainsi, pour tout $A \in \mathcal{F}_1$ et tout $C_2 \in \mathcal{C}_2$, $A \times C_2 \in \mathcal{G}$.
5. On répète le même argument. Pour un $A \in \mathcal{F}_1$ fixé, soit $\mathcal{H}_2 = \{ B \in \mathcal{F}_2 \mid A \times B \in \mathcal{G} \}$.
6. $\mathcal{H}_2$ contient $\mathcal{C}_2$ et est une tribu, donc $\mathcal{H}_2 = \mathcal{F}_2$.
7. Ainsi, tout rectangle $A \times B \in \mathcal{F}_1 \times \mathcal{F}_2$ appartient à $\mathcal{G}$, ce qui prouve que $\mathcal{F}_1 \otimes \mathcal{F}_2 = \mathcal{G}$.
