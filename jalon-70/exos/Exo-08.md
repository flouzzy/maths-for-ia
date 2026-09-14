# Exercice 8 : Volume d'un Simplexe dans $\mathbb{R}^3$ (★★★★★)

**Énoncé :**
On considère le simplexe canonique de $\mathbb{R}^3$ :
$S = \{(x,y,z) \in \mathbb{R}^3 \mid x, y, z \geq 0 \text{ et } x+y+z \leq 1\}$.
Calculer la mesure produit (le volume de Lebesgue) de $S$ en réalisant l'intégration par sections de manière rigoureuse. (Indication : L'espace est $\mathbb{R} \times (\mathbb{R} \times \mathbb{R})$).

**Correction :**
1. La mesure produit sur $\mathbb{R}^3$ est $\lambda_3 = \lambda \otimes \lambda \otimes \lambda$. Par associativité, c'est aussi la mesure produit de la mesure $\lambda$ sur $\mathbb{R}$ (pour la variable $z$) et $\lambda_2$ sur $\mathbb{R}^2$ (pour les variables $x,y$).
2. Calculons le volume par sections le long de l'axe $z$.
   Fixons $z \in \mathbb{R}$. La section $S^z$ dans $\mathbb{R}^2$ (le plan $xy$) est :
   $S^z = \{(x,y) \in \mathbb{R}^2 \mid x,y \geq 0 \text{ et } x+y \leq 1-z\}$.
   - Si $z \notin [0,1]$, alors la condition est impossible à satisfaire, $S^z = \emptyset$ (son aire est 0).
   - Si $z \in [0,1]$, $S^z$ est un triangle rectangle isocèle dans $\mathbb{R}^2$ dont les cathètes mesurent $1-z$.
3. La mesure (aire bidimensionnelle) de $S^z$ est $\lambda_2(S^z) = \frac{1}{2}(1-z)^2$.
4. Le volume total s'obtient en intégrant l'aire des sections par rapport à $z$ (par le théorème sur la mesure produit) :
   $\lambda_3(S) = \int_{\mathbb{R}} \lambda_2(S^z) \, d\lambda(z) = \int_0^1 \frac{1}{2}(1-z)^2 \, dz$.
5. On calcule l'intégrale :
   $\int_0^1 \frac{1}{2}(1-z)^2 \, dz = \left[ -\frac{1}{6}(1-z)^3 \right]_0^1 = 0 - (-\frac{1}{6} \cdot 1^3) = \frac{1}{6}$.
   Le volume du simplexe standard en dimension 3 est bien $1/6$. L'utilisation de la mesure produit permet une formalisation impeccable de la méthode de "l'intégration par tranches" de Cavalieri.
