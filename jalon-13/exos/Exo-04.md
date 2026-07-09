```yaml
title: "Distinction entre Maximum et Borne Supérieure"
difficulty: 2
tags: [Supremum, Maximum, Ensemble Borné]
```
## Énoncé de l'Exercice 04

Soit $A$ un sous-ensemble non vide de $\mathbb{R}$.

Démontrer rigoureusement l'équivalence suivante :
L'ensemble $A$ possède un maximum (c'est-à-dire $\max A$ existe dans $\mathbb{R}$) si et seulement si l'ensemble $A$ possède une borne supérieure dans $\mathbb{R}$ (c'est-à-dire $\sup A$ existe) ET cette borne supérieure appartient à l'ensemble $A$ (c'est-à-dire $\sup A \in A$).

Votre démonstration doit explicitement utiliser les définitions formelles du maximum et de la borne supérieure.

### Définitions Rappelées :


* de l'ensemble $A$ (noté $\max A$) si et seulement si $M_A \in A$ ET pour tout $x \in A$, $x \le M_A$.

* de l'ensemble $A$ (notée $\sup A$) si et seulement si :
    1.  Pour tout $x \in A$, $x \le s_A$ ($s_A$ est un majorant de $A$).
    2.  Pour tout $\varepsilon \in \mathbb{R}$ tel que $\varepsilon > 0$, il existe $x_{\varepsilon} \in A$ tel que $x_{\varepsilon} > s_A - \varepsilon$.

---