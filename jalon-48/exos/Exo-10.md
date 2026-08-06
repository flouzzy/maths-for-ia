# Exercice 10 : Le phénomène de la disparition du gradient (Vanishing Gradient)
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Démontrer formellement pourquoi l'utilisation de la fonction sigmoïde sur un réseau de $L$ couches profondes avec des poids initiaux de faible variance entraîne une atténuation exponentielle du gradient par rapport aux premières couches.

## Correction détaillée
1. Considérons un réseau linéaire en chaîne (une seule dimension par couche) : $a^{(l)} = \sigma(w^{(l)} a^{(l-1)})$ (pas de biais pour simplifier).
2. L'erreur rétropropagée depuis la sortie s'écrit $\delta^{(l)} = \frac{\partial \mathcal{L}}{\partial z^{(l)}}$.
3. La relation de récurrence (Jacobienne) est $\delta^{(l)} = \delta^{(l+1)} \cdot w^{(l+1)} \cdot \sigma'(z^{(l)})$.
4. Si l'on souhaite calculer le gradient pour le poids de la toute première couche $w^{(1)}$, on doit calculer l'erreur $\delta^{(1)}$, qui s'obtient en déroulant la récurrence.
5. $\delta^{(1)} = \delta^{(L)} \prod_{k=2}^{L} w^{(k)} \sigma'(z^{(k-1)})$.
6. Or, on a démontré à l'Exercice 1 que pour la sigmoïde, $\sigma'(x) = \sigma(x)(1 - \sigma(x))$. Cette dérivée admet un maximum global en $x=0$, qui vaut $\sigma'(0) = 0.5 \times (1 - 0.5) = 0.25$.
7. Donc, quel que soit $x$, on a la majoration stricte : $|\sigma'(x)| \leq \frac{1}{4}$.
8. Si les poids sont initialisés avec une variance faible, telle que $|w^{(k)}| < 1$, alors le terme du produit vérifie $|w^{(k)} \sigma'(z^{(k-1)})| < \frac{1}{4}$.
9. En appliquant cette majoration au produit, on obtient : $|\delta^{(1)}| \leq |\delta^{(L)}| \left(\frac{1}{4}\right)^{L-1}$.
10. La conclusion est immédiate : le gradient $\delta^{(1)}$ décroît exponentiellement vers zéro en fonction de la profondeur $L$. C'est le théorème d'impossibilité d'apprentissage profond des années 90, résolu ultérieurement par les fonctions ReLU et les normalisations de type He/Glorot.
