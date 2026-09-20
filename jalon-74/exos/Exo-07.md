### Exercice 7 : Inégalité de Minkowski dans $\ell^p$ \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Vérifier l'inégalité de Minkowski pour les suites $u = (1, 1/2, 0, \dots)$ et $v = (0, 1/2, 1/3, 0, \dots)$ dans l'espace $\ell^2$.

**Correction Détaillée :**
1. L'espace $\ell^2$ est l'espace des suites de carré sommable. La norme est $\|u\|_2 = \sqrt{\sum |u_i|^2}$.
2. Calcul de la norme de $u$ : $\|u\|_2 = \sqrt{1^2 + (1/2)^2} = \sqrt{1 + 1/4} = \sqrt{5/4} \approx 1.118$.
3. Calcul de la norme de $v$ : $\|v\|_2 = \sqrt{0^2 + (1/2)^2 + (1/3)^2} = \sqrt{1/4 + 1/9} = \sqrt{13/36} \approx 0.601$.
4. Somme des normes : $\|u\|_2 + \|v\|_2 = \frac{\sqrt{5}}{2} + \frac{\sqrt{13}}{6} \approx 1.118 + 0.601 = 1.719$.
5. Vecteur somme $u+v$ : $u+v = (1, 1, 1/3, 0, \dots)$.
6. Calcul de la norme de $u+v$ : $\|u+v\|_2 = \sqrt{1^2 + 1^2 + (1/3)^2} = \sqrt{2 + 1/9} = \sqrt{19/9} = \frac{\sqrt{19}}{3} \approx 1.453$.
7. On vérifie bien que $\|u+v\|_2 \le \|u\|_2 + \|v\|_2$, car $1.453 \le 1.719$. L'inégalité triangulaire (Minkowski $p=2$) est respectée.
