# Conditionnement et matrice de Vandermonde

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit un problème de régression au sens des moindres carrés où $f(w) = \frac{1}{2} \|Xw - y\|^2$, avec $X \in \mathbb{R}^{m \times n}$.
1. Démontrez formellement que la Hessienne de $f$ est $H_f(w) = X^T X$.
2. Si $X$ est une matrice mal conditionnée (dont les colonnes sont presque colinéaires), comment se traduit ce phénomène géométriquement sur la fonction $f$ via l'analyse de $H_f(w)$ ?

**Correction mathématique détaillée :**

1. **Développement et dérivées :**
   On peut développer $f(w) = \frac{1}{2} (Xw - y)^T (Xw - y) = \frac{1}{2} w^T X^T X w - y^T X w + \frac{1}{2} y^T y$.
   C'est une forme quadratique.
   Le gradient d'une forme quadratique $w^T A w$ est $2 A w$ (si $A$ symétrique). Ici $A = \frac{1}{2} X^T X$, donc :
   $$\nabla f(w) = X^T X w - X^T y = X^T(Xw - y)$$
   La Hessienne est la matrice jacobienne du gradient. L'application $w \mapsto X^T X w$ étant linéaire :
   $$H_f(w) = X^T X$$
   Cette matrice ne dépend pas de $w$ : $f$ est une vraie fonction quadratique dont la courbure est globale.

2. **Analyse spectrale géométrique :**
   Les courbures principales de la paraboloïde $f$ sont données par les valeurs propres de $X^T X$, qui sont les carrés des valeurs singulières de $X$.
   Si les colonnes de $X$ sont presque colinéaires, la plus petite valeur propre de $X^T X$ sera très proche de zéro, tandis que la plus grande sera grande.
   Géométriquement, la paraboloïde formera un "long ravin plat" le long du vecteur propre associé à la valeur propre proche de zéro. Le conditionnement (ratio $\lambda_{\text{max}} / \lambda_{\text{min}}$) sera immense.
