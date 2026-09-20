# Exercice 9 : Inégalité de Jensen pour les espérances conditionnelles

**Difficulté :** ★★★★★


## Énoncé
Dans le cadre de la théorie probabiliste moderne, prouver l'inégalité de Jensen conditionnelle : si $\varphi$ est convexe et $X$ intégrable, alors pour toute sous-tribu $\mathcal{G}$, on a presque sûrement :
$$ \varphi(\mathbb{E}[X|\mathcal{G}]) \le \mathbb{E}[\varphi(X)|\mathcal{G}] $$

## Correction Détaillée
Toute fonction convexe $\varphi : \mathbb{R} \to \mathbb{R}$ peut s'écrire comme l'enveloppe supérieure d'une famille dénombrable de fonctions affines. Plus précisément, il existe des suites réelles $(a_n)_{n\in\mathbb{N}}$ et $(b_n)_{n\in\mathbb{N}}$ telles que pour tout $x \in \mathbb{R}$ :
$$ \varphi(x) = \sup_{n \in \mathbb{N}} (a_n x + b_n) $$
Pour un $n$ fixé, considérons l'inégalité triviale $a_n X + b_n \le \varphi(X)$.
L'opérateur d'espérance conditionnelle par rapport à $\mathcal{G}$ possède deux propriétés fondamentales : la croissance (monotonie) et la linéarité.
En appliquant l'espérance conditionnelle aux deux membres de l'inégalité, nous obtenons presque sûrement :
$$ \mathbb{E}[a_n X + b_n | \mathcal{G}] \le \mathbb{E}[\varphi(X) | \mathcal{G}] $$
Par linéarité de $\mathbb{E}[\cdot | \mathcal{G}]$ :
$$ a_n \mathbb{E}[X | \mathcal{G}] + b_n \le \mathbb{E}[\varphi(X) | \mathcal{G}] $$
Cette inégalité est vraie presque sûrement pour *chaque* $n \in \mathbb{N}$. L'union dénombrable d'ensembles de mesure nulle étant de mesure nulle, cette inégalité est vraie simultanément pour tous les $n$ presque sûrement.
Ainsi, nous pouvons prendre le supremum sur $n$ du côté gauche tout en conservant l'inégalité :
$$ \sup_{n \in \mathbb{N}} \left( a_n \mathbb{E}[X | \mathcal{G}] + b_n \right) \le \mathbb{E}[\varphi(X) | \mathcal{G}] \quad \text{p.s.} $$
Par définition de l'enveloppe affine, le terme de gauche n'est autre que l'évaluation de $\varphi$ en la variable aléatoire $\mathbb{E}[X | \mathcal{G}]$.
D'où le résultat final :
$$ \varphi(\mathbb{E}[X|\mathcal{G}]) \le \mathbb{E}[\varphi(X)|\mathcal{G}] \quad \text{p.s.} $$
La démonstration met en lumière la puissance de la dualité (fonction comme supremum de minorantes) couplée à la monotonie de l'intégrale.
