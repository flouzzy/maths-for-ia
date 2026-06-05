---
uuid: jalon-140-exo-10
title: "Exercice 10 - Inégalité de Zhang et Surrogate Loss"
type: Exercice
difficulty: 5
---

# Exercice 10 - Inégalité de Zhang et Surrogate Loss

## Énoncé
Soit $(X, Y)$ un couple de variables aléatoires à valeurs dans $\mathcal{X} \times \{-1, 1\}$ suivant une distribution conjointe $\mathbb{P}$. Soit $\eta(x) = \mathbb{P}(Y=1 | X=x)$ la probabilité conditionnelle.
Considérons une fonction de perte de substitution (surrogate loss) $\phi : \mathbb{R} \to \mathbb{R}_+$. On définit le risque $\phi$-associé d'une fonction mesurable $f : \mathcal{X} \to \mathbb{R}$ par :
$$ R_\phi(f) = \mathbb{E}_{(X,Y) \sim \mathbb{P}}[\phi(Y f(X))] $$

Et le risque de classification (0-1) par :
$$ R(f) = \mathbb{E}_{(X,Y) \sim \mathbb{P}}[\mathbb{1}_{Y \neq \text{sign}(f(X))}] $$

Soit $R^*$ le risque de Bayes pour la classification 0-1, et $R_\phi^*$ l'infimum du risque $\phi$-associé sur l'ensemble de toutes les fonctions mesurables.
Montrez l'inégalité de Zhang pour la perte logistique $\phi(z) = \log_2(1 + \exp(-z))$, c'est-à-dire trouvez une relation rigoureuse entre l'excès de risque de classification $R(f) - R^*$ et l'excès de risque $\phi$-associé $R_\phi(f) - R_\phi^*$.

## Correction (Zéro Ellipse Mathématique)

### 1. Expression des risques conditionnels

Commençons par exprimer le risque $\phi$-associé conditionnellement à $X=x$. Le risque conditionnel est :
$$ C_\phi(f(x), x) = \mathbb{E}_{Y|X=x}[\phi(Y f(x))] $$
Puisque $Y \in \{-1, 1\}$ avec $\mathbb{P}(Y=1 | X=x) = \eta(x)$ et $\mathbb{P}(Y=-1 | X=x) = 1 - \eta(x)$, nous avons :
$$ C_\phi(f(x), x) = \eta(x) \phi(f(x)) + (1 - \eta(x)) \phi(-f(x)) $$

De même, le risque 0-1 conditionnel pour un classifieur de signe est :
$$ C(f(x), x) = \mathbb{E}_{Y|X=x}[\mathbb{1}_{Y \neq \text{sign}(f(x))}] = \eta(x) \mathbb{1}_{\text{sign}(f(x)) \neq 1} + (1 - \eta(x)) \mathbb{1}_{\text{sign}(f(x)) \neq -1} $$

Le risque de Bayes conditionnel optimal pour le risque 0-1 est obtenu par la règle de Bayes : on prédit $+1$ si $\eta(x) \ge 1/2$ et $-1$ sinon. Ainsi :
$$ C^*(x) = \min(\eta(x), 1 - \eta(x)) $$

L'excès de risque 0-1 conditionnel pour une prédiction $v = f(x)$ est donc :
$$ \Delta C(v, x) = C(v, x) - C^*(x) = |2\eta(x) - 1| \mathbb{1}_{\text{sign}(v) \neq \text{sign}(\eta(x) - 1/2)} $$

### 2. Infimum du risque $\phi$-associé conditionnel

Soit $H_\phi(\eta)$ l'infimum du risque conditionnel pour une probabilité $\eta \in [0, 1]$ :
$$ H_\phi(\eta) = \inf_{\alpha \in \mathbb{R}} (\eta \phi(\alpha) + (1-\eta) \phi(-\alpha)) $$

Pour la perte logistique $\phi(z) = \log_2(1 + \exp(-z))$ (souvent redimensionnée par $1/\ln(2)$, mais gardons le log base 2 ici pour correspondre à l'entropie binaire en bits), la fonction à minimiser par rapport à $\alpha$ est :
$$ J(\alpha) = \eta \log_2(1 + \exp(-\alpha)) + (1-\eta) \log_2(1 + \exp(\alpha)) $$

Calculons la dérivée par rapport à $\alpha$ pour trouver le minimum. Soit $\ln$ le logarithme népérien. On a $\log_2(u) = \frac{\ln(u)}{\ln(2)}$.
$$ \frac{\partial J(\alpha)}{\partial \alpha} = \frac{1}{\ln(2)} \left[ \eta \frac{-\exp(-\alpha)}{1+\exp(-\alpha)} + (1-\eta) \frac{\exp(\alpha)}{1+\exp(\alpha)} \right] $$
En multipliant par $\frac{1+\exp(\alpha)}{1+\exp(\alpha)}$ dans le premier terme, on remarque que $\frac{\exp(-\alpha)}{1+\exp(-\alpha)} = \frac{1}{1+\exp(\alpha)}$.
$$ \frac{\partial J(\alpha)}{\partial \alpha} = \frac{1}{\ln(2)} \left[ -\frac{\eta}{1+\exp(\alpha)} + \frac{(1-\eta)\exp(\alpha)}{1+\exp(\alpha)} \right] = \frac{1}{\ln(2) (1+\exp(\alpha))} [ -\eta + (1-\eta)\exp(\alpha) ] $$

En annulant la dérivée, on obtient :
$$ (1-\eta)\exp(\alpha) = \eta \implies \exp(\alpha) = \frac{\eta}{1-\eta} \implies \alpha^* = \ln\left(\frac{\eta}{1-\eta}\right) $$

En substituant $\alpha^*$ dans $H_\phi(\eta)$ :
$$ H_\phi(\eta) = \eta \log_2\left(1 + \frac{1-\eta}{\eta}\right) + (1-\eta) \log_2\left(1 + \frac{\eta}{1-\eta}\right) $$
$$ H_\phi(\eta) = \eta \log_2\left(\frac{1}{\eta}\right) + (1-\eta) \log_2\left(\frac{1}{1-\eta}\right) = -\eta \log_2(\eta) - (1-\eta) \log_2(1-\eta) $$
Ceci est exactement l'entropie binaire $h(\eta)$.

### 3. Relation de calibration (Transformée de Zhang)

L'excès de risque $\phi$-conditionnel pour une prédiction $v$ est :
$$ \Delta C_\phi(v, \eta) = \eta \phi(v) + (1-\eta) \phi(-v) - H_\phi(\eta) $$
Nous cherchons à minorer cet excès en fonction de l'excès de risque 0-1, $\Delta C(v, \eta) = |2\eta - 1| \mathbb{1}_{\text{sign}(v) \neq \text{sign}(\eta - 1/2)}$.

Considérons le cas où la prédiction a le mauvais signe, c'est-à-dire $v (\eta - 1/2) \le 0$. Par symétrie, supposons $\eta > 1/2$, donc $v \le 0$. L'excès de risque 0-1 conditionnel est alors $\theta = 2\eta - 1$.
Nous voulons minorer l'excès de risque $\phi$ conditionnel sur toutes les valeurs de $v \le 0$. Puisque $\phi$ est convexe et décroissante (pour la perte logistique), la fonction $\alpha \mapsto \eta \phi(\alpha) + (1-\eta) \phi(-\alpha)$ atteint son minimum sur $\alpha \le 0$ en $\alpha=0$.

Évaluons l'excès en $\alpha=0$ :
$$ \Delta C_\phi(0, \eta) = \eta \log_2(2) + (1-\eta) \log_2(2) - h(\eta) = 1 - h(\eta) $$

Nous voulons lier cet excès $1 - h(\eta)$ à l'excès de risque 0-1 qui est $|2\eta - 1|$. On note que $h(\eta)$ peut s'écrire en fonction de $\delta = \eta - 1/2$. On a $\eta = 1/2 + \delta$ et $1-\eta = 1/2 - \delta$.
Il est bien connu que pour l'entropie binaire, par le développement de Taylor ou l'inégalité de Pinsker :
$$ 1 - h(1/2 + \delta) \ge \frac{2}{\ln(2)} \delta^2 $$

Or, l'excès de risque 0-1 est $\Delta C(v, \eta) = |2\eta - 1| = 2|\delta|$. Ainsi, $\delta^2 = \frac{(\Delta C(v, \eta))^2}{4}$.
L'inégalité devient :
$$ \Delta C_\phi(v, \eta) \ge 1 - h(\eta) \ge \frac{2}{\ln(2)} \frac{(\Delta C(v, \eta))^2}{4} = \frac{1}{2 \ln(2)} (\Delta C(v, \eta))^2 $$

### 4. Intégration sur $\mathcal{X}$

Nous avons établi pour tout $x \in \mathcal{X}$ :
$$ \Delta C_\phi(f(x), \eta(x)) \ge \frac{1}{2 \ln(2)} (\Delta C(f(x), \eta(x)))^2 $$

Prenons l'espérance sur $X$ :
$$ \mathbb{E}_X [\Delta C_\phi(f(X), \eta(X))] \ge \mathbb{E}_X \left[ \frac{1}{2 \ln(2)} (\Delta C(f(X), \eta(X)))^2 \right] $$

Le membre de gauche est l'excès de risque global $\phi$-associé :
$$ \mathbb{E}_X [\Delta C_\phi(f(X), \eta(X))] = \mathbb{E}_X [C_\phi(f(X), X)] - \mathbb{E}_X [C_\phi^*(X)] = R_\phi(f) - R_\phi^* $$

Pour le membre de droite, par l'inégalité de Jensen (puisque la fonction $t \mapsto t^2$ est convexe), l'espérance du carré est minorée par le carré de l'espérance :
$$ \mathbb{E}_X \left[ (\Delta C(f(X), \eta(X)))^2 \right] \ge \left( \mathbb{E}_X [\Delta C(f(X), \eta(X))] \right)^2 $$

Et puisque l'espérance de l'excès de risque 0-1 conditionnel est l'excès de risque 0-1 global :
$$ \mathbb{E}_X [\Delta C(f(X), \eta(X))] = R(f) - R^* $$

Nous obtenons finalement :
$$ R_\phi(f) - R_\phi^* \ge \frac{1}{2 \ln(2)} (R(f) - R^*)^2 $$
Ce qui démontre rigoureusement l'inégalité de Zhang pour la perte logistique, reliant l'excès de risque de la perte de substitution à l'excès de risque de la classification binaire.
