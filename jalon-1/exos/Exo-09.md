# Exercice 9 : Isomorphisme de Stone pour les algèbres de Boole finies

## Énoncé
Soit $(B, \lor, \land, \neg, 0, 1)$ une **algèbre de Boole finie** (c'est-à-dire que le cardinal de l'ensemble $B$ est fini).
On munit $B$ de sa relation d'ordre canonique $\le$ définie par :
$$\forall x, y \in B, \quad x \le y \iff x \land y = x \iff x \lor y = y$$

On définit un **atom** de $B$ comme un élément $a \in B$ tel que $a \neq 0$ et pour tout $x \in B$ :
$$\text{si } x \le a, \quad \text{alors } x = 0 \text{ ou } x = a$$
On note $\mathcal{A}t(B)$ l'ensemble de tous les atomes de $B$.

Considérons l'application suivante, notée $\Phi$ :
$$\Phi : \begin{cases} B \to \mathcal{P}(\mathcal{A}t(B)) \\ x \mapsto \{a \in \mathcal{A}t(B) \mid a \le x\} \end{cases}$$

Le but de cet exercice est de démontrer le **théorème de représentation de Stone** dans le cas fini, à savoir que $\Phi$ est un isomorphisme d'algèbres de Boole, prouvant que toute algèbre de Boole finie est isomorphe à l'algèbre des parties d'un ensemble.

1. Soit $x \in B$. Démontrer que si $x \neq 0$, alors il existe au moins un atome $a \in \mathcal{A}t(B)$ tel que $a \le x$.
2. Démontrer que pour tout $x \in B$, $x = \bigvee_{a \in \Phi(x)} a$ (tout élément est le suprémum des atomes qu'il contient).
3. Démontrer que $\Phi$ est injective.
4. Démontrer que pour tous $x, y \in B$ :
   - $\Phi(x \land y) = \Phi(x) \cap \Phi(y)$
   - $\Phi(x \lor y) = \Phi(x) \cup \Phi(y)$
   - $\Phi(\neg x) = \mathcal{A}t(B) \setminus \Phi(x)$
5. Conclure sur la nature de $\Phi$ et en déduire le cardinal d'une algèbre de Boole finie.

---

## Correction Détaillée

### Question 1 : Existence d'un atome inférieur
Soit $x \in B$ tel que $x \neq 0$.
Considérons l'ensemble des éléments non nuls inférieurs ou égaux à $x$ :
$$E_x = \{y \in B \mid y \neq 0 \text{ et } y \le x\}$$
- Cet ensemble est non vide car $x \in E_x$ (puisque $x \neq 0$ et $x \le x$).
- Puisque l'ensemble $B$ est fini, l'ensemble $E_x$ est également fini.
- Tout ensemble ordonné fini et non vide possède au moins un élément minimal. Soit $a$ un élément minimal de $E_x$.

Montrons que $a$ est un atome de $B$ :
- Par définition de $E_x$, $a \neq 0$.
- Soit $z \in B$ tel que $z \le a$. Par transitivité de la relation d'ordre, puisque $a \le x$, on a $z \le x$.
- Si $z \neq 0$, alors $z \in E_x$. Comme $z \le a$ et que $a$ est minimal dans $E_x$, on a nécessairement $z = a$.
- Ainsi, pour tout $z \le a$, $z = 0$ ou $z = a$. L'élément $a$ est donc un atome de $B$.
Puisque $a \in E_x$, on a $a \le x$. Il existe donc un atome sous tout élément non nul.

---

### Question 2 : Tout élément est la borne supérieure de ses atomes
Soit $x \in B$. Définissons $x' = \bigvee_{a \in \Phi(x)} a$.
- Par définition de $\Phi(x)$, pour tout $a \in \Phi(x)$, nous avons $a \le x$. Par définition de la borne supérieure, nous en déduisons :
  $$x' \le x$$
- Montrons par l'absurde que $x = x'$. Supposons que $x \neq x'$.
  Alors, l'élément $d = x \land \neg x'$ est non nul (sinon $x \le x'$).
  Puisque $d \neq 0$, par le résultat de la question 1, il existe un atome $a_0 \in \mathcal{A}t(B)$ tel que $a_0 \le d$.
  - D'une part, $a_0 \le d \le x$, donc $a_0 \in \Phi(x)$. Par conséquent, $a_0 \le x'$ (par définition de $x'$).
  - D'autre part, $a_0 \le d \le \neg x'$, ce qui implique $a_0 \land x' \le \neg x' \land x' = 0$. Donc $a_0 \land x' = 0$.
  - Or, comme $a_0 \le x'$, nous avons $a_0 \land x' = a_0$.
  - Nous en déduisons $a_0 = 0$, ce qui contredit le fait que $a_0$ est un atome (donc non nul).
L'hypothèse $x \neq x'$ est donc absurde. On en conclut que $x = \bigvee_{a \in \Phi(x)} a$.

---

### Question 3 : Injectivité de $\Phi$
Soient $x, y \in B$ tels que $\Phi(x) = \Phi(y)$.
D'après le résultat de la question 2 :
$$x = \bigvee_{a \in \Phi(x)} a \quad \text{et} \quad y = \bigvee_{a \in \Phi(y)} a$$
Puisque $\Phi(x) = \Phi(y)$, les deux suprémums portent sur le même ensemble d'atomes, d'où :
$$x = y$$
L'application $\Phi$ est donc injective.

---

### Question 4 : Préservation des opérations logiques

1. **Intersection/Conjonction : $\Phi(x \land y) = \Phi(x) \cap \Phi(y)$**
   $$a \in \Phi(x \land y) \iff a \le x \land y \iff a \le x \text{ et } a \le y \iff a \in \Phi(x) \text{ et } a \in \Phi(y) \iff a \in \Phi(x) \cap \Phi(y)$$

2. **Union/Disjonction : $\Phi(x \lor y) = \Phi(x) \cup \Phi(y)$**
   - Si $a \in \Phi(x) \cup \Phi(y)$, alors $a \le x$ ou $a \le y$. Dans les deux cas, $a \le x \lor y$, donc $a \in \Phi(x \lor y)$. D'où $\Phi(x) \cup \Phi(y) \subseteq \Phi(x \lor y)$.
   - Réciproquement, soit $a \in \Phi(x \lor y)$, donc $a \le x \lor y$.
     Alors $a = a \land (x \lor y) = (a \land x) \lor (a \land y)$.
     Puisque $a$ est un atome, les éléments $a \land x$ et $a \land y$ sont soit $0$, soit $a$.
     Si les deux valaient $0$, on aurait $a = 0 \lor 0 = 0$, ce qui est exclu.
     Donc, au moins l'un des deux vaut $a$.
     Si $a \land x = a$, alors $a \le x \implies a \in \Phi(x)$. Si $a \land y = a$, alors $a \le y \implies a \in \Phi(y)$.
     Dans tous les cas, $a \in \Phi(x) \cup \Phi(y)$.
   D'où l'égalité $\Phi(x \lor y) = \Phi(x) \cup \Phi(y)$.

3. **Complément : $\Phi(\neg x) = \mathcal{A}t(B) \setminus \Phi(x)$**
   - Soit $a \in \Phi(\neg x)$, donc $a \le \neg x$.
     Si $a \in \Phi(x)$, on aurait également $a \le x$, donc $a \le x \land \neg x = 0 \implies a = 0$, absurde. Donc $a \notin \Phi(x)$.
   - Réciproquement, soit $a \in \mathcal{A}t(B) \setminus \Phi(x)$.
     Considérons $a \land x$. Puisque $a$ est un atome, $a \land x = 0$ ou $a \land x = a$.
     Comme $a \notin \Phi(x)$, la deuxième option est exclue, donc $a \land x = 0$.
     Alors $a = a \land 1 = a \land (x \lor \neg x) = (a \land x) \lor (a \land \neg x) = 0 \lor (a \land \neg x) = a \land \neg x$.
     D'où $a \le \neg x$, ce qui signifie $a \in \Phi(\neg x)$.
   L'égalité est établie.

---

### Question 5 : Conclusion et cardinalité
- L'application $\Phi$ est injective (Q3) et préserve la structure d'algèbre de Boole (Q4).
- De plus, pour tout sous-ensemble d'atomes $S \subseteq \mathcal{A}t(B)$, l'élément $x_S = \bigvee_{a \in S} a$ vérifie $\Phi(x_S) = S$. L'application $\Phi$ est donc surjective.
- Par conséquent, $\Phi$ est un **isomorphisme d'algèbres de Boole**.
- Toute algèbre de Boole finie $B$ est isomorphe à l'algèbre des parties $\mathcal{P}(\mathcal{A}t(B))$.
- Comme l'ensemble $\mathcal{A}t(B)$ est fini (soit $n$ son cardinal), le cardinal de $\mathcal{P}(\mathcal{A}t(B))$ est égal à $2^n$.

On en déduit le théorème fondamental : **Le cardinal de toute algèbre de Boole finie est une puissance de $2$**.
