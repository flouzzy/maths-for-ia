# Exercice 3 : L'Ensemble des Parties et l'Intersection

**Difficulté :** ⭐⭐
**Thème :** Opérations sur les ensembles, ensemble des parties, preuve d'égalité ensembliste.

## Énoncé

Soient $A$ et $B$ deux ensembles quelconques. On rappelle que l'ensemble des parties de $E$, noté $\mathcal{P}(E)$, est l'ensemble de tous les sous-ensembles de $E$.

Démontrer rigoureusement l'égalité ensembliste suivante :
$$ \mathcal{P}(A \cap B) = \mathcal{P}(A) \cap \mathcal{P}(B) $$

## Correction Détaillée

Pour démontrer l'égalité de deux ensembles, il est nécessaire et suffisant de démontrer la double inclusion. C'est-à-dire, nous devons montrer que $\mathcal{P}(A \cap B) \subseteq \mathcal{P}(A) \cap \mathcal{P}(B)$ et que $\mathcal{P}(A) \cap \mathcal{P}(B) \subseteq \mathcal{P}(A \cap B)$.

Soient $A$ et $B$ des ensembles quelconques, éléments de notre univers de discours défini par la théorie des ensembles ZFC.

### Partie 1 : Démonstration de $\mathcal{P}(A \cap B) \subseteq \mathcal{P}(A) \cap \mathcal{P}(B)$

Pour prouver cette inclusion, nous allons prendre un élément arbitraire de l'ensemble de gauche et montrer qu'il appartient nécessairement à l'ensemble de droite.

1.  Soit $X$ un ensemble. Supposons que $X \in \mathcal{P}(A \cap B)$.
2.  Par définition de l'ensemble des parties, si $X \in \mathcal{P}(A \cap B)$, cela signifie que $X$ est un sous-ensemble de $A \cap B$. Autrement dit, $X \subseteq A \cap B$.
3.  Par définition de l'intersection de deux ensembles, si un ensemble $X$ est un sous-ensemble de $A \cap B$, alors tout élément $x$ de $X$ appartient à $A \cap B$.
    Soit $x$ un élément arbitraire tel que $x \in X$.
    Puisque $X \subseteq A \cap B$, il s'ensuit que $x \in A \cap B$.
4.  Par définition de l'intersection, si $x \in A \cap B$, alors $x \in A$ et $x \in B$.
5.  Comme ceci est vrai pour tout $x \in X$, nous pouvons conclure que tout élément de $X$ est un élément de $A$. Par conséquent, $X \subseteq A$.
6.  De même, comme ceci est vrai pour tout $x \in X$, nous pouvons conclure que tout élément de $X$ est un élément de $B$. Par conséquent, $X \subseteq B$.
7.  Par définition de l'ensemble des parties, puisque $X \subseteq A$, il s'ensuit que $X \in \mathcal{P}(A)$.
8.  De même, puisque $X \subseteq B$, il s'ensuit que $X \in \mathcal{P}(B)$.
9.  Puisque $X \in \mathcal{P}(A)$ et $X \in \mathcal{P}(B)$, par définition de l'intersection d'ensembles, $X$ appartient à l'intersection de $\mathcal{P}(A)$ et $\mathcal{P}(B)$. C'est-à-dire, $X \in \mathcal{P}(A) \cap \mathcal{P}(B)$.
10. Ayant montré que tout $X \in \mathcal{P}(A \cap B)$ implique $X \in \mathcal{P}(A) \cap \mathcal{P}(B)$, nous avons démontré l'inclusion :
    $$ \mathcal{P}(A \cap B) \subseteq \mathcal{P}(A) \cap \mathcal{P}(B) $$

### Partie 2 : Démonstration de $\mathcal{P}(A) \cap \mathcal{P}(B) \subseteq \mathcal{P}(A \cap B)$

Pour prouver cette inclusion, nous allons prendre un élément arbitraire de l'ensemble de droite et montrer qu'il appartient nécessairement à l'ensemble de gauche.

1.  Soit $Y$ un ensemble. Supposons que $Y \in \mathcal{P}(A) \cap \mathcal{P}(B)$.
2.  Par définition de l'intersection de deux ensembles, si $Y \in \mathcal{P}(A) \cap \mathcal{P}(B)$, cela signifie que $Y \in \mathcal{P}(A)$ et $Y \in \mathcal{P}(B)$.
3.  Par définition de l'ensemble des parties, si $Y \in \mathcal{P}(A)$, alors $Y$ est un sous-ensemble de $A$. C'est-à-dire, $Y \subseteq A$.
4.  De même, par définition de l'ensemble des parties, si $Y \in \mathcal{P}(B)$, alors $Y$ est un sous-ensemble de $B$. C'est-à-dire, $Y \subseteq B$.
5.  Nous avons maintenant que $Y \subseteq A$ et $Y \subseteq B$. Cela signifie que tout élément de $Y$ est un élément de $A$, et tout élément de $Y$ est un élément de $B$.
    Soit $y$ un élément arbitraire tel que $y \in Y$.
    Puisque $Y \subseteq A$, il s'ensuit que $y \in A$.
    Puisque $Y \subseteq B$, il s'ensuit que $y \in B$.
6.  Puisque $y \in A$ et $y \in B$, par définition de l'intersection, $y \in A \cap B$.
7.  Comme ceci est vrai pour tout $y \in Y$, nous pouvons conclure que tout élément de $Y$ est un élément de $A \cap B$. Par conséquent, $Y \subseteq A \cap B$.
8.  Par définition de l'ensemble des parties, puisque $Y \subseteq A \cap B$, il s'ensuit que $Y \in \mathcal{P}(A \cap B)$.
9.  Ayant montré que tout $Y \in \mathcal{P}(A) \cap \mathcal{P}(B)$ implique $Y \in \mathcal{P}(A \cap B)$, nous avons démontré l'inclusion :
    $$ \mathcal{P}(A) \cap \mathcal{P}(B) \subseteq \mathcal{P}(A \cap B) $$

### Conclusion

Puisque nous avons démontré les deux inclusions :
1.  $\mathcal{P}(A \cap B) \subseteq \mathcal{P}(A) \cap \mathcal{P}(B)$
2.  $\mathcal{P}(A) \cap \mathcal{P}(B) \subseteq \mathcal{P}(A \cap B)$

Nous pouvons conclure que les deux ensembles sont égaux.
$$ \mathcal{P}(A \cap B) = \mathcal{P}(A) \cap \mathcal{P}(B) $$
La démonstration est achevée.
