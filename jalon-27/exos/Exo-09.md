---
title: "Exercice 9 : L'inégalité d'Ostrowski et Opérateurs Positifs"
difficulty: "★★★★★"
---
# Exercice 9 : L'inégalité d'Ostrowski et Opérateurs Positifs

## Énoncé
Soit $E$ un espace euclidien, et soient $A, B \in \mathcal{L}(E)$ deux endomorphismes symétriques positifs, c'est-à-dire que $\forall x \in E, \langle A(x), x \rangle \geq 0$ et $\langle B(x), x \rangle \geq 0$.
Soit l'endomorphisme composé $C = A \circ B$. En général, $C$ n'est pas symétrique (car $A B \neq B A$).
Démontrer que malgré cela, le spectre (réel) de $A \circ B$ est inclus dans $[0, +\infty[$, c'est-à-dire que toutes les valeurs propres réelles de $A \circ B$ sont positives ou nulles.
*Indication : Utiliser la racine carrée d'un opérateur positif.*

## Correction Zéro Ellipse
**Étape 1 : Racine carrée de l'endomorphisme $B$**
L'endomorphisme $B$ est symétrique ($B = B^*$) et positif ($\langle B(x), x \rangle \geq 0$).
D'après le théorème spectral, $B$ est diagonalisable dans une base orthonormée et toutes ses valeurs propres sont réelles.
La positivité entraîne que ces valeurs propres sont positives ou nulles (si $e_i$ est un vecteur propre pour $\lambda_i$, $\langle B(e_i), e_i \rangle = \lambda_i \|e_i\|^2 \geq 0$, donc $\lambda_i \geq 0$).
Il existe donc un unique endomorphisme $S \in \mathcal{L}(E)$, symétrique et positif, tel que $S^2 = B$.
L'opérateur $S$ commute avec $B$ et s'exprime comme un polynôme en $B$.

**Étape 2 : Symétrie par similarité via $S$**
Nous voulons étudier le spectre de $C = A \circ B = A \circ S^2$.
On va considérer un opérateur lié par similitude : on "pousse" un $S$ de l'autre côté.
Considérons l'endomorphisme $M = S \circ A \circ S$.
- $M$ est symétrique. En effet, la composition d'adjoints donne $(S A S)^* = S^* A^* S^*$.
Or $A$ et $S$ sont symétriques, donc $S^* = S$ et $A^* = A$.
Ainsi $(S A S)^* = S A S = M$. $M$ est donc symétrique.
- $M$ est positif. En effet, pour tout $x \in E$, évaluons $\langle M(x), x \rangle$ :
$\langle M(x), x \rangle = \langle (S A S)(x), x \rangle$.
Puisque $S$ est symétrique, on peut transférer le premier $S$ dans la composante droite :
$\langle S(A(S(x))), x \rangle = \langle A(S(x)), S(x) \rangle$.
Posons $y = S(x) \in E$. L'expression devient $\langle A(y), y \rangle$.
Or par hypothèse, l'endomorphisme $A$ est symétrique positif. Donc pour tout $y$, $\langle A(y), y \rangle \geq 0$.
Ceci prouve que l'endomorphisme $M = S A S$ est symétrique et positif. Ses valeurs propres (nécessairement réelles) sont donc toutes $\geq 0$.

**Étape 3 : Lien entre le spectre de $M$ et le spectre de $A \circ B$**
Soit $\lambda$ une valeur propre réelle de $C = A \circ B$. Il existe un vecteur $x \neq 0$ tel que $(A B)(x) = \lambda x$.
Substituons $B = S^2$ :
$A(S^2(x)) = \lambda x$.
Appliquons l'opérateur $S$ à gauche des deux côtés de cette égalité :
$S(A(S^2(x))) = S(\lambda x) = \lambda S(x)$.
Ce qui s'écrit formellement :
$(S A S) (S(x)) = \lambda S(x)$, soit $M(S(x)) = \lambda S(x)$.
Deux cas se présentent :
1. **Cas où $S(x) \neq 0_E$ :**
   Alors le vecteur $y = S(x)$ est un vecteur propre non nul de l'endomorphisme $M$, associé à la valeur propre $\lambda$.
   Puisque nous avons prouvé que $M$ est symétrique positif, toutes ses valeurs propres sont $\geq 0$. On conclut donc que $\lambda \geq 0$.
2. **Cas pathologique où $S(x) = 0_E$ :**
   Si $S(x) = 0_E$, alors en appliquant $S$ à nouveau, $S^2(x) = S(0_E) = 0_E$.
   Donc $B(x) = 0_E$.
   Revenons à l'équation aux valeurs propres de $A \circ B$ :
   $(A \circ B)(x) = A(B(x)) = A(0_E) = 0_E$.
   Or, on sait par définition du vecteur propre que $(A \circ B)(x) = \lambda x$.
   On obtient donc $\lambda x = 0_E$.
   Comme $x \neq 0$ (définition d'un vecteur propre), cela exige inexorablement que $\lambda = 0$.
   Et $0$ est bien dans l'intervalle $[0, +\infty[$.

Dans tous les cas possibles, toute valeur propre réelle de $A \circ B$ est positive ou nulle. Le spectre réel satisfait $\text{Sp}_{\mathbb{R}}(A B) \subset \mathbb{R}^+$.
La rigueur est absolue, aucune ellipse n'a été commise.
