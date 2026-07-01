---
uuid: "jalon-14-exo-01"
title: "Exercice 1 : Démonstration de la convergence de la suite inverse par la définition $\\epsilon-N$"
tags: ["math/analyse", "suites", "exercice"]
---
# Exercice 1 : Démonstration de la convergence de la suite inverse par la définition $\epsilon-N$
## Énoncé
Chers étudiants,

Nous allons aborder ensemble la première application concrète de la définition rigoureuse de la limite d'une suite. C'est un jalon fondamental dans votre compréhension de l'analyse.

Soit la suite réelle $(u_n)_{n \in \mathbb{N}^*}$ définie pour tout entier $n \ge 1$ par $u_n = \frac{1}{n}$.

En utilisant la définition formelle de la limite (dite "définition $\epsilon-N$"), démontrez rigoureusement que cette suite converge vers 0.

## Correction Détaillée
Mes chers étudiants, abordons cette démonstration avec la rigueur et la précision qu'exige l'analyse mathématique. Chaque étape sera explicitée afin de construire une compréhension solide.

**Étape 1 : Rappel de la définition formelle de la limite d'une suite.**
Commençons par énoncer clairement la définition que nous allons utiliser.
Une suite réelle $(u_n)_{n \in \mathbb{N}^*}$ converge vers un réel $L$ si et seulement si :
Pour tout nombre réel $\epsilon > 0$ (aussi petit soit-il), il existe un entier naturel $N$ (qui dépendra généralement de $\epsilon$) tel que, pour tout entier $n$ vérifiant $n \ge N$, on ait l'inégalité $|u_n - L| < \epsilon$.
Notre objectif est de montrer que pour la suite $u_n = \frac{1}{n}$, la limite $L$ est 0.

**Étape 2 : Identification des éléments et traduction de l'inégalité.**
Dans notre cas précis, la suite est $u_n = \frac{1}{n}$ et la limite que nous souhaitons démontrer est $L=0$.
L'inégalité fondamentale de la définition de la limite est $|u_n - L| < \epsilon$.
Substituons $u_n$ et $L$ par leurs valeurs respectives :
$\left| \frac{1}{n} - 0 \right| < \epsilon$

**Étape 3 : Simplification de l'expression de l'inégalité.**
Simplifions l'expression à l'intérieur de la valeur absolue.
$\left| \frac{1}{n} - 0 \right| = \left| \frac{1}{n} \right|$.
Puisque l'indice $n$ appartient à $\mathbb{N}^*$, cela signifie que $n$ est un entier strictement positif ($n \ge 1$). Par conséquent, $\frac{1}{n}$ est également un nombre strictement positif.
Pour un nombre positif $x$, sa valeur absolue est $x$ lui-même (c'est-à-dire $|x|=x$).
Donc, $\left| \frac{1}{n} \right| = \frac{1}{n}$.
L'inégalité à satisfaire se réduit donc à :
$\frac{1}{n} < \epsilon$

**Étape 4 : Détermination de la condition sur $n$ en fonction de $\epsilon$.**
Nous cherchons à trouver un entier $N$ tel que pour tout $n \ge N$, l'inégalité $\frac{1}{n} < \epsilon$ soit vérifiée.
Manipulons l'inégalité $\frac{1}{n} < \epsilon$ pour isoler $n$.
Puisque $\epsilon > 0$ (par définition de la limite) et $n > 0$ (car $n \in \mathbb{N}^*$), nous pouvons multiplier les deux côtés de l'inégalité par $n$ et diviser par $\epsilon$ sans changer le sens de l'inégalité.
Multiplions par $n$ :
$1 < n \epsilon$
Divisons par $\epsilon$ :
$\frac{1}{\epsilon} < n$
Ou, de manière équivalente :
$n > \frac{1}{\epsilon}$
Cette dernière inégalité nous donne la condition que $n$ doit satisfaire pour que $|u_n - L| < \epsilon$ soit vraie.

**Étape 5 : Choix de l'entier $N$ en fonction de $\epsilon$.**
Nous devons trouver un entier $N$ tel que si $n \ge N$, alors la condition $n > \frac{1}{\epsilon}$ est automatiquement satisfaite.
Pour cela, il suffit de choisir $N$ comme le plus petit entier qui est strictement supérieur à $\frac{1}{\epsilon}$.
La fonction partie entière, notée $\lfloor x \rfloor$, donne le plus grand entier inférieur ou égal à $x$. Par exemple, $\lfloor 3.14 \rfloor = 3$ et $\lfloor 5 \rfloor = 5$.
Donc, $\lfloor \frac{1}{\epsilon} \rfloor$ est un entier tel que $\lfloor \frac{1}{\epsilon} \rfloor \le \frac{1}{\epsilon}$.
Pour obtenir un entier $N$ qui est *strictement* supérieur à $\frac{1}{\epsilon}$, nous pouvons choisir :
$N = \lfloor \frac{1}{\epsilon} \rfloor + 1$
Ce choix garantit que $N$ est un entier. De plus, par la propriété de la partie entière, nous savons que $x < \lfloor x \rfloor + 1$. En appliquant cela à $x = \frac{1}{\epsilon}$, nous avons $\frac{1}{\epsilon} < \lfloor \frac{1}{\epsilon} \rfloor + 1$.
Ainsi, notre choix de $N$ satisfait $N > \frac{1}{\epsilon}$.
Il est important de noter que $N$ doit être un entier positif. Puisque $\epsilon > 0$, $\frac{1}{\epsilon} > 0$. Donc $\lfloor \frac{1}{\epsilon} \rfloor \ge 0$, et $N = \lfloor \frac{1}{\epsilon} \rfloor + 1 \ge 1$. Ce choix est donc valide pour $n \in \mathbb{N}^*$.

**Étape 6 : Vérification formelle de la définition.**
Nous avons maintenant tous les éléments pour rédiger la démonstration formelle.
Soit $\epsilon > 0$ un nombre réel arbitrairement choisi.
Nous choisissons l'entier $N = \lfloor \frac{1}{\epsilon} \rfloor + 1$.
Par la définition de la partie entière, nous savons que pour tout réel $x$, $\lfloor x \rfloor \le x < \lfloor x \rfloor + 1$.
En appliquant cette propriété à $x = \frac{1}{\epsilon}$, nous obtenons :
$\lfloor \frac{1}{\epsilon} \rfloor < \frac{1}{\epsilon} < \lfloor \frac{1}{\epsilon} \rfloor + 1$.
De cette inégalité, nous déduisons directement que $N = \lfloor \frac{1}{\epsilon} \rfloor + 1 > \frac{1}{\epsilon}$.

Considérons maintenant un entier $n$ quelconque tel que $n \ge N$.
Puisque $n \ge N$ et que nous avons établi que $N > \frac{1}{\epsilon}$, par la propriété de transitivité des inégalités, nous avons :
$n > \frac{1}{\epsilon}$
Comme $n$ et $\epsilon$ sont tous deux des nombres strictement positifs, nous pouvons prendre l'inverse des deux côtés de l'inégalité. Attention, prendre l'inverse de nombres positifs inverse le sens de l'inégalité :
$\frac{1}{n} < \epsilon$
Et comme nous l'avons établi à l'Étape 3, $\frac{1}{n} = \left| \frac{1}{n} - 0 \right|$.
Par conséquent, nous avons bien $\left| \frac{1}{n} - 0 \right| < \epsilon$ pour tout $n \ge N$.

**Étape 7 : Conclusion.**
Nous avons démontré que pour tout $\epsilon > 0$, il existe un entier $N$ (que nous avons construit explicitement comme $N = \lfloor \frac{1}{\epsilon} \rfloor + 1$) tel que pour tout entier $n \ge N$, l'inégalité $|u_n - 0| < \epsilon$ est satisfaite.
Conformément à la définition formelle de la limite, nous pouvons donc affirmer que la suite $(u_n)_{n \in \mathbb{N}^*}$ définie par $u_n = \frac{1}{n}$ converge vers 0.

Ceci est un premier pas crucial dans la maîtrise des concepts de convergence en analyse. Félicitations pour cette première démonstration rigoureuse !