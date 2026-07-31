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

## 1. Introduction et Origines Analytiques

L'étude des intégrales dépendant d'un paramètre trouve son origine dans le besoin fondamental de la physique mathématique, notamment chez Euler et Laplace, de manipuler des expressions intégrales complexes représentant des phénomènes continus (comme le potentiel gravitationnel ou la diffusion de la chaleur). Lorsqu'une grandeur physique est exprimée sous forme d'intégrale, la question naturelle est d'étudier comment cette grandeur varie lorsque les conditions initiales ou les paramètres du système sont modifiés de manière infinitésimale.

L'enjeu algébrique sous-jacent consiste à justifier l'interversion de deux processus limites continus : l'intégration et le passage à la limite (ou la dérivation). De manière informelle, on souhaite pouvoir écrire :
$$ \frac{d}{dx} \int_I f(x,t) dt = \int_I \frac{\partial f}{\partial x}(x,t) dt $$
Cette interversion n'est pas trivialement acquise, particulièrement lorsque l'intervalle d'intégration est non borné (intégrales généralisées). La formalisation rigoureuse de ce cadre a nécessité le développement des théorèmes de continuité et de dérivation sous le signe intégral, qui préfigurent la puissance de la théorie de la mesure de Lebesgue et du théorème de convergence dominée.

## 2. Continuité des Intégrales à Paramètre

### Théorème de Continuité sous le Signe Intégral

Soient $A$ un intervalle de $\mathbb{R}$, $I$ un intervalle d'intégration (borné ou non), et une fonction $f : A \times I \to \mathbb{R}$ ou $\mathbb{C}$. On définit la fonction $F$ sur l'ensemble $A$ par :
$$ F(x) = \int_I f(x, t) dt $$

**Théorème.** Si les trois conditions suivantes sont satisfaites :
1. $\forall t \in I$, l'application $x \mapsto f(x, t)$ est continue sur $A$.
2. $\forall x \in A$, l'application $t \mapsto f(x, t)$ est continue par morceaux sur $I$.
3. **Hypothèse de domination locale :** Pour tout segment $K \subset A$, il existe une fonction $\varphi_K : I \to \mathbb{R}^+$ continue par morceaux et intégrable sur $I$, telle que :
   $$ \forall x \in K, \forall t \in I, \quad |f(x, t)| \le \varphi_K(t) $$
Alors, l'application $F$ est définie et continue sur $A$.

### Exemple Concret Immédiat : Étude d'une fonction Gamma incomplète

Considérons $F(x) = \int_0^{+\infty} e^{-xt} \frac{\sin(t)}{t} dt$ pour $x \in ]0, +\infty[$.
Soit $f(x, t) = e^{-xt} \frac{\sin(t)}{t}$ prolongée par continuité en $t=0$ par $e^{-x \cdot 0} \cdot 1 = 1$.
1. Pour $t \ge 0$ fixé, $x \mapsto f(x,t)$ est continue sur $]0, +\infty[$.
2. Pour $x > 0$ fixé, $t \mapsto f(x,t)$ est continue sur $[0, +\infty[$.
3. Fixons un segment $K = [a, b] \subset ]0, +\infty[$ avec $0 < a < b$. Pour $x \in K$ et $t \ge 0$, on a :
   $$ |f(x,t)| = e^{-xt} \left|\frac{\sin(t)}{t}\right| \le e^{-xt} \le e^{-at} $$
   Or, l'application $t \mapsto e^{-at}$ est intégrable sur $[0, +\infty[$ car $a > 0$.
Par le théorème de continuité, $F$ est continue sur $]0, +\infty[$.

### Contre-exemple : Rupture de continuité

Soit $f(x, t) = x e^{-xt^2}$ sur $A = \mathbb{R}^+$ et $I = [0, +\infty[$.
Pour $x > 0$, $F(x) = \int_0^{+\infty} x e^{-xt^2} dt = \sqrt{x} \int_0^{+\infty} e^{-u^2} du = \sqrt{x} \frac{\sqrt{\pi}}{2}$.
Cependant, pour $x = 0$, $F(0) = \int_0^{+\infty} 0 dt = 0$.
Ici $F(x)$ ne présente pas de discontinuité, mais considérons un exemple classique de la littérature où l'interversion limite-intégrale échoue en l'absence de domination globale uniforme.

## 3. Dérivation et Règle de Leibniz

### Théorème de Dérivation (Forme de Leibniz)

**Théorème.** Si les conditions suivantes sont satisfaites :
1. $\forall t \in I$, l'application $x \mapsto f(x, t)$ est de classe $\mathcal{C}^1$ sur $A$.
2. $\forall x \in A$, les applications $t \mapsto f(x, t)$ et $t \mapsto \frac{\partial f}{\partial x}(x, t)$ sont continues par morceaux et intégrables sur $I$.
3. **Hypothèse de domination de la dérivée :** Pour tout segment $K \subset A$, il existe $\psi_K : I \to \mathbb{R}^+$ intégrable sur $I$ telle que :
   $$ \forall x \in K, \forall t \in I, \quad \left| \frac{\partial f}{\partial x}(x, t) \right| \le \psi_K(t) $$
Alors $F$ est de classe $\mathcal{C}^1$ sur $A$ et :
$$ F'(x) = \int_I \frac{\partial f}{\partial x}(x, t) dt $$

### Démonstration Ligne par Ligne (Cas d'un segment compact)

Supposons $I = [a,b]$ compact et $f$ de classe $\mathcal{C}^1$ sur $A \times [a,b]$.
Par le théorème des accroissements finis, pour $x, x+h \in A$ :
$$ \frac{F(x+h) - F(x)}{h} = \int_a^b \frac{f(x+h, t) - f(x, t)}{h} dt = \int_a^b \frac{\partial f}{\partial x}(x + \theta h, t) dt $$
avec $0 < \theta < 1$. Puisque $\frac{\partial f}{\partial x}$ est continue sur le compact $A \times [a,b]$, elle y est uniformément continue (théorème de Heine). Par conséquent :
$$ \forall \epsilon > 0, \exists \delta > 0, |h| < \delta \implies \left| \frac{\partial f}{\partial x}(x+\theta h, t) - \frac{\partial f}{\partial x}(x, t) \right| < \epsilon $$
Donc :
$$ \left| \frac{F(x+h) - F(x)}{h} - \int_a^b \frac{\partial f}{\partial x}(x, t) dt \right| \le \int_a^b \epsilon dt = \epsilon (b-a) $$
En faisant tendre $h \to 0$, on obtient exactement $F'(x) = \int_a^b \frac{\partial f}{\partial x}(x, t) dt$.

### Exemple Concret Immédiat : Calcul de l'intégrale de Gauss paramétrée

Soit $F(x) = \int_0^{+\infty} e^{-t^2} \cos(xt) dt$.
Posons $f(x, t) = e^{-t^2} \cos(xt)$. La fonction $f$ vérifie :
$\frac{\partial f}{\partial x}(x,t) = -t e^{-t^2} \sin(xt)$.
Majoration : $\left| \frac{\partial f}{\partial x}(x,t) \right| \le t e^{-t^2}$.
La fonction $\psi(t) = t e^{-t^2}$ est intégrable sur $[0, +\infty[$ (car primitive $- \frac{1}{2} e^{-t^2}$).
Ainsi $F \in \mathcal{C}^1(\mathbb{R})$ et $F'(x) = \int_0^{+\infty} -t e^{-t^2} \sin(xt) dt$.
Par intégration par parties : $u(t) = \sin(xt)$ et $v'(t) = -t e^{-t^2}$ (donc $v(t) = \frac{1}{2} e^{-t^2}$) :
$F'(x) = \left[ \frac{1}{2} e^{-t^2} \sin(xt) \right]_0^{+\infty} - \frac{x}{2} \int_0^{+\infty} e^{-t^2} \cos(xt) dt = -\frac{x}{2} F(x)$.
C'est une équation différentielle linéaire du premier ordre : $F'(x) + \frac{x}{2} F(x) = 0$.
Solution : $F(x) = F(0) e^{-x^2/4}$. Sachant que $F(0) = \int_0^{+\infty} e^{-t^2} dt = \frac{\sqrt{\pi}}{2}$, on conclut que :
$$ \int_0^{+\infty} e^{-t^2} \cos(xt) dt = \frac{\sqrt{\pi}}{2} e^{-x^2/4} $$

## 4. Applications en Théorie de l'Information et Intelligence Artificielle

### Estimation et Interversion du Gradient

En apprentissage statistique, le calcul du risque attendu est une intégrale dépendant du paramètre du modèle $\theta$ :
$$ \mathcal{L}(\theta) = \int_{\mathcal{X} \times \mathcal{Y}} L(f_\theta(x), y) p(x, y) dx dy $$
L'algorithme de descente de gradient stochastique (SGD) postule que le gradient de l'espérance est l'espérance du gradient :
$$ \nabla_\theta \mathbb{E}[L] = \mathbb{E}[\nabla_\theta L] $$
Cette égalité stricte repose entièrement sur l'application du théorème de Leibniz pour dériver sous le signe de la somme continue, validant mathématiquement l'architecture de rétropropagation à travers des couches dont les poids varient de manière infinitésimale.
