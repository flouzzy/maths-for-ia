## Exercice 10 : Égalité presque partout \quad $$\bigstar\bigstar\bigstar\bigstar\star$$

**Énoncé :**
Soient $f, g \in \mathcal{M}_+$ telles que $f = g$ presque partout (i.e. $\mu(\{x \mid f(x) \neq g(x)\}) = 0$).
Montrer que $\int_X f \, d\mu = \int_X g \, d\mu$.

**Correction :**
1. Soit $N = \{x \in X \mid f(x) \neq g(x)\}$. Par hypothèse, $\mu(N) = 0$.
2. Définissons $f_1 = f \mathbf{1}_{N^c}$ et $f_2 = f \mathbf{1}_N$. Ainsi $f = f_1 + f_2$.
3. De même, $g = g_1 + g_2$ avec $g_1 = g \mathbf{1}_{N^c}$ et $g_2 = g \mathbf{1}_N$.
4. Sur $N^c$, on a $f = g$, donc $f_1 = g_1$ pour tout $x \in X$.
5. On va montrer que pour toute fonction $h \in \mathcal{M}_+$ s'annulant sur $N^c$ (comme $f_2$ et $g_2$), on a $\int_X h \, d\mu = 0$.
   En effet, si $s \le h$ est étagée, $s = \sum a_i \mathbf{1}_{A_i}$, puisque $s = 0$ sur $N^c$, les $A_i$ correspondant à $a_i > 0$ sont inclus dans $N$.
   Leur mesure est donc nulle ($\mu(A_i) \le \mu(N) = 0$). D'où $\int s \, d\mu = 0$ et le sup est nul.
6. Le théorème de linéarité sur $\mathcal{M}_+$ (qui sera prouvé formellement via Beppo-Levi, mais anticipons sa structure) permet d'écrire l'intégrale comme une décomposition sur les partitions de l'espace : pour une fonction étagée, l'intégrale sur un ensemble de mesure nulle ne contribue rien.
7. Ainsi, formellement (par définition stricte) :
   $\int f \, d\mu = \sup \{ \int s \, d\mu \mid s \le f \}$.
   Soit $s \le f$. Posons $s' = s \mathbf{1}_{N^c}$. On a $s = s'$ presque partout, donc $\int s \, d\mu = \int s' \, d\mu$.
   De plus $s' \le f \mathbf{1}_{N^c} = g \mathbf{1}_{N^c} \le g$.
   Donc $\int s \, d\mu = \int s' \, d\mu \le \int g \, d\mu$.
8. En prenant le supremum sur $s \le f$, on trouve $\int_X f \, d\mu \le \int_X g \, d\mu$.
9. Par symétrie, en échangeant les rôles de $f$ et $g$, on obtient $\int_X g \, d\mu \le \int_X f \, d\mu$.
10. D'où l'égalité stricte $\int_X f \, d\mu = \int_X g \, d\mu$.
