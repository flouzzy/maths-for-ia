---
uuid: "jalon-140-exo-10"
title: "Exercice 10 - Jalon 140"
---
# Exercice 10 : Analyse du Classifieur de Bayes Optimal et de la Minimisation du Risque Exponentiel
**Difficulté:** ★★★★★

## Énoncé
Soit un problème de classification binaire où la variable de classe $Y$ prend ses valeurs dans $\{-1, 1\}$ et la variable d'entrée $X$ prend ses valeurs dans un espace $\mathcal{X}$. On note $\eta(x) = P(Y=1|X=x)$ la probabilité conditionnelle de la classe positive.

Le classifieur de Bayes optimal $h^*(x)$ est défini comme la règle de décision qui minimise le risque de classification $R(h) = E_X[P(Y \neq h(X)|X)]$. Son risque minimal est $R^*(h^*) = E_X[\min(\eta(X), 1-\eta(X))]$.

On considère la fonction de perte exponentielle (surrogate loss) définie par $L_{exp}(y, f(x)) = e^{-y f(x)}$, où $f: \mathcal{X} \to \mathbb{R}$ est une fonction de score. Le classifieur associé à une fonction de score $f$ est $h_f(x) = \text{sgn}(f(x))$.

1.  **Minimisation du Risque Conditionnel Exponentiel (★★★★)**
    Pour un $x \in \mathcal{X}$ fixé, on cherche la fonction de score $f^*(x)$ qui minimise le risque exponentiel conditionnel $R_{exp}(f|x) = E_Y[e^{-Y f(X)} | X=x]$.
    Démontrez que $f^*(x) = \frac{1}{2} \log \left( \frac{\eta(x)}{1-\eta(x)} \right)$.

2.  **Lien avec le Classifieur de Bayes (★★★★)**
    Montrez que le classifieur $h_{f^*}(x) = \text{sgn}(f^*(x))$ est équivalent au classifieur de Bayes optimal $h^*(x)$.

3.  **Analyse du Risque Exponentiel Minimal (★★★★★)**
    Soit $R_{exp}^* = E_X[R_{exp}(f^*|X)]$ le risque exponentiel minimal.
    Démontrez que $R_{exp}^* = E_X[2\sqrt{\eta(X)(1-\eta(X))}]$.

4.  **Borne Supérieure de l'Excès de Risque de Classification (★★★★★)**
    En utilisant les résultats précédents, et en considérant la relation entre le risque de classification $R(h_f) = E_X[P(Y \neq h_f(X)|X)]$ et le risque exponentiel $R_{exp}(f) = E_X[R_{exp}(f|X)]$, montrez qu'il existe une constante $C > 0$ telle que pour tout classifieur $h_f$ dérivé d'une fonction de score $f$, l'excès de risque de classification est borné par l'excès de risque exponentiel :
    $R(h_f) - R^*(h^*) \le C \cdot (R_{exp}(f) - R_{exp}^*)$.
    *Indication : Vous pourrez utiliser le fait que pour tout $x \in \mathcal{X}$ et pour toute fonction de score $f(x)$, l'excès de risque de classification conditionnel est borné par l'excès de risque exponentiel conditionnel de la manière suivante :*
    $P(Y \neq \text{sgn}(f(X))|X=x) - \min(\eta(X), 1-\eta(X)) \le \frac{1}{2} \left( \eta(X) e^{-f(X)} + (1-\eta(X)) e^{f(X)} - 2\sqrt{\eta(X)(1-\eta(X))} \right)$.
    *Vous n'avez pas à prouver cette inégalité, mais à l'utiliser pour dériver la borne globale.*

## Correction Pas-à-Pas

### Question 1 : Minimisation du Risque Conditionnel Exponentiel

Le risque exponentiel conditionnel pour un $x \in \mathcal{X}$ fixé est donné par :
$R_{exp}(f|x) = E_Y[e^{-Y f(X)} | X=x]$

Puisque $Y \in \{-1, 1\}$, on peut développer l'espérance :
$R_{exp}(f|x) = P(Y=1|X=x) \cdot e^{-1 \cdot f(x)} + P(Y=-1|X=x) \cdot e^{-(-1) \cdot f(x)}$
$R_{exp}(f|x) = \eta(x) e^{-f(x)} + (1-\eta(x)) e^{f(x)}$

Pour trouver la fonction de score $f^*(x)$ qui minimise ce risque, nous allons dériver $R_{exp}(f|x)$ par rapport à $f(x)$ et égaliser la dérivée à zéro.
Soit $g(f) = \eta(x) e^{-f} + (1-\eta(x)) e^{f}$.
La dérivée première par rapport à $f$ est :
$\frac{\partial g(f)}{\partial f} = \frac{\partial}{\partial f} (\eta(x) e^{-f}) + \frac{\partial}{\partial f} ((1-\eta(x)) e^{f})$
$\frac{\partial g(f)}{\partial f} = \eta(x) (-e^{-f}) + (1-\eta(x)) (e^{f})$
$\frac{\partial g(f)}{\partial f} = -\eta(x) e^{-f} + (1-\eta(x)) e^{f}$

Pour trouver le minimum, nous égalisons la dérivée à zéro :
$-\eta(x) e^{-f^*(x)} + (1-\eta(x)) e^{f^*(x)} = 0$
$(1-\eta(x)) e^{f^*(x)} = \eta(x) e^{-f^*(x)}$

Multiplions les deux côtés par $e^{f^*(x)}$ :
$(1-\eta(x)) e^{f^*(x)} e^{f^*(x)} = \eta(x) e^{-f^*(x)} e^{f^*(x)}$
$(1-\eta(x)) e^{2f^*(x)} = \eta(x) e^0$
$(1-\eta(x)) e^{2f^*(x)} = \eta(x)$

Divisons par $(1-\eta(x))$ :
$e^{2f^*(x)} = \frac{\eta(x)}{1-\eta(x)}$

Prenons le logarithme naturel des deux côtés :
$\ln(e^{2f^*(x)}) = \ln\left(\frac{\eta(x)}{1-\eta(x)}\right)$
$2f^*(x) = \ln\left(\frac{\eta(x)}{1-\eta(x)}\right)$

Enfin, divisons par 2 :
$f^*(x) = \frac{1}{2} \ln\left(\frac{\eta(x)}{1-\eta(x)}\right)$

Pour confirmer qu'il s'agit bien d'un minimum, nous pouvons calculer la dérivée seconde :
$\frac{\partial^2 g(f)}{\partial f^2} = \frac{\partial}{\partial f} (-\eta(x) e^{-f} + (1-\eta(x)) e^{f})$
$\frac{\partial^2 g(f)}{\partial f^2} = -\eta(x) (-e^{-f}) + (1-\eta(x)) (e^{f})$
$\frac{\partial^2 g(f)}{\partial f^2} = \eta(x) e^{-f} + (1-\eta(x)) e^{f}$
Puisque $\eta(x) \in [0,1]$ et $e^{-f}, e^f > 0$, la dérivée seconde est toujours positive. Cela confirme que $f^*(x)$ est bien un minimum global.

### Question 2 : Lien avec le Classifieur de Bayes

Le classifieur associé à $f^*(x)$ est $h_{f^*}(x) = \text{sgn}(f^*(x))$.
Nous avons $f^*(x) = \frac{1}{2} \ln\left(\frac{\eta(x)}{1-\eta(x)}\right)$.
Le signe de $f^*(x)$ est déterminé par le signe de $\ln\left(\frac{\eta(x)}{1-\eta(x)}\right)$.
Le logarithme naturel est positif si son argument est supérieur à 1, négatif si son argument est inférieur à 1, et nul si son argument est égal à 1.

Analysons les cas :
1.  Si $\eta(x) > 1-\eta(x)$ :
    Cela implique $2\eta(x) > 1$, soit $\eta(x) > 0.5$.
    Dans ce cas, $\frac{\eta(x)}{1-\eta(x)} > 1$, donc $\ln\left(\frac{\eta(x)}{1-\eta(x)}\right) > 0$.
    Par conséquent, $f^*(x) > 0$, et $h_{f^*}(x) = \text{sgn}(f^*(x)) = 1$.
    Le classifieur de Bayes optimal $h^*(x)$ est défini comme $h^*(x) = 1$ si $\eta(x) > 0.5$.
    Donc, $h_{f^*}(x) = h^*(x)$.

2.  Si $\eta(x) < 1-\eta(x)$ :
    Cela implique $2\eta(x) < 1$, soit $\eta(x) < 0.5$.
    Dans ce cas, $\frac{\eta(x)}{1-\eta(x)} < 1$, donc $\ln\left(\frac{\eta(x)}{1-\eta(x)}\right) < 0$.
    Par conséquent, $f^*(x) < 0$, et $h_{f^*}(x) = \text{sgn}(f^*(x)) = -1$.
    Le classifieur de Bayes optimal $h^*(x)$ est défini comme $h^*(x) = -1$ si $\eta(x) < 0.5$.
    Donc, $h_{f^*}(x) = h^*(x)$.

3.  Si $\eta(x) = 1-\eta(x)$ :
    Cela implique $2\eta(x) = 1$, soit $\eta(x) = 0.5$.
    Dans ce cas, $\frac{\eta(x)}{1-\eta(x)} = 1$, donc $\ln\left(\frac{\eta(x)}{1-\eta(x)}\right) = 0$.
    Par conséquent, $f^*(x) = 0$.
    Le classifieur de Bayes optimal $h^*(x)$ est généralement défini comme $1$ (ou $-1$) par convention lorsque $\eta(x) = 0.5$. Par exemple, $h^*(x) = \text{sgn}(\eta(x) - 0.5)$ donnerait $h^*(x)=0$ si $\eta(x)=0.5$, ce qui est une convention à gérer. Si l'on utilise la convention $h^*(x) = 1$ pour $\eta(x) \ge 0.5$, alors $h_{f^*}(x) = \text{sgn}(0)$ est souvent défini comme $1$ ou $-1$ selon la convention. Cependant, l'important est que le point de décision est le même.

Dans tous les cas, le signe de $f^*(x)$ est le même que le signe de $\eta(x) - 0.5$.
Par conséquent, le classifieur $h_{f^*}(x) = \text{sgn}(f^*(x))$ est équivalent au classifieur de Bayes optimal $h^*(x) = \text{sgn}(\eta(x) - 0.5)$.

### Question 3 : Analyse du Risque Exponentiel Minimal

Le risque exponentiel minimal conditionnel pour un $x$ fixé est $R_{exp}(f^*|x)$.
Nous substituons $f^*(x) = \frac{1}{2} \ln\left(\frac{\eta(x)}{1-\eta(x)}\right)$ dans l'expression de $R_{exp}(f|x)$ :
$R_{exp}(f^*|x) = \eta(x) e^{-f^*(x)} + (1-\eta(x)) e^{f^*(x)}$

Calculons $e^{f^*(x)}$ et $e^{-f^*(x)}$ :
$e^{f^*(x)} = e^{\frac{1}{2} \ln\left(\frac{\eta(x)}{1-\eta(x)}\right)} = \left(e^{\ln\left(\frac{\eta(x)}{1-\eta(x)}\right)}\right)^{1/2} = \left(\frac{\eta(x)}{1-\eta(x)}\right)^{1/2} = \sqrt{\frac{\eta(x)}{1-\eta(x)}}$
$e^{-f^*(x)} = e^{-\frac{1}{2} \ln\left(\frac{\eta(x)}{1-\eta(x)}\right)} = \left(e^{\ln\left(\frac{\eta(x)}{1-\eta(x)}\right)}\right)^{-1/2} = \left(\frac{\eta(x)}{1-\eta(x)}\right)^{-1/2} = \sqrt{\frac{1-\eta(x)}{\eta(x)}}$

Maintenant, substituons ces expressions dans $R_{exp}(f^*|x)$ :
$R_{exp}(f^*|x) = \eta(x) \sqrt{\frac{1-\eta(x)}{\eta(x)}} + (1-\eta(x)) \sqrt{\frac{\eta(x)}{1-\eta(x)}}$
$R_{exp}(f^*|x) = \frac{\eta(x) \sqrt{1-\eta(x)}}{\sqrt{\eta(x)}} + \frac{(1-\eta(x)) \sqrt{\eta(x)}}{\sqrt{1-\eta(x)}}$
$R_{exp}(f^*|x) = \sqrt{\eta(x)} \sqrt{1-\eta(x)} + \sqrt{1-\eta(x)} \sqrt{\eta(x)}$
$R_{exp}(f^*|x) = \sqrt{\eta(x)(1-\eta(x))} + \sqrt{\eta(x)(1-\eta(x))}$
$R_{exp}(f^*|x) = 2\sqrt{\eta(x)(1-\eta(x))}$

Le risque exponentiel minimal total $R_{exp}^*$ est l'espérance de ce risque conditionnel sur $X$ :
$R_{exp}^* = E_X[R_{exp}(f^*|X)]$
$R_{exp}^* = E_X[2\sqrt{\eta(X)(1-\eta(X))}]$

### Question 4 : Borne Supérieure de l'Excès de Risque de Classification

Nous voulons montrer que $R(h_f) - R^*(h^*) \le C \cdot (R_{exp}(f) - R_{exp}^*)$ pour une constante $C > 0$.

Nous avons l'inégalité donnée en indication :
$P(Y \neq \text{sgn}(f(X))|X=x) - \min(\eta(X), 1-\eta(X)) \le \frac{1}{2} \left( \eta(X) e^{-f(X)} + (1-\eta(X)) e^{f(X)} - 2\sqrt{\eta(X)(1-\eta(X))} \right)$

Définissons les termes pour plus de clarté :
*   Le terme de gauche est l'excès de risque de classification conditionnel en $x$ :
    $E_{class}(f|x) = P(Y \neq h_f(X)|X=x) - \min(\eta(X), 1-\eta(X))$
*   Le terme de droite est $\frac{1}{2}$ fois l'excès de risque exponentiel conditionnel en $x$ :
    $E_{exp}(f|x) = \eta(X) e^{-f(X)} + (1-\eta(X)) e^{f(X)} - 2\sqrt{\eta(X)(1-\eta(X))}$
    Nous savons d'après la Question 1 et la Question 3 que $R_{exp}(f|x) = \eta(X) e^{-f(X)} + (1-\eta(X)) e^{f(X)}$ et $R_{exp}(f^*|x) = 2\sqrt{\eta(X)(1-\eta(X))}$.
    Donc, $E_{exp}(f|x) = R_{exp}(f|x) - R_{exp}(f^*|x)$.

L'inégalité donnée peut donc s'écrire :
$E_{class}(f|x) \le \frac{1}{2} (R_{exp}(f|x) - R_{exp}(f^*|x))$

Pour obtenir la borne globale, nous prenons l'espérance des deux côtés de cette inégalité par rapport à $X$.
$E_X[E_{class}(f|X)] \le E_X\left[\frac{1}{2} (R_{exp}(f|X) - R_{exp}(f^*|X))\right]$

Développons le terme de gauche :
$E_X[E_{class}(f|X)] = E_X[P(Y \neq h_f(X)|X)] - E_X[\min(\eta(X), 1-\eta(X))]$
$E_X[E_{class}(f|X)] = R(h_f) - R^*(h^*)$

Développons le terme de droite :
$E_X\left[\frac{1}{2} (R_{exp}(f|X) - R_{exp}(f^*|X))\right] = \frac{1}{2} E_X[R_{exp}(f|X) - R_{exp}(f^*|X)]$
$E_X\left[\frac{1}{2} (R_{exp}(f|X) - R_{exp}(f^*|X))\right] = \frac{1}{2} (E_X[R_{exp}(f|X)] - E_X[R_{exp}(f^*|X)])$
$E_X\left[\frac{1}{2} (R_{exp}(f|X) - R_{exp}(f^*|X))\right] = \frac{1}{2} (R_{exp}(f) - R_{exp}^*)$

En combinant les deux côtés, nous obtenons :
$R(h_f) - R^*(h^*) \le \frac{1}{2} (R_{exp}(f) - R_{exp}^*)$

Cette inégalité montre que l'excès de risque de classification est borné par la moitié de l'excès de risque exponentiel.
Nous pouvons donc identifier la constante $C = \frac{1}{2}$.
Puisque $C = \frac{1}{2} > 0$, la condition est satisfaite.

Conclusion : Il existe une constante $C = \frac{1}{2}$ telle que pour tout classifieur $h_f$ dérivé d'une fonction de score $f$, l'excès de risque de classification est borné par l'excès de risque exponentiel :
$R(h_f) - R^*(h^*) \le \frac{1}{2} (R_{exp}(f) - R_{exp}^*)$
