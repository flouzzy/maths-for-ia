# Exercice 4 : Concentration de la distance au plus proche voisin (Niveau 4)

## Énoncé
Soient $X, X_1, \dots, X_n$ des variables aléatoires indépendantes et identiquement distribuées (i.i.d.) selon la loi uniforme sur le cube unité $[0, 1]^d$ en dimension $d$.
On s'intéresse à la distance minimale entre un point fixé $y \in [0, 1]^d$ et les points de notre échantillon aléatoire. Définissons la fonction :
$$f(X_1, \dots, X_n) = \min_{1 \le i \le n} \|X_i - y\|$$
où $\|\cdot\|$ désigne la norme euclidienne standard.
1. Montrer que $f$ satisfait la propriété des différences bornées et déterminer les constantes $c_i$ associées.
2. Établir une inégalité de concentration pour $f$.
3. Expliquer le lien avec la "malédiction de la dimension" en IA.

---

## Correction Détaillée

### 1. Propriété des différences bornées
Soient $x = (x_1, \dots, x_n) \in ([0, 1]^d)^n$ et $x^{(k)} = (x_1, \dots, x_{k-1}, x'_k, x_{k+1}, \dots, x_n) \in ([0, 1]^d)^n$ deux configurations de points ne différant que par le $k$-ème point.

Calculons la différence $f(x) - f(x^{(k)})$ :
$$f(x) - f(x^{(k)}) = \min_{1 \le i \le n} \|x_i - y\| - \min_{1 \le i \le n} \|x^{(k)}_i - y\|$$

Nous pouvons réécrire cela. Notons $d(x_i, y) = \|x_i - y\|$.
Rappelons la propriété classique du minimum : pour toutes suites réelles $u_i$ et $v_i$, on a $|\min_i u_i - \min_i v_i| \le \max_i |u_i - v_i|$.
Puisque les coordonnées de $x$ et $x^{(k)}$ ne diffèrent que pour $i=k$, le seul terme qui change dans le calcul du minimum est le $k$-ème terme.
D'où :
$$f(x) - f(x^{(k)}) \le \max_{1 \le i \le n} |d(x_i, y) - d(x^{(k)}_i, y)| = |d(x_k, y) - d(x'_k, y)|$$

Par l'inégalité triangulaire inverse pour la norme euclidienne, on a :
$$| \|x_k - y\| - \|x'_k - y\| | \le \|x_k - x'_k\|$$

Puisque les points $x_k$ et $x'_k$ sont dans le cube unité $[0, 1]^d$, la distance maximale entre deux points quelconques du cube est donnée par la longueur de la grande diagonale :
$$\|x_k - x'_k\| \le \sqrt{\sum_{j=1}^d (1 - 0)^2} = \sqrt{d}$$

Ainsi, pour tout $k \in \{1, \dots, n\}$ :
$$|f(x) - f(x^{(k)})| \le \sqrt{d}$$

La constante $c_k = \sqrt{d}$ est une borne uniforme. Cependant, nous pouvons obtenir une borne bien plus fine si nous restreignons notre espace. Mais au sens strict sur le cube $[0, 1]^d$, la constante de Lipschitz globale par rapport à chaque coordonnée dans la métrique euclidienne est effectivement bornée par le diamètre du cube, c'est-à-dire $c_k = \sqrt{d}$.

### 2. Inégalité de concentration
En utilisant les constantes $c_k = \sqrt{d}$ pour tout $k$, la somme des carrés donne :
$$\sum_{k=1}^n c_k^2 = n d$$

Par l'inégalité de McDiarmid, on en déduit que pour tout $t > 0$ :
$$\mathbb{P}\Big(|f(X) - \mathbb{E}[f(X)]| \ge t\Big) \le 2 \exp\left( - \frac{2 t^2}{n d} \right)$$

### 3. Lien avec la malédiction de la dimension en IA
En grande dimension (quand $d$ est grand), la constante de concentration devient très lâche car la borne contient le terme $d$ au dénominateur de l'exposant. 
En réalité, la distance moyenne au plus proche voisin dans $[0, 1]^d$ décroît avec $n$ comme $n^{-1/d}$. 
Quand la dimension $d \to \infty$, $n^{-1/d} \to 1$. Cela signifie que tous les points dans un espace de grande dimension ont tendance à être à la même distance les uns des autres (environ $\sqrt{d}/2$). La notion de "plus proche voisin" perd alors tout son sens discriminatoire, car la variance et les fluctuations de la distance deviennent négligeables par rapport à la distance moyenne elle-même. Les algorithmes basés sur les distances locales (comme les k-Plus Proches Voisins ou les noyaux RBF) souffrent énormément de ce phénomène géométrique décrit par la concentration.
