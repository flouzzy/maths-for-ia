\subsection*{Exercice 10 : Non-multiplicabilité des distributions \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

**Énoncé :**
La multiplication de deux distributions n'est pas définie en général. Montrer cela en exhibant une contradiction si l'on suppose que le produit suit l'associativité usuelle, en considérant le produit de $\delta_0$, $x$, et la distribution Valeur Principale (v.p. $1/x$). Note : on admet que $x \delta_0 = 0$ et $x \cdot \text{v.p.}(1/x) = 1$.

**Correction :**
Si la multiplication était bien définie sur l'ensemble des distributions et associative, on aurait pour trois distributions $T, U, V$ :
$$(T \times U) \times V = T \times (U \times V)$$
Prenons $T = \delta_0$, $U = x$ (la fonction $f(x)=x$ vue comme distribution), et $V = \text{v.p.}(1/x)$ (qui est la distribution associée à la fonction $1/x$ en gérant la singularité en 0).
Calculons le terme de gauche :
$$(\delta_0 \times x) \times \text{v.p.}(1/x)$$
On admet que $\delta_0 \times x = 0$ (car $\langle x\delta_0, \phi \rangle = \langle \delta_0, x\phi \rangle = 0 \cdot \phi(0) = 0$). Donc le terme de gauche vaut $0 \times \text{v.p.}(1/x) = 0$.
Calculons le terme de droite :
$$\delta_0 \times (x \times \text{v.p.}(1/x))$$
On admet que $x \times \text{v.p.}(1/x) = 1$ (la fonction constante 1, car on annule la singularité). Donc le terme de droite vaut :
$$\delta_0 \times 1$$
Le produit d'une distribution $T$ par une fonction infiniment dérivable $\alpha$ (ici $\alpha(x)=1$) est défini par $\langle \alpha T, \phi \rangle = \langle T, \alpha \phi \rangle$.
Donc $\langle 1 \cdot \delta_0, \phi \rangle = \langle \delta_0, 1 \cdot \phi \rangle = \phi(0) = \langle \delta_0, \phi \rangle$. D'où $\delta_0 \times 1 = \delta_0$.
Nous obtenons :
$$0 = \delta_0$$
Ce qui est une contradiction absolue (l'action sur une fonction valant $1$ en $0$ donne $0=1$). Ainsi, on ne peut pas définir de manière cohérente la multiplication de deux distributions quelconques.
