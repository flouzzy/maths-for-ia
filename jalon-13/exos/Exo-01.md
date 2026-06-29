```yaml
title: "Supremum et Infimum d'un Ensemble Fondamental"
difficulty: 1
tags: [Supremum, Infimum, Bornes, Nombres Réels]
```
## Énoncé de l'Exercice 01

Soit l'ensemble $A$ défini par :
$$ A = \left\{ (-1)^n \cdot \frac{n+1}{n} \mid n \in \mathbb{N}^* \right\} $$
où $\mathbb{N}^* = \{1, 2, 3, \ldots\}$ désigne l'ensemble des entiers naturels non nuls.

1.  Déterminer, si elles existent, la borne supérieure $\sup A$ et la borne inférieure $\inf A$ de l'ensemble $A$ dans $\mathbb{R}$.
2.  Pour chaque borne déterminée, justifier votre affirmation en utilisant les définitions précises de la borne supérieure et de la borne inférieure.

### Définitions Rappelées :

Pour un ensemble $S \subset \mathbb{R}$ non vide :
*   Un nombre réel $M$ est un **majorant** de $S$ si et seulement si pour tout $s \in S$, $s \le M$.
*   Un nombre réel $m$ est un **minorant** de $S$ si et seulement si pour tout $s \in S$, $s \ge m$.
*   La **borne supérieure** de $S$, notée $\sup S$, est le plus petit des majorants de $S$. Formellement, $s_0 = \sup S$ si et seulement si :
    1.  Pour tout $s \in S$, $s \le s_0$ ($s_0$ est un majorant de $S$).
    2.  Pour tout $\varepsilon \in \mathbb{R}$ tel que $\varepsilon > 0$, il existe $s_{\varepsilon} \in S$ tel que $s_{\varepsilon} > s_0 - \varepsilon$.
*   La **borne inférieure** de $S$, notée $\inf S$, est le plus grand des minorants de $S$. Formellement, $i_0 = \inf S$ si et seulement si :
    1.  Pour tout $s \in S$, $s \ge i_0$ ($i_0$ est un minorant de $S$).
    2.  Pour tout $\varepsilon \in \mathbb{R}$ tel que $\varepsilon > 0$, il existe $s_{\varepsilon} \in S$ tel que $s_{\varepsilon} < i_0 + \varepsilon$.

---