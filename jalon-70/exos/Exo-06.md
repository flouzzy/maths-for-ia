# Exercice 6 : L'indépendance de deux variables aléatoires via la mesure produit (★★★★☆)

**Énoncé :**
Soit $(\Omega, \mathcal{A}, \mathbb{P})$ un espace probabilisé. Soient $X : \Omega \to \mathbb{R}$ et $Y : \Omega \to \mathbb{R}$ deux variables aléatoires (c'est-à-dire des fonctions mesurables).
On note $\mathbb{P}_X$ et $\mathbb{P}_Y$ leurs lois respectives sur $\mathbb{R}$. La loi jointe est la mesure $\mathbb{P}_{(X,Y)}$ sur $\mathbb{R}^2$ définie par $\mathbb{P}_{(X,Y)}(C) = \mathbb{P}(\{\omega \in \Omega \mid (X(\omega), Y(\omega)) \in C\})$.
Montrer que si la loi jointe est égale à la mesure produit, soit $\mathbb{P}_{(X,Y)} = \mathbb{P}_X \otimes \mathbb{P}_Y$, alors pour tous boréliens $A, B \in \mathcal{B}(\mathbb{R})$, les événements $\{X \in A\}$ et $\{Y \in B\}$ sont indépendants.

**Correction :**
1. L'objectif est de démontrer que $\mathbb{P}(\{X \in A\} \cap \{Y \in B\}) = \mathbb{P}(X \in A) \mathbb{P}(Y \in B)$.
2. Considérons le sous-ensemble de $\mathbb{R}^2$ défini par le rectangle borélien $C = A \times B$.
3. Par définition de la loi jointe :
   $\mathbb{P}_{(X,Y)}(A \times B) = \mathbb{P}(\{\omega \in \Omega \mid (X(\omega), Y(\omega)) \in A \times B\})$.
   Or $(X(\omega), Y(\omega)) \in A \times B$ est logiquement équivalent à $(X(\omega) \in A) \text{ et } (Y(\omega) \in B)$.
   L'ensemble des $\omega$ réalisant cela est exactement l'intersection $\{\omega \in \Omega \mid X(\omega) \in A\} \cap \{\omega \in \Omega \mid Y(\omega) \in B\}$, ce qu'on note plus simplement $\{X \in A\} \cap \{Y \in B\}$.
   Donc $\mathbb{P}_{(X,Y)}(A \times B) = \mathbb{P}(\{X \in A\} \cap \{Y \in B\})$.
4. D'autre part, par hypothèse, la loi jointe est la mesure produit : $\mathbb{P}_{(X,Y)} = \mathbb{P}_X \otimes \mathbb{P}_Y$.
   Par définition de la mesure produit évaluée sur un rectangle mesurable, on a :
   $(\mathbb{P}_X \otimes \mathbb{P}_Y)(A \times B) = \mathbb{P}_X(A) \cdot \mathbb{P}_Y(B)$.
5. Or, par définition des lois marginales, $\mathbb{P}_X(A) = \mathbb{P}(X \in A)$ et $\mathbb{P}_Y(B) = \mathbb{P}(Y \in B)$.
6. En combinant (3), (4) et (5), on obtient exactement :
   $\mathbb{P}(\{X \in A\} \cap \{Y \in B\}) = \mathbb{P}(X \in A) \cdot \mathbb{P}(Y \in B)$.
   Cela démontre bien l'indépendance des événements. L'indépendance de variables aléatoires s'exprime profondément comme la factorisation de leur mesure conjointe en une mesure produit tensoriel.
