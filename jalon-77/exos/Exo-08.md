# Exercice 8 : Séparabilité de $L^p(\mathbb{R})$

**Niveau :** \bigstar\bigstar\bigstar\bigstar\bigstar

**Énoncé :**
Un espace est séparable s'il admet une partie dénombrable dense.
Montrer que pour $1 \le p < +\infty$, $L^p(\mathbb{R})$ est séparable.
(Astuce : Utiliser la densité des fonctions en escalier, puis rationaliser les coefficients et les bornes).

**Correction Détaillée :**
1. **Étape 1 : Densité des fonctions en escalier**
   On sait que l'ensemble $\mathcal{E}$ des fonctions en escalier (combinaisons linéaires d'indicatrices d'intervalles bornés) est dense dans $L^p(\mathbb{R})$.
   Or $\mathcal{E}$ n'est pas dénombrable.

2. **Étape 2 : Restrictions rationnelles**
   Considérons le sous-ensemble $\mathcal{E}_{\mathbb{Q}}$ constitué des fonctions de la forme :
   $s(x) = \sum_{k=1}^m q_k \mathbf{1}_{[a_k, b_k]}(x)$
   où les coefficients $q_k \in \mathbb{Q}$, les bornes des intervalles $a_k, b_k \in \mathbb{Q}$, et $m \in \mathbb{N}$.
   L'ensemble $\mathcal{E}_{\mathbb{Q}}$ est une union dénombrable de produits finis d'ensembles dénombrables, il est donc dénombrable.

3. **Étape 3 : Densité de $\mathcal{E}_{\mathbb{Q}}$ dans $\mathcal{E}$**
   Soit $s \in \mathcal{E}$. Écrivons $s = \sum_{k=1}^m \alpha_k \mathbf{1}_{[A_k, B_k]}$.
   Pour tout $\varepsilon > 0$, on peut approcher chaque réel $\alpha_k$ par un rationnel $q_k$, et chaque réel $A_k, B_k$ par des rationnels $a_k, b_k$.
   En choisissant ces rationnels suffisamment proches, la norme $L^p$ de la différence s'écrit comme une somme d'aires de petits "décalages" horizontaux et verticaux.
   La norme $\|s - s_q\|_p$ peut être rendue arbitrairement petite.

4. **Étape 4 : Conclusion**
   Puisque $\mathcal{E}_{\mathbb{Q}}$ est dense dans $\mathcal{E}$, et que $\mathcal{E}$ est dense dans $L^p(\mathbb{R})$, par transitivité de la densité, $\mathcal{E}_{\mathbb{Q}}$ (qui est dénombrable) est dense dans $L^p(\mathbb{R})$. L'espace est séparable.
