---
uuid: "jalon-79"
title: "Convergence L2 et Identité de Parseval"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/traitement-du-signal
prev: "[[Jalon 78 (Séries de Fourier).md]]"
next: "[[Jalon 80 (Transformée de Fourier dans L1).md]]"
---

# Jalon 79 : Convergence $L^2$ et Identité de Parseval

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous démontiez une voiture pour la vendre en pièces détachées.
    - La voiture entière a un certain poids ($L^2$ norme du signal).
    - Vous la démontez en moteurs, roues, boulons (les coefficients de Fourier $c_n$).
    - L'**Identité de Parseval**, c'est simplement dire que le poids de la voiture entière est exactement égal à la somme des poids de toutes les pièces détachées. Rien ne s'est perdu pendant le démontage.
    - En sciences, cela veut dire que l'**énergie** d'un son peut être calculée soit en regardant le son lui-même, soit en additionnant l'énergie de chaque note pure qui le compose.
- **Le "Pourquoi on a inventé ça" :** Parfois, on ne sait pas calculer l'intégrale d'une fonction complexe. Mais si on connaît ses fréquences, on peut trouver la réponse par une simple somme. Inversement, cela permet de calculer des sommes infinies de nombres en utilisant des intégrales. C'est le pont final qui prouve que la décomposition de Fourier est "parfaite" dans le monde de l'énergie ($L^2$).
- **Visualisation :** Un graphique où l'aire sous la courbe (énergie temporelle) est égale à la somme des hauteurs de bâtons dans un spectre (énergie fréquentielle).

## 2. Formalisation

Soit $f \in L^2([0, 2\pi])$ une fonction $2\pi$-périodique.

### A. Théorème de convergence en moyenne quadratique

> **Théorème :**
> La série de Fourier d'une fonction $f \in L^2$ converge vers $f$ au sens de la norme $L^2$ :
> $$\lim_{N \to \infty} \| f - S_N(f) \|_2 = 0$$
> Autrement dit, $\lim_{N \to \infty} \int_0^{2\pi} | f(t) - \sum_{n=-N}^N c_n e^{int} |^2 dt = 0$.

### B. L'Identité de Parseval

> **Théorème (Identité de Parseval) :**
> Pour toute fonction $f \in L^2([0, 2\pi])$, on a :
> $$\frac{1}{2\pi} \int_0^{2\pi} |f(t)|^2 dt = \sum_{n=-\infty}^{+\infty} |c_n(f)|^2$$
> En version réelle avec $a_n, b_n$ :
> $$\frac{1}{2\pi} \int_0^{2\pi} |f(t)|^2 dt = \frac{a_0^2}{4} + \frac{1}{2} \sum_{n=1}^\infty (a_n^2 + b_n^2)$$

## 3. Démonstrations

### Démonstration de l'Identité de Parseval (Cadre Hilbertien)

1. **Structure de Hilbert :** On travaille dans l'espace de Hilbert $H = L^2([0, 2\pi])$ muni du produit scalaire $\langle f, g \rangle = \frac{1}{2\pi} \int_0^{2\pi} f \bar{g}$.
2. **Base orthonormée :** On sait que la famille $e_n(t) = e^{int}$ est une famille orthonormée de $H$. On admet qu'elle est **totale** (son adhérence est $H$, voir Jalon 77 sur la densité).
3. **Projection orthogonale :** La somme partielle $S_N(f) = \sum_{n=-N}^N c_n e_n$ est la projection orthogonale de $f$ sur le sous-espace $H_N = \text{vect}(e_{-N}, \dots, e_N)$.
4. **Pythagore infini :** Comme la famille est une base hilbertienne, pour tout $f \in H$ :
   $f = \sum_{n=-\infty}^{+\infty} \langle f, e_n \rangle e_n$.
5. **Calcul de la norme :**
   $$\|f\|^2 = \langle f, f \rangle = \langle \sum_n c_n e_n, \sum_m c_m e_m \rangle = \sum_n \sum_m c_n \bar{c}_m \langle e_n, e_m \rangle$$
6. **Utilisation de l'orthonormalité :** Comme $\langle e_n, e_m \rangle = \delta_{nm}$, tous les termes de la double somme s'annulent sauf quand $n=m$.
7. **Conclusion :** $\|f\|^2 = \sum_{n=-\infty}^{+\infty} |c_n|^2$.

## 4. Exercices d'Application

### Exercice 1 : Calcul de la somme de Bâle ($\sum 1/n^2$)
**Énoncé :** Utiliser la série de Fourier de $f(t) = t$ sur $]-\pi, \pi]$ pour calculer $\sum_{n=1}^\infty \frac{1}{n^2}$.
**Correction Détaillée :**
1. **Calcul de la norme :** $\frac{1}{2\pi} \int_{-\pi}^\pi t^2 dt = \frac{1}{2\pi} [\frac{t^3}{3}]_{-\pi}^\pi = \frac{1}{2\pi} \frac{2\pi^3}{3} = \frac{\pi^2}{3}$.
2. **Coefficients :** On a calculé au Jalon 78 que $a_n=0$ et $b_n = \frac{2(-1)^{n+1}}{n}$. Pour $n \ge 1$, $|c_n|^2 + |c_{-n}|^2 = \frac{1}{2}(a_n^2 + b_n^2) = \frac{1}{2}(0 + \frac{4}{n^2}) = \frac{2}{n^2}$. $a_0 = 0$.
3. **Parseval :** $\frac{\pi^2}{3} = 0 + \sum_{n=1}^\infty \frac{2}{n^2}$.
4. **Résultat :** $\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$.

### Exercice 2 : Niveau Avancé (Inégalité de Wirtinger)
**Énoncé :** Soit $f$ de classe $\mathcal{C}^1$ sur $[0, 2\pi]$ telle que $f(0)=f(2\pi)$ et $\int_0^{2\pi} f(t) dt = 0$. Montrer que $\int_0^{2\pi} |f(t)|^2 dt \le \int_0^{2\pi} |f'(t)|^2 dt$.
**Correction Détaillée :**
On utilise les coefficients de Fourier. $c_n(f') = i n c_n(f)$.
Par Parseval : $\int |f'|^2 = \sum n^2 |c_n|^2$ et $\int |f|^2 = \sum |c_n|^2$.
Comme $\int f = 0$, alors $c_0 = 0$. Pour $n \neq 0$, $n^2 \ge 1$, donc $\sum n^2 |c_n|^2 \ge \sum |c_n|^2$.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** Parseval est la raison pour laquelle on peut entraîner des modèles dans le domaine fréquentiel. L'erreur quadratique (MSE) est la même, qu'on la calcule sur les pixels ou sur les fréquences.
- **Example Concret :**
    - **Filtrage Passe-bas (Low-pass) :** En compressant une image, on supprime les hautes fréquences (petits $|c_n|$). Parseval nous dit exactement quel pourcentage de l'énergie (donc de l'information visuelle) on a perdu en faisant cette coupure.
    - **Analyse du Bruit :** Le bruit blanc a des coefficients de Fourier de même amplitude en moyenne. Parseval permet de calculer le rapport Signal/Bruit (SNR) de manière très efficace.
    - **Audio Generation (Diff-Wave) :** Les modèles de diffusion pour l'audio travaillent souvent sur des représentations de Fourier. La fonction de perte est définie dans l'espace fréquentiel, et Parseval garantit que minimiser cette perte revient à minimiser l'erreur sur l'onde sonore réelle.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 78 (Séries de Fourier).md]], [[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L2).md]]
- **Concepts Futurs dépendants :** [[Jalon 81 (Transformée de Fourier dans L2).md]], [[Jalon 116 (Variétés riemanniennes).md]]
