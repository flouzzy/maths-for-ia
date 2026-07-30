---
uuid: "jalon-40"
title: "Intégrales dépendant d'un paramètre"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/calcul-differentiel
prev: "[[Jalon 39 (Intégrales généralisées sur un intervalle quelconque et critères de convergence.).md]]"
next: "[[Jalon 41 (Équations différentielles linéaires du premier ordre et méthode de variation de la constante.).md]]"
---

# Jalon 40 : Intégrales dépendant d'un paramètre

## 1. Origine et intuition géométrique

L'intégration classique permet de sommer de façon continue les valeurs d'une fonction $f(t)$ sur un intervalle $I$. Cependant, dans de nombreux problèmes physiques et probabilistes, la fonction que l'on intègre dépend également d'une variable externe $x$, appelée *paramètre*. L'intégrale définit alors une nouvelle fonction :
$$ F(x) = \int_I f(x,t) \, \mathrm{d}t $$

Géométriquement, considérons une surface $z = f(x,t)$ dans l'espace $\mathbb{R}^3$. Pour un $x_0$ fixé, la fonction $t \mapsto f(x_0, t)$ représente une courbe plane, intersection de la surface avec le plan d'équation $x = x_0$. L'intégrale $F(x_0)$ correspond à l'aire algébrique sous cette courbe. Faire varier le paramètre $x$ revient à translater ce plan d'intersection, et $F(x)$ mesure la variation continue de cette aire.

Historiquement, de nombreuses fonctions spéciales (comme la fonction Gamma d'Euler) ne peuvent s'exprimer par des combinaisons élémentaires, mais apparaissent naturellement sous forme d'intégrales dépendant d'un paramètre. L'enjeu analytique central est de déterminer sous quelles conditions on peut dériver ou intégrer $F(x)$ en intervertissant l'ordre des opérations limite et intégrale :
$$ \frac{\mathrm{d}}{\mathrm{d}x} \int_I f(x,t) \, \mathrm{d}t \overset{?}{=} \int_I \frac{\partial f}{\partial x}(x,t) \, \mathrm{d}t $$
Ces théorèmes d'interversion, initiés par Leibniz, nécessitent des hypothèses strictes de régularité (continuité) et de contrôle du comportement asymptotique (domination), afin d'éviter les singularités où l'aire divergerait brutalement.

## 2. Théorèmes fondamentaux sur un intervalle quelconque

Soit $I$ un intervalle de $\mathbb{R}$ (éventuellement non borné, par exemple $[a, +\infty[$) et $A$ une partie de $\mathbb{R}$ ou $\mathbb{C}$ (souvent un intervalle d'étude pour le paramètre).
Soit $f : A \times I \to \mathbb{C}$ (ou $\mathbb{R}$) une fonction. L'intégrale à paramètre étudiée est :
$$ F(x) = \int_I f(x,t) \, \mathrm{d}t \quad \text{pour } x \in A $$

### A. Continuité sous le signe intégral

> **Théorème de continuité (Théorème de convergence dominée paramétrique)**
> Soit $f : A \times I \to \mathbb{C}$ vérifiant :
> 1. Pour tout $t \in I$, l'application $x \mapsto f(x,t)$ est continue sur $A$.
> 2. Pour tout $x \in A$, l'application $t \mapsto f(x,t)$ est continue par morceaux sur $I$.
> 3. (Hypothèse de domination) Il existe une fonction $\varphi : I \to \mathbb{R}_+$ intégrable sur $I$ (indépendante de $x$) telle que :
>    $$ \forall (x,t) \in A \times I, \quad |f(x,t)| \leq \varphi(t) $$
> Alors $F : A \to \mathbb{C}$ est continue sur $A$.

**Exemple d'application immédiate : La transformée de Laplace**
Considérons $F(x) = \int_0^{+\infty} e^{-xt} \frac{\sin(t)}{t} \, \mathrm{d}t$ pour $x \in A = ]0, +\infty[$.
Soit $[a, +\infty[$ un intervalle fermé dans $A$ avec $a > 0$. Posons $f(x,t) = e^{-xt} \frac{\sin(t)}{t}$.
- Pour $t > 0$ fixé, $x \mapsto e^{-xt} \frac{\sin(t)}{t}$ est continue sur $[a, +\infty[$.
- Pour $x \geq a$ fixé, $t \mapsto e^{-xt} \frac{\sin(t)}{t}$ est continue sur $]0, +\infty[$ (prolongeable par continuité en $0$).
- Domination : $\forall (x,t) \in [a, +\infty[ \times ]0, +\infty[, \quad |f(x,t)| \leq e^{-at}$.
La fonction $\varphi(t) = e^{-at}$ est intégrable sur $]0, +\infty[$ car $a > 0$.
Donc $F$ est continue sur tout intervalle $[a, +\infty[$, et donc sur $]0, +\infty[$.

### B. Dérivation sous le signe intégral (Règle de Leibniz)

> **Théorème de dérivation (Classe $\mathcal{C}^1$)**
> Soit $I$ un intervalle de $\mathbb{R}$ et $A$ un intervalle ouvert de $\mathbb{R}$. Soit $f : A \times I \to \mathbb{C}$ vérifiant :
> 1. Pour tout $t \in I$, la fonction $x \mapsto f(x,t)$ est dérivable sur $A$, et $\frac{\partial f}{\partial x}$ est définie sur $A \times I$.
> 2. Pour tout $x \in A$, les fonctions $t \mapsto f(x,t)$ et $t \mapsto \frac{\partial f}{\partial x}(x,t)$ sont continues par morceaux sur $I$.
> 3. (Hypothèse d'intégrabilité) Il existe $x_0 \in A$ tel que $t \mapsto f(x_0, t)$ est intégrable sur $I$.
> 4. (Hypothèse de domination de la dérivée) Il existe une fonction $\psi : I \to \mathbb{R}_+$ intégrable sur $I$ telle que :
>    $$ \forall (x,t) \in A \times I, \quad \left| \frac{\partial f}{\partial x}(x,t) \right| \leq \psi(t) $$
> Alors $F(x) = \int_I f(x,t) \, \mathrm{d}t$ est bien définie pour tout $x \in A$, elle est de classe $\mathcal{C}^1$ sur $A$, et :
> $$ F'(x) = \int_I \frac{\partial f}{\partial x}(x,t) \, \mathrm{d}t $$

### C. Cas des segments d'intégration finis (Généralisation faible)

Si $I = [a,b]$ est un segment fini, toute fonction continue sur $A \times [a,b]$ satisfait l'hypothèse de domination localement, puisque toute fonction continue sur un compact y est bornée. Les théorèmes s'appliquent donc systématiquement sans avoir besoin de rechercher activement une fonction de domination complexe pour des domaines locaux.

## 3. Démonstration rigoureuse : La règle de Leibniz par les accroissements finis

Nous allons démontrer le théorème de dérivation sur un intervalle quelconque en utilisant le théorème de convergence dominée séquentielle et l'inégalité des accroissements finis.

**Étape 1 : Initialisation et formalisation séquentielle**
Soit $x \in A$. L'ouvert $A$ permet de choisir une suite $(h_n)_{n \in \mathbb{N}}$ de réels non nuls telle que $x+h_n \in A$ pour tout $n$, et $h_n \to 0$ lorsque $n \to +\infty$.
On étudie le taux d'accroissement de $F$ :
$$ \frac{F(x+h_n) - F(x)}{h_n} = \int_I \frac{f(x+h_n, t) - f(x,t)}{h_n} \, \mathrm{d}t $$
Posons $g_n(t) = \frac{f(x+h_n, t) - f(x,t)}{h_n}$.

**Étape 2 : Convergence ponctuelle**
Par hypothèse, $x \mapsto f(x,t)$ est dérivable en $x$. Par définition du taux d'accroissement pour la dérivée partielle :
$$ \forall t \in I, \quad \lim_{n \to +\infty} g_n(t) = \frac{\partial f}{\partial x}(x,t) $$

**Étape 3 : Domination par l'inégalité des accroissements finis**
Pour $t \in I$ fixé, appliquons le théorème des accroissements finis (ou l'inégalité si la fonction est à valeurs complexes) à l'application $u \mapsto f(u,t)$ entre $x$ et $x+h_n$.
Il existe un réel $\theta_n(t) \in ]x, x+h_n[$ (ou $]x+h_n, x[$ selon le signe de $h_n$) tel que :
$$ |g_n(t)| = \left| \frac{f(x+h_n, t) - f(x,t)}{h_n} \right| \leq \sup_{u \in [x, x+h_n]} \left| \frac{\partial f}{\partial x}(u,t) \right| $$
Or, l'hypothèse globale de domination de la dérivée impose :
$$ \forall u \in A, \quad \left| \frac{\partial f}{\partial x}(u,t) \right| \leq \psi(t) $$
Ainsi, pour tout $n \in \mathbb{N}$ et tout $t \in I$ :
$$ |g_n(t)| \leq \psi(t) $$
avec $\psi$ intégrable sur $I$.

**Étape 4 : Conclusion par convergence dominée**
La suite de fonctions $(g_n)$ converge simplement vers $\frac{\partial f}{\partial x}(x,\cdot)$, et est dominée par la fonction intégrable $\psi$. Par le théorème de convergence dominée (séquentiel) de Lebesgue :
$$ \lim_{n \to +\infty} \int_I g_n(t) \, \mathrm{d}t = \int_I \lim_{n \to +\infty} g_n(t) \, \mathrm{d}t = \int_I \frac{\partial f}{\partial x}(x,t) \, \mathrm{d}t $$
Cette limite étant vraie pour toute suite $(h_n)$ tendant vers $0$, on conclut que la dérivée $F'(x)$ existe et vérifie la relation attendue. La continuité de la dérivée s'obtient similairement par le théorème de continuité, en appliquant les hypothèses de régularité supplémentaires sur la dérivée partielle.

## 4. Lien fondamental avec l'Intelligence Artificielle

En apprentissage automatique (Machine Learning) probabiliste et en inférence variationnelle, on cherche souvent à optimiser une espérance par rapport aux paramètres d'une distribution.
Soit une fonction de coût $C(z)$ dépendant d'une variable aléatoire continue $Z \sim p_\theta(z)$, où $\theta$ est le paramètre du modèle (par exemple, les poids d'un réseau de neurones). L'objectif est d'optimiser le risque espéré :
$$ J(\theta) = \mathbb{E}_{Z \sim p_\theta}[C(Z)] = \int_{\mathcal{Z}} C(z) p_\theta(z) \, \mathrm{d}z $$
Pour optimiser $J$ par descente de gradient, il faut calculer $\nabla_\theta J(\theta)$. Sous les conditions strictes de domination (souvent garanties par la régularité des lois de probabilité exponentielles utilisées, comme les lois normales), le théorème de dérivation sous le signe intégral autorise l'interversion :
$$ \nabla_\theta J(\theta) = \int_{\mathcal{Z}} C(z) \nabla_\theta p_\theta(z) \, \mathrm{d}z $$
C'est le fondement du gradient par l'astuce de REINFORCE (ou _score function estimator_), pivot pour l'apprentissage par renforcement et les Auto-Encodeurs Variationnels (VAE). Sans l'assise mathématique des intégrales à paramètre, la backpropagation stochastique n'aurait aucune validité théorique.
