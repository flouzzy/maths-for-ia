# Exercice 6 : Croissance polynomiale
**Énoncé :** Soit $\mathcal{H}$ une classe de fonctions de dimension VC égale à $d$. Le lemme de Sauer affirme que $\Pi_{\mathcal{H}}(n) \le \sum_{i=0}^d \binom{n}{i}$. Démontrer que pour $n \ge d$, $\sum_{i=0}^d \binom{n}{i} \le \left(\frac{en}{d}\right)^d$.

**Correction Détaillée :**
* *Analyse de l'énoncé :* On cherche à majorer une somme partielle de coefficients binomiaux par une expression puissance simple. Cette astuce est classique en théorie de l'apprentissage pour obtenir une borne gérable.
* *Résolution pas-à-pas :*
  1. Partons de la somme $\sum_{i=0}^d \binom{n}{i}$. Puisque $n \ge d$, nous avons pour tout $0 \le i \le d$, $\left(\frac{n}{d}\right)^{d-i} \ge 1$.
  2. Nous pouvons donc multiplier chaque terme de la somme par ce facteur qui est supérieur ou égal à 1 :
     $$ \sum_{i=0}^d \binom{n}{i} \le \sum_{i=0}^d \binom{n}{i} \left(\frac{n}{d}\right)^{d-i} $$
  3. Factorisons le terme $\left(\frac{n}{d}\right)^d$ à droite de la somme :
     $$ \sum_{i=0}^d \binom{n}{i} \left(\frac{n}{d}\right)^{-i} \left(\frac{n}{d}\right)^d = \left(\frac{n}{d}\right)^d \sum_{i=0}^d \binom{n}{i} \left(\frac{d}{n}\right)^i $$
  4. Observons la somme restante. Tous ses termes sont positifs, on peut donc la majorer en étendant la somme jusqu'à $n$ (puisque $\binom{n}{i}=0$ pour $i>n$ et on ajoute des termes positifs) :
     $$ \sum_{i=0}^d \binom{n}{i} \left(\frac{d}{n}\right)^i \le \sum_{i=0}^n \binom{n}{i} \left(\frac{d}{n}\right)^i 1^{n-i} $$
  5. On reconnaît le développement du binôme de Newton $(x+y)^n = \sum_{i=0}^n \binom{n}{i} x^i y^{n-i}$ avec $x = \frac{d}{n}$ et $y = 1$ :
     $$ \sum_{i=0}^n \binom{n}{i} \left(\frac{d}{n}\right)^i 1^{n-i} = \left(1 + \frac{d}{n}\right)^n $$
  6. On utilise maintenant l'inégalité fondamentale $1 + x \le e^x$ pour tout $x \in \mathbb{R}$. En posant $x = \frac{d}{n}$ :
     $$ \left(1 + \frac{d}{n}\right)^n \le \left(e^{d/n}\right)^n = e^d $$
  7. En rassemblant les inégalités :
     $$ \sum_{i=0}^d \binom{n}{i} \le \left(\frac{n}{d}\right)^d e^d = \left(\frac{en}{d}\right)^d $$
  8. Ce qui achève la démonstration.
