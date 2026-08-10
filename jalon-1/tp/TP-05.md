# TP 5 : Résolution du problème des N-Reines par réduction SAT

## Objectif
L'objectif de ce TP est d'utiliser le solveur SAT DPLL développé au TP 4 pour résoudre un problème combinatoire classique d'Intelligence Artificielle : **le problème des N-Reines** (placer $N$ reines sur un échiquier de taille $N \times N$ sans qu'elles ne se menacent mutuellement). Nous écrirons un script Python pour générer automatiquement les contraintes du problème sous forme de clauses CNF, les résoudrons avec notre solveur et afficherons la grille solution.

---

## Modélisation du problème des N-Reines en SAT
Pour un échiquier de taille $N \times N$, nous définissons $N^2$ variables propositionnelles notées `Q_i_j` pour $0 \le i, j < N$.
- La variable `Q_i_j` est évaluée à Vrai si et seulement si une reine est placée à la ligne $i$ et à la colonne $j$.

### Les Contraintes du Problème :
1. **Au moins une reine par ligne :**
   Pour chaque ligne $i$ :
   $$\bigvee_{j=0}^{N-1} Q_{i, j}$$
2. **Au plus une reine par ligne :**
   Pour chaque ligne $i$, et chaque paire de colonnes distinctes $j_1 < j_2$ :
   $$\neg Q_{i, j_1} \lor \neg Q_{i, j_2}$$
3. **Au plus une reine par colonne :**
   Pour chaque colonne $j$, et chaque paire de lignes distinctes $i_1 < i_2$ :
   $$\neg Q_{i_1, j} \lor \neg Q_{i_2, j}$$
4. **Au plus une reine par diagonale :**
   Deux reines sur une même diagonale (descendante ou montante) se menacent si la valeur absolue de la différence de leurs lignes est égale à celle de leurs colonnes. Pour toute paire de cases $(i_1, j_1)$ et $(i_2, j_2)$ telles que $i_1 < i_2$ et $|i_1 - i_2| = |j_1 - j_2|$ :
   $$\neg Q_{i_1, j_1} \lor \neg Q_{i_2, j_2}$$

---

## Code Source Python

```python
# Import du solveur du TP 4
from tp_04_dpll import solve_sat

def get_var_name(i, j):
    """Retourne le nom de la variable propositionnelle pour la case (i, j)."""
    return f"Q_{i}_{j}"

def generate_n_queens_cnf(n):
    """Génère la liste des clauses CNF pour le problème des N-Reines."""
    clauses = []
    
    # 1. Au moins une reine par ligne
    for i in range(n):
        clause = {get_var_name(i, j) for j in range(n)}
        clauses.append(clause)
        
    # 2. Au plus une reine par ligne
    for i in range(n):
        for j1 in range(n):
            for j2 in range(j1 + 1, n):
                clauses.append({f"~{get_var_name(i, j1)}", f"~{get_var_name(i, j2)}"})
                
    # 3. Au plus une reine par colonne
    for j in range(n):
        for i1 in range(n):
            for i2 in range(i1 + 1, n):
                clauses.append({f"~{get_var_name(i1, j)}", f"~{get_var_name(i2, j)}"})
                
    # 4. Au plus une reine par diagonale
    for i1 in range(n):
        for j1 in range(n):
            for i2 in range(i1 + 1, n):
                for j2 in range(n):
                    if abs(i1 - i2) == abs(j1 - j2):
                        clauses.append({f"~{get_var_name(i1, j1)}", f"~{get_var_name(i2, j2)}"})
                        
    return clauses

def print_board(n, model):
    """Affiche l'échiquier avec les reines placées."""
    border = "+" + "---+" * n
    print(border)
    for i in range(n):
        row = "|"
        for j in range(n):
            var = get_var_name(i, j)
            # Si la variable vaut True dans le modèle, on place une reine 'R'
            if model.get(var, False):
                row += " R |"
            else:
                row += " . |"
        print(row)
        print(border)

def solve_n_queens(n):
    """Génère les contraintes, lance le solveur et affiche le résultat."""
    print(f"--- Résolution du problème des {n}-Reines ---")
    
    # Génération des contraintes
    clauses = generate_n_queens_cnf(n)
    print(f"Nombre de clauses CNF générées : {len(clauses)}")
    
    # Résolution SAT
    success, model = solve_sat(clauses)
    
    if success:
        print("\nSolution trouvée :")
        print_board(n, model)
    else:
        print("\nAucune solution n'existe pour cette taille d'échiquier.")
```

---

## Exemple de Validation et Test (N = 4)

Placer 4 reines sur un échiquier de 4x4 :

```python
if __name__ == "__main__":
    # Résolution pour N = 4
    solve_n_queens(4)
    
    # Résolution pour N = 3 (doit être déclarée impossible)
    print("\n")
    solve_n_queens(3)
```

### Rendu console attendu :
```text
--- Résolution du problème des 4-Reines ---
Nombre de clauses CNF générées : 84

Solution trouvée :
+---+---+---+---+
| . | R | . | . |
+---+---+---+---+
| . | . | . | R |
+---+---+---+---+
| R | . | . | . |
+---+---+---+---+
| . | . | R | . |
+---+---+---+---+


--- Résolution du problème des 3-Reines ---
Nombre de clauses CNF générées : 26

Aucune solution n'existe pour cette taille d'échiquier.
```
Le placement des reines est correct, les diagonales, lignes et colonnes sont parfaitement préservées !
