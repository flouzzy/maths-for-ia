# Exercice 7 : Complétude du connecteur NOR (barre de Peirce)

## Énoncé
Le connecteur binaire $\downarrow$ (appelé connecteur NOR ou flèche de Peirce) est défini par la règle d'évaluation sémantique suivante :
$$\text{Pour toute valuation } v, \quad v(A \downarrow B) = 1 \iff v(A) = 0 \text{ et } v(B) = 0$$
Ce qui correspond sémantiquement à $\neg(A \lor B)$.

Démontrer que le singleton $\{\downarrow\}$ est un **système complet de connecteurs** (ou base fonctionnellement complète) en exprimant à l'aide de ce seul connecteur :
1. La négation $\neg A$.
2. La disjonction $A \lor B$.
3. La conjonction $A \land B$.

---

## Correction Détaillée

### Question 1 : Expression de la négation $\neg A$
Montrons que $\neg A \equiv A \downarrow A$.
Soit $v$ une valuation quelconque.
- D'après la définition du connecteur $\downarrow$ :
  $$v(A \downarrow A) = 1 \iff v(A) = 0 \text{ et } v(A) = 0 \iff v(A) = 0$$
- Ainsi, $v(A \downarrow A) = 1 - v(A) = v(\neg A)$.
Les deux expressions prennent les mêmes valeurs de vérité pour toutes les valuations possibles. Nous avons donc bien :
$$\neg A \equiv A \downarrow A$$

---

### Question 2 : Expression de la disjonction $A \lor B$
Par double négation, nous savons que $A \lor B \equiv \neg(\neg(A \lor B))$.
- Par définition du connecteur $\downarrow$, nous avons $\neg(A \lor B) \equiv A \downarrow B$.
- Par conséquent, la disjonction est la négation du connecteur $\downarrow$ :
  $$A \lor B \equiv \neg(A \downarrow B)$$
- En utilisant le résultat de la question 1 pour exprimer la négation d'une formule $X = (A \downarrow B)$, nous avons :
  $$\neg X \equiv X \downarrow X \implies \neg(A \downarrow B) \equiv (A \downarrow B) \downarrow (A \downarrow B)$$
Les deux expressions sont logiquement équivalentes :
$$A \lor B \equiv (A \downarrow B) \downarrow (A \downarrow B)$$

---

### Question 3 : Expression de la conjonction $A \land B$
Par les lois de De Morgan, nous savons que la conjonction peut s'écrire sous forme d'une négation sur des termes niés :
$$A \land B \equiv \neg(\neg A \lor \neg B)$$
- Par définition du connecteur $\downarrow$, la négation d'une disjonction s'écrit avec la flèche :
  $$\neg(X \lor Y) \equiv X \downarrow Y$$
- Posons $X = \neg A$ et $Y = \neg B$. L'expression devient :
  $$A \land B \equiv \neg A \downarrow \neg B$$
- Remplaçons désormais les négations internes $\neg A$ et $\neg B$ en utilisant le connecteur $\downarrow$ d'après la question 1 :
  $$\neg A \equiv A \downarrow A \quad \text{et} \quad \neg B \equiv B \downarrow B$$
- En substituant ces formes, nous obtenons :
  $$A \land B \equiv (A \downarrow A) \downarrow (B \downarrow B)$$

---

### Synthèse
Nous avons réussi à exprimer les trois connecteurs fondamentaux $\{\neg, \lor, \land\}$ uniquement à l'aide de la flèche de Peirce $\downarrow$ :
- $\neg A \equiv A \downarrow A$
- $A \lor B \equiv (A \downarrow B) \downarrow (A \downarrow B)$
- $A \land B \equiv (A \downarrow A) \downarrow (B \downarrow B)$

Puisque le système de connecteurs $\{\neg, \lor, \land\}$ est complet, le singleton $\{\downarrow\}$ est également un système complet de connecteurs.
