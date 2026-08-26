---
title: "Exercice 04 : Homogénéité de l'intégrale"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 04 : Homogénéité de l'intégrale

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré, $f : X \to [0, +\infty]$ mesurable, et $c > 0$ une constante réelle.
Montrez, en utilisant strictement la définition par le supremum, que $\int_X (c \cdot f) \, d\mu = c \cdot \int_X f \, d\mu$.

### Correction détaillée

1. L'intégrale de la fonction $c \cdot f$ est définie par :
   $$ I = \int_X (cf) \, d\mu = \sup \left\lbrace \int_X s \, d\mu \ \middle| \ s \in \mathcal{E}_+, 0 \le s \le cf \right\rbrace $$
2. Si $s$ est une fonction simple positive telle que $0 \le s \le cf$, alors la fonction $\frac{1}{c} s$ est également une fonction simple positive, et elle vérifie $0 \le \frac{1}{c} s \le f$.
   Posons $t = \frac{1}{c} s$. Il est élémentaire de vérifier sur l'expression canonique des fonctions simples que l'intégrale est linéaire, donc $\int_X s \, d\mu = \int_X (ct) \, d\mu = c \int_X t \, d\mu$.
3. L'ensemble sur lequel on prend le supremum pour $I$ peut donc s'écrire :
   $$ \left\lbrace c \int_X t \, d\mu \ \middle| \ t \in \mathcal{E}_+, 0 \le t \le f \right\rbrace $$
4. Les propriétés de la borne supérieure (supremum) affirment que pour tout ensemble de réels $A$ et tout scalaire positif $c$, $\sup(c \cdot A) = c \cdot \sup(A)$.
5. En appliquant ceci à notre ensemble :
   $$ I = c \cdot \sup \left\lbrace \int_X t \, d\mu \ \middle| \ t \in \mathcal{E}_+, 0 \le t \le f \right\rbrace $$
6. Or, ce supremum est par définition l'intégrale de $f$. On a donc :
   $$ \int_X (cf) \, d\mu = c \int_X f \, d\mu $$
