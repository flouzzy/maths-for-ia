# Exercice 5 : Conversion en forme normale conjonctive (CNF)

## Énoncé
Soient $P$, $Q$, $R$ et $S$ quatre variables propositionnelles.
On considère la formule propositionnelle suivante :
$$H = (P \Rightarrow Q) \Rightarrow (R \land \neg S)$$

Convertir la formule $H$ en **Forme Normale Conjonctive (CNF)** (conjonction de clauses disjonctives) en détaillant chaque étape de transformation algébrique.

---

## Correction Détaillée

Une formule est sous Forme Normale Conjonctive (CNF) si elle se présente sous la forme :
$$\bigwedge_{i=1}^n \left( \bigvee_{j=1}^{m_i} L_{i,j} \right)$$
où chaque $L_{i,j}$ est un littéral (une variable propositionnelle ou sa négation).

Pour transformer $H$ en CNF, nous appliquons un algorithme en trois grandes étapes :
1. Élimination des connecteurs d'implication ($\Rightarrow$).
2. Descente des négations ($\neg$) au niveau des variables (en utilisant les lois de De Morgan et de double négation).
3. Distribution des disjonctions ($\lor$) par rapport aux conjonctions ($\land$).

---

### Étape 1 : Élimination des connecteurs d'implication ($\Rightarrow$)
Rappelons la règle d'équivalence de base : $A \Rightarrow B \equiv \neg A \lor B$.

1. Éliminons l'implication principale de $H$. Posons $A = (P \Rightarrow Q)$ et $B = (R \land \neg S)$. L'expression devient :
   $$H \equiv \neg(P \Rightarrow Q) \lor (R \land \neg S)$$
2. Éliminons l'implication résiduelle à l'intérieur de la négation :
   $$P \Rightarrow Q \equiv \neg P \lor Q$$
3. Substituons ce résultat dans la formule complète :
   $$H \equiv \neg(\neg P \lor Q) \lor (R \land \neg S)$$

---

### Étape 2 : Descente des négations ($\neg$)
Appliquons la loi de De Morgan sur le premier bloc $\neg(\neg P \lor Q)$ :
$$\neg(\neg P \lor Q) \equiv \neg(\neg P) \land \neg Q$$

Par la règle de double négation ($\neg\neg P \equiv P$) :
$$\neg(\neg P \lor Q) \equiv P \land \neg Q$$

Substituons cette forme simplifiée dans l'expression globale de $H$ :
$$H \equiv (P \land \neg Q) \lor (R \land \neg S)$$

---

### Étape 3 : Distribution de la disjonction ($\lor$) par rapport à la conjonction ($\land$)
Nous devons maintenant distribuer la disjonction extérieure par rapport aux conjonctions intérieures.
Soient $X = (P \land \neg Q)$ et $Y = (R \land \neg S)$. L'expression est $X \lor Y$.

1. Distribuons d'abord le bloc $X$ sur la conjonction $Y = (R \land \neg S)$ :
   $$X \lor (R \land \neg S) \equiv (X \lor R) \land (X \lor \neg S)$$
2. Remplaçons maintenant $X$ par sa valeur originelle $(P \land \neg Q)$ dans le premier terme $(X \lor R)$ :
   $$X \lor R \equiv (P \land \neg Q) \lor R$$
   Appliquons la distributivité de $\lor$ par rapport à $\land$ sur ce terme :
   $$(P \land \neg Q) \lor R \equiv (P \lor R) \land (\neg Q \lor R)$$
3. Remplaçons $X$ dans le second terme $(X \lor \neg S)$ :
   $$X \lor \neg S \equiv (P \land \neg Q) \lor \neg S$$
   Distribuons également :
   $$(P \land \neg Q) \lor \neg S \equiv (P \lor \neg S) \land (\neg Q \lor \neg S)$$
4. Assemblons maintenant les résultats des points 2 et 3 dans la formule générale obtenue au point 1 :
   $$H \equiv \Big( (P \lor R) \land (\neg Q \lor R) \Big) \land \Big( (P \lor \neg S) \land (\neg Q \lor \neg S) \Big)$$
5. Par associativité de la conjonction $\land$, nous pouvons supprimer les parenthèses superflues :
   $$H \equiv (P \lor R) \land (\neg Q \lor R) \land (P \lor \neg S) \land (\neg Q \lor \neg S)$$

---

### Résultat final
La formule $H$ sous Forme Normale Conjonctive est :
$$H \equiv (P \lor R) \land (\neg Q \lor R) \land (P \lor \neg S) \land (\neg Q \lor \neg S)$$

Cette CNF est composée de $4$ clauses disjonctives :
- Clause 1 : $P \lor R$
- Clause 2 : $\neg Q \lor R$
- Clause 3 : $P \lor \neg S$
- Clause 4 : $\neg Q \lor \neg S$
