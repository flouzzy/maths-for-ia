## Exercice 7 : Fonctions de classe $C^1$ denses dans $W^{1,p}$ (Théorie de Sobolev) \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Donner un aperçu de la manière dont la densité des fonctions régulières est étendue aux espaces de Sobolev. On considère l'espace $W^{1,p}(\mathbb{R}) = \{u \in L^p(\mathbb{R}) \mid u' \in L^p(\mathbb{R})\}$ où $u'$ est la dérivée faible. Pourquoi les fonctions lisses sont-elles denses dans cet espace ?

**Correction :**
La norme de l'espace de Sobolev $W^{1,p}(\mathbb{R})$ est $\| u \|_{W^{1,p}} = \| u \|_p + \| u' \|_p$.
Pour montrer que les fonctions lisses $C_c^\infty(\mathbb{R})$ sont denses, la technique standard est la régularisation par convolution (ou mollification).

Soit $u \in W^{1,p}(\mathbb{R})$. Soit $\rho_\epsilon$ un mollifieur standard de classe $C_c^\infty$.
On pose $u_\epsilon = u * \rho_\epsilon$.
Par les propriétés de la convolution, $u_\epsilon$ est infiniment dérivable (de classe $C^\infty$) et $u_\epsilon \in L^p$.
De plus, on a la commutation fondamentale des dérivées et de la convolution pour les dérivées faibles :
$(u_\epsilon)' = (u * \rho_\epsilon)' = u' * \rho_\epsilon$.

En utilisant les théorèmes de densité standards dans $L^p$ (similaires à l'exercice 4 pour $L^p$) :
1. $u_\epsilon \to u$ dans $L^p(\mathbb{R})$.
2. $(u_\epsilon)' = u' * \rho_\epsilon \to u'$ dans $L^p(\mathbb{R})$ car $u' \in L^p(\mathbb{R})$.

Ainsi, par définition de la norme de Sobolev :
$\| u_\epsilon - u \|_{W^{1,p}} = \| u_\epsilon - u \|_p + \| (u_\epsilon)' - u' \|_p \to 0$ lorsque $\epsilon \to 0$.
Une fonction de $W^{1,p}$ peut donc toujours être approchée par une fonction de classe $C^\infty$, et par troncature supplémentaire, par des fonctions de $C_c^\infty$. C'est le théorème de Meyers-Serrin.
