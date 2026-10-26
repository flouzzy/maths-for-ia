# Exercice 2 : Inégalité de Bienaymé-Tchebychev

$\bigstar\star\star\star\star$

**Énoncé :**
La tension délivrée par un générateur électrique est une variable aléatoire $U$. On sait que l'espérance de la tension est $\mathbb{E}[U] = 220$ Volts, et son écart-type est $\sigma = 5$ Volts.
Quelle est la garantie de trouver la tension entre $205$ Volts et $235$ Volts ?

**Correction :**
Nous cherchons à minorer la probabilité de l'événement $\{205 \le U \le 235\}$.
On peut réécrire cet événement sous la forme d'un écart à la moyenne. Puisque $\mu = 220$, on remarque que :
$$ 205 \le U \le 235 \iff -15 \le U - 220 \le 15 \iff |U - \mu| \le 15 $$
Nous cherchons donc à minorer $\mathbb{P}(|U - \mu| \le 15)$.
L'événement contraire est $\{|U - \mu| > 15\}$.
Puisque $U$ a une variance finie $\sigma^2 = 5^2 = 25$, on applique l'inégalité de Bienaymé-Tchebychev :
$$ \mathbb{P}(|U - \mu| \ge a) \le \frac{\sigma^2}{a^2} $$
Ici, $a = 15$.
$$ \mathbb{P}(|U - 220| \ge 15) \le \frac{25}{15^2} = \frac{25}{225} $$
En simplifiant :
$$ \frac{25}{225} = \frac{1}{9} $$
Par passage à l'événement complémentaire :
$$ \mathbb{P}(|U - 220| \le 15) = 1 - \mathbb{P}(|U - 220| > 15) \ge 1 - \frac{1}{9} $$
$$ \mathbb{P}(205 \le U \le 235) \ge \frac{8}{9} $$
La probabilité est donc d'au moins $\frac{8}{9}$ (soit environ $88.89\%$).
