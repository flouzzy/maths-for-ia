---
uuid: "jalon-91"
title: "Inégalités de concentration"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/theorie
prev: "[[Jalon 90 (Les modes de convergence).md]]"
next: "[[Jalon 92 (Démonstration rigoureuse de la loi forte des grands nombres.).md]]"
---

# Jalon 91 : Inégalités de concentration

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez que vous soyez le gérant d'un restaurant. Vous savez qu'en moyenne, un client dépense 20€.
    - **Markov :** C'est le niveau de base. Il dit : "Il est impossible que tout le monde dépense 200€, car alors la moyenne ne pourrait pas être 20€". Plus vous demandez un écart grand par rapport à la moyenne, plus la chance que cela arrive diminue.
    - **Tchebychev :** C'est plus précis. Si vous savez aussi que les dépenses sont très régulières (petite variance), vous pouvez être presque sûr que personne ne dépensera 100€.
    - **Hoeffding / Chernoff :** C'est le niveau expert. Si vous avez des milliers de clients indépendants, la probabilité que la moyenne de la journée s'éloigne de 20€ devient **incroyablement petite**, elle s'écrase vers zéro à une vitesse folle (exponentielle).
- **Le "Pourquoi on a inventé ça" :** En science, on ne connaît jamais tout. On a souvent juste une moyenne ou une variance. Les inégalités de concentration nous permettent de dire : "Je ne sais pas exactement ce qui va se passer, mais je peux vous garantir avec 99,9% de certitude que l'erreur ne dépassera pas telle valeur".
- **Visualisation :** Une cloche de probabilité. L'aire des "queues" (les événements extrêmes) devient minuscule très rapidement quand on s'éloigne du centre.

## 2. Formalisation & Rigueur Académique

### A. Inégalité de Markov (Le socle)

> **Théorème 1 :**
> Soit $X$ une variable aléatoire positive admettant une espérance. Pour tout $a > 0$ :
> $$P(X \ge a) \le \frac{\mathbb{E}[X]}{a}$$

### B. Inégalité de Bienaymé-Tchebychev

> **Théorème 2 :**
> Soit $X$ une variable aléatoire admettant une variance $\sigma^2$. Pour tout $\epsilon > 0$ :
> $$P(|X - \mathbb{E}[X]| \ge \epsilon) \le \frac{Var(X)}{\epsilon^2}$$

### C. Inégalité de Hoeffding (Concentration exponentielle)

> **Théorème 3 :**
> Soient $X_1, \dots, X_n$ des variables aléatoires **indépendantes** telles que $X_i \in [a_i, b_i]$. Soit $S_n = \sum X_i$. Pour tout $t > 0$ :
> $$P(S_n - \mathbb{E}[S_n] \ge t) \le \exp\left( - \frac{2t^2}{\sum (b_i - a_i)^2} \right)$$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : De Markov à Tchebychev

1. **Cadre :** Soit $X$ une V.A. de moyenne $\mu$ et de variance $\sigma^2$. Soit $\epsilon > 0$.
2. **Transformation :** L'événement $\{ |X - \mu| \ge \epsilon \}$ est identique à l'événement $\{ (X - \mu)^2 \ge \epsilon^2 \}$.
3. **Application de Markov :** Posons $Y = (X - \mu)^2$. $Y$ est une variable aléatoire **positive**. Son espérance est $\mathbb{E}[Y] = Var(X) = \sigma^2$.
   D'après l'inégalité de Markov appliquée à $Y$ avec le seuil $a = \epsilon^2$ :
   $$P(Y \ge \epsilon^2) \le \frac{\mathbb{E}[Y]}{\epsilon^2}$$
4. **Conclusion :**
   $$P(|X - \mu| \ge \epsilon) \le \frac{\sigma^2}{\epsilon^2}$$

### Principe de l'inégalité de Chernoff

Pour obtenir une décroissance exponentielle, on applique Markov à la variable $e^{\lambda X}$ pour un $\lambda > 0$ bien choisi :
$P(X \ge a) = P(e^{\lambda X} \ge e^{\lambda a}) \le \frac{\mathbb{E}[e^{\lambda X}]}{e^{\lambda a}}$.
On minimise ensuite par rapport à $\lambda$ pour obtenir la borne la plus serrée possible.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Sondage d'opinion
**Énoncé :** On veut estimer la proportion $p$ de gens votant "Oui" dans une population. On interroge $n$ personnes. On veut que notre erreur soit inférieure à $1\%$ avec une confiance de $95\%$. Combien de personnes faut-il interroger (via Tchebychev) ?
**Correction Détaillée :**
1. Soit $\bar{X}_n$ la moyenne des votes (0 ou 1). $\mathbb{E}[\bar{X}_n] = p$ and $Var(\bar{X}_n) = \frac{p(1-p)}{n} \le \frac{1}{4n}$ (le max est pour $p=0.5$).
2. On veut $P(|\bar{X}_n - p| \ge 0.01) \le 0.05$.
3. Tchebychev : $P \le \frac{1/4n}{(0.01)^2} = \frac{1}{0.0004 n} = \frac{2500}{n}$.
4. On pose $\frac{2500}{n} = 0.05 \implies n = \frac{2500}{0.05} = 50,000$.
*Note : Avec Hoeffding, on trouverait un nombre beaucoup plus petit (environ 18,000), illustrant la puissance de la concentration exponentielle.*

### Exercice 2 : Niveau Avancé (Loi des grands nombres faible)
**Énoncé :** Utiliser Tchebychev pour prouver que si $X_i$ sont IID de variance finie, alors $\bar{X}_n \xrightarrow{P} \mathbb{E}[X]$.
**Correction Détaillée :**
C'est immédiat : $P(|\bar{X}_n - \mu| \ge \epsilon) \le \frac{\sigma^2}{n\epsilon^2}$. Quand $n \to \infty$, cette probabilité tend vers 0 pour tout $\epsilon > 0$. C'est la définition de la convergence en probabilité.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Les inégalités de concentration sont le fondement de la **Théorie de l'Apprentissage Statistique** (Statistical Learning Theory). Elles permettent de borner l'erreur de généralisation.
- **Example Concret :**
    - **Bornes PAC (Probably Approximately Correct) :** On prouve qu'avec $N$ exemples, la probabilité que notre modèle soit "très mauvais" est inférieure à $\delta$. La formule de Hoeffding donne typiquement $N \ge \frac{1}{2\epsilon^2} \ln(2/\delta)$. C'est ce qui nous dit combien de données sont nécessaires pour apprendre une tâche.
    - **Multi-Armed Bandits :** L'algorithme **UCB** (Upper Confidence Bound) utilise des inégalités de concentration pour décider quel bras de levier tirer. Il calcule une "borne supérieure de confiance" sur le gain de chaque bras et choisit le plus prometteur.
    - **Stabilité de la SGD :** On utilise ces inégalités pour garantir que les trajectoires de l'optimisation ne s'éloignent pas trop du chemin idéal, malgré le bruit des mini-batchs.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 87 (Intégration et Espérance mathématique).md]], [[Jalon 88 (Indépendance d'événements et de variables aléatoires).md]]
- **Concepts Futurs dépendants :** [[Jalon 92 (Démonstration rigoureuse de la loi forte des grands nombres.).md]], [[Jalon 137 (Preuve des bornes de generalisation universelles de Vapnik via la dimension VC).md]]
