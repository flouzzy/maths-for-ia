## Exercice 8 : L'inégalité de Bonferroni Généralisée
$\bigstar\bigstar\bigstar\bigstar\star$

### Énoncé

Soient $A_1, A_2, \dots, A_n$ des événements. Posons $S_1 = \sum_{i=1}^n \mathbb{P}(A_i)$ et $S_2 = \sum_{1 \le i < j \le n} \mathbb{P}(A_i \cap A_j)$.
Démontrer que :
$$ \mathbb{P}\left(\bigcup_{i=1}^n A_i\right) \ge S_1 - S_2 $$
*Indication : Procéder par récurrence sur n en utilisant la formule de l'union à chaque étape.*


### Correction Détaillée

**Démonstration par récurrence :**

**Initialisation :**
Pour $n=1$, l'inégalité s'écrit $\mathbb{P}(A_1) \ge \mathbb{P}(A_1) - 0$, ce qui est vrai avec égalité.
Pour $n=2$, l'inégalité s'écrit $\mathbb{P}(A_1 \cup A_2) \ge \mathbb{P}(A_1) + \mathbb{P}(A_2) - \mathbb{P}(A_1 \cap A_2)$. En fait, d'après la formule de l'union, il y a égalité exacte. La propriété est donc vraie au rang $2$.

**Hérédité :**
Supposons l'inégalité vraie au rang $n$. Montrons-la au rang $n+1$.
Posons $U_n = \bigcup_{i=1}^n A_i$. On s'intéresse à $\mathbb{P}(U_n \cup A_{n+1})$.
Par la formule de l'union pour deux événements :
$\mathbb{P}(U_n \cup A_{n+1}) = \mathbb{P}(U_n) + \mathbb{P}(A_{n+1}) - \mathbb{P}(U_n \cap A_{n+1})$.

Par hypothèse de récurrence, $\mathbb{P}(U_n) \ge \sum_{i=1}^n \mathbb{P}(A_i) - \sum_{1 \le i < j \le n} \mathbb{P}(A_i \cap A_j)$.
Remplaçons dans l'équation :
$\mathbb{P}(U_n \cup A_{n+1}) \ge \sum_{i=1}^{n+1} \mathbb{P}(A_i) - \sum_{1 \le i < j \le n} \mathbb{P}(A_i \cap A_j) - \mathbb{P}(U_n \cap A_{n+1})$.  **(Équation $\star$)**

Maintenant, nous devons majorer le terme soustractif $\mathbb{P}(U_n \cap A_{n+1})$.
L'événement $U_n \cap A_{n+1}$ peut s'écrire, par distributivité de l'intersection sur l'union :
$U_n \cap A_{n+1} = \left(\bigcup_{i=1}^n A_i\right) \cap A_{n+1} = \bigcup_{i=1}^n (A_i \cap A_{n+1})$.
Appliquons l'inégalité de Boole (ou sous-additivité) à cette union :
$\mathbb{P}(U_n \cap A_{n+1}) = \mathbb{P}\left(\bigcup_{i=1}^n (A_i \cap A_{n+1})\right) \le \sum_{i=1}^n \mathbb{P}(A_i \cap A_{n+1})$.

Comme ce terme est soustrait dans l'équation $\star$, une majoration de $\mathbb{P}(U_n \cap A_{n+1})$ donne une minoration de la différence globale :
$- \mathbb{P}(U_n \cap A_{n+1}) \ge - \sum_{i=1}^n \mathbb{P}(A_i \cap A_{n+1})$.

En substituant dans $\star$, nous obtenons :
$\mathbb{P}(U_n \cup A_{n+1}) \ge \sum_{i=1}^{n+1} \mathbb{P}(A_i) - \sum_{1 \le i < j \le n} \mathbb{P}(A_i \cap A_j) - \sum_{i=1}^n \mathbb{P}(A_i \cap A_{n+1})$.
Les deux derniers termes se regroupent exactement pour former toutes les paires $\mathbb{P}(A_i \cap A_j)$ pour $1 \le i < j \le n+1$. En effet, le dernier terme ajoute toutes les paires impliquant le nouvel élément $A_{n+1}$.
Ainsi :
$\mathbb{P}\left(\bigcup_{i=1}^{n+1} A_i\right) \ge \sum_{i=1}^{n+1} \mathbb{P}(A_i) - \sum_{1 \le i < j \le n+1} \mathbb{P}(A_i \cap A_j)$.
L'inégalité est prouvée par récurrence. Cette minoration est très utilisée en statistiques pour les tests multiples.
