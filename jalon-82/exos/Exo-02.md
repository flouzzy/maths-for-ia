# Exercice 2 : Action d'une combinaison de Diracs
**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé
On considère la distribution $T = \delta_{\pi} - 2\delta_{-\pi} + 3\delta_0$. Calculer $\langle T, \varphi \rangle$ pour la fonction test $\varphi(x) = \sin(x) \cos(x)$.

## Correction Détaillée
1. Par linéarité des distributions, l'action de $T$ sur $\varphi$ se décompose comme suit :
   $$ \langle T, \varphi \rangle = \langle \delta_{\pi}, \varphi \rangle - 2\langle \delta_{-\pi}, \varphi \rangle + 3\langle \delta_0, \varphi \rangle $$
2. Par définition de la distribution de Dirac $\delta_a$, $\langle \delta_a, \varphi \rangle = \varphi(a)$.
3. On remplace par les évaluations de $\varphi$ aux points donnés :
   $$ \langle T, \varphi \rangle = \varphi(\pi) - 2\varphi(-\pi) + 3\varphi(0) $$
4. Calculons les valeurs de $\varphi$ à ces points :
   - Pour $x = \pi$ : $\varphi(\pi) = \sin(\pi) \cos(\pi) = 0 \times (-1) = 0$.
   - Pour $x = -\pi$ : $\varphi(-\pi) = \sin(-\pi) \cos(-\pi) = 0 \times (-1) = 0$.
   - Pour $x = 0$ : $\varphi(0) = \sin(0) \cos(0) = 0 \times 1 = 0$.
5. En remplaçant ces valeurs dans l'expression de $\langle T, \varphi \rangle$ :
   $$ \langle T, \varphi \rangle = 0 - 2(0) + 3(0) = 0 $$
6. L'action de la distribution $T$ sur cette fonction test particulière est donc nulle.
