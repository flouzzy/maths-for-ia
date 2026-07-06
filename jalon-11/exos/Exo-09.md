# Exercice 9: Indépendance linéaire de formes linéaires
## Énoncé
Soient $\phi_1, \dots, \phi_p \in E^*$. Montrer qu'elles sont linéairement indépendantes si et seulement si l'intersection de leurs noyaux $\bigcap_{i=1}^p \ker \phi_i$ est de dimension $n-p$.

## Correction détaillée
1. **Étape 1:** On définit l'application linéaire $\Phi : E \to \mathbb{K}^p$ par $\Phi(x) = (\phi_1(x), \dots, \phi_p(x))$.
2. **Étape 2:** Le noyau de $\Phi$ est exactement l'intersection des noyaux : $\ker \Phi = \bigcap_{i=1}^p \ker \phi_i$.
3. **Étape 3:** D'après le théorème du rang, $\dim E = \dim \ker \Phi + \dim \text{Im}(\Phi)$. Donc $\dim \bigcap \ker \phi_i = n - \dim \text{Im}(\Phi)$.
4. **Étape 4:** L'image de la transposée $\Phi^t : (\mathbb{K}^p)^* \to E^*$ est le sous-espace engendré par les $\phi_i$. Or $\text{rg}(\Phi) = \text{rg}(\Phi^t) = \dim \text{Vect}(\phi_1, \dots, \phi_p)$.
5. **Étape 5:** Ainsi, $\dim \text{Vect}(\phi_1, \dots, \phi_p) = p$ (c'est-à-dire que la famille est libre) si et seulement si $\text{rg}(\Phi) = p$, ce qui équivaut à $\dim \bigcap \ker \phi_i = n - p$.
6. **Conclusion:** L'équivalence est rigoureusement prouvée via l'application associée et le théorème du rang.

$\blacksquare$
