# Exercice 2 : Dérivation de la fonction ReLU
**Difficulté :** $\bigstar\star\star\star\star$

## Énoncé
Calculer le sous-gradient de la fonction ReLU, définie par $\text{ReLU}(x) = \max(0, x)$.

## Correction détaillée
1. La fonction ReLU est définie par deux morceaux : $f(x) = x$ si $x > 0$, et $f(x) = 0$ si $x < 0$.
2. Pour $x > 0$, la fonction est linéaire et sa dérivée est trivialement $f'(x) = 1$.
3. Pour $x < 0$, la fonction est constante et sa dérivée est $f'(x) = 0$.
4. En $x = 0$, la fonction n'est pas strictement dérivable au sens classique car les limites des taux d'accroissement diffèrent à gauche (0) et à droite (1).
5. En théorie de l'optimisation non-lisse, on utilise le sous-différentiel $\partial f(0)$, qui est l'intervalle $[0, 1]$.
6. En pratique dans les réseaux de neurones, on choisit une valeur arbitraire dans cet intervalle, usuellement $0$ (ou parfois $1$). On adopte donc la convention $\text{ReLU}'(0) = 0$.
7. L'expression finale pour le gradient est la fonction indicatrice : $\text{ReLU}'(x) = \mathbf{1}_{\{x > 0\}}$.
Ce calcul simple permet un passage arrière rapide sans calcul exponentiel.
