---
uuid: "jalon-37"
title: "Intégrale de Riemann sur un segment"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/calcul-integral
prev: "[[Jalon 36 (Livrable IA).md]]"
next: "[[Jalon 38 (Théorème fondamental de l'analyse).md]]"
---

# Jalon 37 : Intégrale de Riemann sur un segment

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous vouliez mesurer la surface d'un champ dont l'un des bords est une rivière sinueuse. Comme vous ne connaissez que la formule du rectangle (longueur $\times$ largeur), vous décidez de découper votre champ en plein de petites bandes verticales très fines. Chaque bande ressemble presque à un rectangle. En additionnant la surface de tous ces petits rectangles, vous obtenez une excellente approximation de la surface totale. Plus les bandes sont fines, plus vous êtes précis.
- **Le "Pourquoi on a inventé ça" :** Avant Riemann, on calculait des aires au cas par cas. L'intégrale de Riemann a apporté une méthode **universelle** et rigoureuse pour sommer une infinité de quantités infiniment petites. C'est l'outil de base pour calculer des moyennes, des probabilités et des énergies.
- **Visualisation :** On dessine une courbe, et on remplit l'espace en dessous avec des rectangles qui "montent" jusqu'à toucher la courbe. L'intégrale est la limite de la somme de ces aires quand la largeur des rectangles tend vers zéro.

## 2. Formalisation & Rigueur Académique

### A. Fonctions en Escalier et Subdivision

Soit $[a, b]$ un segment de $\mathbb{R}$.

> **Définition 1 (Subdivision) :**
> On appelle **subdivision** de $[a, b]$ toute famille finie de points $\sigma = (x_0, x_1, \dots, x_n)$ telle que $a = x_0 < x_1 < \dots < x_n = b$. Le **pas** de la subdivision est $\delta(\sigma) = \max (x_i - x_{i-1})$.

> **Définition 2 (Fonction en escalier) :**
> Une fonction $f : [a, b] \to \mathbb{R}$ est dite **en escalier** s'il existe une subdivision $\sigma$ telle que $f$ soit constante sur chaque intervalle ouvert $]x_{i-1}, x_i[$.

> **Définition 3 (Intégrale d'une fonction en escalier) :**
> Si $f$ est une fonction en escalier valant $c_i$ sur $]x_{i-1}, x_i[$, son intégrale est :
> $$\int_a^b f(t) dt = \sum_{i=1}^n c_i (x_i - x_{i-1})$$

### B. L'Intégrale de Riemann

Soit $f : [a, b] \to \mathbb{R}$ une fonction **bornée**.

> **Définition 4 (Fonction Riemann-intégrable) :**
> On définit l'intégrale inférieure $I_-(f) = \sup \{ \int g \mid g \in \mathcal{E}, g \le f \}$ et l'intégrale supérieure $I_+(f) = \inf \{ \int h \mid h \in \mathcal{E}, h \ge f \}$, où $\mathcal{E}$ est l'ensemble des fonctions en escalier.
> $f$ est dite **intégrable au sens de Riemann** si $I_-(f) = I_+(f)$. Cette valeur commune est notée $\int_a^b f(t) dt$.

### C. Propriétés de l'Intégrale

> **Théorème (Propriétés Fondamentales) :**
> 1. **Linéarité :** $\int (\alpha f + \beta g) = \alpha \int f + \beta \int g$.
> 2. **Positivité :** Si $f \ge 0$, alors $\int f \ge 0$.
> 3. **Relation de Chasles :** $\int_a^b f = \int_a^c f + \int_c^b f$.
> 4. **Inégalité de la moyenne :** $|\int_a^b f(t) dt| \le (b-a) \sup |f|$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Toute fonction continue est Riemann-intégrable

1. **Cadre :** Soit $f : [a, b] \to \mathbb{R}$ continue.
2. **Étape 1 : Continuité uniforme (Théorème de Heine)**
   Comme $[a, b]$ est un compact, $f$ est uniformément continue.
   $\forall \epsilon > 0, \exists \delta > 0$ tel que $\forall t, s \in [a, b], |t - s| < \delta \implies |f(t) - f(s)| < \frac{\epsilon}{b-a}$.
3. **Étape 2 : Construction des fonctions en escalier**
   Soit $\sigma = (x_0, \dots, x_n)$ une subdivision de pas inférieur à $\delta$.
   Sur chaque $[x_{i-1}, x_i]$, posons $m_i = \inf f$ et $M_i = \sup f$.
   Définissons $g$ (en dessous) par $g(t) = m_i$ et $h$ (au-dessus) par $h(t) = M_i$.
4. **Étape 3 : Calcul de l'écart**
   $$\int_a^b h(t) dt - \int_a^b g(t) dt = \sum_{i=1}^n (M_i - m_i)(x_i - x_{i-1})$$
   Par continuité uniforme, $M_i - m_i < \frac{\epsilon}{b-a}$ car l'écart entre deux points de l'intervalle est inférieur au pas $\delta$.
   $$\int_a^b h - \int_a^b g < \frac{\epsilon}{b-a} \sum_{i=1}^n (x_i - x_{i-1}) = \frac{\epsilon}{b-a} (b-a) = \epsilon$$
5. **Conclusion :** Comme on peut rendre l'écart arbitrairement petit, les bornes supérieure et inférieure coïncident. $f$ est intégrable.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Calcul par les sommes de Riemann
**Énoncé :** Calculer $\int_0^1 t^2 dt$ en utilisant une subdivision régulière $x_k = \frac{k}{n}$.
**Correction Détaillée :**
1. Somme de Riemann à droite : $S_n = \frac{1}{n} \sum_{k=1}^n (\frac{k}{n})^2 = \frac{1}{n^3} \sum_{k=1}^n k^2$.
2. Formule connue : $\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$.
3. Développement : $S_n = \frac{2n^3 + 3n^2 + n}{6n^3} = \frac{1}{3} + \frac{1}{2n} + \frac{1}{6n^2}$.
4. Limite : $\lim_{n \to \infty} S_n = \frac{1}{3}$.

### Exercice 2 : Niveau Avancé (Intégrabilité d'une fonction monotone)
**Énoncé :** Montrer que toute fonction monotone sur $[a, b]$ est Riemann-intégrable.
**Correction Détaillée :**
Supposons $f$ croissante. Pour une subdivision régulière de pas $h = \frac{b-a}{n}$, on a :
$M_i = f(x_i)$ et $m_i = f(x_{i-1})$.
$\int h - \int g = \sum (f(x_i) - f(x_{i-1})) \frac{b-a}{n} = \frac{b-a}{n} [f(b) - f(a)]$.
Quand $n \to \infty$, cet écart tend vers 0. La fonction est donc intégrable.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** L'intégrale est le passage obligé pour définir les **espérances mathématiques** et les **probabilités continues**, piliers de l'IA statistique. Elle permet aussi de définir la **Perte Cumulative** (Cumulative Loss) sur une période de temps.
- **Exemple Concret :**
    - **Calcul de l'AUC (Area Under the Curve) :** Pour évaluer un classifieur, on trace la courbe ROC. La performance est mesurée par l'aire sous cette courbe (intégrale de la sensibilité par rapport à la spécificité).
    - **Processus de Diffusion (Image Gen) :** Les modèles comme Stable Diffusion reposent sur des équations différentielles stochastiques dont la résolution implique des intégrales temporelles pour reconstruire l'image à partir du bruit.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 18 (Continuité des fonctions d'une variable réelle).md]], [[Jalon 35 (Caractérisation séquentielle des ouverts).md]]
- **Concepts Futurs dépendants :** [[Jalon 38 (Théorème fondamental de l'analyse).md]], [[Jalon 61 (Insuffisances de l'intégrale de Riemann).md]]
