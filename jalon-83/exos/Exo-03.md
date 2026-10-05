# Exercice 3 : Dérivée d'une fonction exponentielle tronquée  \quad $\bigstar\bigstar\star\star\star$


## Énoncé
Soit la fonction $f(x) = e^x \mathbf{1}_{[0, +\infty[}(x)$, où $\mathbf{1}_{[0, +\infty[}$ est la fonction indicatrice (fonction de Heaviside $H$).
Calculer la dérivée de $f$ au sens des distributions, notée $T_f'$.

## Correction
La fonction $f$ est donnée par :
$$
f(x) = \begin{cases}
e^x & \text{si } x > 0 \\
0 & \text{si } x < 0
\end{cases}
$$
$f$ est de classe $C^\infty$ sur $]-\infty, 0[$ et sur $]0, +\infty[$.
Sa dérivée usuelle $\{f'\}$ est :
$$
\{f'\}(x) = \begin{cases}
e^x & \text{si } x > 0 \\
0 & \text{si } x < 0
\end{cases}
$$
On remarque que $\{f'\}(x) = f(x)$.

Étudions la continuité en $x = 0$ :
- Limite à droite : $f(0^+) = e^0 = 1$
- Limite à gauche : $f(0^-) = 0$
La fonction $f$ présente un saut en $x=0$ de valeur $\sigma_0 = 1 - 0 = 1$.

D'après la formule des sauts :
$$ T_f' = T_{\{f'\}} + \sigma_0 \delta_0 $$
Donc, au sens des distributions :
$$ f' = f + \delta_0 $$

Cette relation montre que $f$ est solution au sens des distributions de l'équation différentielle $y' - y = \delta_0$. C'est ce qu'on appelle la solution fondamentale de l'opérateur $L = \frac{d}{dx} - \text{id}$.
