---
uuid: jalon-83-exo-10
title: "Exercice 10 - Dérivation des distributions"
---

# Exercice 10 $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
En électrostatique 3D, le potentiel $V(r)$ créé par une charge ponctuelle $q$ placée à l'origine vérifie l'équation de Poisson :
$$ \Delta V = -\frac{q}{\varepsilon_0} \delta_0 $$
On donne que, en dehors de l'origine ($r > 0$), le Laplacien s'écrit en coordonnées sphériques pour un champ à symétrie radiale $V(r)$ :
$$ \Delta V = \frac{1}{r} \frac{d^2}{dr^2} (r V) $$
1. En dehors de l'origine ($r \neq 0$), quelle équation différentielle usuelle vérifie le champ $V$ ?
2. Résoudre cette équation pour trouver la forme de $V(r)$ à une constante près (le potentiel de Coulomb).
3. (Difficile, hors calcul explicite) : Pourquoi le calcul brut du Laplacien usuel sur la fonction trouvée en 2. donnerait 0 partout, rendant l'équation de Poisson fausse sans la théorie des distributions ?

**Correction pas à pas :**
1. En dehors de l'origine, l'équation de Poisson indique que la densité de charge (le membre de droite) est nulle, car la masse de Dirac $\delta_0$ a son support réduit au point $\{0\}$.
Donc sur $\mathbb{R}^3 \setminus \{0\}$, le potentiel vérifie l'équation de Laplace homogène :
$$ \Delta V = 0 $$
En utilisant la forme radiale donnée :
$$ \frac{1}{r} \frac{d^2}{dr^2} (r V(r)) = 0 $$

2. Puisque $r \neq 0$, cela équivaut à :
$$ \frac{d^2}{dr^2} (r V(r)) = 0 $$
En intégrant deux fois par rapport à $r$ :
$$ r V(r) = C_1 r + C_2 \implies V(r) = C_1 + \frac{C_2}{r} $$
La constante $C_1$ représente un potentiel de fond constant, que l'on fixe généralement à 0 (condition aux limites à l'infini pour une charge localisée). Donc $V(r) = \frac{C_2}{r}$. C'est la forme bien connue du potentiel de Coulomb.

3. Si l'on applique l'opérateur Laplacien *au sens classique* à la fonction $V(r) = 1/r$, le calcul partout où la fonction est de classe $C^2$ (donc pour tout $r>0$) donnerait exactement $0$, comme calculé au point 1.
En $r=0$, la fonction n'est pas définie (elle diverge), donc le Laplacien classique n'a pas de sens. L'équation de la physique serait "\Delta V = 0 presque partout, et indéfini en 0", ce qui est incapable de représenter formellement la charge électrique $q$.
La théorie des distributions vient corriger cela : la distribution associée à $1/r$ dans $\mathbb{R}^3$ (intégrable au voisinage de l'origine grâce à l'élément de volume $4\pi r^2 dr$) possède un Laplacien distributionnel. Le calcul rigoureux (faisant intervenir le théorème de flux-divergence sur une petite sphère évidée autour de 0) montre que $\Delta (1/r) = -4\pi \delta_0$. C'est ce pic infiniment concentré qui matérialise mathématiquement la charge ponctuelle $q$ dans l'équation de Poisson, réconciliant l'électromagnétisme de Maxwell et l'analyse fonctionnelle. $\blacksquare$
