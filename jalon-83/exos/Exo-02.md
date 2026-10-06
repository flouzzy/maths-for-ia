# Exercice 2 : Dérivée seconde de la valeur absolue  \quad $\bigstar\bigstar\star\star\star$


## Énoncé
En utilisant le résultat de l'exercice précédent, calculer la dérivée seconde au sens des distributions de la fonction $f(x) = |x|$.

## Correction
D'après l'exercice 1, on a $f'(x) = \text{sgn}(x)$ au sens des distributions, où $\text{sgn}(x)$ vaut $1$ si $x > 0$ et $-1$ si $x < 0$.
Pour calculer $f''(x)$, il faut dériver la distribution $\text{sgn}(x)$.
La fonction $\text{sgn}(x)$ est de classe $C^1$ par morceaux sur $\mathbb{R} \setminus \{0\}$.
Sa dérivée usuelle est nulle presque partout :
$$ \{\text{sgn}'\}(x) = 0 \quad \text{pour tout } x \neq 0 $$
Étudions le saut de la fonction signe en $x = 0$ :
- Limite à droite : $\text{sgn}(0^+) = 1$
- Limite à gauche : $\text{sgn}(0^-) = -1$
Le saut en $0$ est $\sigma_0 = \text{sgn}(0^+) - \text{sgn}(0^-) = 1 - (-1) = 2$.

Par la formule des sauts, on a :
$$ \text{sgn}' = \{\text{sgn}'\} + \sigma_0 \delta_0 = 0 + 2\delta_0 = 2\delta_0 $$

On conclut donc que :
$$ f''(x) = (|x|)'' = 2\delta_0 $$
La "pointe" de la valeur absolue génère une impulsion de Dirac (avec une masse de 2) dans la dérivée seconde.
