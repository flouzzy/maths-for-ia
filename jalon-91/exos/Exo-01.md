# Exercice 1 : Application directe de Markov

$\bigstar\star\star\star\star$

**Énoncé :**
Un serveur informatique reçoit en moyenne $500$ requêtes par minute. On suppose que le nombre de requêtes $X$ est une variable aléatoire à valeurs dans $\mathbb{N}$.
Montrer que la probabilité de recevoir plus de $2000$ requêtes en une minute est au plus de $25\%$.

**Correction :**
La variable $X$ représentant un nombre de requêtes est positive ou nulle ($X \ge 0$).
On nous donne l'espérance de $X$ : $\mathbb{E}[X] = 500$.
On cherche à majorer la probabilité de l'événement $\{X \ge 2000\}$.
Puisque $X \ge 0$ et admet une espérance finie, on peut appliquer l'inégalité de Markov pour $a = 2000 > 0$.
L'inégalité stipule que :
$$ \mathbb{P}(X \ge a) \le \frac{\mathbb{E}[X]}{a} $$
En remplaçant par les valeurs numériques :
$$ \mathbb{P}(X \ge 2000) \le \frac{500}{2000} $$
En simplifiant la fraction :
$$ \frac{500}{2000} = \frac{1}{4} = 0.25 $$
Ainsi, $\mathbb{P}(X \ge 2000) \le 25\%$.
La démonstration est terminée, sans supposer aucune loi de probabilité spécifique pour $X$ (comme une loi de Poisson par exemple).
