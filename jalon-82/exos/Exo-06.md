# Exercice 6 : Produit d'une distribution par une fonction C-infinie
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
Soit $T \in \mathcal{D}'(\mathbb{R})$ et $\alpha \in C^\infty(\mathbb{R})$. On définit le produit $\alpha T$ par $\langle \alpha T, \varphi \rangle = \langle T, \alpha\varphi \rangle$. Calculer $x \cdot \delta_0$ et $x \cdot \text{vp}(1/x)$.

## Correction Détaillée
1. Calculons d'abord le produit $x \cdot \delta_0$. Soit $\varphi \in \mathcal{D}(\mathbb{R})$ une fonction test quelconque.
2. Par la définition du produit d'une distribution par une fonction $C^\infty$, posons $\alpha(x) = x$. On a :
   $$ \langle x \cdot \delta_0, \varphi \rangle = \langle \delta_0, \alpha\varphi \rangle $$
3. L'action du Dirac en 0 consiste à évaluer la fonction à l'intérieur du crochet en $x=0$.
   $$ \langle \delta_0, \alpha\varphi \rangle = (\alpha\varphi)(0) = \alpha(0)\varphi(0) $$
4. Puisque $\alpha(x) = x$, on a $\alpha(0) = 0$. Donc :
   $$ 0 \times \varphi(0) = 0 $$
5. Ceci étant vrai pour toute fonction test $\varphi$, on conclut que la distribution $x \cdot \delta_0$ est la distribution nulle : $x \cdot \delta_0 = 0$.

6. Calculons maintenant $x \cdot \text{vp}(1/x)$. Pour $\varphi \in \mathcal{D}(\mathbb{R})$ :
   $$ \langle x \cdot \text{vp}(1/x), \varphi \rangle = \langle \text{vp}(1/x), x\varphi \rangle $$
7. Par définition de la Valeur Principale :
   $$ \langle \text{vp}(1/x), x\varphi \rangle = \lim_{\epsilon \to 0^+} \int_{|x| > \epsilon} \frac{x\varphi(x)}{x} \,dx $$
8. On simplifie la fraction pour $x \neq 0$ :
   $$ \lim_{\epsilon \to 0^+} \int_{|x| > \epsilon} \varphi(x) \,dx $$
9. La fonction $\varphi$ étant continue et à support compact, elle est intégrable sur $\mathbb{R}$. La limite de l'intégrale sur $\{|x| > \epsilon\}$ correspond simplement à l'intégrale de Lebesgue complète sur $\mathbb{R}$ (puisque le point 0 est de mesure nulle) :
   $$ \int_{\mathbb{R}} \varphi(x) \,dx = \langle T_1, \varphi \rangle $$
10. La distribution $x \cdot \text{vp}(1/x)$ est donc égale à la distribution constante $1$ (régulière). $x \cdot \text{vp}(1/x) = 1$.
