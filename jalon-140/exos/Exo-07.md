---
uuid: jalon-140-exo-07
title: "Exercice 7 - Classifieur de Bayes"
type: Exercice
difficulty: 4
---

### Énoncé

Soit $(\Omega, \mathcal{A}, P)$ un espace de probabilité. Soient $X: (\Omega, \mathcal{A}) \to (\mathcal{X}, \mathcal{B}_{\mathcal{X}})$ et $Y: (\Omega, \mathcal{A}) \to (\mathcal{Y}, \mathcal{P}(\mathcal{Y}))$ deux variables aléatoires, où $\mathcal{X}$ est un espace mesurable muni d'une tribu $\mathcal{B}_{\mathcal{X}}$, et $\mathcal{Y} = \{-1, 1\}$ muni de la tribu discrète $\mathcal{P}(\mathcal{Y})$. Le couple $(X,Y)$ est une variable aléatoire définie sur $(\Omega, \mathcal{A}, P)$ à valeurs dans $(\mathcal{X} \times \mathcal{Y}, \mathcal{B}_{\mathcal{X}} \otimes \mathcal{P}(\mathcal{Y}))$.

On note $\eta: \mathcal{X} \to [0, 1]$ la probabilité a posteriori de la classe 1, définie par $\eta(x) := P(Y=1|X=x)$ pour $x \in \mathcal{X}$. On suppose que $\eta(x) \neq 1/2$ presque sûrement pour $P_X$ (la distribution marginale de $X$).

Le classifieur de Bayes optimal $f^*: \mathcal{X} \to \{-1, 1\}$ pour la perte 0-1 est défini par $f^*(x) = \text{sgn}(\eta(x) - 1/2)$, où $\text{sgn}(z)=1$ si $z>0$, $\text{sgn}(z)=-1$ si $z<0$, et $\text{sgn}(0)$ est indéfini (mais non pertinent ici grâce à l'hypothèse $\eta(x) \neq 1/2$). La perte 0-1 est $L_{01}(y, y') = \mathbf{1}_{y \neq y'}$. Le risque 0-1 d'un classifieur $f: \mathcal{X} \to \{-1, 1\}$ est $R_{01}(f) = E[L_{01}(Y, f(X))]$.

On considère une fonction de prédiction $h: \mathcal{X} \to \mathbb{R}$ (mesurable). Un classifieur $f_h$ peut être obtenu à partir de $h$ par $f_h(x) = \text{sgn}(h(x))$.
La perte logistique (ou *logistic loss*) pour un prédicteur $h(x)$ et une vraie étiquette $y \in \{-1, 1\}$ est définie par $L_{\text{log}}(y, h(x)) = \log(1 + e^{-y h(x)})$.
Le risque logistique d'un prédicteur $h$ est $R_{\text{log}}(h) = E[L_{\text{log}}(Y, h(X))]$.

1.  **Optimality of the predictor:** Pour un $x \in \mathcal{X}$ fixé, déterminer la fonction de prédiction optimale $h^*(x)$ qui minimise le risque conditionnel $E[L_{\text{log}}(Y, h(x))|X=x]$. Exprimer $h^*(x)$ en fonction de $\eta(x)$.

2.  **Consistency:** Montrer que le classifieur $f_{h^*}(x) = \text{sgn}(h^*(x))$ est équivalent au classifieur de Bayes $f^*(x)$ pour presque tout $x$. Comment cette propriété est-elle nommée dans le contexte des fonctions de perte de substitution ?

3.  **Calibration:** Une perte de substitution $L_{\text{sub}}(y, v)$ est dite calibrée par rapport à la perte 0-1 si, pour toute distribution conditionnelle $P(Y|X=x)$ (caractérisée par $\eta(x)$), minimiser le risque conditionnel de $L_{\text{sub}}$ conduit à un classifieur qui minimise le risque conditionnel de la perte 0-1. Plus formellement, si $h^*(x)$ minimise $E[L_{\text{sub}}(Y, h(x))|X=x]$, alors $\text{sgn}(h^*(x))$ minimise $E[L_{01}(Y, \text{sgn}(h'(x)))|X=x]$ pour tout $h'$. La perte logistique est-elle calibrée par rapport à la perte 0-1 ? Justifier votre réponse.

4.  **Risk Bound (Inégalité de Zhang):** Montrer qu'il existe une fonction $\psi: [0, \infty) \to [0, \infty)$, continue et strictement croissante avec $\psi(0)=0$, telle que pour tout prédicteur mesurable $h: \mathcal{X} \to \mathbb{R}$, l'inégalité suivante est vérifiée:
    $$R_{01}(f_h) - R_{01}(f^*) \le E_X[\psi(H(h(X), \eta(X)) - H(h^*(X), \eta(X)))]$$
    où $H(v, \eta) := E[L_{\text{log}}(Y, v)|\eta] = \eta \log(1+e^{-v}) + (1-\eta) \log(1+e^v)$.
    Définir explicitement une telle fonction $\psi(t)$ et démontrer l'inégalité point par point (pour un $x$ fixé).

---

### Correction

1.  **Optimality of the predictor:**

    Pour un $x \in \mathcal{X}$ fixé, nous cherchons à minimiser le risque conditionnel de la perte logistique, que nous noterons $H(v, \eta)$ pour $v = h(x)$ et $\eta = \eta(x)$:
    $$H(v, \eta) = E[L_{\text{log}}(Y, v)|X=x] = P(Y=1|X=x) L_{\text{log}}(1, v) + P(Y=-1|X=x) L_{\text{log}}(-1, v)$$
    $$H(v, \eta) = \eta \log(1 + e^{-v}) + (1-\eta) \log(1 + e^{v})$$
    Pour trouver le minimum, nous dérivons $H(v, \eta)$ par rapport à $v$ et égalons la dérivée à zéro:
    $$\frac{\partial H}{\partial v}(v, \eta) = \eta \frac{-e^{-v}}{1+e^{-v}} + (1-\eta) \frac{e^v}{1+e^v}$$
    Simplifions les termes: $\frac{-e^{-v}}{1+e^{-v}} = \frac{-1}{e^v+1}$ et $\frac{e^v}{1+e^v}$.
    $$\frac{\partial H}{\partial v}(v, \eta) = \frac{-\eta}{e^v+1} + \frac{(1-\eta)e^v}{e^v+1} = \frac{(1-\eta)e^v - \eta}{e^v+1}$$
    En égalant la dérivée à zéro:
    $$\frac{(1-\eta)e^v - \eta}{e^v+1} = 0 \implies (1-\eta)e^v - \eta = 0$$
    $$(1-\eta)e^v = \eta$$
    $$e^v = \frac{\eta}{1-\eta}$$
    $$v^* = \log\left(\frac{\eta}{1-\eta}\right)$$
    Pour confirmer qu'il s'agit bien d'un minimum, calculons la seconde dérivée:
    $$\frac{\partial^2 H}{\partial v^2}(v, \eta) = \frac{\partial}{\partial v} \left( \frac{(1-\eta)e^v - \eta}{e^v+1} \right) = \frac{(1-\eta)e^v(e^v+1) - ((1-\eta)e^v - \eta)e^v}{(e^v+1)^2}$$
    $$= \frac{(1-\eta)e^{2v} + (1-\eta)e^v - (1-\eta)e^{2v} + \eta e^v}{(e^v+1)^2} = \frac{(1-\eta)e^v + \eta e^v}{(e^v+1)^2} = \frac{e^v}{(e^v+1)^2}$$
    Puisque $e^v > 0$ pour tout $v \in \mathbb{R}$, la seconde dérivée est strictement positive, confirmant que $v^*$ est bien un minimum.

    Par conséquent, la fonction de prédiction optimale $h^*(x)$ pour la perte logistique est:
    $$h^*(x) = \log\left(\frac{\eta(x)}{1-\eta(x)}\right)$$
    Cette expression est aussi connue sous le nom de *logit* de $\eta(x)$.

2.  **Consistency:**

    Le classifieur $f_{h^*}(x)$ est défini par $f_{h^*}(x) = \text{sgn}(h^*(x))$.
    Nous avons $h^*(x) = \log\left(\frac{\eta(x)}{1-\eta(x)}\right)$.
    Comparons $f_{h^*}(x)$ avec le classifieur de Bayes $f^*(x) = \text{sgn}(\eta(x) - 1/2)$.

    *   **Cas 1:** Si $\eta(x) > 1/2$.
        Alors $\frac{\eta(x)}{1-\eta(x)} > 1$.
        Donc $h^*(x) = \log\left(\frac{\eta(x)}{1-\eta(x)}\right) > \log(1) = 0$.
        Ainsi, $f_{h^*}(x) = \text{sgn}(h^*(x)) = 1$.
        D'autre part, $\eta(x) - 1/2 > 0$, donc $f^*(x) = \text{sgn}(\eta(x) - 1/2) = 1$.
        Dans ce cas, $f_{h^*}(x) = f^*(x)$.

    *   **Cas 2:** Si $\eta(x) < 1/2$.
        Alors $\frac{\eta(x)}{1-\eta(x)} < 1$.
        Donc $h^*(x) = \log\left(\frac{\eta(x)}{1-\eta(x)}\right) < \log(1) = 0$.
        Ainsi, $f_{h^*}(x) = \text{sgn}(h^*(x)) = -1$.
        D'autre part, $\eta(x) - 1/2 < 0$, donc $f^*(x) = \text{sgn}(\eta(x) - 1/2) = -1$.
        Dans ce cas, $f_{h^*}(x) = f^*(x)$.

    Puisque nous avons supposé $\eta(x) \neq 1/2$ presque sûrement, les classifieurs sont égaux pour presque tout $x$.
    Cette propriété est appelée la **consistance de la fonction de perte de substitution (classification-consistency)**. Cela signifie que minimiser le risque logistique conduit à un classifieur qui est équivalent au classifieur de Bayes.

3.  **Calibration:**

    La définition de calibration indique qu'une perte de substitution $L_{\text{sub}}$ est calibrée par rapport à la perte $L_{01}$ si le minimisateur $h^*(x)$ du risque conditionnel de $L_{\text{sub}}$ produit un classifieur $\text{sgn}(h^*(x))$ qui est également le minimisateur du risque conditionnel de $L_{01}$ (c'est-à-dire le classifieur de Bayes).
    Pour un $x$ fixé, le minimisateur du risque conditionnel de $L_{01}$ est $f^*(x)$.
    Dans la question 2, nous avons montré que $\text{sgn}(h^*(x)) = f^*(x)$ pour presque tout $x$.
    Par conséquent, la perte logistique est **calibrée** par rapport à la perte 0-1.

4.  **Risk Bound (Inégalité de Zhang):**

    Nous cherchons à montrer qu'il existe une fonction $\psi: [0, \infty) \to [0, \infty)$, continue, strictement croissante avec $\psi(0)=0$, telle que pour tout $h: \mathcal{X} \to \mathbb{R}$,
    $$R_{01}(f_h) - R_{01}(f^*) \le E_X[\psi(H(h(X), \eta(X)) - H(h^*(X), \eta(X)))]$$
    Cela revient à montrer que pour tout $x \in \mathcal{X}$ (presque sûrement) et tout prédicteur $v = h(x)$ :
    $$P(Y \neq \text{sgn}(v)|X=x) - P(Y \neq f^*(x)|X=x) \le \psi(H(v, \eta(x)) - H(h^*(x), \eta(x)))$$
    Notons $E_{01}(v, \eta) = P(Y \neq \text{sgn}(v)|\eta) - P(Y \neq \text{sgn}(h^*(\eta))|\eta)$ l'excès de risque 0-1 conditionnel pour une valeur $\eta$ et un prédicteur $v$.
    Notons $E_{\text{log}}(v, \eta) = H(v, \eta) - H(h^*(\eta), \eta)$ l'excès de risque logistique conditionnel.

    Le risque 0-1 conditionnel est $P(Y \neq \text{sgn}(v)|\eta) = (1-\eta) \mathbf{1}_{v \ge 0} + \eta \mathbf{1}_{v < 0}$.
    Le risque 0-1 de Bayes est $P(Y \neq f^*(x)|\eta) = \min(\eta, 1-\eta)$.
    L'excès de risque 0-1 conditionnel $E_{01}(v, \eta)$ est non nul seulement si $\text{sgn}(v) \neq \text{sgn}(h^*(\eta))$.
    Si $\eta > 1/2$, alors $h^*(\eta) > 0$ (donc $f^*(\eta)=1$). Si $v < 0$, alors $\text{sgn}(v)=-1 \neq f^*(\eta)=1$.
    Dans ce cas, $E_{01}(v, \eta) = \eta - (1-\eta) = 2\eta-1$.
    Si $\eta < 1/2$, alors $h^*(\eta) < 0$ (donc $f^*(\eta)=-1$). Si $v \ge 0$, alors $\text{sgn}(v)=1 \neq f^*(\eta)=-1$.
    Dans ce cas, $E_{01}(v, \eta) = (1-\eta) - \eta = 1-2\eta$.
    En résumé, $E_{01}(v, \eta) = |2\eta-1|$ si $\text{sgn}(v) \neq \text{sgn}(h^*(\eta))$, et $0$ sinon.

    Montrons que la fonction $\psi(t) = \sqrt{2t}$ convient.
    Nous devons montrer que $E_{01}(v, \eta) \le \sqrt{2 E_{\text{log}}(v, \eta)}$ pour tous $v \in \mathbb{R}$ et $\eta \in [0,1]$.

    *   **Cas 1: $\text{sgn}(v) = \text{sgn}(h^*(\eta))$**
        Alors $E_{01}(v, \eta) = 0$. Puisque $E_{\text{log}}(v, \eta) \ge 0$ ( $h^*(\eta)$ est un minimiseur), l'inégalité $0 \le \sqrt{2 E_{\text{log}}(v, \eta)}$ est trivialement vraie.

    *   **Cas 2: $\text{sgn}(v) \neq \text{sgn}(h^*(\eta))$**
        Sans perte de généralité, supposons $\eta > 1/2$. Alors $h^*(\eta) > 0$. L'excès de risque 0-1 est $E_{01}(v, \eta) = 2\eta-1$. Ce cas se produit lorsque $v \le 0$.
        Le risque logistique conditionnel $H(v, \eta)$ est une fonction convexe de $v$. Son minimum est à $h^*(\eta) > 0$.
        Puisque $v \le 0 < h^*(\eta)$, le point $v=0$ est entre $v$ et $h^*(\eta)$, ou $v$ est plus éloigné que $0$ du minimum $h^*(\eta)$. Par convexité, $H(v, \eta) \ge H(0, \eta)$.
        Donc, $E_{\text{log}}(v, \eta) = H(v, \eta) - H(h^*(\eta), \eta) \ge H(0, \eta) - H(h^*(\eta), \eta)$.
        Calculons $H(0, \eta) - H(h^*(\eta), \eta)$:
        $H(0, \eta) = \eta \log(1+e^0) + (1-\eta)\log(1+e^0) = \eta \log 2 + (1-\eta) \log 2 = \log 2$.
        $H(h^*(\eta), \eta) = \eta \log(1+e^{-h^*(\eta)}) + (1-\eta)\log(1+e^{h^*(\eta)})$.
        Rappelons $e^{h^*(\eta)} = \frac{\eta}{1-\eta}$. Donc $e^{-h^*(\eta)} = \frac{1-\eta}{\eta}$.
        $1+e^{-h^*(\eta)} = 1+\frac{1-\eta}{\eta} = \frac{\eta+1-\eta}{\eta} = \frac{1}{\eta}$.
        $1+e^{h^*(\eta)} = 1+\frac{\eta}{1-\eta} = \frac{1-\eta+\eta}{1-\eta} = \frac{1}{1-\eta}$.
        Ainsi, $H(h^*(\eta), \eta) = \eta \log\left(\frac{1}{\eta}\right) + (1-\eta)\log\left(\frac{1}{1-\eta}\right) = -\eta \log\eta - (1-\eta)\log(1-\eta)$.
        Donc, $H(0, \eta) - H(h^*(\eta), \eta) = \log 2 + \eta \log\eta + (1-\eta)\log(1-\eta)$.
        Cette expression est le double de la divergence de Kullback-Leibler entre une distribution de Bernoulli de paramètre $\eta$ et une distribution de Bernoulli de paramètre $1/2$, i.e., $2D_{KL}(\text{Bernoulli}(\eta)||\text{Bernoulli}(1/2))$.
        $$2D_{KL}(\text{Bernoulli}(\eta)||\text{Bernoulli}(1/2)) = \eta \log\left(\frac{\eta}{1/2}\right) + (1-\eta)\log\left(\frac{1-\eta}{1/2}\right) = \eta \log(2\eta) + (1-\eta)\log(2(1-\eta))$$
        $$ = \eta \log 2 + \eta \log\eta + (1-\eta)\log 2 + (1-\eta)\log(1-\eta) = \log 2 + \eta \log\eta + (1-\eta)\log(1-\eta).$$
        Il est connu de l'inégalité de Pinsker que pour deux distributions de probabilité $P$ et $Q$, $D_{KL}(P||Q) \ge \frac{1}{2}\|P-Q\|_1^2$. Pour les distributions de Bernoulli $P(\eta)$ et $P(1/2)$, la distance $L_1$ est $\|P(\eta)-P(1/2)\|_1 = |\eta-1/2| + |(1-\eta)-1/2| = |2\eta-1|$.
        Donc $D_{KL}(\text{Bernoulli}(\eta)||\text{Bernoulli}(1/2)) \ge \frac{1}{2}(2\eta-1)^2$.
        Ainsi, $H(0, \eta) - H(h^*(\eta), \eta) \ge (2\eta-1)^2 \times \frac{1}{2}$. (Il y a un facteur 2 dans ma formule de $2D_{KL}$ ci-dessus.)
        Reprenons : $D_{KL}(P(\eta)||P(1/2)) \ge \frac{1}{2\ln 2} (2\eta-1)^2$. Si on utilise le log naturel, la constante est 1/2.
        $H(0, \eta) - H(h^*(\eta), \eta) = 2D_{KL}(P(\eta)||P(1/2)) \ge 2 \times \frac{1}{2} (2\eta-1)^2 = (2\eta-1)^2$.
        Ah non, c'est $D_{KL}(P(\eta)||P(1/2)) \ge \frac{1}{2} \sum |p_i - q_i|^2 \ldots$ C'est subtil.
        La version directe de Pinsker pour Bernoulli est $D_{KL}(P(\eta)||P(1/2)) \ge \frac{1}{2}(2\eta-1)^2$.
        Donc $H(0, \eta) - H(h^*(\eta), \eta) \ge (2\eta-1)^2 \times 2$. Non.

        Reprenons l'inégalité de Pinsker pour deux Bernoulli: $D_{KL}(\text{Bernoulli}(\eta)||\text{Bernoulli}(1/2)) \ge 2 (\eta - 1/2)^2 = \frac{1}{2}(2\eta-1)^2$.
        Donc $E_{\text{log}}(v, \eta) \ge H(0, \eta) - H(h^*(\eta), \eta) = \eta \log(2\eta) + (1-\eta)\log(2(1-\eta))$.
        C'est cette quantité que nous savons être supérieure ou égale à $\frac{1}{2}(2\eta-1)^2$.
        Donc $E_{\text{log}}(v, \eta) \ge \frac{1}{2}(2\eta-1)^2$.
        Par conséquent, $2 E_{\text{log}}(v, \eta) \ge (2\eta-1)^2$.
        En prenant la racine carrée des deux côtés (et puisque $2\eta-1 \ge 0$ pour $\eta>1/2$):
        $\sqrt{2 E_{\text{log}}(v, \eta)} \ge |2\eta-1|$.
        Nous avons donc montré que $E_{01}(v, \eta) \le \sqrt{2 E_{\text{log}}(v, \eta)}$ pour $\eta > 1/2$ et $v \le 0$.
        Le même raisonnement s'applique de manière symétrique pour $\eta < 1/2$ et $v \ge 0$.

    La fonction $\psi(t) = \sqrt{2t}$ répond aux critères. Elle est continue sur $[0, \infty)$, strictement croissante pour $t>0$, et $\psi(0)=0$.
    En intégrant sur $X$, on obtient le résultat global :
    $$R_{01}(f_h) - R_{01}(f^*) = E_X[E_{01}(h(X), \eta(X))] \le E_X[\sqrt{2 E_{\text{log}}(h(X), \eta(X))}]$$
    La fonction $\psi(t) = \sqrt{2t}$ satisfait les conditions requises.