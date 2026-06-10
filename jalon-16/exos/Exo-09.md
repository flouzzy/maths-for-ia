# Exercice 09 : Approximation d'intégrales par des sommes
**Niveau :** Très Difficile (Concours)
**Notion ciblée :** Évaluation asymptotique du reste d'une série convergente.

## Énoncé
Soit $R_N = \sum_{n=N+1}^\infty \frac{1}{n^2}$.
Donner un équivalent simple de $R_N$ quand $N \to +\infty$.

## Correction Détaillée
1. **Vérification de l'existence :**
   La série $\sum 1/n^2$ converge (Riemann, $\alpha=2$), donc le reste $R_N$ tend vers $0$ et est bien défini.

2. **Encadrement par des intégrales :**
   La fonction $f(t) = 1/t^2$ est décroissante et positive.
   Par conséquent, pour un entier $n$, pour tout $t \in [n, n+1]$ :
   $$f(n+1) \le f(t) \le f(n)$$
   En intégrant cette relation de $n$ à $n+1$ :
   $$\frac{1}{(n+1)^2} \le \int_n^{n+1} \frac{1}{t^2} dt \le \frac{1}{n^2}$$

3. **Sommation des encadrements :**
   On somme les inégalités de $n=N+1$ à l'infini (les séries et intégrales convergent).
   Partie gauche de l'inégalité de droite :
   $$\sum_{n=N+1}^\infty \int_n^{n+1} \frac{1}{t^2} dt \le \sum_{n=N+1}^\infty \frac{1}{n^2} = R_N$$
   La somme d'intégrales se télescope :
   $$\int_{N+1}^\infty \frac{1}{t^2} dt \le R_N$$

   Pour l'autre côté de l'inégalité (décalage d'indice), on somme la partie gauche de $n=N$ :
   $$\sum_{n=N}^\infty \frac{1}{(n+1)^2} \le \sum_{n=N}^\infty \int_n^{n+1} \frac{1}{t^2} dt$$
   $$R_N = \sum_{k=N+1}^\infty \frac{1}{k^2} \le \int_N^\infty \frac{1}{t^2} dt$$

4. **Calcul des intégrales :**
   $$\int_A^\infty t^{-2} dt = \left[ -t^{-1} \right]_A^\infty = \frac{1}{A}$$
   On injecte dans l'encadrement :
   $$\frac{1}{N+1} \le R_N \le \frac{1}{N}$$

5. **Déduction de l'équivalent :**
   Puisque $\lim_{N \to \infty} \frac{N}{N+1} = 1$, les termes bornant $R_N$ sont tous deux équivalents à $\frac{1}{N}$.
   Le théorème des gendarmes sur l'équivalence garantit que :
   $$R_N \sim_{+\infty} \frac{1}{N}$$
