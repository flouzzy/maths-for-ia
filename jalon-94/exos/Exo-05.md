# Exercice 5 : Théorème de la Limite Centrale et Intervalle de Confiance \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Un institut de sondage souhaite estimer la proportion $p$ d'électeurs favorables à un candidat.
Il interroge $n=1000$ personnes. Soit $F_n$ la proportion empirique des personnes favorables obtenues dans l'échantillon.
Montrer comment le TCL permet de construire un intervalle de confiance asymptotique à $95\%$ pour la proportion $p$, et donner la forme de cet intervalle. Quelle est la marge d'erreur maximale ?

**Correction :**

Soit $X_i$ la variable de Bernoulli qui vaut $1$ si la $i$-ème personne est favorable et $0$ sinon. $X_i \sim \mathcal{B}(p)$.
La proportion empirique est $F_n = \frac{1}{n} \sum_{i=1}^n X_i$.
L'espérance de $X_i$ est $p$, sa variance est $p(1-p)$.
L'espérance de $F_n$ est $p$, et sa variance est $\frac{p(1-p)}{n}$.

Le TCL indique que :
$$Z_n = \frac{F_n - p}{\sqrt{\frac{p(1-p)}{n}}} \xrightarrow{\mathcal{L}} \mathcal{N}(0, 1)$$

Pour un niveau de confiance de $95\%$, on cherche la valeur limite $z_{\alpha/2}$ telle que $\mathbb{P}(-z_{\alpha/2} \le Z_n \le z_{\alpha/2}) = 0.95$.
Dans les tables de la loi normale, $\Phi(1.96) \approx 0.975$, donc $z_{\alpha/2} = 1.96$.

On a donc, approximativement :
$$\mathbb{P}\left( -1.96 \le \frac{F_n - p}{\sqrt{\frac{p(1-p)}{n}}} \le 1.96 \right) \approx 0.95$$
En isolant $p$ dans l'inégalité (et en remplaçant au dénominateur le $p(1-p)$ inconnu par son estimateur convergent $F_n(1-F_n)$ ou par sa majoration $1/4$), on obtient l'intervalle de confiance :
$$IC_{95\%} = \left[ F_n - 1.96 \sqrt{\frac{F_n(1-F_n)}{n}} , F_n + 1.96 \sqrt{\frac{F_n(1-F_n)}{n}} \right]$$

La marge d'erreur est $E = 1.96 \sqrt{\frac{p(1-p)}{n}}$.
Puisque la fonction $p \mapsto p(1-p)$ est maximale pour $p=0.5$ avec une valeur de $1/4$, la marge d'erreur maximale est :
$$E_{\max} = 1.96 \sqrt{\frac{0.25}{1000}} = \frac{1.96}{2 \sqrt{1000}} = \frac{1.96}{63.24} \approx 0.03099$$
La marge d'erreur maximale est donc d'environ $3.1\%$ (ce qui est la fameuse règle des "$3\%$" pour des sondages sur un millier de personnes).
