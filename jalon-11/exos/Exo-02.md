---
uuid: "exo-11-02"
title: "Exercice 2: Caractérisation d'un hyperplan vectoriel"
---
# Exercice 2: Caractérisation d'un hyperplan vectoriel (Difficulté $\star \star$)

## Énoncé
Dans $E = \mathbb{R}^3$, on considère le sous-espace $H = \{ (x, y, z) \in \mathbb{R}^3 \mid 2x - y + 3z = 0 \}$. Démontrer rigoureusement que $H$ est un hyperplan et expliciter une forme linéaire l'engendrant en tant que noyau.

## Correction détaillée

1. **Définition de l'application candidate :**
   Considérons l'application $\phi : \mathbb{R}^3 \to \mathbb{R}$ définie par $\phi(x, y, z) = 2x - y + 3z$.

2. **Démonstration de la linéarité de $\phi$ :**
   Soient $u = (x_1, y_1, z_1)$ et $v = (x_2, y_2, z_2)$ deux vecteurs de $\mathbb{R}^3$. Soient $\alpha, \beta \in \mathbb{R}$.
   $$\phi(\alpha u + \beta v) = \phi(\alpha x_1 + \beta x_2, \alpha y_1 + \beta y_2, \alpha z_1 + \beta z_2)$$
   $$= 2(\alpha x_1 + \beta x_2) - (\alpha y_1 + \beta y_2) + 3(\alpha z_1 + \beta z_2)$$
   En réarrangeant les termes scalaires :
   $$= \alpha(2x_1 - y_1 + 3z_1) + \beta(2x_2 - y_2 + 3z_2)$$
   $$= \alpha \phi(u) + \beta \phi(v)$$
   L'application $\phi$ est donc une forme linéaire (un élément de $E^*$).

3. **Vérification de la non-nullité :**
   Pour s'assurer que $\phi$ engendre un hyperplan (et non l'espace total), il faut que $\phi$ ne soit pas l'application nulle.
   Évaluons $\phi$ sur le vecteur de la base canonique $e_1 = (1, 0, 0)$ :
   $$\phi(1, 0, 0) = 2(1) - 0 + 3(0) = 2 \neq 0$$
   Donc $\phi \neq 0_{E^*}$.

4. **Lien avec le noyau :**
   Par définition, l'ensemble $H$ est exactement constitué des vecteurs $u \in \mathbb{R}^3$ tels que $\phi(u) = 0$.
   Ainsi, $H = \ker \phi$.

**Conclusion :**
L'ensemble $H$ étant le noyau d'une forme linéaire non identiquement nulle sur un espace de dimension $3$, $H$ est formellement un hyperplan de $\mathbb{R}^3$, et par le théorème des dimensions, $\dim(H) = 3 - 1 = 2$.
