---
uuid: "jalon-39"
title: "Intégrales généralisées sur un intervalle quelconque"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/probabilites
prev: "[[Jalon 38 (Théorème fondamental de l'analyse).md]]"
next: "[[Jalon 40 (Intégrales dépendant d'un paramètre).md]]"
---

# Jalon 39 : Intégrales généralisées sur un intervalle quelconque

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous peignez une clôture qui s'étend à l'infini vers la droite. Plus vous avancez, plus la clôture devient basse, s'écrasant presque contre le sol. La question est : aurez-vous besoin d'une quantité infinie de peinture, ou bien un seul pot suffira-t-il pour peindre cette clôture "infinie" ? Si la hauteur de la clôture diminue assez vite (comme $1/x^2$), vous n'utiliserez qu'une quantité finie de peinture. C'est le concept d'**intégrale généralisée**.
- **Le "Pourquoi on a inventé ça" :** L'intégrale de Riemann classique ne fonctionne que sur des segments finis $[a, b]$ avec des fonctions bornées. Mais en statistiques ou en physique, on a souvent besoin de sommer des choses sur tout l'espace (de $-\infty$ à $+\infty$) ou près de points où la fonction explose (comme $1/x$ en 0). Il fallait donc étendre la définition de l'intégrale par un passage à la limite.
- **Visualisation :** On calcule l'aire jusqu'à un point $X$, puis on regarde ce qui se passe quand $X$ devient de plus en plus grand. Si l'aire se stabilise vers une valeur fixe, l'intégrale **converge**. Sinon, elle **diverge**.

## 2. Formalisation & Rigueur Académique

### A. Définitions Formelles

Soit $f : [a, b[ \to \mathbb{R}$ une fonction continue par morceaux, où $b$ peut être réel ou $+\infty$.

> **Définition 1 (Convergence) :**
> On dit que l'intégrale $\int_a^b f(t) dt$ **converge** si la fonction $X \mapsto \int_a^X f(t) dt$ admet une limite finie quand $X \to b$. Cette limite est alors notée $\int_a^b f(t) dt$. Dans le cas contraire, on dit que l'intégrale **diverge**.

> **Définition 2 (Convergence absolue) :**
> L'intégrale $\int_a^b f(t) dt$ est dite **absolument convergente** si $\int_a^b |f(t)| dt$ converge.
> *Propriété :* L'absolue convergence implique la convergence.

### B. Critères de Convergence (Fonctions Positives)

Soient $f, g$ deux fonctions positives sur $[a, b[$.

> **Critère de Comparaison :**
> Si $0 \le f \le g$ au voisinage de $b$ :
> - $\int g \text{ converge} \implies \int f \text{ converge}$.
> - $\int f \text{ diverge} \implies \int g \text{ diverge}$.

> **Intégrales de Riemann de référence :**
> 1. $\int_a^{+\infty} \frac{dt}{t^\alpha}$ converge $\iff \alpha > 1$ (avec $a > 0$).
> 2. $\int_0^a \frac{dt}{t^\alpha}$ converge $\iff \alpha < 1$ (avec $a > 0$).

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Convergence de l'intégrale de Riemann $\int_1^{+\infty} \frac{dt}{t^\alpha}$

1. **Initialisation :** Soit $f(t) = t^{-\alpha}$ sur $[1, +\infty[$. Calculons $I(X) = \int_1^X t^{-\alpha} dt$.
2. **Étape 1 : Calcul de la primitive**
   - Si $\alpha = 1$ : $I(X) = [\ln(t)]_1^X = \ln(X)$.
   - Si $\alpha \neq 1$ : $I(X) = [\frac{t^{1-\alpha}}{1-\alpha}]_1^X = \frac{X^{1-\alpha} - 1}{1-\alpha}$.
3. **Étape 2 : Passage à la limite ($X \to +\infty$)**
   - Si $\alpha = 1$ : $\ln(X) \to +\infty$, donc divergence.
   - Si $\alpha < 1$ : $1-\alpha > 0$, donc $X^{1-\alpha} \to +\infty$, donc divergence.
   - Si $\alpha > 1$ : $1-\alpha < 0$, donc $X^{1-\alpha} \to 0$. La limite est $\frac{-1}{1-\alpha} = \frac{1}{\alpha - 1}$.
4. **Conclusion :** L'intégrale converge si et seulement si $\alpha > 1$.

### Démonstration : L'absolue convergence implique la convergence

1. **Hypothèse :** $\int_a^b |f(t)| dt$ converge.
2. **Technique :** On utilise le critère de Cauchy pour les fonctions. Soit $\epsilon > 0$. Comme $\int |f|$ converge, il existe $B$ tel que pour tous $X, Y > B$ : $|\int_X^Y |f(t)| dt| < \epsilon$.
3. **Majoration :** Par l'inégalité triangulaire pour les intégrales :
   $$|\int_X^Y f(t) dt| \le \int_X^Y |f(t)| dt < \epsilon$$
4. **Conclusion :** La fonction $X \mapsto \int_a^X f(t) dt$ vérifie le critère de Cauchy en $b$, elle admet donc une limite finie.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Étude de convergence
**Énoncé :** Étudier la convergence de $I = \int_0^{+\infty} \frac{dt}{1 + t^2}$.
**Correction Détaillée :**
1. La fonction $f(t) = \frac{1}{1+t^2}$ est continue sur $[0, +\infty[$. Le seul problème est en $+\infty$.
2. Équivalent : $f(t) \sim \frac{1}{t^2}$ quand $t \to +\infty$.
3. Référence : $\int_1^{+\infty} \frac{dt}{t^2}$ est une intégrale de Riemann convergente ($\alpha = 2 > 1$).
4. Conclusion : Par critère d'équivalence pour les fonctions positives, $I$ converge.
*Note : on peut même calculer sa valeur : $[\arctan(t)]_0^{+\infty} = \pi/2$.*

### Exercice 2 : Niveau Avancé (Intégrale de Dirichlet)
**Énoncé :** Montrer que $\int_0^{+\infty} \frac{\sin(t)}{t} dt$ converge mais n'est pas absolument convergente.
**Correction Détaillée :**
* *Convergence :* On utilise une intégration par parties sur $[1, X]$ : $\int_1^X \frac{\sin(t)}{t} dt = [\frac{-\cos(t)}{t}]_1^X - \int_1^X \frac{\cos(t)}{t^2} dt$. Le terme entre crochets tend vers $\cos(1)$ et l'intégrale de droite converge absolument (car $\le 1/t^2$).
* *Non absolue convergence :* On montre que $\int_0^{n\pi} \frac{|\sin(t)|}{t} dt \ge \sum_{k=1}^n \frac{1}{k\pi} \int_{(k-1)\pi}^{k\pi} |\sin(t)| dt = \frac{2}{\pi} \sum \frac{1}{k}$, ce qui diverge (série harmonique).

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, presque toutes les distributions de probabilités continues (Normale, Cauchy, Pareto) sont définies sur des intervalles infinis. La condition pour que ces fonctions soient des densités de probabilité est que leur **intégrale généralisée sur tout l'espace soit égale à 1**.
- **Exemple Concret :**
    - **La Loi Normale (Gaussienne) :** $\int_{-\infty}^{+\infty} e^{-x^2/2} dx = \sqrt{2\pi}$. Sans la théorie des intégrales généralisées, on ne pourrait pas normaliser nos modèles.
    - **Queues de distribution (Heavy Tails) :** Dans la détection d'anomalies ou la finance, on utilise des distributions de Pareto $\frac{1}{x^{\alpha+1}}$. Si $\alpha \le 1$, l'espérance (qui est une intégrale généralisée) n'existe pas (elle diverge). Cela explique pourquoi certains risques extrêmes sont imprévisibles par les modèles classiques.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 37 (Intégrale de Riemann sur un segment).md]], [[Jalon 14 (Suites réelles et complexes).md]]
- **Concepts Futurs dépendants :** [[Jalon 40 (Intégrales dépendant d'un paramètre).md]], [[Jalon 80 (Transformée de Fourier dans L1).md]]
