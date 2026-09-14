## Exercice 2 : Produit de mesures discrètes \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soient $X_1 = X_2 = \mathbb{N}$ munis de la tribu $\mathcal{P}(\mathbb{N})$ et de la mesure de comptage $c$.
Montrer que $c \otimes c$ est la mesure de comptage sur $\mathbb{N}^2$. Calculer la mesure du sous-ensemble $D = \{ (n, n) \mid n \in \{1, 2, 3\} \}$.

**Correction :**
1. Tout sous-ensemble de $\mathbb{N}^2$ peut s'écrire comme une union au plus dénombrable de singletons.
2. Pour un singleton $E = \{(a, b)\} = \{a\} \times \{b\}$, qui est un rectangle mesurable, on a :
   $(c \otimes c)(E) = c(\{a\}) \cdot c(\{b\}) = 1 \cdot 1 = 1$.
3. La mesure $c \otimes c$ attribue un poids de 1 à chaque point de $\mathbb{N}^2$, c'est donc bien la mesure de comptage sur cet espace.
4. L'ensemble $D = \{(1,1), (2,2), (3,3)\}$ est l'union disjointe de 3 singletons.
5. $(c \otimes c)(D) = 1 + 1 + 1 = 3$.
