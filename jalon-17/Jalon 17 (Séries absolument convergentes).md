---
uuid: "jalon-17"
title: "Séries absolument convergentes, semi-convergentes et produit de Cauchy de deux séries"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/calcul-series
prev: "[[Jalon-16.md]]"
next: "[[Jalon 18 (Continuité des fonctions d'une variable réelle).md]]"
---

# Jalon 17 : Séries absolument convergentes, semi-convergentes et produit de Cauchy de deux séries

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez que vous fassiez des pas en avant (positifs) et des pas en arrière (négatifs).
  - La **Convergence Absolue**, c'est comme si, même en transformant tous vos pas en arrière en pas en avant, la distance totale que vous parcourez restait finie. C'est une stabilité très forte : peu importe l'ordre dans lequel vous faites vos pas, vous finirez toujours au même endroit.
  - La **Semi-Convergence**, c'est un équilibre fragile. Si vous faites tous vos pas vers l'avant, vous allez à l'infini. Mais parce que vous alternez intelligemment entre avant et arrière, les distances s'annulent juste assez pour que vous restiez à un endroit précis. Si vous changez l'ordre des pas, tout s'écroule !
  - Le **Produit de Cauchy**, c'est la recette pour multiplier deux sommes infinies, comme on multiplierait deux parenthèses géantes en s'assurant de n'oublier aucun mélange de termes.
- **Le "Pourquoi on a inventé ça" :** On a besoin de manipuler des séries qui ne sont pas toujours positives. La convergence absolue est le "laissez-passer" qui permet de manipuler les séries infinies presque aussi facilement que des sommes finies (on peut changer l'ordre, regrouper, multiplier).
- **Visualisation :** Imaginez une spirale qui tourne autour d'un point central. Si la longueur totale du fil de la spirale est finie, c'est absolument convergent. Si la spirale tourne indéfiniment mais se rapproche du centre parce que les tours se compensent, c'est semi-convergent.

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Definitions Formelles
Soit $\sum u_n$ une série à termes dans $\mathbb{K}$ ($\mathbb{R}$ ou $\mathbb{C}$).
1. **Convergence Absolue :** La série $\sum u_n$ converge absolument si la série des valeurs absolues $\sum |u_n|$ converge.
2. **Semi-Convergence :** La série $\sum u_n$ est semi-convergente si elle converge, mais ne converge pas absolument.
3. **Produit de Cauchy :** Soient $\sum a_n$ et $\sum b_n$ deux séries. La série produit $\sum c_n$ est définie par le terme général :
   $$c_n = \sum_{k=0}^n a_k b_{n-k}$$

### B. Théorèmes, Propositions & Lemmes
> **Théorème de Convergence Absolue :**
> Toute série absolument convergente est convergente.
> $$\sum |u_n| \text{ converge } \implies \sum u_n \text{ converge}$$
> De plus, $|\sum_{n=0}^\infty u_n| \le \sum_{n=0}^\infty |u_n|$.

> **Théorème de Mertens (Produit de Cauchy) :**
> Si $\sum a_n$ converge absolument vers $A$ et si $\sum b_n$ converge vers $B$, alors le produit de Cauchy $\sum c_n$ converge vers $AB$.

> **Théorème de réarrangement de Riemann (Curiosité) :**
> Si $\sum u_n$ est semi-convergente, on peut changer l'ordre de ses termes pour que la nouvelle série converge vers n'importe quel réel donné, ou même diverge.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : La convergence absolue implique la convergence
Soit $\sum u_n$ une série telle que $\sum |u_n|$ converge. Montrons que $\sum u_n$ converge dans $\mathbb{R}$ (ou $\mathbb{C}$) en utilisant le critère de Cauchy.

1. **Initialisation / Cadre :** Puisque $\sum |u_n|$ converge, elle vérifie le critère de Cauchy pour les séries.
   Soit $\epsilon > 0$. Il existe $N \in \mathbb{N}$ tel que pour tous $p \ge q \ge N$ :
   $$\sum_{n=q}^p |u_n| < \epsilon$$

2. **Étape 1 : Application de l'inégalité triangulaire généralisée**
   Considérons la somme partielle de la série originale entre les indices $q$ et $p$ :
   $|\sum_{n=q}^p u_n| = |u_q + u_{q+1} + ... + u_p|$.
   Par l'inégalité triangulaire (itérée $p-q$ fois) :
   $$|u_q + ... + u_p| \le |u_q| + |u_{q+1}| + ... + |u_p|$$
   Ce qui s'écrit :
   $$|\sum_{n=q}^p u_n| \le \sum_{n=q}^p |u_n|$$

3. **Étape 2 : Majoration par $\epsilon$**
   En utilisant la condition de l'étape 1 :
   Comme $\sum_{n=q}^p |u_n| < \epsilon$, on en déduit immédiatement :
   $$|\sum_{n=q}^p u_n| < \epsilon$$

4. **Étape 3 : Conclusion sur le critère de Cauchy**
   Nous avons montré que pour tout $\epsilon > 0$, il existe $N \in \mathbb{N}$ tel que pour tous $p \ge q \ge N$, $|\sum_{n=q}^p u_n| < \epsilon$.
   La série $\sum u_n$ vérifie donc le critère de Cauchy.

5. **Conclusion :**
   Puisque $\mathbb{R}$ (ou $\mathbb{C}$) est un espace complet, toute suite de Cauchy (et donc toute série vérifiant le critère de Cauchy) converge.
   La série $\sum u_n$ est donc convergente.

## 4. Exercices d'Application & Pratique de Concours
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Série Alternée (Semi-convergence)
**Énoncé :** Étudier la convergence et la convergence absolue de la série harmonique alternée $\sum_{n=1}^\infty \frac{(-1)^n}{n}$.
**Correction Détaillée :**
1. **Convergence Absolue :** La série des valeurs absolues est $\sum |\frac{(-1)^n}{n}| = \sum \frac{1}{n}$.
   - C'est la série harmonique (Riemann $\alpha=1$). Elle diverge.
   - La série ne converge donc **pas absolument**.
2. **Convergence (Critère des séries alternées) :** Soit $u_n = \frac{(-1)^n}{n}$.
   - Posons $a_n = |u_n| = 1/n$.
   - $(a_n)$ est une suite positive, décroissante ($1/(n+1) < 1/n$) et tend vers 0.
   - D'après le théorème de Leibniz sur les séries alternées, la série $\sum u_n$ converge.
**Conclusion :** La série est **semi-convergente**.

### Exercice 2 : Niveau Avancé (Produit de Cauchy)
**Énoncé :** Soit la série exponentielle $E(x) = \sum_{n=0}^\infty \frac{x^n}{n!}$. Démontrer par produit de Cauchy que $E(x)E(y) = E(x+y)$.
**Correction Détaillée :**
1. **Convergence Absolue :** Pour tout $x \in \mathbb{R}$, $\sum \frac{x^n}{n!}$ converge absolument (d'Alembert : $\frac{|x|^{n+1}}{(n+1)!} \times \frac{n!}{|x|^n} = \frac{|x|}{n+1} \to 0$).
2. **Calcul du produit de Cauchy :** $E(x)E(y) = (\sum \frac{x^n}{n!}) (\sum \frac{y^n}{n!})$.
   - Le terme général $c_n$ est : $c_n = \sum_{k=0}^n \frac{x^k}{k!} \frac{y^{n-k}}{(n-k)!}$.
3. **Utilisation de la formule du binôme :** Multiplions et divisons par $n!$ :
   $c_n = \frac{1}{n!} \sum_{k=0}^n \frac{n!}{k!(n-k)!} x^k y^{n-k} = \frac{1}{n!} \sum_{k=0}^n \binom{n}{k} x^k y^{n-k}$.
   - D'après le binôme de Newton : $\sum_{k=0}^n \binom{n}{k} x^k y^{n-k} = (x+y)^n$.
4. **Réassemblage :** $c_n = \frac{(x+y)^n}{n!}$.
**Conclusion :** $\sum c_n = \sum \frac{(x+y)^n}{n!} = E(x+y)$. L'identité est prouvée.

## 5. Ancrage & Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** En IA, les séries absolument convergentes garantissent la stabilité des **Noyaux de Convolution** infinis et des **Séries Temporelles**.
- **Exemple Concret :** Dans le **Traitement du Signal (Audio/Image)**, on utilise souvent des filtres dont la réponse impulsionnelle est infinie (filtres IIR). Pour que le filtre soit stable (qu'il n'amplifie pas le bruit à l'infini), la série de ses coefficients doit être **absolument convergente**. De même, le produit de Cauchy est l'opération fondamentale derrière la **Convolution Discrète** de deux signaux. Si vous multipliez deux polynômes de prédiction (utilisés dans les modèles ARMA), vous effectuez un produit de Cauchy.

## 6. Liens Sémantiques & Maillage Obsidian
- **Concepts Précédents requis :** [[Jalon 14 (Suites réelles et complexes)]], [[Jalon-16]]
- **Concepts Futurs dépendants :** [[Jalon 23 (Séries entières)]], [[Jalon 80 (Transformée de Fourier dans L^1)]], [[Jalon 126 (Noyaux définis positifs)]]
