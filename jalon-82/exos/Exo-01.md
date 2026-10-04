# Exercice 1 : Action du Dirac translaté et linéarité
Difficulté : $\bigstar\star\star\star\star$

**Énoncé :**
Soit $\varphi(x) = e^{-x^2} \in \mathcal{D}(\mathbb{R})$.
On considère la distribution $T = 3\delta_2 - 5\delta_{-1}$.
Calculez rigoureusement $\langle T, \varphi \rangle$ en justifiant les étapes par les propriétés de linéarité des distributions et la définition de la distribution de Dirac.

**Correction Détaillée :**
1. La distribution $T$ est définie comme une combinaison linéaire de deux distributions de Dirac : $T = 3\delta_2 - 5\delta_{-1}$.
2. Par définition, l'espace des distributions $\mathcal{D}'(\mathbb{R})$ est un espace vectoriel. L'action d'une distribution sur une fonction test est linéaire.
3. Ainsi, pour toute fonction test $\varphi \in \mathcal{D}(\mathbb{R})$, nous avons :
   $$\langle T, \varphi \rangle = \langle 3\delta_2 - 5\delta_{-1}, \varphi \rangle = 3\langle \delta_2, \varphi \rangle - 5\langle \delta_{-1}, \varphi \rangle$$
4. Par définition de la distribution de Dirac translatée au point $a$, $\langle \delta_a, \varphi \rangle = \varphi(a)$.
5. Nous appliquons cette définition pour $a = 2$ et $a = -1$ :
   $$\langle T, \varphi \rangle = 3\varphi(2) - 5\varphi(-1)$$
6. Remplaçons $\varphi(x)$ par son expression $e^{-x^2}$ :
   $$\varphi(2) = e^{-(2)^2} = e^{-4}$$
   $$\varphi(-1) = e^{-(-1)^2} = e^{-1}$$
7. Le résultat final est donc :
   $$\langle T, \varphi \rangle = 3e^{-4} - 5e^{-1}$$
