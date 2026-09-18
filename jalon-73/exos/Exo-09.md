# Exercice 9 : La convexité de la fonction puissance

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Dans le cours, pour prouver que $f+g \in L^p$, nous avons utilisé l'inégalité $(a+b)^p \le 2^{p-1}(a^p+b^p)$ pour $a,b \ge 0$ et $p \ge 1$.

1. Démontrer rigoureusement cette inégalité en utilisant la convexité de la fonction $x \mapsto x^p$.
2. Proposer une démonstration alternative par l'étude de fonction de $\phi(t) = (1+t)^p - 2^{p-1}(1+t^p)$ sur $[0, 1]$.

---

## Correction détaillée

1. **Preuve par la convexité :**
   Soit $h(x) = x^p$ pour $x \ge 0$ et $p \ge 1$.
   La dérivée seconde est $h''(x) = p(p-1)x^{p-2}$.
   Puisque $p \ge 1$ et $x \ge 0$, on a $h''(x) \ge 0$. La fonction $h$ est donc strictement convexe.
   Par définition de la convexité avec $\lambda = 1/2 \in [0,1]$ :
   $$ h\left( \frac{1}{2}a + \frac{1}{2}b \right) \le \frac{1}{2}h(a) + \frac{1}{2}h(b) $$
   $$ \left( \frac{a+b}{2} \right)^p \le \frac{1}{2} a^p + \frac{1}{2} b^p $$
   En factorisant le membre de gauche :
   $$ \frac{(a+b)^p}{2^p} \le \frac{a^p + b^p}{2} $$
   En multipliant par $2^p$, on obtient le résultat cherché :
   $$ (a+b)^p \le 2^{p-1} (a^p + b^p) $$

2. **Preuve analytique :**
   Par symétrie, supposons $a \ge b$. Si $b=0$, l'inégalité $a^p \le 2^{p-1}a^p$ est évidente car $2^{p-1} \ge 1$.
   Si $b > 0$, divisons l'inégalité par $a^p$ et posons $t = b/a \in [0, 1]$. L'inégalité équivaut à montrer que pour tout $t \in [0,1]$ :
   $$ (1+t)^p \le 2^{p-1}(1+t^p) \iff \phi(t) \le 0 $$
   Étudions les variations de $\phi(t) = (1+t)^p - 2^{p-1}(1+t^p)$.
   $$ \phi'(t) = p(1+t)^{p-1} - 2^{p-1} p t^{p-1} = p \left( (1+t)^{p-1} - (2t)^{p-1} \right) $$
   Cherchons le signe de $\phi'(t)$. La fonction $x \mapsto x^{p-1}$ est strictement croissante.
   $\phi'(t) \le 0 \iff (1+t)^{p-1} \le (2t)^{p-1} \iff 1+t \le 2t \iff 1 \le t$.
   Donc pour $t \in [0, 1]$, on a $t \le 1 \implies \phi'(t) \ge 0$.
   La fonction $\phi$ est donc croissante sur $[0, 1]$.
   Son maximum est atteint en $t=1$.
   Or $\phi(1) = (1+1)^p - 2^{p-1}(1+1^p) = 2^p - 2^{p-1}(2) = 2^p - 2^p = 0$.
   Puisque $\phi$ croît jusqu'à un maximum qui vaut 0, on a bien $\phi(t) \le 0$ pour tout $t \in [0, 1]$.
