# Exercice 8 : Compacité des fonctions Hölderiennes

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit $0 < \alpha \le 1$. Une fonction $f : [0, 1] \to \mathbb{R}$ est dite $\alpha$-hölderienne de constante $C > 0$ si :
$$ \forall x, y \in [0, 1], \quad |f(x) - f(y)| \le C|x - y|^\alpha $$
Soit $\mathcal{H}_{\alpha, C}$ l'ensemble des fonctions $\alpha$-hölderiennes de constante au plus $C$, telles que $|f(0)| \le M$.
Démontrer que $\mathcal{H}_{\alpha, C}$ est une partie compacte de $(\mathcal{C}([0, 1]), \| \cdot \|_\infty)$.

## Résolution Détaillée

Un sous-ensemble d'un espace métrique est compact si et seulement s'il est fermé, et relativement compact. L'espace de départ $[0, 1]$ étant compact, nous procéderons en deux temps via le théorème d'Arzelà-Ascoli.

### 1. Relative Compacité (Arzelà-Ascoli)

Vérifions les hypothèses du théorème d'Arzelà-Ascoli pour $\mathcal{H}_{\alpha, C}$.

**Équicontinuité :**
Soit $\epsilon > 0$. Fixons $\delta = \left(\frac{\epsilon}{C}\right)^{1/\alpha} > 0$.
Pour tout $f \in \mathcal{H}_{\alpha, C}$ et pour tous $x, y \in [0, 1]$ avec $|x - y| < \delta$ :
$$ |f(x) - f(y)| \le C|x - y|^\alpha < C \left(\left(\frac{\epsilon}{C}\right)^{1/\alpha}\right)^\alpha = C \frac{\epsilon}{C} = \epsilon $$
Le module $\delta$ ne dépend ni de $x, y$ ni de la fonction $f$. La famille est donc équicontinue.

**Bornitude ponctuelle :**
Soit $x \in [0, 1]$ et $f \in \mathcal{H}_{\alpha, C}$. Appliquons la propriété de Hölder entre $0$ et $x$ :
$$ |f(x) - f(0)| \le C|x - 0|^\alpha \le C $$
(puisque $x \le 1$, $x^\alpha \le 1$).
Donc $|f(x)| \le |f(0)| + C \le M + C$.
La famille est bornée uniformément, donc ponctuellement bornée par $M+C$.
D'après le théorème d'Arzelà-Ascoli, la famille $\mathcal{H}_{\alpha, C}$ est relativement compacte.

### 2. Fermeture dans $\mathcal{C}([0, 1])$

Il reste à montrer que l'adhérence de l'ensemble ne produit aucune fonction sortant de cette classe. Montrons que $\mathcal{H}_{\alpha, C}$ est un sous-ensemble fermé pour la norme uniforme.
Soit $(f_n)$ une suite d'éléments de $\mathcal{H}_{\alpha, C}$ qui converge uniformément vers une fonction $f$.
Prenons $x, y \in [0, 1]$ quelconques fixes. Pour tout $n \in \mathbb{N}$ :
$$ |f_n(x) - f_n(y)| \le C|x - y|^\alpha $$
Passons à la limite quand $n \to \infty$. Par convergence uniforme, $f_n(x) \to f(x)$ et $f_n(y) \to f(y)$.
Les valeurs absolues étant continues, on obtient :
$$ |f(x) - f(y)| = \lim_{n\to\infty} |f_n(x) - f_n(y)| \le C|x - y|^\alpha $$
La fonction limite $f$ vérifie la propriété de Hölder.
De plus, $f_n(0) \to f(0)$. Puisque $|f_n(0)| \le M$ pour tout $n$, l'inégalité large est préservée à la limite, donc $|f(0)| \le M$.
Ainsi $f \in \mathcal{H}_{\alpha, C}$. L'ensemble est fermé.

### Conclusion

Étant un sous-ensemble fermé et relativement compact dans un espace complet, l'ensemble $\mathcal{H}_{\alpha, C}$ est un compact de $\mathcal{C}([0, 1])$. $\blacksquare$
