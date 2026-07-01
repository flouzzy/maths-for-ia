---
uuid: "jalon-14-exo-05"
title: "Exercice 5 : Convergence d'une suite rationnelle perturbée : application de la définition $(\epsilon, N)$"
tags: ["math/analyse", "suites", "exercice"]
---
# Exercice 5 : Convergence d'une suite rationnelle perturbée : application de la définition $(\epsilon, N)$

## Énoncé

Chers étudiants,

Nous allons explorer la convergence d'une suite dont l'expression peut sembler un peu intimidante au premier abord, mais dont la limite est tout à fait accessible avec les outils appropriés. Cet exercice est conçu pour renforcer votre compréhension de la définition rigoureuse de la limite d'une suite.

Considérons la suite réelle $(u_n)_{n \in \mathbb{N}}$ définie pour tout $n \ge 2$ par :
$$u_n = \frac{n^2 + n\sin(n) + 5}{2n^2 - 3n + 1}$$

1.  **Détermination intuitive de la limite :**
    En utilisant des arguments de comparaison des ordres de grandeur des termes lorsque $n$ tend vers l'infini (par exemple, en factorisant le terme dominant au numérateur et au dénominateur), déterminez la valeur $L$ vers laquelle la suite $(u_n)$ semble converger. Justifiez brièvement votre raisonnement.

2.  **Démonstration rigoureuse de la convergence :**
    En utilisant la définition rigoureuse de la limite $(\epsilon, N)$, démontrez formellement que la suite $(u_n)$ converge vers la valeur $L$ trouvée à la question précédente. C'est-à-dire, pour tout $\epsilon > 0$, il existe un entier $N \in \mathbb{N}$ tel que pour tout $n > N$, on ait $|u_n - L| < \epsilon$.

## Correction Détaillée

Chers étudiants, abordons cet exercice avec la rigueur et la clarté qui s'imposent.

### Question 1 : Détermination intuitive de la limite

Pour déterminer la limite de la suite $(u_n)$ lorsque $n \to \infty$, nous allons analyser le comportement des termes dominants au numérateur et au dénominateur.

Nous avons :
$$u_n = \frac{n^2 + n\sin(n) + 5}{2n^2 - 3n + 1}$$

Factorisons le terme de plus haut degré, $n^2$, au numérateur et au dénominateur :
$$u_n = \frac{n^2 \left(1 + \frac{\sin(n)}{n} + \frac{5}{n^2}\right)}{n^2 \left(2 - \frac{3}{n} + \frac{1}{n^2}\right)}$$

Pour $n \ge 2$, le dénominateur $2n^2 - 3n + 1$ est non nul. En effet, les racines du trinôme $2x^2 - 3x + 1$ sont $x=1/2$ et $x=1$. Ainsi, pour $n \ge 2$, $2n^2 - 3n + 1 > 0$. Nous pouvons donc simplifier par $n^2$ :
$$u_n = \frac{1 + \frac{\sin(n)}{n} + \frac{5}{n^2}}{2 - \frac{3}{n} + \frac{1}{n^2}}$$

Analysons le comportement de chaque terme lorsque $n \to \infty$ :
*   $\lim_{n \to \infty} \frac{5}{n^2} = 0$
*   $\lim_{n \to \infty} \frac{3}{n} = 0$
*   $\lim_{n \to \infty} \frac{1}{n^2} = 0$
*   Pour le terme $\frac{\sin(n)}{n}$, nous savons que $-1 \le \sin(n) \le 1$. Par conséquent, pour $n > 0$, nous avons $-\frac{1}{n} \le \frac{\sin(n)}{n} \le \frac{1}{n}$.
    Puisque $\lim_{n \to \infty} -\frac{1}{n} = 0$ et $\lim_{n \to \infty} \frac{1}{n} = 0$, le théorème des gendarmes (ou théorème d'encadrement) nous assure que $\lim_{n \to \infty} \frac{\sin(n)}{n} = 0$.

En substituant ces limites dans l'expression de $u_n$ :
$$\lim_{n \to \infty} u_n = \frac{1 + 0 + 0}{2 - 0 + 0} = \frac{1}{2}$$

Ainsi, la limite intuitive de la suite $(u_n)$ est $L = \frac{1}{2}$.

### Question 2 : Démonstration rigoureuse de la convergence (définition $\epsilon, N$)

Nous voulons démontrer que $\lim_{n \to \infty} u_n = \frac{1}{2}$ en utilisant la définition $(\epsilon, N)$.
Cela signifie que pour tout $\epsilon > 0$, nous devons trouver un entier $N$ tel que pour tout $n > N$, nous ayons $|u_n - \frac{1}{2}| < \epsilon$.

Commençons par évaluer l'expression $|u_n - \frac{1}{2}|$ :
$$|u_n - \frac{1}{2}| = \left|\frac{n^2 + n\sin(n) + 5}{2n^2 - 3n + 1} - \frac{1}{2}\right|$$

Pour combiner les fractions, nous mettons sur un dénominateur commun :
$$|u_n - \frac{1}{2}| = \left|\frac{2(n^2 + n\sin(n) + 5) - (2n^2 - 3n + 1)}{2(2n^2 - 3n + 1)}\right|$$
$$|u_n - \frac{1}{2}| = \left|\frac{2n^2 + 2n\sin(n) + 10 - 2n^2 + 3n - 1}{2(2n^2 - 3n + 1)}\right|$$
$$|u_n - \frac{1}{2}| = \left|\frac{2n\sin(n) + 3n + 9}{2(2n^2 - 3n + 1)}\right|$$

Maintenant, nous devons majorer le numérateur et minorer le dénominateur.

**Majoration du numérateur :**
Nous utilisons l'inégalité triangulaire et le fait que $|\sin(n)| \le 1$ pour tout $n \in \mathbb{N}$ :
$$|2n\sin(n) + 3n + 9| \le |2n\sin(n)| + |3n| + |9|$$
$$|2n\sin(n) + 3n + 9| \le 2n|\sin(n)| + 3n + 9$$
$$|2n\sin(n) + 3n + 9| \le 2n(1) + 3n + 9$$
$$|2n\sin(n) + 3n + 9| \le 5n + 9$$
Pour $n \ge 1$, nous avons $9 \le 9n$. Donc $5n+9 \le 5n+9n = 14n$.
Ainsi, pour $n \ge 1$, nous avons :
$$|2n\sin(n) + 3n + 9| \le 14n$$

**Minoration du dénominateur :**
Le dénominateur est $2(2n^2 - 3n + 1)$. Nous savons que pour $n \ge 2$, $2n^2 - 3n + 1 > 0$.
Nous cherchons une minoration de la forme $Cn^2$ pour un certain $C > 0$.
Considérons le terme $2n^2 - 3n + 1$.
Pour $n \ge 3$, nous avons $n^2 - 3n + 1 \ge 0$ (car les racines de $x^2 - 3x + 1 = 0$ sont $\frac{3 \pm \sqrt{5}}{2}$, et $\frac{3+\sqrt{5}}{2} \approx 2.618$).
Donc, pour $n \ge 3$, $2n^2 - 3n + 1 = n^2 + (n^2 - 3n + 1) \ge n^2$.
Par conséquent, pour $n \ge 3$:
$$2(2n^2 - 3n + 1) \ge 2n^2$$

**Combinaison des majorations et minorations :**
En utilisant les inégalités obtenues pour $n \ge 3$ :
$$|u_n - \frac{1}{2}| = \frac{|2n\sin(n) + 3n + 9|}{2(2n^2 - 3n + 1)} \le \frac{14n}{2n^2}$$
$$|u_n - \frac{1}{2}| \le \frac{7}{n}$$

Maintenant, nous voulons que $|u_n - \frac{1}{2}| < \epsilon$.
Nous avons montré que $|u_n - \frac{1}{2}| \le \frac{7}{n}$.
Donc, si nous choisissons $n$ tel que $\frac{7}{n} < \epsilon$, alors l'inégalité sera satisfaite.
$$\frac{7}{n} < \epsilon \iff n > \frac{7}{\epsilon}$$

**Choix de N :**
Soit $\epsilon > 0$ donné. Nous devons choisir un entier $N$.
Nous avons besoin que $n \ge 3$ pour que nos minorations et majorations soient valides.
Nous choisissons $N = \max\left(2, \left\lceil \frac{7}{\epsilon} \right\rceil\right)$.
(Note : $n \ge 2$ est la condition pour que la suite soit bien définie. $n \ge 3$ est la condition pour nos bornes. $\lceil x \rceil$ désigne la partie entière par excès de $x$.)

**Conclusion :**
Pour tout $\epsilon > 0$, choisissons $N = \max\left(2, \left\lceil \frac{7}{\epsilon} \right\rceil\right)$.
Alors, pour tout $n > N$, nous avons $n \ge 3$ (car $N \ge 2$, et si $7/\epsilon < 3$, alors $N=3$ ou plus).
Et pour $n > N$, nous avons $n > \frac{7}{\epsilon}$, ce qui implique $\frac{7}{n} < \epsilon$.
Par conséquent, pour tout $n > N$, nous avons :
$$|u_n - \frac{1}{2}| \le \frac{7}{n} < \epsilon$$
Ceci démontre, par la définition $(\epsilon, N)$, que la suite $(u_n)$ converge vers $\frac{1}{2}$.

Ceci conclut notre exploration rigoureuse de la convergence de cette suite. Bravo pour votre persévérance !