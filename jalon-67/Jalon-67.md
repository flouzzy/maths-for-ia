# Le Théorème de Convergence Monotone de Beppo-Levi

La construction de l'intégrale de Lebesgue, que nous avons amorcée pour les fonctions étagées puis étendue aux fonctions mesurables positives, trouve son véritable triomphe dans ses théorèmes de passage à la limite. Historiquement, l'intégrale de Riemann, bien qu'élégante et suffisante pour les fonctions continues par morceaux, souffrait d'une lacune rédhibitoire : l'espace des fonctions intégrables au sens de Riemann n'est pas complet pour la métrique $L^1$, et les théorèmes permettant d'intervertir limite et intégrale exigeaient une convergence uniforme, une condition beaucoup trop forte pour la physique moderne et la théorie des probabilités. En 1906, le mathématicien italien Beppo Levi (1875-1961), s'appuyant sur les travaux fondateurs d'Henri Lebesgue (1902), formule un résultat d'une simplicité et d'une puissance inouïes : si une suite de fonctions mesurables positives croît, alors la limite de leurs intégrales est l'intégrale de leur limite. Ce résultat, pierre angulaire de l'analyse fonctionnelle, libère les mathématiques de la contrainte d'uniformité et ouvre la voie à l'étude des espaces $L^p$, indispensables à la mécanique quantique et à la théorie de l'apprentissage statistique.

## 1. Énoncé et structure du théorème de convergence monotone

Le théorème de convergence monotone est le premier grand théorème d'interversion de la théorie de la mesure. Il ne requiert ni continuité, ni domination par une fonction intégrable, mais repose exclusivement sur la positivité et la monotonie (croissance) de la suite de fonctions.

**Théorème (Beppo-Levi / Convergence Monotone) :**
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $\bar{\mathbb{R}}_+ = [0, +\infty]$.
On suppose que la suite est croissante presque partout :
$$ \forall n \in \mathbb{N}, \quad f_n(x) \le f_{n+1}(x) \quad \mu\text{-p.p.} $$
Alors, la suite $(f_n)$ converge simplement presque partout vers une fonction mesurable positive $f : X \to \bar{\mathbb{R}}_+$, et l'on a :
$$ \lim_{n \to +\infty} \int_X f_n \, d\mu = \int_X \left( \lim_{n \to +\infty} f_n \right) \, d\mu = \int_X f \, d\mu. $$

Ici, l'espace $X$ est l'espace ambiant, $\mathcal{A}$ est la tribu (ou $\sigma$-algèbre) des ensembles mesurables, et $\mu$ est la mesure (par exemple, la mesure de Lebesgue sur $\mathbb{R}$ ou une mesure de probabilité). Les fonctions $f_n$ prennent leurs valeurs dans la droite achevée positive pour autoriser des limites infinies, garantissant que l'égalité reste vraie même si les deux membres valent $+\infty$.

**Exemple concret de passage à la limite :**
Considérons l'espace $X = ]0, 1]$ muni de la mesure de Lebesgue $\lambda$. Définissons la suite de fonctions $(f_n)$ par :
$$ f_n(x) = \begin{cases} \frac{1}{\sqrt{x}} & \text{si } x \in [\frac{1}{n}, 1] \\ 0 & \text{si } x \in ]0, \frac{1}{n}[ \end{cases} $$
Pour tout $x \in ]0, 1]$, on a $f_n(x) \le f_{n+1}(x)$ (dès que $n$ est assez grand pour que $x \ge \frac{1}{n}$). La suite de fonctions croît vers la fonction $f(x) = \frac{1}{\sqrt{x}}$.
Calculons l'intégrale de $f_n$ :
$$ \int_{]0,1]} f_n \, d\lambda = \int_{\frac{1}{n}}^1 x^{-1/2} \, dx = \left[ 2x^{1/2} \right]_{\frac{1}{n}}^1 = 2 - \frac{2}{\sqrt{n}}. $$
La limite de ces intégrales lorsque $n \to +\infty$ est $2$.
D'autre part, l'intégrale de la fonction limite $f$ est :
$$ \int_{]0,1]} \frac{1}{\sqrt{x}} \, d\lambda = \left[ 2\sqrt{x} \right]_0^1 = 2. $$
L'égalité de Beppo-Levi est parfaitement vérifiée : $\lim_{n} \int f_n = \int \lim_n f_n = 2$.
Remarquons que la convergence de $f_n$ vers $f$ est simplement ponctuelle et non uniforme sur $]0, 1]$ (la différence $f(x) - f_n(x) = \frac{1}{\sqrt{x}}$ sur $]0, \frac{1}{n}[$ tend vers $+\infty$ en $0$). L'intégrale de Riemann ne permet pas d'invoquer ses théorèmes d'interversion ici, soulignant la supériorité du cadre de Lebesgue.

**Contre-exemple (défaut de croissance) :**
La condition de croissance est impérative. Si $(f_n)$ n'est pas croissante, l'égalité peut faillir. Prenons $X = \mathbb{R}$ et $f_n(x) = n \cdot \mathbf{1}_{]0, 1/n]}(x)$. On a $\lim_{n} f_n(x) = 0$ pour tout $x \in \mathbb{R}$. Pourtant :
$$ \int_{\mathbb{R}} f_n \, d\lambda = n \cdot \frac{1}{n} = 1 \quad \text{et} \quad \int_{\mathbb{R}} 0 \, d\lambda = 0. $$
Ici, $1 \neq 0$. La suite des intégrales ne converge pas vers l'intégrale de la limite car la suite $(f_n)$ n'est pas croissante, la masse "s'échappant" vers l'infini le long de l'axe des ordonnées. Ce phénomène de perte de masse sera formellement traité par le Lemme de Fatou.

## 2. Démonstration rigoureuse par les fonctions étagées

La preuve de ce théorème repose sur l'approximation des fonctions mesurables positives par des fonctions étagées, c'est-à-dire des combinaisons linéaires finies d'indicatrices d'ensembles mesurables.

**Étape 1 : Inégalité évidente**
Puisque $(f_n)$ est croissante, on a $f_n(x) \le f(x)$ pour tout $n$ et tout $x$. L'intégrale de Lebesgue respecte l'ordre (par définition, comme suprémum des intégrales des fonctions étagées minorantes). Ainsi :
$$ \int_X f_n \, d\mu \le \int_X f \, d\mu. $$
En passant à la limite (la suite des réels $\int_X f_n \, d\mu$ étant croissante, elle admet une limite dans $\bar{\mathbb{R}}_+$) :
$$ \lim_{n \to +\infty} \int_X f_n \, d\mu \le \int_X f \, d\mu. $$
Il reste à prouver l'inégalité inverse : $\int_X f \, d\mu \le \lim_{n} \int_X f_n \, d\mu$.

**Étape 2 : Minoration par une fonction étagée arbitraire**
Par définition de l'intégrale d'une fonction mesurable positive $f$, on a :
$$ \int_X f \, d\mu = \sup \left\{ \int_X s \, d\mu \ \middle| \ s \text{ étagée}, \ 0 \le s \le f \right\}. $$
Soit donc $s$ une fonction étagée quelconque telle que $0 \le s(x) \le f(x)$ pour tout $x \in X$. Si l'on prouve que $\int_X s \, d\mu \le \lim_n \int_X f_n \, d\mu$, alors par passage au suprémum sur toutes les fonctions $s$, l'inégalité inverse sera démontrée.

**Étape 3 : Introduction d'un paramètre d'abattement $\alpha$**
Soit un réel $\alpha$ tel que $0 < \alpha < 1$. Puisque $s$ est bornée et s'annule en dehors d'un ensemble de mesure finie (si $\int s < +\infty$), la fonction $\alpha s$ est strictement inférieure à $s$ partout où $s(x) > 0$. Or, on sait que $\lim_n f_n(x) = f(x) \ge s(x)$. Par conséquent, pour tout $x$ tel que $s(x) > 0$, on a :
$$ f(x) > \alpha s(x). $$
Puisque $f_n(x) \to f(x)$, il existera nécessairement un rang à partir duquel $f_n(x) \ge \alpha s(x)$.
Définissons les ensembles :
$$ A_n = \{ x \in X \mid f_n(x) \ge \alpha s(x) \}. $$
Puisque $(f_n)$ est croissante, la suite d'ensembles $(A_n)$ est emboîtée croissante : $A_n \subset A_{n+1}$.
De plus, d'après ce qui précède, tout $x \in X$ finit par appartenir à un $A_n$ (si $s(x)=0$, $x \in A_0$, sinon il y entre pour $n$ assez grand). Ainsi, $X = \bigcup_{n \in \mathbb{N}} A_n$.

**Étape 4 : Utilisation de la continuité croissante de la mesure**
Sur l'ensemble $X$, nous avons la minoration triviale :
$$ f_n \ge f_n \cdot \mathbf{1}_{A_n} \ge \alpha s \cdot \mathbf{1}_{A_n}. $$
En intégrant cette inégalité :
$$ \int_X f_n \, d\mu \ge \int_X \alpha s \cdot \mathbf{1}_{A_n} \, d\mu = \alpha \int_{A_n} s \, d\mu. $$
La fonction étagée $s$ s'écrit $s = \sum_{i=1}^k c_i \mathbf{1}_{E_i}$ avec $c_i > 0$ et $E_i \in \mathcal{A}$ disjoints. Son intégrale sur $A_n$ est :
$$ \int_{A_n} s \, d\mu = \sum_{i=1}^k c_i \mu(E_i \cap A_n). $$
Puisque $(A_n)$ croît vers $X$, $(E_i \cap A_n)$ croît vers $E_i \cap X = E_i$. Par la propriété de continuité croissante des mesures (fondamentale pour toute mesure axiomatique), on a $\lim_n \mu(E_i \cap A_n) = \mu(E_i)$.
Ainsi,
$$ \lim_{n \to +\infty} \int_{A_n} s \, d\mu = \sum_{i=1}^k c_i \mu(E_i) = \int_X s \, d\mu. $$
Revenons à l'inégalité de l'intégrale :
$$ \lim_{n \to +\infty} \int_X f_n \, d\mu \ge \alpha \lim_{n \to +\infty} \int_{A_n} s \, d\mu = \alpha \int_X s \, d\mu. $$

**Étape 5 : Conclusion**
L'inégalité $\lim_{n \to +\infty} \int_X f_n \, d\mu \ge \alpha \int_X s \, d\mu$ est vraie pour tout $\alpha \in ]0, 1[$. En faisant tendre $\alpha \to 1$, on obtient :
$$ \lim_{n \to +\infty} \int_X f_n \, d\mu \ge \int_X s \, d\mu. $$
Puisque ceci est vrai pour toute fonction étagée minorant $f$, on prend le suprémum sur toutes ces fonctions $s$, ce qui donne, par définition de l'intégrale de $f$ :
$$ \lim_{n \to +\infty} \int_X f_n \, d\mu \ge \int_X f \, d\mu. $$
Les deux inégalités opposées étant démontrées, l'égalité stricte est établie. La démonstration est achevée.

## 3. L'intégration termes à termes des séries de fonctions

Un corollaire immédiat du théorème de Beppo-Levi, extrêmement utilisé en pratique, concerne l'intégration des séries de fonctions positives.

**Corollaire :**
Soit $(g_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables positives de $X$ dans $\bar{\mathbb{R}}_+$. Alors,
$$ \int_X \left( \sum_{n=0}^{+\infty} g_n(x) \right) d\mu(x) = \sum_{n=0}^{+\infty} \int_X g_n(x) \, d\mu(x). $$

**Démonstration :**
Il suffit de définir la suite des sommes partielles $f_N = \sum_{n=0}^N g_n$. Comme les $g_n$ sont positives, la suite $(f_N)$ est croissante en tout point $x$. Par le théorème de Beppo-Levi appliqué à $(f_N)$, la limite des intégrales des $f_N$ est l'intégrale de la limite (la série infinie). L'intégrale étant linéaire (ce qu'on prouve sur des sommes finies de fonctions positives), l'intégrale de la somme partielle est la somme des intégrales, d'où le résultat par passage à la limite.

**Exemple concret (l'intégrale de Gauss-Poisson) :**
Calculons l'intégrale $I = \int_{0}^{1} \frac{-\ln(x)}{1-x} \, dx$.
On exprime $\frac{1}{1-x}$ comme une somme géométrique : $\frac{1}{1-x} = \sum_{n=0}^{+\infty} x^n$, valable pour $x \in ]0, 1[$.
La fonction à intégrer est $f(x) = \sum_{n=0}^{+\infty} (-x^n \ln(x))$.
Posons $g_n(x) = -x^n \ln(x)$. Sur $]0, 1[$, $\ln(x) < 0$, donc $g_n(x) > 0$. Les $g_n$ sont des fonctions positives mesurables.
Par le corollaire de Beppo-Levi (intégration terme à terme pour les séries à termes positifs) :
$$ \int_{0}^{1} \left( \sum_{n=0}^{+\infty} -x^n \ln(x) \right) dx = \sum_{n=0}^{+\infty} \int_{0}^{1} -x^n \ln(x) \, dx. $$
Pour calculer $\int_0^1 -x^n \ln(x) \, dx$, on procède à une intégration par parties :
$u(x) = -\ln(x) \Rightarrow u'(x) = -1/x$
$v'(x) = x^n \Rightarrow v(x) = \frac{x^{n+1}}{n+1}$
$$ \int_{0}^{1} -x^n \ln(x) \, dx = \left[ -\ln(x) \frac{x^{n+1}}{n+1} \right]_0^1 - \int_0^1 \left(-\frac{1}{x}\right) \frac{x^{n+1}}{n+1} \, dx. $$
Le terme de bord s'annule (en $1$, $\ln(1)=0$; en $0$, limite usuelle $x^\alpha \ln(x) \to 0$).
Reste l'intégrale $\int_0^1 \frac{x^n}{n+1} \, dx = \left[ \frac{x^{n+1}}{(n+1)^2} \right]_0^1 = \frac{1}{(n+1)^2}$.
Finalement, l'intégrale totale est :
$$ I = \sum_{n=0}^{+\infty} \frac{1}{(n+1)^2} = \sum_{k=1}^{+\infty} \frac{1}{k^2} = \frac{\pi^2}{6}. $$
(Problème de Bâle résolu par Euler). Le théorème de convergence monotone garantit la parfaite rigueur de cette interversion.

## 4. Portée en probabilités et en Intelligence Artificielle

En théorie des probabilités (où l'espace mesuré est $(\Omega, \mathcal{F}, \mathbb{P})$), le théorème de Beppo-Levi affirme que pour toute suite croissante de variables aléatoires positives $X_n \nearrow X$, l'espérance mathématique respecte la limite : $\mathbb{E}[X_n] \nearrow \mathbb{E}[X]$.

Dans les algorithmes d'apprentissage statistique, et singulièrement l'algorithme d'Espérance-Maximisation (EM) utilisé pour les modèles à variables latentes (comme les mélanges gaussiens GMM), on construit itérativement une borne inférieure (Evidence Lower Bound - ELBO) de la log-vraisemblance. La mise à jour des paramètres génère une suite de log-vraisemblances empiriques strictement croissantes. Si la fonction de coût (modélisée comme une intégrale d'une densité de probabilité) possède des propriétés d'accroissement monotone, les théorèmes d'interversion de type Beppo-Levi permettent de justifier le passage à la limite sous l'intégrale et d'assurer que l'algorithme converge bien vers un extremum local de la fonction objectif originale, y compris dans des espaces de Hilbert de dimension infinie (comme dans le Variational Inference ou les processus gaussiens). De manière similaire, en analyse convexe stochastique, la convergence de fonctions de coût régularisées repose sur des lois fortes des grands nombres, elles-mêmes établies rigoureusement grâce aux théorèmes de convergence monotone et de convergence dominée.
