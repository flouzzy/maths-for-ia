# Produit d'événements indépendants (Loi Log-Normale et Normales)

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

Soient $X$ et $Y$ deux variables aléatoires indépendantes suivant des lois normales centrées réduites : $X, Y \sim \mathcal{N}(0,1)$.
On pose $Z = e^X e^Y$.
Déterminer la nature exacte de la loi de $Z$.

### Correction

Soient $X, Y \sim \mathcal{N}(0,1)$ deux variables aléatoires normales standard indépendantes, et $Z = e^X e^Y$.

1. Commençons par simplifier l'expression algébrique de la variable $Z$. Par les propriétés de l'exponentielle réelle :
   $Z = e^X e^Y = e^{X+Y}$.
2. Posons la variable intermédiaire $S = X + Y$. Nous devons déterminer la loi de $S$.
3. Les variables $X$ et $Y$ sont gaussiennes et indépendantes. Un résultat fondamental de probabilités indique que la somme de deux variables gaussiennes indépendantes est elle-même une variable gaussienne.
4. Déterminons les paramètres (espérance et variance) de $S$ :
   - Par linéarité de l'espérance : $\mathbb{E}[S] = \mathbb{E}[X+Y] = \mathbb{E}[X] + \mathbb{E}[Y] = 0 + 0 = 0$.
   - Les variables étant indépendantes, l'identité de Bienaymé permet de sommer les variances : $\text{Var}(S) = \text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) = 1 + 1 = 2$.
5. On en déduit que $S \sim \mathcal{N}(0, 2)$.
6. Revenons à $Z$ : $Z = e^S$.
7. Par définition formelle, la variable aléatoire définie comme l'exponentielle d'une variable aléatoire normale suit une loi **Log-Normale**.
8. Les paramètres de cette loi log-normale sont directement les paramètres de la loi normale sous-jacente $S$.
Donc, $Z$ suit une loi Log-Normale de paramètres $\mu = 0$ et $\sigma^2 = 2$, ce que l'on note $Z \sim \mathcal{LN}(0, 2)$.
