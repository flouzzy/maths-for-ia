# Exercice 8 : L'échafaudage de Weierstrass
**Énoncé :**
Étudier la suite $f_n(x) = \sqrt{x^2 + \frac{1}{n}}$ sur $\mathbb{R}$.

**Solution Rigoureuse :**
1. **Convergence simple :**
Pour tout $x \in \mathbb{R}$ fixé, la continuité de la fonction racine carrée assure que :
$$\lim_{n \to +\infty} \sqrt{x^2 + \frac{1}{n}} = \sqrt{x^2} = |x|$$
La limite simple est $f(x) = |x|$.

2. **Convergence uniforme :**
Nous devons évaluer la quantité $|f_n(x) - f(x)|$.
$$f_n(x) - f(x) = \sqrt{x^2 + \frac{1}{n}} - \sqrt{x^2}$$
Pour contourner la soustraction de racines, utilisons l'expression conjuguée :
$$f_n(x) - f(x) = \frac{(x^2 + \frac{1}{n}) - x^2}{\sqrt{x^2 + \frac{1}{n}} + \sqrt{x^2}} = \frac{\frac{1}{n}}{\sqrt{x^2 + \frac{1}{n}} + |x|}$$
Cette quantité est strictement positive, et maximale lorsque le dénominateur est minimal, ce qui se produit au point $x = 0$.
Le supremum de la différence est donc :
$$\sup_{x \in \mathbb{R}} |f_n(x) - f(x)| = \frac{\frac{1}{n}}{\sqrt{\frac{1}{n}} + 0} = \frac{1}{n \frac{1}{\sqrt{n}}} = \frac{1}{\sqrt{n}}$$
Puisque $\lim_{n \to +\infty} \frac{1}{\sqrt{n}} = 0$, la norme de la convergence uniforme tend vers 0.
La suite de fonctions $f_n$ converge uniformément vers la fonction valeur absolue sur $\mathbb{R}$.
*Remarque de structure :* C'est un point de passage fondamental pour démontrer le théorème de Stone-Weierstrass. Les fonctions $f_n$ sont de classe $\mathcal{C}^\infty$ (pour $n$ fini, la singularité de $|x|$ en zéro est évitée car l'argument du radical est strictement positif), alors que la limite ne l'est pas. C'est l'archétype de la régularisation de Lebesgue.
