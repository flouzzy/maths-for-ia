# Généralisation aux espaces de Lebesgue

### Énoncé $\quad \bigstar\bigstar\bigstar\bigstar\bigstar$

Montrer que si l'architecture est dense dans $\mathcal{C}(I_n)$ pour la norme $\|\cdot\|_\infty$, alors elle est également dense dans l'espace de Lebesgue $L^p(I_n)$ pour $1 \le p < \infty$.

### Démonstration Détaillée

Ce résultat repose sur la densité des fonctions continues dans $L^p$. Pour tout $f \in L^p(I_n)$ et $\epsilon > 0$, on sait par la théorie de la mesure de Lebesgue qu'il existe $g \in \mathcal{C}(I_n)$ telle que $\|f - g\|_p < \epsilon/2$. Par le théorème d'approximation, il existe un réseau $h$ tel que $\|g - h\|_\infty < \epsilon/2$. Puisque le domaine $I_n$ a une mesure finie (volume 1), l'inégalité de Hölder donne $\|g - h\|_p \le \|g - h\|_\infty < \epsilon/2$. Par l'inégalité triangulaire dans $L^p$, on a $\|f - h\|_p < \epsilon$. L'approximation en norme $L^p$ est donc garantie.
