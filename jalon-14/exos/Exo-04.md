---
uuid: "jalon-14-exo-04"
title: "Exercice 4 : Convergence d'une suite complexe par la définition $(\epsilon, N)$"
tags: ["math/analyse", "suites", "exercice", "limites", "epsilon-N", "suites complexes"]
---
# Exercice 4 : Convergence d'une suite complexe par la définition $(\epsilon, N)$
## Énoncé
Soit la suite de nombres complexes $(u_n)_{n \in \mathbb{N}^*}$ définie pour tout $n \in \mathbb{N}^*$ par :
$$u_n = \frac{2n+i}{n+2i}$$

1.  Conjecturer la limite $L$ de la suite $(u_n)$ lorsque $n \to +\infty$.
2.  Démontrer rigoureusement, en utilisant la définition formelle $(\epsilon, N)$ de la limite, que la suite $(u_n)$ converge vers la limite $L$ conjecturée.

## Correction Détaillée

### Partie 1 : Conjecturer la limite $L$

Pour conjecturer la limite de la suite $(u_n)$ lorsque $n \to +\infty$, nous allons examiner le comportement de l'expression de $u_n$ pour de grandes valeurs de $n$.

L'expression de $u_n$ est une fraction dont le numérateur et le dénominateur sont des expressions linéaires en $n$ (avec des termes constants complexes) :
$$u_n = \frac{2n+i}{n+2i}$$

Pour analyser le comportement asymptotique, il est souvent utile de diviser le numérateur et le dénominateur par la plus haute puissance de $n$ présente, qui est ici $n$.
$$u_n = \frac{\frac{2n}{n} + \frac{i}{n}}{\frac{n}{n} + \frac{2i}{n}}$$
$$u_n = \frac{2 + \frac{i}{n}}{1 + \frac{2i}{n}}$$

Maintenant, nous considérons le comportement de chaque terme lorsque $n \to +\infty$ :
*   Le terme $\frac{i}{n}$ tend vers $0$ lorsque $n \to +\infty$, car $| \frac{i}{n} | = \frac{|i|}{n} = \frac{1}{n}$, et $\frac{1}{n} \to 0$.
*   De même, le terme $\frac{2i}{n}$ tend vers $0$ lorsque $n \to +\infty$, car $| \frac{2i}{n} | = \frac{|2i|}{n} = \frac{2}{n}$, et $\frac{2}{n} \to 0$.

En substituant ces limites dans l'expression de $u_n$, nous obtenons :
$$\lim_{n \to +\infty} u_n = \frac{2 + 0}{1 + 0} = \frac{2}{1} = 2$$

Nous conjecturons donc que la limite $L$ de la suite $(u_n)$ est $2$.

### Partie 2 : Démonstration rigoureuse par la définition $(\epsilon, N)$

La définition formelle de la limite pour une suite de nombres complexes $(u_n)$ convergeant vers un nombre complexe $L$ est la suivante :
Pour tout $\epsilon > 0$, il existe un entier naturel $N$ (qui peut dépendre de $\epsilon$) tel que pour tout $n > N$, on ait $|u_n - L| < \epsilon$.

Dans notre cas, $L=2$. Nous devons donc montrer que pour tout $\epsilon > 0$, il existe un $N \in \mathbb{N}^*$ tel que pour tout $n > N$, $|u_n - 2| < \epsilon$.

**Étape 1 : Calculer l'expression $|u_n - L|$**

Nous commençons par calculer la différence $u_n - L$ :
$$u_n - 2 = \frac{2n+i}{n+2i} - 2$$
Pour combiner ces termes, nous mettons $2$ au même dénominateur :
$$u_n - 2 = \frac{2n+i}{n+2i} - \frac{2(n+2i)}{n+2i}$$
$$u_n - 2 = \frac{(2n+i) - (2n+4i)}{n+2i}$$
$$u_n - 2 = \frac{2n+i - 2n-4i}{n+2i}$$
$$u_n - 2 = \frac{-3i}{n+2i}$$

Maintenant, nous calculons le module de cette expression :
$$|u_n - 2| = \left| \frac{-3i}{n+2i} \right|$$
En utilisant la propriété du module $|z_1/z_2| = |z_1|/|z_2|$ :
$$|u_n - 2| = \frac{|-3i|}{|n+2i|}$$
Le module de $-3i$ est $|-3i| = \sqrt{0^2 + (-3)^2} = \sqrt{9} = 3$.
Le module de $n+2i$ est $|n+2i| = \sqrt{n^2 + 2^2} = \sqrt{n^2+4}$.
Donc, l'expression devient :
$$|u_n - 2| = \frac{3}{\sqrt{n^2+4}}$$

**Étape 2 : Établir l'inégalité $|u_n - L| < \epsilon$ et résoudre pour $n$**

Nous voulons trouver $N$ tel que pour tout $n > N$, nous ayons :
$$\frac{3}{\sqrt{n^2+4}} < \epsilon$$
Puisque $\epsilon > 0$ et $\frac{3}{\sqrt{n^2+4}} > 0$, nous pouvons inverser l'inégalité en prenant les réciproques, ce qui change le sens de l'inégalité :
$$\frac{\sqrt{n^2+4}}{3} > \frac{1}{\epsilon}$$
Multiplions par $3$ :
$$\sqrt{n^2+4} > \frac{3}{\epsilon}$$
Les deux membres de l'inégalité sont positifs, nous pouvons donc élever au carré sans changer le sens de l'inégalité :
$$n^2+4 > \left(\frac{3}{\epsilon}\right)^2$$
$$n^2+4 > \frac{9}{\epsilon^2}$$
Isolons $n^2$ :
$$n^2 > \frac{9}{\epsilon^2} - 4$$

**Étape 3 : Déterminer la valeur de $N$**

Nous devons maintenant choisir $N$ en fonction de $\epsilon$. Nous devons considérer deux cas pour l'expression $\frac{9}{\epsilon^2} - 4$.

*   **Cas 1 : $\frac{9}{\epsilon^2} - 4 \le 0$**
    Cette condition est équivalente à $\frac{9}{\epsilon^2} \le 4$, ce qui signifie $\epsilon^2 \ge \frac{9}{4}$, ou $\epsilon \ge \frac{3}{2}$.
    Dans ce cas, l'inégalité $n^2 > \frac{9}{\epsilon^2} - 4$ est toujours vraie pour tout $n \in \mathbb{N}^*$ (puisque $n^2 \ge 1$ et $\frac{9}{\epsilon^2} - 4$ est négatif ou nul).
    Par conséquent, pour $\epsilon \ge \frac{3}{2}$, nous pouvons choisir $N=1$ (car la suite est définie pour $n \in \mathbb{N}^*$, donc $n > 1$ ou $n=1$ suffit).

*   **Cas 2 : $\frac{9}{\epsilon^2} - 4 > 0$**
    Cette condition est équivalente à $\frac{9}{\epsilon^2} > 4$, ce qui signifie $\epsilon^2 < \frac{9}{4}$, ou $0 < \epsilon < \frac{3}{2}$.
    Dans ce cas, nous devons prendre la racine carrée des deux côtés de l'inégalité $n^2 > \frac{9}{\epsilon^2} - 4$ (les deux membres sont positifs) :
    $$n > \sqrt{\frac{9}{\epsilon^2} - 4}$$
    Pour garantir que $n > \sqrt{\frac{9}{\epsilon^2} - 4}$, nous pouvons choisir $N$ comme le plus petit entier supérieur ou égal à $\sqrt{\frac{9}{\epsilon^2} - 4}$. Plus précisément, nous pouvons prendre $N = \lfloor \sqrt{\frac{9}{\epsilon^2} - 4} \rfloor + 1$.
    Puisque $n \in \mathbb{N}^*$, $N$ doit être au moins $1$.

**Synthèse du choix de $N$ :**
Pour couvrir les deux cas de manière élégante et rigoureuse, nous pouvons définir $N$ comme suit :
$$N = \max\left(1, \left\lfloor \sqrt{\max\left(0, \frac{9}{\epsilon^2} - 4\right)} \right\rfloor + 1\right)$$
Expliquons ce choix :
*   Le terme $\max\left(0, \frac{9}{\epsilon^2} - 4\right)$ garantit que nous prenons la racine carrée d'un nombre positif ou nul, même si $\frac{9}{\epsilon^2} - 4$ est négatif (dans ce cas, la racine est $\sqrt{0}=0$).
*   La fonction $\lfloor \cdot \rfloor$ (partie entière inférieure) nous donne le plus grand entier inférieur ou égal à la valeur.
*   Ajouter $1$ à $\lfloor \cdot \rfloor$ garantit que $N$ est strictement supérieur à $\sqrt{\max\left(0, \frac{9}{\epsilon^2} - 4\right)}$.
*   Le $\max(1, \dots)$ assure que $N$ est toujours au moins $1$, ce qui est nécessaire car $n \in \mathbb{N}^*$.

**Conclusion de la démonstration :**
Soit $\epsilon > 0$ un nombre réel arbitrairement petit.
Nous avons montré que pour que $|u_n - 2| < \epsilon$, il suffit que $n > \sqrt{\max\left(0, \frac{9}{\epsilon^2} - 4\right)}$.
Choisissons $N = \max\left(1, \left\lfloor \sqrt{\max\left(0, \frac{9}{\epsilon^2} - 4\right)} \right\rfloor + 1\right)$.
Alors, pour tout $n \in \mathbb{N}^*$ tel que $n > N$, nous avons :
$$n > N \ge \left\lfloor \sqrt{\max\left(0, \frac{9}{\epsilon^2} - 4\right)} \right\rfloor + 1 > \sqrt{\max\left(0, \frac{9}{\epsilon^2} - 4\right)}$$
Ceci implique $n^2 > \max\left(0, \frac{9}{\epsilon^2} - 4\right)$.
Si $\frac{9}{\epsilon^2} - 4 \le 0$, alors $n^2 > 0$, ce qui est vrai pour tout $n \in \mathbb{N}^*$.
Si $\frac{9}{\epsilon^2} - 4 > 0$, alors $n^2 > \frac{9}{\epsilon^2} - 4$.
Dans les deux cas, l'inégalité $n^2 > \frac{9}{\epsilon^2} - 4$ est satisfaite.
En remontant les étapes de l'inégalité, nous obtenons successivement :
$n^2+4 > \frac{9}{\epsilon^2}$
$\sqrt{n^2+4} > \frac{3}{\epsilon}$
$\frac{3}{\sqrt{n^2+4}} < \epsilon$
Et donc $|u_n - 2| < \epsilon$.

Puisque nous avons trouvé un tel $N$ pour tout $\epsilon > 0$, la suite $(u_n)$ converge bien vers $2$ selon la définition formelle de la limite.