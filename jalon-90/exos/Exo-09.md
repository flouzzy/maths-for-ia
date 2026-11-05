# Exercice 9 : La méthode de sous-suite de Riesz

Niveau : $\bigstar\bigstar\bigstar\bigstar\bigstar$

Montrer que si $X_n \xrightarrow{\mathbb{P}} X$, alors il existe une sous-suite $(X_{\varphi(k)})_{k \in \mathbb{N}}$ strictement croissante telle que $X_{\varphi(k)} \xrightarrow{\text{p.s.}} X$ quand $k \to +\infty$.

## Correction

L'idée (due à F. Riesz) est de sélectionner une sous-suite qui converge "très vite" en probabilité pour pouvoir appliquer le lemme de Borel-Cantelli.
Par définition de la convergence en probabilité, pour tout $\varepsilon > 0$, $\lim_{n \to \infty} \mathbb{P}(|X_n - X| > \varepsilon) = 0$.
Pour chaque entier $k \ge 1$, appliquons cette définition avec $\varepsilon_k = \frac{1}{k}$. La probabilité tend vers 0, donc il existe un rang (notons-le $\varphi(k)$) tel que pour tout $n \ge \varphi(k)$, on a :
$$\mathbb{P}\left(|X_n - X| > \frac{1}{k}\right) \le \frac{1}{2^k}$$
Pour s'assurer que $\varphi$ est strictement croissante, on construit la suite par récurrence en choisissant $\varphi(k+1) > \varphi(k)$.
Définissons les événements $A_k = \left\{ |X_{\varphi(k)} - X| > \frac{1}{k} \right\}$.
Par construction, on a $\mathbb{P}(A_k) \le \frac{1}{2^k}$.
La série géométrique $\sum \frac{1}{2^k}$ est convergente. Ainsi, la série des probabilités $\sum \mathbb{P}(A_k)$ converge.
D'après le lemme de Borel-Cantelli, la probabilité que l'événement $A_k$ se réalise pour une infinité d'indices $k$ est nulle :
$$\mathbb{P}(\limsup A_k) = 0$$
Donc, presque sûrement, les événements $A_k$ ne se produisent qu'un nombre fini de fois.
Cela signifie que pour presqu'aucun $\omega \in \Omega$, il existe un rang $K_\omega$ tel que pour tout $k \ge K_\omega$, $\omega \notin A_k$.
Si $\omega \notin A_k$, cela veut dire que :
$$|X_{\varphi(k)}(\omega) - X(\omega)| \le \frac{1}{k}$$
Cette inégalité garantit que, pour presque tout $\omega \in \Omega$, la limite simple de la sous-suite numérique $(X_{\varphi(k)}(\omega))_{k \in \mathbb{N}}$ est $X(\omega)$.
En effet, pour tout $\varepsilon > 0$, en choisissant $k \ge \max(K_\omega, \lceil \frac{1}{\varepsilon} \rceil)$, on a $|X_{\varphi(k)}(\omega) - X(\omega)| \le \varepsilon$.
La sous-suite $(X_{\varphi(k)})$ converge donc presque sûrement vers $X$.
Ce résultat puissant explique en grande partie pourquoi la convergence en probabilité partage tant de propriétés avec la convergence presque sûre.
