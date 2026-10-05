# Exercice 10 : Résolution d'une équation distributionnelle simple
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Trouver toutes les distributions $T \in \mathcal{D}'(\mathbb{R})$ vérifiant l'équation $x \cdot T = 0$. (Indice : utiliser une fonction plateau $\theta \in \mathcal{D}(\mathbb{R})$ avec $\theta(0) = 1$, et écrire toute fonction test $\varphi$ sous la forme $\varphi(x) = \varphi(0)\theta(x) + x\psi(x)$ avec $\psi \in \mathcal{D}(\mathbb{R})$).

## Correction Détaillée
1. Soit $T$ une distribution telle que $x \cdot T = 0$. Par définition du produit par une fonction régulière, cela signifie que pour toute fonction test $\phi$, $\langle x \cdot T, \phi \rangle = \langle T, x\phi \rangle = 0$.
2. Soit $\varphi \in \mathcal{D}(\mathbb{R})$ une fonction test quelconque.
3. Fixons une fonction test $\theta \in \mathcal{D}(\mathbb{R})$ telle que $\theta(x) = 1$ sur un voisinage de $0$. (Cela implique $\theta(0) = 1$).
4. On peut toujours écrire l'identité algébrique :
   $$ \varphi(x) = \varphi(0)\theta(x) + (\varphi(x) - \varphi(0)\theta(x)) $$
5. Étudions le terme $r(x) = \varphi(x) - \varphi(0)\theta(x)$. Cette fonction appartient à $\mathcal{D}(\mathbb{R})$ (combinaison linéaire de fonctions $C^\infty$ à support compact).
6. De plus, évaluons en $0$ : $r(0) = \varphi(0) - \varphi(0)\theta(0) = \varphi(0) - \varphi(0) = 0$.
7. Puisque $r(0) = 0$ et que $r \in C^\infty$, le théorème de Taylor avec reste intégral (ou simplement le lemme de division de Hadamard) garantit l'existence d'une fonction $\psi \in C^\infty(\mathbb{R})$ telle que $r(x) = x\psi(x)$.
8. Comme $r$ est à support compact, $\psi$ l'est aussi (hors du support de $r$, $x\psi(x) = 0$, donc $\psi(x) = 0$ pour $x \neq 0$). Ainsi $\psi \in \mathcal{D}(\mathbb{R})$.
9. On a donc la décomposition :
   $$ \varphi(x) = \varphi(0)\theta(x) + x\psi(x) $$
10. Évaluons l'action de la distribution $T$ sur la fonction test $\varphi$ :
    $$ \langle T, \varphi \rangle = \langle T, \varphi(0)\theta + x\psi \rangle $$
11. Par linéarité de la distribution $T$ :
    $$ \langle T, \varphi \rangle = \varphi(0)\langle T, \theta \rangle + \langle T, x\psi \rangle $$
12. Par l'hypothèse de départ, l'action de $T$ sur une fonction de la forme $x \mapsto x\psi(x)$ est nulle, donc $\langle T, x\psi \rangle = 0$.
13. Il reste :
    $$ \langle T, \varphi \rangle = \varphi(0) \langle T, \theta \rangle $$
14. La quantité $\langle T, \theta \rangle$ est un nombre complexe fixe, appelons-le $C$.
15. L'équation devient :
    $$ \langle T, \varphi \rangle = C \varphi(0) = C \langle \delta_0, \varphi \rangle = \langle C\delta_0, \varphi \rangle $$
16. Puisque cela est vrai pour toute fonction test $\varphi$, on conclut que la distribution $T$ est proportionnelle à la masse de Dirac.
17. Conclusion : les solutions de l'équation $x \cdot T = 0$ sont exactement les distributions de la forme $T = C\delta_0$, où $C$ est une constante arbitraire.
