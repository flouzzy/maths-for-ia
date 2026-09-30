\subsection*{Exercice 5 : Équation différentielle résolue par Fourier \quad $\bigstar\bigstar\bigstar\star\star$}

On cherche à résoudre l'équation différentielle suivante pour une fonction $y \in \mathcal{C}^1(\mathbb{R}) \cap L^1(\mathbb{R})$ avec $y' \in L^1(\mathbb{R})$ :
$$ -y''(t) + \alpha^2 y(t) = f(t) \quad (\text{avec } \alpha > 0) $$
où $f \in L^1(\mathbb{R})$ est donnée.
On suppose que $y'' \in L^1(\mathbb{R})$.
En utilisant la transformée de Fourier, exprimer $\hat{y}(\xi)$ en fonction de $\hat{f}(\xi)$ et $\alpha$.

---
**Correction :**

Appliquons la transformée de Fourier linéaire à l'équation différentielle complète.
$$ \mathcal{F}(-y''(t) + \alpha^2 y(t)) = \mathcal{F}(f(t)) $$
$$ -\mathcal{F}(y'')(\xi) + \alpha^2 \mathcal{F}(y)(\xi) = \hat{f}(\xi) $$
On utilise la propriété de dérivation de la transformée de Fourier.
Pour la dérivée première : $\mathcal{F}(y')(\xi) = i\xi \hat{y}(\xi)$.
Pour la dérivée seconde : $\mathcal{F}(y'')(\xi) = \mathcal{F}((y')')(\xi) = i\xi \mathcal{F}(y')(\xi) = i\xi (i\xi \hat{y}(\xi)) = -\xi^2 \hat{y}(\xi)$.
Substituons ceci dans l'équation :
$$ -(-\xi^2 \hat{y}(\xi)) + \alpha^2 \hat{y}(\xi) = \hat{f}(\xi) $$
$$ \xi^2 \hat{y}(\xi) + \alpha^2 \hat{y}(\xi) = \hat{f}(\xi) $$
Factorisons par $\hat{y}(\xi)$ :
$$ (\xi^2 + \alpha^2) \hat{y}(\xi) = \hat{f}(\xi) $$
Isolons $\hat{y}(\xi)$ :
$$ \hat{y}(\xi) = \frac{1}{\xi^2 + \alpha^2} \hat{f}(\xi) $$
L'équation différentielle, qui était une équation analytique complexe, est devenue une simple équation algébrique (multiplication) dans le domaine de Fourier.
On remarque que $\frac{1}{\xi^2 + \alpha^2}$ ressemble (à un facteur multiplicatif près) à la transformée de l'exponentielle symétrique trouvée dans l'exercice 3.
