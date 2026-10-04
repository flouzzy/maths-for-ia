# Exercice 9 : Théorème de structure locale (Distribution à support ponctuel)
Difficulté : $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Un théorème fondamental de Schwartz affirme que toute distribution $T$ dont le support est réduit au point $\{0\}$ est nécessairement une combinaison linéaire finie de la masse de Dirac et de ses dérivées.
Soit $T \in \mathcal{D}'(\mathbb{R})$ d'ordre 1 tel que $\text{supp}(T) = \{0\}$.
Montrez qu'il existe deux constantes $c_0$ et $c_1$ telles que pour toute $\varphi \in \mathcal{D}(\mathbb{R})$ :
$$ \langle T, \varphi \rangle = c_0 \varphi(0) - c_1 \varphi'(0) $$
*Indication : Utilisez l'hypothèse de l'ordre 1 et construisez une fonction test auxiliaire astucieuse en utilisant un développement de Taylor à l'ordre 1.*

**Correction Détaillée :**
1. **Utilisation de l'hypothèse de l'ordre 1 :**
   Le théorème de continuité pour une distribution d'ordre $m=1$ dont le support est compact (ici $\{0\}$) indique qu'il existe une constante $C > 0$ telle que pour toute fonction test $\varphi \in \mathcal{D}(\mathbb{R})$ :
   $$ |\langle T, \varphi \rangle| \le C \left( \sup_{x \in \mathbb{R}} |\varphi(x)| + \sup_{x \in \mathbb{R}} |\varphi'(x)| \right) $$
   De plus, comme $\text{supp}(T) = \{0\}$, l'action de $T$ sur toute fonction test qui s'annule au voisinage de 0 est strictement nulle.

2. **Décomposition par Taylor-Lagrange :**
   Soit $\varphi \in \mathcal{D}(\mathbb{R})$ une fonction test quelconque.
   Isolons le comportement de $\varphi$ en 0 en définissant un "polynôme" de Taylor complété par une fonction plateau.
   Soit $\theta \in \mathcal{D}(\mathbb{R})$ une fonction "cut-off" valant 1 sur un petit voisinage $[-1, 1]$ de l'origine.
   On écrit la décomposition exacte :
   $$ \varphi(x) = \left[ \varphi(0) + x\varphi'(0) \right]\theta(x) + R(x) $$
   où le reste $R(x)$ est défini par : $R(x) = \varphi(x) - \left[ \varphi(0) + x\varphi'(0) \right]\theta(x)$.
   Remarquons que $R(x)$ est dans $\mathcal{D}(\mathbb{R})$ car cest une combinaison linéaire de fonctions infiniment dérivables à support compact.

3. **Analyse du Reste $R(x)$ au voisinage de 0 :**
   Pour $x \in [-1, 1]$, $\theta(x) = 1$, donc $R(x) = \varphi(x) - \varphi(0) - x\varphi'(0)$.
   Évaluons le reste et ses dérivées en $x=0$ :
   *   $R(0) = \varphi(0) - \varphi(0) - 0 = 0$.
   *   $R'(x) = \varphi'(x) - \varphi'(0)$ (toujours pour $x \in [-1,1]$), donc $R'(0) = \varphi'(0) - \varphi'(0) = 0$.

   Puisque $R(0) = 0$ et $R'(0) = 0$, et que la fonction est $C^\infty$, par la formule de Taylor, on a au voisinage de zéro : $|R(x)| \le K x^2$ et $|R'(x)| \le K' |x|$ pour certaines constantes.

4. **Action de $T$ sur le Reste :**
   Considérons une suite d'homothéties du reste : $R_n(x) = R(x) \chi(nx)$ où $\chi$ est une autre fonction "cut-off" valant 1 sur $[-1,1]$ et de support dans $[-2,2]$.
   La fonction $R_n$ a son support concentré autour de 0 (sur $[-2/n, 2/n]$).
   Comme le support de $T$ est $\{0\}$, l'action de $T$ sur $R$ est la même que sur la fonction $R$ restreinte au voisinage de zéro, on peut rigoureusement montrer que $\langle T, R \rangle = \lim_{n \to \infty} \langle T, R_n \rangle$.
   Appliquons la majoration de l'ordre 1 à $R_n$ :
   $|\langle T, R_n \rangle| \le C \left( \sup |R_n| + \sup |R'_n| \right)$.
   Or $\sup |R_n| \sim \sup_{|x|<2/n} |x^2| \sim 4/n^2 \to 0$.
   Et par la règle du produit, $R'_n(x) = R'(x)\chi(nx) + n R(x)\chi'(nx)$.
   $\sup |R'(x)\chi(nx)| \sim \sup_{|x|<2/n} |x| \sim 2/n \to 0$.
   $\sup |n R(x)\chi'(nx)| \sim n \cdot \sup_{|x|<2/n} x^2 \sim n \cdot 4/n^2 = 4/n \to 0$.
   Donc $\sup |R'_n| \to 0$.
   Ainsi, $|\langle T, R_n \rangle| \to 0$.
   Conclusion cruciale : $\langle T, R \rangle = 0$.

5. **Détermination de l'action de T sur $\varphi$ :**
   Reprenons la décomposition de l'étape 2 et appliquons la linéarité de $T$ :
   $$ \langle T, \varphi \rangle = \langle T, \varphi(0)\theta + \varphi'(0)(x\theta) + R \rangle $$
   $$ \langle T, \varphi \rangle = \varphi(0)\langle T, \theta \rangle + \varphi'(0)\langle T, x\theta \rangle + \langle T, R \rangle $$
   Comme $\langle T, R \rangle = 0$, il reste :
   $$ \langle T, \varphi \rangle = \varphi(0)\langle T, \theta \rangle + \varphi'(0)\langle T, x\theta \rangle $$
   Les quantités $\langle T, \theta \rangle$ et $\langle T, x\theta \rangle$ sont des constantes scalaires fixes indépendantes de $\varphi$.
   Posons $c_0 = \langle T, \theta \rangle$ et $c_1 = -\langle T, x\theta \rangle$.
   On obtient la formule finale :
   $$ \langle T, \varphi \rangle = c_0 \varphi(0) - c_1 \varphi'(0) $$
