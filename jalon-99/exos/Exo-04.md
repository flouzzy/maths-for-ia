# Exercice 4 : Fonctionnelles sous-linéaires $\bigstar\bigstar\star\star\star$

## Énoncé
Soit $E$ un espace vectoriel. Une fonction $p: E \to \mathbb{R}$ est sous-linéaire. Démontrer que $p(0) = 0$ et $p(-x) \geq -p(x)$.

## Correction Complète
Par définition d'une fonction sous-linéaire $p$, on a :
1) $p(x + y) \leq p(x) + p(y)$ (sous-additivité)
2) $p(\lambda x) = \lambda p(x)$ pour tout $\lambda \geq 0$ (homogénéité positive)
Prenons $x = 0$ et $\lambda = 2$. L'homogénéité donne $p(0) = p(2 \cdot 0) = 2p(0)$.
En soustrayant $p(0)$ de chaque côté, on trouve :
$p(0) = 0$.
Ensuite, considérons l'évaluation au vecteur nul en le décomposant : $0 = x + (-x)$.
Par sous-additivité :
$p(0) = p(x - x) \leq p(x) + p(-x)$.
Puisque $p(0) = 0$, on obtient :
$0 \leq p(x) + p(-x) \implies p(-x) \geq -p(x)$.
Ceci démontre que toute fonction sous-linéaire engendre des jauges symétriques. $\blacksquare$
