---
uuid: "jalon-71"
title: "Théorèmes de Fubini-Tonelli"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 70 (Espaces mesurés produits).md]]"
next: "[[Jalon 72 (Livrable IA).md]]"
---

# Jalon 71 : Théorèmes de Fubini-Tonelli

## 1. Genèse et Intuition Physique

Le calcul d'intégrales multiples se pose naturellement dès que l'on cherche à évaluer des grandeurs réparties dans l'espace ou le plan : la masse d'un solide dont la densité varie, le volume d'un fluide sous une surface, ou encore la probabilité conjointe de plusieurs événements.

L'intuition physique sous-jacente au théorème de Fubini est celle du principe de Cavalieri : le volume d'un solide peut être obtenu en sommant (intégrant) l'aire de ses sections parallèles. Concrètement, pour évaluer une quantité globale sur un domaine 2D, on peut soit "balayer" le domaine en calculant la somme des contributions sur des lignes horizontales, puis sommer ces lignes verticalement, soit faire l'inverse (colonnes puis lignes horizontales). Le bon sens physique postule que la quantité totale est invariante par rapport à la méthode de balayage. Les théorèmes de Tonelli et Fubini constituent la formalisation rigoureuse de cette invariance dans le cadre de la théorie de la mesure de Lebesgue, en précisant les conditions (positivité ou intégrabilité absolue) sous lesquelles cette interversion des signes d'intégration est légitime.

## 2. Définitions, Théorèmes et Exemples

### Cadre formel

Soient $(X_1, \mathcal{F}_1, \mu_1)$ et $(X_2, \mathcal{F}_2, \mu_2)$ deux espaces mesurés $\sigma$-finis.
Soit $(X_1 \times X_2, \mathcal{F}_1 \otimes \mathcal{F}_2, \mu_1 \otimes \mu_2)$ l'espace produit associé.
Soit $f : X_1 \times X_2 \to \overline{\mathbb{R}}$ ou $\mathbb{C}$ une fonction mesurable.

### Théorème de Tonelli (Cas positif)

**Théorème** :
Si $f \ge 0$ (fonction mesurable positive), alors :
1. Les fonctions partielles $x_1 \mapsto \int_{X_2} f(x_1, x_2) d\mu_2(x_2)$ et $x_2 \mapsto \int_{X_1} f(x_1, x_2) d\mu_1(x_1)$ sont mesurables et positives.
2. L'égalité suivante est vérifiée (dans $[0, +\infty]$) :
   $$ \int_{X_1 \times X_2} f d(\mu_1 \otimes \mu_2) = \int_{X_1} \left( \int_{X_2} f(x_1, x_2) d\mu_2(x_2) \right) d\mu_1(x_1) = \int_{X_2} \left( \int_{X_1} f(x_1, x_2) d\mu_1(x_1) \right) d\mu_2(x_2) $$

### Théorème de Fubini (Cas intégrable)

**Théorème** :
Soit $f : X_1 \times X_2 \to \mathbb{C}$ (ou $\mathbb{R}$) mesurable.
On suppose que l'une des trois intégrales suivantes est finie (en appliquant le théorème de Tonelli à $|f|$) :
- $\int_{X_1 \times X_2} |f| d(\mu_1 \otimes \mu_2) < +\infty$
- $\int_{X_1} \left( \int_{X_2} |f| d\mu_2 \right) d\mu_1 < +\infty$
- $\int_{X_2} \left( \int_{X_1} |f| d\mu_1 \right) d\mu_2 < +\infty$

Alors, la fonction $f$ est intégrable par rapport à la mesure produit $\mu_1 \otimes \mu_2$, et on a l'égalité des intégrales :
$$ \int_{X_1 \times X_2} f d(\mu_1 \otimes \mu_2) = \int_{X_1} \left( \int_{X_2} f d\mu_2 \right) d\mu_1 = \int_{X_2} \left( \int_{X_1} f d\mu_1 \right) d\mu_2 $$
*(Pour presque tout $x_1$, la fonction partielle $x_2 \mapsto f(x_1, x_2)$ est intégrable, et réciproquement).*

### Exemples Concrets et Application Immédiate

**Exemple 1 : Intégrale d'un produit (Variables séparables)**
Soit $f(x,y) = e^{-x} e^{-2y}$ sur $X_1 = [0, +\infty[$, $X_2 = [0, +\infty[$.
On a $\int_{0}^{+\infty} \int_{0}^{+\infty} e^{-x-2y} dx dy = \left( \int_0^{+\infty} e^{-x} dx \right) \left( \int_0^{+\infty} e^{-2y} dy \right) = 1 \times \frac{1}{2} = \frac{1}{2}$.
Ici, $f \ge 0$, donc Tonelli garantit que le produit des intégrales est bien l'intégrale sur $\mathbb{R}_+^2$.

**Exemple 2 : Calcul de volume par section (Tonelli)**
Soit le domaine $D = \{(x,y) \in \mathbb{R}^2 \mid 0 \le x \le 1, 0 \le y \le x^2\}$.
L'aire de $D$ vaut $\iint_D 1 dx dy$.
En intégrant d'abord en $y$ (tranches verticales) : $\int_0^1 \left( \int_0^{x^2} 1 dy \right) dx = \int_0^1 x^2 dx = \frac{1}{3}$.
En intégrant d'abord en $x$ (tranches horizontales) : $\int_0^1 \left( \int_{\sqrt{y}}^1 1 dx \right) dy = \int_0^1 (1 - \sqrt{y}) dy = 1 - \frac{2}{3} = \frac{1}{3}$.
L'égalité vérifie empiriquement Tonelli.

**Exemple 3 : Intégrale double convergente via Fubini**
Évaluons $I = \int_{0}^1 \int_0^1 \frac{x-y}{x+y} dx dy$.
Attention, ce domaine nécessite prudence. Si $f(x,y) = \frac{x-y}{(x+y)^3}$, l'intégrale absolue diverge en $(0,0)$.
Prenons $f(x,y) = x \cos(xy)$ sur $[0,1] \times [0,\pi/2]$. $f$ change de signe mais $|f|$ est bornée (continue sur un compact), donc Lebesgue-intégrable.
Intégration d'abord selon $y$ : $\int_0^1 \left( [ \sin(xy) ]_{y=0}^{y=\pi/2} \right) dx = \int_0^1 \sin(\frac{\pi x}{2}) dx = [-\frac{2}{\pi} \cos(\frac{\pi x}{2})]_0^1 = \frac{2}{\pi}$.

**Exemple 4 : La condition de Fubini est indispensable (Contre-exemple classique)**
Soit $f(x,y) = \frac{x^2-y^2}{(x^2+y^2)^2}$ sur $[0,1] \times [0,1] \setminus \{(0,0)\}$.
On a $\int_0^1 \left( \int_0^1 f(x,y) dy \right) dx = \int_0^1 [\frac{y}{x^2+y^2}]_0^1 dx = \int_0^1 \frac{1}{x^2+1} dx = \frac{\pi}{4}$.
Mais $\int_0^1 \left( \int_0^1 f(x,y) dx \right) dy = -\frac{\pi}{4}$.
Pourquoi l'égalité est-elle fausse ? Car Tonelli sur la valeur absolue donne $\iint |f| = +\infty$. $f$ n'est pas intégrable, Fubini ne s'applique pas.

**Exemple 5 : L'intégrale de Gauss**
Le calcul de $I = \int_0^{+\infty} e^{-x^2} dx$ s'appuie sur Tonelli : $I^2 = \int_0^{+\infty} e^{-x^2} dx \int_0^{+\infty} e^{-y^2} dy = \iint_{\mathbb{R}_+^2} e^{-(x^2+y^2)} dx dy$.
Par passage en polaires, $I^2 = \int_0^{\pi/2} \int_0^{+\infty} e^{-r^2} r dr d\theta = \frac{\pi}{4}$, d'où $I = \frac{\sqrt{\pi}}{2}$.

**Exemple 6 : Espace de probabilité (Marginalisation)**
Soit une densité conjointe $p(x,y)$ (fonction positive d'intégrale 1).
Tonelli assure que $\int_\mathbb{R} \left( \int_\mathbb{R} p(x,y) dy \right) dx = 1$, ce qui justifie que la distribution marginale $p_X(x) = \int p(x,y) dy$ est une densité de probabilité bien définie.

**Exemple 7 : Fubini-Tonelli et séries**
Les sommes doubles sont des intégrales par rapport à la mesure de comptage sur $\mathbb{N}^2$.
Si $u_{n,m} \ge 0$, alors $\sum_n \sum_m u_{n,m} = \sum_m \sum_n u_{n,m}$ (Tonelli).
Si $\sum_n \sum_m |u_{n,m}| < +\infty$, alors on peut sommer $u_{n,m}$ (qui peut avoir des signes variables) dans n'importe quel ordre (Fubini).

## 3. Démonstrations

La démonstration des théorèmes de Tonelli et Fubini s'appuie fondamentalement sur le lemme des classes monotones (ou lemme de Dynkin) et se décompose en plusieurs étapes :

1. **Cas des ensembles mesurables (Indicatrices) :**
   Si $f = \mathbf{1}_E$ avec $E \in \mathcal{F}_1 \otimes \mathcal{F}_2$. On considère la classe $\mathcal{M}$ des ensembles $E$ pour lesquels la propriété d'interversion de Tonelli est vraie. On montre aisément que la propriété est vraie pour les "pavés mesurables" $A_1 \times A_2$.
   Puisque l'application $E \mapsto \iint \mathbf{1}_E$ définit une mesure, et que la classe des pavés forme une algèbre qui engendre $\mathcal{F}_1 \otimes \mathcal{F}_2$, le lemme d'extension des mesures de Carathéodory (ou les classes monotones) permet de conclure que l'égalité est vraie pour tout $E \in \mathcal{F}_1 \otimes \mathcal{F}_2$. L'hypothèse $\sigma$-finie est ici cruciale pour l'unicité de l'extension.

2. **Cas des fonctions étagées positives :**
   Par linéarité de l'intégrale (qui commute avec les sommes finies), la relation établie pour les indicatrices s'étend immédiatement à toute combinaison linéaire positive d'indicatrices (fonctions étagées positives).

3. **Cas des fonctions mesurables positives (Tonelli complet) :**
   Toute fonction $f \ge 0$ mesurable est la limite simple d'une suite croissante $(f_n)_{n \in \mathbb{N}}$ de fonctions étagées positives.
   On applique le théorème de convergence monotone (Beppo-Levi) à la suite $(f_n)$. La limite passe sous l'intégrale par rapport à $\mu_2$, donnant une suite croissante de fonctions mesurables en $x_1$, sur laquelle on réapplique Beppo-Levi par rapport à $\mu_1$. Cela prouve l'égalité pour $f$.

4. **Cas des fonctions intégrables (Fubini) :**
   Si $f$ est de signe quelconque, mais vérifie l'hypothèse de la finitude de l'intégrale de $|f|$, on décompose $f = f^+ - f^-$ en sa partie positive et sa partie négative.
   Par Tonelli, $f^+$ et $f^-$ ont des intégrales finies. Par linéarité, l'intégrale itérée de $f$ est la différence des intégrales itérées de $f^+$ et $f^-$, d'où le résultat. Dans le cas complexe, on décompose en parties réelle et imaginaire.

## 4. Applications en Physique, Logique et AI

- **Physique Théorique (Mécanique Quantique et Statistique) :** Le calcul de grandeurs macroscopiques à partir d'états microscopiques continus requiert constamment des intégrations sur l'espace des phases (positions et impulsions). Le théorème de Fubini garantit que le calcul du volume de l'espace des phases (théorème de Liouville) ou de la fonction de partition est indépendant de l'ordre d'intégration sur les degrés de liberté des particules.
- **Théorie des Probabilités :** La démonstration de l'indépendance de variables aléatoires s'appuie de façon incontournable sur Fubini. L'espérance du produit de deux variables aléatoires indépendantes $X$ et $Y$ se décompose en $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$ car la mesure jointe est le produit des mesures marginales, et l'intégrale double factorise grâce à Fubini.
- **Intelligence Artificielle (Réseaux de Neurones et VAE) :**
    - Dans la modélisation générative (comme les Auto-encodeurs variationnels, VAE), la vraisemblance marginale des données $P(X) = \int P(X|Z)P(Z) dZ$ est une intégration sur l'espace latent $Z$.
    - L'estimation de paramètres par maximum de vraisemblance et l'utilisation de divergences (comme Kullback-Leibler) impliquent des doubles sommes (ou intégrales croisées sur des batchs et des dimensions). Le théorème de Tonelli assure la légitimité des inversions d'espérance algorithmique et de sommation spatiale.
    - Pour les processus gaussiens, le calcul des noyaux covariants par intégration marginale repose fondamentalement sur les garanties analytiques offertes par ces théorèmes.
