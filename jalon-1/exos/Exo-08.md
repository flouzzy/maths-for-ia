# Exercice 8 : Théorème d'interpolation de Craig

## Énoncé
Le **théorème d'interpolation de Craig** est un résultat fondamental de la logique mathématique. Dans le cadre de la logique propositionnelle, il s'énonce ainsi :
> Soient $A$ et $B$ deux formules telles que $A \Rightarrow B$ est une tautologie ($\models A \Rightarrow B$).
> Si $A$ et $B$ partagent au moins une variable propositionnelle commune, alors il existe une formule $I$, appelée **interpolant de Craig**, telle que :
> 1. $\models A \Rightarrow I$
> 2. $\models I \Rightarrow B$
> 3. Toutes les variables propositionnelles apparaissant dans $I$ apparaissent à la fois dans $A$ et dans $B$.

Considérons les deux formules propositionnelles suivantes :
- $A = P \land (\neg Q \lor R)$
- $B = (P \land S) \lor (P \land \neg S \lor T)$

1. Démontrer que $\models A \Rightarrow B$ en effectuant une simplification sémantique de $A$ et $B$.
2. Déterminer l'ensemble $\mathcal{V}_A$ des variables de $A$, l'ensemble $\mathcal{V}_B$ des variables de $B$, et leur intersection $\mathcal{V}_C = \mathcal{V}_A \cap \mathcal{V}_B$.
3. Proposer un interpolant de Craig $I$ pour ce couple de formules et prouver qu'il satisfait aux trois conditions du théorème.

---

## Correction Détaillée

### Question 1 : Preuve de la tautologie $\models A \Rightarrow B$
Commençons par simplifier et analyser les conditions sous lesquelles les deux formules sont vraies.

- **Analyse de $A$ :**
  $$A = P \land (\neg Q \lor R)$$
  Pour que $v(A) = 1$, il faut et il suffit que :
  - $v(P) = 1$
  - et $v(\neg Q \lor R) = 1$.
  En particulier, toute valuation satisfaisant $A$ doit nécessairement affecter la valeur $1$ à la variable $P$.

- **Analyse de $B$ :**
  $$B = (P \land S) \lor (P \land \neg S \lor T)$$
  Grâce à la commutativité et l'associativité de la disjonction, réécrivons $B$ :
  $$B \equiv (P \land S) \lor (P \land \neg S) \lor T$$
  Appliquons la distributivité de la conjonction par rapport à la disjonction sur les deux premiers termes :
  $$(P \land S) \lor (P \land \neg S) \equiv P \land (S \lor \neg S)$$
  Puisque $S \lor \neg S \equiv 1$, nous avons :
  $$P \land 1 \equiv P$$
  Substituons cela dans l'expression de $B$ :
  $$B \equiv P \lor T$$

- **Analyse de l'implication $A \Rightarrow B$ :**
  Remplaçons $B$ par sa forme simplifiée $P \lor T$ :
  $$A \Rightarrow B \equiv \big( P \land (\neg Q \lor R) \big) \Rightarrow (P \lor T)$$
  Soit $v$ une valuation telle que $v(A) = 1$. D'après l'analyse de $A$, cela implique $v(P) = 1$.
  Si $v(P) = 1$, alors la disjonction $P \lor T$ est vraie :
  $$v(P \lor T) = \max(v(P), v(T)) = \max(1, v(T)) = 1 \implies v(B) = 1$$
  Ainsi, toute valuation qui rend $A$ vraie rend également $B$ vraie.
  Par conséquent, $A \Rightarrow B$ est une tautologie, notée $\models A \Rightarrow B$.

---

### Question 2 : Intersection des variables propositionnelles
Listons les variables propositionnelles contenues dans chaque formule :
- Pour $A = P \land (\neg Q \lor R)$, l'ensemble des variables est :
  $$\mathcal{V}_A = \{P, Q, R\}$$
- Pour $B = (P \land S) \lor (P \land \neg S \lor T)$, l'ensemble des variables est :
  $$\mathcal{V}_B = \{P, S, T\}$$
- L'intersection des ensembles de variables est :
  $$\mathcal{V}_C = \mathcal{V}_A \cap \mathcal{V}_B = \{P\}$$

L'unique variable commune aux deux formules est donc $P$. L'interpolant de Craig $I$ ne pourra contenir que la seule variable propositionnelle $P$ (ou être une constante logique $0$ ou $1$).

---

### Question 3 : Détermination et validation de l'interpolant $I$
Puisque le seul atome autorisé dans $I$ est $P$, les seuls choix possibles pour $I$ (à équivalence logique près) sont $P$, $\neg P$, $0$ ou $1$.

- Testons la formule **$I = P$** :
  1. **Condition 3 :** Les variables de $I$ sont incluses dans $\mathcal{V}_C$. C'est le cas puisque $\text{Var}(I) = \{P\} \subseteq \{P\}$.
  2. **Condition 1 ($\models A \Rightarrow I$) :**
     $$A \Rightarrow I \equiv \big( P \land (\neg Q \lor R) \big) \Rightarrow P$$
     Soit $v$ une valuation. Si $v(A) = 1$, alors $v(P) = 1$, donc $v(I) = 1$.
     L'implication est donc toujours vraie. C'est une tautologie.
  3. **Condition 2 ($\models I \Rightarrow B$) :**
     $$I \Rightarrow B \equiv P \Rightarrow (P \lor T)$$
     Soit $v$ une valuation. Si $v(I) = 1$, alors $v(P) = 1$, ce qui implique $v(P \lor T) = 1$, d'où $v(B) = 1$.
     L'implication est donc toujours vraie. C'est une tautologie.

L'ensemble des trois conditions du théorème d'interpolation de Craig est satisfait par la formule :
$$I = P$$

*Remarque constructive :* Pour construire l'interpolant sémantiquement dans le cas général pour une variable commune $C$, on peut écrire $I = A[C/1] \lor A[C/0]$ ou $I = A[C/1] \land A[C/0]$ selon le sens de l'implication.
