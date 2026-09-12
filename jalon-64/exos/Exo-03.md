---
title: "Exercice 3 : Monotonie de la mesure extérieure"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

## Énoncé

La mesure extérieure doit respecter une propriété intuitive de "monotonie" : un sous-ensemble ne peut pas être "plus gros" que l'ensemble qui le contient.
Soient $A$ et $B$ deux parties de $\mathbb{R}$ telles que $A \subset B$.
Démontrer, directement à partir de la définition par les recouvrements, que :
$$\lambda^*(A) \le \lambda^*(B)$$

## Correction Détaillée

Si $\lambda^*(B) = +\infty$, l'inégalité $\lambda^*(A) \le +\infty$ est trivialement vérifiée. Supposons donc que $\lambda^*(B) < +\infty$.

Soit $\epsilon > 0$ un réel strictement positif.
Par définition de la mesure extérieure $\lambda^*(B)$ en tant qu'infimum de la somme des longueurs des recouvrements par des intervalles ouverts, par caractérisation de la borne inférieure, il existe un recouvrement de $B$ par une suite dénombrable d'intervalles ouverts $(I_n)_{n \in \mathbb{N}^*}$ telle que :
$$B \subset \bigcup_{n=1}^{+\infty} I_n \quad \text{et} \quad \sum_{n=1}^{+\infty} \ell(I_n) \le \lambda^*(B) + \epsilon$$

Puisque nous avons supposé comme hypothèse géométrique que $A \subset B$, l'inclusion est transitive vis-à-vis du recouvrement. On a donc :
$$A \subset B \subset \bigcup_{n=1}^{+\infty} I_n$$
Ainsi, la suite d'intervalles ouverts $(I_n)_{n \in \mathbb{N}^*}$ constitue également un recouvrement valide pour l'ensemble $A$.

La mesure extérieure de $A$ étant définie comme le plus grand minorant (infimum) sur **tous** les recouvrements possibles de $A$, elle est nécessairement inférieure ou égale à la somme des longueurs du recouvrement spécifique $(I_n)$ :
$$\lambda^*(A) \le \sum_{n=1}^{+\infty} \ell(I_n)$$

En combinant les inégalités, on obtient :
$$\lambda^*(A) \le \sum_{n=1}^{+\infty} \ell(I_n) \le \lambda^*(B) + \epsilon$$

Nous avons donc l'inégalité numérique :
$$\lambda^*(A) \le \lambda^*(B) + \epsilon$$
Cette inégalité algébrique est rigoureusement vraie pour tout réel $\epsilon > 0$. Par passage à la limite lorsque $\epsilon$ tend vers $0$ par valeurs supérieures, le terme $\epsilon$ disparaît, ce qui donne l'inégalité stricte ou large :
$$\lambda^*(A) \le \lambda^*(B)$$
Ce qui achève la démonstration de la monotonie de la mesure extérieure.
