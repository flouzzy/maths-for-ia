---
title: "Exercice 8 : Distance de Hausdorff entre compacts"
---

### Exercice 8 : Distance de Hausdorff entre compacts \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $(X, d)$ un espace métrique. Pour tout compact non vide $A$ de $X$ et tout point $x \in X$, on définit la distance d'un point à un ensemble : $d(x, A) = \inf_{a \in A} d(x, a)$.
La distance de Hausdorff entre deux compacts non vides $A$ et $B$ est définie par :
$$d_H(A, B) = \max \left( \sup_{a \in A} d(a, B), \sup_{b \in B} d(b, A) \right)$$
Démontrer que si $d_H(A, B) = 0$, alors $A = B$. Pourquoi l'hypothèse de compacité (ou au moins d'être fermé) est-elle cruciale ?

**Correction Détaillée :**
Supposons que $d_H(A, B) = 0$. Par définition de la distance de Hausdorff (qui est un maximum de termes positifs ou nuls), cela implique que :
$$\sup_{a \in A} d(a, B) = 0 \quad \text{et} \quad \sup_{b \in B} d(b, A) = 0$$
Considérons la première condition : $\sup_{a \in A} d(a, B) = 0$.
Cela signifie que pour tout élément $a \in A$, on a $d(a, B) = 0$.
Par définition de la distance à un ensemble, on a donc $\inf_{b \in B} d(a, b) = 0$.
Puisque $B$ est un ensemble compact, la borne inférieure de la distance continue $x \mapsto d(a, x)$ sur $B$ est atteinte. Il existe donc au moins un élément $b_0 \in B$ tel que $d(a, b_0) = 0$.
Par l'axiome de séparation de la distance $d$, on en déduit que $a = b_0$, et par conséquent, $a \in B$.
Ceci étant valable pour tout $a \in A$, on a montré l'inclusion $A \subset B$.
Un raisonnement rigoureusement symétrique à partir de l'hypothèse $\sup_{b \in B} d(b, A) = 0$ montre que pour tout $b \in B$, il existe $a_0 \in A$ tel que $b=a_0$, d'où $B \subset A$.
Les deux inclusions réciproques impliquent l'égalité des ensembles : $A = B$.
**Rôle de la compacité/fermeture :** Si les ensembles n'étaient pas fermés, avoir $\inf_{b \in B} d(a, b) = 0$ signifierait seulement que $a$ est dans l'adhérence de $B$ (notée $\bar{B}$). Ainsi $d_H(A, B) = 0$ entraînerait seulement $\bar{A} = \bar{B}$. Par exemple, dans $\mathbb{R}$, pour $A=]0, 1[$ et $B=[0, 1]$, on a $d_H(A, B) = 0$ mais $A \neq B$. La compacité garantit que l'ensemble contient sa propre frontière, préservant ainsi l'axiome de séparation sur l'espace des parties compactes.
