```yaml
title: "Démonstration de la Borne Supérieure par Définition"
difficulty: 1
tags: [Supremum, Définition, Nombres Réels]
```
## Énoncé de l'Exercice 02

Soit l'ensemble $A$ défini par :
$$ A = \left\{ 1 - \frac{1}{n} \mid n \in \mathbb{N}^* \right\} $$
où $\mathbb{N}^* = \{1, 2, 3, \ldots\}$ désigne l'ensemble des entiers naturels non nuls.

Démontrer rigoureusement, en utilisant la définition formelle de la borne supérieure, que $\sup A = 1$.

### Définition Rappelée :

Un nombre réel $s_0$ est la **borne supérieure** d'un ensemble $S \subset \mathbb{R}$ non vide si et seulement si les deux conditions suivantes sont satisfaites :
1.  **Condition de Majorant** : Pour tout élément $x$ de l'ensemble $S$, on a $x \le s_0$.
2.  **Condition de Plus Petit Majorant** : Pour tout nombre réel $\varepsilon$ strictement positif ($\varepsilon > 0$), il existe au moins un élément $x_{\varepsilon}$ dans l'ensemble $S$ tel que $x_{\varepsilon} > s_0 - \varepsilon$.

---