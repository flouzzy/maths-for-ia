# TP 3 : Transformation de Tseitin pour la mise en CNF linéaire

## Objectif
L'objectif de ce TP est d'implémenter la **transformation de Tseitin** en Python. La conversion naïve d'une formule en Forme Normale Conjonctive (CNF) par simple application des règles de distributivité peut conduire à une explosion exponentielle de la taille de la formule. La transformation de Tseitin contourne ce problème en introduisant des variables auxiliaires pour chaque sous-formule, permettant de générer une formule en CNF équisatisfiable de taille **linéaire** par rapport à la formule initiale.

---

## Principes Théoriques et Modélisation
Pour chaque sous-formule (nœud interne ou feuille de notre AST), la transformation de Tseitin introduit une nouvelle variable propositionnelle $x_i$.
On ajoute ensuite des clauses qui forcent la variable $x_i$ à être équivalente à l'application de l'opérateur logique sur ses enfants.

### Équivalences logiques en CNF :

1. **Négation :** $x_C \Leftrightarrow \neg x_A$
   - Équivalent à : $(\neg x_C \lor \neg x_A) \land (x_C \lor x_A)$
   
2. **Conjonction :** $x_C \Leftrightarrow (x_A \land x_B)$
   - Équivalent à : $(\neg x_C \lor x_A) \land (\neg x_C \lor x_B) \land (\neg x_A \lor \neg x_B \lor x_C)$
   
3. **Disjonction :** $x_C \Leftrightarrow (x_A \lor x_B)$
   - Équivalent à : $(\neg x_C \lor x_A \lor x_B) \land (\neg x_A \lor x_C) \land (\neg x_B \lor x_C)$
   
4. **Implication :** $x_C \Leftrightarrow (x_A \Rightarrow x_B)$
   - Équivalent à : $(\neg x_C \lor \neg x_A \lor x_B) \land (x_A \lor x_C) \land (\neg x_B \lor x_C)$

La CNF finale est constituée de la conjonction de toutes ces contraintes de nœuds, à laquelle on ajoute la clause unitaire $(x_{root})$ qui force la formule générale à être vraie.

---

## Code Source Python

Chaque clause sera représentée sous forme d'un ensemble de littéraux (un littéral étant une chaîne de caractères comme `"P"` ou `"~P"`). La CNF est une liste de clauses (liste de sets).

```python
# Import des classes du TP 1
from tp_01_ast import Formula, Variable, Not, And, Or, Implies, Equiv

class TseitinTransformer:
    def __init__(self):
        self.counter = 0
        self.clauses = []
        
    def _new_variable(self):
        """Crée une variable auxiliaire unique (ex: _t1, _t2, ...)."""
        self.counter += 1
        return f"_t{self.counter}"
        
    def transform(self, formula: Formula):
        """
        Point d'entrée principal. 
        Retourne : (variable_racine, liste_de_clauses_CNF)
        """
        self.clauses = []
        self.counter = 0
        root_var = self._traverse(formula)
        # On force la racine à être Vraie en ajoutant la clause unitaire {root_var}
        self.clauses.append({root_var})
        return root_var, self.clauses
        
    def _traverse(self, node: Formula):
        """Parcours récursif de l'AST."""
        if isinstance(node, Variable):
            return node.name
            
        elif isinstance(node, Not):
            child_var = self._traverse(node.child)
            fresh_var = self._new_variable()
            # Contrainte : fresh_var <=> ~child_var
            # (~fresh_var v ~child_var) & (fresh_var v child_var)
            self.clauses.append({f"~{fresh_var}", f"~{child_var}"})
            self.clauses.append({fresh_var, child_var})
            return fresh_var
            
        elif isinstance(node, And):
            left_var = self._traverse(node.left)
            right_var = self._traverse(node.right)
            fresh_var = self._new_variable()
            # Contrainte : fresh_var <=> (left_var & right_var)
            # (~fresh_var v left_var) & (~fresh_var v right_var) & (~left_var v ~right_var v fresh_var)
            self.clauses.append({f"~{fresh_var}", left_var})
            self.clauses.append({f"~{fresh_var}", right_var})
            self.clauses.append({f"~{left_var}", f"~{right_var}", fresh_var})
            return fresh_var
            
        elif isinstance(node, Or):
            left_var = self._traverse(node.left)
            right_var = self._traverse(node.right)
            fresh_var = self._new_variable()
            # Contrainte : fresh_var <=> (left_var | right_var)
            # (~fresh_var v left_var v right_var) & (~left_var v fresh_var) & (~right_var v fresh_var)
            self.clauses.append({f"~{fresh_var}", left_var, right_var})
            self.clauses.append({f"~{left_var}", fresh_var})
            self.clauses.append({f"~{right_var}", fresh_var})
            return fresh_var
            
        elif isinstance(node, Implies):
            left_var = self._traverse(node.left)
            right_var = self._traverse(node.right)
            fresh_var = self._new_variable()
            # Contrainte : fresh_var <=> (left_var => right_var)
            # equivalent a : fresh_var <=> (~left_var | right_var)
            # (~fresh_var v ~left_var v right_var) & (left_var v fresh_var) & (~right_var v fresh_var)
            self.clauses.append({f"~{fresh_var}", f"~{left_var}", right_var})
            self.clauses.append({left_var, fresh_var})
            self.clauses.append({f"~{right_var}", fresh_var})
            return fresh_var
            
        else:
            raise NotImplementedError("Type de noeud non pris en charge.")

def print_cnf(clauses):
    """Affiche de manière lisible la liste des clauses CNF."""
    formatted_clauses = []
    for clause in clauses:
        sorted_literals = sorted(list(clause), key=lambda x: x.replace("~", ""))
        formatted_clauses.append("(" + " | ".join(sorted_literals) + ")")
    print(" & ".join(formatted_clauses))
```

---

## Exemple d'Utilisation

Mettons sous CNF la formule $(P \land Q) \lor R$ :

```python
if __name__ == "__main__":
    p = Variable("P")
    q = Variable("Q")
    r = Variable("R")
    
    # Formule : (P & Q) | R
    formula = Or(And(p, q), r)
    print("Formule de départ :", formula)
    
    transformer = TseitinTransformer()
    root, clauses = transformer.transform(formula)
    
    print("\nVariable représentative de la racine :", root)
    print("\nCNF équisatisfiable générée par Tseitin :")
    print_cnf(clauses)
```

### Sortie console attendue :
```text
Formule de départ : ((P & Q) | R)

Variable représentative de la racine : _t2

CNF équisatisfiable générée par Tseitin :
(~_t1 | P) & (~_t1 | Q) & (~P | ~Q | _t1) & (~_t2 | R | _t1) & (~_t1 | _t2) & (~R | _t2) & (_t2)
```
Ce format est directement exploitable par les solveurs SAT standard.
