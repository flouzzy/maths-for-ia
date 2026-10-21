# Exercice 5 : Perplexité et Entropie

$\bigstar\bigstar\bigstar\star\star$


En traitement du langage naturel (NLP), la qualité d'un modèle de langage est souvent mesurée par sa perplexité, définie comme $PP = \exp(H(P, Q))$.

Soit une langue imaginaire constituée de seulement $N=10^4$ mots possibles. On suppose que la distribution réelle $P$ est uniforme sur l'ensemble de ces mots. Un modèle imparfait $Q$ modélise cette distribution comme uniforme sur un sous-ensemble strict de $K=10^3$ mots (et 0 pour les autres).

**1.** Calculer la perplexité du modèle parfait ($Q=P$).
**2.** Pourquoi la perplexité du modèle imparfait $Q$ est-elle infinie (et l'entropie croisée infinie) ?

**Correction :**

**1.** Pour le modèle parfait, $Q=P$. La distribution est uniforme sur $N$ mots, donc $p(x) = \frac{1}{N}$.
L'entropie croisée est :
$$H(P, P) = H(P) = - \sum_{x} p(x) \ln p(x) = - \sum_{x=1}^{N} \frac{1}{N} \ln\left(\frac{1}{N}\right) = \ln(N)$$
La perplexité est donc :
$$PP = \exp(H(P)) = \exp(\ln(N)) = N = 10^4$$
La perplexité d'une distribution uniforme est exactement le nombre de choix possibles.

**2.** Pour le modèle imparfait $Q$, il existe au moins un mot $x^*$ tel que $p(x^*) = \frac{1}{N} > 0$ mais $q(x^*) = 0$ (car le support de $Q$ est plus petit que celui de $P$).
L'entropie croisée contient le terme :
$$- p(x^*) \ln(q(x^*)) = - \frac{1}{N} \ln(0)$$
Or $\lim_{z \to 0^+} \ln(z) = -\infty$, donc le terme tend vers $+\infty$.
L'entropie croisée est infinie. Par conséquent, la perplexité l'est aussi.
Cela illustre un principe de base en IA : un modèle ne doit jamais assigner une probabilité strictement nulle à un événement possible, sinon il encourt une pénalité infinie s'il est surpris par la réalité.
