# TP 4 : Implémentation d'un solveur SAT DPLL

## Objectif
L'objectif de ce TP est de concevoir et de coder en Python pur un **solveur SAT** complet basé sur l'algorithme historique **DPLL** (Davis-Putnam-Logemann-Loveland) incorporant la technique de la **propagation unitaire**. Le programme prendra en entrée une formule sous forme de clauses CNF (comme celle générée au TP 3) et déterminera si la formule est satisfaisable, en fournissant une affectation valide des variables le cas échéant.

---

## Modélisation de l'algorithme DPLL
L'algorithme DPLL est une recherche par séparation et évaluation (backtracking) dans l'arbre binaire des affectations de variables, optimisée par la propagation de contraintes forcées.

### Les étapes de la fonction récursive :
1. **Propagation unitaire :** Si une clause est réduite à un seul littéral $\{L\}$ (clause unitaire), alors le littéral $L$ doit obligatoirement être évalué à Vrai pour satisfaire cette clause.
   - On simplifie les clauses sous l'hypothèse $L = True$.
   - On répète cette étape jusqu'à ce qu'il n'y ait plus aucune clause unitaire.
2. **Conditions d'arrêt :**
   - Si l'ensemble des clauses est vide, toutes les contraintes sont satisfaites. La formule est **Satisfaisable**. On renvoie `(True, affectation_courante)`.
   - Si l'ensemble contient une clause vide (un ensemble vide `{}`), cela signifie qu'une contradiction a été atteinte. La branche actuelle est **Insatisfaisable**. On renvoie `(False, None)`.
3. **Branchement (Heuristique) :**
   - On choisit une variable propositionnelle libre $P$ (qui n'a pas encore de valeur affectée).
   - On tente de résoudre récursivement en posant $P = True$.
   - En cas d'échec (retourne `False`), on tente de résoudre en posant $P = False$.
   - Si les deux branches échouent, on retourne `(False, None)`.

---

## Code Source Python

```python
def parse_literal(literal):
    """Sépare le signe du nom de la variable. Retourne (nom, est_negatif)."""
    if literal.startswith("~"):
        return literal[1:], True
    return literal, False

def negate_literal(literal):
    """Retourne le littéral complémentaire."""
    if literal.startswith("~"):
        return literal[1:]
    return f"~{literal}"

def simplify_cnf(clauses, literal):
    """
    Simplifie la CNF en supposant que 'literal' est Vrai.
    - Supprime toutes les clauses contenant 'literal'.
    - Supprime la négation de 'literal' de toutes les clauses restantes.
    """
    neg_lit = negate_literal(literal)
    new_clauses = []
    
    for clause in clauses:
        if literal in clause:
            # La clause est satisfaite, on la supprime de l'ensemble
            continue
        # On crée une nouvelle clause en enlevant la négation du littéral
        new_clause = {lit for lit in clause if lit != neg_lit}
        new_clauses.append(new_clause)
        
    return new_clauses

def dpll(clauses, assignment):
    """
    Fonction récursive principale de l'algorithme DPLL.
    clauses : liste de sets (clauses CNF)
    assignment : dictionnaire (variable -> bool)
    """
    # 1. Propagation unitaire
    unit_clauses = [c for c in clauses if len(c) == 1]
    while unit_clauses:
        # On extrait le littéral unique de la première clause unitaire
        lit = list(unit_clauses[0])[0]
        var, is_neg = parse_literal(lit)
        
        # Enregistrement de l'affectation forcée
        assignment[var] = not is_neg
        
        # Simplification de la CNF
        clauses = simplify_cnf(clauses, lit)
        
        # Cas d'arrêt immédiat après simplification
        if len(clauses) == 0:
            return True, assignment
        if any(len(c) == 0 for c in clauses):
            return False, None
            
        unit_clauses = [c for c in clauses if len(c) == 1]

    # 2. Cas d'arrêt de base
    if len(clauses) == 0:
        return True, assignment
    if any(len(c) == 0 for c in clauses):
        return False, None

    # 3. Branchement (Choix d'une variable non encore assignée)
    # On prend la première variable de la première clause restante
    chosen_lit = list(clauses[0])[0]
    chosen_var, _ = parse_literal(chosen_lit)

    # Tentative branche 1 : chosen_var = True (littéral chosen_var est vrai)
    assignment_true = assignment.copy()
    assignment_true[chosen_var] = True
    clauses_true = simplify_cnf(clauses, chosen_var)
    success, res = dpll(clauses_true, assignment_true)
    if success:
        return True, res

    # Tentative branche 2 : chosen_var = False (littéral ~chosen_var est vrai)
    assignment_false = assignment.copy()
    assignment_false[chosen_var] = False
    clauses_false = simplify_cnf(clauses, f"~{chosen_var}")
    return dpll(clauses_false, assignment_false)

def solve_sat(clauses):
    """Point d'entrée utilisateur pour résoudre une CNF."""
    # On s'assure d'éliminer les doublons et de travailler sur une liste de sets indépendants
    cleaned_clauses = [set(c) for c in clauses]
    return dpll(cleaned_clauses, {})
```

---

## Exemple de Validation et Test

Résolvons l'ensemble contradictoire du TP 2 et un cas satisfaisable :

```python
if __name__ == "__main__":
    # Test 1 : Base insatisfaisable du TP 2 :
    # (P v Q) & (~P v Q) & (P v ~Q) & (~P v ~Q)
    cnf_contradiction = [
        {"P", "Q"},
        {"~P", "Q"},
        {"P", "~Q"},
        {"~P", "~Q"}
    ]
    print("Résolution du Test 1 (Contradiction) :")
    sat, model = solve_sat(cnf_contradiction)
    print("Satisfaisable :", sat)
    print("Modèle :", model)
    
    # Test 2 : Base satisfaisable :
    # (~P v Q) & (~Q v R) & (~R v ~P) & (P)
    # Doit forcer P=True, ce qui force Q=True (propagation), ce qui force R=True (propagation),
    # ce qui rend la 3ème clause (~R v ~P) fausse car ~True v ~True = Faux.
    # On s'attend à ce que cette formule soit déclarée insatisfaisable.
    cnf_test2 = [
        {"~P", "Q"},
        {"~Q", "R"},
        {"~R", "~P"},
        {"P"}
    ]
    print("\nRésolution du Test 2 (Propagation forcée menant à un échec) :")
    sat, model = solve_sat(cnf_test2)
    print("Satisfaisable :", sat)
    print("Modèle :", model)
    
    # Test 3 : Base satisfaisable :
    # (~P v Q) & (~Q v R) & (P)
    # Doit forcer P=True, Q=True, R=True
    cnf_satisfaisable = [
        {"~P", "Q"},
        {"~Q", "R"},
        {"P"}
    ]
    print("\nRésolution du Test 3 (Satisfaisable avec propagation) :")
    sat, model = solve_sat(cnf_satisfaisable)
    print("Satisfaisable :", sat)
    print("Modèle :", model)
```

### Sortie attendue :
```text
Résolution du Test 1 (Contradiction) :
Satisfaisable : False
Modèle : None

Résolution du Test 2 (Propagation forcée menant à un échec) :
Satisfaisable : False
Modèle : None

Résolution du Test 3 (Satisfaisable avec propagation) :
Satisfaisable : True
Modèle : {'P': True, 'Q': True, 'R': True}
```
Our SAT-solver is fully operational!
