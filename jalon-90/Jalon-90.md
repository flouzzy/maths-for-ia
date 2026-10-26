---
uuid: "jalon-90"
title: "Les modes de convergence en probabilités"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/asymptotique
prev: "[[Jalon-89.md]]"
next: "[[Jalon 91 (Inégalités de concentration).md]]"
---

# Jalon 90 : Les modes de convergence en probabilités

## 1. Introduction historique et conceptuelle

L'étude des phénomènes aléatoires, initiée par Pascal et Fermat au XVIIe siècle, s'est longtemps cantonnée à des espaces d'états finis où la notion de probabilité se résumait à des rapports de dénombrement. Cependant, l'avènement de la physique statistique au XIXe siècle (Maxwell, Boltzmann) et le besoin de modéliser des erreurs de mesure continues (Gauss, Laplace) ont forcé les mathématiciens à considérer des suites infinies de variables aléatoires.

Le problème fondamental qui s'est alors posé était le suivant : que signifie "converger" pour une suite d'applications mesurables $X_n : \Omega \to \mathbb{R}$ dont les valeurs dépendent du hasard de $\omega \in \Omega$ ? Contrairement à l'analyse réelle classique où une suite numérique $(x_n)_{n \in \mathbb{N}}$ converge vers $x$ si la distance $|x_n - x|$ tend vers zéro, ici la distance $|X_n(\omega) - X(\omega)|$ dépend de la réalisation $\omega$.

Andrey Kolmogorov, dans ses fondements axiomatiques de 1933, a apporté la réponse définitive en montrant qu'il n'existe pas une, mais plusieurs façons de mesurer cette proximité asymptotique. Selon que l'on s'intéresse à la réalisation de chaque trajectoire individuelle, à la moyenne globale des erreurs, à la probabilité de commettre une grande erreur, ou simplement à la forme asymptotique de la distribution des résultats, on définit quatre modes de convergence distincts. Cette richesse conceptuelle est la pierre angulaire de toute la statistique inférentielle et de l'apprentissage automatique moderne.

## 2. Définitions, Théorèmes et Exemples

### 2.1 La Convergence Presque Sûre (p.s.)

La convergence presque sûre est le mode le plus fort. Elle stipule que pour presque tout tirage du hasard (c'est-à-dire avec une probabilité de 1), la suite des réalisations converge.

**Définition (Convergence Presque Sûre) :**
Soit $(X_n)_{n \in \mathbb{N}}$ une suite de variables aléatoires et $X$ une variable aléatoire définies sur le même espace de probabilité $(\Omega, \mathcal{F}, \mathbb{P})$. On dit que $X_n$ converge presque sûrement vers $X$, noté $X_n \xrightarrow{\text{p.s.}} X$, si :
$$ \mathbb{P}\left(\left\{ \omega \in \Omega \mid \lim_{n \to \infty} X_n(\omega) = X(\omega) \right\}\right) = 1 $$

Ce qui est équivalent, en termes d'événements, à :
$$ \mathbb{P}\left( \bigcup_{\epsilon > 0} \bigcap_{N \in \mathbb{N}} \bigcup_{n \geq N} \{ |X_n - X| > \epsilon \} \right) = 0 $$

**Exemple Concret 1 :**
Considérons l'espace de probabilité continu $\Omega = [0, 1]$ muni de la mesure de Lebesgue $\mathbb{P} = \lambda$ sur les boréliens.
Soit la suite de variables aléatoires définie par $X_n(\omega) = \omega^n$.
- Pour $\omega \in [0, 1[$, on a $\lim_{n \to \infty} \omega^n = 0$.
- Pour $\omega = 1$, on a $\lim_{n \to \infty} 1^n = 1$.

Soit $X$ la variable constante égale à $0$.
L'ensemble des $\omega$ pour lesquels la suite ne converge pas vers $0$ est $\{1\}$.
Or $\mathbb{P}(\{1\}) = \lambda(\{1\}) = 0$.
Donc, $X_n \xrightarrow{\text{p.s.}} 0$. La convergence a lieu "presque partout".

### 2.2 La Convergence en Probabilité

Ce mode exige seulement que la probabilité d'observer un écart significatif entre $X_n$ et $X$ tende vers zéro, sans garantir que chaque trajectoire individuelle se stabilise de manière monotone.

**Définition (Convergence en Probabilité) :**
On dit que $X_n$ converge en probabilité vers $X$, noté $X_n \xrightarrow{\mathbb{P}} X$, si pour tout $\epsilon > 0$ :
$$ \lim_{n \to \infty} \mathbb{P}(|X_n - X| > \epsilon) = 0 $$

**Théorème (Lien entre p.s. et probabilité) :**
Si $X_n \xrightarrow{\text{p.s.}} X$, alors $X_n \xrightarrow{\mathbb{P}} X$. La réciproque est généralement fausse.

**Cas limite : Une suite qui converge en probabilité mais pas presque sûrement (La machine à écrire glissante)**
Soit $\Omega = [0, 1]$ avec la mesure de Lebesgue.
On définit $X_n$ comme la fonction indicatrice d'un intervalle $I_n$ qui "balaie" $[0,1]$ de gauche à droite tout en devenant de plus en plus étroit.
Plus formellement, pour $n = 2^k + j$ avec $0 \leq j < 2^k$, on pose $I_n = \left[ \frac{j}{2^k}, \frac{j+1}{2^k} \right]$ et $X_n(\omega) = \mathbf{1}_{I_n}(\omega)$.
- Pour tout $\epsilon \in ]0, 1[$, $\mathbb{P}(|X_n - 0| > \epsilon) = \mathbb{P}(\omega \in I_n) = \frac{1}{2^k}$. Comme $k \to \infty$ quand $n \to \infty$, cette probabilité tend vers $0$. Donc $X_n \xrightarrow{\mathbb{P}} 0$.
- Cependant, pour tout $\omega \in [0, 1]$, la suite $(X_n(\omega))_{n \in \mathbb{N}}$ prend la valeur $1$ une infinité de fois (chaque fois qu'un "balayage" passe sur $\omega$). La suite de réels $(X_n(\omega))$ alterne infiniment entre $0$ et $1$, donc elle ne converge pour *aucun* $\omega$. La convergence p.s. n'a lieu nulle part.

### 2.3 La Convergence dans $L^p$

Ce mode s'intéresse à la convergence de la moyenne des erreurs élevées à une puissance $p$.

**Définition (Convergence dans $L^p$) :**
Pour $p \geq 1$, on suppose que $X_n$ et $X$ admettent un moment d'ordre $p$ fini ($\mathbb{E}[|X|^p] < \infty$). On dit que $X_n$ converge vers $X$ dans $L^p$, noté $X_n \xrightarrow{L^p} X$, si :
$$ \lim_{n \to \infty} \mathbb{E}[|X_n - X|^p] = 0 $$
Le cas $p=2$ correspond à la convergence en moyenne quadratique (souvent utilisée pour estimer l'erreur quadratique moyenne en régression).

**Théorème (Lien entre $L^p$ et probabilité) :**
Si $X_n \xrightarrow{L^p} X$, alors $X_n \xrightarrow{\mathbb{P}} X$.

**Exemple Concret 2 : Convergence $L^2$**
Soit $\Omega = ]0, 1]$ avec la mesure de Lebesgue.
Posons $X_n(\omega) = \sqrt{n} \mathbf{1}_{]0, 1/n]}(\omega)$.
- Convergence en probabilité vers $0$ : Pour $\epsilon > 0$, $\mathbb{P}(|X_n| > \epsilon) = \mathbb{P}(]0, 1/n]) = \frac{1}{n} \xrightarrow{n \to \infty} 0$. Donc $X_n \xrightarrow{\mathbb{P}} 0$.
- Convergence $L^2$ : Calculons la limite de la moyenne des carrés de l'erreur :
  $$ \mathbb{E}[|X_n - 0|^2] = \int_0^1 (\sqrt{n} \mathbf{1}_{]0, 1/n]}(\omega))^2 \, d\omega = \int_0^{1/n} n \, d\omega = n \times \frac{1}{n} = 1 \neq 0 $$
  La suite $(X_n)$ ne converge donc *pas* vers $0$ dans $L^2$. La pointe infiniment haute et étroite accumule trop de "masse" pour que la moyenne globale s'écrase.

### 2.4 La Convergence en Loi (ou convergence étroite)

Ce mode est le plus faible. Il ne nécessite même pas que les variables aléatoires soient définies sur le même espace de probabilité $\Omega$. Il stipule simplement que les fonctions de répartition (ou les densités) se ressemblent de plus en plus asymptotiquement.

**Définition (Convergence en Loi) :**
Soit $(X_n)$ une suite de variables aléatoires de fonctions de répartition $F_n(x) = \mathbb{P}(X_n \leq x)$, et $X$ une variable de fonction de répartition $F$. On dit que $X_n$ converge en loi vers $X$, noté $X_n \xrightarrow{\mathcal{L}} X$, si :
$$ \lim_{n \to \infty} F_n(x) = F(x) $$
pour tout point $x$ où la fonction $F$ est continue.

**Définition alternative équivalente (Théorème de Portmanteau partiel) :**
$X_n \xrightarrow{\mathcal{L}} X$ si et seulement si pour toute fonction $h : \mathbb{R} \to \mathbb{R}$ continue et bornée :
$$ \lim_{n \to \infty} \mathbb{E}[h(X_n)] = \mathbb{E}[h(X)] $$

**Exemple Concret 3 : Convergence en loi vers une constante**
Considérons une suite de variables aléatoires $X_n$ suivant des lois normales centrées de variance décroissante : $X_n \sim \mathcal{N}(0, 1/n)$.
La densité de $X_n$ est $f_n(x) = \frac{\sqrt{n}}{\sqrt{2\pi}} e^{-n x^2 / 2}$.
Lorsque $n \to \infty$, la "cloche" devient infiniment fine et haute autour de $0$.
Soit $X$ la variable certaine constante égale à $0$ (distribution de Dirac $\delta_0$). Sa fonction de répartition est $F(x) = 0$ pour $x < 0$ et $F(x) = 1$ pour $x \geq 0$.
La fonction de répartition de $X_n$ est $F_n(x) = \int_{-\infty}^x f_n(t) \, dt$.
- Si $x < 0$, $\lim F_n(x) = 0 = F(x)$.
- Si $x > 0$, $\lim F_n(x) = 1 = F(x)$.
(En $x=0$, $F_n(0) = 1/2$, mais cela n'a pas d'importance car $F$ est discontinue en $0$).
Donc $X_n \xrightarrow{\mathcal{L}} 0$.

## 3. Démonstrations

### Démonstration : $L^p \implies \mathbb{P}$
Nous allons démontrer rigoureusement que la convergence dans $L^p$ implique la convergence en probabilité.
**Preuve :**
1. Soit $p \geq 1$. Supposons que $X_n \xrightarrow{L^p} X$, c'est-à-dire que $\lim_{n \to \infty} \mathbb{E}[|X_n - X|^p] = 0$.
2. Soit un $\epsilon > 0$ arbitraire. Nous voulons évaluer $\mathbb{P}(|X_n - X| > \epsilon)$.
3. Soit $Y_n = |X_n - X|^p$. L'événement $\{ |X_n - X| > \epsilon \}$ est strictement identique à l'événement $\{ |X_n - X|^p > \epsilon^p \}$, car la fonction $x \mapsto x^p$ est strictement croissante sur $\mathbb{R}_+$.
4. Appliquons l'inégalité de Markov à la variable aléatoire positive ou nulle $Y_n$ avec le seuil $a = \epsilon^p > 0$ :
   $$ \mathbb{P}(Y_n > \epsilon^p) \leq \frac{\mathbb{E}[Y_n]}{\epsilon^p} $$
   C'est-à-dire :
   $$ \mathbb{P}(|X_n - X| > \epsilon) \leq \frac{\mathbb{E}[|X_n - X|^p]}{\epsilon^p} $$
5. Passons à la limite quand $n \to \infty$. Puisque l'hypothèse est $\lim_{n \to \infty} \mathbb{E}[|X_n - X|^p] = 0$, et que $\epsilon^p$ est une constante strictement positive, le membre de droite tend vers $0$.
6. Or, une probabilité est toujours minorée par $0$. Par le théorème d'encadrement (gendarmes) :
   $$ 0 \leq \lim_{n \to \infty} \mathbb{P}(|X_n - X| > \epsilon) \leq 0 $$
   Donc $\lim_{n \to \infty} \mathbb{P}(|X_n - X| > \epsilon) = 0$.
$\blacksquare$

### Démonstration : $\mathbb{P} \implies \mathcal{L}$
Nous allons montrer que si $(X_n)$ et $X$ sont définies sur le même espace et que $X_n \xrightarrow{\mathbb{P}} X$, alors $X_n \xrightarrow{\mathcal{L}} X$.
**Preuve :**
1. Nous utilisons la caractérisation par l'espérance de fonctions continues bornées. Soit $h : \mathbb{R} \to \mathbb{R}$ continue et bornée. Il existe $M > 0$ tel que $\forall x \in \mathbb{R}, |h(x)| \leq M$.
2. Soit $\epsilon' > 0$. $h$ étant uniformément continue sur tout compact, et la distribution de $X$ étant tendue (pour tout $\eta > 0$, il existe $A > 0$ tel que $\mathbb{P}(|X| > A) < \eta$), il existe une constante $\delta > 0$ telle que :
   $$ \text{Si } |x - y| \leq \delta \text{ et } |x| \leq A, \text{ alors } |h(x) - h(y)| \leq \frac{\epsilon'}{2} $$
3. Écrivons l'écart en espérance :
   $$ |\mathbb{E}[h(X_n)] - \mathbb{E}[h(X)]| = |\mathbb{E}[h(X_n) - h(X)]| \leq \mathbb{E}[|h(X_n) - h(X)|] $$
4. Découpons l'espace des événements $\Omega$ en deux sous-ensembles :
   - L'événement favorable $A_n = \{ |X_n - X| \leq \delta \}$
   - L'événement défavorable $A_n^c = \{ |X_n - X| > \delta \}$
5. On sépare l'intégrale (espérance) sur ces deux événements :
   $$ \mathbb{E}[|h(X_n) - h(X)|] = \mathbb{E}[|h(X_n) - h(X)| \mathbf{1}_{A_n}] + \mathbb{E}[|h(X_n) - h(X)| \mathbf{1}_{A_n^c}] $$
6. Majoration sur l'événement $A_n$ (où les points sont très proches) :
   Puisque $|X_n - X| \leq \delta$, alors (modulo l'approximation compacte) $|h(X_n) - h(X)| \leq \epsilon'/2$. Donc :
   $$ \mathbb{E}[|h(X_n) - h(X)| \mathbf{1}_{A_n}] \leq \frac{\epsilon'}{2} \mathbb{P}(A_n) \leq \frac{\epsilon'}{2} $$
7. Majoration sur l'événement $A_n^c$ (où les points sont éloignés) :
   Nous utilisons la borne globale de $h$. On a $|h(X_n) - h(X)| \leq |h(X_n)| + |h(X)| \leq 2M$. Donc :
   $$ \mathbb{E}[|h(X_n) - h(X)| \mathbf{1}_{A_n^c}] \leq 2M \mathbb{P}(A_n^c) = 2M \mathbb{P}(|X_n - X| > \delta) $$
8. Somme des majorations :
   $$ |\mathbb{E}[h(X_n)] - \mathbb{E}[h(X)]| \leq \frac{\epsilon'}{2} + 2M \mathbb{P}(|X_n - X| > \delta) $$
9. Passage à la limite sur $n$ :
   Puisque $X_n \xrightarrow{\mathbb{P}} X$, par définition pour $\delta > 0$, $\lim_{n \to \infty} \mathbb{P}(|X_n - X| > \delta) = 0$.
   Ainsi, pour $n$ assez grand, $2M \mathbb{P}(|X_n - X| > \delta) \leq \epsilon'/2$.
   Il vient alors pour $n$ assez grand :
   $$ |\mathbb{E}[h(X_n)] - \mathbb{E}[h(X)]| \leq \epsilon' $$
10. Comme $\epsilon'$ a été choisi arbitrairement petit, on conclut que $\lim_{n \to \infty} |\mathbb{E}[h(X_n)] - \mathbb{E}[h(X)]| = 0$, ce qui prouve la convergence en loi.
$\blacksquare$

## 4. Applications en Physique, Logique et Intelligence Artificielle

### La Consistance des estimateurs
En apprentissage automatique, nous cherchons souvent à estimer un paramètre cible inconnu $\theta^* \in \mathbb{R}^d$ à partir d'un jeu de données aléatoire $(D_n)$ de taille $n$.
L'estimateur $\hat{\theta}_n = f(D_n)$ est une variable aléatoire dépendante de l'échantillon.
- On dit que l'estimateur est **fortement consistant** si $\hat{\theta}_n \xrightarrow{\text{p.s.}} \theta^*$. C'est la garantie absolue (au sens de Kolmogorov) que l'algorithme "trouvera" avec certitude la vraie valeur s'il dispose d'une infinité de données.
- On dit que l'estimateur est **faiblement consistant** si $\hat{\theta}_n \xrightarrow{\mathbb{P}} \theta^*$.

### Régression et Fonctions de Coût ($L^2$)
Lors de l'optimisation des poids d'un réseau de neurones avec l'Erreur Quadratique Moyenne (MSE), l'objectif mathématique est explicitement de minimiser l'écart entre la prédiction $f_\theta(X)$ et la cible $Y$ au sens de la norme $L^2$. La convergence asymptotique de la loss empirique vers zéro correspond exactement au fait de chercher une suite de fonctions $f_{\theta_n}$ telle que $f_{\theta_n}(X) \xrightarrow{L^2} Y$. Comme montré plus haut, si cette convergence a lieu, elle entraîne la convergence en probabilité.

### Generative Adversarial Networks (GANs) et Convergence en Loi
Dans l'architecture des GANs, le modèle générateur produit une variable aléatoire complexe $X_{gen}$ (une image artificielle) tentant d'imiter la variable cible $X_{reel}$. L'objectif d'entraînement, tel que formalisé par la distance de Wasserstein ou le critère Min-Max, n'est en aucun cas d'obtenir que $X_{gen}$ converge presque sûrement vers une image spécifique de la base de données.
L'objectif est d'atteindre la **convergence en loi** : $X_{gen} \xrightarrow{\mathcal{L}} X_{reel}$. La "cloche" (la variété des visages générés) doit parfaitement se superposer à la "cloche" réelle, même si un échantillon précis tiré du bruit générera un visage qui n'existe pour aucune image spécifique $\omega$ du jeu d'entraînement.
