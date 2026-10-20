# Exercice 8 : La méthode du moment de Berry-Esseen pour des dés \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $X$ la variable aléatoire représentant le résultat du lancer d'un dé équilibré à 6 faces. On lance le dé $n$ fois et on note $S_n$ la somme des résultats.
1. Calculer les moments $\mathbb{E}[X]$, $\mathbb{E}[X^2]$, $\text{Var}(X)$ et le moment absolu centré d'ordre 3, $\rho = \mathbb{E}[|X - \mu|^3]$.
2. Déduire une borne supérieure explicite de l'erreur d'approximation du Théorème Central Limite donnée par le théorème de Berry-Esseen pour $n=100$. (Prendre la constante $C=0.4748$).

**Correction :**

1. La loi de $X$ est une loi uniforme discrète sur $\{1, 2, 3, 4, 5, 6\}$.
$\mu = \mathbb{E}[X] = \frac{1+2+3+4+5+6}{6} = \frac{21}{6} = 3.5$.
$\mathbb{E}[X^2] = \frac{1^2+2^2+3^2+4^2+5^2+6^2}{6} = \frac{91}{6}$.
$\sigma^2 = \text{Var}(X) = \mathbb{E}[X^2] - \mu^2 = \frac{91}{6} - \frac{49}{4} = \frac{182 - 147}{12} = \frac{35}{12} \approx 2.9167$.
L'écart-type est $\sigma = \sqrt{35/12} \approx 1.7078$.

Calculons le moment absolu centré d'ordre 3 : $\rho = \mathbb{E}[|X - 3.5|^3]$.
Les valeurs possibles de $|X - 3.5|$ sont :
- Pour $x \in \{3, 4\}$ : $|3 - 3.5| = |4 - 3.5| = 0.5$
- Pour $x \in \{2, 5\}$ : $|2 - 3.5| = |5 - 3.5| = 1.5$
- Pour $x \in \{1, 6\}$ : $|1 - 3.5| = |6 - 3.5| = 2.5$
La probabilité de chaque paire est $2/6 = 1/3$.
Ainsi :
$\rho = \frac{1}{3} \left( (0.5)^3 + (1.5)^3 + (2.5)^3 \right) = \frac{1}{3} \left( 0.125 + 3.375 + 15.625 \right) = \frac{1}{3} (19.125) = 6.375$.

2. Borne de Berry-Esseen :
L'inégalité garantit que l'erreur entre la fonction de répartition de $Z_n$ et celle de la loi normale est au plus :
$$\Delta \le \frac{C \rho}{\sigma^3 \sqrt{n}}$$
Avec $n=100$, on a $\sqrt{n} = 10$.
$\sigma^3 = (35/12)^{3/2} \approx (1.7078)^3 \approx 4.981$.
Donc :
$$\Delta \le \frac{0.4748 \times 6.375}{4.981 \times 10} = \frac{3.02685}{49.81} \approx 0.0608$$
Ainsi, l'approximation du TCL pour 100 lancers de dé garantit une erreur absolue sur les probabilités cumulées au maximum d'environ $6.08\%$.
