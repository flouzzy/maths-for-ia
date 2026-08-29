# Exercice 8 : Intégrale de la loi exponentielle en probabilités $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
En théorie des probabilités, on cherche à calculer l'espérance d'une variable aléatoire positive $X$. Montrer que $E[X] = \int_0^\infty P(X > t) dt$ en utilisant le TCM.

## Correction Détaillée
1. Soit $X$ une variable aléatoire réelle positive de loi $P_X$ (mesure sur $\mathbb{R}_+$).
   Par définition, $E[X] = \int_0^\infty x dP_X(x)$.
2. Écrivons $x = \int_0^x 1 dt = \int_0^\infty \mathbf{1}_{\{t < x\}} dt$.
3. Substituons dans l'espérance :
   $E[X] = \int_0^\infty \left( \int_0^\infty \mathbf{1}_{\{t < x\}} dt \right) dP_X(x)$.
4. L'intégrande $\mathbf{1}_{\{t < x\}}$ est une fonction mesurable positive sur $\mathbb{R}_+ \times \mathbb{R}_+$. Le théorème de Tonelli (qui repose fondamentalement sur Beppo Levi pour intervertir des sommes continues) nous permet d'intervertir les intégrales :
   $$ E[X] = \int_0^\infty \left( \int_0^\infty \mathbf{1}_{\{t < x\}} dP_X(x) \right) dt $$
5. Or, l'intégrale intérieure est exactement la probabilité que $X > t$ :
   $$ \int_0^\infty \mathbf{1}_{\{x > t\}} dP_X(x) = P(X > t) $$
6. On obtient donc :
   $$ E[X] = \int_0^\infty P(X > t) dt $$
7. Ce résultat classique est une application élégante de la robustesse des intégrales de fonctions positives (TCM/Tonelli).
