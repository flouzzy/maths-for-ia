# Exercice 1 : Vérification de la Continuité d'une Fonction Affine en un Point par la Définition Epsilon-Delta

**Jalon 18 : Continuité des fonctions d'une variable réelle**
**Difficulté :** $\star \rule{0.5cm}{0.05cm}\rule{0.5cm}{0.05cm}\rule{0.5cm}{0.05cm}\rule{0.5cm}{0.05cm}$ (1/5)

---

### Énoncé

Mes chers étudiants,

Pour ce premier exercice sur la continuité, nous allons revenir aux fondements mêmes de cette notion cruciale. La compréhension rigoureuse de la définition formelle est la pierre angulaire de toute étude avancée en analyse.

**Rappel théorique :**
Soit $f: I \to \mathbb{R}$ une fonction définie sur un intervalle $I \subset \mathbb{R}$, et soit $x_0 \in I$.
On dit que la fonction $f$ est **continue au point $x_0$** si et seulement si :
Pour tout $\varepsilon > 0$, il existe un $\delta > 0$ tel que, pour tout $x \in I$, si $|x - x_0| < \delta$, alors $|f(x) - f(x_0)| < \varepsilon$.

**Question :**
Considérons la fonction $f: \mathbb{R} \to \mathbb{R}$ définie par $f(x) = 3x + 2$.
En utilisant la définition $\varepsilon-\delta$ de la continuité, démontrez que la fonction $f$ est continue au point $x_0 = 1$.

---

### Corrigé

Nous allons suivre scrupuleusement la définition $\varepsilon-\delta$ pour démontrer la continuité de $f$ au point $x_0 = 1$.

1.  **Identification des éléments de la définition :**
    *   La fonction est $f(x) = 3x + 2$.
    *   Le point d'intérêt est $x_0 = 1$.
    *   L'intervalle de définition est $I = \mathbb{R}$.

2.  **Calcul de $f(x_0)$ :**
    Commençons par évaluer la fonction au point $x_0 = 1$.
    $f(1) = 3(1) + 2 = 3 + 2 = 5$.

3.  **Mise en place de l'inégalité à démontrer :**
    Selon la définition, nous devons montrer que pour tout $\varepsilon > 0$, il existe un $\delta > 0$ tel que si $|x - 1| < \delta$, alors $|f(x) - f(1)| < \varepsilon$.

4.  **Analyse de l'expression $|f(x) - f(1)|$ :**
    Substituons les expressions de $f(x)$ et $f(1)$ dans l'inégalité :
    $|f(x) - f(1)| = |(3x + 2) - 5|$
    $|f(x) - f(1)| = |3x - 3|$

    Nous pouvons factoriser le terme $3$ dans l'expression :
    $|f(x) - f(1)| = |3(x - 1)|$

    En utilisant la propriété de la valeur absolue $|ab| = |a||b|$, nous obtenons :
    $|f(x) - f(1)| = |3| \cdot |x - 1|$
    $|f(x) - f(1)| = 3|x - 1|$

5.  **Établissement du lien entre $|x - x_0|$ et $|f(x) - f(x_0)|$ :**
    Nous voulons que $3|x - 1| < \varepsilon$.
    Pour atteindre cet objectif, nous devons choisir $\delta$ de manière appropriée.
    Si nous divisons l'inégalité $3|x - 1| < \varepsilon$ par $3$ (qui est un nombre positif), nous obtenons :
    $|x - 1| < \frac{\varepsilon}{3}$

6.  **Choix de $\delta$ :**
    Cette dernière inégalité nous suggère un choix pour $\delta$. Si nous choisissons $\delta = \frac{\varepsilon}{3}$, alors l'implication désirée devrait se vérifier.
    Puisque $\varepsilon > 0$, $\frac{\varepsilon}{3}$ est également strictement positif, ce qui est une condition requise pour $\delta$.

7.  **Rédaction formelle de la démonstration :**
    Soit $\varepsilon$ un nombre réel strictement positif ($\varepsilon > 0$).
    Nous cherchons à trouver un $\delta > 0$ tel que si $|x - 1| < \delta$, alors $|f(x) - f(1)| < \varepsilon$.

    Posons $\delta = \frac{\varepsilon}{3}$. Puisque $\varepsilon > 0$, nous avons bien $\delta > 0$.

    Maintenant, supposons que $x \in \mathbb{R}$ est tel que $|x - 1| < \delta$.
    En substituant la valeur de $\delta$, nous avons :
    $|x - 1| < \frac{\varepsilon}{3}$

    Multiplions les deux côtés de cette inégalité par $3$ (qui est un nombre positif, donc l'inégalité est préservée) :
    $3|x - 1| < 3 \cdot \frac{\varepsilon}{3}$
    $3|x - 1| < \varepsilon$

    Nous avons précédemment établi que $3|x - 1| = |3(x - 1)| = |3x - 3| = |(3x + 2) - 5| = |f(x) - f(1)|$.
    Donc, nous pouvons écrire :
    $|f(x) - f(1)| < \varepsilon$

    Nous avons ainsi démontré que pour tout $\varepsilon > 0$, il existe un $\delta = \frac{\varepsilon}{3} > 0$ tel que si $|x - 1| < \delta$, alors $|f(x) - f(1)| < \varepsilon$.

    Par conséquent, selon la définition $\varepsilon-\delta$, la fonction $f(x) = 3x + 2$ est continue au point $x_0 = 1$.

---