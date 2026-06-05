---
uuid: jalon-140-exo-06
title: "Exercice 6 - Classifieur de Bayes"
type: Exercice
difficulty: 3
---

### Énoncé

Soit un espace probabilisé $(\Omega, \mathcal{A}, P)$. Nous considérons la classification binaire avec un espace de caractéristiques $\mathcal{X}$ (un espace mesurable) et un espace d'étiquettes $\mathcal{Y} = \{-1, 1\}$. Soient $X: \Omega \to \mathcal{X}$ et $Y: \Omega \to \mathcal{Y}$ des variables aléatoires représentant respectivement les caractéristiques et l'étiquette. La distribution conjointe de $(X,Y)$ est $P_{X,Y}$.

Le problème de classification consiste à trouver une fonction $h: \mathcal{X} \to \mathcal{Y}$ (un classifieur) qui minimise le risque de classification, défini par la perte $0-1$:
$$ L_{01}(y, \hat{y}) = \mathbb{I}(y \neq \hat{y}) $$
où $\mathbb{I}(\cdot)$ est la fonction indicatrice. Le risque $0-1$ d'un classifieur $h$ est $R_{01}(h) = E[L_{01}(Y, h(X))]$.
Le classifieur de Bayes optimal, noté $h^*$, minimise $R_{01}(h)$. Il est donné par $h^*(x) = \text{sgn}(\eta(x) - 1/2)$, où $\eta(x) = P(Y=1|X=x)$ est la probabilité conditionnelle a posteriori.

Dans la pratique, la perte $0-1$ est non-convexe et difficile à optimiser. On utilise souvent une fonction de perte de substitution (surrogate loss) $\phi: \mathbb{R} \to \mathbb{R}$. Pour une fonction de score $f: \mathcal{X} \to \mathbb{R}$, le risque de substitution associé est $R_{\phi}(f) = E[\phi(Y f(X))]$. On cherche à trouver un $f$ qui minimise $R_{\phi}(f)$, et l'on forme ensuite le classifieur $h_f(x) = \text{sgn}(f(x))$.

Pour un $x \in \mathcal{X}$ donné, la minimisation du risque conditionnel $E[\phi(Y f(X))|X=x]$ par rapport à $f(x)$ conduit à minimiser la fonction $g_{\eta(x)}(t)$ définie par:
$$ g_{\eta}(t) = \eta \phi(t) + (1-\eta) \phi(-t) $$
où $\eta = \eta(x) = P(Y=1|X=x)$.

Une fonction de perte de substitution $\phi$ est dite *classification calibrée* (ou *Fisher consistante*) si minimiser le risque de substitution $R_{\phi}(f)$ pour une fonction de score $f$ implique que le classifieur $h_f(x) = \text{sgn}(f(x))$ est optimal par rapport à la perte $0-1$. Plus formellement, $\phi$ est classification calibrée si pour tout $\eta \in [0,1]$, tout $t^* \in \text{argmin}_{t \in \mathbb{R}} g_{\eta}(t)$ satisfait:
*   Si $\eta > 1/2$, alors $t^* > 0$.
*   Si $\eta < 1/2$, alors $t^* < 0$.
*   Si $\eta = 1/2$, alors $t^* = 0$.

Nous supposons que $\phi$ est une fonction strictement convexe et continûment différentiable sur $\mathbb{R}$.

**Question 1**:
Démontrer que la fonction de perte de substitution $\phi$ est classification calibrée si et seulement si sa dérivée en $0$ est strictement négative, c'est-à-dire $\phi'(0) < 0$.

**Question 2**:
En vous basant sur la condition établie en Question 1, donnez:
1.  Deux exemples de fonctions de perte de substitution couramment utilisées qui sont classification calibrées.
2.  Un exemple d'une fonction de perte de substitution convexe et différentiable qui n'est PAS classification calibrée.
Justifiez vos choix en détail.

### Correction

#### Typage des variables et des espaces

*   $(\Omega, \mathcal{A}, P)$ : Espace probabilisé, où $\Omega$ est l'ensemble des éventualités, $\mathcal{A}$ est une $\sigma$-algèbre sur $\Omega$, et $P$ est une mesure de probabilité sur $(\Omega, \mathcal{A})$.
*   $\mathcal{X}$ : Espace des caractéristiques, muni d'une $\sigma$-algèbre $\mathcal{B}_{\mathcal{X}}$ pour le rendre mesurable.
*   $\mathcal{Y} = \{-1, 1\}$ : Espace des étiquettes.
*   $X: \Omega \to \mathcal{X}$ : Variable aléatoire des caractéristiques, $\mathcal{A}$-$\mathcal{B}_{\mathcal{X}}$-mesurable.
*   $Y: \Omega \to \mathcal{Y}$ : Variable aléatoire de l'étiquette, $\mathcal{A}$-$\mathcal{P}(\mathcal{Y})$-mesurable.
*   $P_{X,Y}$ : Distribution conjointe de $(X,Y)$ sur $\mathcal{X} \times \mathcal{Y}$.
*   $\eta(x) = P(Y=1|X=x)$ : Probabilité conditionnelle a posteriori, définie $P_X$-presque partout sur $\mathcal{X}$.
*   $h: \mathcal{X} \to \mathcal{Y}$ : Un classifieur.
*   $f: \mathcal{X} \to \mathbb{R}$ : Une fonction de score.
*   $L_{01}: \mathcal{Y} \times \mathcal{Y} \to \{0,1\}$ : La fonction de perte $0-1$.
*   $\phi: \mathbb{R} \to \mathbb{R}$ : La fonction de perte de substitution, supposée strictement convexe et continûment différentiable.
*   $g_{\eta}: \mathbb{R} \to \mathbb{R}$ : La fonction de risque conditionnel pondéré, $g_{\eta}(t) = \eta \phi(t) + (1-\eta) \phi(-t)$.

#### Question 1 : Preuve de la condition de calibration

Soit $\phi: \mathbb{R} \to \mathbb{R}$ une fonction strictement convexe et continûment différentiable.
Nous voulons montrer que $\phi$ est classification calibrée si et seulement si $\phi'(0) < 0$.

**Partie 1: Démontrer que si $\phi$ est classification calibrée, alors $\phi'(0) < 0$.**

Supposons que $\phi$ est classification calibrée. Par définition, pour tout $\eta \in [0,1]$, tout $t^* \in \text{argmin}_{t \in \mathbb{R}} g_{\eta}(t)$ satisfait:
*   $t^* > 0$ si $\eta > 1/2$.
*   $t^* < 0$ si $\eta < 1/2$.
*   $t^* = 0$ si $\eta = 1/2$.

Puisque $\phi$ est strictement convexe et continûment différentiable, la fonction $g_{\eta}(t) = \eta \phi(t) + (1-\eta) \phi(-t)$ est également strictement convexe et continûment différentiable (la stricte convexité de $\phi$ implique $\phi''(t) \ge 0$, et $g_{\eta}''(t) = \eta \phi''(t) + (1-\eta)\phi''(-t) \ge 0$. Si $\phi''(t)>0$ pour tout $t$, alors $g_{\eta}''(t)>0$). Par conséquent, il existe un unique minimiseur $t^*$ de $g_{\eta}(t)$, qui satisfait la condition du premier ordre $g'_{\eta}(t^*) = 0$.

Calculons la dérivée de $g_{\eta}(t)$:
$$ g'_{\eta}(t) = \frac{d}{dt} \left( \eta \phi(t) + (1-\eta) \phi(-t) \right) = \eta \phi'(t) - (1-\eta) \phi'(-t) $$
(où l'on a utilisé la règle de la chaîne pour $\frac{d}{dt} \phi(-t) = -\phi'(-t)$).

Évaluons cette dérivée en $t=0$:
$$ g'_{\eta}(0) = \eta \phi'(0) - (1-\eta) \phi'(0) = (2\eta - 1) \phi'(0) $$

Considérons le cas où $\eta > 1/2$. La condition de calibration implique que le minimiseur $t^*$ doit être strictement positif ($t^* > 0$). Pour qu'un minimiseur unique $t^* > 0$ existe pour une fonction strictement convexe et différentiable, sa dérivée en $t=0$ doit être strictement négative (pour que la fonction décroisse initialement vers un minimum positif).
Donc, si $\eta > 1/2$, il faut que $g'_{\eta}(0) < 0$.
$$ (2\eta - 1) \phi'(0) < 0 $$
Puisque $\eta > 1/2$, nous avons $2\eta - 1 > 0$. Par conséquent, nous devons avoir $\phi'(0) < 0$.

Considérons le cas où $\eta < 1/2$. La condition de calibration implique que le minimiseur $t^*$ doit être strictement négatif ($t^* < 0$). Pour qu'un minimiseur unique $t^* < 0$ existe pour une fonction strictement convexe et différentiable, sa dérivée en $t=0$ doit être strictement positive (pour que la fonction croisse initialement vers un minimum négatif).
Donc, si $\eta < 1/2$, il faut que $g'_{\eta}(0) > 0$.
$$ (2\eta - 1) \phi'(0) > 0 $$
Puisque $\eta < 1/2$, nous avons $2\eta - 1 < 0$. Par conséquent, nous devons avoir $\phi'(0) < 0$.

Les deux cas $\eta > 1/2$ et $\eta < 1/2$ conduisent à la même condition nécessaire: $\phi'(0) < 0$.
Il est important de noter que $\phi'(0)$ ne peut pas être nul. Si $\phi'(0) = 0$, alors $g'_{\eta}(0)=0$ pour tout $\eta$.
Si $\phi'(0)=0$, alors pour $\eta > 1/2$, $g'_{\eta}(0)=0$. De plus, puisque $\phi$ est strictement convexe et différentiable, $\phi'$ est strictement croissante.
Pour tout $t > 0$: $\phi'(t) > \phi'(0) = 0$. Pour tout $t < 0$: $\phi'(t) < \phi'(0) = 0$.
Alors, pour $t > 0$:
$$ g'_{\eta}(t) = \eta \phi'(t) - (1-\eta) \phi'(-t) $$
Puisque $t>0$, $-t<0$. Donc $\phi'(t)>0$ et $\phi'(-t)<0$.
$$ g'_{\eta}(t) = \eta (\text{positif}) - (1-\eta) (\text{négatif}) = (\text{positif}) + (\text{positif}) > 0 $$
Ainsi, pour $t>0$, $g'_{\eta}(t) > 0$. Cela signifie que $g_{\eta}(t)$ est strictement croissante pour $t>0$.
Comme $g'_{\eta}(0)=0$, et $g_{\eta}(t)$ est strictement croissante pour $t>0$, le minimiseur unique $t^*$ de $g_{\eta}(t)$ doit être $\le 0$. Ceci contredit la condition de calibration pour $\eta > 1/2$ (qui exige $t^* > 0$).
Donc, $\phi'(0)$ ne peut pas être $0$.
En combinant avec $\phi'(0) \le 0$, nous obtenons $\phi'(0) < 0$.

**Partie 2: Démontrer que si $\phi'(0) < 0$, alors $\phi$ est classification calibrée.**

Supposons que $\phi$ est strictement convexe, continûment différentiable, et que $\phi'(0) < 0$.
Nous devons vérifier les trois conditions de calibration.

1.  **Cas $\eta > 1/2$**:
    Nous avons $g'_{\eta}(0) = (2\eta - 1) \phi'(0)$. Puisque $\eta > 1/2$, $2\eta - 1 > 0$. Puisque $\phi'(0) < 0$, il s'ensuit que $g'_{\eta}(0) < 0$.
    Comme $g_{\eta}(t)$ est strictement convexe (car $\phi$ est strictement convexe), sa dérivée $g'_{\eta}(t)$ est strictement croissante.
    Puisque $g'_{\eta}(0) < 0$ et $g'_{\eta}(t)$ est strictement croissante, il existe un unique $t^* > 0$ tel que $g'_{\eta}(t^*) = 0$. Ce $t^*$ est le minimiseur unique de $g_{\eta}(t)$, et il est strictement positif. La condition est satisfaite.

2.  **Cas $\eta < 1/2$**:
    Nous avons $g'_{\eta}(0) = (2\eta - 1) \phi'(0)$. Puisque $\eta < 1/2$, $2\eta - 1 < 0$. Puisque $\phi'(0) < 0$, il s'ensuit que $g'_{\eta}(0) > 0$.
    Comme $g_{\eta}(t)$ est strictement convexe, sa dérivée $g'_{\eta}(t)$ est strictement croissante.
    Puisque $g'_{\eta}(0) > 0$ et $g'_{\eta}(t)$ est strictement croissante, il existe un unique $t^* < 0$ tel que $g'_{\eta}(t^*) = 0$. Ce $t^*$ est le minimiseur unique de $g_{\eta}(t)$, et il est strictement négatif. La condition est satisfaite.

3.  **Cas $\eta = 1/2$**:
    Nous avons $g'_{1/2}(0) = (2(1/2) - 1) \phi'(0) = 0 \cdot \phi'(0) = 0$.
    $g'_{1/2}(t) = \frac{1}{2}(\phi'(t) - \phi'(-t))$.
    Puisque $\phi$ est strictement convexe, $\phi'$ est strictement croissante.
    Pour $t > 0$: $t > -t$. Comme $\phi'$ est strictement croissante, $\phi'(t) > \phi'(-t)$. Donc $g'_{1/2}(t) = \frac{1}{2}(\phi'(t) - \phi'(-t)) > 0$.
    Pour $t < 0$: $t < -t$. Comme $\phi'$ est strictement croissante, $\phi'(t) < \phi'(-t)$. Donc $g'_{1/2}(t) = \frac{1}{2}(\phi'(t) - \phi'(-t)) < 0$.
    Ceci implique que $g'_{1/2}(t)$ est négative pour $t<0$, nulle pour $t=0$, et positive pour $t>0$. Par conséquent, $t=0$ est l'unique minimiseur de $g_{1/2}(t)$. La condition est satisfaite.

Puisque toutes les conditions sont satisfaites, $\phi$ est classification calibrée.

**Conclusion de la Question 1**: Une fonction de perte de substitution $\phi$ qui est strictement convexe et continûment différentiable est classification calibrée si et seulement si $\phi'(0) < 0$.

#### Question 2 : Exemples de fonctions de perte

Nous utilisons la condition établie : $\phi$ doit être strictement convexe et continûment différentiable avec $\phi'(0) < 0$.

**1. Exemples de pertes classification calibrées:**

a)  **La perte exponentielle (Exponential Loss)**: $\phi(t) = e^{-t}$
    *   **Stricte convexité**: $\phi'(t) = -e^{-t}$ et $\phi''(t) = e^{-t}$. Puisque $\phi''(t) > 0$ pour tout $t \in \mathbb{R}$, $\phi$ est strictement convexe.
    *   **Différentiabilité**: $\phi$ est continûment différentiable de manière triviale (exponentielle).
    *   **Condition $\phi'(0) < 0$**: $\phi'(0) = -e^{-0} = -1$. Puisque $-1 < 0$, la condition est satisfaite.
    *   **Conclusion**: La perte exponentielle est classification calibrée.

b)  **La perte logistique (Logistic Loss)**: $\phi(t) = \log(1+e^{-t})$
    *   **Stricte convexité**:
        $\phi'(t) = \frac{-e^{-t}}{1+e^{-t}}$
        $\phi''(t) = \frac{-(-e^{-t})(1+e^{-t}) - (-e^{-t})(-e^{-t})}{(1+e^{-t})^2} = \frac{e^{-t}(1+e^{-t}) - e^{-2t}}{(1+e^{-t})^2} = \frac{e^{-t} + e^{-2t} - e^{-2t}}{(1+e^{-t})^2} = \frac{e^{-t}}{(1+e^{-t})^2}$.
        Puisque $\phi''(t) > 0$ pour tout $t \in \mathbb{R}$, $\phi$ est strictement convexe.
    *   **Différentiabilité**: $\phi$ est continûment différentiable.
    *   **Condition $\phi'(0) < 0$**: $\phi'(0) = \frac{-e^{-0}}{1+e^{-0}} = \frac{-1}{1+1} = -1/2$. Puisque $-1/2 < 0$, la condition est satisfaite.
    *   **Conclusion**: La perte logistique est classification calibrée.

c)  **La perte au carré (Squared Error Loss) modifiée pour la classification**: $\phi(t) = \frac{1}{2}(1-t)^2$
    *   **Stricte convexité**: $\phi'(t) = -(1-t)$ et $\phi''(t) = 1$. Puisque $\phi''(t) = 1 > 0$ pour tout $t \in \mathbb{R}$, $\phi$ est strictement convexe.
    *   **Différentiabilité**: $\phi$ est continûment différentiable.
    *   **Condition $\phi'(0) < 0$**: $\phi'(0) = -(1-0) = -1$. Puisque $-1 < 0$, la condition est satisfaite.
    *   **Conclusion**: Cette perte au carré est classification calibrée.

**2. Exemple d'une perte non-calibrée (mais convexe et différentiable):**

**La perte quadratique centrée**: $\phi(t) = t^2 + C$, où $C$ est une constante. Pour simplifier, prenons $C=0$, donc $\phi(t) = t^2$.
    *   **Stricte convexité**: $\phi'(t) = 2t$ et $\phi''(t) = 2$. Puisque $\phi''(t) = 2 > 0$ pour tout $t \in \mathbb{R}$, $\phi$ est strictement convexe.
    *   **Différentiabilité**: $\phi$ est continûment différentiable.
    *   **Condition $\phi'(0) < 0$**: $\phi'(0) = 2(0) = 0$. Puisque $\phi'(0) = 0$, la condition n'est PAS satisfaite.
    *   **Justification détaillée de la non-calibration**: D'après la preuve de la Question 1, si $\phi'(0) = 0$, alors pour tout $\eta \in [0,1]$, on a $g'_{\eta}(0)=0$.
        Pour $\eta > 1/2$ (par exemple $\eta = 0.75$), le minimiseur $t^*$ devrait être positif.
        Cependant, pour $\phi(t)=t^2$:
        $g_{\eta}(t) = \eta t^2 + (1-\eta) (-t)^2 = \eta t^2 + (1-\eta) t^2 = t^2$.
        Le minimiseur de $g_{\eta}(t)=t^2$ est $t^*=0$, et ce pour toute valeur de $\eta$.
        Ceci contredit la définition de la calibration qui exige $t^* > 0$ pour $\eta > 1/2$ et $t^* < 0$ pour $\eta < 1/2$.
        Par conséquent, la perte $\phi(t)=t^2$ n'est PAS classification calibrée.