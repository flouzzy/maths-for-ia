---
uuid: "jalon-83"
title: "Dérivation au sens des distributions"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 82 (Introduction à la théorie des distributions de Schwartz).md]]"
next: "[[Jalon 84 (Livrable IA).md]]"
---

# 1. Introduction et Genèse

La dérivation est le concept fondateur de l'analyse, introduit par Newton et Leibniz pour mesurer des taux de variation (vitesses, pentes). Cependant, l'opération classique de dérivation est extrêmement exigeante : elle réclame que le graphe de la fonction soit lisse, sans rupture de pente ni saut brutal. Face aux lois physiques qui présentent des discontinuités fondamentales – comme la répartition de densité d'un milieu hétérogène (changement de phase), le front d'une onde de choc (acoustique) ou le potentiel électrique aux bornes d'un condensateur – la dérivée classique s'effondre.

Le génie de la théorie des distributions de Laurent Schwartz (fin des années 1940) est d'avoir étendu le domaine de validité de la dérivation. Comment dériver l'indérivable ? L'idée provient de la formule d'intégration par parties. Si l'on ne peut pas dériver un signal "rugueux" $T$, on le multiplie par une fonction "test" $\phi$ infiniment douce, puis on intègre. Au lieu de faire peser l'opérateur de dérivation sur $T$, on bascule la dérivée sur la fonction test $\phi$, moyennant un changement de signe.

Ainsi, dans l'univers des distributions, tout objet devient indéfiniment dérivable. Les sauts discontinus (comme la fonction de Heaviside) donnent naissance à des impulsions (distribution de Dirac), ouvrant la voie à la résolution rigoureuse des équations aux dérivées partielles fondamentales de la physique (chaleur, ondes, Maxwell). Plus tard, Sobolev exploitera cette dérivée "faible" pour bâtir des espaces fonctionnels (les espaces de Sobolev $H^s$) qui sont aujourd'hui l'ossature théorique de l'analyse fonctionnelle et du calcul des variations moderne.

# 2. Définitions, Théorèmes et Exemples Concrets

## 2.1. Définition de la dérivation d'une distribution

Soit $\Omega$ un ouvert de $\mathbb{R}^n$, $\mathcal{D}(\Omega)$ l'espace des fonctions tests (fonctions $C^\infty$ à support compact) et $\mathcal{D}'(\Omega)$ l'espace des distributions sur $\Omega$.

Rappelons que pour une fonction $f \in C^1(\Omega)$ et une fonction test $\phi \in \mathcal{D}(\Omega)$, la formule de Stokes (ou l'intégration par parties en 1D) stipule, en raison de l'annulation de $\phi$ sur le bord du domaine (car à support compact), que :
$$ \int_{\Omega} \partial_i f(x) \phi(x) \, dx = - \int_{\Omega} f(x) \partial_i \phi(x) \, dx $$
En notation des distributions, cela s'écrit $\langle T_{\partial_i f}, \phi \rangle = - \langle T_f, \partial_i \phi \rangle$. Cette formule algébrique ne fait plus appel à la dérivabilité de $f$.

**Définition (Dérivation au sens des distributions) :**
Pour toute distribution $T \in \mathcal{D}'(\Omega)$, on définit sa dérivée partielle d'ordre $i$ par rapport à la coordonnée $x_i$, notée $\partial_i T$, par son action sur n'importe quelle fonction test $\phi \in \mathcal{D}(\Omega)$ :
$$ \langle \partial_i T, \phi \rangle = - \langle T, \partial_i \phi \rangle $$

Cette définition garantit que $\partial_i T$ est une forme linéaire continue sur $\mathcal{D}(\Omega)$, donc elle-même une distribution.

**Théorème Fondamental :**
Toute distribution est infiniment dérivable au sens des distributions. En particulier, toute fonction $L^1_{loc}(\Omega)$ possède des dérivées de tout ordre dans $\mathcal{D}'(\Omega)$.

## 2.2. Le Sceau de l'Heaviside et l'Impulsion de Dirac

Le cas 1D le plus célèbre concerne la fonction échelon de Heaviside $H(x)$, définie par $H(x) = 1$ si $x > 0$, et $H(x) = 0$ si $x \le 0$. Cette fonction présente un saut d'amplitude 1 en $x = 0$.

**Exemple Concret :**
Calculons la dérivée de $H$ au sens des distributions.
Pour toute fonction test $\phi \in \mathcal{D}(\mathbb{R})$ :
$$ \langle H', \phi \rangle = - \langle H, \phi' \rangle = - \int_{\mathbb{R}} H(x) \phi'(x) \, dx $$
$$ = - \int_0^{+\infty} 1 \cdot \phi'(x) \, dx = - [\phi(x)]_0^{+\infty} $$
Comme $\phi$ est à support compact, $\lim_{x \to +\infty} \phi(x) = 0$. Donc :
$$ \langle H', \phi \rangle = - (0 - \phi(0)) = \phi(0) $$
Or, par définition, l'évaluation de $\phi$ en 0 est l'action de la masse de Dirac $\delta_0$.
Ainsi, l'égalité fondamentale est démontrée :
$$ H' = \delta_0 \text{ au sens de } \mathcal{D}'(\mathbb{R}) $$

**Interprétation Géométrique :** La dérivée d'une fonction avec un saut est nulle là où elle est constante, et égale à un Dirac centré au point de discontinuité, pondéré par la hauteur du saut.

## 2.3. Introduction aux Espaces de Sobolev $H^1(\mathbb{R})$

Dériver dans $\mathcal{D}'$ donne toujours un résultat, mais ce résultat n'est plus forcément une "vraie" fonction. Souvent, pour résoudre des équations de physique (qui impliquent l'énergie), on souhaite que la dérivée soit encore de carré intégrable.

**Définition (Espace de Sobolev $H^1$) :**
L'espace de Sobolev $H^1(\mathbb{R})$ (ou $W^{1,2}(\mathbb{R})$) est l'ensemble des fonctions $f \in L^2(\mathbb{R})$ dont la dérivée première au sens des distributions $f'$ est également une fonction de $L^2(\mathbb{R})$.
$$ H^1(\mathbb{R}) = \{ f \in L^2(\mathbb{R}) \mid f' \in L^2(\mathbb{R}) \} $$
Cet espace est muni du produit scalaire : $\langle f, g \rangle_{H^1} = \langle f, g \rangle_{L^2} + \langle f', g' \rangle_{L^2}$. C'est un espace de Hilbert fondamental pour les EDP.

**Cas Limite :**
La fonction $f(x) = e^{-|x|}$ appartient à $H^1(\mathbb{R})$. Bien qu'elle possède une "pointe" en 0 (non dérivable classiquement), sa dérivée distributionnelle $f'(x) = -\text{sgn}(x) e^{-|x|}$ ne génère pas de Dirac (car il n'y a pas de saut, la fonction est continue) et $f'$ appartient bien à $L^2$. En revanche, l'échelon de Heaviside n'est pas dans $H^1$ car $\delta_0 \notin L^2$.

# 3. Démonstrations

**Théorème (Formule des sauts 1D) :**
Soit $f : \mathbb{R} \to \mathbb{R}$ une fonction de classe $C^1$ par morceaux, avec un unique point de discontinuité de première espèce en $a \in \mathbb{R}$. Soit $\sigma = f(a^+) - f(a^-)$ le saut de la fonction en $a$. Soit $\{f'\}$ la dérivée usuelle de $f$ (définie partout sauf en $a$).
Alors la dérivée distributionnelle $f'$ est donnée par :
$$ f' = \{f'\} + \sigma \delta_a $$

**Démonstration Rigoureuse ligne par ligne :**
Soit $\phi \in \mathcal{D}(\mathbb{R})$ une fonction test. Par définition de la dérivée distributionnelle :
$$ \langle f', \phi \rangle = - \langle f, \phi' \rangle = - \int_{\mathbb{R}} f(x) \phi'(x) \, dx $$
On découpe l'intégrale au point de discontinuité $a$ :
$$ = - \left( \int_{-\infty}^{a} f(x) \phi'(x) \, dx + \int_{a}^{+\infty} f(x) \phi'(x) \, dx \right) $$
Sur chaque intervalle $]-\infty, a[$ et $]a, +\infty[$, la fonction $f$ est de classe $C^1$. On peut appliquer l'intégration par parties usuelle. De plus, $\phi$ s'annule à l'infini :
Pour le premier terme :
$$ \int_{-\infty}^{a} f(x) \phi'(x) \, dx = [f(x)\phi(x)]_{-\infty}^{a^-} - \int_{-\infty}^{a} \{f'(x)\} \phi(x) \, dx = f(a^-)\phi(a) - \int_{-\infty}^{a} \{f'(x)\} \phi(x) \, dx $$
Pour le second terme :
$$ \int_{a}^{+\infty} f(x) \phi'(x) \, dx = [f(x)\phi(x)]_{a^+}^{+\infty} - \int_{a}^{+\infty} \{f'(x)\} \phi(x) \, dx = - f(a^+)\phi(a) - \int_{a}^{+\infty} \{f'(x)\} \phi(x) \, dx $$
En additionnant les deux intégrations par parties et en réintroduisant le signe moins initial :
$$ \langle f', \phi \rangle = - \left( f(a^-)\phi(a) - f(a^+)\phi(a) - \int_{-\infty}^{a} \{f'\} \phi - \int_{a}^{+\infty} \{f'\} \phi \right) $$
$$ \langle f', \phi \rangle = (f(a^+) - f(a^-))\phi(a) + \int_{\mathbb{R}} \{f'(x)\} \phi(x) \, dx $$
$$ \langle f', \phi \rangle = \sigma \langle \delta_a, \phi \rangle + \langle \{f'\}, \phi \rangle $$
Puisque cette égalité est vraie pour toute fonction test $\phi$, on conclut dans $\mathcal{D}'(\mathbb{R})$ que :
$$ f' = \{f'\} + \sigma \delta_a \quad \blacksquare $$

# 4. Applications en Physique, Logique et Intelligence Artificielle

La théorie de la dérivation des distributions donne un sens mathématique aux "Solutions Faibles".
En mécanique des fluides et en dynamique des gaz, les ondes de choc se forment à cause de la non-linéarité des équations de Navier-Stokes ou de Burgers. À travers le front de choc, la pression et la densité subissent des sauts discontinus. Les équations différentielles de base (conservation de la masse, quantité de mouvement) n'ont plus de sens au sens classique sur ce front. En revanche, en les écrivant au sens des distributions, la formule des sauts redonne instantanément les relations de Rankine-Hugoniot, fondement de l'aérodynamique supersonique.

Dans le domaine de l'Intelligence Artificielle, la théorie de l'apprentissage profond (Deep Learning) repose sur le calcul massif des gradients de fonctions de coût pour la Rétropropagation (Backpropagation). Cependant, l'une des fonctions d'activation les plus utilisées, la ReLU (Rectified Linear Unit), définie par $f(x) = \max(0, x)$, n'est pas dérivable en 0.
Grâce à la théorie des distributions, sa dérivée est parfaitement définie globalement : $f'(x) = H(x)$ (l'échelon de Heaviside). Si l'on demande la dérivée seconde de l'activation (nécessaire dans les méthodes d'optimisation d'ordre 2 comme Newton ou le calcul du Hessien), on obtient exactement le Dirac $\delta_0$. Le formalisme de Sobolev $H^1$ permet d'ailleurs de garantir que les réseaux de neurones (vus comme des approximations dans l'espace de Sobolev) minimisent le risque structurel et ne sur-ajustent pas, via des pénalités de régularisation (Weight Decay) qui correspondent mathématiquement à borner la norme $H^1$ de la fonction approchée.
