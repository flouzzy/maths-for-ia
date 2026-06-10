# Exercice 10 : Bornes de généralisation pour les SVM via McDiarmid (Niveau 10)

## Énoncé
Dans le cadre de la classification linéaire par Séparateurs à Vaste Marge (SVM), on cherche à borner l'erreur de généralisation.
Soit $S = (Z_1, \dots, Z_n)$ avec $Z_i = (X_i, Y_i) \in \mathcal{X} \times \{-1, 1\}$ un échantillon i.i.d. de taille $n$.
On suppose que $\|X_i\|_2 \le R$ presque sûrement.
On considère un algorithme d'apprentissage stable $A$ qui associe à un échantillon $S$ un vecteur de poids $w_S \in \mathbb{R}^d$.
Le classifieur associé est $h_S(x) = \text{sign}(\langle w_S, x \rangle)$.
Le risque réel est $R(w_S) = \mathbb{E}_{(X, Y)}[\mathbf{1}_{Y \langle w_S, X \rangle < 0}]$ et le risque empirique régularisé (perte charnière / hinge loss) est :
$$\widehat{R}_S(w_S) = \frac{1}{n} \sum_{i=1}^n \ell(w_S, Z_i) \quad \text{où} \quad \ell(w, (x, y)) = \max(0, 1 - y \langle w, x \rangle)$$
On suppose que l'algorithme $A$ vérifie une propriété de **stabilité uniforme** : il existe une constante $\beta \ge 0$ telle que pour tout échantillon $S$, pour tout $i \in \{1, \dots, n\}$ et pour tout échantillon modifié $S^{(i)}$ où le $i$-ème point est remplacé par un point $Z'_i$ indépendant :
$$\sup_{z \in \mathcal{X} \times \{-1, 1\}} |\ell(w_S, z) - \ell(w_{S^{(i)}}, z)| \le \beta$$
1. Soit la fonction $F(S) = R(w_S) - \widehat{R}_S(w_S)$.
Montrer que $F$ satisfait la propriété des différences bornées et déterminer les constantes $c_i$ associées en fonction de $\beta$ et du fait que la perte est bornée par une constante $M > 0$.
2. Établir une borne supérieure sur la probabilité de déviation de $F(S)$ par rapport à sa moyenne $\mathbb{E}[F(S)]$.
3. Démontrer le théorème de généralisation finale : pour tout $\delta \in (0, 1)$, avec probabilité d'au moins $1 - \delta$ :
$$R(w_S) \le \widehat{R}_S(w_S) + \mathbb{E}[R(w_S) - \widehat{R}_S(w_S)] + \left( 2 n \beta + M \right) \sqrt{\frac{\ln(1/\delta)}{2 n}}$$

---

## Correction Détaillée

### 1. Propriété des différences bornées
Soient $S = (Z_1, \dots, Z_n)$ et $S^{(i)} = (Z_1, \dots, Z'_i, \dots, Z_n)$ deux échantillons ne différant que par le $i$-ème point.
Écrivons la différence $F(S) - F(S^{(i)})$ :
$$F(S) - F(S^{(i)}) = \big( R(w_S) - \widehat{R}_S(w_S) \big) - \big( R(w_{S^{(i)}}) - \widehat{R}_{S^{(i)}}(w_{S^{(i)}}) \big)$$
$$= \big( R(w_S) - R(w_{S^{(i)}}) \big) + \big( \widehat{R}_{S^{(i)}}(w_{S^{(i)}}) - \widehat{R}_S(w_S) \big)$$

Analysons chacun des deux blocs de cette somme.
- **Bloc 1 : Différence des risques réels $R(w_S) - R(w_{S^{(i)}})$.**
Par définition du risque réel comme espérance par rapport à une nouvelle observation $Z = (X, Y)$ :
$$R(w_S) - R(w_{S^{(i)}}) = \mathbb{E}_Z[\ell(w_S, Z)] - \mathbb{E}_Z[\ell(w_{S^{(i)}}, Z)] = \mathbb{E}_Z\big[ \ell(w_S, Z) - \ell(w_{S^{(i)}}, Z) \big]$$
En utilisant la définition de la stabilité uniforme :
$$R(w_S) - R(w_{S^{(i)}}) \le \mathbb{E}_Z\left[ \sup_{z} |\ell(w_S, z) - \ell(w_{S^{(i)}}, z)| \right] \le \beta$$

- **Bloc 2 : Différence des risques empiriques $\widehat{R}_{S^{(i)}}(w_{S^{(i)}}) - \widehat{R}_S(w_S)$.**
Écrivons explicitement les deux moyennes empiriques :
$$\widehat{R}_{S^{(i)}}(w_{S^{(i)}}) - \widehat{R}_S(w_S) = \frac{1}{n} \sum_{j=1}^n \ell(w_{S^{(i)}}, Z^{(i)}_j) - \frac{1}{n} \sum_{j=1}^n \ell(w_S, Z_j)$$
$$= \frac{1}{n} \Big( \ell(w_{S^{(i)}}, Z'_i) - \ell(w_S, Z_i) \Big) + \frac{1}{n} \sum_{j \neq i} \big( \ell(w_{S^{(i)}}, Z_j) - \ell(w_S, Z_j) \big)$$

Majoration du terme isolé : la perte est bornée par $M > 0$, donc :
$$\frac{1}{n} \Big( \ell(w_{S^{(i)}}, Z'_i) - \ell(w_S, Z_i) \Big) \le \frac{M}{n}$$
Majoration de la somme restante : par stabilité uniforme, chaque terme vérifie $\ell(w_{S^{(i)}}, Z_j) - \ell(w_S, Z_j) \le \beta$. Il y a $n-1$ termes dans la somme :
$$\frac{1}{n} \sum_{j \neq i} \big( \ell(w_{S^{(i)}}, Z_j) - \ell(w_S, Z_j) \big) \le \frac{n-1}{n} \beta$$
En combinant ces deux majorations, le bloc 2 vérifie :
$$\widehat{R}_{S^{(i)}}(w_{S^{(i)}}) - \widehat{R}_S(w_S) \le \frac{M}{n} + \frac{n-1}{n} \beta$$

- **Synthèse :**
En sommant les résultats obtenus pour les blocs 1 et 2, nous obtenons :
$$F(S) - F(S^{(i)}) \le \beta + \frac{M}{n} + \frac{n-1}{n} \beta = \left( 1 + \frac{n-1}{n} \right) \beta + \frac{M}{n} = \frac{2n - 1}{n} \beta + \frac{M}{n}$$
Pour simplifier et conserver une borne supérieure propre, on peut majorer grossièrement $\frac{2n-1}{n}$ par $2$. D'où :
$$F(S) - F(S^{(i)}) \le 2 \beta + \frac{M}{n}$$

Par symétrie des rôles, la même borne s'applique à $F(S^{(i)}) - F(S)$. Les constantes de McDiarmid associées à la fonction $F$ sont donc :
$$c_i = 2 \beta + \frac{M}{n} \quad \forall i \in \{1, \dots, n\}$$

### 2. Inégalité de concentration de McDiarmid
Calculons la somme des carrés des constantes :
$$\sum_{i=1}^n c_i^2 = n \left( 2 \beta + \frac{M}{n} \right)^2 = \frac{(2n \beta + M)^2}{n}$$

En appliquant le théorème de McDiarmid à la variable aléatoire $F(S)$, nous obtenons pour tout $\epsilon > 0$ :
$$\mathbb{P}\Big( F(S) - \mathbb{E}[F(S)] \ge \epsilon \Big) \le \exp\left( - \frac{2 \epsilon^2}{\sum_{i=1}^n c_i^2} \right) = \exp\left( - \frac{2 n \epsilon^2}{(2n \beta + M)^2} \right)$$

### 3. Preuve du théorème de généralisation finale
Posons le terme de droite de l'inégalité de probabilité égal à $\delta$ :
$$\exp\left( - \frac{2 n \epsilon^2}{(2n \beta + M)^2} \right) = \delta \implies - \frac{2 n \epsilon^2}{(2n \beta + M)^2} = \ln(\delta)$$
$$\epsilon^2 = \frac{(2n \beta + M)^2 \ln(1/\delta)}{2 n} \implies \epsilon = \left( 2n \beta + M \right) \sqrt{\frac{\ln(1/\delta)}{2 n}}$$

Ainsi, avec probabilité d'au moins $1 - \delta$, nous avons :
$$F(S) \le \mathbb{E}[F(S)] + \epsilon$$
$$R(w_S) - \widehat{R}_S(w_S) \le \mathbb{E}[R(w_S) - \widehat{R}_S(w_S)] + \left( 2n \beta + M \right) \sqrt{\frac{\ln(1/\delta)}{2 n}}$$

En réarrangeant les termes pour isoler le risque réel $R(w_S)$, le théorème de généralisation finale est formellement et rigoureusement démontré.
*Remarque d'excellence :* Pour les algorithmes fortement régularisés (comme les SVM avec un paramètre de régularisation $\lambda$), on peut prouver que la stabilité uniforme $\beta$ décroît en $\mathcal{O}(1/n \lambda)$. Dans ce cas, le terme $2n\beta$ est un $\mathcal{O}(1/\lambda)$, et la borne globale décroît bien en $\mathcal{O}(1/\sqrt{n})$, ce qui garantit la consistance de l'apprentissage.
