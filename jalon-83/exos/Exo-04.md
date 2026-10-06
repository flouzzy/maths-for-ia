---
uuid: jalon-83-exo-04
title: "Exercice 04 - Dérivation des distributions"
---

# Exercice 04 $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $T \in \mathcal{D}'(\mathbb{R})$ une distribution et $\alpha \in C^\infty(\mathbb{R})$ une fonction infiniment dérivable.
Le produit $\alpha T$ est défini par $\langle \alpha T, \phi \rangle = \langle T, \alpha \phi \rangle$ pour toute fonction test $\phi \in \mathcal{D}(\mathbb{R})$.
1. Démontrer la règle de Leibniz pour les distributions : $(\alpha T)' = \alpha' T + \alpha T'$.
2. Application : Calculer la dérivée de $f(x) = x \cdot \text{sgn}(x)$ en utilisant cette règle, et vérifier que cela correspond au calcul direct de la dérivée de $|x|$ (puisque $x \text{sgn}(x) = |x|$).

**Correction pas à pas :**
1. Soit $\phi \in \mathcal{D}(\mathbb{R})$. Appliquons la définition de la dérivée à la distribution $\alpha T$ :
$$ \langle (\alpha T)', \phi \rangle = - \langle \alpha T, \phi' \rangle $$
Par définition du produit d'une distribution par une fonction $C^\infty$ :
$$ = - \langle T, \alpha \phi' \rangle $$
Or, par la règle de Leibniz sur les fonctions (ici $\alpha$ et $\phi$ sont de classe $C^\infty$) :
$$ (\alpha \phi)' = \alpha' \phi + \alpha \phi' \implies \alpha \phi' = (\alpha \phi)' - \alpha' \phi $$
Substituons cette expression :
$$ = - \langle T, (\alpha \phi)' - \alpha' \phi \rangle $$
Par linéarité de la distribution $T$ :
$$ = - \langle T, (\alpha \phi)' \rangle + \langle T, \alpha' \phi \rangle $$
Le premier terme est par définition l'action de la dérivée $T'$ sur la fonction test $(\alpha \phi)$ :
$$ - \langle T, (\alpha \phi)' \rangle = \langle T', \alpha \phi \rangle = \langle \alpha T', \phi \rangle $$
Le second terme est par définition l'action de $(\alpha' T)$ sur $\phi$ :
$$ \langle T, \alpha' \phi \rangle = \langle \alpha' T, \phi \rangle $$
En regroupant :
$$ \langle (\alpha T)', \phi \rangle = \langle \alpha T', \phi \rangle + \langle \alpha' T, \phi \rangle = \langle \alpha T' + \alpha' T, \phi \rangle $$
Cette égalité étant vraie pour tout $\phi \in \mathcal{D}(\mathbb{R})$, on conclut que $(\alpha T)' = \alpha T' + \alpha' T$.

2. Appliquons à $\alpha(x) = x$ (qui est bien $C^\infty$) et $T = \text{sgn}(x)$.
On sait que $\alpha'(x) = 1$ et $T' = 2\delta_0$ (d'après un exercice précédent).
D'après la formule de Leibniz :
$$ (x \cdot \text{sgn})' = 1 \cdot \text{sgn} + x \cdot (2\delta_0) $$
Évaluons le terme $x \cdot (2\delta_0)$. Pour toute fonction test $\phi$ :
$$ \langle x \cdot (2\delta_0), \phi \rangle = \langle 2\delta_0, x\phi(x) \rangle = 2(0 \cdot \phi(0)) = 0 $$
Ainsi la distribution $x \delta_0$ est nulle (la masse de Dirac est concentrée en 0, où le coefficient multiplicateur $x$ vaut 0).
Il reste donc $(x \cdot \text{sgn})' = \text{sgn}$.
Comme $x \text{sgn}(x) = |x|$, on retrouve bien que $(|x|)' = \text{sgn}$, ce qui confirme la cohérence du calcul algébrique sur les distributions. $\blacksquare$
