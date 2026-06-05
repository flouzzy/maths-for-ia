---
uuid: jalon-140-exo-01
title: "Exercice 1 - Classifieur de Bayes"
type: Exercice
difficulty: 1
---

## Énoncé

Soit un problème de classification binaire où les données $(X, Y)$ sont des réalisations d'une variable aléatoire $(X, Y)$ définie sur un espace de probabilité $(\Omega, \mathcal{A}, P)$, à valeurs dans $\mathcal{X} \times \mathcal{Y}$.
L'espace d'entrée $\mathcal{X}$ est un espace mesurable $(\mathcal{X}, \mathcal{B}_{\mathcal{X}})$ et l'espace des étiquettes $\mathcal{Y} = \{-1, 1\}$.
La distribution jointe de $(X, Y)$ est notée $P_{XY}$.
On définit la fonction de régression $\eta: \mathcal{X} \to [0, 1]$ par $\eta(x) = P(Y=1|X=x)$, pour tout $x \in \mathcal{X}$ tel que $P_X(\{x\}) > 0$ si $\mathcal{X}$ est discret, ou presque partout $P_X$ si $\mathcal{X}$ est continu.

Un classifieur est une fonction mesurable $h: \mathcal{X} \to \mathcal{Y}$.
La fonction de perte 0-1 est définie par $L_{01}(y', y) = \mathbb{I}(y' \neq y)$, où $\mathbb{I}$ est la fonction indicatrice.
Le risque (ou erreur de classification attendue) d'un classifieur $h$ est défini comme l'espérance de la perte 0-1 :
$$R(h) = E[L_{01}(h(X), Y)]$$

1.  Démontrer que le risque $R(h)$ peut être exprimé sous la forme $E_X[P(h(X) \neq Y | X)]$. Préciser la signification de l'espérance $E_X[\cdot]$.
2.  Déterminer le classifieur de Bayes optimal $h^*: \mathcal{X} \to \mathcal{Y}$ qui minimise le risque $R(h)$ pour toute fonction mesurable $h$. Justifier rigoureusement votre démarche.
3.  Calculer le risque de Bayes $R(h^*)$.
4.  On définit la marge conditionnelle $m: \mathcal{X} \to [-1, 1]$ par $m(x) = P(Y=1|X=x) - P(Y=-1|X=x)$. Réexprimer le classifieur de Bayes $h^*(x)$ et le risque de Bayes $R(h^*)$ en fonction de $m(x)$.

## Correction

**Définitions préalables et notations :**

*   Soit $(\Omega, \mathcal{A}, P)$ l'espace de probabilité sous-jacent.
*   $X: \Omega \to \mathcal{X}$ est une variable aléatoire mesurable définie de $(\Omega, \mathcal{A})$ vers l'espace mesurable d'entrée $(\mathcal{X}, \mathcal{B}_{\mathcal{X}})$.
*   $Y: \Omega \to \mathcal{Y}$ est une variable aléatoire mesurable définie de $(\Omega, \mathcal{A})$ vers l'espace mesurable des étiquettes $(\mathcal{Y}, \mathcal{B}_{\mathcal{Y}})$, où $\mathcal{Y} = \{-1, 1\}$ et $\mathcal{B}_{\mathcal{Y}}$ est la $\sigma$-algèbre discrète sur $\mathcal{Y}$.
*   Le couple $(X, Y)$ est une variable aléatoire mesurable de $(\Omega, \mathcal{A})$ vers $(\mathcal{X} \times \mathcal{Y}, \mathcal{B}_{\mathcal{X}} \otimes \mathcal{B}_{\mathcal{Y}})$.
*   La distribution jointe $P_{XY}$ est la mesure de probabilité image $P \circ (X,Y)^{-1}$ sur $(\mathcal{X} \times \mathcal{Y}, \mathcal{B}_{\mathcal{X}} \otimes \mathcal{B}_{\mathcal{Y}})$.
*   La distribution marginale de $X$ est $P_X = P \circ X^{-1}$ sur $(\mathcal{X}, \mathcal{B}_{\mathcal{X}})$.
*   La fonction de régression $\eta(x) = P(Y=1|X=x)$ est une fonction mesurable de $(\mathcal{X}, \mathcal{B}_{\mathcal{X}})$ dans $([0, 1], \mathcal{B}_{[0,1]})$. Par définition, pour tout ensemble mesurable $A \in \mathcal{B}_{\mathcal{X}}$, l'espérance $E[\mathbb{I}(Y=1) \mathbb{I}(X \in A)]$ est égale à $E[\eta(X) \mathbb{I}(X \in A)]$.
*   Le classifieur $h: \mathcal{X} \to \mathcal{Y}$ est une fonction mesurable de $(\mathcal{X}, \mathcal{B}_{\mathcal{X}})$ vers $(\mathcal{Y}, \mathcal{B}_{\mathcal{Y}})$.
*   La fonction de perte 0-1 est $L_{01}(y', y) = \mathbb{I}(y' \neq y)$.

---

**1. Démontrer que le risque $R(h)$ peut être exprimé sous la forme $E_X[P(h(X) \neq Y | X)]$. Préciser la signification de l'espérance $E_X[\cdot]$.**

Le risque $R(h)$ est défini comme l'espérance mathématique de la perte $L_{01}(h(X), Y)$ :
$$R(h) = E[L_{01}(h(X), Y)]$$
En substituant la définition de la fonction de perte 0-1, nous obtenons :
$$R(h) = E[\mathbb{I}(h(X) \neq Y)]$$
Pour une variable aléatoire $Z$, l'espérance $E[Z]$ peut être calculée en utilisant la loi de l'espérance totale, qui stipule que $E[Z] = E_X[E[Z|X]]$ où $E_X[\cdot]$ est l'espérance par rapport à la distribution de $X$.
Dans notre cas, $Z = \mathbb{I}(h(X) \neq Y)$. Appliquons la loi de l'espérance totale :
$$R(h) = E_X[E[\mathbb{I}(h(X) \neq Y) | X]]$$
L'expression $E[\mathbb{I}(A) | B]$ représente la probabilité conditionnelle $P(A|B)$. Par conséquent, $E[\mathbb{I}(h(X) \neq Y) | X]$ est la probabilité que $h(X)$ soit différent de $Y$, conditionnellement à la valeur de $X$:
$$E[\mathbb{I}(h(X) \neq Y) | X] = P(h(X) \neq Y | X)$$
En substituant cette identité dans l'expression du risque, nous obtenons :
$$R(h) = E_X[P(h(X) \neq Y | X)]$$
L'espérance $E_X[\cdot]$ désigne l'espérance par rapport à la distribution marginale de la variable aléatoire $X$. Formellement, pour une fonction mesurable $f: \mathcal{X} \to \mathbb{R}$, $E_X[f(X)]$ est définie par l'intégrale par rapport à la mesure de probabilité $P_X$:
$$E_X[f(X)] = \int_{\mathcal{X}} f(x) dP_X(x)$$
Cela signifie que nous moyennons la probabilité d'erreur conditionnelle sur toutes les valeurs possibles de $X$, pondérées par la probabilité de survenue de ces valeurs.

---

**2. Déterminer le classifieur de Bayes optimal $h^*: \mathcal{X} \to \mathcal{Y}$ qui minimise le risque $R(h)$ pour toute fonction mesurable $h$. Justifier rigoureusement votre démarche.**

Pour minimiser le risque total $R(h) = E_X[P(h(X) \neq Y | X)]$, il suffit de minimiser l'intégrande, c'est-à-dire la probabilité d'erreur conditionnelle $P(h(x) \neq Y | X=x)$, pour chaque $x \in \mathcal{X}$ (plus précisément, pour $x$ dans le support de $P_X$, ou presque partout $P_X$).
Fixons un point $x \in \mathcal{X}$. Le classifieur $h(x)$ peut prendre l'une des deux valeurs : $1$ ou $-1$. Analysons la probabilité d'erreur conditionnelle pour chacun de ces choix.

**Cas 1 : $h(x) = 1$**
Si le classifieur prédit $h(x)=1$, une erreur se produit si l'étiquette réelle $Y$ est $-1$.
La probabilité d'erreur conditionnelle est donc :
$$P(h(x) \neq Y | X=x) = P(Y=-1 | X=x)$$
Nous savons que $P(Y=-1 | X=x) = 1 - P(Y=1 | X=x)$.
En utilisant la définition de la fonction de régression $\eta(x) = P(Y=1 | X=x)$, nous obtenons :
$$P(h(x) \neq Y | X=x) = 1 - \eta(x)$$

**Cas 2 : $h(x) = -1$**
Si le classifieur prédit $h(x)=-1$, une erreur se produit si l'étiquette réelle $Y$ est $1$.
La probabilité d'erreur conditionnelle est donc :
$$P(h(x) \neq Y | X=x) = P(Y=1 | X=x)$$
En utilisant la définition de $\eta(x)$, nous obtenons :
$$P(h(x) \neq Y | X=x) = \eta(x)$$

Pour minimiser $P(h(x) \neq Y | X=x)$, nous devons choisir la valeur de $h(x)$ qui correspond à la plus petite des deux probabilités : $\eta(x)$ ou $1 - \eta(x)$.

*   Si $\eta(x) < 1 - \eta(x)$ :
    Cela est équivalent à $2\eta(x) < 1$, soit $\eta(x) < 1/2$.
    Dans ce cas, la valeur minimale est $\eta(x)$, et nous choisissons $h(x) = -1$.
*   Si $1 - \eta(x) < \eta(x)$ :
    Cela est équivalent à $1 < 2\eta(x)$, soit $\eta(x) > 1/2$.
    Dans ce cas, la valeur minimale est $1 - \eta(x)$, et nous choisissons $h(x) = 1$.
*   Si $\eta(x) = 1 - \eta(x)$ :
    Cela est équivalent à $2\eta(x) = 1$, soit $\eta(x) = 1/2$.
    Dans ce cas, les deux choix $h(x)=1$ et $h(x)=-1$ conduisent à la même probabilité d'erreur conditionnelle de $1/2$. Pour garantir l'unicité de la définition du classifieur de Bayes, une convention est souvent adoptée, par exemple choisir $h^*(x)=1$.

En combinant ces conditions, le classifieur de Bayes optimal $h^*(x)$ est défini comme :
$$h^*(x) = \begin{cases} 1 & \text{si } \eta(x) \ge 1/2 \\ -1 & \text{si } \eta(x) < 1/2 \end{cases}$$
Cette fonction $h^*$ est mesurable car la fonction $\eta$ est mesurable et les seuils sont constants. Le classifieur $h^*(x)$ minimise la probabilité d'erreur conditionnelle pour chaque $x$, et par conséquent minimise le risque total $R(h)$, qui est l'espérance de ces probabilités d'erreur conditionnelles.

---

**3. Calculer le risque de Bayes $R(h^*)$.**

Le risque de Bayes $R(h^*)$ est le risque minimal atteignable par tout classifieur. Il est obtenu en remplaçant la probabilité d'erreur conditionnelle $P(h(X) \neq Y | X)$ par sa valeur minimale $\min(\eta(X), 1 - \eta(X))$ dans l'expression du risque dérivée à la question 1.
$$R(h^*) = E_X[P(h^*(X) \neq Y | X)]$$
Pour chaque $x \in \mathcal{X}$, la probabilité d'erreur minimale est :
$$P(h^*(x) \neq Y | X=x) = \min(\eta(x), 1 - \eta(x))$$
Donc, le risque de Bayes s'écrit :
$$R(h^*) = E_X[\min(\eta(X), 1 - \eta(X))]$$
Cette formule exprime le risque de Bayes comme l'espérance de la probabilité d'erreur conditionnelle minimale, moyennée sur toutes les entrées $X$ selon leur distribution $P_X$.

---

**4. On définit la marge conditionnelle $m: \mathcal{X} \to [-1, 1]$ par $m(x) = P(Y=1|X=x) - P(Y=-1|X=x)$. Réexprimer le classifieur de Bayes $h^*(x)$ et le risque de Bayes $R(h^*)$ en fonction de $m(x)$.**

Nous avons la définition de la marge conditionnelle :
$$m(x) = P(Y=1|X=x) - P(Y=-1|X=x)$$
Nous savons que $P(Y=1|X=x) = \eta(x)$ et $P(Y=-1|X=x) = 1 - \eta(x)$.
En substituant ces expressions dans la définition de $m(x)$ :
$$m(x) = \eta(x) - (1 - \eta(x))$$
$$m(x) = \eta(x) - 1 + \eta(x)$$
$$m(x) = 2\eta(x) - 1$$
Nous pouvons également exprimer $\eta(x)$ en fonction de $m(x)$ en résolvant pour $\eta(x)$ :
$$2\eta(x) = m(x) + 1 \implies \eta(x) = \frac{m(x) + 1}{2}$$

**Réexpression de $h^*(x)$ en fonction de $m(x)$ :**

Le classifieur de Bayes $h^*(x)$ est défini par les conditions sur $\eta(x)$ :
$$h^*(x) = \begin{cases} 1 & \text{si } \eta(x) \ge 1/2 \\ -1 & \text{si } \eta(x) < 1/2 \end{cases}$$
Substituons l'expression de $\eta(x)$ en fonction de $m(x)$ dans ces conditions :
*   **Condition $\eta(x) \ge 1/2$ :**
    $\frac{m(x) + 1}{2} \ge \frac{1}{2}$
    Multiplions les deux côtés par 2 :
    $m(x) + 1 \ge 1$
    Soustrayons 1 des deux côtés :
    $m(x) \ge 0$
*   **Condition $\eta(x) < 1/2$ :**
    $\frac{m(x) + 1}{2} < \frac{1}{2}$
    Multiplions les deux côtés par 2 :
    $m(x) + 1 < 1$
    Soustrayons 1 des deux côtés :
    $m(x) < 0$

Ainsi, le classifieur de Bayes $h^*(x)$ peut être exprimé comme :
$$h^*(x) = \begin{cases} 1 & \text{si } m(x) \ge 0 \\ -1 & \text{si } m(x) < 0 \end{cases}$$
Cette fonction est également connue sous la forme $h^*(x) = \text{sgn}(m(x))$, avec la convention que $\text{sgn}(0)=1$ pour maintenir la cohérence avec le choix $\eta(x) \ge 1/2 \implies h^*(x)=1$.

**Réexpression de $R(h^*)$ en fonction de $m(x)$ :**

Le risque de Bayes $R(h^*)$ est donné par $E_X[\min(\eta(X), 1 - \eta(X))]$.
Nous devons exprimer $\min(\eta(x), 1 - \eta(x))$ en fonction de $m(x)$.
Nous avons déjà les expressions :
$\eta(x) = \frac{m(x) + 1}{2}$
$1 - \eta(x) = 1 - \frac{m(x) + 1}{2} = \frac{2 - (m(x) + 1)}{2} = \frac{1 - m(x)}{2}$

Maintenant, nous cherchons $\min\left(\frac{m(x) + 1}{2}, \frac{1 - m(x)}{2}\right)$.
Puisque $Y \in \{-1, 1\}$, $P(Y=1|X=x) \in [0, 1]$ et $P(Y=-1|X=x) \in [0, 1]$, donc $m(x) \in [-1, 1]$.
*   Si $m(x) \ge 0$:
    Alors $m(x)+1 \ge 1-m(x)$ (car $2m(x) \ge 0$).
    Donc, $\min\left(\frac{m(x) + 1}{2}, \frac{1 - m(x)}{2}\right) = \frac{1 - m(x)}{2}$.
    Pour $m(x) \ge 0$, nous avons $|m(x)| = m(x)$. Par conséquent, $\frac{1 - m(x)}{2} = \frac{1 - |m(x)|}{2}$.
*   Si $m(x) < 0$:
    Alors $m(x)+1 < 1-m(x)$ (car $2m(x) < 0$).
    Donc, $\min\left(\frac{m(x) + 1}{2}, \frac{1 - m(x)}{2}\right) = \frac{m(x) + 1}{2}$.
    Pour $m(x) < 0$, nous avons $|m(x)| = -m(x)$, ce qui implique $m(x) = -|m(x)|$.
    Par conséquent, $\frac{m(x) + 1}{2} = \frac{-|m(x)| + 1}{2} = \frac{1 - |m(x)|}{2}$.

Dans les deux cas ($m(x) \ge 0$ et $m(x) < 0$), nous obtenons la même expression :
$$\min(\eta(x), 1 - \eta(x)) = \frac{1 - |m(x)|}{2}$$
En substituant cette expression dans la formule du risque de Bayes :
$$R(h^*) = E_X\left[\frac{1 - |m(X)|}{2}\right]$$
Par linéarité de l'espérance :
$$R(h^*) = \frac{1}{2} E_X[1 - |m(X)|]$$
$$R(h^*) = \frac{1}{2} (E_X[1] - E_X[|m(X)|])$$
Puisque $E_X[1] = 1$:
$$R(h^*) = \frac{1}{2} (1 - E_X[|m(X)|])$$