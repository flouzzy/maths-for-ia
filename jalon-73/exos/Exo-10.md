# Exercice 10 : Non-continuité de la translation dans $L^\infty(\mathbb{R})$ \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Montrer que la continuité de la translation n'est pas vérifiée dans $L^\infty(\mathbb{R})$.
Indication : on pourra considérer la fonction indicatrice d'un intervalle.

**Correction :**
Considérons $f = 1_{[-1, 1]}$, la fonction indicatrice de l'intervalle $[-1, 1]$.
Cette fonction est bornée, donc $f \in L^\infty(\mathbb{R})$ et $\|f\|_\infty = 1$.

Calculons $\tau_h f - f$ pour $h > 0$.
$\tau_h f(x) = f(x-h) = 1_{[-1, 1]}(x-h) = 1_{[-1+h, 1+h]}(x)$.
Ainsi, $\tau_h f(x) - f(x) = 1_{[-1+h, 1+h]}(x) - 1_{[-1, 1]}(x)$.

Si $0 < h < 2$ :
- Pour $x \in ]1, 1+h]$, $\tau_h f(x) = 1$ et $f(x) = 0$, donc la différence vaut $1$.
- L'intervalle $]1, 1+h]$ a une mesure de Lebesgue $h > 0$.
Donc le supremum essentiel de $|\tau_h f - f|$ est au moins $1$.
On a donc $\|\tau_h f - f\|_\infty = 1$ pour tout $h \in ]0, 2[$.

Ainsi, $\lim_{h \to 0^+} \|\tau_h f - f\|_\infty = 1 \neq 0$.
La translation n'est donc pas continue sur $L^\infty(\mathbb{R})$. C'est une différence topologique fondamentale avec les espaces $L^p$ pour $p < +\infty$.
