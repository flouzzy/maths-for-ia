## Exercice 2 : Approximation d'une fonction affine \quad $\bigstar\star\star\star\star$

Soit la fonction de Heaviside modifiée $H(x)$ telle que l'on puisse approcher une fonction affine. Comment utiliser deux neurones ReLU $\sigma(x) = \max(0, x)$ pour représenter exactement une fonction affine par morceaux avec un changement de pente ?

**Correction :**
Soit $f(x)$ une fonction affine par morceaux telle que $f(x) = a x + b$ pour $x < x_0$ et $f(x) = c x + d$ pour $x \ge x_0$, avec continuité en $x_0$ ($a x_0 + b = c x_0 + d$).
On peut utiliser deux ReLUs pour construire cela.
Posons $G(x) = a x + b + (c-a) \max(0, x - x_0)$.
Puisque $x = \max(0, x) - \max(0, -x)$, l'expression affine totale peut s'écrire uniquement avec des ReLUs.
Plus simplement, on écrit $G(x) = a \max(0, x) - a \max(0, -x) + b + (c-a) \max(0, x - x_0)$.
Le réseau représente exactement la fonction.
