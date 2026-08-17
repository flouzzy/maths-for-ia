## Exercice 5 : Mesure de Lebesgue et Hahn-Banach \quad $\bigstar\bigstar\bigstar\star\star$

Lors de la preuve de Cybenko, justifier formellement pourquoi l'espace fonctionnel généré $S$ est dense si et seulement si l'unique mesure $\mu$ l'annulant est la mesure nulle.

**Correction :**
Par le théorème de Hahn-Banach, si un sous-espace $S$ d'un espace vectoriel normé (ici $\mathcal{C}(I_n)$ avec la norme infinie) n'est pas dense, alors son adhérence $\overline{S}$ est un sous-espace strict fermé.
Il existe alors une forme linéaire continue non nulle $L$ telle que $\ker(L) \supset \overline{S}$, c'est-à-dire $L(f) = 0$ pour tout $f \in S$.
Le théorème de Riesz-Markov-Kakutani stipule que pour l'espace dual de $\mathcal{C}(I_n)$, toute forme linéaire continue $L$ s'exprime de manière unique par une intégrale contre une mesure de Borel régulière signée $\mu$ finie : $L(f) = \int f d\mu$.
Ainsi, $\overline{S}$ est strict équivaut à l'existence d'une mesure $\mu \neq 0$ telle que $\int \sigma(w^T x + b) d\mu(x) = 0$ pour tout $w, b$.
Par contraposée, si la seule mesure vérifiant cette propriété est $\mu = 0$, alors la forme linéaire est nulle, et aucune telle forme n'existe pour séparer un point extérieur de $\overline{S}$. Donc $\overline{S} = \mathcal{C}(I_n)$, soit $S$ dense.
