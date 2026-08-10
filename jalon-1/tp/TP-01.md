# TP 1 : Arbre syntaxique abstrait pour formules logiques

## Objectif
L'objectif de ce TP est de concevoir et d'implémenter en Python une structure de données d'**Arbre Syntaxique Abstrait (AST)** permettant de modéliser, de représenter sous forme textuelle propre et d'évaluer sémantiquement n'importe quelle formule bien formée de la logique propositionnelle.

---

## Conception Théorique
Pour modéliser une formule logique en programmation orientée objet, nous utilisons le patron de conception **Composite**.
- Une classe de base abstraite `Formula` définit l'interface commune.
- Les variables propositionnelles sont représentées par des nœuds feuilles (`Variable`).
- Les connecteurs logiques correspondent à des nœuds internes unaires (`Not`) ou binaires (`And`, `Or`, `Implies`, `Equiv`).

Chaque classe doit implémenter trois opérations clés :
1. `__str__(self)` : retourne une représentation textuelle parenthésée de la formule.
2. `get_variables(self)` : retourne l'ensemble (`set`) des variables propositionnelles présentes dans la formule.
3. `evaluate(self, valuation)` : évalue la valeur de vérité ($True$ ou $False$) de la formule pour une valuation donnée sous forme de dictionnaire Python `{nom_variable: booléen}`.

---

## Code Source Python (from scratch)

Voici l'implémentation complète des classes en Python :

```python
from abc import ABC, abstractmethod

class Formula(ABC):
    """Classe abstraite de base pour toutes les formules propositionnelles."""
    
    @abstractmethod
    def __str__(self):
        """Retourne la représentation textuelle sous forme de chaîne de caractères."""
        pass
        
    @abstractmethod
    def get_variables(self):
        """Retourne un ensemble (set) de toutes les variables propositionnelles de la formule."""
        pass
        
    @abstractmethod
    def evaluate(self, valuation):
        """Évalue la formule pour une valuation donnée (dictionnaire de type dict[str, bool])."""
        pass


class Variable(Formula):
    """Représente une variable propositionnelle (atome, feuille de l'arbre)."""
    
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name
        
    def get_variables(self):
        return {self.name}
        
    def evaluate(self, valuation):
        if self.name not in valuation:
            raise ValueError(f"La variable {self.name} n'est pas définie dans la valuation fournie.")
        return valuation[self.name]


class Not(Formula):
    """Représente le connecteur de négation (noeud interne unaire)."""
    
    def __init__(self, child):
        self.child = child
        
    def __str__(self):
        return f"~({self.child})"
        
    def get_variables(self):
        return self.child.get_variables()
        
    def evaluate(self, valuation):
        return not self.child.evaluate(valuation)


class BinaryOperator(Formula, ABC):
    """Classe intermédiaire pour les opérateurs binaires (conjonction, disjonction, etc.)."""
    
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def get_variables(self):
        return self.left.get_variables().union(self.right.get_variables())


class And(BinaryOperator):
    """Représente le connecteur de conjonction ET (noeud interne binaire)."""
    
    def __str__(self):
        return f"({self.left} & {self.right})"
        
    def evaluate(self, valuation):
        return self.left.evaluate(valuation) and self.right.evaluate(valuation)


class Or(BinaryOperator):
    """Représente le connecteur de disjonction OU (noeud interne binaire)."""
    
    def __str__(self):
        return f"({self.left} | {self.right})"
        
    def evaluate(self, valuation):
        return self.left.evaluate(valuation) or self.right.evaluate(valuation)


class Implies(BinaryOperator):
    """Représente le connecteur d'implication (SI ... ALORS ...)."""
    
    def __str__(self):
        return f"({self.left} => {self.right})"
        
    def evaluate(self, valuation):
        # A => B est équivalent à (non A) ou B
        return (not self.left.evaluate(valuation)) or self.right.evaluate(valuation)


class Equiv(BinaryOperator):
    """Représente le connecteur d'équivalence équivalent (SI ET SEULEMENT SI)."""
    
    def __str__(self):
        return f"({self.left} <=> {self.right})"
        
    def evaluate(self, valuation):
        return self.left.evaluate(valuation) == self.right.evaluate(valuation)
```

---

## Validation et Exemple d'utilisation

Ajoutons un script de test pour valider notre implémentation :

```python
if __name__ == "__main__":
    # Définition des variables
    p = Variable("P")
    q = Variable("Q")
    r = Variable("R")
    
    # Construction de la formule : (P & Q) => (R | ~P)
    formule = Implies(And(p, q), Or(r, Not(p)))
    
    print("Formule logique générée :")
    print(formule)  # Doit afficher : ((P & Q) => (R | ~(P)))
    
    print("\nExtraction des variables :")
    print(formule.get_variables())  # Doit afficher : {'P', 'Q', 'R'}
    
    # Définition d'une valuation
    valuation_1 = {"P": True, "Q": True, "R": False}
    print(f"\nÉvaluation avec la valuation {valuation_1} :")
    res_1 = formule.evaluate(valuation_1)
    print(f"Résultat : {res_1}")  # Doit afficher : False (car Vrai => Faux est Faux)
    
    valuation_2 = {"P": False, "Q": True, "R": False}
    print(f"\nÉvaluation avec la valuation {valuation_2} :")
    res_2 = formule.evaluate(valuation_2)
    print(f"Résultat : {res_2}")  # Doit afficher : True (car Faux => Vrai est Vrai)
```
