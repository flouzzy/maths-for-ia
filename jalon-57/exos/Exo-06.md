# Exercice 6 : Généralisation de l'inégalité d'erreur a posteriori
**Niveau :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $f : X \to X$ une contraction stricte de rapport $k < 1$ sur un espace métrique complet. Soit $x^*$ son point fixe.
Pour une suite $(x_n)$ générée par $x_{n+1} = f(x_n)$, démontrer rigoureusement la majoration de l'erreur *a posteriori* (ou en ligne) :
$$d(x_n, x^*) \leq \frac{k}{1-k} d(x_n, x_{n-1})$$

**Démonstration pas à pas :**
1. L'inégalité triangulaire de la distance affirme que pour tout $p > n \geq 1$,
   $d(x_n, x_p) \leq \sum_{i=n}^{p-1} d(x_i, x_{i+1})$.
2. On sait par hypothèse de contraction que $d(x_i, x_{i+1}) = d(f(x_{i-1}), f(x_i)) \leq k \, d(x_{i-1}, x_i)$.
   Par itération, on ramène ce terme à l'intervalle d'indice $n$ et $n-1$ :
   $d(x_i, x_{i+1}) \leq k^{i-n+1} d(x_{n-1}, x_n)$.
3. Injectons cette majoration dans l'inégalité triangulaire initiale :
   $d(x_n, x_p) \leq \sum_{i=n}^{p-1} k^{i-n+1} d(x_{n-1}, x_n)$.
4. Factorisons le terme de distance fixe $d(x_{n-1}, x_n)$ de la somme :
   $d(x_n, x_p) \leq d(x_{n-1}, x_n) \sum_{i=n}^{p-1} k^{i-n+1}$.
5. Procédons à un changement d'indice de sommation $j = i - n + 1$. Les bornes deviennent : pour $i=n$, $j=1$ ; pour $i=p-1$, $j=p-n$.
   $d(x_n, x_p) \leq d(x_{n-1}, x_n) \sum_{j=1}^{p-n} k^j$.
6. La somme est une série géométrique finie. En factorisant $k$, on obtient :
   $\sum_{j=1}^{p-n} k^j = k \sum_{m=0}^{p-n-1} k^m \leq k \sum_{m=0}^{\infty} k^m = \frac{k}{1-k}$ (puisque $k < 1$).
7. On obtient alors la majoration indépendante de $p$ :
   $d(x_n, x_p) \leq \frac{k}{1-k} d(x_{n-1}, x_n)$.
8. Puisque l'espace est complet, on sait que la suite $(x_p)$ converge vers $x^*$ lorsque $p \to \infty$. Par continuité de la distance en son deuxième argument, le passage à la limite $\lim_{p \to \infty} d(x_n, x_p)$ donne $d(x_n, x^*)$. L'inégalité large est préservée au passage à la limite, menant à :
   $d(x_n, x^*) \leq \frac{k}{1-k} d(x_{n-1}, x_n)$.
Cette borne est cruciale car elle permet d'obtenir un critère d'arrêt en algorithmique : on peut garantir l'erreur absolue courante uniquement en observant le résidu empirique entre les deux dernières itérations.
