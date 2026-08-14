# Approximation de Heaviside

### Énoncé $\quad \bigstar\bigstar\bigstar\star\star$

Prouver que la fonction de Heaviside (marche d'escalier), bien que discontinue, peut être approchée par une suite de fonctions générées par un réseau de neurones, pour la topologie de la convergence ponctuelle.

### Démonstration Détaillée

Bien que le théorème universel classique s'applique aux fonctions continues pour la norme uniforme, on peut approcher une discontinuité de manière ponctuelle. La sigmoïde standard $\sigma(kx)$ pour $k \to \infty$ converge ponctuellement vers $0$ pour $x<0$, vers $1$ pour $x>0$, et vers $0.5$ en $x=0$. Ainsi, une seule couche cachée avec un seul neurone suffit pour obtenir cette convergence, illustrant que la limite forte de l'espace des réseaux englobe les fonctions étagées.
