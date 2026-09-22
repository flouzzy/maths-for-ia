# Exercice 3 : Extraction de sous-suite convergente p.p.
**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
En reprenant la suite $(f_n)$ de l'exercice 2, extraire explicitement une sous-suite $(f_{\varphi(n)})$ qui converge presque partout vers $0$.

**Correction :**
La suite est $f_n = \mathbf{1}_{I_{k,j}}$ avec $n = \frac{k(k-1)}{2} + j + 1$.
Pour extraire une sous-suite convergente presque partout vers 0, il suffit de choisir, pour chaque $k$, le premier intervalle $I_{k,0} = [0, 1/k]$.
Posons $\varphi(k) = \frac{k(k-1)}{2} + 1$ (ce qui correspond à $j=0$).
Alors $g_k = f_{\varphi(k)} = \mathbf{1}_{[0, 1/k]}$.
Soit $x \in ]0, 1]$. Par la propriété d'Archimède, il existe $K \in \mathbb{N}^*$ tel que $1/K < x$. Pour tout $k \ge K$, $1/k \le 1/K < x$, donc $x \notin [0, 1/k]$. Ainsi $g_k(x) = 0$ pour tout $k \ge K$.
La suite $(g_k(x))$ est nulle à partir d'un certain rang, donc elle converge vers 0.
La seule exception est $x=0$, où $g_k(0) = 1$ pour tout $k$, donc $g_k(0) \to 1$.
Ainsi, $(f_{\varphi(k)})$ converge vers $0$ ponctuellement sur $]0, 1]$, c'est-à-dire presque partout (puisque $\{0\}$ est de mesure nulle).
