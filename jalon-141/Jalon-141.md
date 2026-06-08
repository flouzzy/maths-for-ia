---
uuid: "jalon-141"
title: "Théorèmes de Glivenko-Cantelli généralisés pour les classes de fonctions VC."
year: 3
trimester: 12
tags:
  - math/fondations
  - ia/theorie
prev: "[[Jalon-140.md]]"
next: "[[Jalon-142.md]]"
---

# Jalon 141 : Théorèmes de Glivenko-Cantelli généralisés pour les classes de fonctions VC.

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*
- **La Métaphore :** Imaginez que vous observez une forêt gigantesque et que vous essayez d'estimer la proportion de chênes. Si vous prenez un petit échantillon d'arbres, votre estimation sera approximative. Si vous en prenez un très grand nombre, votre estimation va se rapprocher de la vraie proportion. Le théorème de Glivenko-Cantelli nous dit que, peu importe la forme de la forêt, cette convergence est garantie et uniforme pour des classes de "questions" pas trop complexes (mesurées par la dimension VC).
- **Le "Pourquoi on a inventé ça" :** En apprentissage statistique, on veut s'assurer que si notre modèle est bon sur les données d'entraînement (le risque empirique est faible), il sera aussi bon sur des données invisibles (le risque réel sera faible). On avait besoin d'un outil pour prouver que, pour des familles de modèles "raisonnables", l'erreur empirique converge uniformément vers l'erreur réelle.
- **Visualisation :** Visualisez deux courbes : la courbe de l'erreur empirique (calculée sur l'échantillon) et la courbe de l'erreur réelle (inconnue mais théorique) en fonction de la complexité du modèle. Le théorème garantit que l'écart maximal entre ces deux courbes se resserre inéluctablement vers zéro au fur et à mesure que la taille de l'échantillon augmente, formant un "tube de confiance" de plus en plus fin.

## 2. Formalisation & Rigueur Académique

### A. Définitions Formelles
Soit $(\mathcal{Z}, \mathcal{F})$ un espace mesurable. Soit $\mathcal{P}$ une distribution de probabilité sur $\mathcal{Z}$.
Soit $S = (Z_1, \dots, Z_n)$ un échantillon de variables aléatoires indépendantes et identiquement distribuées selon $\mathcal{P}$.
Soit $\mathcal{H}$ une classe de fonctions $h: \mathcal{Z} \to \{0, 1\}$.

Pour chaque $h \in \mathcal{H}$, on définit l'espérance (ou risque réel) par :
$$ R(h) = \mathbb{E}_{Z \sim \mathcal{P}}[h(Z)] $$

Et on définit la moyenne empirique (ou risque empirique) par :
$$ R_n(h) = \frac{1}{n} \sum_{i=1}^n h(Z_i) $$

La classe $\mathcal{H}$ est dite une **classe de Glivenko-Cantelli (GC)** pour $\mathcal{P}$ si :
$$ \lim_{n \to \infty} \sup_{h \in \mathcal{H}} |R_n(h) - R(h)| = 0 \quad \text{presque sûrement.} $$
Elle est dite classe de **Glivenko-Cantelli universelle** si cette propriété est vraie pour toute distribution de probabilité $\mathcal{P}$.

### B. Théorèmes, Propositions & Lemmes
> **Théorème de Glivenko-Cantelli (Version Classique) :**
> Soit $\mathcal{Z} = \mathbb{R}$ et $\mathcal{H} = \{ z \mapsto \mathbb{I}_{z \le t} \mid t \in \mathbb{R} \}$. Soit $F(t) = \mathcal{P}(Z \le t)$ la fonction de répartition réelle et $F_n(t) = \frac{1}{n} \sum_{i=1}^n \mathbb{I}_{Z_i \le t}$ la fonction de répartition empirique. Alors :
> $$ \lim_{n \to \infty} \sup_{t \in \mathbb{R}} |F_n(t) - F(t)| = 0 \quad \text{presque sûrement.} $$

> **Théorème de Glivenko-Cantelli Généralisé (Vapnik-Chervonenkis) :**
> Soit $\mathcal{H}$ une classe de fonctions à valeurs dans $\{0, 1\}$. La classe $\mathcal{H}$ est une classe de Glivenko-Cantelli universelle si et seulement si sa dimension de Vapnik-Chervonenkis (dimension VC) est finie :
> $$ \text{VCdim}(\mathcal{H}) < \infty $$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration du Théorème Pivot : Condition suffisante de Glivenko-Cantelli via la dimension VC

1. **Initialisation / Cadre :**
Nous allons démontrer que si $\text{VCdim}(\mathcal{H}) = d < \infty$, alors $\mathcal{H}$ est une classe GC universelle.
Nous utiliserons la borne de Vapnik-Chervonenkis (démontrée dans les jalons précédents) qui stipule que, pour tout $\epsilon > 0$ :
$$ \mathbb{P}\left( \sup_{h \in \mathcal{H}} |R_n(h) - R(h)| > \epsilon \right) \le 4 \Pi_{\mathcal{H}}(2n) \exp\left(-\frac{n \epsilon^2}{8}\right) $$
où $\Pi_{\mathcal{H}}(m)$ est la fonction de croissance de la classe $\mathcal{H}$.

2. **Étape 1 : Application du Lemme de Sauer-Shelah :**
Puisque $\text{VCdim}(\mathcal{H}) = d < \infty$, le Lemme de Sauer-Shelah nous donne une borne polynomiale sur la fonction de croissance :
$$ \forall m \ge d, \quad \Pi_{\mathcal{H}}(m) \le \left(\frac{em}{d}\right)^d $$
En injectant cela dans la borne de probabilité pour $2n \ge d$, nous obtenons :
$$ \mathbb{P}\left( \sup_{h \in \mathcal{H}} |R_n(h) - R(h)| > \epsilon \right) \le 4 \left(\frac{2en}{d}\right)^d \exp\left(-\frac{n \epsilon^2}{8}\right) $$

3. **Étape 2 (Transition micro-calculatoire) : Étude de la série :**
Pour prouver la convergence presque sûre, nous voulons utiliser le lemme de Borel-Cantelli. Nous devons donc montrer que la série des probabilités est convergente pour tout $\epsilon > 0$.
Posons $A_n(\epsilon) = \left\{ \sup_{h \in \mathcal{H}} |R_n(h) - R(h)| > \epsilon \right\}$.
Nous considérons la série :
$$ \sum_{n=1}^\infty \mathbb{P}(A_n(\epsilon)) \le \sum_{n=1}^\infty 4 \left(\frac{2en}{d}\right)^d \exp\left(-\frac{n \epsilon^2}{8}\right) $$
Le terme général de cette série est de la forme $C \cdot n^d \cdot \alpha^n$ avec $C = 4(2e/d)^d$ et $\alpha = \exp(-\epsilon^2/8)$.
Puisque $\epsilon > 0$, nous avons $\epsilon^2/8 > 0$ et donc $\alpha < 1$.
Une série dont le terme général est le produit d'un polynôme en $n$ et d'une exponentielle décroissante $\alpha^n$ (avec $0 < \alpha < 1$) est toujours convergente. En effet, par le critère de d'Alembert :
$$ \lim_{n \to \infty} \frac{(n+1)^d \alpha^{n+1}}{n^d \alpha^n} = \lim_{n \to \infty} \left(\frac{n+1}{n}\right)^d \alpha = 1^d \cdot \alpha = \alpha < 1 $$
Ainsi, la série converge :
$$ \sum_{n=1}^\infty \mathbb{P}(A_n(\epsilon)) < \infty $$

4. **Conclusion :**
Puisque la série des probabilités converge pour tout $\epsilon > 0$, le premier lemme de Borel-Cantelli affirme que la probabilité que l'événement $A_n(\epsilon)$ se réalise une infinité de fois est nulle :
$$ \mathbb{P}\left(\limsup_{n \to \infty} A_n(\epsilon)\right) = 0 $$
Autrement dit, avec probabilité 1, il existe un rang $N$ à partir duquel $\sup_{h \in \mathcal{H}} |R_n(h) - R(h)| \le \epsilon$.
Comme cela est vrai pour tout $\epsilon > 0$ rationnel (union dénombrable d'ensembles de mesure 1), nous concluons que :
$$ \mathbb{P}\left( \lim_{n \to \infty} \sup_{h \in \mathcal{H}} |R_n(h) - R(h)| = 0 \right) = 1 $$
Ceci montre exactement que la classe $\mathcal{H}$ est de Glivenko-Cantelli universelle, achevant la démonstration.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Application Directe
**Énoncé :** Soit $\mathcal{X} = \mathbb{R}$ et $\mathcal{H}$ la classe des intervalles de la forme $(-\infty, a]$ pour $a \in \mathbb{R}$. Montrer que $\mathcal{H}$ est une classe de Glivenko-Cantelli en calculant sa dimension VC.

**Correction Détaillée :**
* *Analyse de l'énoncé :* On doit trouver la dimension VC de la classe des demi-droites réelles gauches.
* *Résolution pas-à-pas :*
  1. Considérons un ensemble d'un point $\{x_1\}$. L'éclatement de cet ensemble est immédiat. Pour avoir le label 1, on choisit $a = x_1$. Pour avoir le label 0, on choisit $a < x_1$. Donc $\text{VCdim}(\mathcal{H}) \ge 1$.
  2. Considérons un ensemble de deux points distincts $\{x_1, x_2\}$ avec $x_1 < x_2$.
  3. Essayons d'obtenir l'étiquetage $(0, 1)$ sur $(x_1, x_2)$. Cela exigerait que l'intervalle $(-\infty, a]$ ne contienne pas $x_1$ mais contienne $x_2$. Donc $x_1 > a$ et $x_2 \le a$. Cela implique $x_1 > x_2$, ce qui contredit notre hypothèse $x_1 < x_2$.
  4. Par conséquent, aucun ensemble de 2 points ne peut être éclaté par $\mathcal{H}$.
  5. Donc $\text{VCdim}(\mathcal{H}) = 1$.
  6. Puisque la dimension VC est finie (1 < $\infty$), le théorème généralisé stipule que $\mathcal{H}$ est une classe de Glivenko-Cantelli universelle. Cela correspond exactement au Théorème de Glivenko-Cantelli classique sur la convergence de la fonction de répartition empirique.

### Exercice 2 : Niveau Avancé (Inspiré Concours X / ENS / MIT)
**Énoncé :** Soit $\mathcal{H}_1$ et $\mathcal{H}_2$ deux classes de fonctions de Glivenko-Cantelli sur un même espace. On définit la classe union $\mathcal{H} = \mathcal{H}_1 \cup \mathcal{H}_2$. Démontrer, en utilisant uniquement la définition de limite uniforme presque sûre, que $\mathcal{H}$ est également une classe de Glivenko-Cantelli.

**Correction Détaillée :**
* *Analyse de l'énoncé :* On ne passe pas par la dimension VC ici, mais par une manipulation de la borne supérieure (le sup) sur des ensembles.
* *Résolution pas-à-pas :*
  1. Par hypothèse, nous savons que :
     $$ \lim_{n \to \infty} \sup_{h \in \mathcal{H}_1} |R_n(h) - R(h)| = 0 \quad \text{p.s.} $$
     $$ \lim_{n \to \infty} \sup_{h \in \mathcal{H}_2} |R_n(h) - R(h)| = 0 \quad \text{p.s.} $$
  2. Soit $\Omega_1$ l'ensemble de probabilité 1 où la première limite est vraie, et $\Omega_2$ l'ensemble de probabilité 1 où la deuxième limite est vraie.
  3. L'intersection $\Omega' = \Omega_1 \cap \Omega_2$ est aussi de probabilité 1 (car l'intersection de deux événements presque sûrs est presque sûre : $\mathbb{P}(\Omega_1 \cap \Omega_2) = 1 - \mathbb{P}(\Omega_1^c \cup \Omega_2^c) \ge 1 - (0 + 0) = 1$).
  4. Pour tout $\omega \in \Omega'$, évaluons la borne supérieure sur la classe union $\mathcal{H}$ :
     $$ \sup_{h \in \mathcal{H}_1 \cup \mathcal{H}_2} |R_n(h) - R(h)| = \max \left( \sup_{h \in \mathcal{H}_1} |R_n(h) - R(h)|, \sup_{h \in \mathcal{H}_2} |R_n(h) - R(h)| \right) $$
  5. Soit $\epsilon > 0$. Puisque $\omega \in \Omega_1$, il existe $N_1$ tel que pour tout $n \ge N_1$, $\sup_{h \in \mathcal{H}_1} |R_n(h) - R(h)| \le \epsilon$.
  6. Puisque $\omega \in \Omega_2$, il existe $N_2$ tel que pour tout $n \ge N_2$, $\sup_{h \in \mathcal{H}_2} |R_n(h) - R(h)| \le \epsilon$.
  7. Posons $N = \max(N_1, N_2)$. Pour tout $n \ge N$, nous avons simultanément :
     $$ \sup_{h \in \mathcal{H}_1} |R_n(h) - R(h)| \le \epsilon \quad \text{et} \quad \sup_{h \in \mathcal{H}_2} |R_n(h) - R(h)| \le \epsilon $$
  8. Par conséquent, pour tout $n \ge N$ :
     $$ \max \left( \sup_{h \in \mathcal{H}_1} |R_n(h) - R(h)|, \sup_{h \in \mathcal{H}_2} |R_n(h) - R(h)| \right) \le \epsilon $$
  9. Ceci prouve que $\lim_{n \to \infty} \sup_{h \in \mathcal{H}} |R_n(h) - R(h)| = 0$ sur $\Omega'$.
  10. Puisque $\mathbb{P}(\Omega') = 1$, on conclut que $\mathcal{H}$ est une classe de Glivenko-Cantelli.

## 5. Ancrage & Application en Intelligence Artificielle
- **Le Pont Théorique :** Le théorème de Glivenko-Cantelli généralisé est la pierre angulaire de la théorie de l'apprentissage. Il garantit que l'apprentissage est possible (PAC-apprenabilité). Si l'on choisit un modèle dans une classe de complexité finie (dimension VC finie), l'optimisation de la perte empirique (par exemple la descente de gradient sur les données d'entraînement) convergera asymptotiquement vers l'optimisation de la véritable perte de test. C'est l'assurance-vie mathématique qui justifie pourquoi on s'acharne à minimiser l'erreur d'entraînement.
- **Exemple Concret :** Dans la conception d'un classifieur linéaire (comme une SVM sans noyau) en dimension $d$, on sait que la classe d'hypothèses $\mathcal{H}$ a une dimension VC de $d+1$. Cette finitude implique, via Glivenko-Cantelli, que pour tout $\epsilon$, il existe une taille de dataset $N$ au-delà de laquelle l'erreur d'entraînement de la SVM reflètera fidèlement son erreur en production. L'algorithme d'apprentissage n'est plus "aveugle".

## 6. Liens Sémantiques & Maillage Obsidian
- **Concepts Précédents requis :** [[Jalon-136.md]], [[Jalon-140.md]]
- **Concepts Futurs dépendants :** [[Jalon-142.md]], [[Jalon-144.md]]
