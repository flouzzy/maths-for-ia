```yaml
title: "Densité des Nombres Rationnels dans les Nombres Réels"
difficulty: 3
tags: [Densité, Rationnels, Réels, Archimède, Bornes]
```
## Énoncé de l'Exercice 06

Démontrer la propriété de densité des nombres rationnels $\mathbb{Q}$ dans les nombres réels $\mathbb{R}$. Cette propriété énonce que pour tout couple de nombres réels $(a, b)$ tels que $a < b$, il existe au moins un nombre rationnel $q$ qui est strictement compris entre $a$ et $b$.

Formellement :
$$ \forall (a,b) \in \mathbb{R}^2, \quad \text{si } a < b \text{, alors } \exists q \in \mathbb{Q} \text{ tel que } a < q < b $$

Votre démonstration doit s'appuyer explicitement sur la propriété d'Archimède.

### Propriété d'Archimède Rappelée :

Pour tout nombre réel $x > 0$ et tout nombre réel $y > 0$, il existe un entier naturel $n \in \mathbb{N}^*$ tel que $nx > y$.
Une autre formulation équivalente est : Pour tout nombre réel $\varepsilon > 0$, il existe un entier naturel $n \in \mathbb{N}^*$ tel que $0 < 1/n < \varepsilon$.

### Définition de $\mathbb{Q}$ Rappelée :

L'ensemble des nombres rationnels $\mathbb{Q}$ est défini comme $\mathbb{Q} = \{ p/q \mid p \in \mathbb{Z}, q \in \mathbb{N}^* \}$.

---