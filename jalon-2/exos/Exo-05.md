# Exercice 5 - Difficulté: Niveau 3

## 1. Énoncé
Démontrer par analyse-synthèse que toute fonction $f: \mathbb{R} \to \mathbb{R}$ se décompose de manière unique en la somme d'une fonction paire et d'une fonction impaire.

## 2. Démonstration (Zéro Ellipse)
**Analyse :** Supposons que $f = P + I$ où $P$ est paire ($P(-x) = P(x)$) et $I$ est impaire ($I(-x) = -I(x)$). Pour tout $x \in \mathbb{R}$, on a $f(x) = P(x) + I(x)$. Et $f(-x) = P(-x) + I(-x) = P(x) - I(x)$. En additionnant ces deux équations, on obtient $f(x) + f(-x) = 2P(x)$, d'où $P(x) = \frac{f(x) + f(-x)}{2}$. En les soustrayant, on obtient $f(x) - f(-x) = 2I(x)$, d'où $I(x) = \frac{f(x) - f(-x)}{2}$. Si une telle décomposition existe, elle est donc unique.
**Synthèse :** Posons $P(x) = \frac{f(x) + f(-x)}{2}$ et $I(x) = \frac{f(x) - f(-x)}{2}$. $P$ est paire : $P(-x) = \frac{f(-x) + f(x)}{2} = P(x)$. $I$ est impaire : $I(-x) = \frac{f(-x) - f(x)}{2} = -\frac{f(x) - f(-x)}{2} = -I(x)$. Enfin, pour tout $x \in \mathbb{R}, P(x) + I(x) = \frac{f(x) + f(-x) + f(x) - f(-x)}{2} = \frac{2f(x)}{2} = f(x)$. La décomposition existe et est bien de la forme annoncée.
