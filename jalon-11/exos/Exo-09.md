# Exercice 9: Indépendance de vecteurs via l'espace dual
## Énoncé
Soient $u, v \in E$. Montrer que $u$ et $v$ sont linéairement indépendants si et seulement s'il existe $\varphi \in E^*$ telle que $\varphi(u) = 1$ et $\varphi(v) = 0$.


## Correction détaillée
**Sens indirect :**
Supposons qu'il existe une forme linéaire $\varphi \in E^*$ telle que $\varphi(u) = 1$ et $\varphi(v) = 0$.
Soient $\lambda, \mu \in \mathbb{K}$ tels que $\lambda u + \mu v = 0_E$.
Appliquons la forme linéaire $\varphi$ à cette équation :
$\varphi(\lambda u + \mu v) = \varphi(0_E)$
Par linéarité de $\varphi$, on obtient :
$\lambda \varphi(u) + \mu \varphi(v) = 0$
En substituant les valeurs :
$\lambda(1) + \mu(0) = 0 \implies \lambda = 0$.
Si $\lambda = 0$, alors $\mu v = 0_E$. Comme $\varphi(v) = 0$, $v$ ne peut pas être le vecteur nul (sinon l'indépendance est impossible). De plus, on peut invoquer une seconde forme pour isoler $\mu$, ou plus simplement, si $\mu v = 0$ et $v \neq 0$ (car $\mu v + 0 = 0$ et on a montré que $\lambda = 0$), alors $\mu=0$.
Donc $u$ et $v$ sont linéairement indépendants.

**Sens direct :**
Supposons que $u$ et $v$ sont linéairement indépendants.
La famille $(u, v)$ est une famille libre dans $E$.
D'après le théorème de la base incomplète (en supposant $\dim E \ge 2$), nous pouvons compléter cette famille pour former une base $\mathcal{B} = (u, v, e_3, \dots, e_n)$ de l'espace $E$.
Soit $\mathcal{B}^* = (u^*, v^*, e_3^*, \dots, e_n^*)$ la base duale associée à $\mathcal{B}$.
Par définition de la base duale, la forme linéaire $u^*$ vérifie :
$u^*(u) = 1$ et $u^*(v) = 0$.
Il suffit de choisir $\varphi = u^*$ pour démontrer l'existence requise. L'équivalence est donc prouvée.
