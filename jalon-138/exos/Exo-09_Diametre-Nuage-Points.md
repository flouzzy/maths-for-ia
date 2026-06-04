# Exercice 9 : Concentration du diamètre d'un nuage de points aléatoires (Niveau 9)

## Énoncé
Soient $X_1, \dots, X_n$ des variables aléatoires indépendantes à valeurs dans la boule unité fermée $\mathcal{B} = \{ x \in \mathbb{R}^d \mid \|x\|_2 \le 1 \}$ en dimension $d$.
On définit le diamètre de ce nuage de points par :
$$\Delta(X_1, \dots, X_n) = \max_{1 \le i, j \le n} \|X_i - X_j\|_2$$
1. Montrer que la fonction $\Delta$ satisfait la propriété des différences bornées et déterminer les constantes $c_k$.
2. Établir une inégalité de concentration pour $\Delta$.
3. Montrer que ce diamètre se concentre de manière beaucoup plus forte lorsque $n \to \infty$ que les distances individuelles entre points.

---

## Correction Détaillée

### 1. Propriété des différences bornées
Soient $x = (x_1, \dots, x_n) \in \mathcal{B}^n$ et $x^{(k)} = (x_1, \dots, x_{k-1}, x'_k, x_{k+1}, \dots, x_n) \in \mathcal{B}^n$ deux configurations de points ne différant que par le point $k$.

Soit $\Delta(x) = \max_{1 \le i, j \le n} \|x_i - x_j\|_2$.
Supposons sans perte de généralité que le maximum pour la configuration modifiée $x^{(k)}$ soit atteint pour une paire d'indices $(p, q)$.
$$\Delta(x^{(k)}) = \|x^{(k)}_p - x^{(k)}_q\|_2$$

Plusieurs cas se présentent selon que l'indice perturbé $k$ est impliqué ou non dans cette paire optimale :
- **Cas 1 : $k \neq p$ et $k \neq q$.**
Dans ce cas, les points réalisant le diamètre de $x^{(k)}$ n'ont pas été modifiés. D'où :
$$\Delta(x^{(k)}) = \|x_p - x_q\|_2 \le \Delta(x)$$
ce qui donne immédiatement :
$$\Delta(x^{(k)}) - \Delta(x) \le 0 \le 2$$

- **Cas 2 : $k = p$ (ou par symétrie $k = q$).**
Dans ce cas, le diamètre de la configuration modifiée fait intervenir le point perturbé $x'_k$ :
$$\Delta(x^{(k)}) = \|x'_k - x^{(k)}_q\|_2$$
Par l'inégalité triangulaire euclidienne :
$$\|x'_k - x^{(k)}_q\|_2 \le \|x'_k - x_k\|_2 + \|x_k - x_q\|_2$$

Puisque $\|x_k - x_q\|_2$ fait intervenir deux points de la configuration originale $x$, sa longueur est inférieure ou égale au diamètre original :
$$\|x_k - x_q\|_2 \le \Delta(x)$$
De plus, les points $x_k$ et $x'_k$ appartiennent tous deux à la boule unité fermée $\mathcal{B}$. Le diamètre de la boule unité étant égal à 2, on a :
$$\|x'_k - x_k\|_2 \le 2$$
D'où :
$$\Delta(x^{(k)}) \le 2 + \Delta(x) \implies \Delta(x^{(k)}) - \Delta(x) \le 2$$

Par une symétrie parfaite des rôles (en remplaçant $x'_k$ par $x_k$), nous obtenons l'inégalité inverse :
$$\Delta(x) - \Delta(x^{(k)}) \le 2$$

Nous en déduisons que pour tout $k \in \{1, \dots, n\}$ :
$$|\Delta(x) - \Delta(x^{(k)})| \le 2$$

La fonction $\Delta$ satisfait la propriété des différences bornées de McDiarmid avec les constantes uniformes $c_k = 2$ pour tout $k \in \{1, \dots, n\}$.

### 2. Inégalité de concentration
La somme des carrés des constantes est :
$$\sum_{k=1}^n c_k^2 = \sum_{k=1}^n 2^2 = 4 n$$

Par application directe de l'inégalité de McDiarmid à la variable aléatoire $\Delta(X_1, \dots, X_n)$, nous obtenons pour tout $t > 0$ :
$$\mathbb{P}\Big(|\Delta(X) - \mathbb{E}[\Delta(X)]| \ge t\Big) \le 2 \exp\left( - \frac{2 t^2}{4 n} \right) = 2 \exp\left( - \frac{t^2}{2 n} \right)$$

### 3. Discussion sur la force de la concentration
Cette inégalité de concentration montre que les fluctuations du diamètre du nuage de points sont au plus d'ordre $\sqrt{n}$ (l'écart-type est majoré par $\sqrt{n}$).
Cependant, à mesure que le nombre de points $n$ devient extrêmement grand, le diamètre $\Delta(X)$ de points tirés aléatoirement dans la boule unité va converger presque sûrement vers le diamètre théorique maximal de la boule, c'est-à-dire 2 (si la distribution des points a un support complet dans la boule).
La variance du diamètre s'amenuise et le diamètre se stabilise très rapidement. Ce résultat est fondamental dans l'analyse des algorithmes de clustering (comme les K-Means) ou dans le calcul des enveloppes convexes de grands ensembles de données en IA.
