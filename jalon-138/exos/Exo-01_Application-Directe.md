# Exercice 1 : Limites des inégalités de Markov et Bienaymé-Tchebychev (Niveau 1)

## Énoncé
Soit $X$ une variable aléatoire réelle positive de moyenne $\mathbb{E}[X] = \mu$ et de variance $\text{Var}(X) = \sigma^2$.
1. Rappeler l'inégalité de Markov pour $X$ et donner un exemple de loi de probabilité pour laquelle l'inégalité est une égalité (cas d'égalité de Markov).
2. Rappeler l'inégalité de Bienaymé-Tchebychev pour $X$ et démontrer qu'elle est également optimale en construisant une variable aléatoire discrète qui sature cette borne.
3. Discuter de la lenteur de la décroissance de la queue de distribution fournie par ces deux inégalités par rapport aux bornes de concentration exponentielles.

---

## Correction Détaillée

### 1. Inégalité de Markov et cas d'égalité
L'inégalité de Markov s'énonce ainsi : pour toute variable aléatoire réelle positive $X$ de moyenne finie et pour tout $t > 0$ :
$$\mathbb{P}(X \ge t) \le \frac{\mathbb{E}[X]}{t}$$

Pour trouver une loi de probabilité saturant cette borne, considérons une variable aléatoire discrète $X$ prenant deux valeurs : $0$ et $t$.
Posons la loi de $X$ comme suit :
$$\mathbb{P}(X = t) = p \quad \text{et} \quad \mathbb{P}(X = 0) = 1-p$$
où $p \in [0, 1]$.
Calculons la moyenne de $X$ :
$$\mathbb{E}[X] = 0 \times (1-p) + t \times p = t p$$

Pour cette variable aléatoire, nous avons :
$$\mathbb{P}(X \ge t) = \mathbb{P}(X = t) = p$$
D'autre part, la borne de Markov donne :
$$\frac{\mathbb{E}[X]}{t} = \frac{t p}{t} = p$$
On constate que $\mathbb{P}(X \ge t) = \frac{\mathbb{E}[X]}{t}$, la borne de Markov est donc saturée (cas d'égalité).

### 2. Inégalité de Bienaymé-Tchebychev et cas d'égalité
L'inégalité de Bienaymé-Tchebychev s'énonce ainsi : pour toute variable aléatoire $X$ admettant une variance $\sigma^2$ et de moyenne $\mu$ :
$$\mathbb{P}(|X - \mu| \ge t) \le \frac{\sigma^2}{t^2}$$

Pour saturer cette inégalité pour un seuil $t > 0$ donné, définissons une variable aléatoire symétrique $X$ prenant trois valeurs : $\mu - t$, $\mu$ et $\mu + t$.
Posons sa loi de probabilité :
$$\mathbb{P}(X = \mu - t) = \frac{p}{2}, \quad \mathbb{P}(X = \mu + t) = \frac{p}{2}, \quad \text{et} \quad \mathbb{P}(X = \mu) = 1 - p$$
où $p \in (0, 1]$$.
Calculons l'espérance de $X$ :
$$\mathbb{E}[X] = (\mu - t)\frac{p}{2} + (\mu + t)\frac{p}{2} + \mu(1-p) = \mu$$
L'espérance est bien $\mu$. Calculons maintenant la variance :
$$\text{Var}(X) = \mathbb{E}[(X - \mu)^2] = (\mu - t - \mu)^2 \frac{p}{2} + (\mu + t - \mu)^2 \frac{p}{2} + (\mu - \mu)^2 (1-p)$$
$$\text{Var}(X) = t^2 \frac{p}{2} + t^2 \frac{p}{2} = p t^2$$
Donc $\sigma^2 = p t^2$, ce qui implique $p = \frac{\sigma^2}{t^2}$.

Pour cette loi, calculons le terme de gauche de l'inégalité :
$$\mathbb{P}(|X - \mu| \ge t) = \mathbb{P}(X = \mu - t) + \mathbb{P}(X = \mu + t) = \frac{p}{2} + \frac{p}{2} = p$$
Et le terme de droite (la borne) :
$$\frac{\sigma^2}{t^2} = \frac{p t^2}{t^2} = p$$
L'inégalité est saturée avec égalité stricte : $\mathbb{P}(|X - \mu| \ge t) = \frac{\sigma^2}{t^2}$.

### 3. Comparaison avec les bornes exponentielles
Bien que ces deux inégalités soient optimales au sens où l'on peut construire des lois de probabilité qui les saturent, elles présentent une limite majeure : leur décroissance est polynomiale. 
- Pour Markov : décroissance en $\mathcal{O}(1/t)$.
- Pour Bienaymé-Tchebychev : décroissance en $\mathcal{O}(1/t^2)$.

Dans les applications de grande dimension et d'apprentissage statistique, une décroissance en $1/t^2$ est insuffisante pour compenser le grand nombre de variables ou la complexité d'une classe de fonctions. Les inégalités de concentration avancées (comme Hoeffding, Chernoff, McDiarmid) tirent parti de l'indépendance de plusieurs variables pour obtenir une décroissance de la forme $\exp(-c t^2)$, dite exponentielle ou sous-gaussienne. Cette décroissance ultra-rapide permet de contrôler les déviations même si le nombre de variables ou la dimension de l'espace tend vers l'infini.
