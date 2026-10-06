## Exercice 2 : Inégalité de Boole-Bonferroni simple
$\bigstar\star\star\star\star$

### Énoncé

Soient $A$ et $B$ deux événements d'un espace probabilisé $(\Omega, \mathcal{F}, \mathbb{P})$.
On donne $\mathbb{P}(A) = 0.9$ et $\mathbb{P}(B) = 0.8$.
1. Montrer rigoureusement que la probabilité de l'intersection $\mathbb{P}(A \cap B)$ est au moins égale à $0.7$.
2. Donner un exemple concret (avec un jeu de cartes par exemple) où cette borne inférieure est atteinte de façon exacte.


### Correction Détaillée

1. **Démonstration de la borne inférieure :**
D'après les axiomes de Kolmogorov, pour tout événement $E$, on a $\mathbb{P}(E) \le 1$.
En particulier pour l'union $A \cup B$, on a :
$\mathbb{P}(A \cup B) \le 1$

Or, par la formule de l'union (ou formule de Poincaré pour deux événements) :
$\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$

En substituant cette expression dans l'inégalité :
$\mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B) \le 1$

En isolant $\mathbb{P}(A \cap B)$, nous obtenons :
$\mathbb{P}(A \cap B) \ge \mathbb{P}(A) + \mathbb{P}(B) - 1$

Application numérique :
$\mathbb{P}(A \cap B) \ge 0.9 + 0.8 - 1 = 1.7 - 1 = 0.7$.
Ainsi, $\mathbb{P}(A \cap B) \ge 0.7$.

2. **Exemple où la borne est atteinte :**
Pour que $\mathbb{P}(A \cap B) = 0.7$, il faut que l'inégalité initiale soit une égalité, c'est-à-dire que $\mathbb{P}(A \cup B) = 1$.
Prenons une urne de $10$ boules numérotées de $1$ à $10$.
Soit $A = \{1, 2, 3, 4, 5, 6, 7, 8, 9\}$ (les $9$ premières boules, $\mathbb{P}(A) = 0.9$).
Soit $B = \{3, 4, 5, 6, 7, 8, 9, 10\}$ (les $8$ dernières boules, $\mathbb{P}(B) = 0.8$).
On a $A \cup B = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\} = \Omega$, donc $\mathbb{P}(A \cup B) = 1$.
Et $A \cap B = \{3, 4, 5, 6, 7, 8, 9\}$. Il y a exactement $7$ boules dans l'intersection.
Donc $\mathbb{P}(A \cap B) = \frac{7}{10} = 0.7$. La borne est exactement atteinte.
