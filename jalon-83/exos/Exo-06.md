# Exercice 6 : Équation différentielle $T' = 0$  \quad $\bigstar\bigstar\bigstar\star\star$


## Énoncé
Soit $T \in \mathcal{D}'(\mathbb{R})$ une distribution vérifiant $T' = 0$.
Montrer que $T$ est une distribution constante, c'est-à-dire qu'il existe $C \in \mathbb{R}$ tel que pour toute $\phi \in \mathcal{D}(\mathbb{R})$, $\langle T, \phi \rangle = C \int_{\mathbb{R}} \phi(x) dx$.

## Correction
Soit $\phi \in \mathcal{D}(\mathbb{R})$.
Nous devons trouver une fonction $\psi \in \mathcal{D}(\mathbb{R})$ telle que $\psi' = \phi$.
Si une telle fonction $\psi$ à support compact existe, alors par définition du théorème fondamental de l'analyse, il est nécessaire que l'intégrale de sa dérivée sur $\mathbb{R}$ soit nulle :
$$ \int_{\mathbb{R}} \phi(x) dx = \int_{\mathbb{R}} \psi'(x) dx = [\psi(x)]_{-\infty}^{+\infty} = 0 $$
Soit $\phi_0 \in \mathcal{D}(\mathbb{R})$ une fonction fixée d'intégrale 1, par exemple une "bosse" (bump function) bien choisie telle que $\int \phi_0(x)dx = 1$.
Toute fonction test $\phi \in \mathcal{D}(\mathbb{R})$ peut se décomposer sous la forme :
$$ \phi(x) = \left( \int_{\mathbb{R}} \phi(t)dt \right) \phi_0(x) + \chi(x) $$
où $\chi(x) = \phi(x) - \left( \int_{\mathbb{R}} \phi(t)dt \right) \phi_0(x)$.
Vérifions l'intégrale de $\chi$ :
$$ \int_{\mathbb{R}} \chi(x) dx = \int_{\mathbb{R}} \phi(x) dx - \left( \int_{\mathbb{R}} \phi(t)dt \right) \int_{\mathbb{R}} \phi_0(x) dx = \int_{\mathbb{R}} \phi(x) dx - \int_{\mathbb{R}} \phi(x) dx \times 1 = 0 $$
Puisque l'intégrale de $\chi$ est nulle, la fonction définie par $\psi(x) = \int_{-\infty}^x \chi(t) dt$ est à support compact, donc $\psi \in \mathcal{D}(\mathbb{R})$ et $\psi' = \chi$.

Calculons maintenant l'action de $T$ sur $\phi$ :
$$ \langle T, \phi \rangle = \left\langle T, \left( \int \phi \right) \phi_0 + \chi \right\rangle = \left( \int \phi \right) \langle T, \phi_0 \rangle + \langle T, \chi \rangle $$
On sait que $\chi = \psi'$. Donc :
$$ \langle T, \chi \rangle = \langle T, \psi' \rangle = - \langle T', \psi \rangle $$
Mais par hypothèse, $T' = 0$. Donc $\langle T, \chi \rangle = 0$.
Il reste :
$$ \langle T, \phi \rangle = \left( \int_{\mathbb{R}} \phi(t)dt \right) \langle T, \phi_0 \rangle $$
En posant la constante $C = \langle T, \phi_0 \rangle$, on obtient bien :
$$ \langle T, \phi \rangle = C \int_{\mathbb{R}} \phi(x) dx $$
$T$ est donc la distribution associée à la fonction constante $f(x) = C$.
