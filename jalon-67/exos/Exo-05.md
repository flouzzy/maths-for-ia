# Exercice 5 : Théorème de Beppo Levi sur l'espace des suites (l1)

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
L'espace $\ell^1(\mathbb{N})$ est l'espace des suites réelles sommables. On considère $\mathbb{N}$ muni de la tribu discrète $\mathcal{P}(\mathbb{N})$ et de la mesure de comptage $\mu$.
Montrer rigoureusement l'interversion de limites pour une suite double positive $a_{i,j} \ge 0$ :
$$\lim_{n \to \infty} \sum_{i=0}^\infty a_{i,n} = \sum_{i=0}^\infty \lim_{n \to \infty} a_{i,n}$$
en supposant que pour tout $i$, la suite $(a_{i,n})_{n}$ est croissante.

**Solution Détaillée :**
1. L'intégration sur $\mathbb{N}$ avec la mesure de comptage équivaut formellement à la sommation infinie.
Précisément, pour une fonction $f: \mathbb{N} \to \mathbb{R}^+$, $\int_{\mathbb{N}} f d\mu = \sum_{i=0}^\infty f(i)$.

2. Nous définissons une suite de fonctions sur $\mathbb{N}$ : $f_n(i) = a_{i,n}$.
- Ces fonctions sont positives : $f_n(i) \ge 0$.
- La suite de fonctions est croissante : par hypothèse, pour tout $i$, la suite $(a_{i,n})$ est croissante, donc $f_n(i) \le f_{n+1}(i)$.
- Les fonctions $f_n$ sont trivialement mesurables car la tribu est $\mathcal{P}(\mathbb{N})$.

3. La fonction limite simple est $f(i) = \lim_{n \to \infty} a_{i,n}$, qui existe (éventuellement $+\infty$) car la suite est croissante.

4. On applique le Théorème de Convergence Monotone de Beppo Levi :
$$\lim_{n \to \infty} \int_{\mathbb{N}} f_n d\mu = \int_{\mathbb{N}} f d\mu$$

5. En traduisant cela avec le symbole somme, nous obtenons exactement le résultat :
$$\lim_{n \to \infty} \sum_{i=0}^\infty a_{i,n} = \sum_{i=0}^\infty \lim_{n \to \infty} a_{i,n}$$
Ceci démontre que le TCM n'est pas limité à l'intégrale de Lebesgue classique sur $\mathbb{R}$, mais s'applique à toute théorie de la mesure, couvrant ainsi l'analyse discrète de manière unifiée.
