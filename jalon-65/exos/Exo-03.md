---
uuid: "jalon-65-exo-03"
title: "Exercice 3 : Supremum d'une famille non dénombrable"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 3 : Supremum d'une famille non dénombrable

## Énoncé

Soit $(f_t)_{t \in [0, 1]}$ une famille non dénombrable de fonctions mesurables de $\mathbb{R}$ dans $\mathbb{R}$. La fonction $g(x) = \sup_{t \in [0, 1]} f_t(x)$ est-elle nécessairement mesurable ? Prouvez-le ou donnez un contre-exemple.

## Solution Détaillée

Non, elle n'est pas nécessairement mesurable. Le supremum d'une famille non dénombrable de fonctions mesurables peut être non mesurable. Considérons un ensemble de Vitali $V \subset [0, 1]$ non borélien. Définissons pour chaque $t \in V$ la fonction constante $f_t(x) = 1$ si $x = t$ et $0$ sinon, et pour $t \notin V$, $f_t(x) = 0$. Chaque $f_t$ est la fonction indicatrice d'un point ou de l'ensemble vide, donc mesurable (borélienne). Cependant, $g(x) = \sup_{t \in [0, 1]} f_t(x) = \mathbb{1}_V(x)$. Comme $V$ n'est pas mesurable, la fonction indicatrice $\mathbb{1}_V$ n'est pas mesurable. $\blacksquare$
