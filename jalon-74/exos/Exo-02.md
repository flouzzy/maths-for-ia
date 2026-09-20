# Exercice 2 : Inégalité de Jensen discrète

**Difficulté :** ★☆☆☆☆


## Énoncé
En utilisant la fonction $\varphi(x) = x^2$ et la variable aléatoire discrète $X$ prenant les valeurs 1 et 3 avec équiprobabilité, démontrer numériquement l'inégalité de Jensen.

## Correction Détaillée
1. Calcul de l'espérance de $X$ :
$$ \mathbb{E}[X] = \frac{1}{2}(1) + \frac{1}{2}(3) = \frac{1+3}{2} = 2 $$

2. Calcul de l'image de l'espérance :
$$ \varphi(\mathbb{E}[X]) = 2^2 = 4 $$

3. Calcul de l'espérance de l'image $\varphi(X)$ :
$$ \mathbb{E}[\varphi(X)] = \frac{1}{2}\varphi(1) + \frac{1}{2}\varphi(3) = \frac{1}{2}(1^2) + \frac{1}{2}(3^2) = \frac{1 + 9}{2} = \frac{10}{2} = 5 $$

4. Conclusion :
On a $\varphi(\mathbb{E}[X]) = 4$ et $\mathbb{E}[\varphi(X)] = 5$. Puisque $4 \le 5$, l'inégalité de Jensen est numériquement vérifiée. La convexité de la fonction carré garantit ce résultat.
