---
title: "Exercice 3 : Polynôme minimal d'une symétrie"
difficulty: 2
---

# Exercice 3 : Polynôme minimal d'une symétrie (★★☆☆☆)

## Énoncé

Soit $E$ un $\mathbb{K}$-espace vectoriel. Un endomorphisme $s \in \mathcal{L}(E)$ est appelé une symétrie si $s^2 = \text{id}_E$.
Soit $s$ une symétrie non triviale (c'est-à-dire $s \neq \text{id}_E$ et $s \neq -\text{id}_E$).
La définition axiomatique d'une symétrie vectorielle est que l'endomorphisme composé deux fois avec lui-même redonne l'identité :
$$ s \circ s = s^2 = \text{id}_E $$
Cette relation algébrique fondamentale se réécrit en passant tous les termes du même côté de l'égalité :
$$ s^2 - \text{id}_E = 0_{\mathcal{L}(E)} $$

Déterminer le polynôme minimal de $s$.

## Solution Rigoureuse

Par définition de la symétrie, nous avons $s^2 = \text{id}_E$, ce qui peut se réécrire sous la forme :
$$s^2 - \text{id}_E = 0_{\mathcal{L}(E)}$$
Considérons le polynôme $P(X) = X^2 - 1 \in \mathbb{K}[X]$. En évaluant ce polynôme en $s$, nous obtenons $P(s) = s^2 - \text{id}_E = 0_{\mathcal{L}(E)}$.
Ainsi, $P$ est un polynôme annulateur de $s$.

Le polynôme minimal $\pi_s$ engendre l'idéal annulateur de $s$. Par conséquent, $\pi_s$ divise tout polynôme annulateur de $s$. En particulier, $\pi_s$ divise $P(X) = X^2 - 1 = (X - 1)(X + 1)$.

Puisque les polynômes unitaires qui divisent $(X-1)(X+1)$ sont exactement $1$, $X-1$, $X+1$, et $(X-1)(X+1)$, examinons chacun de ces cas :
1. Si $\pi_s(X) = 1$, alors $\pi_s(s) = \text{id}_E$. Or $\text{id}_E \neq 0_{\mathcal{L}(E)}$ car $E$ n'est pas l'espace nul. Donc $\pi_s(X) \neq 1$.
2. Si $\pi_s(X) = X - 1$, alors $\pi_s(s) = s - \text{id}_E = 0_{\mathcal{L}(E)}$, ce qui implique $s = \text{id}_E$. Or, l'énoncé stipule que $s$ est non triviale ($s \neq \text{id}_E$). Donc $\pi_s(X) \neq X - 1$.
3. Si $\pi_s(X) = X + 1$, alors $\pi_s(s) = s + \text{id}_E = 0_{\mathcal{L}(E)}$, ce qui implique $s = -\text{id}_E$. Or, l'énoncé stipule que $s \neq -\text{id}_E$. Donc $\pi_s(X) \neq X + 1$.

Puisque $\pi_s$ divise $(X-1)(X+1)$ et qu'il n'est égal à aucun de ses diviseurs stricts propres, il s'ensuit par élimination rigoureuse que le polynôme minimal de $s$ est le polynôme lui-même :
$$\pi_s(X) = X^2 - 1$$
