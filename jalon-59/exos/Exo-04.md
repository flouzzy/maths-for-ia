# Exercice 4 : Famille Lipschitzienne et compacité

**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé

Soit $\mathcal{F}$ l'ensemble des fonctions $f : [0, 1] \to \mathbb{R}$ telles que :
1. $f(0) = 0$
2. Pour tous $x, y \in [0, 1]$, $|f(x) - f(y)| \le L |x - y|$, où $L > 0$ est une constante fixée.

Montrer que toute suite de fonctions $(f_n)_{n\in\mathbb{N}}$ extraite de $\mathcal{F}$ admet une sous-suite uniformément convergente sur $[0, 1]$.

## Résolution Détaillée

Pour répondre à cette question, nous allons utiliser le théorème d'Arzelà-Ascoli. Il faut vérifier les deux conditions sur la famille $\mathcal{F}$ : l'équicontinuité et la bornitude ponctuelle.

### 1. Équicontinuité

L'hypothèse indique que toutes les fonctions de $\mathcal{F}$ sont $L$-Lipschitziennes avec la même constante $L$.
Soit $\epsilon > 0$. Fixons $\delta = \frac{\epsilon}{L} > 0$.
Pour toute fonction $f \in \mathcal{F}$ et pour tous $x, y \in [0, 1]$ tels que $|x - y| < \delta$, nous avons :
$$ |f(x) - f(y)| \le L |x - y| < L \left( \frac{\epsilon}{L} \right) = \epsilon $$
Le module de continuité uniforme $\delta$ dépend uniquement de $\epsilon$ et de $L$, mais est complètement indépendant du choix de $f \in \mathcal{F}$.
La famille $\mathcal{F}$ est donc (uniformément) équicontinue sur le compact $[0, 1]$.

### 2. Bornitude ponctuelle (et uniforme)

Soit $x \in [0, 1]$. Pour toute $f \in \mathcal{F}$, appliquons la condition de Lipschitz entre le point $x$ et le point $0$ :
$$ |f(x) - f(0)| \le L |x - 0| = L x $$
Comme $f(0) = 0$ et $x \le 1$, nous obtenons :
$$ |f(x)| \le L x \le L $$
Ainsi, pour tout $x \in [0, 1]$, l'ensemble d'évaluation $\{f(x) \mid f \in \mathcal{F}\}$ est inclus dans l'intervalle fermé borné $[-L, L]$ de $\mathbb{R}$. Cet ensemble est donc relativement compact (par le théorème de Bolzano-Weierstrass dans $\mathbb{R}$).

### Conclusion par Arzelà-Ascoli

L'espace de départ $[0, 1]$ est un espace topologique compact.
L'espace d'arrivée $\mathbb{R}$ est un espace métrique complet.
La famille $\mathcal{F}$ est équicontinue et ponctuellement relativement compacte.
D'après le théorème d'Arzelà-Ascoli, la famille $\mathcal{F}$ est relativement compacte dans l'espace des fonctions continues muni de la topologie de la convergence uniforme (norme infinie).
Par conséquent, toute suite $(f_n)$ de $\mathcal{F}$ admet une sous-suite $(f_{\phi(n)})$ qui converge uniformément sur $[0, 1]$ vers une certaine fonction continue $f$. $\blacksquare$
