# Exercice 9 : Produit de variables et transformation logarithmique \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $(X_n)_{n \ge 1}$ une suite de variables aléatoires réelles I.I.D. strictement positives, admettant une espérance $\mu > 0$ et une variance $\sigma^2 > 0$. On définit $P_n = \prod_{i=1}^n X_i$.
Montrer rigoureusement que la variable aléatoire $\frac{\ln P_n - n \mathbb{E}[\ln X_1]}{\sqrt{n \text{Var}(\ln X_1)}}$ converge en loi vers une loi $\mathcal{N}(0, 1)$ (en précisant les hypothèses implicites requises).
Application : En déduire le comportement asymptotique du processus géométrique, fondamental en finance (Mouvement Brownien Géométrique discret).

**Correction :**

Considérons le logarithme du produit :
$$\ln P_n = \ln \left( \prod_{i=1}^n X_i \right) = \sum_{i=1}^n \ln X_i$$
Posons $Y_i = \ln X_i$. Puisque les $X_i$ sont I.I.D., par composition avec une fonction mesurable, les variables $Y_i$ sont également I.I.D.

Pour appliquer le Théorème Central Limite à la somme $\sum_{i=1}^n Y_i$, nous devons supposer implicitement que la variable aléatoire $Y_1$ admet un moment d'ordre deux fini. Autrement dit, il faut exiger que $\mathbb{E}[(\ln X_1)^2] < \infty$. (Avoir $\mathbb{E}[X_1]$ et $\text{Var}(X_1)$ finies n'implique pas automatiquement que $\text{Var}(\ln X_1)$ est finie si la loi de $X_1$ charge trop le voisinage de $0$).

Sous cette hypothèse indispensable, soient $m = \mathbb{E}[Y_1] = \mathbb{E}[\ln X_1]$ et $v^2 = \text{Var}(Y_1) = \text{Var}(\ln X_1)$.
Le TCL classique s'applique à la somme des $Y_i$ :
$$\frac{\sum_{i=1}^n Y_i - n m}{v \sqrt{n}} \xrightarrow{\mathcal{L}} \mathcal{N}(0, 1)$$
Ce qui est exactement l'énoncé voulu :
$$\frac{\ln P_n - n \mathbb{E}[\ln X_1]}{\sqrt{n \text{Var}(\ln X_1)}} \xrightarrow{\mathcal{L}} \mathcal{N}(0, 1)$$

Application (Mouvement Brownien Géométrique Discret) :
Dans les modèles financiers (comme le modèle de Black-Scholes discret), la valeur d'un actif au temps $n$ s'écrit $S_n = S_0 \prod_{i=1}^n X_i$, où $X_i = 1 + R_i$ est le facteur de rendement journalier.
Le théorème montre que $\ln S_n = \ln S_0 + \ln P_n$ se comporte asymptotiquement comme une variable normale, dont l'espérance est $n \mathbb{E}[\ln X_1]$ et la variance $n \text{Var}(\ln X_1)$.
Il en découle que le produit $P_n$ (et donc $S_n$) suit asymptotiquement une **loi log-normale**. Ceci justifie mathématiquement pourquoi les cours des actions sur de longues périodes sont modélisés par des distributions log-normales.
