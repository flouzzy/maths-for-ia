## Exercice 5 : La formule de Poincaré (Principe d'inclusion-exclusion)
$\bigstar\bigstar\bigstar\star\star$

### Énoncé

1. Démontrer, à partir des axiomes de Kolmogorov, la formule de l'union pour $3$ événements $A, B, C$ :
$$ \mathbb{P}(A \cup B \cup C) = \mathbb{P}(A) + \mathbb{P}(B) + \mathbb{P}(C) - \mathbb{P}(A \cap B) - \mathbb{P}(A \cap C) - \mathbb{P}(B \cap C) + \mathbb{P}(A \cap B \cap C) $$
2. Application : On tire une carte dans un jeu de 52 cartes. Quelle est la probabilité que ce soit un As, un Cœur, ou une Figure (Valet, Dame, Roi) ?


### Correction Détaillée

1. **Démonstration de la formule pour 3 événements :**
Posons $D = B \cup C$.
L'événement $A \cup B \cup C$ peut s'écrire $A \cup D$.
Par la formule de l'union pour deux événements, on a :
$\mathbb{P}(A \cup D) = \mathbb{P}(A) + \mathbb{P}(D) - \mathbb{P}(A \cap D)$

Exprimons $\mathbb{P}(D)$ avec la formule de l'union :
$\mathbb{P}(D) = \mathbb{P}(B \cup C) = \mathbb{P}(B) + \mathbb{P}(C) - \mathbb{P}(B \cap C)$.

Exprimons le terme d'intersection $\mathbb{P}(A \cap D)$ :
L'événement $A \cap D = A \cap (B \cup C)$. Par distributivité de l'intersection sur l'union, ceci équivaut à $(A \cap B) \cup (A \cap C)$.
Appliquons la formule de l'union pour deux événements sur cette union :
$\mathbb{P}(A \cap D) = \mathbb{P}((A \cap B) \cup (A \cap C)) = \mathbb{P}(A \cap B) + \mathbb{P}(A \cap C) - \mathbb{P}((A \cap B) \cap (A \cap C))$.
L'intersection de $(A \cap B)$ et $(A \cap C)$ est simplement $A \cap B \cap C$.
Donc :
$\mathbb{P}(A \cap D) = \mathbb{P}(A \cap B) + \mathbb{P}(A \cap C) - \mathbb{P}(A \cap B \cap C)$.

Substituons les deux expressions obtenues dans l'équation initiale :
$\mathbb{P}(A \cup B \cup C) = \mathbb{P}(A) + \left[ \mathbb{P}(B) + \mathbb{P}(C) - \mathbb{P}(B \cap C) \right] - \left[ \mathbb{P}(A \cap B) + \mathbb{P}(A \cap C) - \mathbb{P}(A \cap B \cap C) \right]$.
En développant le signe moins, on trouve exactement :
$\mathbb{P}(A \cup B \cup C) = \mathbb{P}(A) + \mathbb{P}(B) + \mathbb{P}(C) - \mathbb{P}(A \cap B) - \mathbb{P}(A \cap C) - \mathbb{P}(B \cap C) + \mathbb{P}(A \cap B \cap C)$.

2. **Application au tirage de cartes :**
Soit $\Omega$ l'ensemble des 52 cartes. $\text{Card}(\Omega) = 52$. On utilise la probabilité uniforme.
$A$ = "Tirer un As". $\mathbb{P}(A) = \frac{4}{52}$.
$B$ = "Tirer un Cœur". $\mathbb{P}(B) = \frac{13}{52}$.
$C$ = "Tirer une Figure". $\mathbb{P}(C) = \frac{12}{52}$ (3 figures $\times$ 4 couleurs).

Calculons les intersections 2 à 2 :
$A \cap B$ = "As de Cœur". $\mathbb{P}(A \cap B) = \frac{1}{52}$.
$A \cap C$ = "Tirer un As ET une Figure". Impossible, donc $\mathbb{P}(A \cap C) = 0$.
$B \cap C$ = "Tirer une Figure de Cœur" (Valet, Dame, Roi de Cœur). $\mathbb{P}(B \cap C) = \frac{3}{52}$.

Calculons l'intersection 3 à 3 :
$A \cap B \cap C$ = "Tirer un As de Cœur qui soit une Figure". C'est impossible, donc $\mathbb{P}(A \cap B \cap C) = 0$.

Appliquons la formule :
$\mathbb{P}(A \cup B \cup C) = \frac{4}{52} + \frac{13}{52} + \frac{12}{52} - \frac{1}{52} - 0 - \frac{3}{52} + 0 = \frac{25}{52}$.
La probabilité est de $25 / 52$.
