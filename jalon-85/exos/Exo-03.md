## Exercice 3 : Sous-additivité pour une suite d'événements
$\bigstar\bigstar\star\star\star$

### Énoncé

Montrer rigoureusement par récurrence l'inégalité de Boole (ou borne de l'union) pour $n$ événements $(A_1, \dots, A_n)$ :
$$ \mathbb{P}\left(\bigcup_{i=1}^n A_i\right) \le \sum_{i=1}^n \mathbb{P}(A_i) $$
Ensuite, justifier que cela reste vrai pour une union dénombrable infinie (inégalité $\sigma$-sous-additive) en utilisant le théorème de continuité monotone croissante.


### Correction Détaillée

**Démonstration par récurrence pour l'union finie :**

**Initialisation :**
Pour $n=1$, l'inégalité s'écrit $\mathbb{P}(A_1) \le \mathbb{P}(A_1)$, ce qui est trivialement vrai avec égalité.
Pour $n=2$, par la formule de l'union, nous avons :
$\mathbb{P}(A_1 \cup A_2) = \mathbb{P}(A_1) + \mathbb{P}(A_2) - \mathbb{P}(A_1 \cap A_2)$.
Puisque $\mathbb{P}(A_1 \cap A_2) \ge 0$ (premier axiome de Kolmogorov : positivité de la mesure de probabilité), nous en déduisons :
$\mathbb{P}(A_1 \cup A_2) \le \mathbb{P}(A_1) + \mathbb{P}(A_2)$.

**Hérédité :**
Supposons l'inégalité vraie au rang $n$. Soient $n+1$ événements.
$\mathbb{P}\left(\bigcup_{i=1}^{n+1} A_i\right) = \mathbb{P}\left(\left(\bigcup_{i=1}^n A_i\right) \cup A_{n+1}\right)$.
Appliquons l'inégalité au rang $2$ avec l'événement $U_n = \bigcup_{i=1}^n A_i$ et $A_{n+1}$ :
$\mathbb{P}(U_n \cup A_{n+1}) \le \mathbb{P}(U_n) + \mathbb{P}(A_{n+1})$.
Par l'hypothèse de récurrence, $\mathbb{P}(U_n) \le \sum_{i=1}^n \mathbb{P}(A_i)$.
Ainsi :
$\mathbb{P}\left(\bigcup_{i=1}^{n+1} A_i\right) \le \sum_{i=1}^n \mathbb{P}(A_i) + \mathbb{P}(A_{n+1}) = \sum_{i=1}^{n+1} \mathbb{P}(A_i)$.
La propriété est héréditaire, donc vraie pour tout $n \ge 1$.

**Généralisation à l'union dénombrable infinie :**
Soit $(A_n)_{n \ge 1}$ une suite infinie d'événements.
Posons $B_n = \bigcup_{i=1}^n A_i$.
La suite $(B_n)$ est une suite croissante d'événements car $B_1 \subset B_2 \subset B_3 \dots$
Sa limite (union sur tous les entiers) est $B = \bigcup_{i=1}^\infty A_i$.
Par le théorème de continuité croissante (axiome de $\sigma$-additivité étendu), on a :
$\mathbb{P}(B) = \lim_{n \to \infty} \mathbb{P}(B_n)$.
Or, pour tout $n$, d'après le résultat précédent :
$\mathbb{P}(B_n) \le \sum_{i=1}^n \mathbb{P}(A_i)$.
En passant à la limite quand $n \to \infty$ (la limite préserve les inégalités larges) :
$\mathbb{P}\left(\bigcup_{i=1}^\infty A_i\right) \le \lim_{n \to \infty} \sum_{i=1}^n \mathbb{P}(A_i) = \sum_{i=1}^\infty \mathbb{P}(A_i)$.
L'inégalité est démontrée dans le cas dénombrable.
