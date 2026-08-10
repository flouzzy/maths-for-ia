## Exercice 1 : Compacité de l'intervalle unité \quad $\bigstar\star\star\star\star$

**Énoncé :** En utilisant le théorème de Bolzano-Weierstrass, démontrer rigoureusement que l'intervalle fermé $[0, 1]$ est séquentiellement compact dans $\mathbb{R}$.

**Correction Détaillée :**
Soit $(x_n)_{n \in \mathbb{N}}$ une suite d'éléments de $[0, 1]$.
La suite $(x_n)$ est bornée car pour tout $n$, $0 \le x_n \le 1$.
D'après le théorème de Bolzano-Weierstrass dans $\mathbb{R}$ (toute suite réelle bornée admet une sous-suite convergente), il existe une sous-suite $(x_{\phi(n)})_{n \in \mathbb{N}}$ (où $\phi : \mathbb{N} \to \mathbb{N}$ est strictement croissante) qui converge vers un réel $l \in \mathbb{R}$.
Puisque pour tout $n$, $x_{\phi(n)} \in [0, 1]$, et que le passage à la limite préserve les inégalités larges, on a :
$0 \le \lim_{n \to \infty} x_{\phi(n)} \le 1$, c'est-à-dire $0 \le l \le 1$.
Donc $l \in [0, 1]$.
Ainsi, de toute suite de $[0, 1]$, on a pu extraire une sous-suite convergente dans $[0, 1]$. Par définition, $[0, 1]$ est séquentiellement compact.