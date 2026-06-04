---
uuid: "jalon-22"
title: "Séries de fonctions, convergence normale, théorèmes d'interversion limite-intégrale et limite-dérivée"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/convergence-series
prev: "[[Jalon 21 (Suites de fonctions).md]]"
next: "[[Jalon 23 (Séries entières).md]]"
---

# Jalon 22 : Séries de fonctions, convergence normale, théorèmes d'interversion limite-intégrale et limite-dérivée

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez que vous construisiez un orchestre virtuel. Chaque musicien joue une note (une fonction). La **Série de fonctions**, c'est le son global produit par l'orchestre quand tous les musiciens jouent en même temps. 
  - La **Convergence Normale**, c'est comme si chaque musicien jouait de moins en moins fort selon une règle stricte, de sorte que même si vous aviez un nombre infini de musiciens, le volume sonore total resterait agréable et ne vous exploserait pas les oreilles. C'est la forme de convergence la plus "sûre".
  - Les **Théorèmes d'Interversion**, c'est la question : "Est-ce que le son global de l'orchestre (la somme) est le même que si j'enregistrais chaque musicien séparément puis que je mixais le tout (l'intégrale ou la dérivée) ?" La réponse est OUI, si l'orchestre est bien discipliné (si la convergence est uniforme ou normale).
- **Le "Pourquoi on a inventé ça" :** De nombreux signaux complexes (comme la voix humaine) ne sont pas des fonctions simples, mais des sommes infinies de fonctions simples (des ondes). Pour manipuler ces signaux (les filtrer, les compresser), on doit savoir quand on a le droit d'échanger l'ordre des opérations mathématiques.
- **Visualisation :** Imaginez empiler des couches de calque transparents. Chaque calque a un dessin. La série est l'image finale vue par transparence. La convergence normale garantit que l'image finale n'est pas un gribouillis illisible.

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $\sum u_n(x)$ une série de fonctions définies sur $D \subset \mathbb{R}$.
1. **Convergence Simple (CS) :** La série converge simplement si pour tout $x \in D$, la série numérique $\sum u_n(x)$ converge. On note $S(x) = \sum_{n=0}^\infty u_n(x)$.
2. **Convergence Uniforme (CU) :** La série converge uniformément si la suite des sommes partielles $S_N(x) = \sum_{n=0}^N u_n(x)$ converge uniformément vers $S(x)$ sur $D$.
3. **Convergence Normale (CN) :** La série converge normalement sur $D$ si la série numérique des supremums converge :
   $$\sum_{n=0}^\infty \|u_n\|_\infty \text{ converge, où } \|u_n\|_\infty = \sup_{x \in D} |u_n(x)|$$

### B. Théorèmes, Propositions & Lemmes
> **Hiérarchie des convergences :**
> Convergence Normale $\implies$ Convergence Uniforme $\implies$ Convergence Simple.
> (La réciproque est fausse).

> **Théorème de Continuité :**
> Si chaque $u_n$ est continue et si la série $\sum u_n$ converge **uniformément**, alors la somme $S$ est continue.

> **Théorème d'Interversion $\sum$ et $\int$ :**
> Si $\sum u_n$ converge uniformément vers $S$ sur $[a, b]$ et si les $u_n$ sont continues, alors :
> $$\int_a^b \left( \sum_{n=0}^\infty u_n(t) \right) dt = \sum_{n=0}^\infty \int_a^b u_n(t) dt$$

> **Théorème d'Interversion $\sum$ et Dérivation :**
> Si les $u_n$ sont de classe $C^1$, si $\sum u_n(x_0)$ converge, et si $\sum u'_n$ converge **uniformément**, alors $S$ est de classe $C^1$ et $S' = \sum u'_n$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : La convergence normale implique la convergence uniforme
Soit $\sum u_n$ une série de fonctions convergeant normalement sur $D$. Montrons qu'elle converge uniformément.

1. **Initialisation / Cadre :** 
   - Par hypothèse, la série numérique $\sum \alpha_n$ converge, où $\alpha_n = \sup_{x \in D} |u_n(x)|$.
   - Nous voulons montrer que la suite des sommes partielles $S_N(x) = \sum_{n=0}^N u_n(x)$ vérifie le critère de Cauchy uniforme.

2. **Étape 1 : Application du critère de Cauchy numérique**
   Soit $\epsilon > 0$. Comme $\sum \alpha_n$ converge, elle est de Cauchy.
   Il existe $N \in \mathbb{N}$ tel que pour tous $p \ge q \ge N$ :
   $$\sum_{n=q}^p \alpha_n < \epsilon$$

3. **Étape 2 : Majoration du reste de la série de fonctions**
   Pour tout $x \in D$ and pour tout $p \ge q \ge N$, considérons l'écart entre deux sommes partielles :
   $|S_p(x) - S_{q-1}(x)| = |\sum_{n=q}^p u_n(x)|$.
   Par l'inégalité triangulaire :
   $$|\sum_{n=q}^p u_n(x)| \le \sum_{n=q}^p |u_n(x)|$$
   Par définition du supremum $\|u_n\|_\infty = \alpha_n$, on a $|u_n(x)| \le \alpha_n$ pour tout $x \in D$.
   D'où :
   $$|\sum_{n=q}^p u_n(x)| \le \sum_{n=q}^p \alpha_n$$

4. **Étape 3 : Passage au supremum**
   En utilisant la majoration de l'étape 1, on a pour tout $x \in D$ :
   $|S_p(x) - S_{q-1}(x)| < \epsilon$.
   Comme cette majoration est indépendante de $x$, on peut passer au supremum sur $D$ :
   $$\sup_{x \in D} |S_p(x) - S_{q-1}(x)| \le \sum_{n=q}^p \alpha_n < \epsilon$$

5. **Conclusion :**
   La suite $(S_N)$ vérifie le critère de Cauchy uniforme sur $D$. Puisque l'espace des fonctions bornées sur $D$ muni de la norme $\| \cdot \|_\infty$ est complet, la série converge uniformément.

## 4. Exercices d'Application & Pratique de Concours
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Étude de convergence normale
**Énoncé :** Étudier la convergence de la série $\sum_{n=1}^\infty \frac{\sin(nx)}{n^2}$ sur $\mathbb{R}$.
**Correction Détaillée :**
1. **Terme général :** $u_n(x) = \frac{\sin(nx)}{n^2}$.
2. **Calcul de la norme infini :** On sait que $|\sin(nx)| \le 1$ pour tout $x$.
   - Donc $|u_n(x)| \le \frac{1}{n^2}$.
   - Le supremum est atteint (par exemple en $x = \frac{\pi}{2n}$).
   - $\|u_n\|_\infty = \frac{1}{n^2}$.
3. **Série des normes :** $\sum \|u_n\|_\infty = \sum \frac{1}{n^2}$.
   - C'est une série de Riemann convergente ($\alpha = 2 > 1$).
**Conclusion :** La série converge normalement (et donc uniformément) sur $\mathbb{R}$. Sa somme est une fonction continue.

### Exercice 2 : Niveau Avancé (Somme d'une série et interversion)
**Énoncé :** Justifier que $\int_0^1 \sum_{n=1}^\infty \frac{x^n}{n^2} dx = \sum_{n=1}^\infty \frac{1}{n^2(n+1)}$.
**Correction Détaillée :**
1. **Hypothèses :** Soit $u_n(x) = \frac{x^n}{n^2}$.
   - Sur $[0, 1]$, $\|u_n\|_\infty = u_n(1) = 1/n^2$.
   - La série $\sum u_n$ converge normalement sur $[0, 1]$.
2. **Interversion :** Comme il y a convergence uniforme, on peut intervertir $\int$ et $\sum$.
   - $\int_0^1 (\sum u_n(x)) dx = \sum \int_0^1 \frac{x^n}{n^2} dx$.
3. **Calcul de l'intégrale :**
   - $\int_0^1 \frac{x^n}{n^2} dx = \frac{1}{n^2} [ \frac{x^{n+1}}{n+1} ]_0^1 = \frac{1}{n^2(n+1)}$.
**Conclusion :** L'égalité est justifiée par la convergence normale de la série sur le segment d'intégration.

## 5. Ancrage & Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** Les séries de fonctions sont le fondement de l'**Analyse Harmonique** et des **Séries de Fourier**. Tout signal complexe (audio, série temporelle boursière) est décomposé en une série de fonctions sinus et cosinus.
- **Exemple Concret :** Dans la **Compression de Données (Spectrogrammes)** et les **Réseaux de Neurones Récurrents (RNN)**, on manipule des sommes infinies pour modéliser des dépendances temporelles. La convergence normale garantit que si on ajoute de plus en plus de détails (harmoniques) pour reconstruire un son, le signal résultant ne diverge pas et reste "écoutable" (physiquement possible). Les théorèmes d'interversion permettent de dériver ces séries pour calculer la vitesse de changement d'un signal (fréquence instantanée).

## 6. Liens Sémantiques & Maillage Obsidian
- **Concepts Précédents requis :** [[Jalon 16 (Séries numériques à termes positifs)]], [[Jalon 21 (Suites de fonctions)]]
- **Concepts Futurs dépendants :** [[Jalon 23 (Séries entières)]], [[Jalon 78 (Séries de Fourier)]], [[Jalon 80 (Transformée de Fourier dans L^1)]]
