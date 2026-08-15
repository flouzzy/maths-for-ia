# Exercice 3 : La porte logique XOR (version continue) $\bigstar\bigstar\star\star\star$
Considérons $I_2 = [0,1]^2$. On veut approcher la fonction surface $f(x_1, x_2) = x_1 + x_2 - 2x_1 x_2$.
Montrer comment utiliser des ReLUs $\sigma(t) = \max(0, t)$ pour approcher le terme croisé $x_1 x_2$.

\textbf{Correction détaillée}
On sait que $2x_1 x_2 = (x_1 + x_2)^2 - x_1^2 - x_2^2$.
Pour approcher la fonction carré $t \mapsto t^2$ sur $[0, 2]$, on peut utiliser une somme de ReLUs.
Puisque $t^2$ est convexe, on peut l'approcher par une ligne brisée convexe, qui est une combinaison linéaire de fonctions $\max(0, t - t_i)$.
Soit $N$ le nombre de segments. On subdivise $[0, 2]$ en $t_i = i \frac{2}{N}$.
La fonction approchant $t^2$ est de la forme $H_N(t) = \sum_{i=1}^{N-1} c_i \max(0, t - t_i) + c_0 t + b_0$.
Ainsi, la multiplication $x_1 x_2 = \frac{1}{2} (H_N(x_1+x_2) - H_N(x_1) - H_N(x_2))$ peut être approchée arbitrairement près.
Puisque $H_N$ est une somme de ReLUs, $x_1 x_2$ s'exprime comme une combinaison linéaire de ReLUs de la forme $\sigma(w^T x + b)$.
La densité s'ensuit.
