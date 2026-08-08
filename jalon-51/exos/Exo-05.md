## Exercice 5 : Intersection de boules \quad $\bigstar\bigstar\star$

**Énoncé :** Dans un espace métrique, si deux boules fermées $\overline{B}(x, r_1)$ et $\overline{B}(y, r_2)$ sont disjointes, démontrer strictement que $d(x, y) > r_1 + r_2$.

**Correction :** Procédons par l'absurde. Supposons que $d(x, y) \le r_1 + r_2$.
Dans l'espace euclidien $\mathbb{R}^n$, si la distance entre les centres est inférieure à la somme des rayons, l'intersection est non vide. Cependant, dans un espace métrique général, on ne peut pas construire trivialement un point milieu.
En fait, l'implication proposée dans l'énoncé s'écrit par contraposée : si $d(x, y) \le r_1 + r_2$, alors les boules peuvent-elles être disjointes ?
Dans la distance discrète, si $r_1=r_2=1/2$, et $x \neq y$, $d(x,y)=1 \le 1/2+1/2=1$. Les boules fermées $\overline{B}(x, 1/2)=\{x\}$ et $\overline{B}(y, 1/2)=\{y\}$ sont disjointes, bien que $d(x,y) = r_1+r_2$.
Donc, $d(x, y) > r_1 + r_2$ est **faux en général** pour impliquer des boules disjointes, il faut une métrique stricte comme une norme sur un EV.
Réciproquement, montrons que si $\overline{B}(x, r_1) \cap \overline{B}(y, r_2) \neq \emptyset$, alors $d(x,y) \le r_1+r_2$.
Soit $z$ dans l'intersection. $d(x, z) \le r_1$ et $d(y, z) \le r_2$.
Par inégalité triangulaire, $d(x, y) \le d(x, z) + d(z, y) \le r_1 + r_2$.
Par contraposée absolue, si $d(x, y) > r_1 + r_2$, alors les boules sont strictement disjointes.
