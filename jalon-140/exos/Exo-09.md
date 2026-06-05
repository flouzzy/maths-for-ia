```yaml
---
uuid: jalon-140-exo-09
title: "Exercice 9 - Classifieur de Bayes"
type: Exercice
difficulty: 5
---

### Exercice 9 - Classifieur de Bayes

#### Énoncé

Soit un problème de classification binaire supervisé. On dispose d'un espace mesurable d'entrée $(\mathcal{X}, \mathcal{A}_{\mathcal{X}})$ et d'un espace mesurable de sortie $(\mathcal{Y}, \mathcal{A}_{\mathcal{Y}})$, où $\mathcal{Y} = \{-1, 1\}$.
Soit $(X, Y)$ un vecteur aléatoire défini sur un espace de probabilité $(\Omega, \mathcal{F}, P)$, à valeurs dans $\mathcal{X} \times \mathcal{Y}$. La distribution $P_{X,Y}$ est inconnue. On note $\eta(x) = P(Y=1|X=x)$ la probabilité conditionnelle a posteriori pour $X=x$.

**Partie 1 : Classifieur de Bayes Optimal et Risque 0-1**

1.  **Définition du Risque 0-1 :** La fonction de perte 0-1 est définie par $\ell_{01}: \mathcal{Y} \times \mathcal{Y} \to \{0, 1\}$ avec $\ell_{01}(y', y) = \mathbf{1}_{y' \neq y}$. Pour un classifieur mesurable $h: \mathcal{X} \to \mathcal{Y}$, le risque associé est $R(h) = E[\ell_{01}(h(X), Y)]$. Démontrer que ce risque peut s'écrire $R(h) = E_X[ \eta(X) \mathbf{1}_{h(X)=-1} + (1-\eta(X)) \mathbf{1}_{h(X)=1} ]$.
2.  **Classifieur de Bayes :** Démontrer que le classifieur de Bayes $h^*$, qui minimise le risque $R(h)$, est donné par $h^*(x) = \text{sgn}(\eta(x) - 1/2)$, où $\text{sgn}(0)$ est défini par convention comme $1$. Préciser le risque de Bayes $R^* = R(h^*)$.
3.  **Excès de Risque :** Pour un classifieur $h$, l'excès de risque 0-1 est $R(h) - R^*$. Montrer que $R(h) - R^* = E_X[ 2|\eta(X) - 1/2| \mathbf{1}_{h(X) \neq h^*(X)} ]$.

**Partie 2 : Fonction de Perte de Substitution Logistique**

Considérons une fonction de score mesurable $f: \mathcal{X} \to \mathbb{R}$ telle que le classifieur associé est $h_f(x) = \text{sgn}(f(x))$.
La fonction de perte logistique est définie pour $z \in \mathbb{R}$ par $\phi(z) = \log(1+e^{-z})$. Le risque logistique associé à la fonction $f$ est $R_{\phi}(f) = E[\phi(Y f(X))]$.

4.  **Minimisation du Risque Logistique Conditionnel :** Pour un $x \in \mathcal{X}$ fixé, et un scalaire $t \in \mathbb{R}$, on définit la fonction $g_{\eta(x)}(t) = E[\phi(Y t) | X=x]$. Démontrer que $g_{\eta(x)}(t) = \eta(x) \log(1+e^{-t}) + (1-\eta(x)) \log(1+e^t)$.
5.  **Minimisation de $g_{\eta(x)}(t)$ :** Montrer que la minimisation de $g_{\eta(x)}(t)$ par rapport à $t$ est équivalente à résoudre l'équation $\eta(x) = \frac{e^t}{1+e^t}$. Déduire que la fonction $f_{\phi}^*(x)$ qui minimise $R_{\phi}(f)$ pour tout $x$ (presque sûrement) est donnée par $f_{\phi}^*(x) = \log \left( \frac{\eta(x)}{1-\eta(x)} \right)$.

**Partie 3 : Consistance et Inégalité de Zhang**

6.  **Calibration :** Montrer que la perte logistique est calibrée par rapport à la perte 0-1. C'est-à-dire, montrer que pour tout $x \in \mathcal{X}$, $\text{sgn}(f_{\phi}^*(x)) = h^*(x)$. Expliquer la signification de ce résultat en termes de consistance.
7.  **Inégalité de Zhang (Borne Locale) :**
    Soit $f: \mathcal{X} \to \mathbb{R}$ une fonction de score et $h_f(x) = \text{sgn}(f(x))$. Soit $f_{\phi}^*$ la fonction de score logistique optimale et $R_{\phi}^* = R_{\phi}(f_{\phi}^*)$.
    On définit l'excès de risque logistique conditionnel par $\Delta_{\phi}(x, t) = \mathcal{H}(\eta(x), t) - \mathcal{H}(\eta(x), f_{\phi}^*(x))$, où $\mathcal{H}(\eta, t) = \eta \log(1+e^{-t}) + (1-\eta) \log(1+e^t)$.
    a. Démontrer que $\Delta_{\phi}(x, t) = D_{KL}(\text{Bernoulli}(\eta(x)) || \text{Bernoulli}(\sigma(t)))$, où $\sigma(t) = \frac{e^t}{1+e^t}$ et $D_{KL}$ est la divergence de Kullback-Leibler.
    b. Utiliser l'inégalité de Pinsker, qui stipule que pour deux distributions de Bernoulli $P, Q$ avec probabilités de succès $p, q$, $D_{KL}(p || q) \geq 2(p-q)^2$ (pour une version simplifiée et plus lâche de Pinsker), pour montrer que $(\eta(x) - \sigma(t))^2 \leq \frac{1}{2} \Delta_{\phi}(x, t)$.
    c. Montrer que si $\text{sgn}(t) \neq h^*(x)$, alors $|\eta(x) - 1/2| \leq |\eta(x) - \sigma(t)|$.
    d. En déduire qu'il existe une constante $C > 0$ telle que, pour tout $x \in \mathcal{X}$ et pour tout $t \in \mathbb{R}$:
       $2|\eta(x) - 1/2| \mathbf{1}_{\text{sgn}(t) \neq h^*(x)} \leq C \sqrt{\Delta_{\phi}(x, t)}$.
    e. En intégrant sur $X$, conclure à l'inégalité de Zhang : $R(h_f) - R^* \leq E_X[ C \sqrt{\Delta_{\phi}(X, f(X))} ]$. Expliquer pourquoi ce résultat est important pour la théorie de l'apprentissage statistique.

---

### CORRECTION

#### Partie 1 : Classifieur de Bayes Optimal et Risque 0-1

1.  **Définition du Risque 0-1 :**
    Soit $(\mathcal{X}, \mathcal{A}_{\mathcal{X}})$ l'espace mesurable d'entrée et $(\mathcal{Y}, \mathcal{A}_{\mathcal{Y}})$ l'espace mesurable de sortie, avec $\mathcal{Y} = \{-1, 1\}$.
    Soit $(X, Y)$ un vecteur aléatoire sur un espace de probabilité $(\Omega, \mathcal{F}, P)$, à valeurs dans $\mathcal{X} \times \mathcal{Y}$. Sa distribution est notée $P_{X,Y}$.
    La fonction de perte 0-1 est $\ell_{01}: \mathcal{Y} \times \mathcal{Y} \to \{0, 1\}$ définie par $\ell_{01}(y', y) = \mathbf{1}_{y' \neq y}$.
    Pour un classifieur mesurable $h: \mathcal{X} \to \mathcal{Y}$, le risque associé est $R(h) = E[\ell_{01}(h(X), Y)]$.
    Par la formule de l'espérance totale (ou d'espérance conditionnelle itérée), $R(h) = E_X[E[\ell_{01}(h(X), Y) | X]]$.
    Fixons $x \in \mathcal{X}$. L'espérance conditionnelle de la perte est :
    $$E[\ell_{01}(h(X), Y) | X=x] = E[\mathbf{1}_{h(x) \neq Y} | X=x]$$
    $$= P(h(x) \neq Y | X=x)$$
    Puisque $\mathcal{Y} = \{-1, 1\}$, cette probabilité peut être décomposée en deux cas mutuellement exclusifs :
    $$P(h(x) \neq Y | X=x) = P(Y=1, h(x)=-1 | X=x) + P(Y=-1, h(x)=1 | X=x)$$
    Par définition des probabilités conditionnelles, et puisque $h(x)$ est une valeur fixe pour un $x$ donné :
    $$= P(Y=1 | X=x) \mathbf{1}_{h(x)=-1} + P(Y=-1 | X=x) \mathbf{1}_{h(x)=1}$$
    En utilisant la notation $\eta(x) = P(Y=1|X=x)$, nous avons $P(Y=-1|X=x) = 1 - P(Y=1|X=x) = 1 - \eta(x)$.
    Donc, l'espérance conditionnelle devient :
    $$E[\ell_{01}(h(X), Y) | X=x] = \eta(x) \mathbf{1}_{h(x)=-1} + (1-\eta(x)) \mathbf{1}_{h(x)=1}$$
    En intégrant cette espérance conditionnelle sur la distribution de $X$, nous obtenons le risque total :
    $$R(h) = E_X[ \eta(X) \mathbf{1}_{h(X)=-1} + (1-\eta(X)) \mathbf{1}_{h(X)=1} ]$$

2.  **Classifieur de Bayes :**
    Pour minimiser le risque $R(h)$, il est nécessaire et suffisant de minimiser l'intégrande $E[\ell_{01}(h(X), Y) | X=x]$ pour chaque $x \in \mathcal{X}$ (pour presque tout $x$ par rapport à la mesure de $X$).
    Soit $x \in \mathcal{X}$ fixé. Nous devons choisir $h(x) \in \{-1, 1\}$ pour minimiser l'expression $L(h(x)) = \eta(x) \mathbf{1}_{h(x)=-1} + (1-\eta(x)) \mathbf{1}_{h(x)=1}$.
    *   Si nous choisissons $h(x)=1$, la valeur de la perte conditionnelle est $L(1) = (1-\eta(x))$.
    *   Si nous choisissons $h(x)=-1$, la valeur de la perte conditionnelle est $L(-1) = \eta(x)$.
    Le choix optimal $h^*(x)$ sera celui qui donne la valeur minimale :
    *   Si $1-\eta(x) < \eta(x) \implies 1 < 2\eta(x) \implies \eta(x) > 1/2$, alors $h^*(x)=1$.
    *   Si $\eta(x) < 1-\eta(x) \implies 2\eta(x) < 1 \implies \eta(x) < 1/2$, alors $h^*(x)=-1$.
    *   Si $\eta(x) = 1/2$, les deux choix donnent la même perte conditionnelle de $1/2$. Par convention, nous définissons $\text{sgn}(0)=1$, donc $h^*(x)=1$.
    Ces conditions peuvent être résumées par la fonction $\text{sgn}$:
    $$h^*(x) = \text{sgn}(\eta(x) - 1/2)$$
    Le classifieur de Bayes $h^*$ est donc $h^*(x) = \text{sgn}(\eta(x) - 1/2)$ pour presque tout $x \in \mathcal{X}$.
    Le risque de Bayes $R^* = R(h^*)$ est obtenu en substituant $h^*(x)$ dans l'expression du risque :
    $$R^* = E_X[ \eta(X) \mathbf{1}_{h^*(X)=-1} + (1-\eta(X)) \mathbf{1}_{h^*(X)=1} ]$$
    Pour un $x$ donné :
    *   Si $\eta(x) > 1/2$, alors $h^*(x)=1$, et la perte conditionnelle est $1-\eta(x)$.
    *   Si $\eta(x) < 1/2$, alors $h^*(x)=-1$, et la perte conditionnelle est $\eta(x)$.
    *   Si $\eta(x) = 1/2$, alors $h^*(x)=1$, et la perte conditionnelle est $1-\eta(x) = 1/2$.
    Dans tous les cas, la perte conditionnelle minimale est $\min(\eta(x), 1-\eta(x))$.
    Nous pouvons exprimer $\min(\eta(x), 1-\eta(x))$ comme $1/2 - |\eta(x) - 1/2|$.
    Par conséquent, le risque de Bayes est :
    $$R^* = E_X[ \min(\eta(X), 1-\eta(X)) ] = E_X[ 1/2 - |\eta(X) - 1/2| ] = 1/2 - E_X[|\eta(X) - 1/2|]$$

3.  **Excès de Risque :**
    L'excès de risque 0-1 pour un classifieur $h$ est $R(h) - R^*$.
    $$R(h) - R^* = E_X[ (\eta(X) \mathbf{1}_{h(X)=-1} + (1-\eta(X)) \mathbf{1}_{h(X)=1}) - \min(\eta(X), 1-\eta(X)) ]$$
    Concentrons-nous sur la différence de risque conditionnel pour un $x$ donné :
    $$\Delta_x(h(x)) = (\eta(x) \mathbf{1}_{h(x)=-1} + (1-\eta(x)) \mathbf{1}_{h(x)=1}) - \min(\eta(x), 1-\eta(x))$$
    Analysons $\Delta_x(h(x))$ en fonction de $\eta(x)$ et $h(x)$ :
    *   **Cas 1 : $\eta(x) > 1/2$.** Alors $h^*(x)=1$, et $\min(\eta(x), 1-\eta(x)) = 1-\eta(x)$.
        *   Si $h(x)=1$ (i.e., $h(x) = h^*(x)$) : $\Delta_x(1) = (1-\eta(x)) - (1-\eta(x)) = 0$.
        *   Si $h(x)=-1$ (i.e., $h(x) \neq h^*(x)$) : $\Delta_x(-1) = \eta(x) - (1-\eta(x)) = 2\eta(x) - 1$.
            Puisque $\eta(x) > 1/2$, $2\eta(x) - 1 = 2(\eta(x) - 1/2) = 2|\eta(x) - 1/2|$.
    *   **Cas 2 : $\eta(x) < 1/2$.** Alors $h^*(x)=-1$, et $\min(\eta(x), 1-\eta(x)) = \eta(x)$.
        *   Si $h(x)=-1$ (i.e., $h(x) = h^*(x)$) : $\Delta_x(-1) = \eta(x) - \eta(x) = 0$.
        *   Si $h(x)=1$ (i.e., $h(x) \neq h^*(x)$) : $\Delta_x(1) = (1-\eta(x)) - \eta(x) = 1 - 2\eta(x)$.
            Puisque $\eta(x) < 1/2$, $1 - 2\eta(x) = 2(1/2 - \eta(x)) = 2|\eta(x) - 1/2|$.
    *   **Cas 3 : $\eta(x) = 1/2$.** Alors $h^*(x)=1$ (par convention $\text{sgn}(0)=1$), et $\min(\eta(x), 1-\eta(x)) = 1/2$.
        *   Si $h(x)=1$ (i.e., $h(x) = h^*(x)$) : $\Delta_x(1) = 1/2 - 1/2 = 0$.
        *   Si $h(x)=-1$ (i.e., $h(x) \neq h^*(x)$) : $\Delta_x(-1) = 1/2 - 1/2 = 0$.
            Dans ce cas, $2|\eta(x) - 1/2| = 0$, donc la contribution à l'excès de risque est bien 0.
    En résumé, la contribution conditionnelle à l'excès de risque est $2|\eta(x) - 1/2|$ si $h(x) \neq h^*(x)$, et $0$ si $h(x) = h^*(x)$.
    Nous pouvons donc écrire : $\Delta_x(h(x)) = 2|\eta(x) - 1/2| \mathbf{1}_{h(x) \neq h^*(x)}$.
    En intégrant sur $X$, l'excès de risque total est :
    $$R(h) - R^* = E_X[ 2|\eta(X) - 1/2| \mathbf{1}_{h(X) \neq h^*(X)} ]$$

#### Partie 2 : Fonction de Perte de Substitution Logistique

4.  **Minimisation du Risque Logistique Conditionnel :**
    La fonction de perte logistique est $\phi: \mathbb{R} \to \mathbb{R}$ définie par $\phi(z) = \log(1+e^{-z})$.
    Le risque logistique associé à une fonction de score mesurable $f: \mathcal{X} \to \mathbb{R}$ est $R_{\phi}(f) = E[\phi(Y f(X))]$.
    Pour un $x \in \mathcal{X}$ fixé, et un scalaire $t \in \mathbb{R}$, nous définissons la fonction d'excès de risque conditionnel logistique $g_{\eta(x)}(t) = E[\phi(Y t) | X=x]$.
    Par la loi de l'espérance conditionnelle discrète (pour $Y \in \{-1, 1\}$) :
    $$g_{\eta(x)}(t) = P(Y=1|X=x) \phi(1 \cdot t) + P(Y=-1|X=x) \phi(-1 \cdot t)$$
    En utilisant $\eta(x) = P(Y=1|X=x)$ et $P(Y=-1|X=x) = 1-\eta(x)$ :
    $$g_{\eta(x)}(t) = \eta(x) \phi(t) + (1-\eta(x)) \phi(-t)$$
    En substituant la définition de $\phi(z) = \log(1+e^{-z})$ :
    $$g_{\eta(x)}(t) = \eta(x) \log(1+e^{-t}) + (1-\eta(x)) \log(1+e^{-(-t)})$$
    $$g_{\eta(x)}(t) = \eta(x) \log(1+e^{-t}) + (1-\eta(x)) \log(1+e^t)$$

5.  **Minimisation de $g_{\eta(x)}(t)$ :**
    La fonction $\phi(z) = \log(1+e^{-z})$ est strictement convexe. Sa dérivée seconde $\phi''(z) = \frac{e^z}{(e^z+1)^2} > 0$ pour tout $z \in \mathbb{R}$.
    Par conséquent, $g_{\eta(x)}(t)$ est une combinaison convexe de fonctions convexes (pour $\eta(x) \in [0,1]$), donc elle est strictement convexe par rapport à $t$. Son minimum est unique et est trouvé en annulant sa dérivée première par rapport à $t$.
    Calculons la dérivée première de $g_{\eta(x)}(t)$:
    $$\frac{\partial}{\partial t} g_{\eta(x)}(t) = \eta(x) \frac{\partial}{\partial t} \log(1+e^{-t}) + (1-\eta(x)) \frac{\partial}{\partial t} \log(1+e^t)$$
    On a $\frac{\partial}{\partial t} \log(1+e^{-t}) = \frac{-e^{-t}}{1+e^{-t}} = \frac{-1}{e^t+1}$.
    Et $\frac{\partial}{\partial t} \log(1+e^t) = \frac{e^t}{1+e^t}$.
    Donc, en annulant la dérivée première :
    $$-\eta(x) \frac{1}{e^t+1} + (1-\eta(x)) \frac{e^t}{e^t+1} = 0$$
    Puisque $e^t+1 > 0$, nous pouvons multiplier par $(e^t+1)$:
    $$-\eta(x) + (1-\eta(x))e^t = 0$$
    $$(1-\eta(x))e^t = \eta(x)$$
    Si $1-\eta(x) \neq 0$ (c'est-à-dire $\eta(x) \neq 1$), nous pouvons diviser par $1-\eta(x)$ :
    $$e^t = \frac{\eta(x)}{1-\eta(x)}$$
    Pour $\eta(x) = 1$, l'équation devient $0 = 1$, ce qui est impossible. Cela signifie que si $\eta(x)=1$, la perte est $\log(1+e^{-t})$, qui est minimisée lorsque $t \to \infty$. Dans ce cas, $f_{\phi}^*(x)$ serait $\infty$.
    Pour $\eta(x)=0$, l'équation devient $e^t = 0$, ce qui est impossible. Cela signifie que si $\eta(x)=0$, la perte est $\log(1+e^t)$, qui est minimisée lorsque $t \to -\infty$. Dans ce cas, $f_{\phi}^*(x)$ serait $-\infty$.
    En dehors de ces cas limites, nous prenons le logarithme naturel :
    $$t = \log \left( \frac{\eta(x)}{1-\eta(x)} \right)$$
    Cette valeur de $t$ est la fonction de score logistique optimale $f_{\phi}^*(x)$.
    $$f_{\phi}^*(x) = \log \left( \frac{\eta(x)}{1-\eta(x)} \right)$$
    Cette fonction est connue sous le nom de "logit" de $\eta(x)$, c'est-à-dire $f_{\phi}^*(x) = \text{logit}(\eta(x))$.
    L'équation $\eta(x) = \frac{e^t}{1+e^t}$ est la fonction inverse du logit, la fonction sigmoïde $\sigma(t)$. Sa résolution pour $t$ conduit directement à $t = \log \left( \frac{\eta(x)}{1-\eta(x)} \right)$. La minimisation de $g_{\eta(x)}(t)$ est donc équivalente à résoudre $\eta(x) = \sigma(t)$.

#### Partie 3 : Consistance et Inégalité de Zhang

6.  **Calibration :**
    Une fonction de perte de substitution $\phi$ est dite calibrée par rapport à la perte 0-1 si la minimisation du risque $\phi$-associé conduit à un classifieur dont le signe est celui du classifieur de Bayes optimal. Formellement, il faut montrer que $\text{sgn}(f_{\phi}^*(x)) = h^*(x)$ pour tout $x \in \mathcal{X}$ (presque sûrement).
    Nous avons $h^*(x) = \text{sgn}(\eta(x) - 1/2)$ et $f_{\phi}^*(x) = \log \left( \frac{\eta(x)}{1-\eta(x)} \right)$.
    Analysons les cas pour $\eta(x) \in [0,1]$ :
    *   **Si $\eta(x) > 1/2$ :**
        *   Alors $\eta(x) - 1/2 > 0$, donc $h^*(x)=1$.
        *   Pour $f_{\phi}^*(x)$, on a $\eta(x) > 1-\eta(x)$, ce qui implique $\frac{\eta(x)}{1-\eta(x)} > 1$.
        *   Puisque la fonction $\log(u)$ est strictement croissante, $\log \left( \frac{\eta(x)}{1-\eta(x)} \right) > \log(1) = 0$.
        *   Donc, $f_{\phi}^*(x) > 0$, ce qui implique $\text{sgn}(f_{\phi}^*(x))=1$.
        Dans ce cas, $\text{sgn}(f_{\phi}^*(x)) = h^*(x)$.
    *   **Si $\eta(x) < 1/2$ :**
        *   Alors $\eta(x) - 1/2 < 0$, donc $h^*(x)=-1$.
        *   Pour $f_{\phi}^*(x)$, on a $\eta(x) < 1-\eta(x)$, ce qui implique $0 < \frac{\eta(x)}{1-\eta(x)} < 1$.
        *   Donc, $\log \left( \frac{\eta(x)}{1-\eta(x)} \right) < \log(1) = 0$.
        *   Donc, $f_{\phi}^*(x) < 0$, ce qui implique $\text{sgn}(f_{\phi}^*(x))=-1$.
        Dans ce cas, $\text{sgn}(f_{\phi}^*(x)) = h^*(x)$.
    *   **Si $\eta(x) = 1/2$ :**
        *   Alors $\eta(x) - 1/2 = 0$. Par convention, $h^*(x)=1$.
        *   Pour $f_{\phi}^*(x)$, on a $\frac{\eta(x)}{1-\eta(x)} = \frac{1/2}{1/2} = 1$.
        *   Donc, $\log(1) = 0$.
        *   Par convention, $\text{sgn}(0)=1$. Donc $\text{sgn}(f_{\phi}^*(x))=1$.
        Dans ce cas, $\text{sgn}(f_{\phi}^*(x)) = h^*(x)$.
    Dans tous les cas, $\text{sgn}(f_{\phi}^*(x)) = h^*(x)$.
    Ceci démontre que la perte logistique est **calibrée** par rapport à la perte 0-1.
    La signification de ce résultat est fondamentale en apprentissage statistique : un algorithme qui minimise le risque logistique (par exemple, la régression logistique) convergera, avec suffisamment de données d'entraînement et une capacité suffisante du modèle, vers une fonction de score $f_{\phi}^*$ dont le signe reproduit celui du classifieur de Bayes optimal $h^*$. Cela garantit la **consistance** de la méthode : en minimisant la perte de substitution, on se rapproche du classifieur optimal en termes de perte 0-1, ce qui est le but final de la classification.

7.  **Inégalité de Zhang (Borne Locale) :**
    a. Démontrer que $\Delta_{\phi}(x, t) = D_{KL}(\text{Bernoulli}(\eta(x)) || \text{Bernoulli}(\sigma(t)))$.
    Nous avons $\mathcal{H}(\eta, t) = \eta \log(1+e^{-t}) + (1-\eta) \log(1+e^t)$.
    Recall $\sigma(t) = \frac{e^t}{1+e^t}$, donc $1-\sigma(t) = \frac{1}{1+e^t}$.
    Nous pouvons réécrire $\log(1+e^{-t}) = \log\left(\frac{1+e^t}{e^t}\right) = \log(1+e^t) - t$.
    Alternativement, $\log(1+e^{-t}) = \log(1/(1-\sigma(t)))$.
    Et $\log(1+e^t) = \log(1/\sigma(t))$.
    Donc, $\mathcal{H}(\eta, t) = \eta \log\left(\frac{1}{1-\sigma(t)}\right) + (1-\eta) \log\left(\frac{1}{\sigma(t)}\right)$
    $$ = -\eta \log(1-\sigma(t)) - (1-\eta) \log(\sigma(t))$$
    Le minimum de $\mathcal{H}(\eta, t)$ par rapport à $t$ est atteint à $t = f_{\phi}^*(x) = \log(\frac{\eta(x)}{1-\eta(x)})$, ce qui équivaut à $\sigma(f_{\phi}^*(x)) = \eta(x)$.
    Donc, $\mathcal{H}(\eta(x), f_{\phi}^*(x)) = -\eta(x) \log(1-\eta(x)) - (1-\eta(x)) \log(\eta(x))$.
    L'excès de risque logistique conditionnel est :
    $$\Delta_{\phi}(x, t) = \mathcal{H}(\eta(x), t) - \mathcal{H}(\eta(x), f_{\phi}^*(x))$$
    $$ = [-\eta(x) \log(1-\sigma(t)) - (1-\eta(x)) \log(\sigma(t))] - [-\eta(x) \log(1-\eta(x)) - (1-\eta(x)) \log(\eta(x))]$$
    $$ = \eta(x) \log\left(\frac{\eta(x)}{1-\sigma(t)}\right) + (1-\eta(x)) \log\left(\frac{1-\eta(x)}{\sigma(t)}\right)$$
    Ceci est précisément la définition de la divergence de Kullback-Leibler $D_{KL}(p||q)$ pour deux distributions de Bernoulli, $P = \text{Bernoulli}(\eta(x))$ et $Q = \text{Bernoulli}(\sigma(t))$, où $p=\eta(x)$ et $q=\sigma(t)$.
    Donc, $\Delta_{\phi}(x, t) = D_{KL}(\text{Bernoulli}(\eta(x)) || \text{Bernoulli}(\sigma(t)))$.

    b. Utiliser l'inégalité de Pinsker pour montrer que $(\eta(x) - \sigma(t))^2 \leq \frac{1}{2} \Delta_{\phi}(x, t)$.
    L'inégalité de Pinsker pour les distributions de Bernoulli $P=(p, 1-p)$ et $Q=(q, 1-q)$ s'écrit $D_{KL}(P||Q) \geq 2 (p-q)^2$. Attention, la forme standard de Pinsker est $D_{KL}(P||Q) \geq \frac{1}{2} (\text{TV}(P,Q))^2$, où $\text{TV}(P,Q) = |p-q|$. Donc $D_{KL}(P||Q) \geq \frac{1}{2} (p-q)^2$.
    En appliquant cette forme à $\Delta_{\phi}(x, t) = D_{KL}(\text{Bernoulli}(\eta(x)) || \text{Bernoulli}(\sigma(t)))$, avec $p=\eta(x)$ et $q=\sigma(t)$:
    $$\Delta_{\phi}(x, t) \geq \frac{1}{2} (\eta(x) - \sigma(t))^2$$
    En réarrangeant, nous obtenons :
    $$(\eta(x) - \sigma(t))^2 \leq 2 \Delta_{\phi}(x, t)$$
    D'où, $|\eta(x) - \sigma(t)| \leq \sqrt{2 \Delta_{\phi}(x, t)}$. Note : La constante de Pinsker est parfois donnée comme $\frac{1}{2 \ln 2}$ ou $1/2$. Pour rester simple, nous utiliserons $1/2$, ce qui donne $C_1=2$.

    c. Montrer que si $\text{sgn}(t) \neq h^*(x)$, alors $|\eta(x) - 1/2| \leq |\eta(x) - \sigma(t)|$.
    Nous savons que $h^*(x) = \text{sgn}(\eta(x) - 1/2)$.
    La fonction sigmoïde $\sigma(t) = 1/(1+e^{-t})$ est strictement croissante et $\sigma(0)=1/2$.
    De plus, $\eta(x) = \sigma(f_{\phi}^*(x))$.
    La condition $\text{sgn}(t) \neq h^*(x)$ signifie que $t$ et $f_{\phi}^*(x)$ ont des signes opposés, ou l'un est nul et l'autre non-nul.
    Par exemple, si $\eta(x) > 1/2$, alors $h^*(x)=1$ et $f_{\phi}^*(x)>0$. La condition $\text{sgn}(t) \neq h^*(x)$ implique $t \leq 0$.
    Dans ce cas, $\eta(x) > 1/2$ et $\sigma(t) \leq 1/2$.
    Ainsi, $\eta(x)$ et $\sigma(t)$ sont de part et d'autre de $1/2$.
    Ceci implique que $|\eta(x) - \sigma(t)| = |\eta(x) - 1/2| + |\sigma(t) - 1/2|$.
    Par conséquent, $|\eta(x) - \sigma(t)| \geq |\eta(x) - 1/2|$.
    Cette inégalité est valable si $\eta(x)$ et $\sigma(t)$ sont de part et d'autre de $1/2$.
    Si $\eta(x) = 1/2$, alors $h^*(x)=1$. Si $\text{sgn}(t) \neq h^*(x)$, alors $t \leq 0$. Alors $\sigma(t) \leq 1/2$.
    $|\eta(x) - 1/2| = 0$. Donc $0 \leq |\eta(x) - \sigma(t)|$ est toujours vrai.

    d. En déduire qu'il existe une constante $C > 0$ telle que, pour tout $x \in \mathcal{X}$ et pour tout $t \in \mathbb{R}$:
       $2|\eta(x) - 1/2| \mathbf{1}_{\text{sgn}(t) \neq h^*(x)} \leq C \sqrt{\Delta_{\phi}(x, t)}$.
    En utilisant les résultats des points (b) et (c) :
    Si $\text{sgn}(t) \neq h^*(x)$, nous avons :
    $$2|\eta(x) - 1/2| \leq 2|\eta(x) - \sigma(t)|$$
    Et du point (b) :
    $$|\eta(x) - \sigma(t)| \leq \sqrt{2 \Delta_{\phi}(x, t)}$$
    En combinant ces deux inégalités :
    $$2|\eta(x) - 1/2| \mathbf{1}_{\text{sgn}(t) \neq h^*(x)} \leq 2 \sqrt{2 \Delta_{\phi}(x, t)}$$
    Soit $C = 2\sqrt{2}$. Donc :
    $$2|\eta(x) - 1/2| \mathbf{1}_{\text{sgn}(t) \neq h^*(x)} \leq C \sqrt{\Delta_{\phi}(x, t)}$$

    e. En intégrant sur $X$, conclure à l'inégalité de Zhang : $R(h_f) - R^* \leq E_X[ C \sqrt{\Delta_{\phi}(X, f(X))} ]$. Expliquer pourquoi ce résultat est important pour la théorie de l'apprentissage statistique.
    Nous avons montré au point (3) de la Partie 1 que l'excès de risque 0-1 est :
    $$R(h_f) - R^* = E_X[ 2|\eta(X) - 1/2| \mathbf{1}_{h_f(X) \neq h^*(X)} ]$$
    En utilisant l'inégalité démontrée au point (d) pour $t=f(X)$, nous pouvons borner l'intégrande :
    $$2|\eta(X) - 1/2| \mathbf{1}_{h_f(X) \neq h^*(X)} \leq C \sqrt{\Delta_{\phi}(X, f(X))}$$
    En prenant l'espérance sur $X$ des deux côtés de l'inégalité :
    $$E_X[ 2|\eta(X) - 1/2| \mathbf{1}_{h_f(X) \neq h^*(X)} ] \leq E_X[ C \sqrt{\Delta_{\phi}(X, f(X))} ]$$
    Donc, nous obtenons l'inégalité de Zhang :
    $$R(h_f) - R^* \leq C E_X[ \sqrt{\Delta_{\phi}(X, f(X))} ]$$
    où $C = 2\sqrt{2}$. Notez que $\Delta_{\phi}(X, f(X)) = R_{\phi}(f) - R_{\phi}^*$ n'est pas tout à fait correct ici car $\Delta_{\phi}(X, f(X))$ est l'excès de risque logistique *conditionnel* pour un $X$ donné et une valeur $f(X)$ alors que $R_{\phi}(f) - R_{\phi}^*$ est l'excès de risque *total*. L'inégalité devrait être $R(h_f) - R^* \leq C E_X[ \sqrt{\mathcal{H}(\eta(X), f(X)) - \mathcal{H}(\eta(X), f_{\phi}^*(X))} ]$.
    Ce résultat est d'une importance capitale en théorie de l'apprentissage statistique. Il établit un lien quantitatif entre l'excès de risque d'une perte de substitution (ici la perte logistique) et l'excès de risque de la perte 0-1. Si un algorithme d'apprentissage est capable de minimiser l'excès de risque de la perte de substitution (c'est-à-dire que $R_{\phi}(f)$ se rapproche de $R_{\phi}^*$), alors cette inégalité garantit que l'excès de risque 0-1 du classifieur obtenu se rapproche également de zéro. En d'autres termes, elle fournit une justification théorique solide pour l'utilisation de pertes de substitution convexes et différentiables dans la pratique, en montrant qu'elles sont de "bons proxies" pour la perte 0-1 non-convexe et non-différentiable. Cela permet de développer des algorithmes d'optimisation efficaces pour la classification.
