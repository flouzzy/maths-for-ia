# TP 2 : Générateur automatique de tables de vérité

## Objectif
L'objectif de ce TP est de concevoir un générateur automatique de tables de vérité en Python. À partir de n'importe quel arbre de formule logique implémenté au TP 1, le programme doit lister toutes les variables libres, générer les $2^n$ combinaisons de valeurs de vérité possibles, évaluer la formule et imprimer la table de vérité finale proprement formatée en Markdown.

---

## Algorithme et Méthode
1. **Extraction et tri des variables :** On extrait l'ensemble des variables propositionnelles libres de la formule en appelant `formula.get_variables()`. On convertit cet ensemble en une liste ordonnée alphabétiquement afin de garantir un affichage reproductible et cohérent des colonnes.
2. **Génération de l'espace des valuations $\{0, 1\}^n$ :** On utilise la récursion pour engendrer toutes les $2^n$ configurations de vérité sans utiliser de bibliothèque standard afin de rester strictement "from scratch".
3. **Évaluation et formatage :** Pour chaque configuration (valuation), on évalue la formule à l'aide de sa méthode `.evaluate(valuation)`. On affiche chaque ligne avec des symboles lisibles (par exemple `1` ou `T` pour True, `0` ou `F` pour False) et on trace la grille de la table au format Markdown.

---

## Code Source Python

```python
# Import des classes du TP 1
# On suppose les classes du TP 1 présentes dans le même fichier ou importées
from tp_01_ast import Formula, Variable, Not, And, Or, Implies, Equiv

def generate_combinations(n):
    """Génère récursivement toutes les 2^n combinaisons de valeurs de vérité de True à False."""
    if n == 0:
        return [()]
    sub_combinations = generate_combinations(n - 1)
    return [(True,) + combo for combo in sub_combinations] + [(False,) + combo for combo in sub_combinations]

def generate_truth_table(formula: Formula):
    """Génère et affiche la table de vérité d'une formule au format Markdown."""
    
    # 1. Extraction et tri des variables propositionnelles
    vars_list = sorted(list(formula.get_variables()))
    n = len(vars_list)
    
    # 2. Construction des en-têtes Markdown
    headers = vars_list + [str(formula)]
    header_line = " | ".join(headers)
    separator_line = " | ".join(["---"] * len(headers))
    
    table_lines = [header_line, separator_line]
    
    # 3. Génération de toutes les valuations possibles (2^n)
    combinations = generate_combinations(n)
    
    # Pour respecter l'ordre traditionnel (Vrai en premier, c'est-à-dire 1 puis 0),
    # product avec [True, False] trie naturellement de True à False.
    
    tautology = True
    contradiction = True
    
    for combo in combinations:
        # Création du dictionnaire de valuation
        valuation = {vars_list[i]: combo[i] for i in range(n)}
        
        # Évaluation de la formule pour cette valuation
        result = formula.evaluate(valuation)
        
        # Suivi de la nature de la formule
        if result:
            contradiction = False
        else:
            tautology = False
            
        # Conversion des valeurs booléennes en chaînes de caractères ('1' ou '0')
        row_values = [("1" if val else "0") for val in combo] + [("1" if result else "0")]
        table_lines.append(" | ".join(row_values))
        
    # Affichage de la table de vérité
    print("\n".join(table_lines))
    
    # 4. Diagnostic de la formule
    print("\n---")
    print("### Diagnostic de la formule :")
    if tautology:
        print("La formule est une **Tautologie** (toujours vraie).")
    elif contradiction:
        print("La formule est une **Contradiction** (toujours fausse).")
    else:
        print("La formule est **Contingente** (satisfaisable, possède au moins un modèle et un contre-modèle).")
```

---

## Exemple d'Exécution

Modélisons la formule du tiers exclu et l'implication logique :

```python
if __name__ == "__main__":
    # Test 1 : Tiers exclu : P | ~P
    p = Variable("P")
    tiers_exclu = Or(p, Not(p))
    print("### Table de vérité de la formule : P | ~P")
    generate_truth_table(tiers_exclu)
    
    # Test 2 : Formule contingente : (P & Q) => R
    q = Variable("Q")
    r = Variable("R")
    contingence = Implies(And(p, q), r)
    print("\n### Table de vérité de la formule : (P & Q) => R")
    generate_truth_table(contingence)
    
    # Test 3 : Loi de Peirce : ((P => Q) => P) => P
    peirce = Implies(Implies(Implies(p, q), p), p)
    print("\n### Table de vérité de la Loi de Peirce : ((P => Q) => P) => P")
    generate_truth_table(peirce)
```

### Rendu attendu en console pour le Test 3 (Loi de Peirce) :
```markdown
P | Q | (((P => Q) => P) => P)
--- | --- | ---
1 | 1 | 1
1 | 0 | 1
0 | 1 | 1
0 | 0 | 1

---
### Diagnostic de la formule :
La formule est une **Tautologie** (toujours vraie).
```
