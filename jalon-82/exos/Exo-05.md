# Exercice 5 : Produit d'une distribution par une fonction lisse
Difficulté : $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $T \in \mathcal{D}'(\mathbb{R})$ une distribution et $\alpha \in C^\infty(\mathbb{R})$ une fonction indéfiniment dérivable.
On définit le produit $\alpha T$ par son action sur toute fonction test $\varphi \in \mathcal{D}(\mathbb{R})$ par :
$$ \langle \alpha T, \varphi \rangle = \langle T, \alpha \varphi \rangle $$
1. Justifiez rigoureusement pourquoi cette définition a un sens mathématique.
2. Calculez explicitement l'action de la distribution $x \delta_0$ sur une fonction test quelconque et simplifiez. Que peut-on conclure sur la distribution $x \delta_0$ ?

**Correction Détaillée :**
1. **Justification de la définition du produit :**
   Pour que l'expression $\langle T, \alpha \varphi \rangle$ ait un sens, il est impératif que la fonction $\alpha \varphi$ appartienne à l'espace des fonctions tests $\mathcal{D}(\mathbb{R})$.
   Vérifions les deux conditions d'appartenance à $\mathcal{D}(\mathbb{R})$ pour $\psi = \alpha \varphi$ :
   *   **Régularité :** Par hypothèse, $\alpha \in C^\infty(\mathbb{R})$ et $\varphi \in C^\infty(\mathbb{R})$. Le produit de deux fonctions indéfiniment dérivables est indéfiniment dérivable (formule de Leibniz). Donc $\psi \in C^\infty(\mathbb{R})$.
   *   **Support compact :** Le support du produit est inclus dans l'intersection des supports. $\text{supp}(\alpha \varphi) \subset \text{supp}(\alpha) \cap \text{supp}(\varphi) \subset \text{supp}(\varphi)$.
       Comme $\varphi \in \mathcal{D}(\mathbb{R})$, son support est compact. Or, tout sous-ensemble fermé d'un compact est compact dans $\mathbb{R}$. Le support de $\psi$ est donc fermé (par définition du support) et borné (inclus dans le compact $\text{supp}(\varphi)$), il est donc compact.
   Ainsi, $\alpha \varphi \in \mathcal{D}(\mathbb{R})$. La forme linéaire agissant par $\varphi \mapsto \langle T, \alpha \varphi \rangle$ est bien définie (et on peut montrer qu'elle est continue), donc $\alpha T$ est bien une distribution.

2. **Calcul de $x \delta_0$ :**
   Soit $\varphi \in \mathcal{D}(\mathbb{R})$. En appliquant la définition précédente avec $\alpha(x) = x$ et $T = \delta_0$ :
   $$ \langle x \delta_0, \varphi \rangle = \langle \delta_0, x \varphi \rangle $$
   Par définition de l'action de la masse de Dirac en 0, elle évalue la fonction test à l'origine $x=0$. La fonction test ici est la fonction $g(x) = x \varphi(x)$.
   $$ \langle \delta_0, g \rangle = g(0) = 0 \cdot \varphi(0) = 0 $$
   Nous obtenons donc que pour toute fonction test $\varphi$, l'action de $x \delta_0$ renvoie 0.
   En théorie des distributions, l'égalité de deux distributions signifie l'égalité de leur action sur toute fonction test.
   Nous pouvons donc conclure de manière formelle que :
   $$ x \delta_0 = 0 $$
