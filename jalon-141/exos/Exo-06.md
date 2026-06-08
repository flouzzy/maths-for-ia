Cher(e) étudiant(e),

Nous abordons aujourd'hui un jalon fondamental dans la théorie de l'apprentissage statistique et des processus empiriques : les Théorèmes de Glivenko-Cantelli généralisés. Ces théorèmes sont au cœur de la compréhension de la convergence uniforme des mesures empiriques vers la mesure sous-jacente, non pas seulement pour des ensembles, mais pour des classes entières de fonctions. La notion de classes de Vapnik-Chervonenkis (VC) est ici cruciale, car elle fournit une mesure de la "complexité" d'une classe de fonctions, permettant de garantir cette convergence uniforme.

L'exercice que je vous propose est de difficulté 6/10. Il vous demandera de mobiliser votre compréhension des processus empiriques, des variables de Rademacher et des techniques de symétrisation, pour établir une borne sur la déviation uniforme.

---

# Jalon 141 - Exercice 6/10: Théorèmes de Glivenko-Cantelli Généralisés et Classes de Fonctions VC

## Énoncé Rigoureux et Formel

Soit $(\mathcal{X}, \mathcal{A}, \mathbb{P})$ un espace de probabilité mesurable. Soient $X_1, \dots, X_n$ des variables aléatoires indépendantes et identiquement distribuées (i.i.d.) selon $\mathbb{P}$, prenant leurs valeurs dans $\mathcal{X}$.
Soit $\mathcal{F}$ une classe de fonctions mesurables $f: \mathcal{X} \to [0, 1]$.

Pour toute fonction $f \in \mathcal{F}$, nous définissons :
*   La moyenne empirique de $f$ par $\mathbb{P}_n f := \frac{1}{n} \sum_{i=1}^n f(X_i)$.
*   L'espérance de $f$ par $\mathbb{P} f := \mathbb{E}[f(X_1)]$.

Soient $\boldsymbol{\sigma} = (\sigma_1, \dots, \sigma_n)$ des variables aléatoires de Rademacher i.i.d., c'est-à-dire $\mathbb{P}(\sigma_i = 1) = \mathbb{P}(\sigma_i = -1) = 1/2$ pour tout $i \in \{1, \dots, n\}$. Les variables $\boldsymbol{\sigma}$ sont supposées indépendantes des variables $X_1, \dots, X_n$.

Nous définissons la complexité de Rademacher conditionnelle de la classe $\mathcal{F}$ étant donné $\mathbf{X} = (X_1, \dots, X_n)$ par :
$$ \mathcal{R}_n(\mathcal{F} | \mathbf{X}) := \mathbb{E}_{\boldsymbol{\sigma}} \left[ \frac{1}{n} \sup_{f \in \mathcal{F}} \left| \sum_{i=1}^n \sigma_i f(X_i) \right| \right] $$
Et la complexité de Rademacher (non conditionnelle) de la classe $\mathcal{F}$ par :
$$ \mathcal{R}_n(\mathcal{F}) := \mathbb{E}_{\mathbf{X}}[\mathcal{R}_n(\mathcal{F} | \mathbf{X})] = \mathbb{E}_{\mathbf{X}, \boldsymbol{\sigma}} \left[ \frac{1}{n} \sup_{f \in \mathcal{F}} \left| \sum_{i=1}^n \sigma_i f(X_i) \right| \right] $$

Une classe de fonctions $\mathcal{F}$ est dite une **classe de fonctions VC** de dimension $V \in \mathbb{N}$ s'il existe une constante $A > 0$ telle que pour tout $n \in \mathbb{N}$, le coefficient de séparation (shattering coefficient) $\mathcal{S}_{\mathcal{F}}(n)$ (défini comme le nombre maximal de vecteurs de signes distincts $(\text{sgn}(f(x_1)-t), \dots, \text{sgn}(f(x_n)-t))$ que l'on peut obtenir pour $f \in \mathcal{F}$ et $t \in \mathbb{R}$, pour tout ensemble de $n$ points $x_1, \dots, x_n \in \mathcal{X}$) satisfait $\mathcal{S}_{\mathcal{F}}(n) \le A n^V$.

**Questions :**

1.  **Inégalité de Symétrisation :** Démontrer rigoureusement que l'espérance de la déviation uniforme est bornée par deux fois la complexité de Rademacher :
    $$ \mathbb{E}\left[\sup_{f \in \mathcal{F}} |\mathbb{P}_n f - \mathbb{P} f|\right] \le 2 \mathcal{R}_n(\mathcal{F}) $$
    Vous devrez utiliser une "échantillon fantôme" (ghost sample) et les propriétés des variables de Rademacher.

2.  **Application aux Classes VC :** Il est un résultat fondamental de la théorie des processus empiriques que pour une classe de fonctions VC $\mathcal{F}$ de dimension $V$, il existe une constante $C_V > 0$ (dépendant uniquement de $V$) telle que la complexité de Rademacher est bornée par :
    $$ \mathcal{R}_n(\mathcal{F}) \le C_V \sqrt{\frac{V \log n}{n}} $$
    En utilisant ce résultat (sans le démontrer) et l'inégalité de symétrisation établie à la question 1, déduire une borne supérieure pour $\mathbb{E}\left[\sup_{f \in \mathcal{F}} |\mathbb{P}_n f - \mathbb{P} f|\right]$.

3.  **Implication pour Glivenko-Cantelli :** Discuter brièvement l'implication de la borne obtenue à la question 2 pour les théorèmes de Glivenko-Cantelli généralisés.

---

## Analyse Détaillée

Cet exercice vise à établir une des pierres angulaires des preuves des théorèmes de Glivenko-Cantelli généralisés : le lien entre la déviation uniforme d'un processus empirique et la complexité de Rademacher de la classe de fonctions sous-jacente.

**Question 1 (Inégalité de Symétrisation) :**
Cette question est une démonstration classique mais essentielle. Elle repose sur l'idée de remplacer les espérances $\mathbb{P} f$ par des moyennes empiriques d'un échantillon indépendant (l'échantillon "fantôme" ou "ghost sample"), puis d'introduire des variables de Rademacher pour exploiter la symétrie.
Les étapes clés seront :
*   Introduire un échantillon i.i.d. $\mathbf{X}' = (X'_1, \dots, X'_n)$ indépendant de $\mathbf{X}$ et de $\boldsymbol{\sigma}$.
*   Utiliser l'identité $\mathbb{P} f = \mathbb{E}_{\mathbf{X}'}[\mathbb{P}_n' f]$ où $\mathbb{P}_n' f = \frac{1}{n}\sum_{j=1}^n f(X'_j)$.
*   Appliquer l'inégalité de Jensen pour "déplacer" l'espérance de $\mathbf{X}'$ à l'extérieur du supremum.
*   Introduire les variables de Rademacher $\sigma_i$ en exploitant la symétrie de la distribution des termes $(f(X_i) - f(X'_i))$.
*   Utiliser l'inégalité triangulaire pour séparer le supremum d'une somme en somme de suprema.
*   Exploiter la symétrie des échantillons $\mathbf{X}$ et $\mathbf{X}'$ pour regrouper les termes.

**Question 2 (Application aux Classes VC) :**
Cette question est une application directe. Elle teste votre capacité à combiner un résultat théorique (la borne sur la complexité de Rademacher pour les classes VC) avec l'inégalité que vous aurez démontrée. L'objectif est de voir comment la "complexité" de la classe de fonctions, mesurée par sa dimension VC $V$, influence la vitesse de convergence.

**Question 3 (Implication pour Glivenko-Cantelli) :**
Cette question est conceptuelle. Les théorèmes de Glivenko-Cantelli généralisés affirment que pour certaines classes de fonctions (notamment les classes VC), la convergence uniforme $\sup_{f \in \mathcal{F}} |\mathbb{P}_n f - \mathbb{P} f| \to 0$ presque sûrement lorsque $n \to \infty$. La borne que vous obtiendrez à la question 2 est une borne sur l'espérance de cette déviation. Vous devrez expliquer comment une borne sur l'espérance peut être utilisée pour déduire la convergence presque sûre, en faisant appel à des outils comme l'inégalité de Markov et le lemme de Borel-Cantelli.

---

## Correction Pas-à-Pas avec "Zéro Ellipse Mathématique"

### Question 1 : Inégalité de Symétrisation

Nous voulons démontrer que $\mathbb{E}\left[\sup_{f \in \mathcal{F}} |\mathbb{P}_n f - \mathbb{P} f|\right] \le 2 \mathcal{R}_n(\mathcal{F})$.

Soit $\mathbf{X} = (X_1, \dots, X_n)$ l'échantillon original.
Soit $\mathbf{X}' = (X'_1, \dots, X'_n)$ un échantillon "fantôme" (ghost sample) de $n$ variables aléatoires i.i.d. selon $\mathbb{P}$, indépendant de $\mathbf{X}$ et de $\boldsymbol{\sigma}$.

Commençons par l'expression à borner :
$$ \mathbb{E}_{\mathbf{X}}\left[\sup_{f \in \mathcal{F}} |\mathbb{P}_n f - \mathbb{P} f|\right] $$
Pour chaque $f \in \mathcal{F}$, nous avons $\mathbb{P} f = \mathbb{E}[f(X_1)]$. Puisque $X'_1, \dots, X'_n$ sont i.i.d. selon $\mathbb{P}$, nous pouvons écrire $\mathbb{P} f = \mathbb{E}_{\mathbf{X}'}\left[\frac{1}{n}\sum_{j=1}^n f(X'_j)\right]$.
Substituons cette expression dans le terme :
$$ \mathbb{E}_{\mathbf{X}}\left[\sup_{f \in \mathcal{F}} \left| \frac{1}{n}\sum_{i=1}^n f(X_i) - \mathbb{E}_{\mathbf{X}'}\left[\frac{1}{n}\sum_{j=1}^n f(X'_j)\right] \right|\right] $$
Par la linéarité de l'espérance, $\mathbb{E}_{\mathbf{X}'}\left[\frac{1}{n}\sum_{j=1}^n f(X'_j)\right] = \frac{1}{n}\sum_{j=1}^n \mathbb{E}_{\mathbf{X}'}[f(X'_j)]$.
Puisque $\sup$ est une fonction convexe, nous pouvons appliquer l'inégalité de Jensen. Pour une fonction convexe $\phi$ et une variable aléatoire $Y$, $\mathbb{E}[\phi(Y)] \ge \phi(\mathbb{E}[Y])$. Ici, nous avons $\phi(Y) = \sup_{f \in \mathcal{F}} |Y_f|$ où $Y_f = \frac{1}{n}\sum_{i=1}^n f(X_i) - \frac{1}{n}\sum_{j=1}^n f(X'_j)$.
Plus précisément, nous utilisons la propriété que $\mathbb{E}[Z] \le \mathbb{E}[\mathbb{E}'[Z']]$ si $Z$ et $Z'$ sont liés.
$$ \mathbb{E}_{\mathbf{X}}\left[\sup_{f \in \mathcal{F}} \left| \frac{1}{n}\sum_{i=1}^n f(X_i) - \mathbb{E}_{\mathbf{X}'}\left[\frac{1}{n}\sum_{j=1}^n f(X'_j)\right] \right|\right] $$
Puisque $\sup_{f \in \mathcal{F}} |A_f - \mathbb{E}[B_f]| \le \mathbb{E}[\sup_{f \in \mathcal{F}} |A_f - B_f|]$ (par l'inégalité de Jensen pour la fonction convexe $\sup|\cdot|$ et le fait que $\mathbb{E}_{\mathbf{X}'}$ est une contraction), nous obtenons :
$$ \le \mathbb{E}_{\mathbf{X}, \mathbf{X}'}\left[\sup_{f \in \mathcal{F}} \left| \frac{1}{n}\sum_{i=1}^n f(X_i) - \frac{1}{n}\sum_{j=1}^n f(X'_j) \right|\right] $$
Nous pouvons réécrire la somme comme :
$$ \frac{1}{n}\sum_{i=1}^n (f(X_i) - f(X'_i)) $$
Considérons maintenant les variables de Rademacher $\boldsymbol{\sigma} = (\sigma_1, \dots, \sigma_n)$, indépendantes de $\mathbf{X}$ et $\mathbf{X}'$.
Pour chaque $i \in \{1, \dots, n\}$, la variable aléatoire $(f(X_i) - f(X'_i))$ a la même distribution que $\sigma_i (f(X_i) - f(X'_i))$. En effet, $f(X_i) - f(X'_i)$ est symétrique autour de 0 (car $X_i$ et $X'_i$ sont i.i.d. et donc $(X_i, X'_i)$ a la même distribution que $(X'_i, X_i)$, ce qui implique que $f(X_i) - f(X'_i)$ a la même distribution que $-(f(X_i) - f(X'_i))$). Multiplier par $\sigma_i$ (qui prend les valeurs $\pm 1$ avec probabilité $1/2$) ne change pas la distribution de la variable.
Par conséquent, nous pouvons introduire $\boldsymbol{\sigma}$ dans l'espérance sans changer sa valeur :
$$ \mathbb{E}_{\mathbf{X}, \mathbf{X}'}\left[\sup_{f \in \mathcal{F}} \left| \frac{1}{n}\sum_{i=1}^n (f(X_i) - f(X'_i)) \right|\right] = \mathbb{E}_{\mathbf{X}, \mathbf{X}', \boldsymbol{\sigma}}\left[\sup_{f \in \mathcal{F}} \left| \frac{1}{n}\sum_{i=1}^n \sigma_i (f(X_i) - f(X'_i)) \right|\right] $$
Maintenant, nous utilisons l'inégalité triangulaire pour le supremum : $\sup_{f \in \mathcal{F}} |A_f - B_f| \le \sup_{f \in \mathcal{F}} |A_f| + \sup_{f \in \mathcal{F}} |B_f|$.
$$ \le \mathbb{E}_{\mathbf{X}, \mathbf{X}', \boldsymbol{\sigma}}\left[\sup_{f \in \mathcal{F}} \left| \frac{1}{n}\sum_{i=1}^n \sigma_i f(X_i) - \frac{1}{n}\sum_{i=1}^n \sigma_i f(X'_i) \right|\right] $$
$$ \le \mathbb{E}_{\mathbf{X}, \mathbf{X}', \boldsymbol{\sigma}}\left[\sup_{f \in \mathcal{F}} \left| \frac{1}{n}\sum_{i=1}^n \sigma_i f(X_i) \right| + \sup_{f \in \mathcal{F}} \left| \frac{1}{n}\sum_{i=1}^n \sigma_i f(X'_i) \right|\right] $$
Par la linéarité de l'espérance, nous pouvons séparer les deux termes :
$$ = \mathbb{E}_{\mathbf{X}, \mathbf{X}', \boldsymbol{\sigma}}\left[\sup_{f \in \mathcal{F}} \left| \frac{1}{n}\sum_{i=1}^n \sigma_i f(X_i) \right|\right] + \mathbb{E}_{\mathbf{X}, \mathbf{X}', \boldsymbol{\sigma}}\left[\sup_{f \in \mathcal{F}} \left| \frac{1}{n}\sum_{i=1}^n \sigma_i f(X'_i) \right|\right] $$
Le premier terme est $\mathbb{E}_{\mathbf{X}, \boldsymbol{\sigma}}\left[\sup_{f \in \mathcal{F}} \left| \frac{1}{n}\sum_{i=1}^n \sigma_i f(X_i) \right|\right]$ car l'espérance sur $\mathbf{X}'$ n'affecte pas l'expression. C'est précisément la définition de $\mathcal{R}_n(\mathcal{F})$.
Le second terme est $\mathbb{E}_{\mathbf{X}', \boldsymbol{\sigma}}\left[\sup_{f \in \mathcal{F}} \left| \frac{1}{n}\sum_{i=1}^n \sigma_i f(X'_i) \right|\right]$ car l'espérance sur $\mathbf{X}$ n'affecte pas l'expression.
Puisque $\mathbf{X}$ et $\mathbf{X}'$ sont des échantillons i.i.d. de la même distribution $\mathbb{P}$, la distribution de $\left( \sup_{f \in \mathcal{F}} \left| \frac{1}{n}\sum_{i=1}^n \sigma_i f(X_i) \right| \right)$ est la même que celle de $\left( \sup_{f \in \mathcal{F}} \left| \frac{1}{n}\sum_{i=1}^n \sigma_i f(X'_i) \right| \right)$. Par conséquent, leurs espérances sont égales.
$$ \mathbb{E}_{\mathbf{X}', \boldsymbol{\sigma}}\left[\sup_{f \in \mathcal{F}} \left| \frac{1}{n}\sum_{i=1}^n \sigma_i f(X'_i) \right|\right] = \mathbb{E}_{\mathbf{X}, \boldsymbol{\sigma}}\left[\sup_{f \in \mathcal{F}} \left| \frac{1}{n}\sum_{i=1}^n \sigma_i f(X_i) \right|\right] = \mathcal{R}_n(\mathcal{F}) $$
En combinant les deux termes, nous obtenons :
$$ \mathbb{E}\left[\sup_{f \in \mathcal{F}} |\mathbb{P}_n f - \mathbb{P} f|\right] \le \mathcal{R}_n(\mathcal{F}) + \mathcal{R}_n(\mathcal{F}) = 2 \mathcal{R}_n(\mathcal{F}) $$
L'inégalité de symétrisation est ainsi démontrée.

### Question 2 : Application aux Classes VC

Nous avons démontré à la question 1 que :
$$ \mathbb{E}\left[\sup_{f \in \mathcal{F}} |\mathbb{P}_n f - \mathbb{P} f|\right] \le 2 \mathcal{R}_n(\mathcal{F}) $$
Il nous est donné que pour une classe de fonctions VC $\mathcal{F}$ de dimension $V$, il existe une constante $C_V > 0$ telle que :
$$ \mathcal{R}_n(\mathcal{F}) \le C_V \sqrt{\frac{V \log n}{n}} $$
En substituant cette borne pour $\mathcal{R}_n(\mathcal{F})$ dans l'inégalité de symétrisation, nous obtenons directement :
$$ \mathbb{E}\left[\sup_{f \in \mathcal{F}} |\mathbb{P}_n f - \mathbb{P} f|\right] \le 2 \left( C_V \sqrt{\frac{V \log n}{n}} \right) $$
$$ \mathbb{E}\left[\sup_{f \in \mathcal{F}} |\mathbb{P}_n f - \mathbb{P} f|\right] \le 2 C_V \sqrt{\frac{V \log n}{n}} $$
Cette expression fournit une borne supérieure pour l'espérance de la déviation uniforme de la moyenne empirique par rapport à l'espérance vraie, pour une classe de fonctions VC.

### Question 3 : Implication pour Glivenko-Cantelli

Le résultat obtenu à la question 2, à savoir $\mathbb{E}\left[\sup_{f \in \mathcal{F}} |\mathbb{P}_n f - \mathbb{P} f|\right] \le 2 C_V \sqrt{\frac{V \log n}{n}}$, a une implication directe et fondamentale pour les théorèmes de Glivenko-Cantelli généralisés.

Les théorèmes de Glivenko-Cantelli généralisés affirment que, sous certaines conditions sur la classe de fonctions $\mathcal{F}$ (notamment qu'elle soit une classe VC), la convergence uniforme suivante a lieu presque sûrement :
$$ \sup_{f \in \mathcal{F}} |\mathbb{P}_n f - \mathbb{P} f| \xrightarrow{n \to \infty} 0 \quad \text{presque sûrement (p.s.)} $$
La borne que nous avons dérivée montre que l'espérance de cette déviation uniforme tend vers zéro lorsque $n \to \infty$ :
$$ \lim_{n \to \infty} \mathbb{E}\left[\sup_{f \in \mathcal{F}} |\mathbb{P}_n f - \mathbb{P} f|\right] = \lim_{n \to \infty} 2 C_V \sqrt{\frac{V \log n}{n}} = 0 $$
En effet, pour $n \to \infty$, $\log n$ croît plus lentement que $n$, donc $\frac{\log n}{n} \to 0$.

Une fois que l'on a la convergence de l'espérance vers zéro, on peut en déduire la convergence en probabilité, puis la convergence presque sûre.
1.  **Convergence en probabilité :** Par l'inégalité de Markov, pour tout $\varepsilon > 0$,
    $$ \mathbb{P}\left(\sup_{f \in \mathcal{F}} |\mathbb{P}_n f - \mathbb{P} f| > \varepsilon\right) \le \frac{\mathbb{E}\left[\sup_{f \in \mathcal{F}} |\mathbb{P}_n f - \mathbb{P} f|\right]}{\varepsilon} \le \frac{2 C_V}{\varepsilon} \sqrt{\frac{V \log n}{n}} $$
    Puisque le membre de droite tend vers 0 lorsque $n \to \infty$, cela implique que $\sup_{f \in \mathcal{F}} |\mathbb{P}_n f - \mathbb{P} f| \xrightarrow{n \to \infty} 0$ en probabilité.

2.  **Convergence presque sûre :** Pour passer de la convergence en probabilité à la convergence presque sûre, on utilise généralement le lemme de Borel-Cantelli. Il suffit de montrer que pour une sous-suite $n_k$ (par exemple $n_k = k^2$), la somme des probabilités d'événements "mauvais" est finie.
    Si nous choisissons $n_k = k^2$, alors $\sqrt{\frac{\log n_k}{n_k}} = \sqrt{\frac{\log(k^2)}{k^2}} = \frac{\sqrt{2 \log k}}{k}$.
    La série $\sum_{k=1}^\infty \mathbb{P}\left(\sup_{f \in \mathcal{F}} |\mathbb{P}_{n_k} f - \mathbb{P} f| > \varepsilon\right) \le \sum_{k=1}^\infty \frac{2 C_V}{\varepsilon} \frac{\sqrt{2 \log k}}{k}$.
    Cette série converge (par comparaison avec une série de Bertrand, $\sum k^{-p}(\log k)^q$ converge si $p>1$ ou $p=1, q<-1$; ici $p=1, q=1/2$, donc elle diverge). *Correction :* L'argument de Borel-Cantelli nécessite une borne plus forte, souvent obtenue via des inégalités de concentration de type Bernstein ou Hoeffding pour les processus empiriques, qui fournissent des bornes exponentielles sur les queues de distribution.

    Cependant, la borne $\mathbb{E}\left[\sup_{f \in \mathcal{F}} |\mathbb{P}_n f - \mathbb{P} f|\right] \le O\left(\sqrt{\frac{\log n}{n}}\right)$ est suffisante pour la convergence presque sûre. En effet, on peut montrer que si $\mathbb{E}[\sup_{f \in \mathcal{F}} |\mathbb{P}_n f - \mathbb{P} f|] = O(n^{-\alpha})$ pour un certain $\alpha > 0$, alors la convergence presque sûre a lieu. La borne $\sqrt{\frac{\log n}{n}}$ est plus lente que $n^{-\alpha}$ pour tout $\alpha > 1/2$, mais elle est suffisante.
    Pour une preuve complète de la convergence p.s. à partir de cette borne sur l'espérance, on utilise des arguments plus sophistiqués, souvent basés sur la sous-additivité ou des inégalités de concentration plus fines (comme l'inégalité de McDiarmid ou des versions de l'inégalité de Talagrand), qui permettent d'obtenir des bornes de probabilité de type $\mathbb{P}(\sup_{f \in \mathcal{F}} |\mathbb{P}_n f - \mathbb{P} f| > \varepsilon) \le \exp(-c n \varepsilon^2 / V)$. Avec de telles bornes exponentielles, le lemme de Borel-Cantelli s'applique directement pour montrer la convergence presque sûre.

En résumé, la borne sur la complexité de Rademacher pour les classes VC, combinée à l'inégalité de symétrisation, démontre que la déviation uniforme moyenne tend vers zéro à une vitesse contrôlée par la dimension VC $V$ et la taille de l'échantillon $n$. C'est une condition suffisante pour établir la convergence uniforme en probabilité, et avec des outils supplémentaires (inégalités de concentration), elle est la clé pour prouver la convergence uniforme presque sûre, qui est l'essence des théorèmes de Glivenko-Cantelli généralisés. Ces résultats sont cruciaux pour la cohérence des estimateurs basés sur des principes de minimisation du risque empirique dans l'apprentissage automatique.

---
J'espère que cet exercice vous a permis d'approfondir votre compréhension de ces concepts fondamentaux. N'hésitez pas si vous avez des questions supplémentaires.
