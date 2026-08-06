# Exercice 3 : Gradient d'un neurone linéaire unique
**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé
Soit un neurone avec la fonction identité, c'est-à-dire $y = w \cdot x + b$. La fonction de perte est l'erreur quadratique moyenne $\mathcal{L} = \frac{1}{2}(y - y_{\text{cible}})^2$. Calculer les gradients de $\mathcal{L}$ par rapport au poids $w$ et au biais $b$.

## Correction détaillée
1. Par la règle de la chaîne, on a $\frac{\partial \mathcal{L}}{\partial w} = \frac{\partial \mathcal{L}}{\partial y} \frac{\partial y}{\partial w}$.
2. Calculons la dérivée de la perte par rapport à la sortie : $\frac{\partial \mathcal{L}}{\partial y} = \frac{\partial}{\partial y} \left( \frac{1}{2}(y - y_{\text{cible}})^2 \right) = (y - y_{\text{cible}})$.
3. Calculons la dérivée de la sortie par rapport au poids $w$ : $\frac{\partial y}{\partial w} = \frac{\partial}{\partial w}(w \cdot x + b) = x$.
4. En multipliant les deux termes, on obtient le gradient par rapport au poids : $\frac{\partial \mathcal{L}}{\partial w} = (y - y_{\text{cible}}) \cdot x$.
5. De manière analogue, pour le biais : $\frac{\partial \mathcal{L}}{\partial b} = \frac{\partial \mathcal{L}}{\partial y} \frac{\partial y}{\partial b}$.
6. La dérivée de la sortie par rapport au biais est : $\frac{\partial y}{\partial b} = 1$.
7. On obtient le gradient par rapport au biais : $\frac{\partial \mathcal{L}}{\partial b} = (y - y_{\text{cible}}) \cdot 1 = y - y_{\text{cible}}$.
Ce résultat illustre le fait que l'ajustement du poids est proportionnel à l'erreur commise multipliée par l'entrée reçue.
