# Exercice 1 : Dérivée première de la valeur absolue  \quad $\bigstar\star\star\star\star$


## Énoncé
Soit la fonction $f(x) = |x|$.
1. Tracer l'allure de la fonction $f$.
2. Calculer sa dérivée au sens des distributions, notée $f'$.

## Correction
1. La fonction $f(x) = |x|$ est la fonction valeur absolue. Elle est continue sur $\mathbb{R}$, vaut $x$ pour $x \ge 0$, et $-x$ pour $x \le 0$. Son graphe est en forme de "V" avec une pointe à l'origine.

2. On utilise la formule des sauts pour calculer sa dérivée au sens des distributions.
La fonction $f$ est de classe $C^1$ par morceaux sur $\mathbb{R} \setminus \{0\}$.
Sa dérivée usuelle $\{f'\}$ est définie par :
$$
\{f'\}(x) = \begin{cases}
1 & \text{si } x > 0 \\
-1 & \text{si } x < 0
\end{cases}
$$
Cette fonction est exactement la fonction signe, notée $\text{sgn}(x)$.
Étudions le saut de la fonction $f$ en $x = 0$ :
- Limite à droite : $f(0^+) = \lim_{x \to 0, x>0} x = 0$
- Limite à gauche : $f(0^-) = \lim_{x \to 0, x<0} (-x) = 0$
La fonction $f$ étant continue en $0$, le saut est $\sigma_0 = f(0^+) - f(0^-) = 0 - 0 = 0$.

Par la formule des sauts, on a :
$$ f' = \{f'\} + \sigma_0 \delta_0 = \text{sgn}(x) + 0 \cdot \delta_0 = \text{sgn}(x) $$
La dérivée au sens des distributions de la fonction valeur absolue est donc la fonction signe.
