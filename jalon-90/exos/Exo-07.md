# Exercice 07

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit la suite $(X_n)$ définie par la "machine à écrire". On partitionne l'intervalle $\Omega = [0, 1]$ muni de la mesure de Lebesgue en dyadiques.
Pour $n \ge 1$, écrivons $n = 2^k + m$ où $k \ge 0$ et $0 \le m < 2^k$.
On définit $X_n$ comme la fonction indicatrice de l'intervalle $I_{k, m} = [\frac{m}{2^k}, \frac{m+1}{2^k}]$.
Prouvez de manière exhaustive que cette suite converge en probabilité, dans tous les espaces $L^p$ pour $p \ge 1$, mais **ne converge presque sûrement en aucun point**.

**Correction :**

**1. Convergence en probabilité :**
Soit un seuil $\varepsilon \in ]0, 1[$. (Si $\varepsilon \ge 1$, l'événement est vide car $X_n \in \{0, 1\}$).
Évaluons la probabilité de l'événement déviant : $\mathbb{P}(|X_n - 0| > \varepsilon) = \mathbb{P}(X_n = 1)$.
La variable $X_n$ vaut $1$ exclusivement sur l'intervalle $I_{k, m}$. Sa probabilité correspond donc à la longueur de cet intervalle.
$$ \mathbb{P}(X_n = 1) = \lambda\left( \left[\frac{m}{2^k}, \frac{m+1}{2^k}\right] \right) = \frac{1}{2^k} $$
Lorsque $n$ tend vers l'infini, la puissance de 2 qui l'encadre inférieurement, $2^k$, tend inévitablement vers l'infini. Donc $k \to \infty$.
Ainsi, $\lim_{n \to \infty} \mathbb{P}(|X_n| > \varepsilon) = \lim_{k \to \infty} \frac{1}{2^k} = 0$.
La suite converge bien en probabilité vers $0$.

**2. Convergence dans $L^p$ :**
Soit $p \ge 1$. Calculons la norme $L^p$ de la différence :
$$ \mathbb{E}[|X_n - 0|^p] = \int_{\Omega} |X_n(\omega)|^p \, d\mathbb{P}(\omega) $$
Puisque $X_n$ prend ses valeurs dans $\{0, 1\}$, l'opération d'élévation à la puissance $p$ laisse ses valeurs invariantes : $|X_n|^p = X_n$.
L'espérance se réduit à nouveau à la probabilité de l'événement support :
$$ \mathbb{E}[|X_n|^p] = \mathbb{E}[X_n] = \mathbb{P}(X_n = 1) = \frac{1}{2^k} $$
La limite de cette quantité est $0$. Donc la suite converge vers $0$ dans tous les espaces $L^p$.

**3. Absence absolue de convergence presque sûre :**
Pour démontrer l'absence de convergence ponctuelle, fixons un $\omega \in [0, 1]$ arbitraire.
Pour tout niveau de subdivision dyadique $k \ge 0$, les intervalles $(I_{k, m})_{m=0}^{2^k-1}$ forment une partition complète (aux bornes près, de mesure nulle) du segment $[0, 1]$.
Par conséquent, pour chaque entier $k$, il existe un unique indice $m_k$ tel que $\omega \in I_{k, m_k}$.
Soit la sous-suite d'indices définie par $n_k = 2^k + m_k$. Pour ces indices spécifiques, la fonction valant 1 sur cet intervalle est "activée" au point $\omega$.
Ainsi, pour tout $k$, $X_{n_k}(\omega) = 1$.
Il en découle trivialement que la limite supérieure de la suite évaluée en $\omega$ vaut :
$$ \limsup_{n \to \infty} X_n(\omega) = 1 $$

À l'inverse, considérons la sous-suite d'indices obtenue en sélectionnant l'intervalle *opposé* au point $\omega$ dans la partition. Il existe d'autres indices $m'_k \neq m_k$ tels que $\omega \notin I_{k, m'_k}$.
Pour ces indices $n'_k = 2^k + m'_k$, nous aurons inévitablement $X_{n'_k}(\omega) = 0$.
La limite inférieure vaut donc :
$$ \liminf_{n \to \infty} X_n(\omega) = 0 $$

Puisque la limite supérieure ($1$) diffère strictement de la limite inférieure ($0$), la suite ponctuelle $(X_n(\omega))$ oscille indéfiniment et ne converge pas.
Ceci étant vrai pour tout $\omega \in [0, 1]$, l'ensemble des points de convergence est vide. L'événement de convergence a une probabilité de $0$. La suite ne converge donc pas presque sûrement.
