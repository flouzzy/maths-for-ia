# Exercice 10 - Exploration Approfondie de la Continuité des Fonctions Réelles

Cet exercice est conçu pour tester votre compréhension approfondie et votre capacité à appliquer rigoureusement les concepts de continuité des fonctions d'une variable réelle. Chaque partie exige une démonstration formelle et détaillée, respectant la règle de Zéro Ellipse Mathématique.

---

**Partie A : Continuité en un point par la définition $\epsilon-\delta$.**

Soit la fonction $f: \mathbb{R} \to \mathbb{R}$ définie par :
$$ f(x) = \begin{cases} \frac{\sin(x^2)}{x} & \text{si } x \neq 0 \\ 0 & \text{si } x = 0 \end{cases} $$
Démontrez, en utilisant la définition formelle $(\epsilon-\delta)$ de la continuité, que la fonction $f$ est continue au point $x_0 = 0$.

---

**Partie B : Continuité uniforme.**

Soit la fonction $g: [0, +\infty) \to \mathbb{R}$ définie par $g(x) = \sqrt{x}$.
Démontrez, en utilisant la définition formelle de la continuité uniforme, que la fonction $g$ est uniformément continue sur l'intervalle $[0, +\infty)$.

---

**Partie C : Théorèmes des valeurs intermédiaires et des bornes atteintes.**

1.  Soit $h: [0,1] \to [0,1]$ une fonction continue. Démontrez qu'il existe au moins un point $c \in [0,1]$ tel que $h(c) = c$. (Ce point $c$ est appelé un point fixe de $h$).
2.  Soit $f: [a,b] \to \mathbb{R}$ une fonction continue, où $a, b \in \mathbb{R}$ avec $a < b$. Soient $y_1, y_2, \dots, y_n$ des points quelconques de l'intervalle $[a,b]$, où $n \in \mathbb{N}^*$. Démontrez qu'il existe un point $c \in [a,b]$ tel que $f(c) = \frac{f(y_1) + f(y_2) + \dots + f(y_n)}{n}$.

---

**Partie D : Équation fonctionnelle de Cauchy.**

Trouvez toutes les fonctions $f: \mathbb{R} \to \mathbb{R}$ qui sont continues et qui satisfont l'équation fonctionnelle suivante pour tous $x, y \in \mathbb{R}$ :
$$ f(x+y) = f(x) + f(y) $$
(Cette équation est connue sous le nom d'équation fonctionnelle de Cauchy).

---

# Correction de l'Exercice 10

---

**Partie A : Continuité en un point par la définition $\epsilon-\delta$.**

Pour démontrer que la fonction $f$ est continue au point $x_0 = 0$, nous devons montrer que pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que pour tout $x \in \mathbb{R}$, si $|x - 0| < \delta$, alors $|f(x) - f(0)| < \epsilon$.
Puisque $f(0) = 0$, cette condition se simplifie à : pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que pour tout $x \in \mathbb{R}$, si $|x| < \delta$, alors $|f(x)| < \epsilon$.

Soit $\epsilon > 0$ un nombre réel arbitraire. Nous cherchons à déterminer un $\delta > 0$ approprié.

Considérons deux cas pour $x$:

1.  **Cas $x=0$ :**
    Dans ce cas, $|f(0) - f(0)| = |0 - 0| = 0$. Puisque $0 < \epsilon$ pour tout $\epsilon > 0$, la condition est satisfaite pour $x=0$.

2.  **Cas $x \neq 0$ :**
    Dans ce cas, $f(x) = \frac{\sin(x^2)}{x}$. Nous pouvons réécrire $f(x)$ en multipliant et divisant par $x$ (ce qui est permis car $x \neq 0$) :
    $$ f(x) = \frac{\sin(x^2)}{x^2} \cdot x $$
    Nous voulons que $|f(x)| < \epsilon$. En utilisant la propriété du module, nous avons :
    $$ |f(x)| = \left|\frac{\sin(x^2)}{x^2} \cdot x\right| = \left|\frac{\sin(x^2)}{x^2}\right| \cdot |x| $$
    Nous savons que $\lim_{u \to 0} \frac{\sin u}{u} = 1$.
    Par la définition de la limite, pour $\epsilon_0 = \frac{1}{2} > 0$, il existe un $\delta_0 > 0$ tel que si $0 < |u| < \delta_0$, alors $\left|\frac{\sin u}{u} - 1\right| < \frac{1}{2}$.
    Cette inégalité implique :
    $$ -\frac{1}{2} < \frac{\sin u}{u} - 1 < \frac{1}{2} $$
    En ajoutant $1$ à toutes les parties de l'inégalité, nous obtenons :
    $$ \frac{1}{2} < \frac{\sin u}{u} < \frac{3}{2} $$
    Par conséquent, pour $0 < |u| < \delta_0$, nous avons $\left|\frac{\sin u}{u}\right| < \frac{3}{2}$.

    Appliquons ceci avec $u = x^2$. Si $0 < |x^2| < \delta_0$, alors $\left|\frac{\sin(x^2)}{x^2}\right| < \frac{3}{2}$.
    La condition $0 < |x^2| < \delta_0$ est équivalente à $0 < |x| < \sqrt{\delta_0}$.
    Posons $\delta_1 = \sqrt{\delta_0}$.
    Ainsi, pour tout $x$ tel que $0 < |x| < \delta_1$, nous avons $\left|\frac{\sin(x^2)}{x^2}\right| < \frac{3}{2}$.

    Maintenant, nous pouvons majorer $|f(x)|$ pour $0 < |x| < \delta_1$:
    $$ |f(x)| = \left|\frac{\sin(x^2)}{x^2}\right| \cdot |x| < \frac{3}{2} |x| $$
    Nous voulons que cette expression soit inférieure à $\epsilon$. C'est-à-dire, nous voulons $\frac{3}{2} |x| < \epsilon$.
    Ceci est équivalent à $|x| < \frac{2\epsilon}{3}$.

    Pour satisfaire toutes les conditions, nous choisissons $\delta = \min\left(\delta_1, \frac{2\epsilon}{3}\right)$.
    Avec ce choix de $\delta$, si $|x| < \delta$:
    *   Si $x=0$, nous avons déjà montré que $|f(0)-f(0)| = 0 < \epsilon$.
    *   Si $x \neq 0$, alors $0 < |x| < \delta$.
        Puisque $\delta \le \delta_1$, nous avons $0 < |x| < \delta_1$, ce qui implique $\left|\frac{\sin(x^2)}{x^2}\right| < \frac{3}{2}$.
        Puisque $\delta \le \frac{2\epsilon}{3}$, nous avons $|x| < \frac{2\epsilon}{3}$.
        En combinant ces deux inégalités, nous obtenons :
        $$ |f(x) - f(0)| = |f(x)| = \left|\frac{\sin(x^2)}{x^2}\right| \cdot |x| < \frac{3}{2} \cdot \frac{2\epsilon}{3} = \epsilon $$
    Dans tous les cas, si $|x| < \delta$, alors $|f(x) - f(0)| < \epsilon$.
    Par conséquent, la fonction $f$ est continue au point $x_0 = 0$.

---

**Partie B : Continuité uniforme.**

Une fonction $g: I \to \mathbb{R}$ est uniformément continue sur un intervalle $I$ si pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que pour tous $x, y \in I$, si $|x-y| < \delta$, alors $|g(x) - g(y)| < \epsilon$.

Soit $\epsilon > 0$ un nombre réel arbitraire. Nous cherchons à déterminer un $\delta > 0$ tel que pour tous $x, y \in [0, +\infty)$, si $|x-y| < \delta$, alors $|\sqrt{x} - \sqrt{y}| < \epsilon$.

Considérons la quantité $|\sqrt{x} - \sqrt{y}|$.
Nous allons utiliser l'inégalité suivante : pour tous $x, y \ge 0$, $|\sqrt{x} - \sqrt{y}| \le \sqrt{|x-y|}$.
Démontrons cette inégalité :
Sans perte de généralité, supposons $x \ge y \ge 0$. Alors $\sqrt{x} \ge \sqrt{y} \ge 0$.
L'inégalité à prouver devient $\sqrt{x} - \sqrt{y} \le \sqrt{x-y}$.
Puisque les deux membres de l'inégalité sont non-négatifs, nous pouvons élever au carré sans changer le sens de l'inégalité :
$$ (\sqrt{x} - \sqrt{y})^2 \le (\sqrt{x-y})^2 $$
$$ x + y - 2\sqrt{xy} \le x-y $$
En soustrayant $x$ des deux côtés :
$$ y - 2\sqrt{xy} \le -y $$
En ajoutant $y$ aux deux côtés :
$$ 2y - 2\sqrt{xy} \le 0 $$
En divisant par $2$ :
$$ y - \sqrt{xy} \le 0 $$
$$ y \le \sqrt{xy} $$
Puisque $y \ge 0$, nous pouvons élever au carré les deux côtés :
$$ y^2 \le xy $$
En soustrayant $xy$ des deux côtés :
$$ y^2 - xy \le 0 $$
En factorisant $y$ :
$$ y(y-x) \le 0 $$
Puisque nous avons supposé $x \ge y$, il s'ensuit que $y-x \le 0$.
De plus, $y \ge 0$.
Le produit d'un nombre non-négatif ($y$) et d'un nombre non-positif ($y-x$) est toujours non-positif.
Donc, $y(y-x) \le 0$ est vrai.
L'inégalité $|\sqrt{x} - \sqrt{y}| \le \sqrt{|x-y|}$ est donc démontrée pour tous $x, y \ge 0$.

Maintenant, revenons à la preuve de la continuité uniforme.
Nous voulons que $|\sqrt{x} - \sqrt{y}| < \epsilon$.
En utilisant l'inégalité que nous venons de prouver, il suffit de s'assurer que $\sqrt{|x-y|} < \epsilon$.
Pour que $\sqrt{|x-y|} < \epsilon$, nous devons avoir $|x-y| < \epsilon^2$.

Nous choisissons donc $\delta = \epsilon^2$.
Soient $x, y \in [0, +\infty)$ tels que $|x-y| < \delta$.
Alors, par notre choix de $\delta$, nous avons $|x-y| < \epsilon^2$.
En prenant la racine carrée des deux côtés (les deux côtés sont non-négatifs) :
$$ \sqrt{|x-y|} < \sqrt{\epsilon^2} $$
$$ \sqrt{|x-y|} < \epsilon $$
En utilisant l'inégalité démontrée précédemment, $|\sqrt{x} - \sqrt{y}| \le \sqrt{|x-y|}$, nous obtenons :
$$ |\sqrt{x} - \sqrt{y}| < \epsilon $$
Ainsi, pour tout $\epsilon > 0$, nous avons trouvé un $\delta = \epsilon^2 > 0$ tel que pour tous $x, y \in [0, +\infty)$, si $|x-y| < \delta$, alors $|g(x) - g(y)| < \epsilon$.
Par conséquent, la fonction $g(x) = \sqrt{x}$ est uniformément continue sur l'intervalle $[0, +\infty)$.

---

**Partie C : Théorèmes des valeurs intermédiaires et des bornes atteintes.**

**1. Point fixe pour $h: [0,1] \to [0,1]$ continue.**

Soit $h: [0,1] \to [0,1]$ une fonction continue. Nous voulons démontrer qu'il existe au moins un point $c \in [0,1]$ tel que $h(c) = c$.
Pour cela, nous allons introduire une fonction auxiliaire $k(x)$ et appliquer le Théorème des Valeurs Intermédiaires (TVI).

Définissons la fonction $k: [0,1] \to \mathbb{R}$ par $k(x) = h(x) - x$.
*   **Continuité de $k(x)$ :** La fonction $h(x)$ est continue sur $[0,1]$ par hypothèse. La fonction $j(x) = x$ (la fonction identité) est continue sur $[0,1]$ car c'est un polynôme. La différence de deux fonctions continues est continue. Par conséquent, $k(x) = h(x) - x$ est continue sur l'intervalle fermé et borné $[0,1]$.

*   **Évaluation aux bornes de l'intervalle :**
    *   Calculons $k(0)$:
        $k(0) = h(0) - 0 = h(0)$.
        Puisque $h$ est une fonction de $[0,1]$ vers $[0,1]$, la valeur $h(0)$ doit être dans l'intervalle $[0,1]$.
        Donc, $h(0) \ge 0$. Par conséquent, $k(0) \ge 0$.
    *   Calculons $k(1)$:
        $k(1) = h(1) - 1$.
        Puisque $h$ est une fonction de $[0,1]$ vers $[0,1]$, la valeur $h(1)$ doit être dans l'intervalle $[0,1]$.
        Donc, $h(1) \le 1$. Par conséquent, $h(1) - 1 \le 0$. Donc, $k(1) \le 0$.

*   **Application du Théorème des Valeurs Intermédiaires (TVI) :**
    Nous avons $k(0) \ge 0$ et $k(1) \le 0$.
    Nous distinguons trois cas :
    1.  Si $k(0) = 0$, alors $h(0) - 0 = 0$, ce qui signifie $h(0) = 0$. Dans ce cas, $c=0$ est un point fixe.
    2.  Si $k(1) = 0$, alors $h(1) - 1 = 0$, ce qui signifie $h(1) = 1$. Dans ce cas, $c=1$ est un point fixe.
    3.  Si $k(0) > 0$ et $k(1) < 0$, alors $k(1) < 0 < k(0)$.
        Puisque $k$ est continue sur l'intervalle $[0,1]$ et que $0$ est une valeur comprise entre $k(1)$ et $k(0)$, le Théorème des Valeurs Intermédiaires garantit l'existence d'au moins un point $c \in (0,1)$ tel que $k(c) = 0$.
        La condition $k(c) = 0$ signifie $h(c) - c = 0$, ce qui est équivalent à $h(c) = c$.

Dans tous les cas, il existe au moins un point $c \in [0,1]$ tel que $h(c) = c$.
Ceci démontre l'existence d'un point fixe pour la fonction $h$.

**2. Généralisation du Théorème des Valeurs Intermédiaires.**

Soit $f: [a,b] \to \mathbb{R}$ une fonction continue. Soient $y_1, y_2, \dots, y_n$ des points quelconques de l'intervalle $[a,b]$, où $n \in \mathbb{N}^*$. Nous voulons démontrer qu'il existe un point $c \in [a,b]$ tel que $f(c) = \frac{f(y_1) + f(y_2) + \dots + f(y_n)}{n}$.

Soit $A$ la moyenne arithmétique des valeurs de la fonction aux points $y_i$:
$$ A = \frac{f(y_1) + f(y_2) + \dots + f(y_n)}{n} $$

*   **Application du Théorème des Bornes Atteintes (TBA) :**
    Puisque $f$ est continue sur l'intervalle fermé et borné $[a,b]$, le Théorème des Bornes Atteintes (aussi appelé Théorème de Weierstrass) garantit que $f$ atteint son minimum et son maximum sur cet intervalle.
    Soit $m = \min_{x \in [a,b]} f(x)$ et $M = \max_{x \in [a,b]} f(x)$.
    Il existe donc $x_{min} \in [a,b]$ tel que $f(x_{min}) = m$, et il existe $x_{max} \in [a,b]$ tel que $f(x_{max}) = M$.
    Pour tout $x \in [a,b]$, nous avons $m \le f(x) \le M$.

*   **Encadrement de la moyenne $A$ :**
    Puisque $y_1, y_2, \dots, y_n$ sont des points de l'intervalle $[a,b]$, nous avons pour chaque $i \in \{1, \dots, n\}$ :
    $$ m \le f(y_i) \le M $$
    En sommant ces $n$ inégalités, nous obtenons :
    $$ \sum_{i=1}^n m \le \sum_{i=1}^n f(y_i) \le \sum_{i=1}^n M $$
    $$ n \cdot m \le f(y_1) + f(y_2) + \dots + f(y_n) \le n \cdot M $$
    Puisque $n \in \mathbb{N}^*$, $n$ est un entier strictement positif. Nous pouvons diviser l'inégalité par $n$ sans changer son sens :
    $$ m \le \frac{f(y_1) + f(y_2) + \dots + f(y_n)}{n} \le M $$
    Donc, nous avons $m \le A \le M$.

*   **Application du Théorème des Valeurs Intermédiaires (TVI) :**
    Nous avons montré que $f(x_{min}) = m$ et $f(x_{max}) = M$.
    L'inégalité $m \le A \le M$ peut donc s'écrire $f(x_{min}) \le A \le f(x_{max})$.
    Puisque $f$ est continue sur l'intervalle $[a,b]$ (qui contient $x_{min}$ et $x_{max}$), et que $A$ est une valeur comprise entre $f(x_{min})$ et $f(x_{max})$, le Théorème des Valeurs Intermédiaires garantit l'existence d'au moins un point $c$ dans l'intervalle $[a,b]$ (plus précisément, entre $x_{min}$ et $x_{max}$, donc dans $[a,b]$) tel que $f(c) = A$.
    Par conséquent, il existe un point $c \in [a,b]$ tel que $f(c) = \frac{f(y_1) + f(y_2) + \dots + f(y_n)}{n}$.
    Ceci complète la démonstration.

---

**Partie D : Équation fonctionnelle de Cauchy.**

Nous cherchons toutes les fonctions $f: \mathbb{R} \to \mathbb{R}$ qui sont continues et qui satisfont l'équation fonctionnelle $f(x+y) = f(x) + f(y)$ pour tous $x, y \in \mathbb{R}$.

**Étape 1 : Déterminer $f(0)$.**
Substituons $x=0$ et $y=0$ dans l'équation fonctionnelle :
$f(0+0) = f(0) + f(0)$
$f(0) = 2f(0)$
En soustrayant $f(0)$ des deux côtés, nous obtenons :
$f(0) = 0$.

**Étape 2 : Déterminer $f(nx)$ pour $n \in \mathbb{N}$.**
*   Pour $n=1$: $f(1x) = f(x)$.
*   Pour $n=2$: $f(2x) = f(x+x) = f(x) + f(x) = 2f(x)$.
*   Pour $n=3$: $f(3x) = f(2x+x) = f(2x) + f(x) = 2f(x) + f(x) = 3f(x)$.
Nous allons prouver par induction que $f(nx) = nf(x)$ pour tout $n \in \mathbb{N}$ et tout $x \in \mathbb{R}$.
*   **Base de l'induction :** Pour $n=0$, $f(0x) = f(0) = 0$. Et $0f(x) = 0$. Donc $f(0x) = 0f(x)$ est vrai. Pour $n=1$, $f(1x) = f(x)$ et $1f(x) = f(x)$, donc $f(1x) = 1f(x)$ est vrai.
*   **Hypothèse d'induction :** Supposons que $f(kx) = kf(x)$ pour un certain entier naturel $k \ge 0$.
*   **Étape d'induction :** Nous voulons montrer que $f((k+1)x) = (k+1)f(x)$.
    $f((k+1)x) = f(kx + x)$
    En utilisant l'équation fonctionnelle avec $X=kx$ et $Y=x$:
    $f(kx + x) = f(kx) + f(x)$
    En utilisant l'hypothèse d'induction $f(kx) = kf(x)$:
    $f(kx) + f(x) = kf(x) + f(x)$
    En factorisant $f(x)$:
    $kf(x) + f(x) = (k+1)f(x)$.
    Donc, $f((k+1)x) = (k+1)f(x)$.
Par le principe d'induction mathématique, $f(nx) = nf(x)$ pour tout $n \in \mathbb{N}$ et tout $x \in \mathbb{R}$.

**Étape 3 : Déterminer $f(nx)$ pour $n \in \mathbb{Z}$.**
Nous avons $f(0) = 0$.
Pour $x \in \mathbb{R}$, $f(x + (-x)) = f(x) + f(-x)$.
Puisque $f(x + (-x)) = f(0) = 0$, nous avons $0 = f(x) + f(-x)$.
Ceci implique $f(-x) = -f(x)$ pour tout $x \in \mathbb{R}$.
Maintenant, si $n$ est un entier négatif, soit $n = -m$ où $m \in \mathbb{N}^*$.
Alors $f(nx) = f(-mx) = -f(mx)$ (en utilisant $f(-y) = -f(y)$ avec $y=mx$).
Puisque $m \in \mathbb{N}^*$, nous savons que $f(mx) = mf(x)$.
Donc, $-f(mx) = -mf(x)$.
Ainsi, $f(nx) = -mf(x) = nf(x)$ pour tout $n \in \mathbb{Z}$.

**Étape 4 : Déterminer $f(qx)$ pour $q \in \mathbb{Q}$.**
Soit $q \in \mathbb{Q}$. Alors $q$ peut s'écrire sous la forme $\frac{m}{n}$ où $m \in \mathbb{Z}$ et $n \in \mathbb{N}^*$.
Nous voulons montrer que $f(qx) = qf(x)$.
Considérons $f(nx)$. Nous savons que $f(nx) = nf(x)$.
Soit $y = qx = \frac{m}{n}x$. Alors $ny = nx \frac{m}{n} = mx$.
Donc, $f(ny) = f(mx)$.
En utilisant la propriété $f(kx) = kf(x)$ pour $k \in \mathbb{Z}$:
$nf(y) = mf(x)$.
En substituant $y = qx$:
$nf(qx) = mf(x)$.
En divisant par $n$ (ce qui est permis car $n \in \mathbb{N}^*$, donc $n \neq 0$):
$f(qx) = \frac{m}{n}f(x)$.
Puisque $q = \frac{m}{n}$, nous avons :
$f(qx) = qf(x)$ pour tout $q \in \mathbb{Q}$ et tout $x \in \mathbb{R}$.

**Étape 5 : Déterminer $f(x)$ pour $x \in \mathbb{R}$ en utilisant la continuité.**
Posons $x=1$ dans la relation $f(qx) = qf(x)$.
Alors $f(q) = qf(1)$ pour tout $q \in \mathbb{Q}$.
Soit $a = f(1)$. C'est une constante réelle.
Donc, $f(q) = aq$ pour tout $q \in \mathbb{Q}$.

Maintenant, nous utilisons la condition de continuité de $f$.
Soit $x \in \mathbb{R}$ un nombre réel arbitraire.
Nous savons qu'il existe une suite de nombres rationnels $(q_k)_{k \in \mathbb{N}}$ telle que $\lim_{k \to \infty} q_k = x$.
Puisque la fonction $f$ est continue sur $\mathbb{R}$, par la caractérisation séquentielle de la continuité, si $\lim_{k \to \infty} q_k = x$, alors $\lim_{k \to \infty} f(q_k) = f(x)$.
Nous savons que pour chaque $q_k \in \mathbb{Q}$, $f(q_k) = aq_k$.
Donc, $\lim_{k \to \infty} f(q_k) = \lim_{k \to \infty} (aq_k)$.
Par les propriétés des limites, la limite d'un produit est le produit des limites (si elles existent) :
$\lim_{k \to \infty} (aq_k) = a \lim_{k \to \infty} q_k$.
Puisque $\lim_{k \to \infty} q_k = x$, nous avons :
$a \lim_{k \to \infty} q_k = ax$.
En combinant ces résultats, nous obtenons :
$f(x) = ax$ pour tout $x \in \mathbb{R}$.

**Étape 6 : Vérifier la solution.**
Nous avons trouvé que les fonctions continues satisfaisant l'équation de Cauchy doivent être de la forme $f(x) = ax$ pour une constante $a \in \mathbb{R}$.
Vérifions si ces fonctions satisfont les conditions données :
1.  **Continuité :** La fonction $f(x) = ax$ est une fonction linéaire (un polynôme de degré 1 ou 0 si $a=0$). Les fonctions polynomiales sont continues sur tout $\mathbb{R}$. Donc, la condition de continuité est satisfaite.
2.  **Équation fonctionnelle :** Vérifions si $f(x+y) = f(x) + f(y)$ est satisfaite.
    Membre de gauche : $f(x+y) = a(x+y) = ax + ay$.
    Membre de droite : $f(x) + f(y) = ax + ay$.
    Puisque $ax+ay = ax+ay$, l'équation fonctionnelle est satisfaite.

**Conclusion :**
Les seules fonctions $f: \mathbb{R} \to \mathbb{R}$ qui sont continues et qui satisfont l'équation fonctionnelle de Cauchy $f(x+y) = f(x) + f(y)$ pour tous $x, y \in \mathbb{R}$ sont les fonctions de la forme $f(x) = ax$, où $a$ est une constante réelle arbitraire.
