# Exercice 8: Bidual et forme spécifique
## Énoncé
Soit $E$ un espace vectoriel de dimension finie. Soit $\alpha \in E$. On définit l'application d'évaluation sur $E^*$ :
$\text{ev}_\alpha : E^* \to \mathbb{K}$
$\varphi \mapsto \varphi(\alpha)$
Montrer rigoureusement que si $\text{ev}_\alpha = 0_{E^{**}}$, alors $\alpha = 0_E$.


## Correction détaillée
L'application $\text{ev}_\alpha$ est l'image du vecteur $\alpha$ par l'isomorphisme canonique $\Psi : E \to E^{**}$.
Supposons que $\text{ev}_\alpha = 0_{E^{**}}$.
Par définition, cela signifie que pour toute forme linéaire $\varphi \in E^*$, on a $\text{ev}_\alpha(\varphi) = 0$, soit $\varphi(\alpha) = 0$.

Procédons par l'absurde. Supposons que $\alpha \neq 0_E$.
Puisque $\alpha$ est un vecteur non nul d'un espace vectoriel de dimension finie $n$, on peut, par le théorème de la base incomplète, construire une base $\mathcal{B} = (e_1, e_2, \dots, e_n)$ de $E$ telle que $e_1 = \alpha$.
Soit $\mathcal{B}^* = (e_1^*, e_2^*, \dots, e_n^*)$ la base duale associée à $\mathcal{B}$.
Par définition de la base duale, la forme linéaire $e_1^*$ vérifie $e_1^*(e_1) = 1$.
Or, $e_1 = \alpha$, donc $e_1^*(\alpha) = 1 \neq 0$.
Nous avons trouvé une forme linéaire spécifique $\varphi = e_1^* \in E^*$ telle que $\varphi(\alpha) \neq 0$.
Ceci contredit l'hypothèse selon laquelle $\forall \varphi \in E^*, \varphi(\alpha) = 0$.

Par conséquent, notre supposition de départ $\alpha \neq 0_E$ est fausse.
On conclut que nécessairement, $\alpha = 0_E$.
Cela confirme que le noyau de l'application canonique dans le bidual est réduit à $\{0\}$, assurant son injectivité.
