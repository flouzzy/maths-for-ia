---
uuid: "jalon-64"
title: "Construction de la mesure de Lebesgue"
year: 2
trimester: 6
tags:
  - math/mesure
  - ia/abstraction
prev: "[[Jalon 63 (Définition axiomatique d'une mesure).md]]"
next: "[[Jalon 65 (Fonctions mesurables).md]]"
---

# Jalon 64 : Construction de la mesure de Lebesgue

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous ayez une règle infiniment précise. Mesurer la longueur d'un segment bien droit, c'est facile. Mais comment mesurer la "longueur" d'un nuage de points éparpillés sur la règle ?
    - L'idée de la **mesure extérieure**, c'est de recouvrir votre nuage de points avec plein de petits pansements (des intervalles ouverts). Vous additionnez la longueur de tous les pansements.
    - Comme vous voulez être le plus précis possible, vous essayez de trouver la combinaison de pansements qui utilise le moins de longueur totale.
    - La **Mesure de Lebesgue**, c'est le résultat final de ce "meilleur recouvrement possible". Elle permet de donner un sens mathématique à la notion de "taille" pour des ensembles extrêmement découpés ou bizarres.
- **Le "Pourquoi on a inventé ça" :** On s'est rendu compte que certains ensembles (comme les nombres rationnels) sont partout sur la droite, mais ne prennent en fait "aucune place" réelle. Pour construire une théorie de l'intégration solide (Jalon 61), il fallait définir cette "place" (cette mesure) de manière indiscutable.
- **Visualisation :** On recouvre un ensemble complexe par une infinité de petits segments de plus en plus fins. Si la longueur totale de ces segments se stabilise, on a trouvé la mesure.

## 2. Formalisation

### A. La Mesure Extérieure

Soit $\mathcal{P}(\mathbb{R})$ l'ensemble de toutes les parties de $\mathbb{R}$.

> **Définition 1 (Mesure extérieure de Lebesgue) :**
> Pour toute partie $A \subset \mathbb{R}$, on définit $\lambda^*(A)$ par :
> $$\lambda^*(A) = \inf \left\{ \sum_{n=1}^\infty \ell(I_n) \mid A \subset \bigcup_{n=1}^\infty I_n \right\}$$
> où les $I_n = ]a_n, b_n[$ sont des intervalles ouverts et $\ell(I_n) = b_n - a_n$.

$\lambda^*$ est définie sur TOUT $\mathcal{P}(\mathbb{R})$, mais elle n'est pas $\sigma$-additive sur tout $\mathcal{P}(\mathbb{R})$. On doit restreindre son domaine.

### B. Le Critère de Carathéodory

> **Définition 2 (Ensemble Lebesgue-mesurable) :**
> Une partie $E \subset \mathbb{R}$ est dite **mesurable au sens de Lebesgue** si pour toute partie $A \subset \mathbb{R}$ :
> $$\lambda^*(A) = \lambda^*(A \cap E) + \lambda^*(A \cap ( \mathbb{R} \setminus E ))$$
> L'ensemble de ces parties forme une tribu, notée $\mathcal{L}(\mathbb{R})$.

### C. La Mesure de Lebesgue

> **Définition 3 (Mesure de Lebesgue) :**
> On appelle **mesure de Lebesgue** (notée $\lambda$) la restriction de la mesure extérieure $\lambda^*$ à la tribu des ensembles mesurables. $(\mathbb{R}, \mathcal{L}(\mathbb{R}), \lambda)$ est un espace mesuré complet.

## 3. Démonstrations

### Démonstration : Un ensemble dénombrable est de mesure nulle

1. **Cadre :** Soit $A = \{a_1, a_2, \dots, a_n, \dots \}$ un ensemble dénombrable de $\mathbb{R}$.
2. **Construction du recouvrement :** Soit $\epsilon > 0$. Pour chaque point $a_n$, on choisit un petit intervalle ouvert $I_n$ centré en $a_n$ de longueur $\epsilon / 2^{n+1}$.
   $I_n = ] a_n - \frac{\epsilon}{2^{n+2}}, a_n + \frac{\epsilon}{2^{n+2}} [$.
3. **Calcul de la longueur totale :**
   $A \subset \bigcup_{n=1}^\infty I_n$.
   $\sum_{n=1}^\infty \ell(I_n) = \sum_{n=1}^\infty \frac{\epsilon}{2^{n+1}} = \frac{\epsilon}{2} \sum_{n=1}^\infty \frac{1}{2^n}$.
4. **Somme géométrique :** $\sum_{n=1}^\infty (1/2)^n = 1$.
   Donc $\sum \ell(I_n) = \epsilon/2$.
5. **Conclusion :** Par définition de l'infimum, $\lambda^*(A) \le \epsilon/2$. Comme ceci est vrai pour tout $\epsilon > 0$, alors $\lambda^*(A) = 0$. Donc $\lambda(A) = 0$.

## 4. Exercices d'Application

### Exercice 1 : Mesure de $\mathbb{Q}$
**Énoncé :** Quelle est la mesure de Lebesgue de l'ensemble des nombres rationnels $\mathbb{Q}$ ?
**Correction Détaillée :**
$\mathbb{Q}$ est un ensemble dénombrable (Jalon 4). D'après la démonstration précédente, sa mesure est nulle.
**Conséquence :** Bien que les rationnels soient "partout" (denses), ils ne pèsent rien face aux irrationnels. En jetant un dard au hasard sur la droite réelle, la probabilité de tomber sur une fraction est exactement 0.

### Exercice 2 : Niveau Avancé (Invariance par translation)
**Énoncé :** Montrer que pour tout $x \in \mathbb{R}$ and $A \in \mathcal{L}(\mathbb{R})$, $\lambda(A + x) = \lambda(A)$.
**Correction Détaillée :**
Si on recouvre $A$ par des intervalles $I_n$, alors les intervalles $I_n + x$ recouvrent $A+x$. Comme $\ell(I_n + x) = \ell(I_n)$, les sommes des longueurs sont identiques. En prenant l'infimum, on obtient $\lambda^*(A+x) = \lambda^*(A)$. Comme le critère de mesurabilité est aussi préservé, la mesure de Lebesgue est invariante par translation.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, nous utilisons des **fonctions de densité de probabilité** (PDF). On dit que $f$ est la PDF d'une variable $X$ si $P(X \in A) = \int_A f(x) d\lambda(x)$. L'intégrale est prise par rapport à la mesure de Lebesgue.
- **Example Concret :**
    - **Échantillonnage (Sampling) :** Quand on génère un nombre entre 0 et 1 (ex: `random.uniform()`), l'ordinateur essaie de simuler la mesure de Lebesgue sur $[0, 1]$. La propriété de "mesure nulle" explique pourquoi on n'obtiendra jamais exactement 0.50000000... avec une précision infinie.
    - **Support des données :** Dans les modèles génératifs (GANs), on parle souvent du "support" de la distribution des données. Si les données réelles (ex: des images de haute qualité) se situent sur une variété de dimension faible, alors leur mesure de Lebesgue dans l'espace total est **nulle**. Cela explique pourquoi les fonctions de perte comme la divergence KL peuvent exploser (on essaie de diviser par zéro).
    - **Changement de variable :** Quand on transforme des données (ex: Normalisation), le Jacobien (Jalon 46) nous dit comment la mesure de Lebesgue est "étirée" ou "compressée" par la transformation.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 63 (Définition axiomatique d'une mesure).md]], [[Jalon 13 (Structure de R).md]]
- **Concepts Futurs dépendants :** [[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]], [[Jalon 73 (Définition des espaces Lp).md]]
