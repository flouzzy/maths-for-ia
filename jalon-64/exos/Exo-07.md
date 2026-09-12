---
title: "Exercice 7 : Ensembles de type G_delta et régularité extérieure"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

## Énoncé

Dans l'espace topologique usuel de $\mathbb{R}$, un ensemble est de type $G_\delta$ ("G-delta") s'il peut s'écrire comme l'intersection dénombrable d'ensembles ouverts.
Démontrer un théorème de régularité extérieure fondamental : pour toute partie $A \subset \mathbb{R}$, il existe un sous-ensemble $G$ de type $G_\delta$ tel que $A \subset G$ et vérifiant :
$$\lambda(G) = \lambda^*(A)$$
*(Remarque: La notation $\lambda(G)$ est valide car tout ouvert est mesurable, donc toute intersection dénombrable d'ouverts l'est aussi par structure de tribu).*

## Correction Détaillée

Nous distinguerons le cas où la mesure extérieure est finie du cas infini.

**Cas 1 : La mesure extérieure est infinie ($\lambda^*(A) = +\infty$).**
Le choix le plus trivial pour $G$ est de prendre l'espace tout entier $G = \mathbb{R}$.
L'espace $\mathbb{R}$ est un ouvert (donc de type $G_\delta$).
De plus, $A \subset \mathbb{R}$ et $\lambda(\mathbb{R}) = +\infty = \lambda^*(A)$. Le théorème est vérifié dans ce cas trivial.

**Cas 2 : La mesure extérieure est finie ($\lambda^*(A) < +\infty$).**
Pour tout entier $n \ge 1$, nous prenons un seuil d'erreur $\epsilon_n = \frac{1}{n}$.
Par définition de la mesure extérieure de $A$ via l'infimum, il existe une suite dénombrable d'intervalles ouverts $(I_{n,k})_{k \ge 1}$ constituant un recouvrement de $A$ avec une approximation serrée :
$$A \subset \bigcup_{k=1}^{+\infty} I_{n,k} \quad \text{et} \quad \sum_{k=1}^{+\infty} \ell(I_{n,k}) \le \lambda^*(A) + \frac{1}{n}$$

Posons $O_n = \bigcup_{k=1}^{+\infty} I_{n,k}$.
L'ensemble $O_n$, en tant qu'union (même dénombrable) d'intervalles ouverts, est intrinsèquement un ensemble ouvert de $\mathbb{R}$.
Par construction du recouvrement, on a la garantie géométrique que pour tout $n \ge 1$, $A \subset O_n$.
Par sous-additivité de la mesure, nous avons la majoration :
$$\lambda(O_n) \le \sum_{k=1}^{+\infty} \lambda(I_{n,k}) = \sum_{k=1}^{+\infty} \ell(I_{n,k}) \le \lambda^*(A) + \frac{1}{n}$$

Définissons maintenant l'ensemble d'approximation ultime $G$ comme l'intersection de tous ces ouverts concentriques englobant $A$ :
$$G = \bigcap_{n=1}^{+\infty} O_n$$
Par définition topologique, $G$ est rigoureusement un ensemble de type $G_\delta$.
Puisque chaque $O_n$ contient $A$, l'intersection infinie conserve évidemment cette inclusion, donc $A \subset G$.

Il reste à démontrer l'égalité des mesures.
Par la propriété de monotonie démontrée dans l'exercice 3, l'inclusion $A \subset G$ force l'inégalité mineure :
$$\lambda^*(A) \le \lambda(G)$$

Pour l'inégalité inverse, notons que par construction $G \subset O_n$ pour tout entier $n \ge 1$. Par conséquent :
$$\lambda(G) \le \lambda(O_n) \le \lambda^*(A) + \frac{1}{n}$$
Cette chaîne d'inégalités est mathématiquement robuste et vraie pour tout entier strictement positif $n$.
En appliquant le théorème de passage à la limite lorsque $n \to +\infty$ (ce qui annule le terme $1/n$), nous obtenons l'inégalité majeure :
$$\lambda(G) \le \lambda^*(A)$$

La jonction de ces deux inégalités inébranlables conduit à l'égalité absolue cherchée :
$$\lambda(G) = \lambda^*(A)$$
Ceci démontre que toute partie de $\mathbb{R}$ possède une "enveloppe" topologique mesurable de type $G_\delta$ qui capture exactement sa "taille" volumétrique asymptotique.
