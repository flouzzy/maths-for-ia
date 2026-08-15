# Exercice 8 : Théorème de Stone-Weierstrass $\bigstar\bigstar\bigstar\bigstar\bigstar$
En utilisant le théorème de Stone-Weierstrass, démontrer l'approximation universelle avec $\sigma(x) = x^2$ pour un domaine compact arbitraire $K \subset \mathbb{R}^n$.

\textbf{Correction détaillée}
Considérons l'ensemble $A = \text{Vect}\{ (w^T x + b)^2 \mid w \in \mathbb{R}^n, b \in \mathbb{R} \}$.
Développons le carré : $(w^T x + b)^2 = (w^T x)^2 + 2b w^T x + b^2 = \sum_{i,j} w_i w_j x_i x_j + 2b \sum w_i x_i + b^2$.
On voit que $A$ contient :
- Les constantes (en posant $w=0, b \neq 0$).
- Les fonctions affines $x_i$ (en ajustant $b$).
- Les termes quadratiques et croisés $x_i^2$ et $x_i x_j$ (par polarisation $(x_i+x_j)^2 - x_i^2 - x_j^2$).
Toutefois, l'algèbre engendrée par $A$ engendre tous les polynômes de $\mathbb{R}^n$, qui est dense dans $\mathcal{C}(K)$ par Stone-Weierstrass.
Cependant, l'ensemble $A$ lui-même ne contient QUE les polynômes de degré au plus 2.
Le théorème d'approximation universelle stricto sensu n'est pas vérifié pour les réseaux à une SEULE couche cachée avec $\sigma(x)=x^2$, car ils ne peuvent générer des degrés $\ge 3$.
L'affirmation est fausse pour une seule couche. Elle nécessite plusieurs couches (fonctions composées) pour que $\sigma(x)=x^2$ puisse engendrer par compositions successives des polynômes de degrés arbitrairement élevés, rendant le réseau dense.
