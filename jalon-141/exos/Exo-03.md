# Exercice 3 : Union bound sur un ensemble fini de seuils
**Énoncé :** Considérons un ensemble fini de seuils $T = \{t_1, t_2, \dots, t_K\}$. On veut borner la déviation maximale entre la fonction de répartition empirique $F_n$ et réelle $F$ simultanément sur tous les points de cet ensemble. Démontrer que :
$$\mathbb{P}\left( \max_{t \in T} |F_n(t) - F(t)| \ge \epsilon \right) \le 2 K \exp(-2 n \epsilon^2)$$

**Correction Détaillée :**
* *Analyse de l'énoncé :* On doit passer de la borne ponctuelle (Exercice 2) à une borne uniforme sur un ensemble fini $T$ en utilisant l'inégalité de Boole (union bound).
* *Résolution pas-à-pas :*
  1. Définissons l'événement $A_k$ comme le fait que la déviation dépasse $\epsilon$ au point $t_k$ :
     $$A_k = \{ |F_n(t_k) - F(t_k)| \ge \epsilon \}$$
  2. L'événement que nous voulons borner est l'union de ces événements sur tous les indices $k \in \{1, \dots, K\}$ :
     $$\left\{ \max_{t \in T} |F_n(t) - F(t)| \ge \epsilon \right\} = \bigcup_{k=1}^K A_k$$
  3. L'inégalité de Boole (propriété de sous-additivité des mesures de probabilité) nous dit que la probabilité d'une union d'événements est inférieure ou égale à la somme de leurs probabilités :
     $$\mathbb{P}\left( \bigcup_{k=1}^K A_k \right) \le \sum_{k=1}^K \mathbb{P}(A_k)$$
  4. Or, d'après l'Exercice 2 (Inégalité de Hoeffding), nous savons que pour chaque $k$, $\mathbb{P}(A_k) \le 2 \exp(-2 n \epsilon^2)$.
  5. En sommant ces bornes identiques $K$ fois, on obtient le résultat :
     $$\mathbb{P}\left( \max_{t \in T} |F_n(t) - F(t)| \ge \epsilon \right) \le \sum_{k=1}^K 2 \exp(-2 n \epsilon^2) = 2 K \exp(-2 n \epsilon^2)$$
  Cette méthode met en évidence la difficulté pour passer à un supremum sur tout $\mathbb{R}$, car l'ensemble des seuils serait indénombrable.
