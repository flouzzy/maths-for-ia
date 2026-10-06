# Exercice 4 : Produit d'une fonction $C^\infty$ par une distribution  \quad $\bigstar\bigstar\bigstar\star\star$


## Énoncé
Soit $\alpha \in C^\infty(\mathbb{R})$ et $T \in \mathcal{D}'(\mathbb{R})$.
On définit le produit $\alpha T$ par : $\langle \alpha T, \phi \rangle = \langle T, \alpha \phi \rangle$ pour toute fonction test $\phi \in \mathcal{D}(\mathbb{R})$.
Montrer la règle de Leibniz pour la dérivation :
$$ (\alpha T)' = \alpha' T + \alpha T' $$

## Correction
Soit $\phi \in \mathcal{D}(\mathbb{R})$.
Par définition de la dérivée d'une distribution :
$$ \langle (\alpha T)', \phi \rangle = - \langle \alpha T, \phi' \rangle $$
Par définition du produit d'une fonction lisse par une distribution :
$$ \langle \alpha T, \phi' \rangle = \langle T, \alpha \phi' \rangle $$
D'autre part, évaluons le membre de droite de l'égalité à démontrer :
$$ \langle \alpha' T + \alpha T', \phi \rangle = \langle \alpha' T, \phi \rangle + \langle \alpha T', \phi \rangle $$
$$ = \langle T, \alpha' \phi \rangle + \langle T', \alpha \phi \rangle $$
Par définition de la dérivée de $T$ appliquée à la fonction test $(\alpha \phi)$ (qui est bien dans $\mathcal{D}(\mathbb{R})$ car $\alpha \in C^\infty$ et $\phi$ a un support compact) :
$$ \langle T', \alpha \phi \rangle = - \langle T, (\alpha \phi)' \rangle $$
Or, par la règle de Leibniz usuelle sur les fonctions différentiables :
$$ (\alpha \phi)' = \alpha' \phi + \alpha \phi' $$
Donc :
$$ \langle T', \alpha \phi \rangle = - \langle T, \alpha' \phi + \alpha \phi' \rangle = - \langle T, \alpha' \phi \rangle - \langle T, \alpha \phi' \rangle $$
Revenons au membre de droite complet :
$$ \langle \alpha' T + \alpha T', \phi \rangle = \langle T, \alpha' \phi \rangle - \langle T, \alpha' \phi \rangle - \langle T, \alpha \phi' \rangle $$
Les termes $\langle T, \alpha' \phi \rangle$ s'annulent :
$$ \langle \alpha' T + \alpha T', \phi \rangle = - \langle T, \alpha \phi' \rangle $$
Nous avons ainsi montré que pour tout $\phi \in \mathcal{D}(\mathbb{R})$ :
$$ \langle (\alpha T)', \phi \rangle = \langle \alpha' T + \alpha T', \phi \rangle $$
L'égalité au sens des distributions est donc vérifiée : $(\alpha T)' = \alpha' T + \alpha T'$.
