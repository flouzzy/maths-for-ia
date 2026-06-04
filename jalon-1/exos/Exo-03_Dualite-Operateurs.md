# Exercice 3 : Dualité des connecteurs et foncteurs de vérité

## Énoncé
On restreint dans cet exercice notre langage de formules à l'ensemble des formules positives construites exclusivement à partir des variables de $\mathcal{P}$, des connecteurs de conjonction $\land$, de disjonction $\lor$ et de négation $\neg$.

Soit $F$ une formule. On définit sa **formule duale**, notée $F^*$, par récurrence structurelle sur la complexité de $F$ comme suit :
1. Si $F = p$ (avec $p \in \mathcal{P}$), alors $F^* = p$.
2. Si $F = \neg A$, alors $F^* = \neg (A^*)$.
3. Si $F = A \land B$, alors $F^* = A^* \lor B^*$.
4. Si $F = A \lor B$, alors $F^* = A^* \land B^*$.

Pour toute valuation $v \in \{0, 1\}^\mathcal{P}$, on définit la valuation conjuguée $\bar{v}$ par $\bar{v}(p) = 1 - v(p)$ pour tout $p \in \mathcal{P}$.

1. Démontrer par induction structurelle sur la formule $F$ le théorème de dualité sémantique suivant :
   $$\text{Pour toute valuation } v, \quad v(F^*) = 1 - \bar{v}(F)$$
2. En déduire que $F$ est une tautologie si et seulement si la formule $\neg (F^*[\neg p_1/p_1, \dots, \neg p_n/p_n])$ en est une, où la notation $G[\neg p/p]$ représente la substitution uniforme de la variable $p$ par son opposée $\neg p$.
3. Déterminer et simplifier la duale de la formule :
   $$G = (P \land Q) \lor R$$

---

## Correction Détaillée

### Question 1 : Preuve du théorème de dualité sémantique
Nous allons procéder par induction structurelle sur la formule $F$.
Soit la propriété $\mathcal{H}(F)$ : « Pour toute valuation $v$, $v(F^*) = 1 - \bar{v}(F)$ ».

#### Étape de base (formules atomiques) :
Soit $F = p$ avec $p \in \mathcal{P}$.
- D'après la règle 1 de définition du dual, $F^* = p$. Donc $v(F^*) = v(p)$.
- Évaluons le membre droit :
  $$1 - \bar{v}(F) = 1 - \bar{v}(p)$$
  Par définition de la valuation conjuguée, $\bar{v}(p) = 1 - v(p)$.
  D'où :
  $$1 - \bar{v}(F) = 1 - (1 - v(p)) = v(p)$$
Les deux membres coïncident. L'étape de base est vérifiée.

#### Étape d'induction :
Supposons que $\mathcal{H}(A)$ et $\mathcal{H}(B)$ sont vraies pour deux formules $A$ et $B$.

- **Sous-cas 1 : $F = \neg A$**
  D'après la définition du dual, $F^* = \neg(A^*)$.
  - Évaluons $v(F^*)$ :
    $$v(F^*) = v(\neg (A^*)) = 1 - v(A^*)$$
    Par hypothèse de récurrence sémantique sur $A$, nous avons $v(A^*) = 1 - \bar{v}(A)$.
    D'où :
    $$v(F^*) = 1 - (1 - \bar{v}(A)) = \bar{v}(A)$$
  - Évaluons le membre droit $1 - \bar{v}(F)$ :
    $$1 - \bar{v}(\neg A) = 1 - (1 - \bar{v}(A)) = \bar{v}(A)$$
  Les deux valeurs coïncident. $\mathcal{H}(\neg A)$ est vraie.

- **Sous-cas 2 : $F = A \land B$**
  D'après la définition, $F^* = A^* \lor B^*$.
  - Évaluons $v(F^*)$ :
    $$v(F^*) = v(A^* \lor B^*) = \max(v(A^*), v(B^*))$$
    En utilisant l'hypothèse de récurrence sémantique sur $A$ et $B$ :
    $$v(F^*) = \max(1 - \bar{v}(A), 1 - \bar{v}(B))$$
    Puisque pour tous réels $a$ et $b$, $\max(1-a, 1-b) = 1 - \min(a, b)$, on a :
    $$v(F^*) = 1 - \min(\bar{v}(A), \bar{v}(B))$$
    Par définition sémantique de la conjonction, $\min(\bar{v}(A), \bar{v}(B)) = \bar{v}(A \land B) = \bar{v}(F)$.
    D'où :
    $$v(F^*) = 1 - \bar{v}(F)$$
  Les deux valeurs coïncident. $\mathcal{H}(A \land B)$ est vraie.

- **Sous-cas 3 : $F = A \lor B$**
  D'après la définition, $F^* = A^* \land B^*$.
  - Évaluons $v(F^*)$ :
    $$v(F^*) = v(A^* \land B^*) = \min(v(A^*), v(B^*))$$
    En utilisant l'hypothèse de récurrence :
    $$v(F^*) = \min(1 - \bar{v}(A), 1 - \bar{v}(B))$$
    Puisque $\min(1-a, 1-b) = 1 - \max(a, b)$, on a :
    $$v(F^*) = 1 - \max(\bar{v}(A), \bar{v}(B)) = 1 - \bar{v}(A \lor B) = 1 - \bar{v}(F)$$
  Les deux valeurs coïncident. $\mathcal{H}(A \lor B)$ est vraie.

#### Conclusion de l'induction :
La propriété $\mathcal{H}(F)$ est héréditaire pour tous les constructeurs du langage. Elle est donc vraie pour toute formule $F \in \mathcal{F}$.

---

### Question 2 : Équivalence de validité
Soit $F$ une formule contenant les variables $p_1, \dots, p_n$.
Le résultat de la question 1 montre que la table de vérité de $F^*$ s'obtient en prenant le complément de la table de vérité de $F$ évaluée sur les lignes conjuguées.
Si l'on substitue uniformément chaque variable $p_i$ par sa négation dans $F^*$, on compense le passage à la valuation conjuguée $\bar{v}$.
Ainsi, en posant $H = \neg (F^*[\neg p_1/p_1, \dots, \neg p_n/p_n])$, nous avons pour toute valuation $v$ :
$$v(H) = 1 - v(F^*[\neg p_1/p_1, \dots, \neg p_n/p_n]) = 1 - (1 - v(F)) = v(F)$$
Puisque $v(H) = v(F)$ pour toute valuation $v$, la formule $H$ est sémantiquement équivalente à $F$.
Par conséquent, $F$ est une tautologie si et seulement si $H$ est une tautologie.

---

### Question 3 : Duale de la formule $G = (P \land Q) \lor R$
Appliquons pas-à-pas les règles de construction récursive du dual :
1. Repérons le connecteur principal de $G$. Il s'agit d'une disjonction $\lor$ entre la sous-formule $A = P \land Q$ et $B = R$.
2. Par la règle 4 :
   $$G^* = (P \land Q)^* \land R^*$$
3. Déterminons $(P \land Q)^*$ par la règle 3 :
   $$(P \land Q)^* = P^* \lor Q^*$$
4. D'après la règle 1 pour les atomes :
   $$P^* = P, \quad Q^* = Q, \quad R^* = R$$
5. Réassemblons le tout :
   $$G^* = (P \lor Q) \land R$$

La duale de $(P \land Q) \lor R$ est donc $(P \lor Q) \land R$.
On remarque que la conjonction et la disjonction ont été permutées.
