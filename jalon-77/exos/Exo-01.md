# Exercice 1 : Approximation d'une fonction simple dans $L^1$

**Niveau :** \bigstar\star\star\star\star

**Énoncé :**
Soit $f(x) = \mathbf{1}_{[0, 1]}(x) - \mathbf{1}_{[2, 3]}(x)$. Montrer que $f \in L^1(\mathbb{R})$ (muni de la mesure de Lebesgue). Construire explicitement une fonction continue à support compact $g_\varepsilon$ telle que $\|f - g_\varepsilon\|_1 \le \varepsilon$.

**Correction Détaillée :**
1. **Intégrabilité :**
   $f$ est une fonction étagée. Calculons sa norme $L^1$ :
   $\|f\|_1 = \int_{\mathbb{R}} |f(x)| dx = \int_0^1 1 dx + \int_2^3 |-1| dx = 1 + 1 = 2 < +\infty$.
   Donc $f \in L^1(\mathbb{R})$.

2. **Construction de $g_\varepsilon$ :**
   On va construire $g_\varepsilon$ en lissant les sauts de $f$ à l'aide de fonctions affines sur des intervalles de longueur $\delta > 0$ à définir.
   Posons $g_\varepsilon(x) = 0$ en dehors de $[-\delta, 1+\delta] \cup [2-\delta, 3+\delta]$.
   Sur $[0, 1]$, $g_\varepsilon(x) = 1$. Sur $[2, 3]$, $g_\varepsilon(x) = -1$.
   Pour relier de $0$ à $1$ autour de $x=0$, on pose $g_\varepsilon(x) = 1 + \frac{x}{\delta}$ pour $x \in [-\delta, 0]$.
   Pour relier de $1$ à $0$ autour de $x=1$, on pose $g_\varepsilon(x) = 1 - \frac{x-1}{\delta}$ pour $x \in [1, 1+\delta]$.
   De même, on relie continûment vers $-1$ sur $[2-\delta, 2]$ et on remonte à $0$ sur $[3, 3+\delta]$.
   La fonction $g_\varepsilon$ est par construction continue, et son support est inclus dans $[-1, 4]$ (si $\delta \le 1$), donc compact.

3. **Calcul de l'erreur :**
   L'erreur n'a lieu que sur les zones de "pente".
   $\|f - g_\varepsilon\|_1 = \int_{-\delta}^0 |0 - (1+x/\delta)| dx + \int_1^{1+\delta} |0 - (1-(x-1)/\delta)| dx + \text{symétriques}$.
   L'aire sous chaque "triangle" est $\frac{\text{base} \times \text{hauteur}}{2} = \frac{\delta \times 1}{2} = \frac{\delta}{2}$.
   Il y a 4 triangles, donc l'erreur totale est $4 \times \frac{\delta}{2} = 2\delta$.
   Pour avoir $\|f - g_\varepsilon\|_1 \le \varepsilon$, il suffit de choisir $\delta = \frac{\varepsilon}{2}$.
