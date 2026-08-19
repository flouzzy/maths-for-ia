# Exercice 10 : Paradoxe de l'ensemble de Vitali

**Difficulté :** $\displaystyle \\bigstar\\bigstar\\bigstar$

## Énoncé

L'ensemble de Vitali $V \subset [0, 1]$ est construit de sorte que pour tout rationnel $q \in [-1, 1]$, les translations $V_q = V+q$ soient disjointes, et $\bigcup_{q \in \mathbb{Q} \cap [-1, 1]} V_q \supset [0, 1]$. Expliquer étape par étape pourquoi la tribu des parties mesurables $\mathcal{L}(\mathbb{R})$ ne peut pas être égale à $\mathcal{P}(\mathbb{R})$.

## Correction Détaillée

1. Supposons par l'absurde que $\mathcal{L}(\mathbb{R}) = \mathcal{P}(\mathbb{R})$. Alors tout sous-ensemble de $\mathbb{R}$ admet une mesure de Lebesgue $\lambda$, et en particulier l'ensemble de Vitali $V$.
2. Les ensembles $V_q$ pour $q \in \mathbb{Q} \cap [-1, 1]$ sont dénombrables et disjoints 2 à 2. La mesure de Lebesgue est $\sigma$-additive.
3. Posons $S = \bigcup_q V_q$. Par $\sigma$-additivité, $\lambda(S) = \sum_q \lambda(V_q)$.
4. Par invariance par translation, $\lambda(V_q) = \lambda(V)$. La somme devient $\lambda(S) = \sum_{q} \lambda(V)$.
5. Evaluons cette somme : si $\lambda(V) = 0$, alors $\lambda(S) = 0$. Si $\lambda(V) = c > 0$, alors une somme infinie de constantes strictement positives diverge, donc $\lambda(S) = +\infty$.
6. D'un autre côté, par construction géométrique, on a $[0, 1] \subset S \subset [-1, 2]$. Par monotonie, $\lambda([0, 1]) \le \lambda(S) \le \lambda([-1, 2])$, ce qui donne $1 \le \lambda(S) \le 3$.
7. C'est une contradiction fatale : $\lambda(S)$ doit valoir entre 1 et 3, mais nos calculs d'additivité donnent soit 0 soit $+\infty$.
Conclusion : La supposition initiale est fausse. $V$ ne peut pas appartenir à la tribu sur laquelle $\lambda$ est définie.
