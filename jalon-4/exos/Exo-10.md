# Exercice 10 : Caractérisation de la Surjectivité d'une Fonction par l'Application de Préimage sur l'Ensemble des Parties
**Difficulté :** ⭐⭐⭐⭐⭐
**Thème :** Application de préimage, injectivité, surjectivité, ensemble des parties, ZFC.

## Énoncé
Soient $E$ un ensemble et $F$ un ensemble. On considère une fonction $f: E \to F$.
On définit l'application de préimage $f^*: \mathcal{P}(F) \to \mathcal{P}(E)$ par :
Pour tout $B \in \mathcal{P}(F)$, $f^*(B) = \{x \in E \mid f(x) \in B\}$.

Démontrez l'équivalence suivante :
La fonction $f$ est surjective si et seulement si l'application $f^*$ est injective.

## Correction Détaillée

### Précisions et Hypothèses Fondamentales
*   $E$ et $F$ sont des ensembles. Nous travaillerons dans le cadre de la théorie des ensembles de Zermelo-Fraenkel avec l'Axiome du Choix (ZFC).
*   La définition d'une fonction $f: E \to F$ implique que pour tout $x \in E$, il existe un unique $y \in F$ tel que $f(x)=y$.
*   $\mathcal{P}(X)$ désigne l'ensemble des parties de $X$, défini par $\mathcal{P}(X) = \{A \mid A \subseteq X\}$. L'existence de $\mathcal{P}(X)$ est garantie par l'axiome de l'ensemble des parties de ZFC.
*   Nous supposons que l'ensemble $F$ est non vide. Si $F$ est l'ensemble vide ($\emptyset$), alors :
    *   La fonction $f: E \to \emptyset$ ne peut exister que si $E$ est vide (par l'axiome de la fonctionnalité). Si $E = \emptyset$ et $F = \emptyset$, alors $f$ est surjective par vacuité.
    *   $\mathcal{P}(F) = \mathcal{P}(\emptyset) = \{\emptyset\}$. L'application $f^*: \{\emptyset\} \to \mathcal{P}(\emptyset)$ est définie par $f^*(\emptyset) = \{x \in \emptyset \mid f(x) \in \emptyset\} = \emptyset$. Dans ce cas, $f^*$ est triviale et injective (par vacuité). L'équivalence tient donc dans ce cas trivial.
    Afin d'éviter les arguments par vacuité qui simplifieraient artificiellement certaines étapes, nous allons traiter le cas général où $F$ est un ensemble non vide. Le cas des ensembles finis, comme mentionné dans le thème, est un cas particulier de cette preuve générale.

### Partie 1 : Démonstration de "$f$ est surjective $\implies$ $f^*$ est injective"

**Hypothèse :** La fonction $f: E \to F$ est surjective.
Par définition de la surjectivité, cela signifie que pour tout élément $y \in F$, il existe au moins un élément $x \in E$ tel que $f(x)=y$.

**But :** Démontrer que l'application $f^*: \mathcal{P}(F) \to \mathcal{P}(E)$ est injective.
Par définition de l'injectivité d'une fonction, nous devons montrer que pour tous $B_1 \in \mathcal{P}(F)$ et $B_2 \in \mathcal{P}(F)$, si $f^*(B_1) = f^*(B_2)$, alors $B_1 = B_2$.

Soient $B_1$ un élément arbitraire de $\mathcal{P}(F)$ et $B_2$ un élément arbitraire de $\mathcal{P}(F)$.
Supposons que $f^*(B_1) = f^*(B_2)$.
Par la définition de l'application de préimage $f^*$, cette égalité signifie que :
$$ \{x \in E \mid f(x) \in B_1\} = \{x \in E \mid f(x) \in B_2\} \quad (*)$$.

Nous allons montrer que cette égalité d'ensembles de préimages implique que $B_1$ et $B_2$ sont égaux. Pour cela, nous devons prouver la double inclusion : $B_1 \subseteq B_2$ et $B_2 \subseteq B_1$.

**Démonstration de $B_1 \subseteq B_2$ :**
Soit $y$ un élément arbitraire de $F$ tel que $y \in B_1$.
Puisque $f$ est surjective (par hypothèse) et que $y \in F$, il existe un élément $x_0 \in E$ tel que $f(x_0)=y$.
Comme $f(x_0)=y$ et $y \in B_1$, nous avons $f(x_0) \in B_1$.
Par la définition de l'ensemble $f^*(B_1)$, l'appartenance $f(x_0) \in B_1$ implique que $x_0 \in f^*(B_1)$.
En utilisant l'égalité $(*)$ que nous avons supposée, nous avons $f^*(B_1) = f^*(B_2)$.
Par conséquent, $x_0 \in f^*(B_2)$.
Par la définition de l'ensemble $f^*(B_2)$, l'appartenance $x_0 \in f^*(B_2)$ implique que $f(x_0) \in B_2$.
Or, nous avons établi que $f(x_0)=y$. Donc, $y \in B_2$.
Puisque $y$ était un élément arbitraire de $B_1$, nous avons montré que si $y \in B_1$, alors $y \in B_2$.
Par conséquent, $B_1 \subseteq B_2$.

**Démonstration de $B_2 \subseteq B_1$ :**
La démonstration est symétrique à la précédente.
Soit $y$ un élément arbitraire de $F$ tel que $y \in B_2$.
Puisque $f$ est surjective (par hypothèse) et que $y \in F$, il existe un élément $x_1 \in E$ tel que $f(x_1)=y$.
Comme $f(x_1)=y$ et $y \in B_2$, nous avons $f(x_1) \in B_2$.
Par la définition de l'ensemble $f^*(B_2)$, l'appartenance $f(x_1) \in B_2$ implique que $x_1 \in f^*(B_2)$.
En utilisant l'égalité $(*)$, nous avons $f^*(B_2) = f^*(B_1)$.
Par conséquent, $x_1 \in f^*(B_1)$.
Par la définition de l'ensemble $f^*(B_1)$, l'appartenance $x_1 \in f^*(B_1)$ implique que $f(x_1) \in B_1$.
Or, nous avons établi que $f(x_1)=y$. Donc, $y \in B_1$.
Puisque $y$ était un élément arbitraire de $B_2$, nous avons montré que si $y \in B_2$, alors $y \in B_1$.
Par conséquent, $B_2 \subseteq B_1$.

Puisque nous avons démontré que $B_1 \subseteq B_2$ et $B_2 \subseteq B_1$, nous concluons que $B_1 = B_2$.
Ayant montré que si $f^*(B_1) = f^*(B_2)$ alors $B_1 = B_2$, l'application $f^*$ est injective.

### Partie 2 : Démonstration de "$f^*$ est injective $\implies$ $f$ est surjective"

**Hypothèse :** L'application $f^*: \mathcal{P}(F) \to \mathcal{P}(E)$ est injective.
Par définition de l'injectivité, cela signifie que pour tous $B_1 \in \mathcal{P}(F)$ et $B_2 \in \mathcal{P}(F)$, si $f^*(B_1) = f^*(B_2)$, alors $B_1 = B_2$.

**But :** Démontrer que la fonction $f: E \to F$ est surjective.
Nous allons procéder par preuve par contradiction.

Supposons, par l'absurde, que la fonction $f$ n'est pas surjective.
Par définition de la non-surjectivité, cela signifie qu'il existe au moins un élément $y_0 \in F$ tel que pour tout $x \in E$, l'image $f(x)$ est différente de $y_0$. En d'autres termes, $y_0$ n'appartient pas à l'image de $f$, c'est-à-dire $y_0 \notin \text{Im}(f)$.
Rappelons que nous avons supposé $F$ non vide, donc l'existence d'un tel $y_0$ est possible sans rendre $F$ vide.

Considérons les deux sous-ensembles de $F$ suivants :
1.  $B_1 = \{y_0\}$. Par l'axiome de l'ensemble des parties et l'axiome de la paire de ZFC, $B_1$ est un élément de $\mathcal{P}(F)$.
2.  $B_2 = \emptyset$. Par l'axiome de l'ensemble vide, $\emptyset$ existe, et par l'axiome de l'ensemble des parties, $\emptyset$ est un élément de $\mathcal{P}(F)$.

Maintenant, calculons les préimages de ces ensembles sous l'application $f^*$:

Pour $B_1 = \{y_0\}$ :
La définition de $f^*(B_1)$ est $\{x \in E \mid f(x) \in \{y_0\}\}$.
Cette expression est équivalente à $\{x \in E \mid f(x) = y_0\}$.
Puisque nous avons supposé que $f$ n'est pas surjective et que $y_0$ est précisément l'élément de $F$ pour lequel il n'existe aucun $x \in E$ tel que $f(x)=y_0$, l'ensemble $\{x \in E \mid f(x) = y_0\}$ ne contient aucun élément.
Par conséquent, $f^*(B_1) = \emptyset$.

Pour $B_2 = \emptyset$ :
La définition de $f^*(B_2)$ est $\{x \in E \mid f(x) \in \emptyset\}$.
Puisque l'ensemble vide ne contient aucun élément, il n'existe aucun $y$ tel que $y \in \emptyset$. Par conséquent, il n'existe aucun $f(x)$ tel que $f(x) \in \emptyset$.
L'ensemble $\{x \in E \mid f(x) \in \emptyset\}$ ne contient donc aucun élément.
Ainsi, $f^*(B_2) = \emptyset$.

Nous avons donc trouvé deux éléments $B_1 = \{y_0\}$ et $B_2 = \emptyset$ de $\mathcal{P}(F)$ tels que $f^*(B_1) = \emptyset$ et $f^*(B_2) = \emptyset$.
Il s'ensuit que $f^*(B_1) = f^*(B_2)$.

Cependant, nous savons que $y_0 \in F$ est l'élément qui n'appartient pas à l'image de $f$. Par l'axiome de la paire de ZFC, $\{y_0\}$ est un ensemble contenant $y_0$.
L'ensemble $B_1 = \{y_0\}$ contient l'élément $y_0$.
L'ensemble $B_2 = \emptyset$ ne contient aucun élément.
Puisque $y_0 \in B_1$ et $y_0 \notin B_2$, il s'ensuit que $B_1 \neq B_2$.

Nous avons donc abouti à la situation suivante : $f^*(B_1) = f^*(B_2)$ mais $B_1 \neq B_2$.
Cette conclusion contredit directement notre hypothèse selon laquelle l'application $f^*$ est injective.
Par conséquent, notre hypothèse initiale selon laquelle $f$ n'est pas surjective doit être fausse.
Il s'ensuit que la fonction $f$ est surjective.

### Conclusion
Ayant démontré que $f$ est surjective $\implies$ $f^*$ est injective (Partie 1) et que $f^*$ est injective $\implies$ $f$ est surjective (Partie 2), nous avons prouvé l'équivalence :
La fonction $f: E \to F$ est surjective si et seulement si l'application de préimage $f^*: \mathcal{P}(F) \to \mathcal{P}(E)$ est injective.
Cette preuve est valide pour des ensembles $E$ et $F$ quelconques (finis ou infinis), à condition que $F$ soit non vide. Le cas des ensembles finis est une restriction de ce résultat général.
