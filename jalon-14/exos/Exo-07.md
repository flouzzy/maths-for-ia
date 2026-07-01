---
uuid: "jalon-14-exo-07"
title: "Exercice 7 : Critère de Cauchy pour une suite contractante"
tags: ["math/analyse", "suites", "exercice"]
---
# Exercice 7 : Critère de Cauchy pour une suite contractante
## Énoncé
Mes chers étudiants,

Nous allons aujourd'hui explorer un aspect fondamental de la convergence des suites, à savoir le critère de Cauchy. Ce critère est d'une importance capitale car il permet de démontrer la convergence d'une suite sans avoir besoin de connaître sa limite a priori. Dans un espace complet comme $\mathbb{R}$ ou $\mathbb{C}$, une suite est convergente si et seulement si elle est de Cauchy.

Soit $(u_n)_{n \in \mathbb{N}}$ une suite de nombres réels. On suppose que cette suite satisfait la condition suivante : il existe une constante $C > 0$ et un réel $r \in ]0, 1[$ tels que pour tout entier naturel $n$, nous ayons $|u_{n+1} - u_n| \le C \cdot r^n$.
Dans le cadre de cet exercice, nous allons considérer le cas particulier où $C=1$ et $r=1/2$. Autrement dit, la suite $(u_n)_{n \in \mathbb{N}}$ vérifie la propriété :
$$ \forall n \in \mathbb{N}, \quad |u_{n+1} - u_n| \le \frac{1}{2^n} $$
Votre tâche est de démontrer, en utilisant la définition rigoureuse d'une suite de Cauchy, que la suite $(u_n)_{n \in \mathbb{N}}$ est une suite de Cauchy.

Rappel : Une suite $(u_n)_{n \in \mathbb{N}}$ est dite de Cauchy si pour tout $\epsilon > 0$, il existe un entier naturel $N$ tel que pour tous entiers $p, q$ vérifiant $p > N$ et $q > N$, on ait $|u_p - u_q| < \epsilon$.

## Correction Détaillée

Pour démontrer que la suite $(u_n)_{n \in \mathbb{N}}$ est une suite de Cauchy, nous devons suivre la définition rigoureuse.

1.  **Rappel de la définition d'une suite de Cauchy.**
    Une suite $(u_n)_{n \in \mathbb{N}}$ est une suite de Cauchy si et seulement si :
    $$ \forall \epsilon > 0, \exists N \in \mathbb{N} \text{ tel que } \forall p, q \in \mathbb{N}, \text{ si } p > N \text{ et } q > N, \text{ alors } |u_p - u_q| < \epsilon $$

2.  **Fixer $\epsilon$ et choisir $p, q$.**
    Soit $\epsilon$ un nombre réel strictement positif arbitrairement choisi. Notre objectif est de trouver un entier naturel $N$ (qui dépendra de $\epsilon$) tel que la condition de Cauchy soit satisfaite pour tous $p, q > N$.
    Considérons deux entiers $p$ et $q$ tels que $p > N$ et $q > N$. Sans perte de généralité, nous pouvons supposer que $p > q$. (Si $q > p$, on peut échanger les rôles de $p$ et $q$, car $|u_p - u_q| = |u_q - u_p|$. Si $p=q$, alors $|u_p - u_q| = 0$, ce qui est trivialement inférieur à tout $\epsilon > 0$).

3.  **Décomposition de la différence $|u_p - u_q|$.**
    Puisque $p > q$, nous pouvons exprimer la différence $u_p - u_q$ comme une somme télescopique de différences consécutives. En ajoutant et soustrayant des termes intermédiaires, nous obtenons :
    $$ u_p - u_q = (u_p - u_{p-1}) + (u_{p-1} - u_{p-2}) + \dots + (u_{q+1} - u_q) $$
    Cette somme peut être écrite de manière plus compacte en utilisant le symbole de sommation :
    $$ u_p - u_q = \sum_{k=q}^{p-1} (u_{k+1} - u_k) $$

4.  **Application de l'inégalité triangulaire.**
    En prenant la valeur absolue de cette somme, nous pouvons appliquer l'inégalité triangulaire généralisée, qui stipule que la valeur absolue d'une somme est inférieure ou égale à la somme des valeurs absolues :
    $$ |u_p - u_q| = \left| \sum_{k=q}^{p-1} (u_{k+1} - u_k) \right| \le \sum_{k=q}^{p-1} |u_{k+1} - u_k| $$

5.  **Utilisation de l'hypothèse de l'exercice.**
    L'énoncé nous donne une majoration pour chaque terme $|u_{k+1} - u_k|$ :
    $$ |u_{k+1} - u_k| \le \frac{1}{2^k} \quad \text{pour tout } k \in \mathbb{N} $$
    En substituant cette inégalité dans l'expression précédente, nous obtenons :
    $$ |u_p - u_q| \le \sum_{k=q}^{p-1} \frac{1}{2^k} $$

6.  **Calcul de la somme de la série géométrique.**
    La somme $\sum_{k=q}^{p-1} \frac{1}{2^k}$ est une somme partielle d'une série géométrique de raison $r = 1/2$.
    Nous pouvons factoriser le premier terme $\frac{1}{2^q}$ :
    $$ \sum_{k=q}^{p-1} \frac{1}{2^k} = \frac{1}{2^q} + \frac{1}{2^{q+1}} + \dots + \frac{1}{2^{p-1}} = \frac{1}{2^q} \left( 1 + \frac{1}{2} + \dots + \frac{1}{2^{p-1-q}} \right) $$
    La somme entre parenthèses est une somme partielle d'une série géométrique de $p-q$ termes, commençant par $1 = (1/2)^0$. La formule pour la somme des $m$ premiers termes d'une série géométrique $1 + r + \dots + r^{m-1}$ est $\frac{1-r^m}{1-r}$. Ici, $m = p-q$ et $r=1/2$.
    Donc, la somme entre parenthèses est :
    $$ 1 + \frac{1}{2} + \dots + \frac{1}{2^{p-1-q}} = \frac{1 - (1/2)^{p-q}}{1 - 1/2} = \frac{1 - (1/2)^{p-q}}{1/2} = 2 \left( 1 - \left(\frac{1}{2}\right)^{p-q} \right) $$
    En substituant cela dans l'expression de la somme, nous obtenons :
    $$ \sum_{k=q}^{p-1} \frac{1}{2^k} = \frac{1}{2^q} \cdot 2 \left( 1 - \left(\frac{1}{2}\right)^{p-q} \right) = \frac{2}{2^q} \left( 1 - \left(\frac{1}{2}\right)^{p-q} \right) = \frac{1}{2^{q-1}} \left( 1 - \left(\frac{1}{2}\right)^{p-q} \right) $$

7.  **Majoration de l'expression.**
    Puisque $p > q$, l'exposant $p-q$ est un entier strictement positif. Par conséquent, $(1/2)^{p-q}$ est un nombre positif strictement inférieur à 1.
    Donc, $1 - (1/2)^{p-q} < 1$.
    Ainsi, nous pouvons majorer l'expression de $|u_p - u_q|$ :
    $$ |u_p - u_q| \le \frac{1}{2^{q-1}} \left( 1 - \left(\frac{1}{2}\right)^{p-q} \right) < \frac{1}{2^{q-1}} $$

8.  **Détermination de $N$.**
    Nous voulons que $|u_p - u_q| < \epsilon$. D'après l'étape précédente, il suffit de s'assurer que $\frac{1}{2^{q-1}} < \epsilon$.
    Cette inégalité est équivalente à :
    $$ 2^{q-1} > \frac{1}{\epsilon} $$
    Pour résoudre cette inégalité pour $q$, nous prenons le logarithme en base 2 (ou le logarithme naturel, puis divisons par $\ln 2$) :
    $$ \log_2(2^{q-1}) > \log_2\left(\frac{1}{\epsilon}\right) $$
    $$ q-1 > -\log_2(\epsilon) $$
    $$ q > 1 - \log_2(\epsilon) $$
    Puisque nous avons supposé $p > q > N$, il suffit de choisir $N$ tel que $N \ge 1 - \log_2(\epsilon)$.
    Pour s'assurer que $N$ est un entier naturel, nous pouvons choisir $N$ comme le plus petit entier supérieur ou égal à $1 - \log_2(\epsilon)$, et s'assurer qu'il est non négatif :
    $$ N = \max\left(0, \lfloor 1 - \log_2(\epsilon) \rfloor + 1\right) $$
    Un tel entier $N$ existe toujours pour tout $\epsilon > 0$.

9.  **Conclusion.**
    Pour tout $\epsilon > 0$, nous avons trouvé un entier naturel $N = \max\left(0, \lfloor 1 - \log_2(\epsilon) \rfloor + 1\right)$ tel que pour tous $p, q \in \mathbb{N}$ avec $p > N$ et $q > N$, nous avons $|u_p - u_q| < \epsilon$.
    Par conséquent, la suite $(u_n)_{n \in \mathbb{N}}$ est une suite de Cauchy.