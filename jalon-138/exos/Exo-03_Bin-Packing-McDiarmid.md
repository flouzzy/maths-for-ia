# Exercice 3 : Application de McDiarmid au problème de Bin Packing (Niveau 3)

## Énoncé
Dans le problème classique du *bin packing*, on cherche à ranger $n$ objets de poids aléatoires $X_1, \dots, X_n$ dans un nombre minimal de boîtes (bins) de capacité maximale égale à 1.
On suppose que les poids $X_1, \dots, X_n$ sont des variables aléatoires indépendantes à valeurs dans l'intervalle $[0, 1]$.
Soit $B(X_1, \dots, X_n)$ le nombre minimal de boîtes de capacité 1 nécessaires pour ranger ces objets.
1. Montrer que la fonction $B$ satisfait la propriété des différences bornées et déterminer les constantes $c_i$.
2. Établir une inégalité de concentration pour le nombre de boîtes nécessaires autour de sa moyenne théorique.

---

## Correction Détaillée

### 1. Propriété des différences bornées
Soient $x = (x_1, \dots, x_n) \in [0, 1]^n$ et $x^{(i)} = (x_1, \dots, x_{i-1}, x'_i, x_{i-1}, \dots, x_n) \in [0, 1]^n$ deux configurations de poids d'objets ne différant que par le poids du $i$-ème objet.

Soit $B(x)$ le nombre minimal de boîtes nécessaires pour emballer les objets de poids $x_1, \dots, x_n$.
Supposons que nous ayons une configuration d'emballage optimale pour $x$, utilisant $B(x)$ boîtes. Si nous remplaçons le poids $x_i$ par $x'_i$ :
- Dans le pire des cas, le changement de poids de l'objet $i$ fait qu'il ne rentre plus dans sa boîte d'origine (par exemple si $x'_i > x_i$ et que la boîte était déjà presque pleine). Nous pouvons alors simplement sortir l'objet $i$ de sa boîte et le placer seul dans une nouvelle boîte supplémentaire. Cela nécessite au plus $B(x) + 1$ boîtes.
- Ainsi, le nombre minimal de boîtes nécessaires pour la configuration modifiée vérifie :
$$B(x^{(i)}) \le B(x) + 1 \implies B(x^{(i)}) - B(x) \le 1$$

Par une symétrie parfaite des rôles, en inversant la modification (remplacement de $x'_i$ par $x_i$), on obtient de la même manière :
$$B(x) \le B(x^{(i)}) + 1 \implies B(x) - B(x^{(i)}) \le 1$$

En combinant ces deux inégalités unilatérales, nous établissons que pour tout $i \in \{1, \dots, n\}$ et pour toutes valeurs de poids :
$$|B(x) - B(x^{(i)})| \le 1$$

La fonction $B$ satisfait donc la propriété des différences bornées de McDiarmid avec les constantes uniformes :
$$c_i = 1 \quad \forall i \in \{1, \dots, n\}$$

### 2. Borne de concentration de McDiarmid
Calculons la somme des carrés des constantes :
$$\sum_{i=1}^n c_i^2 = \sum_{i=1}^n 1^2 = n$$

En appliquant directement le théorème de McDiarmid à la variable aléatoire $B(X_1, \dots, X_n)$ (qui est une fonction mesurable des variables indépendantes $X_i$), nous obtenons pour tout $t > 0$ :
$$\mathbb{P}\Big(|B(X) - \mathbb{E}[B(X)]| \ge t\Big) \le 2 \exp\left( - \frac{2 t^2}{n} \right)$$

### Conclusion
Ce résultat montre que, bien que calculer la valeur exacte de $B(X)$ soit un problème NP-difficile en informatique théorique, sa valeur se concentre de manière extrêmement forte autour de sa moyenne théorique. Les fluctuations du nombre de boîtes optimales sont d'un ordre de grandeur de $\sqrt{n}$ au maximum, ce qui permet de prédire les besoins de stockage dans de grands systèmes logistiques de manière très stable.
