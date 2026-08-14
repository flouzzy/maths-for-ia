# Le cas de l'activation ReLU

### Énoncé $\quad \bigstar\bigstar\bigstar\bigstar\star$

Démontrer l'approximation universelle sur le segment $[0, 1]$ en utilisant la fonction ReLU $\sigma(x) = \max(0, x)$ comme fonction d'activation.

### Démonstration Détaillée

Avec ReLU, on peut construire une fonction \og chapeau \fg{} centrée en $c$ avec un support $[c-h, c+h]$ par combinaison de trois ReLU : $g(x) = \frac{1}{h} (\text{ReLU}(x - (c-h)) - 2\text{ReLU}(x-c) + \text{ReLU}(x - (c+h)))$. Toute fonction continue sur $[0, 1]$ peut être approchée uniformément par une somme finie pondérée de ces fonctions chapeaux (interpolation linéaire par morceaux). Ceci démontre que l'architecture ReLU est un approximateur universel.
