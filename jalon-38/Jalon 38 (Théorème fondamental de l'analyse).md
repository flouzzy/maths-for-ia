---
uuid: "jalon-38"
title: "Théorème fondamental de l'analyse"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/calcul-differentiel
prev: "[[Jalon 37 (Intégrale de Riemann sur un segment).md]]"
next: "[[Jalon 39 (Intégrales généralisées sur un intervalle quelconque et critères de convergence.).md]]"
---

# Jalon 38 : Théorème fondamental de l'analyse

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous regardez le compteur de vitesse de votre voiture. Il vous donne votre vitesse instantanée (la dérivée de votre position). Si vous notez cette vitesse à chaque seconde et que vous calculez l'aire sous la courbe de vitesse (l'intégrale), vous obtenez exactement la distance totale parcourue. Le **Théorème Fondamental de l'Analyse** est le pont magique qui relie ces deux mondes : la vitesse (le changement local) et la distance (l'accumulation globale).
- **Le "Pourquoi on a inventé ça" :** Avant ce théorème, la dérivation (trouver la pente) et l'intégration (trouver l'aire) semblaient être deux problèmes totalement différents. Newton et Leibniz ont réalisé qu'ils étaient en fait les "ennemis jurés" l'un de l'autre : l'un est l'opération inverse de l'autre. C'est ce qui a permis de transformer le calcul d'aires complexes en un simple calcul de soustraction de fonctions.
- **Visualisation :** Si on définit une fonction $F(x)$ comme l'aire sous une courbe $f$ entre $a$ et $x$, alors la pente de $F$ au point $x$ est exactement la hauteur de la courbe $f(x)$.

## 2. Formalisation & Rigueur Académique

### A. Définitions et Théorème Fondamental

Soit $f : I \to \mathbb{R}$ une fonction continue sur un intervalle $I \subset \mathbb{R}$.

> **Définition 1 (Primitive) :**
> On appelle **primitive** de $f$ sur $I$ toute fonction $F$ dérivable sur $I$ telle que $F' = f$. Toute fonction continue admet une infinité de primitives, toutes égales à une constante près.

> **Théorème Fondamental de l'Analyse (Partie 1) :**
> Soit $f$ continue sur $[a, b]$. L'application $\Phi : x \mapsto \int_a^x f(t) dt$ est l'unique primitive de $f$ s'annulant en $a$. Elle est de classe $\mathcal{C}^1$ sur $[a, b]$.
> $$\forall x \in [a, b], \quad \Phi'(x) = f(x)$$

> **Théorème Fondamental de l'Analyse (Partie 2) :**
> Si $F$ est une primitive quelconque de $f$, alors :
> $$\int_a^b f(t) dt = [F(t)]_a^b = F(b) - F(a)$$

### B. Techniques d'Intégration

> **Théorème (Intégration par parties - IPP) :**
> Soient $u$ et $v$ deux fonctions de classe $\mathcal{C}^1$ sur $[a, b]$. Alors :
> $$\int_a^b u'(t) v(t) dt = [u(t)v(t)]_a^b - \int_a^b u(t) v'(t) dt$$

> **Théorème (Changement de variable) :**
> Soit $f$ continue sur $I$ et $\phi : [a, b] \to I$ une fonction de classe $\mathcal{C}^1$. Alors :
> $$\int_a^b f(\phi(t)) \phi'(t) dt = \int_{\phi(a)}^{\phi(b)} f(u) du$$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration du Théorème Fondamental (Partie 1)

1. **Objectif :** Montrer que $\lim_{h \to 0} \frac{\Phi(x+h) - \Phi(x)}{h} = f(x)$.
2. **Étape 1 : Expression du taux d'accroissement**
   $$\frac{\Phi(x+h) - \Phi(x)}{h} = \frac{1}{h} \left( \int_a^{x+h} f(t) dt - \int_a^x f(t) dt \right) = \frac{1}{h} \int_x^{x+h} f(t) dt$$ (par la relation de Chasles).
3. **Étape 2 : Utilisation de la continuité**
   Comme $f$ est continue en $x$, pour tout $\epsilon > 0$, il existe $\delta > 0$ tel que $|t - x| < \delta \implies f(x) - \epsilon \le f(t) \le f(x) + \epsilon$.
   Supposons $0 < h < \delta$. Alors pour tout $t \in [x, x+h]$, l'inégalité est vérifiée.
4. **Étape 3 : Encadrement de l'intégrale**
   En intégrant l'encadrement sur $[x, x+h]$ :
   $$\int_x^{x+h} (f(x) - \epsilon) dt \le \int_x^{x+h} f(t) dt \le \int_x^{x+h} (f(x) + \epsilon) dt$$
   $$h(f(x) - \epsilon) \le \int_x^{x+h} f(t) dt \le h(f(x) + \epsilon)$$
5. **Étape 4 : Passage à la limite**
   En divisant par $h$ : $f(x) - \epsilon \le \frac{\Phi(x+h) - \Phi(x)}{h} \le f(x) + \epsilon$.
   Ceci étant vrai pour tout $\epsilon$, le taux d'accroissement tend vers $f(x)$.
6. **Conclusion :** $\Phi$ est dérivable et $\Phi' = f$.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Intégration par parties (IPP)
**Énoncé :** Calculer $I = \int_0^\pi x \sin(x) dx$.
**Correction Détaillée :**
1. On pose $u(x) = x \implies u'(x) = 1$.
2. On pose $v'(x) = \sin(x) \implies v(x) = -\cos(x)$.
3. Formule d'IPP : $I = [x(-\cos(x))]_0^\pi - \int_0^\pi 1 \cdot (-\cos(x)) dx$.
4. $I = (-\pi \cos(\pi) - 0) + \int_0^\pi \cos(x) dx$.
5. $I = \pi + [\sin(x)]_0^\pi = \pi + 0 - 0 = \pi$.

### Exercice 2 : Changement de variable
**Énoncé :** Calculer $J = \int_0^1 \frac{e^t}{1 + e^{2t}} dt$.
**Correction Détaillée :**
1. On pose $u = e^t$, donc $du = e^t dt$.
2. Bornes : si $t=0, u=1$. Si $t=1, u=e$.
3. Substitution : $J = \int_1^e \frac{1}{1 + u^2} du$.
4. Primitive : $J = [\arctan(u)]_1^e = \arctan(e) - \arctan(1)$.
5. Résultat : $J = \arctan(e) - \frac{\pi}{4}$.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Le Théorème Fondamental lie l'optimisation locale (gradients) à la performance globale. C'est ce qui justifie l'utilisation des intégrales pour calculer les espérances des gradients dans les algorithmes stochastiques.
- **Exemple Concret :**
    - **Accumulation du Gradient :** Dans l'entraînement de grands modèles (LLM), on ne peut pas mettre tout un "batch" en mémoire. On calcule le gradient sur des petits sous-groupes et on les **somme** (on les intègre numériquement). Le théorème fondamental garantit que la somme de ces petits changements locaux équivaut au changement total que l'on aurait eu avec le batch entier.
    - **Neural ODEs :** C'est une architecture d'IA moderne où les couches du réseau de neurones ne sont plus discrètes, mais définies par une équation différentielle continue. Pour calculer la sortie du réseau, l'ordinateur résout une intégrale en utilisant le théorème fondamental.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 19 (Dérivabilité).md]], [[Jalon 37 (Intégrale de Riemann sur un segment).md]]
- **Concepts Futurs dépendants :** [[Jalon 39 (Intégrales généralisées sur un intervalle quelconque et critères de convergence.).md]], [[Jalon 43 (Systèmes différentiels linéaires d'ordre 1 et calcul de l'exponentielle de matrice.).md]]
