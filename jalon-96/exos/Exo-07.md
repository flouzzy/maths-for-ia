Niveau de difficulté : $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $P$ une distribution cible sur l'alphabet $\mathcal{X} = \{a, b, c\}$ avec $P(a) = \frac{1}{2}$, $P(b) = \frac{1}{4}$, $P(c) = \frac{1}{4}$.
Un modèle de langage prédit la distribution $Q$ telle que $Q(a) = \frac{1}{3}$, $Q(b) = \frac{1}{3}$, $Q(c) = \frac{1}{3}$.
1. Calculez l'entropie de Shannon $H(P)$.
2. Calculez l'entropie croisée $H(P, Q)$.
3. Calculez la divergence de Kullback-Leibler $D_{KL}(P || Q)$ et vérifiez la relation $H(P, Q) = H(P) + D_{KL}(P || Q)$.

**Corrigé :**
1. L'entropie de Shannon $H(P)$ est donnée par :
$$H(P) = - \sum_{x \in \mathcal{X}} P(x) \log_2 P(x)$$
$$H(P) = - \left( \frac{1}{2} \log_2\left(\frac{1}{2}\right) + \frac{1}{4} \log_2\left(\frac{1}{4}\right) + \frac{1}{4} \log_2\left(\frac{1}{4}\right) \right)$$
$$H(P) = - \left( \frac{1}{2}(-1) + \frac{1}{4}(-2) + \frac{1}{4}(-2) \right) = \frac{1}{2} + \frac{1}{2} + \frac{1}{2} = 1.5 \text{ bits}.$$

2. L'entropie croisée $H(P, Q)$ est :
$$H(P, Q) = - \sum_{x \in \mathcal{X}} P(x) \log_2 Q(x)$$
$$H(P, Q) = - \left( \frac{1}{2} \log_2\left(\frac{1}{3}\right) + \frac{1}{4} \log_2\left(\frac{1}{3}\right) + \frac{1}{4} \log_2\left(\frac{1}{3}\right) \right)$$
$$H(P, Q) = - \left( \frac{1}{2} + \frac{1}{4} + \frac{1}{4} \right) \log_2\left(\frac{1}{3}\right) = - \log_2\left(\frac{1}{3}\right) = \log_2(3) \approx 1.58496 \text{ bits}.$$

3. La divergence KL est :
$$D_{KL}(P || Q) = \sum_{x \in \mathcal{X}} P(x) \log_2 \left(\frac{P(x)}{Q(x)}\right)$$
$$D_{KL}(P || Q) = \frac{1}{2} \log_2\left(\frac{1/2}{1/3}\right) + \frac{1}{4} \log_2\left(\frac{1/4}{1/3}\right) + \frac{1}{4} \log_2\left(\frac{1/4}{1/3}\right)$$
$$D_{KL}(P || Q) = \frac{1}{2} \log_2\left(\frac{3}{2}\right) + \frac{1}{2} \log_2\left(\frac{3}{4}\right)$$
$$D_{KL}(P || Q) = \frac{1}{2} (\log_2 3 - 1) + \frac{1}{2} (\log_2 3 - 2) = \log_2 3 - 1.5 \approx 0.08496 \text{ bits}.$$
On vérifie bien : $H(P, Q) = 1.5 + (\log_2 3 - 1.5) = \log_2 3 \approx 1.58496$, ce qui correspond au résultat de la question 2.
