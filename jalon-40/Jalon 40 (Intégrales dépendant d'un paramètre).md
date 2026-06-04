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

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez que vous cuisinez une soupe. L'intégrale, c'est le goût final de la soupe (le résultat de tout le mélange). Le "paramètre", c'est la température du feu. Si vous changez très légèrement la température, le goût de la soupe va-t-il changer radicalement d'un coup, ou bien va-t-il évoluer de manière fluide et prévisible ? Le calcul des intégrales à paramètres nous permet de savoir quand le résultat global (la soupe) réagit de manière lisse aux changements d'un réglage extérieur (le paramètre).
- **Le "Pourquoi on a inventé ça" :** Dans la vraie vie, beaucoup de fonctions ne sont pas écrites avec des formules simples comme $x^2$. Elles sont définies comme le résultat d'un processus cumulatif (une intégrale). Pour pouvoir optimiser ces processus, il faut savoir si on peut les dériver. On appelle cela "passer la dérivée sous le signe somme".
- **Visualisation :** Imaginez une famille de courbes qui se déforment quand vous bougez un curseur $x$. L'aire sous ces courbes se déforme elle aussi. On cherche à calculer la vitesse à laquelle cette aire change par rapport au curseur.

## 2. Formalisation & Rigueur Académique

Soit $f : A \times I \to \mathbb{R}$ une fonction où $I$ est un intervalle d'intégration et $A$ un intervalle de paramètres. On pose $F(x) = \int_I f(x, t) dt$.

### A. Théorème de Continuité

> **Théorème (Continuité sous le signe $\int$) :**
> Si :
> 1. Pour tout $t \in I$, l'application $x \mapsto f(x, t)$ est continue sur $A$.
> 2. Pour tout $x \in A$, l'application $t \mapsto f(x, t)$ est continue par morceaux sur $I$.
> 3. **Hypothèse de Domination :** Il existe une fonction $g : I \to \mathbb{R}_+$ intégrable sur $I$ telle que :
>    $$\forall (x, t) \in A \times I, \quad |f(x, t)| \le g(t)$$
> Alors $F$ est continue sur $A$.

### B. Théorème de Dérivation (Règle de Leibniz)

> **Théorème (Dérivation sous le signe $\int$) :**
> Si :
> 1. $f$ vérifie les hypothèses de continuité.
> 2. $f$ admet une dérivée partielle $\frac{\partial f}{\partial x}$ continue sur $A \times I$.
> 3. **Hypothèse de Domination de la dérivée :** Il existe une fonction $h : I \to \mathbb{R}_+$ intégrable sur $I$ telle que :
>    $$\forall (x, t) \in A \times I, \quad \left| \frac{\partial f}{\partial x}(x, t) \right| \le h(t)$$
> Alors $F$ est de classe $\mathcal{C}^1$ sur $A$ et :
> $$F'(x) = \int_I \frac{\partial f}{\partial x}(x, t) dt$$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration du Théorème de Dérivation (Esquisse par les accroissements finis)

1. **Objectif :** Montrer que $\frac{F(x+k) - F(x)}{k} \to \int \frac{\partial f}{\partial x}(x, t) dt$.
2. **Étape 1 : Taux d'accroissement de l'intégrale**
   $$\frac{F(x+k) - F(x)}{k} = \int_I \frac{f(x+k, t) - f(x, t)}{k} dt$$
3. **Étape 2 : Théorème des Accroissements Finis (TAF)**
   Pour chaque $t$, il existe $c_{x,k,t}$ entre $x$ et $x+k$ tel que :
   $$\frac{f(x+k, t) - f(x, t)}{k} = \frac{\partial f}{\partial x}(c_{x,k,t}, t)$$
4. **Étape 3 : Domination et Convergence**
   Par hypothèse de domination, $\left| \frac{\partial f}{\partial x} \right| \le h(t)$. On peut donc appliquer le **Théorème de Convergence Dominée** (qui sera vu en détail au Jalon 69, mais dont on utilise ici la version pour fonctions continues). Quand $k \to 0$, $c_{x,k,t} \to x$.
5. **Conclusion :** Par continuité de la dérivée partielle, la limite passe sous l'intégrale.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Calcul d'intégrale à paramètre
**Énoncé :** Soit $F(x) = \int_0^1 \frac{t^x - 1}{\ln(t)} dt$ pour $x > -1$. Calculer $F'(x)$ puis $F(x)$.
**Correction Détaillée :**
1. **Dérivation :** $f(x, t) = \frac{t^x - 1}{\ln(t)}$. La dérivée partielle par rapport à $x$ est $\frac{\partial f}{\partial x} = \frac{\ln(t) t^x}{\ln(t)} = t^x$.
2. **Application du théorème :** $t^x$ est continue et dominée sur tout $[a, b] \subset ]-1, +\infty[$.
3. **Calcul de F'(x) :** $F'(x) = \int_0^1 t^x dt = [\frac{t^{x+1}}{x+1}]_0^1 = \frac{1}{x+1}$.
4. **Intégration de F'(x) :** $F(x) = \ln(x+1) + C$.
5. **Condition initiale :** $F(0) = \int_0^1 \frac{1-1}{\ln(t)} = 0$. Donc $C = 0$.
6. **Résultat :** $F(x) = \ln(x+1)$.

### Exercice 2 : Niveau Avancé (Intégrale de Gauss)
**Énoncé :** En utilisant $G(x) = \int_0^{+\infty} e^{-xt^2} dt$, retrouver la valeur de l'intégrale de Gauss.
**Correction Détaillée :**
C'est un classique des concours. On montre par dérivation sous le signe $\int$ que certaines formes d'intégrales à paramètres permettent de résoudre des intégrales que l'on ne sait pas calculer par des primitives usuelles.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** C'est la base mathématique de l'**Optimisation Stochastique**. En IA, on veut minimiser la perte attendue :
  $$J(\theta) = \mathbb{E}_{x \sim p}[L(x, \theta)] = \int L(x, \theta) p(x) dx$$
  Pour faire une descente de gradient, on doit calculer $\nabla_\theta J(\theta)$.
- **Exemple Concret :**
    - **Interversion Gradient-Intégrale :** Le fait de calculer le gradient sur un "mini-batch" et d'espérer que sa moyenne converge vers le vrai gradient du système repose sur la règle de Leibniz. On dérive *sous* l'intégrale (la somme) pour obtenir le gradient moyen.
    - **Modèles Génératifs (VAE) :** Dans les Variational Auto-Encoders, on maximise une borne (ELBO) qui est une intégrale à paramètre (les paramètres du réseau). La "Reparameterization Trick" est une astuce géniale qui change la variable d'intégration pour faciliter cette dérivation sous le signe $\int$.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 39 (Intégrales généralisées sur un intervalle quelconque et critères de convergence.).md]], [[Jalon 20 (Dérivées successives).md]]
- **Concepts Futurs dépendants :** [[Jalon 69 (Démonstration complète du théorème de convergence dominée de Lebesgue.).md]], [[Jalon 80 (Transformée de Fourier dans L1).md]]
