Niveau de difficulté : $\bigstar\bigstar\star\star\star$

Dans le domaine de l'apprentissage automatique, et plus particulièrement pour les modèles de langage, l'évaluation de la performance des prédictions probabilistes est cruciale. Nous allons explorer trois concepts fondamentaux de la théorie de l'information : l'Entropie de Shannon, la Cross-Entropie et la Divergence de Kullback-Leibler (KL), en les appliquant à un scénario simplifié de prédiction du prochain mot.

Considérons un modèle de langage dont la tâche est de prédire le mot suivant la séquence "Le chien". Notre vocabulaire réduit $\mathcal{V}$ est composé de quatre mots : \{"aboie", "court", "dort", "mange"\}.

Une analyse exhaustive d'un corpus de référence nous donne la distribution de probabilité "vraie" (ou de référence) $p(x)$ pour le mot suivant, où $x \in \mathcal{V}$ :
\begin{itemize}
    \item $p(\text{aboie}) = 0.6$
    \item $p(\text{court}) = 0.2$
    \item $p(\text{dort}) = 0.1$
    \item $p(\text{mange}) = 0.1$
\end{itemize}

Nous avons développé deux modèles de langage différents, M1 et M2, qui, dans le même contexte "Le chien", produisent les distributions de probabilité prédites suivantes :

\textbf{Modèle M1} (distribution $q_1(x)$) :
\begin{itemize}
    \item $q_1(\text{aboie}) = 0.4$
    \item $q_1(\text{court}) = 0.3$
    \item $q_1(\text{dort}) = 0.2$
    \item $q_1(\text{mange}) = 0.1$
\end{itemize}

\textbf{Modèle M2} (distribution $q_2(x)$) :
\begin{itemize}
    \item $q_2(\text{aboie}) = 0.55$
    \item $q_2(\text{court}) = 0.25$
    \item $q_2(\text{dort}) = 0.1$
    \item $q_2(\text{mange}) = 0.1$
\end{itemize}

Pour toutes les questions impliquant des calculs logarithmiques, utilisez le logarithme binaire ($\log_2$) et donnez vos résultats avec quatre décimales.

\textbf{Partie A : L'Entropie de Shannon}

1.  Rappelez la formule de l'Entropie de Shannon $H(p)$ pour une distribution de probabilité discrète $p$.
2.  Calculez l'entropie de la distribution vraie $H(p)$.
3.  Interprétez la valeur obtenue en termes d'incertitude ou de quantité minimale d'information nécessaire pour coder un événement selon la distribution $p$.

\textbf{Partie B : La Cross-Entropie}

1.  Rappelez la formule de la Cross-Entropie $H(p, q)$ entre deux distributions de probabilité discrètes $p$ (vraie) et $q$ (prédite).
2.  Calculez la Cross-Entropie $H(p, q_1)$ entre la distribution vraie $p$ et la distribution prédite par le Modèle M1, $q_1$.
3.  Interprétez la valeur de $H(p, q_1)$ en termes de moyenne des bits nécessaires pour identifier un événement si l'on utilise la distribution $q_1$ pour coder des événements qui suivent en réalité la distribution $p$.

\textbf{Partie C : La Divergence de Kullback-Leibler}

1.  Rappelez la formule de la Divergence de Kullback-Leibler $D_{KL}(p \, || \, q)$ entre deux distributions de probabilité discrètes $p$ et $q$.
2.  Calculez la Divergence de Kullback-Leibler $D_{KL}(p \, || \, q_1)$ entre la distribution vraie $p$ et la distribution prédite par le Modèle M1, $q_1$.
3.  Vérifiez la relation fondamentale entre l'Entropie de Shannon, la Cross-Entropie et la Divergence KL : $H(p, q) = H(p) + D_{KL}(p \, || \, q)$ pour les valeurs que vous avez calculées avec $p$ et $q_1$.
4.  Interprétez la valeur de $D_{KL}(p \, || \, q_1)$ en termes de "perte d'information" ou de "coût" lorsque l'on utilise la distribution $q_1$ pour approximer la distribution $p$.

\textbf{Partie D : Évaluation et Amélioration du Modèle}

1.  Calculez la Cross-Entropie $H(p, q_2)$ entre la distribution vraie $p$ et la distribution prédite par le Modèle M2, $q_2$.
2.  Calculez la Divergence de Kullback-Leibler $D_{KL}(p \, || \, q_2)$ entre la distribution vraie $p$ et la distribution prédite par le Modèle M2, $q_2$.
3.  Comparez les valeurs de Cross-Entropie et de Divergence KL obtenues pour le Modèle M1 et le Modèle M2.
4.  En vous basant sur cette comparaison, expliquez quel modèle est le "meilleur" et pourquoi ces métriques sont utilisées comme fonctions de perte (loss functions) pour entraîner les modèles de langage.

---

\textbf{Corrig\'e}

Pour faciliter les calculs et maintenir la précision requise, nous utiliserons les valeurs approximatives suivantes pour les logarithmes en base 2, arrondies à quatre décimales :
\begin{itemize}
    \item $\log_2(0.6) \approx -0.7370$
    \item $\log_2(0.2) \approx -2.3219$
    \item $\log_2(0.1) \approx -3.3219$
    \item $\log_2(0.4) \approx -1.3219$
    \item $\log_2(0.3) \approx -1.7370$
    \item $\log_2(0.55) \approx -0.8626$
    \item $\log_2(0.25) = -2.0000$ (valeur exacte)
    \item $\log_2(1.5) \approx 0.5850$
    \item $\log_2(0.6667) \approx -0.5850$
    \item $\log_2(0.5) = -1.0000$ (valeur exacte)
    \item $\log_2(1.0) = 0.0000$ (valeur exacte)
    \item $\log_2(1.0909) \approx 0.1265$
    \item $\log_2(0.8) \approx -0.3219$
\end{itemize}

\textbf{Partie A : L'Entropie de Shannon}

1.  \textbf{Formule de l'Entropie de Shannon $H(p)$}\\
    L'Entropie de Shannon pour une distribution de probabilité discrète $p$ sur un ensemble d'événements $\mathcal{X}$ est définie par :
    $$H(p) = - \sum_{x \in \mathcal{X}} p(x) \log_2(p(x))$$
    où $p(x)$ est la probabilité de l'événement $x$, et $\log_2$ est le logarithme en base 2. L'unité de l'entropie est le "bit".

2.  \textbf{Calcul de l'entropie de la distribution vraie $H(p)$}\\
    Les probabilités de la distribution vraie $p$ sont : $p(\text{aboie}) = 0.6$, $p(\text{court}) = 0.2$, $p(\text{dort}) = 0.1$, $p(\text{mange}) = 0.1$.
    $$H(p) = - [p(\text{aboie}) \log_2(p(\text{aboie})) + p(\text{court}) \log_2(p(\text{court})) + p(\text{dort}) \log_2(p(\text{dort})) + p(\text{mange}) \log_2(p(\text{mange}))]$$
    $$H(p) = - [0.6 \log_2(0.6) + 0.2 \log_2(0.2) + 0.1 \log_2(0.1) + 0.1 \log_2(0.1)]$$
    En utilisant les valeurs approximatives de $\log_2$ :
    $$H(p) = - [0.6 \times (-0.7370) + 0.2 \times (-2.3219) + 0.1 \times (-3.3219) + 0.1 \times (-3.3219)]$$
    $$H(p) = - [-0.442200 - 0.464380 - 0.332190 - 0.332190]$$
    En arrondissant chaque terme à quatre décimales avant la somme pour la clarté, nous obtenons :
    $$H(p) = - [-0.4422 - 0.4644 - 0.3322 - 0.3322]$$
    $$H(p) = - [-1.5710]$$
    $$H(p) = 1.5710 \text{ bits}$$

3.  \textbf{Interprétation de $H(p)$}\\
    La valeur $H(p) = 1.5710$ bits représente l'incertitude moyenne inhérente à la distribution $p$. C'est la quantité minimale moyenne d'information (en bits) requise pour coder ou identifier un événement (ici, le mot suivant "Le chien") si l'on connaît la vraie distribution des probabilités. Plus cette valeur est élevée, plus la distribution est "uniforme" et donc plus l'incertitude est grande quant à l'événement qui va se produire. À l'inverse, une valeur faible indique une distribution très concentrée, où certains événements sont beaucoup plus probables que d'autres, réduisant l'incertitude.

\textbf{Partie B : La Cross-Entropie}

1.  \textbf{Formule de la Cross-Entropie $H(p, q)$}\\
    La Cross-Entropie entre une distribution vraie $p$ et une distribution prédite $q$ sur le même ensemble d'événements $\mathcal{X}$ est définie par :
    $$H(p, q) = - \sum_{x \in \mathcal{X}} p(x) \log_2(q(x))$$
    où $p(x)$ est la probabilité vraie de l'événement $x$, et $q(x)$ est la probabilité prédite par le modèle pour l'événement $x$.

2.  \textbf{Calcul de la Cross-Entropie $H(p, q_1)$}\\
    Les probabilités de la distribution vraie $p$ sont : $p(\text{aboie}) = 0.6$, $p(\text{court}) = 0.2$, $p(\text{dort}) = 0.1$, $p(\text{mange}) = 0.1$.
    Les probabilités prédites par le Modèle M1 ($q_1$) sont : $q_1(\text{aboie}) = 0.4$, $q_1(\text{court}) = 0.3$, $q_1(\text{dort}) = 0.2$, $q_1(\text{mange}) = 0.1$.
    $$H(p, q_1) = - [p(\text{aboie}) \log_2(q_1(\text{aboie})) + p(\text{court}) \log_2(q_1(\text{court})) + p(\text{dort}) \log_2(q_1(\text{dort})) + p(\text{mange}) \log_2(q_1(\text{mange}))]$$
    $$H(p, q_1) = - [0.6 \log_2(0.4) + 0.2 \log_2(0.3) + 0.1 \log_2(0.2) + 0.1 \log_2(0.1)]$$
    En utilisant les valeurs approximatives de $\log_2$ :
    $$H(p, q_1) = - [0.6 \times (-1.3219) + 0.2 \times (-1.7370) + 0.1 \times (-2.3219) + 0.1 \times (-3.3219)]$$
    $$H(p, q_1) = - [-0.793140 - 0.347400 - 0.232190 - 0.332190]$$
    En arrondissant chaque terme à quatre décimales avant la somme pour la clarté, nous obtenons :
    $$H(p, q_1) = - [-0.7931 - 0.3474 - 0.2322 - 0.3322]$$
    $$H(p, q_1) = - [-1.7049]$$
    $$H(p, q_1) = 1.7049 \text{ bits}$$

3.  \textbf{Interprétation de $H(p, q_1)$}\\
    La valeur $H(p, q_1) = 1.7049$ bits représente la quantité moyenne de bits nécessaires pour identifier un événement (le mot suivant) si l'on utilise la distribution de probabilité $q_1$ du Modèle M1 pour coder ces événements, alors que la vraie distribution est $p$. C'est la longueur moyenne du code lorsque l'on utilise un code sous-optimal (basé sur $q_1$) pour des données générées par $p$. Idéalement, si $q_1$ était identique à $p$, la Cross-Entropie serait égale à l'Entropie de Shannon $H(p)$. Toute valeur supérieure à $H(p)$ indique une inefficacité due à la différence entre $p$ et $q_1$.

\textbf{Partie C : La Divergence de Kullback-Leibler}

1.  \textbf{Formule de la Divergence de Kullback-Leibler $D_{KL}(p \, || \, q)$}\\
    La Divergence de Kullback-Leibler (KL) entre deux distributions de probabilité discrètes $p$ et $q$ sur le même ensemble d'événements $\mathcal{X}$ est définie par :
    $$D_{KL}(p \, || \, q) = \sum_{x \in \mathcal{X}} p(x) \log_2\left(\frac{p(x)}{q(x)}\right)$$
    Alternativement, elle peut être exprimée comme :
    $$D_{KL}(p \, || \, q) = H(p, q) - H(p)$$

2.  \textbf{Calcul de la Divergence de Kullback-Leibler $D_{KL}(p \, || \, q_1)$}\\
    Nous allons utiliser la première formule pour le calcul direct.
    $$D_{KL}(p \, || \, q_1) = p(\text{aboie}) \log_2\left(\frac{p(\text{aboie})}{q_1(\text{aboie})}\right) + p(\text{court}) \log_2\left(\frac{p(\text{court})}{q_1(\text{court})}\right) + p(\text{dort}) \log_2\left(\frac{p(\text{dort})}{q_1(\text{dort})}\right) + p(\text{mange}) \log_2\left(\frac{p(\text{mange})}{q_1(\text{mange})}\right)$$
    Calcul des termes individuels :
    \begin{itemize}
        \item $0.6 \log_2\left(\frac{0.6}{0.4}\right) = 0.6 \log_2(1.5) \approx 0.6 \times 0.5850 = 0.3510$
        \item $0.2 \log_2\left(\frac{0.2}{0.3}\right) \approx 0.2 \log_2(0.6667) \approx 0.2 \times (-0.5850) = -0.1170$
        \item $0.1 \log_2\left(\frac{0.1}{0.2}\right) = 0.1 \log_2(0.5) = 0.1 \times (-1.0000) = -0.1000$
        \item $0.1 \log_2\left(\frac{0.1}{0.1}\right) = 0.1 \log_2(1.0) = 0.1 \times 0.0000 = 0.0000$
    \end{itemize}
    $$D_{KL}(p \, || \, q_1) = 0.3510 + (-0.1170) + (-0.1000) + 0.0000$$
    $$D_{KL}(p \, || \, q_1) = 0.1340 \text{ bits}$$

3.  \textbf{Vérification de la relation $H(p, q) = H(p) + D_{KL}(p \, || \, q)$}\\
    Nous avons calculé :
    \begin{itemize}
        \item $H(p) = 1.5710$ bits
        \item $H(p, q_1) = 1.7049$ bits
        \item $D_{KL}(p \, || \, q_1) = 0.1340$ bits
    \end{itemize}
    Vérifions la somme :
    $$H(p) + D_{KL}(p \, || \, q_1) = 1.5710 + 0.1340 = 1.7050 \text{ bits}$$
    La valeur calculée de $H(p, q_1)$ est $1.7049$ bits. La légère différence de $0.0001$ est due aux arrondis des calculs intermédiaires. La relation est donc vérifiée avec une excellente précision.

4.  \textbf{Interprétation de $D_{KL}(p \, || \, q_1)$}\\
    La valeur $D_{KL}(p \, || \, q_1) = 0.1340$ bits représente la quantité d'information supplémentaire moyenne que l'on perd (ou le "coût" additionnel) lorsque l'on utilise la distribution $q_1$ pour approximer la vraie distribution $p$. C'est une mesure de la "distance" ou de la divergence entre les deux distributions. Un $D_{KL}$ de zéro signifierait que $q_1$ est identique à $p$. Plus la valeur est élevée, plus les distributions sont différentes, et plus l'approximation est coûteuse en termes d'information. La divergence KL est asymétrique, c'est-à-dire que $D_{KL}(p \, || \, q) \neq D_{KL}(q \, || \, p)$, ce qui signifie que le "coût" d'approximer $p$ par $q$ n'est pas le même que d'approximer $q$ par $p$. Dans le contexte des modèles de langage, c'est la perte d'information due au fait que les prédictions du modèle ne correspondent pas parfaitement à la réalité.

\textbf{Partie D : \'Evaluation et Am\'elioration du Mod\`ele}

1.  \textbf{Calcul de la Cross-Entropie $H(p, q_2)$}\\
    Les probabilités de la distribution vraie $p$ sont les mêmes.
    Les probabilités prédites par le Modèle M2 ($q_2$) sont : $q_2(\text{aboie}) = 0.55$, $q_2(\text{court}) = 0.25$, $q_2(\text{dort}) = 0.1$, $q_2(\text{mange}) = 0.1$.
    $$H(p, q_2) = - [p(\text{aboie}) \log_2(q_2(\text{aboie})) + p(\text{court}) \log_2(q_2(\text{court})) + p(\text{dort}) \log_2(q_2(\text{dort})) + p(\text{mange}) \log_2(q_2(\text{mange}))]$$
    $$H(p, q_2) = - [0.6 \log_2(0.55) + 0.2 \log_2(0.25) + 0.1 \log_2(0.1) + 0.1 \log_2(0.1)]$$
    En utilisant les valeurs approximatives de $\log_2$ :
    $$H(p, q_2) = - [0.6 \times (-0.8626) + 0.2 \times (-2.0000) + 0.1 \times (-3.3219) + 0.1 \times (-3.3219)]$$
    $$H(p, q_2) = - [-0.517560 - 0.400000 - 0.332190 - 0.332190]$$
    En arrondissant chaque terme à quatre décimales avant la somme pour la clarté, nous obtenons :
    $$H(p, q_2) = - [-0.5176 - 0.4000 - 0.3322 - 0.3322]$$
    $$H(p, q_2) = - [-1.5820]$$
    $$H(p, q_2) = 1.5820 \text{ bits}$$

2.  \textbf{Calcul de la Divergence de Kullback-Leibler $D_{KL}(p \, || \, q_2)$}\\
    Nous utiliserons la relation $D_{KL}(p \, || \, q_2) = H(p, q_2) - H(p)$.
    Nous avons $H(p) = 1.5710$ bits et $H(p, q_2) = 1.5820$ bits.
    $$D_{KL}(p \, || \, q_2) = 1.5820 - 1.5710 = 0.0110 \text{ bits}$$
    (Note : Un calcul direct avec les log individuels et arrondis similaires donnerait $D_{KL}(p \, || \, q_2) \approx 0.0115$ bits. La différence est due aux cumuls d'arrondis. La méthode soustractive est souvent plus stable numériquement et cohérente ici avec nos calculs préalables.)

3.  \textbf{Comparaison des Modèles M1 et M2}\\
    Nous récapitulons les résultats dans le tableau suivant :
    \begin{tabular}{|l|c|c|}
        \hline
        \textbf{M\'etrique} & \textbf{Mod\`ele M1 ($q_1$)} & \textbf{Mod\`ele M2 ($q_2$)} \\
        \hline
        Cross-Entropie $H(p, q)$      & $1.7049$      & $1.5820$      \\
        \hline
        Divergence KL $D_{KL}(p \, || \, q)$ & $0.1340$      & $0.0110$      \\
        \hline
    \end{tabular}
    Nous observons que la Cross-Entropie de M2 ($1.5820$) est inférieure à celle de M1 ($1.7049$). De même, la Divergence KL de M2 ($0.0110$) est significativement inférieure à celle de M1 ($0.1340$).

4.  \textbf{Explication du "meilleur" modèle et rôle des métriques}\\
    Le \textbf{Modèle M2 est clairement le meilleur} des deux.
    \begin{itemize}
        \item \textbf{Cross-Entropie} : Une Cross-Entropie plus faible indique que la distribution prédite par le modèle ($q_2$) est plus proche de la distribution vraie ($p$). En d'autres termes, M2 nécessite en moyenne moins de bits pour coder les événements de la distribution vraie en utilisant son propre schéma de codage que M1, ce qui signifie que ses prédictions sont plus efficaces. M2 est plus performant car il prédit des probabilités qui sont plus fidèles à la réalité observée dans les données.
        \item \textbf{Divergence KL} : Une Divergence KL plus faible indique une "distance" plus petite entre la distribution prédite et la distribution vraie. M2 perd moins d'information en approximant $p$ que M1. Un $D_{KL}(p \, || \, q_2) = 0.0110$ est très proche de zéro, ce qui signifie que $q_2$ est une excellente approximation de $p$. C'est le coût additionnel, en termes d'information, d'utiliser $q_2$ au lieu de $p$, et ce coût est minimisé par M2.
    \end{itemize}
    Ces métriques, et en particulier la Cross-Entropie (souvent appelée "Cross-Entropy Loss" en apprentissage automatique), sont utilisées comme \textbf{fonctions de perte (loss functions)} pour entraîner les modèles de langage. L'objectif de l'entraînement est de minimiser cette fonction de perte. En minimisant la Cross-Entropie, le modèle est incité à ajuster ses paramètres de manière à ce que sa distribution de probabilité prédite $q$ se rapproche le plus possible de la distribution vraie $p$. Puisque $H(p)$ est une constante (l'entropie de la vraie distribution, qui ne dépend pas du modèle), minimiser $H(p, q)$ revient à minimiser $D_{KL}(p \, || \, q)$. L'entraînement cherche ainsi à réduire la perte d'information et à rendre les prédictions du modèle aussi fidèles que possible à la réalité statistique des données. Les résultats ci-dessus démontrent qu'en passant de M1 à M2, nous avons réussi à réduire la divergence et à améliorer la fidélité des prédictions du modèle.