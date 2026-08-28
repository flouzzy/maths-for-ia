# Majoration par l'intégrale de Lebesgue

**Difficulté :** $\star\star\star\star☆$

## Énoncé

Montrez rigoureusement (en utilisant la définition par supremum) que pour une fonction mesurable $f \geq 0$ et une constante $c \geq 0$, on a $\int_X cf \, d\mu = c \int_X f \, d\mu$. (On supposera $c > 0$, le cas $c=0$ étant trivial).

---

## Correction détaillée

Soit $g = cf$. Par définition : $\int_X g \, d\mu = \sup \{ \int_X s \, d\mu \mid s \in \mathcal{E}^+, 0 \leq s \leq cf \} $.
Pour toute $s \in \mathcal{E}^+$, $0 \leq s \leq cf \iff 0 \leq \frac{1}{c}s \leq f$. Or, si $s \in \mathcal{E}^+$, alors $t = \frac{1}{c}s \in \mathcal{E}^+$, et par linéarité de l'intégrale sur $\mathcal{E}^+$ (vue en cours), $\int_X s \, d\mu = c \int_X t \, d\mu$.
L'ensemble dont on prend le supremum se réécrit alors :
$$ \left\{ c \int_X t \, d\mu \mid t \in \mathcal{E}^+, 0 \leq t \leq f \right\} $$
En factorisant la constante $c > 0$ hors du supremum :
$$ \sup \left\{ c \int_X t \, d\mu \right\} = c \sup \left\{ \int_X t \, d\mu \right\} = c \int_X f \, d\mu $$
