---
uuid: jalon-83-exo-06
title: "Exercice 06 - Dérivation des distributions"
---

# Exercice 06 $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
La distribution de Dirac peut elle-même être dérivée.
1. À partir de la définition de la dérivation, donner l'expression de $\langle \delta_0', \phi \rangle$ pour une fonction test $\phi$.
2. Généraliser pour obtenir l'expression de $\langle \delta_0^{(n)}, \phi \rangle$.
3. Résoudre l'équation $x T = \delta_0'$ où $T \in \mathcal{D}'(\mathbb{R})$. (On donne que la solution générale de $x S = 0$ est $S = c \delta_0$).

**Correction pas à pas :**
1. Par définition, pour toute $\phi \in \mathcal{D}(\mathbb{R})$ :
$$ \langle \delta_0', \phi \rangle = - \langle \delta_0, \phi' \rangle = - \phi'(0) $$
L'action de la dérivée du Dirac est d'évaluer l'opposé de la dérivée de la fonction test en l'origine.

2. Par itération, pour la dérivée $n$-ième :
$$ \langle \delta_0^{(n)}, \phi \rangle = - \langle \delta_0^{(n-1)}, \phi' \rangle = (-1)^2 \langle \delta_0^{(n-2)}, \phi'' \rangle = \dots = (-1)^n \langle \delta_0, \phi^{(n)} \rangle = (-1)^n \phi^{(n)}(0) $$
La dérivée $n$-ième de Dirac évalue la dérivée $n$-ième de la fonction test (au signe près).

3. On cherche $T$ tel que $x T = \delta_0'$.
Intuitivement, on peut essayer de voir si $T$ est liée à des dérivées de Dirac.
Calculons le produit $x \delta_0''$ :
$$ \langle x \delta_0'', \phi \rangle = \langle \delta_0'', x \phi(x) \rangle = (-1)^2 \frac{d^2}{dx^2}(x \phi(x))\Big|_{x=0} $$
Or $\frac{d}{dx}(x\phi) = \phi + x\phi'$ et $\frac{d^2}{dx^2}(x\phi) = \phi' + \phi' + x\phi'' = 2\phi' + x\phi''$.
En évaluant en 0 :
$$ \langle x \delta_0'', \phi \rangle = 2\phi'(0) + 0 \cdot \phi''(0) = 2\phi'(0) $$
Or $\langle \delta_0', \phi \rangle = -\phi'(0)$.
Donc $x \delta_0'' = -2 \delta_0'$.
On en déduit que $-\frac{1}{2} x \delta_0'' = \delta_0'$.
Une solution particulière est donc $T_0 = -\frac{1}{2} \delta_0''$.
Puisque la solution générale de l'équation homogène $x S = 0$ est $S = c \delta_0$, la solution générale de l'équation complète est :
$$ T = -\frac{1}{2} \delta_0'' + c \delta_0 \quad (c \in \mathbb{R}) \quad \blacksquare $$
