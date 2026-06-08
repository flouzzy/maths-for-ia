# Exercice 5 : Fonction de croissance
**Énoncé :** Démontrer que pour la classe des demi-droites réelles $\mathcal{F} = \{ (-\infty, a] \}$, la fonction de croissance vaut $S_{\mathcal{F}}(n) = n + 1$.
**Correction Détaillée :**
* *Analyse de l'énoncé :* La fonction de croissance compte le nombre maximum de dichotomies réalisables sur $n$ points.
* *Résolution pas-à-pas :*
Soit $S = \{x_1, x_2, \dots, x_n\}$ un ensemble de $n$ points distincts dans $\mathbb{R}$. Supposons, sans perte de généralité, qu'ils sont ordonnés : $x_1 < x_2 < \dots < x_n$.
L'intersection de $(-\infty, a]$ avec $S$ dépend de la position de $a$ par rapport aux points de $S$. Les partitions possibles sont séparées par les valeurs de $a$ tombant entre les points $x_i$.
Les intervalles pertinents pour choisir $a$ sont :
1. $a < x_1$ : l'intersection est $\emptyset$. (1 sous-ensemble)
2. $x_1 \le a < x_2$ : l'intersection est $\{x_1\}$. (1 sous-ensemble)
3. $x_2 \le a < x_3$ : l'intersection est $\{x_1, x_2\}$. (1 sous-ensemble)
...
k. $x_k \le a < x_{k+1}$ : l'intersection est $\{x_1, x_2, \dots, x_k\}$.
...
n+1. $x_n \le a$ : l'intersection est $\{x_1, x_2, \dots, x_n\} = S$. (1 sous-ensemble)

Le nombre de zones délimitées par les $n$ points est exactement $n + 1$. Pour chaque zone, le choix de $a$ produit le même sous-ensemble de $S$. Le nombre de dichotomies distinctes que $\mathcal{F}$ peut réaliser sur $S$ est exactement $n + 1$.
Par définition, la fonction de croissance est le supremum sur tous les ensembles de $n$ points :
$$S_{\mathcal{F}}(n) = \sup_{S, |S|=n} | \{ S \cap (-\infty, a] \mid a \in \mathbb{R} \} | = n + 1.$$
Le résultat est prouvé. $\blacksquare$
